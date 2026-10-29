# 울펜슈타인 3D (Wolfenstein 3D)

<!-- quick:begin -->
## 필요한 파일과 명령어

**1. 받아서 둘 것**

| 놓을 위치 | 무엇 | 구하는 곳 |
| :--- | :--- | :--- |
| `ports/wolf3d/in/Wolf4SDL.nro` | 스위치용 NRO (선택) | 안 둬도 된다. 없으면 Thorhax/Wolf4SDL-NX-Modern 릴리스 v2.2-nx 에서 자동으로 받는다 |
| `ports/wolf3d/in/data` | 울펜슈타인 3D 정품 게임 데이터 | 내가 가진 정품 데이터 (--rom <폴더> 로 따로 줘도 된다) |
| `ports/wolf3d/icon.jpg` | 앱 아이콘 (256x256 JPEG) (선택) | 직접 구하거나 만든다. 없으면 NRO 에 든 아이콘을 그대로 쓴다 |

**2. 이미지**: 앱 아이콘(`icon.jpg`, 256x256 JPEG)만 쓰이고 없으면 NRO 의 기본 아이콘을 씁니다. 이미지는 저장소에 없으니 필요하면 직접 구해 위 위치에 두세요. 배너와 스크린샷은 다루지 않습니다.

**3. 확인하고 실행**

```
python3 build.py guide wolf3d    # 빈 칸과 구하는 곳 확인
python3 build.py wolf3d --rom <내 게임 데이터 폴더> --zip
```

NRO 는 구하지 않아도 됩니다. `in/` 에 없으면 Thorhax/Wolf4SDL-NX-Modern 릴리스 v2.2-nx 에서 받아 sha256 을 확인하고 씁니다.

- 스위치 포트 소스: https://github.com/Thorhax/Wolf4SDL-NX-Modern
<!-- quick:end -->

울펜슈타인 3D (Wolfenstein 3D) 스위치 포트입니다. 원 포트의 릴리스 v2.2-nx 를 그대로 쓰며 한글화는 아직 하지 않았습니다. 실기에서 확인하지 않았습니다.

- 필요한 것: 울펜슈타인 3D 정품 게임 데이터
