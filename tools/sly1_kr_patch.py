#!/usr/bin/env python3
"""ProjectCane.nro 가 슬라이 쿠퍼 1 한국판(SCKA_200.04) ISO 를 받게 판별 문자열을 바꾼다.

업스트림 설치기는 ISO 루트에서 미국판 실행파일 이름(SCUS_971.98)을 찾고, 실행파일 안의
테이블(LEVELINFO, 사운드뱅크, 해설)을 고정 오프셋으로 읽는다. 한국판 실행파일은 같은 오프셋에
같은 구조의 테이블이 있어서, 이름만 같은 길이의 한국판 이름으로 바꿔도 미국판 경로가 그대로 돈다.
그래서 이 도구는 미국판 이름 세 곳만 바꾸고 나머지 바이트는 건드리지 않는다. 미국판 ISO 는 더 받지 않는다.

사용: sly1_kr_patch.py <ProjectCane.nro> <출력 NRO>
"""
import os, sys

UPSTREAM_SIZE = 25694037  # 업스트림 0.5.0 의 ProjectCane.nro
SWAPS = [
    (b'SCUS-971.98', b'SCKA-200.04'),
    (b'SCUS_971.98;1', b'SCKA_200.04;1'),
    (b'SCUS_971.98', b'SCKA_200.04'),
]


def patch(data):
    if len(data) != UPSTREAM_SIZE:
        sys.exit('[오류] 지원하는 ProjectCane 0.5.0 이 아닙니다 (크기 %d)' % len(data))
    out = bytearray(data)
    for old, new in SWAPS:
        assert len(old) == len(new)
        at = bytes(out).find(old)
        if at < 0:
            sys.exit('[오류] 판별 문자열을 찾지 못했습니다: ' + old.decode())
        out[at:at + len(old)] = new
    return bytes(out)


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    src, dst = sys.argv[1:]
    if os.path.abspath(src) == os.path.abspath(dst):
        sys.exit('[오류] 출력은 입력과 다른 파일이어야 합니다')
    out = patch(open(src, 'rb').read())
    tmp = dst + '.part'
    open(tmp, 'wb').write(out)
    os.replace(tmp, dst)
    print('완료:', dst)


if __name__ == '__main__':
    main()
