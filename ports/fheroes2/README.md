# 히어로즈 오브 마이트 앤 매직 2 (fheroes2)

HOMM2 최신 C++ 오픈소스 리메이크 엔진. 공식 한국어 팩 지원

- 엔진: fheroes2
- 필요한 것: HOMM2 원작 게임 데이터 (HEROES2/DATA)
- Required files: fheroes2.nro, fheroes2.cfg (lang = ko)
- Asset folders: anim/, data/, files/, maps/, music/
- Features: Complete engine rewrite in modern C++, 720p widescreen, Korean font
- Status: Verified & 100% playable on Nintendo Switch!

## 사용
`in/fheroes2.nro` 에 빌드된 NRO 를 두고, 내 게임 데이터 폴더를 지정한다.
```
python3 build.py fheroes2 --rom <게임 데이터 폴더> --zip          # 또는 --deploy <homebrew 폴더>
```
덮어쓸 설정 파일은 `overlay/` 에 있다. 게임 데이터와 NRO 는 저장소에 없다.
