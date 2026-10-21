# 드래곤볼 Z RPG (Dragon Ball Z RPG)

드래곤볼 Z 팬메이드 RPG 스위치 포트

- 엔진: mkxp-z
- 필요한 것: 게임 에셋
- Required files: DragonballZrpg.nro, game/DragonballZrpg.mkxpz, DragonballZrpg.opt
- Features: mkxp-z RGSS2 runtime with Switch joypad mappings
- Status: Verified & 100% playable on Nintendo Switch!

## 사용
`in/DragonballZrpg.nro` 에 빌드된 NRO 를 두고, 내 게임 데이터 폴더를 지정한다.
```
python3 build.py dragonball-z-rpg --rom <게임 데이터 폴더> --zip          # 또는 --deploy <homebrew 폴더>
```
덮어쓸 설정 파일은 `overlay/` 에 있다. 게임 데이터와 NRO 는 저장소에 없다.
