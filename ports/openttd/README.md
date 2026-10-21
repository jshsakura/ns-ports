# 오픈 TTD (OpenTTD)

교통망 경영 시뮬레이션 오픈소스 엔진. 한글 폰트 지원

- 엔진: OpenTTD
- 필요한 것: 오픈 그래픽/사운드 베이스셋
- Required files: openttd.nro, openttd.cfg, NanumGothic.ttf, NanumGothicBold.ttf
- Assets: baseset/, lang/ (korean.lng), timidity/ (soundfont)
- Status: Verified & 100% playable on Nintendo Switch!

## 사용
`in/openttd.nro` 에 빌드된 NRO 를 두고, 내 게임 데이터 폴더를 지정한다.
```
python3 build.py openttd --rom <게임 데이터 폴더> --zip          # 또는 --deploy <homebrew 폴더>
```
덮어쓸 설정 파일은 `overlay/` 에 있다. 게임 데이터와 NRO 는 저장소에 없다.
