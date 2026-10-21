# 잭 2 (Jak II)

PS2 공식 한국어 음성 에셋 연동 OpenGOAL 포트

- 엔진: OpenGOAL
- 필요한 것: Jak 2 PS2 ISO (정발판)
- Required files: jak2.nro, gk.nro, data/ directory
- Audio/Subtitles: SCEK official Korean dubbing and dialog data
- Features: Native GOAL decompiled engine, 60fps, widescreen 720p/1080p
- Status: Verified & 100% playable on Nintendo Switch!

## 사용
`in/jak2.nro` 에 빌드된 NRO 를 두고, 내 게임 데이터 폴더를 지정한다.
```
python3 build.py jak2 --rom <게임 데이터 폴더> --zip          # 또는 --deploy <homebrew 폴더>
```
덮어쓸 설정 파일은 `overlay/` 에 있다. 게임 데이터와 NRO 는 저장소에 없다.
