# 소닉 더 헤지혹 1 (Sonic 1 2013)

소닉 1 2013 리마스터 네이티브 디컴파일 포트. 공식 한국어(Language=8) 지원

- 엔진: RSDKv4 Decomp
- 필요한 것: Data.rsdk (모바일 2013 리마스터 데이터)
- Required files: s12013.nro, Data.rsdk, settings.ini
- Localization: Language=8 (Korean official UI & localization)
- Features: 60fps 16:9 widescreen, Spin Dash, Drop Dash, Tails & Knuckles support
- Status: Verified & 100% playable on Nintendo Switch!

## 사용
`in/s12013.nro` 에 빌드된 NRO 를 두고, 내 게임 데이터 폴더를 지정한다.
```
python3 build.py sonic1 --rom <게임 데이터 폴더> --zip          # 또는 --deploy <homebrew 폴더>
```
덮어쓸 설정 파일은 `overlay/` 에 있다. 게임 데이터와 NRO 는 저장소에 없다.
