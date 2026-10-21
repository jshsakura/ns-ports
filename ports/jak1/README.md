# 잭 & 덱스터: 구세계의 유산 (Jak and Daxter)

OpenGOAL 기반 잭 & 덱스터 1 네이티브 포트. 60fps & 16:9 와이드스크린

- 엔진: OpenGOAL
- 필요한 것: Jak 1 PS2 ISO
- Required files: jak1.nro, gk.nro, data/ directory
- Features: Native GOAL decompiled engine, 60fps, 720p/1080p widescreen
- Status: Verified & 100% playable on Nintendo Switch!

## 사용
`in/jak1.nro` 에 빌드된 NRO 를 두고, 내 게임 데이터 폴더를 지정한다.
```
python3 build.py jak1 --rom <게임 데이터 폴더> --zip          # 또는 --deploy <homebrew 폴더>
```
덮어쓸 설정 파일은 `overlay/` 에 있다. 게임 데이터와 NRO 는 저장소에 없다.
