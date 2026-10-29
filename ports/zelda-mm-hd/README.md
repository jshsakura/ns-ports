# 젤다의 전설: 무쥬라의 가면 HD (Majora's Mask)

<!-- quick:begin -->
## 필요한 파일과 명령어

**1. 받아서 둘 것**

| 놓을 위치 | 무엇 | 구하는 곳 |
| :--- | :--- | :--- |
| `ports/zelda-mm-hd/in/zelda-mm-hd.nro` | 스위치용 NRO | https://github.com/2ship2harkinian/2ship2harkinian 의 릴리스를 받거나 직접 빌드 |
| `ports/zelda-mm-hd/in/data` | mm.o2r, 2ship.o2r, mods/MM_Reloaded_v11.0.3_HD.o2r, 2ship2harkinian.json | 내가 가진 정품 데이터 (--rom <폴더> 로 따로 줘도 된다) |
| `ports/zelda-mm-hd/icon.jpg` | 앱 아이콘 (256x256 JPEG) (선택) | 직접 구하거나 만든다. 없으면 NRO 에 든 아이콘을 그대로 쓴다 |

**2. 이미지**: 앱 아이콘(`icon.jpg`, 256x256 JPEG)만 쓰이고 없으면 NRO 의 기본 아이콘을 씁니다. 이미지는 저장소에 없으니 필요하면 직접 구해 위 위치에 두세요. 배너와 스크린샷은 다루지 않습니다.

**3. 확인하고 실행**

```
python3 build.py guide zelda-mm-hd    # 빈 칸과 구하는 곳 확인
python3 build.py zelda-mm-hd --zip
```

- 스위치 포트 소스: https://github.com/2ship2harkinian/2ship2harkinian
<!-- quick:end -->

2 Ship 2 Harkinian v5.0.1 (Battler Bravo) C++ 네이티브 포트 + 60FPS 와이드스크린 + MM-Reloaded v11.0.3 HD 에셋(2.95GB) 실기 배포 완료

- 엔진: 2Ship2Harkinian v5.0.1
- 필요한 것: mm.o2r, 2ship.o2r, mods/MM_Reloaded_v11.0.3_HD.o2r, 2ship2harkinian.json
- Required files: zelda-mm-hd.nro, mm.o2r, 2ship.o2r, 2ship2harkinian.json
- HD Texture Mod: mods/MM_Reloaded_v11.0.3_HD.o2r (2.95 GB)
- Title ID: 05BC5D84DDD7A000
- Features: 60FPS native, 16:9 widescreen, dual-stick 360 camera, instant boot
- Status: Verified & 100% playable on Nintendo Switch!

## 사용
`in/zelda-mm-hd.nro` 에 빌드된 NRO 를 두고, 내 게임 데이터 폴더를 지정한다.
```
python3 build.py zelda-mm-hd --rom <게임 데이터 폴더> --zip          # 또는 --deploy <homebrew 폴더>
```
덮어쓸 설정 파일은 `overlay/` 에 있다. 게임 데이터와 NRO 는 저장소에 없다.
