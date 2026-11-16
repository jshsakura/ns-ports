# 철권 3 Expanded (Tekken 3 Expanded)

<!-- quick:begin -->
## 필요한 파일과 명령어

**1. 받아서 둘 것**

| 놓을 위치 | 무엇 | 구하는 곳 |
| :--- | :--- | :--- |
| `ports/tekken3e/in/tekken3e.nro` | 스위치용 NRO | 직접 빌드한 NRO |
| `ports/tekken3e/in/data` | game.toml, switch.ini 와 게임 데이터 (같은 폴더) | 내가 가진 정품 데이터 (--rom <폴더> 로 따로 줘도 된다) |
| `ports/tekken3e/icon.jpg` | 앱 아이콘 (256x256 JPEG) (선택) | 직접 구하거나 만든다. 없으면 NRO 에 든 아이콘을 그대로 쓴다 |

**2. 이미지**: 앱 아이콘(`icon.jpg`, 256x256 JPEG)만 쓰이고 없으면 NRO 의 기본 아이콘을 씁니다. 이미지는 저장소에 없으니 필요하면 직접 구해 위 위치에 두세요. 배너와 스크린샷은 다루지 않습니다.

**3. 확인하고 실행**

```
python3 build.py guide tekken3e    # 빈 칸과 구하는 곳 확인
python3 build.py tekken3e --rom <내 게임 데이터 폴더> --zip
```
<!-- quick:end -->

개인 빌드. 원작자 표기: omarma.

- 공개 릴리스나 원 프로젝트 링크가 없어 기록용으로만 등록합니다. NRO와 게임 데이터는 이 저장소에 없습니다.
- 필요한 것: game.toml, switch.ini 와 게임 데이터 (같은 폴더)
- 한글 지원: 확인 안 함
- 상태: 실기에서 이 저장소 기준으로 확인하지 않았습니다.
