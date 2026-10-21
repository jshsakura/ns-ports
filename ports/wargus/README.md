# 워크래프트 2: 배틀넷 에디션 (Warcraft 2)

워크래프트 2 캠페인, 맵, BGM 음원 연동 포트

- 엔진: Stratagus / Wargus
- 필요한 것: Warcraft II BNE CD 데이터
- Required files: wargus.nro, campaigns/, maps/, music/, scripts/, sounds/, videos/
- Campaign support: Tides of Darkness & Beyond the Dark Portal expansions
- Status: Verified & 100% playable on Nintendo Switch!

## 사용
`in/wargus.nro` 에 빌드된 NRO 를 두고, 내 게임 데이터 폴더를 지정한다.
```
python3 build.py wargus --rom <게임 데이터 폴더> --zip          # 또는 --deploy <homebrew 폴더>
```
덮어쓸 설정 파일은 `overlay/` 에 있다. 게임 데이터와 NRO 는 저장소에 없다.
