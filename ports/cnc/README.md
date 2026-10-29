# 커맨드 앤 컨커: 타이베리안 던 (C&C 1)

<!-- quick:begin -->
## 필요한 파일과 명령어

**1. 받아서 둘 것**

| 놓을 위치 | 무엇 | 구하는 곳 |
| :--- | :--- | :--- |
| `ports/cnc/in/vanillatd.nro` | 스위치용 NRO | https://github.com/TheAssemblyArmada/Vanilla-Conquer 의 릴리스를 받거나 직접 빌드 |
| `ports/cnc/in/data` | C&C Gold .MIX 파일 및 영상 에셋 | 내가 가진 정품 데이터 (--rom <폴더> 로 따로 줘도 된다) |
| `ports/cnc/icon.jpg` | 앱 아이콘 (256x256 JPEG) (선택) | 직접 구하거나 만든다. 없으면 NRO 에 든 아이콘을 그대로 쓴다 |

**2. 이미지**: 앱 아이콘(`icon.jpg`, 256x256 JPEG)만 쓰이고 없으면 NRO 의 기본 아이콘을 씁니다. 이미지는 저장소에 없으니 필요하면 직접 구해 위 위치에 두세요. 배너와 스크린샷은 다루지 않습니다.

**3. 확인하고 실행**

```
python3 build.py guide cnc    # 빈 칸과 구하는 곳 확인
python3 build.py cnc --rom <내 게임 데이터 폴더> --zip
```

- 스위치 포트 소스: https://github.com/TheAssemblyArmada/Vanilla-Conquer
<!-- quick:end -->

C&C 원작 엔진 복각 포트. GDI/NOD 캠페인 및 컷신 영상 지원

- 엔진: Vanilla-Conquer (TD)
- 필요한 것: C&C Gold .MIX 파일 및 영상 에셋
- Required files: vanillatd.nro, CONQUER.INI, keymap.keys, .MIX archive assets
- Campaign support: Full GDI and NOD campaigns with high quality FMV movies
- Status: Verified & 100% playable on Nintendo Switch!

## 사용
`in/vanillatd.nro` 에 빌드된 NRO 를 두고, 내 게임 데이터 폴더를 지정한다.
```
python3 build.py cnc --rom <게임 데이터 폴더> --zip          # 또는 --deploy <homebrew 폴더>
```
덮어쓸 설정 파일은 `overlay/` 에 있다. 게임 데이터와 NRO 는 저장소에 없다.
