#!/usr/bin/env bash
# 단위 테스트와 공유 전 점검(게임 데이터·개인 경로가 섞였는지)을 함께 돌린다. 하나라도 실패하면 1 로 끝난다.
set -euo pipefail
cd "$(dirname "$0")/.."
python3 -m unittest discover -s tests
python3 tools/legal_check.py
