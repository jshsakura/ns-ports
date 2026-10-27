#!/usr/bin/env python3
"""단테스 인페르노 한글패치를 리눅스에서 적용한다.

Windows 용 DantesInferno_Switch_KR_v1.0.cmd 에 들어 있는 패치 데이터(번역 리소스)를 읽어,
영문 원본 game 폴더를 건드리지 않고 한글판 사본을 만든다. 번역 데이터는 이 저장소에 없고
사용자가 가진 .cmd 안에서만 읽는다.

사용: dante_kr_patch.py --cmd <패치.cmd> --game <영문 game 폴더> --out <한글판 game 폴더>

패치 형식: 원본 뒤에 새 구간을 덧붙이고 맨 앞 머리말(파일 테이블)만 바꾼다.
  구간은 연산 목록이다 (0=원본에서 복사, 1=삽입, 2=0 채우기).
원본과 결과는 모두 SHA-256 으로 검증한다. 어긋나면 아무것도 남기지 않고 멈춘다.
"""
import argparse, base64, gzip, hashlib, io, os, shutil, struct, sys

MARK = '###KRDATA###'
CHUNK = 1 << 22


def die(msg):
    sys.exit('[오류] ' + msg)


def load_specs(cmd_path):
    text = open(cmd_path, encoding='utf-8', errors='replace').read()
    i = text.find(MARK)
    if i < 0:
        die('패치 데이터를 찾지 못했습니다: ' + cmd_path)
    raw = gzip.decompress(base64.b64decode(''.join(text[i + len(MARK):].split())))
    r = io.BytesIO(raw)

    def take(fmt):
        return struct.unpack('<' + fmt, r.read(struct.calcsize('<' + fmt)))[0]

    if r.read(8) != b'DIKRPAT1':
        die('지원하지 않는 패치 데이터입니다')
    specs = []
    for _ in range(take('i')):
        s = {'index': take('B'), 'orig_size': take('q'), 'orig_sha': r.read(32).hex()}
        s['new_hdr'] = r.read(take('i'))
        s['new_size'] = take('q')
        s['tail_sha'] = r.read(32).hex()
        ops = []
        for _ in range(take('i')):
            t = take('B')
            if t == 0:
                ops.append((0, take('q'), take('q')))
            elif t == 1:
                ops.append((1, r.read(take('i')), None))
            elif t == 2:
                ops.append((2, take('q'), None))
            else:
                die('알 수 없는 연산입니다')
        s['ops'] = ops
        specs.append(s)
    return specs


def file_sha(path, limit):
    h, left = hashlib.sha256(), limit
    with open(path, 'rb') as f:
        while left > 0:
            b = f.read(min(CHUNK, left))
            if not b:
                die('파일이 짧습니다: ' + path)
            h.update(b)
            left -= len(b)
    return h.hexdigest()


def patch_one(src, dst, s):
    if os.path.getsize(src) != s['orig_size']:
        die('%s: 지원하는 원본이 아닙니다 (크기 %d, 필요 %d)' % (os.path.basename(src), os.path.getsize(src), s['orig_size']))
    print('  원본 확인 중 (SHA-256)...', flush=True)
    got = file_sha(src, s['orig_size'])
    if got != s['orig_sha']:
        die('%s: 지원하는 원본이 아닙니다 (SHA-256 불일치)' % os.path.basename(src))
    part = dst + '.part'
    try:
        shutil.copyfile(src, part)
        tail = hashlib.sha256()
        with open(src, 'rb') as rd, open(part, 'r+b') as wr:
            wr.seek(s['orig_size'])
            for kind, a, n in s['ops']:
                if kind == 0:
                    if a < 0 or a + n > s['orig_size']:
                        die('복사 범위가 원본을 벗어납니다')
                    rd.seek(a)
                    left = n
                    while left > 0:
                        b = rd.read(min(CHUNK, left))
                        wr.write(b); tail.update(b); left -= len(b)
                elif kind == 1:
                    wr.write(a); tail.update(a)
                else:
                    left = a
                    while left > 0:
                        b = bytes(min(CHUNK, left))
                        wr.write(b); tail.update(b); left -= len(b)
            if wr.tell() != s['new_size']:
                die('결과 크기가 맞지 않습니다')
            if tail.hexdigest() != s['tail_sha']:
                die('결과 SHA-256 이 맞지 않습니다')
            wr.seek(0)
            wr.write(s['new_hdr'])
        os.replace(part, dst)
    finally:
        if os.path.exists(part):
            os.remove(part)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--cmd', required=True, help='DantesInferno_Switch_KR_v1.0.cmd')
    ap.add_argument('--game', required=True, help='영문 원본 game 폴더 (bigfile0.viv, bigfile1.viv ...)')
    ap.add_argument('--out', required=True, help='한글판 game 폴더 (새로 만든다)')
    a = ap.parse_args()
    specs = load_specs(a.cmd)
    if os.path.abspath(a.game) == os.path.abspath(a.out):
        die('--out 은 원본과 다른 폴더여야 합니다')
    os.makedirs(a.out, exist_ok=True)
    patched = {'bigfile%d.viv' % s['index'] for s in specs}
    for name in sorted(os.listdir(a.game)):
        if name in patched:
            continue
        s, d = os.path.join(a.game, name), os.path.join(a.out, name)
        if os.path.isfile(s) and not os.path.exists(d):
            try:
                os.link(s, d)
            except OSError:
                shutil.copyfile(s, d)
    for s in specs:
        name = 'bigfile%d.viv' % s['index']
        print('패치 중:', name, flush=True)
        patch_one(os.path.join(a.game, name), os.path.join(a.out, name), s)
        print('  완료 (%d 바이트)' % os.path.getsize(os.path.join(a.out, name)), flush=True)
    print('한글판 game 폴더:', a.out)


if __name__ == '__main__':
    main()
