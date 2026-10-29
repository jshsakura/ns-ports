# 잭 3 (Jak 3)

<!-- quick:begin -->
## 필요한 파일과 명령어

필요한 것: Jak 3 PS2 ISO (정발판)
NRO: `ports/jak3/in/jak3.nro`

- 스위치 포트 소스: https://github.com/fildicio/jak-project-switch

```
python3 build.py check jak3    # 빈 칸 확인
python3 build.py jak3 --zip
```
<!-- quick:end -->

PS2 공식 한국어 더빙/자막 연동 OpenGOAL 포트

- 엔진: OpenGOAL
- 필요한 것: Jak 3 PS2 ISO (정발판)
- Required files: jak3.nro, gk.nro, data/ directory
- Audio/Subtitles: SCEK official Korean dubbing and dialog data
- Features: Native GOAL decompiled engine, 60fps, widescreen 720p/1080p
- Status: Verified & 100% playable on Nintendo Switch!

## 사용
`in/jak3.nro` 에 빌드된 NRO 를 두고, 내 게임 데이터 폴더를 지정한다.
```
python3 build.py jak3 --rom <게임 데이터 폴더> --zip          # 또는 --deploy <homebrew 폴더>
```
덮어쓸 설정 파일은 `overlay/` 에 있다. 게임 데이터와 NRO 는 저장소에 없다.
