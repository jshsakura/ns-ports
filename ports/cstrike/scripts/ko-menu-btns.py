#!/usr/bin/env python3
"""메인 메뉴 버튼 그림(btns_main.bmp)의 영문 글자를 한글로 다시 굽는다.
시트는 156x26 칸이 라벨 하나당 3칸(평상시, 강조, 눌림)씩 이어진다.
사용: ko-menu-btns.py <원본 btns_main.bmp> <출력 bmp> <한글 TTF>"""
import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont

LABELS = ['', '계속하기', '훈련', '설정', '불러오기', '저장/불러오기', 'HL 안내서', '종료', '플레이 CS',
          '쉬움', '보통', '어려움', '저장하기', '불러오기', '취소', '옵션', '비디오', '오디오', '조작', '완료',
          '빠른 시작', '기본값', '확인', '옵션', '모드', '고급', '', '삭제', '온라인 플레이', '채팅방',
          '랜 플레이', '사용자 설정', '건너뛰기', '나가기', '접속', '새로고침', '필터', '필터', '만들기',
          '만들기', '채팅', '목록', '검색', '서버', '참가', '찾기', '만들기', '게임 참가', '검색', '게임 찾기',
          '게임 시작', '서버 정보', '업데이트', 'IP 추가', '접속 끊기', '콘솔', 'HL/CS 잠금', 'HL 업데이트',
          'CS.Net 방문', 'CS 설명서', '고급', '3D 정보', '모드 보기', '불러오기', '설치', '사이트 방문',
          '새로고침', 'CS 해제', '고급', '게임 보기', '게임 보기']
HIRES = 2  # 원본 156x26 의 배수. 메뉴 코드가 가로 156 단위로 배율을 알아본다
CELL_H, CELL_W = 26 * HIRES, 156 * HIRES
# 원본 세 상태의 글자색(위에서 아래로 밝아지는 주황). 평상시, 강조, 눌림
TONES = [((247, 150, 48), (181, 110, 35)), ((247, 134, 16), (192, 91, 11)), ((247, 164, 1), (192, 111, 1))]
SS = 4

def render(text, font, tone):
    """칸 하나의 밝기(0..255)를 돌려준다. 색은 상태별 팔레트가 입힌다."""
    big = Image.new('L', (CELL_W * SS, CELL_H * SS), 0)
    d = ImageDraw.Draw(big)
    d.text((4 * HIRES * SS, 3 * HIRES * SS), text, font=font, fill=255)
    mask = np.asarray(big.resize((CELL_W, CELL_H), Image.LANCZOS)).astype(float) / 255
    # 위쪽이 밝고 아래로 어두워지는 원본의 그라데이션
    ys = np.linspace(1.0, 0.73, CELL_H)[:, None]
    return (mask * ys * 255).astype('uint8')

def main(src, dst, ttf):
    sheet = Image.open(src)
    n = sheet.height // 26
    assert n == len(LABELS) * 3, (n, len(LABELS))
    font = ImageFont.truetype(ttf, 15 * HIRES * SS)
    out = np.zeros((sheet.height * HIRES, CELL_W), 'uint8')
    for i, text in enumerate(LABELS):
        for s in range(3):
            y = (i * 3 + s) * CELL_H
            if text:
                out[y:y + CELL_H] = render(text, font, TONES[s])
    # 밝기 값 하나가 곧 팔레트 번호다. 세 상태의 색 차이가 작아서 주황 하나로 통일한다.
    base = np.array(TONES[0][0], float)
    pal = (np.arange(256)[:, None] / 255.0 * base).astype('uint8').flatten().tolist()
    img = Image.fromarray(out, 'P')
    img.putpalette(pal)
    img.save(dst, format='BMP')

main(*sys.argv[1:4])
