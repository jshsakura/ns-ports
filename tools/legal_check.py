#!/usr/bin/env python3
"""공유 전 점검: git 추적 파일에 게임 데이터/바이너리/키가 섞였는지, 사설 주소가 있는지 본다. 걸리면 종료코드 1."""
import re
import subprocess
import sys

BAD_EXT = re.compile(r"\.(nro|nsp|xci|nca|o2r|pack|szs|iso|z64|n64|v64|sfc|smc|gba|nds|rom|wad|pak|bps|ips|ups|prod\.keys|keys)$", re.I)
ALLOW = re.compile(r"^(ports/[^/]+/(overlay|overlay-ko|overlay-common)/)")  # 설정/UI 조각 (직접 만든 것만 둔다)
PRIVATE = re.compile(r"\b(192\.168\.\d+\.\d+|100\.(6[4-9]|[7-9]\d|1[01]\d|12[0-7])\.\d+\.\d+|/mnt/[A-Za-z0-9_-]+|/home/[a-z0-9_-]+)\b")
import os
files = [f for f in subprocess.check_output(["git", "ls-files", "-co", "--exclude-standard"], text=True).splitlines() if os.path.exists(f)]  # 작업 폴더에 있는 것만(추적 + 새 파일)
PATCH_OK = re.compile(r"^ports/[^/]+/patches/[^/]+\.(bps|ips|ups)$")  # 차이만 담은 패치는 둔다. 원본 롬 없이는 못 쓴다
bad = [f for f in files if BAD_EXT.search(f) and not PATCH_OK.match(f)]
big = [f for f in files if os.path.getsize(f) > 5_000_000]
priv = []
for f in files:
    if f.endswith((".png", ".jpg", ".webp", ".zip")) or f == "tools/legal_check.py":
        continue
    try:
        for i, line in enumerate(open(f, encoding="utf-8"), 1):
            if PRIVATE.search(line):
                priv.append("%s:%d" % (f, i))
    except (UnicodeDecodeError, OSError):
        pass
for title, items in (("게임 데이터/바이너리 확장자", bad), ("5MB 초과 파일", big), ("사설 주소/내 경로", priv)):
    if items:
        print("[!] %s %d건" % (title, len(items)))
        print("\n".join("    " + x for x in items[:30]))
print("OK" if not (bad or big or priv) else "점검 실패")
sys.exit(1 if (bad or big or priv) else 0)
