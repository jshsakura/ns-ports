#!/usr/bin/env python3
"""스위치 포트를 쇼핑몰 라이브러리에 조립하고 등록한다.

사용: register.py <프로필.json> [--variant ko|original] [--data <게임 데이터 폴더>] [--dry-run] [--no-register]

하는 일
  1) 엔진 NRO 의 이름과 아이콘 교체 (NACP / ASET)
  2) homebrew/<id>/ 에 조립: 게임 데이터(하드링크), 오버레이, 개별 파일, 즐겨찾기 목록
  3) .cookingfoil.json 매니페스트
  4) 서버 API 로 폴더 재스캔(adopt) 후 종류를 port 로 지정 (서버 재시작 없음)

설정 (위에서 아래로 우선: 명령줄 > 환경 변수 > 설정 파일 > 프로필)
  설정 파일: $NS_PORTS_CONFIG, 없으면 <저장소>/ns-ports.config.json, 없으면 ~/.config/ns-ports/config.json
    { "homebrew_dir": "...", "cook_url": "...", "token_file": "...", "variant": "ko",
      "data": { "<포트 id>": "<게임 데이터 폴더>" } }
  환경 변수
    COOK_HOMEBREW_DIR  homebrew 폴더
    COOK_URL           서버 주소. 없으면 등록 단계를 건너뛰고 안내만 한다
    COOK_API_TOKEN     관리자 화면에서 만든 자동화 토큰 (cft_...). 값은 출력하지 않는다
  토큰은 설정 파일에 직접 쓰지 않고 token_file(권한 600 권장)이 가리키는 파일에서 읽는다.

같은 크기인데 내용이 바뀐 파일은 끝에 여분을 붙여 크기를 바꾼다(쇼핑몰이 크기만 보고 넘기는 문제).
"""
import argparse, hashlib, json, os, re, shutil, struct, sys, urllib.request, urllib.error

TEXT_EXT = ('.cfg', '.txt', '.res', '.lst', '.json')
NACP_LANGS, NACP_STRIDE, NACP_NAME = 12, 0x300, 0x200


def load_config():
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for p in (os.environ.get('NS_PORTS_CONFIG'), os.path.join(here, 'ns-ports.config.json'),
              os.path.expanduser('~/.config/ns-ports/config.json')):
        if p and os.path.exists(p):
            try:
                return json.load(open(p, encoding='utf-8'))
            except ValueError as e:
                sys.exit('설정 파일을 읽지 못했습니다: %s (%s)' % (p, e))
    return {}


VARIANT_ALIASES = {'en': 'original', 'stock': 'original', 'global': 'original'}


def load_profile(path, variant=None):
    p = json.load(open(path, encoding='utf-8'))
    base = os.path.dirname(os.path.abspath(path))
    variants = p.pop('variants', None)
    if not variants:
        # 모든 포트는 원본(original)과 한국어(ko) 두 판을 가진다. overlay 는 공통, overlay-ko 는 한국어 전용.
        ov = [o for o in p.get('overlays', ['overlay']) if o != 'overlay-ko'] or ['overlay']
        variants = {'ko': {'overlays': ov + ['overlay-ko']}, 'original': {'overlays': ov}}
    variant = VARIANT_ALIASES.get(variant, variant) or next(iter(variants))
    if variant not in variants:
        sys.exit('없는 판입니다: %s (있는 것: %s)' % (variant, ', '.join(variants)))
    p.update(variants[variant])
    p['_variant'] = variant
    p['_base'] = os.path.normpath(os.path.join(base, p.get('base', '.')))
    for k in ('id', 'title', 'nro'):
        if k not in p:
            sys.exit('프로필에 %s 가 없습니다' % k)
    return p


def rel(p, path):
    return path if os.path.isabs(path) else os.path.join(p['_base'], path)


def need(p, path):
    """빌드 산출물 경로. 없으면 빌드 안내와 함께 멈춘다."""
    full = rel(p, path)
    if not os.path.exists(full):
        sys.exit('산출물이 없습니다: %s\n포트의 BUILD.md 대로 먼저 빌드하세요.' % path)
    return full


