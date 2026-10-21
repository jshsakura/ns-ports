#!/usr/bin/env python3
"""터치 메뉴 cfg 의 영문 문구를 공식 한글 사전(cstrike_koreana.txt)의 한글로 바꾼다.
사용: ko-touch.py <원본 touch 폴더들이 든 cstrike 폴더> <출력 cstrike 폴더> [--report]
원본은 건드리지 않고 출력 폴더에 같은 구조로 쓴다. 사전에 없는 문구는 보고만 한다."""
import re, sys, glob, os

def load(p):
    s = open(p, 'rb').read().decode('utf-16')
    return {m.group(1): m.group(2) for m in re.finditer(r'"([^"]+)"\s*"((?:[^"\\]|\\.)*)"', s)}

def norm(t):
    t = t.replace('&', '').replace('\\n', ' ').replace(';', ' ')
    return re.sub(r'\s+', ' ', t).strip().upper()

COUNTRIES = {
    'GERMANY': '독일', 'AUSTRIA': '오스트리아', 'BELGIUM': '벨기에', 'ITALY': '이탈리아', 'ISRAEL': '이스라엘',
    'SWITZERLAND': '스위스', 'SWITZERLAND/GERMANY': '스위스/독일', 'UNITED STATES OF AMERICA': '미국',
    'UNITED KINGDOM': '영국', 'FRANCE': '프랑스', 'RUSSIA': '러시아', 'CZECH REPUBLIC': '체코', 'CANADA': '캐나다',
    'SOUTH AFRICA': '남아프리카', 'JAPAN': '일본', 'SWEDEN': '스웨덴', 'BRAZIL': '브라질', 'SPAIN': '스페인',
}
FIXED = {
    'N/A': '없음', 'BUY THE ITEM': '아이템 구입', 'CHOOSE A CLASS': '클래스 선택',
    'AUTO-SELECT': '자동 선택', 'CONFIRM THE SELECTION': '선택 확인',
    'PRICE': '가격', 'RATE OF FIRE': '연사 속도', 'PROJECTILE WEIGHT': '탄두 무게', 'MUZZLE VELOCITY': '탄속',
    'MUZZLE ENERGY': '탄 에너지', 'COUNTRY OF ORIGIN': '생산국', 'CLIP CAPACITY': '탄창 용량', 'CALIBER': '구경',
    'WEIGHT (LOADED)': '무게 (장전)', 'WEIGHT (EMPTY)': '무게 (빈 탄창)',
}
UNITS = [(r'(\d[\d.]*)\s*GRAMS/PELLET', r'\1 g/알'), (r'(\d[\d.]*)\s*GRAMS', r'\1 g'),
         (r'(\d[\d.]*)\s*ROUNDS', r'\1발'), (r'(\d[\d.]*)\s*FEET/SECOND', r'\1 ft/s'),
         (r'(\d[\d.]*)\s*JOULES', r'\1 J')]

def rules(body):
    tail = '\\' if body.rstrip().endswith('\\') else ''
    n = norm(body.rstrip('\\ '))
    for k, v in MANUAL:
        if n.startswith(k):
            return v + tail
    key = body.strip().upper()
    if key in FIXED:
        return FIXED[key]
    if key in COUNTRIES:
        return COUNTRIES[key]
    if key.startswith('YOU HAVE ') and '$' in key:
        return '보유 금액 ' + body.strip()[len('YOU HAVE '):]
    if ';' in key:
        parts = [FIXED.get(x.strip()) for x in key.split(';')]
        if all(parts):
            return ';'.join(parts)
    for pat, rep in UNITS:
        if re.fullmatch(pat, key):
            return re.sub(pat, rep, key)
    return None

