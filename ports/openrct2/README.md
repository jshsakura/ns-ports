# RollerCoaster Tycoon 2 (OpenRCT2)

<!-- quick:begin -->
## 필요한 파일과 명령어

필요한 것: RCT2 설치 파일
NRO: `ports/openrct2/in/openrct2.nro`

- 원 프로젝트: https://github.com/OpenRCT2/OpenRCT2
- 스위치 포트 소스: https://github.com/Wander-Eule/OpenRCT2-Switch

```
python3 build.py check openrct2    # 빈 칸 확인
python3 build.py openrct2 --zip
```
<!-- quick:end -->

OpenRCT2 for Switch with touch and controller support, based on the Wander-Eule/OpenRCT2-Switch fork (`7d4673d8b2`, engine 0.5.4).

- `original`: the fork as it is, built without TrueType text.
- `ko`: adds `patches/korean-switch.patch`: an embedded Korean font (NanumBarunGothic, SIL OFL, `assets/`), the `ko-KR` strings,
  and Switch locale handling so the saved language is not reset. The patch applies cleanly to the pinned commit.

```
python3 build.py openrct2 --rom <your RCT2 files> --variant ko --zip
python3 build.py openrct2 --rom <your RCT2 files> --variant original --deploy <homebrew folder>
```
The build runs in a devkitPro container with ICU 78 and libzip (`scripts/Dockerfile`, `scripts/build-icu78.sh`, or `OPENRCT2_BUILDER`).
The builder files are reconstructed from the image that built the shipped NRO and have not been rebuilt from scratch.
Game data (RollerCoaster Tycoon 2) is never included. Without `in/openrct2.nro` and without `--skip-build` the NRO is built; with `--skip-build` an existing NRO is reused.
