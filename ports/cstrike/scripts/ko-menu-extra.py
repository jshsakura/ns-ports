#!/usr/bin/env python3
"""메인 메뉴 제목 그림(head_*.bmp, 460x80)과 보조 버튼 그림(btn_*.bmp, 156x78 = 3상태)을 한글로 다시 굽는다.
둘 다 메뉴 코드가 고정 크기로 늘여 그리므로 2배 해상도로 저장해도 배치는 그대로다.
사용: ko-menu-extra.py <원본 shell 폴더> <출력 폴더> <한글 TTF>"""
import os
import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HEADS = {
    'advanced': '고급', 'advoptions': '고급 옵션', 'audio': '오디오', 'config': '설정', 'controls': '조작',
    'creategame': '게임 만들기', 'custom': '사용자 게임', 'customize': '사용자 설정', 'gameopts': '옵션',
    'gamepad': '게임패드', 'gyro': '자이로스코프', 'inetgames': '인터넷 게임', 'lan': '랜 게임',
    'load': '불러오기', 'multi': '플레이 CS', 'save': '저장', 'saveload': '저장/불러오기', 'touch': '터치',
    'touch_buttons': '터치 버튼', 'touch_options': '터치 옵션', 'video': '비디오', 'vidmodes': '비디오 모드',
    'vidoptions': '비디오 옵션', 'xhair': '조준선',
}
BTNS = {
    'favorite': '즐겨찾기', 'gamepad': '게임패드', 'gyro': '자이로', 'touch': '터치', 'touch_buttons': '터치 버튼',
    'touch_editor': '편집기', 'touch_options': '터치 옵션', 'touch_reset': '초기화', 'touch_save': '저장',
    'touch_select': '선택', 'unfavorite': '즐겨찾기 해제', 'xhair': '조준선',
}
HIRES, SS = 2, 4
TEXT = np.array([140, 85, 28], float)       # 제목 글자색
GLOW = np.array([62, 0, 0], float)          # 글자 둘레의 붉은 번짐
BTN_TONES = [(181, 110, 35), (191, 90, 11), (191, 110, 1)]


def text_mask(text, ttf, size, box_w, box_h, x, y):
    """box_w x box_h 안에 글자를 그리고 0..1 마스크를 돌려준다. 너비를 넘으면 글자를 줄인다."""
    font = ImageFont.truetype(ttf, size * SS)
    w = font.getlength(text) / SS
    if w > box_w - x:
        font = ImageFont.truetype(ttf, int(size * SS * (box_w - x) / w))
    big = Image.new('L', (box_w * SS, box_h * SS), 0)
    ImageDraw.Draw(big).text((x * SS, y * SS), text, font=font, fill=255)
    return big.resize((box_w, box_h), Image.LANCZOS)


def head(text, ttf):
    W, H = 460 * HIRES, 80 * HIRES
    m = text_mask(text, ttf, 54 * HIRES, W, H, 4 * HIRES, 6 * HIRES)
    a = np.asarray(m).astype(float)[..., None] / 255
    halo = np.asarray(m.filter(ImageFilter.GaussianBlur(14 * HIRES))).astype(float)[..., None] / 255
    glow = np.clip(halo * 2.2, 0, 1) * GLOW
    return np.clip(glow * (1 - a) + TEXT * a, 0, 255).astype('uint8')


def btn(text, ttf):
    W, H = 156 * HIRES, 26 * HIRES
    out = np.zeros((H * 3, W, 3), 'uint8')
    for s, tone in enumerate(BTN_TONES):
        m = np.asarray(text_mask(text, ttf, 15 * HIRES, W, H, 4 * HIRES, 3 * HIRES)).astype(float)[..., None] / 255
        ys = np.linspace(1.0, 0.73, H)[:, None, None]
        out[s * H:(s + 1) * H] = (np.array(tone, float) * ys * m).astype('uint8')
    return out


def save_p(arr, path):
    Image.fromarray(arr).quantize(256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(path, format='BMP')


def main(src, dst, ttf):
    os.makedirs(dst, exist_ok=True)
    for k, t in HEADS.items():
        assert os.path.exists(os.path.join(src, f'head_{k}.bmp')), k
        save_p(head(t, ttf), os.path.join(dst, f'head_{k}.bmp'))
    for k, t in BTNS.items():
        assert os.path.exists(os.path.join(src, f'btn_{k}.bmp')), k
        save_p(btn(t, ttf), os.path.join(dst, f'btn_{k}.bmp'))


main(*sys.argv[1:4])