# 사전에 없는 문구(맵 시나리오 설명, 일부 팀 소개, 메뉴 단어). 키는 영문 앞부분이고 norm() 후 startswith 로 맞춘다. 줄바꿈은 ';'.
MANUAL = [
    ('VIP Assassination scenario', 'VIP 암살 시나리오'),
    ('Terrorists:;The Terrorists must eliminate the VIP', '테러리스트:;VIP가 탈출 지점에 도착하기 전에 제거해야 합니다.'),
    ('Counter-Terrorists:;Escort the VIP', '대테러부대:;길을 막는 테러리스트를 제거하며 VIP를 탈출 지점까지 호위해야 합니다.'),
    ('Hostage Rescue and Bomb Plant/Defuse scenario', '인질 구출 및 폭탄 설치/해체 시나리오'),
    ('Hostage Rescue scenario', '인질 구출 시나리오'),
    ('Terrorists:;Prevent hostages', '테러리스트:;대테러부대가 인질을 구출하지 못하게 막아야 합니다.'),
    ('Counter-Terrorists:;Escort the hostages', '대테러부대:;인질을 구출 지점까지 호위해야 합니다.'),
    ('Bomb Plant/Defuse scenario', '폭탄 설치/해체 시나리오'),
    ('Terrorists:;A terrorist carrying C4', '테러리스트:;C4를 든 테러리스트가 목표물 중 하나를 폭파해야 합니다.'),
    ('Counter-Terrorists:;Prevent Terrorists from blowing', '대테러부대:;테러리스트가 목표물을 폭파하지 못하게 막아야 합니다.'),
    ('Terrorist Escape scenario', '테러리스트 탈출 시나리오'),
    ('Terrorists:;Find places with equipment', '테러리스트:;탈출하는 동안 장비가 있는 곳을 찾아 방어에 활용해야 합니다.'),
    ('Counter-Terrorists:;Do not let the Terrorists escape', '대테러부대:;테러리스트가 탈출하지 못하게 막아야 합니다.'),
    ('Terrorists:;Destroy one of the payloads', '테러리스트:;목표물 중 하나를 파괴하고 대테러부대가 인질을 구출하지 못하게 해야 합니다.'),
    ('Counter-Terrorists:;Rescue the hostages and prevent', '대테러부대:;인질을 구출하고 테러리스트가 목표물을 폭파하지 못하게 막아야 합니다.'),
    ('Fight Yard scenario', '난투장 시나리오'),
    ('Pick up weapons from the ground', '바닥의 무기를 줍거나 구매 구역에서 구매해 서로 싸우십시오.'),
    ('Grenade Wars scenario', '수류탄 전쟁 시나리오'),
    ('You have to blow each other up', '고폭 수류탄으로 서로를 날려 버리십시오.'),
    ('Sniper Wars scenario', '저격 전쟁 시나리오'),
    ('You have to kill enemies with a sniper rifle', '저격총으로 적을 처치하십시오.'),
    ('Knife Arena scenario', '칼싸움 경기장 시나리오'),
    ('You have to kill enemies with a knife', '칼로 적을 처치하십시오.'),
    ('1 Health Point scenario', '체력 1 시나리오'),
    ('You need to kill enemies with a knife with one health point', '체력 1로 칼을 사용해 적을 처치해야 합니다.'),
    ('35 Health Points scenario', '체력 35 시나리오'),
    ('You need to kill enemies with a knife with 35', '체력 35로 칼을 사용해 적을 처치해야 합니다.'),
    ('Aim Training scenario', '에임 연습 시나리오'),
    ('On this map, you can train', '이 맵에서는 특정 무기로 에임을 연습할 수 있습니다.'),
    ('Deathmatch scenario', '데스매치 시나리오'),
    ('The objective is simple', '목표는 간단합니다. 서로 죽이십시오.;추가 임무는 없습니다.'),
    ('The map scenario is undefined', '맵 시나리오가 정해져 있지 않습니다.'),
    ("France's elite Counter-Terrorist unit", '프랑스의 엘리트 대테러 부대 GIGN 은 대규모 테러 사건에;결정적으로 대응하는 신속 대응 부대로 만들어졌습니다.;100명 이하로 구성된 GIGN 은 그 명성을 쌓아 왔습니다.'),
    ('The primary missions of the Russian SPETSNAZ', '러시아 스페츠나츠의 주요 임무는 다음과 같습니다.;주요 경제·군사 시설의 정보 수집과 파괴 또는 무력화,;파괴 공작과 전복 활동 조직,'),
    ('carrying out punitive operations', ';;;;반란군에 대한 응징 작전 수행, 반군 부대 편성과 훈련 등.'),
    ('DM  | SELECT WEAPON', 'DM | 무기 선택'),
    ('PRIMARY AMMO', '주무기 탄약'), ('SECONDARY AMMO', '보조무기 탄약'),
    ('RADIO', '무전'), ('CHAT', '채팅'), ('EXIT', '나가기'), ('CLOSE', '닫기'),
    ('BECOME VIP', 'VIP 되기'), ('SHOW SCOREBOARD', '점수판 보기'), ('HIDE SCOREBOARD', '점수판 숨기기'),
]
MANUAL = [(norm(k), v) for k, v in MANUAL]

def build_map(res):
    d = load(res)
    out = {}
    for k, v in d.items():
        if k.startswith('[english]'):
            ko = d.get(k[len('[english]'):])
            if ko and re.search('[가-힣]', ko) and norm(v):
                out.setdefault(norm(v), ko.replace('&', ''))
    return out

if __name__ == '__main__':
    src, dst = sys.argv[1:3]
    dic = sys.argv[3] if len(sys.argv) > 3 and not sys.argv[3].startswith('--') else os.path.join(src, 'resource/cstrike_koreana.txt')
    mp = build_map(dic)
    miss = {}
    pat = re.compile(r'"#([^"]*)"')
    for f in glob.glob(os.path.join(src, 'touch*/**/*.cfg'), recursive=True) + []:
        text = open(f, encoding='utf-8', errors='surrogateescape').read()
        def sub(m):
            lab = m.group(1)
            whole = rules(lab)
            if whole and re.match(r'\d', lab) and any(norm(lab).startswith(k) for k, _ in MANUAL):
                return '"#' + whole + '"'
            lead = re.match(r'^(\d+ |: |# |  )?', lab).group(0)
            body = lab[len(lead):]
            if not body.strip() or body.startswith('$') or body.startswith('\\$'):
                return m.group(0)
            ko = mp.get(norm(body)) or rules(body)
            if ko:
                return '"#' + lead + ko.replace('\\n', ';') + '"'
            miss[lab] = miss.get(lab, 0) + 1
            return m.group(0)
        new = pat.sub(sub, text)
        o = os.path.join(dst, os.path.relpath(f, src))
        os.makedirs(os.path.dirname(o), exist_ok=True)
        open(o, 'w', encoding='utf-8', errors='surrogateescape').write(new)
    for k, n in sorted(miss.items(), key=lambda x: -x[1]):
        print(n, k)
