#!/bin/bash
# 순정(영문)판 공개용 압축본을 만든다. 게임 데이터와 개인 이미지는 넣지 않는다.
# 사용: scripts/release-global.sh   (엔진/게임 빌드 뒤에 실행, 산출: out/release/cstrike-switch-global.zip)
set -e
cd "$(dirname "$0")/.."
rm -rf out/release && mkdir -p out/release
COOK_HOMEBREW_DIR=$PWD/out/release python3 ../../tools/port_register.py port.json --variant original --no-register
R=out/release/cstrike-global
rm -f $R/.cookingfoil.json $R/cstrike/default_favorites.lst  # 개인 즐겨찾기는 공개본에 넣지 않는다
mkdir -p $R/source && cp patches/*.patch $R/source/ && cp release/README-global.txt $R/README.txt
python3 - <<'PY'
import zipfile, os
R = 'out/release'
with zipfile.ZipFile(R + '/cstrike-switch-global.zip', 'w', zipfile.ZIP_DEFLATED) as zf:
    for d, _, fs in os.walk(R + '/cstrike-global'):
        for f in fs:
            p = os.path.join(d, f)
            zf.write(p, os.path.relpath(p, R))
PY
sha256sum out/release/cstrike-switch-global.zip