def retitle_nro(src, icon, title):
    """ASET 의 아이콘과 NACP 이름을 바꾼다(make-nro.py 와 같은 규칙)."""
    b = open(src, 'rb').read()
    i = b.find(b'ASET')
    if i < 0:
        sys.exit('NRO 에 ASET 이 없습니다: ' + src)
    off = lambda o: int.from_bytes(b[i + o:i + o + 8], 'little')
    nacp = bytearray(b[i + off(24):i + off(24) + off(32)])
    raw = title.encode('utf-8')
    if len(raw) >= NACP_NAME:
        sys.exit('이름이 너무 깁니다')
    for k in range(NACP_LANGS):
        nacp[k * NACP_STRIDE:k * NACP_STRIDE + NACP_NAME] = raw + b'\0' * (NACP_NAME - len(raw))
    jpg = open(icon, 'rb').read() if icon else b[i + off(8):i + off(8) + off(16)]  # 아이콘을 안 주면 NRO 의 것을 그대로 쓴다
    hdr = b'ASET' + struct.pack('<I', 0) + struct.pack('<QQQQQQ', 0x38, len(jpg), 0x38 + len(jpg), len(nacp), 0, 0)
    return b[:i] + hdr + jpg + bytes(nacp)


def fetch_url(entry):
    """프로필의 downloads 항목({url, sha256, dest})을 캐시로 받아 내용을 돌려준다. 저장소에는 링크만 둔다."""
    cache = os.path.join(os.path.expanduser(os.environ.get('NS_PORTS_CACHE', '~/.cache/ns-ports')), 'dl')
    os.makedirs(cache, exist_ok=True)
    key = hashlib.sha256(entry['url'].encode()).hexdigest()[:24]
    path = os.path.join(cache, key)
    if not os.path.exists(path):
        req = urllib.request.Request(entry['url'], headers={'User-Agent': 'ns-ports'})
        with urllib.request.urlopen(req, timeout=60) as r:
            open(path, 'wb').write(r.read())
    data = open(path, 'rb').read()
    want = entry.get('sha256')
    if want and hashlib.sha256(data).hexdigest() != want:
        os.remove(path)
        sys.exit('내려받은 파일의 해시가 다릅니다: ' + entry['url'])
    return data


def favorites(path, proto='49'):
    out = []
    for raw in open(path, encoding='utf-8'):
        s = raw.split('#', 1)[0].strip()
        if not s:
            continue
        if not re.fullmatch(r'[A-Za-z0-9.\-]+(:\d{1,5})?', s):
            sys.exit('즐겨찾기 주소 형식이 아닙니다: ' + s)
        out.append('"%s" "%s"\n' % (s if ':' in s else s + ':27015', proto))
    return ''.join(out).encode()


class Dest:
    def __init__(self, root, dry):
        self.root, self.dry, self.changed = root, dry, 0

    def write(self, relpath, data):
        dst = os.path.join(self.root, relpath)
        if os.path.exists(dst):
            old = open(dst, 'rb').read()
            pad = b'\n' if relpath.endswith(TEXT_EXT) else b'\0'
            if old == data or (old.startswith(data) and not old[len(data):].strip(pad)):
                return  # 같거나, 지난번에 크기를 맞추려 붙인 여분만 다르다
            if relpath.endswith('.json'):
                try:
                    if json.loads(old) == json.loads(data):
                        return
                except ValueError:
                    pass
            pad = b'\n' if relpath.endswith(TEXT_EXT) else b'\0'
            while len(data) == len(old):
                data += pad
        self.changed += 1
        print(('(예행) ' if self.dry else '') + '쓰기', relpath, len(data))
        if self.dry:
            return
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        tmp = os.path.join(os.path.dirname(dst), '.tmp-' + os.path.basename(dst))
        open(tmp, 'wb').write(data)
        os.replace(tmp, dst)

    def link_tree(self, src, skip=frozenset()):
        """게임 데이터: 이미 있으면 건너뛰고, 없으면 하드링크(다른 디스크면 복사). skip 의 경로는 연결하지 않는다."""
        n = 0
        for d, _, fs in os.walk(src):
            for f in fs:
                s = os.path.join(d, f)
                r = os.path.relpath(s, src)
                dst = os.path.join(self.root, r)
                if r in skip or os.path.exists(dst):
                    continue
                n += 1
                if self.dry:
                    continue
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                try:
                    os.link(s, dst)
                except OSError:
                    shutil.copyfile(s, dst)
        print(('(예행) ' if self.dry else '') + '게임 데이터 %d개' % n)

    def overlay(self, src, skip=()):
        for d, _, fs in os.walk(src):
            for f in fs:
                s = os.path.join(d, f)
                r = os.path.relpath(s, src)
                if r not in skip:
                    self.write(r, open(s, 'rb').read())


def kind_id(folder):
    return 'm-' + hashlib.sha256(folder.lower().encode()).hexdigest()[:12]


