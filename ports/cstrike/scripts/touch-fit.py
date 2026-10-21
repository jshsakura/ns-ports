#!/usr/bin/env python3
"""터치 메뉴 문구가 버튼 칸에 들어가는지 엔진 규칙(in_touch.c Touch_DrawText)대로 계산한다.
사용: touch-fit.py <영문 원본 폴더> <번역 폴더> <TTF> [화면너비=1280]
번역본이 원본보다 줄이 늘거나 칸 아래로 넘쳐 잘리는 버튼을 출력한다."""
import re, sys, glob, os
from PIL import ImageFont
orig, tr, ttf = sys.argv[1:4]
W = float(sys.argv[4]) if len(sys.argv) > 4 else 1280.0
H = W * 9 / 16
PIX, CHARH = 16, 20                      # 베이크 크기와 charHeight(+4)
SCALE = W * float(os.environ.get("TOUCH_TEXT_H", "0.0175")) / CHARH               # Touch_TTFScale( 1 )
font = ImageFont.truetype(ttf, PIX)
def adv(ch):
    return font.getlength(ch) * SCALE / W   # 정규화 폭
LH = CHARH * SCALE / (W * 9 / 16)          # 줄 높이(정규화)
MAXM = adv('M')
pat = re.compile(r'touch_addbutton\s+"([^"]+)"\s+"#([^"]*)"\s+"[^"]*"\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)')
def lines_needed(text, x1, y1, x2, y2):
    maxx = x2 - MAXM if x2 else 1.0
    chars = list(text); i = 0; y = y1; n = 0; clipped = False
    while i < len(chars):
        x = x1
        while i < len(chars) and chars[i] not in '\n;' and x < maxx:
            x += adv(chars[i]); i += 1
        n += 1
        y += LH
        if y >= y2:
            clipped = i < len(chars)
            break
        if i < len(chars) and chars[i] in '\n;':
            i += 1
    return n, clipped
def load(d):
    out = {}
    for f in glob.glob(os.path.join(d, 'touch*/**/*.cfg'), recursive=True):
        for m in pat.finditer(open(f, encoding='utf-8', errors='replace').read()):
            out[(os.path.relpath(f, d), m.group(1))] = (m.group(2), *map(float, m.groups()[2:]))
    return out
a, b = load(orig), load(tr)
bad = 0
for k, (t, x1, y1, x2, y2) in sorted(b.items()):
    if k not in a or a[k][0] == t:
        continue
    t0 = a[k][0]
    n0, c0 = lines_needed(t0, *a[k][1:])
    n1, c1 = lines_needed(t, x1, y1, x2, y2)
    if c1 and not c0 or n1 > n0 and c1:
        bad += 1
        print(f'{k[0]} {k[1]}: "{t[:40]}" 줄 {n0}->{n1} 잘림' + (' (원문도 잘림)' if c0 else ''))
print('문제', bad, '/ 번역된 버튼', sum(1 for k in b if k in a and a[k][0] != b[k][0]))
