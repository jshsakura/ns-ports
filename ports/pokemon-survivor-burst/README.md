# 포켓몬 서바이버 버스트 (Pokemon Survivor Burst)

포켓몬 서바이버 버스트 닌텐도 스위치 홈브루 포트

- 엔진: mkxp-z
- 필요한 것: 게임 데이터 리소스
- Required files: pokemon-survivor-burst.nro, mkxp.json, soundfont.sf2
- Asset folders: Audio/, Data/, Fonts/, Graphics/, Plugins/, lib/
- Features: Custom mkxp-z Ruby 3.1 runtime with NX controller & bezel fixes
- Status: Verified & 100% playable on Nintendo Switch!

## 사용
`in/pokemon-survivor-burst.nro` 에 빌드된 NRO 를 두고, 내 게임 데이터 폴더를 지정한다.
```
python3 build.py pokemon-survivor-burst --rom <게임 데이터 폴더> --zip          # 또는 --deploy <homebrew 폴더>
```
덮어쓸 설정 파일은 `overlay/` 에 있다. 게임 데이터와 NRO 는 저장소에 없다.