def api(method, path, body=None):
    url = os.environ['COOK_URL'].rstrip('/') + path
    req = urllib.request.Request(url, method=method, data=json.dumps(body).encode() if body is not None else None,
                                 headers={'Authorization': 'Bearer ' + os.environ['COOK_API_TOKEN'],
                                          'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, json.loads(r.read() or b'{}')
    except urllib.error.HTTPError as e:
        return e.code, {}


def register(folder):
    if not os.environ.get('COOK_URL') or not os.environ.get('COOK_API_TOKEN'):
        print('등록 건너뜀: COOK_URL 과 COOK_API_TOKEN 이 필요합니다. 관리자 화면에서 종류를 port 로 지정하세요.')
        return
    st, _ = api('POST', '/api/homebrew/adopt', {})
    print('폴더 재스캔', st)
    st, res = api('POST', '/api/homebrew/kind', {'id': kind_id(folder), 'kind': 'port'})
    if st == 200:
        print('종류 port 로 등록됨 (재시작 없이 반영)')
    elif st == 404:
        print('아직 목록에 없습니다. 재스캔이 끝난 뒤 다시 실행하세요.')
    else:
        print('등록 실패', st)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('profile')
    ap.add_argument('--data', help='게임 데이터 폴더(하드링크)')
    ap.add_argument('--variant', help='프로필의 변형(예: ko, original). 기본은 첫 번째')
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--no-register', action='store_true')
    a = ap.parse_args()
    cfg = load_config()
    p = load_profile(a.profile, a.variant or cfg.get('variant'))
    if not os.environ.get('COOK_URL') and cfg.get('cook_url'):
        os.environ['COOK_URL'] = cfg['cook_url']
    tf = cfg.get('token_file')
    if not os.environ.get('COOK_API_TOKEN') and tf and os.path.exists(os.path.expanduser(tf)):
        os.environ['COOK_API_TOKEN'] = open(os.path.expanduser(tf)).read().strip()
    if not a.data:
        a.data = (cfg.get('data') or {}).get(p['id'])

    hb = os.environ.get('COOK_HOMEBREW_DIR') or cfg.get('homebrew_dir') or p.get('homebrew_dir')
    if not hb:
        sys.exit('homebrew 폴더를 정하세요(COOK_HOMEBREW_DIR 또는 프로필 homebrew_dir)')
    root = os.path.join(hb, p['id'])
    d = Dest(root, a.dry_run)

    if a.data:
        skip = set()
        for ov in p.get('data_exclude_overlays', []):  # 다른 언어판이 덮어쓴 파일은 이 변형에 가져오지 않는다
            b = rel(p, ov)
            skip |= {os.path.relpath(os.path.join(r, f), b) for r, _, fs in os.walk(b) for f in fs}
        d.link_tree(a.data, skip)
    if p.get('icon_url') and not p.get('icon'):
        ic = os.path.join(os.path.expanduser('~/.cache/ns-ports'), 'icon-' + p['id'] + '.jpg')
        os.makedirs(os.path.dirname(ic), exist_ok=True)
        open(ic, 'wb').write(fetch_url({'url': p['icon_url'], 'sha256': p.get('icon_sha256')}))
        p['icon'] = ic
    nro = retitle_nro(need(p, p['nro']['src']), need(p, p['icon']) if p.get('icon') else None, p['title'])
    d.write(p['nro'].get('out', p['id'] + '.nro'), nro)
    for ov in p.get('overlays', []):
        d.overlay(rel(p, ov), set(p.get('overlay_skip', [])))
    for f in p.get('files', []):
        d.write(f['dest'], open(need(p, f['src']), 'rb').read())
    for dl in p.get('downloads', []):  # 재배포가 애매한 이미지 등은 링크만 두고 만드는 쪽 컴퓨터에서 받는다
        try:
            d.write(dl['dest'], fetch_url(dl))
        except OSError as e:
            print('받지 못해 건너뜀: %s (%s)' % (dl['dest'], e))
    fav = p.get('favorites')
    if fav and os.path.exists(rel(p, fav['file'])):
        d.write(fav['dest'], favorites(rel(p, fav['file']), str(fav.get('protocol', '49'))))
    manifest = {'nro': p['nro'].get('out', p['id'] + '.nro'), 'mode': 'folder',
                'reason': p.get('reason', ''), 'rules': [], 'excluded': []}
    d.write('.cookingfoil.json', json.dumps(manifest, ensure_ascii=False, separators=(',', ':')).encode())
    print('바뀐 파일 %d개' % d.changed)
    if not a.dry_run and not a.no_register:
        register(p['id'])


if __name__ == '__main__':
    main()
