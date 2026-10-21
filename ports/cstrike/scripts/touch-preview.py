#!/usr/bin/env python3
"""터치 메뉴 cfg 를 1280x720 그림으로 미리 그린다(엔진 Touch_DrawText 규칙 근사).
사용: touch-preview.py <cstrike 폴더> <cfg 상대경로> <출력.png>"""
import re, sys, os
from PIL import Image, ImageDraw, ImageFont
root, cfg, out = sys.argv[1:4]
W, H = 1280, 720
PIX, CHARH = 16, 20
SCALE = W * 0.0175 / CHARH
font = ImageFont.truetype(os.path.join(root, 'gfx/fonts/tahoma.ttf'), round(PIX * SCALE))
LH = CHARH * SCALE
MAXM = font.getlength('M')
img = Image.new('RGBA', (W, H), (40, 60, 45, 255))
d = ImageDraw.Draw(img, 'RGBA')
pat = re.compile(r'^:?\s*touch_addbutton\s+"?([^"\s]+)"?\s+"([^"]*)"\s+"[^"]*"\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)')
for line in open(os.path.join(root, cfg), encoding='utf-8', errors='replace'):
    if line.lstrip().startswith(('//', ':')):
        continue
    m = pat.match(line.strip())
    if not m:
        continue
    name, tex, x1, y1, x2, y2, r, g, b, a = m.groups()
    x1, y1, x2, y2 = float(x1) * W, float(y1) * H, float(x2) * W, float(y2) * H
    r, g, b, a = int(r), int(g), int(b), int(a)
    if tex.startswith('#'):
        text = tex[1:]
        maxx = (x2 - MAXM) if x2 else W
        x, y = x1, y1
        for seg in text.split(';'):
            x = x1
            for ch in seg:
                if x >= maxx:
                    x = x1
                    y += LH
                d.text((x, y), ch, font=font, fill=(r, g, b, 255))
                x += font.getlength(ch)
            y += LH
            if y >= y2:
                break
    elif tex.startswith('*'):
        d.rectangle([x1, y1, x2, y2], fill=(r, g, b, a))
        if tex == '*white':
            d.rectangle([x1, y1, x2, y2], outline=(255, 174, 0, 200))
    else:
        d.rectangle([x1, y1, x2, y2], outline=(r, g, b, 120))
img.convert('RGB').save(out)
