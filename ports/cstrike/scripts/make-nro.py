#!/usr/bin/env python3
"""엔진 NRO 의 ASET(아이콘, NACP)을 교체해 목록 이름과 아트웍을 정한다.
사용: make-nro.py <엔진.nro> <아이콘.jpg> <이름> <출력.nro>
NACP 이름 칸은 언어 12개, 간격 0x300, 이름 0x200 바이트(그 뒤 0x100 은 제작자)."""
import sys, struct
src, icon, name, out = sys.argv[1:5]
b = open(src, 'rb').read()
i = b.find(b'ASET')
off = lambda o: int.from_bytes(b[i+o:i+o+8], 'little')
nacp = bytearray(b[i+off(24):i+off(24)+off(32)])
raw = name.encode('utf-8')
assert len(raw) < 0x200
for k in range(12):
    nacp[k*0x300:k*0x300+0x200] = raw + b'\0' * (0x200 - len(raw))
jpg = open(icon, 'rb').read()
hdr = b'ASET' + struct.pack('<I', 0) + struct.pack('<QQQQQQ', 0x38, len(jpg), 0x38 + len(jpg), len(nacp), 0, 0)
open(out, 'wb').write(b[:i] + hdr + jpg + bytes(nacp))
