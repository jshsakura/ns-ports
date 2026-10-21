# 워크래프트 1: 오크와 인간 (Warcraft: Orcs & Humans)

워크래프트 1 원작 에셋 기반 Stratagus 엔진 포트

- 엔진: Stratagus / War1gus
- 필요한 것: DATA.WAR 등 DOS/Mac 원작 데이터
- Required files: war1gus.nro, DATA.WAR, CAVE*.WAR, HMAP*.WAR, OMAP*.WAR
- Assets: campaigns/, graphics/, maps/, music/, scripts/, sounds/, videos/
- Features: Stratagus RTS modern engine, widescreen 720p, touch & gamepad controls
- Status: Verified & 100% playable on Nintendo Switch!

## 사용
`in/war1gus.nro` 에 빌드된 NRO 를 두고, 내 게임 데이터 폴더를 지정한다.
```
python3 build.py war1gus --rom <게임 데이터 폴더> --zip          # 또는 --deploy <homebrew 폴더>
```
덮어쓸 설정 파일은 `overlay/` 에 있다. 게임 데이터와 NRO 는 저장소에 없다.
