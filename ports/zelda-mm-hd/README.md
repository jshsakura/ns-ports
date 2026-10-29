# 젤다의 전설: 무쥬라의 가면 HD (Majora's Mask)

<!-- quick:begin -->
## 필요한 파일과 명령어

필요한 것: mm.o2r, 2ship.o2r, mods/MM_Reloaded_v11.0.3_HD.o2r, 2ship2harkinian.json
NRO: `ports/zelda-mm-hd/in/zelda-mm-hd.nro`

- 스위치 포트 소스: https://github.com/2ship2harkinian/2ship2harkinian

```
python3 build.py check zelda-mm-hd    # 빈 칸 확인
python3 build.py zelda-mm-hd --zip
```
<!-- quick:end -->

2 Ship 2 Harkinian v5.0.1 (Battler Bravo) C++ 네이티브 포트 + 60FPS 와이드스크린 + MM-Reloaded v11.0.3 HD 에셋(2.95GB) 실기 배포 완료

- 엔진: 2Ship2Harkinian v5.0.1
- 필요한 것: mm.o2r, 2ship.o2r, mods/MM_Reloaded_v11.0.3_HD.o2r, 2ship2harkinian.json
- Required files: zelda-mm-hd.nro, mm.o2r, 2ship.o2r, 2ship2harkinian.json
- HD Texture Mod: mods/MM_Reloaded_v11.0.3_HD.o2r (2.95 GB)
- Title ID: 05BC5D84DDD7A000 (CookingFoil NSP Forwarder Sync)
- Features: 60FPS native, 16:9 widescreen, dual-stick 360 camera, instant boot
- Status: Verified & 100% playable on Nintendo Switch!

## 사용
`in/zelda-mm-hd.nro` 에 빌드된 NRO 를 두고, 내 게임 데이터 폴더를 지정한다.
```
python3 build.py zelda-mm-hd --rom <게임 데이터 폴더> --zip          # 또는 --deploy <homebrew 폴더>
```
덮어쓸 설정 파일은 `overlay/` 에 있다. 게임 데이터와 NRO 는 저장소에 없다.
