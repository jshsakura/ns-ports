# 슬라이 쿠퍼 1 (Sly Cooper and the Thievius Raccoonus)

<!-- quick:begin -->
## 필요한 파일과 명령어

**1. 받아서 둘 것**

| 놓을 위치 | 무엇 | 구하는 곳 |
| :--- | :--- | :--- |
| `ports/sly1/in/sly1.nro` | ProjectCane 0.5.0 NRO | https://github.com/NaGaa95/ProjectCane 릴리스의 ProjectCane.nro |
| `ports/sly1/in/data` | 한국판 ISO 를 풀어낸 데이터 폴더 | 내 한국판 ISO(SCKA_200.04)로 tools/sly1_extract/README.md 대로 만든다 (--rom 으로 따로 줘도 된다) |
| `ports/sly1/icon.jpg` | 앱 아이콘 (256x256 JPEG) (선택) | 직접 구하거나 만든다. 없으면 NRO 에 든 아이콘을 그대로 쓴다 |

**2. 이미지**: 앱 아이콘(`icon.jpg`, 256x256 JPEG)만 쓰이고 없으면 NRO 의 기본 아이콘을 씁니다. 이미지는 저장소에 없으니 필요하면 직접 구해 위 위치에 두세요. 배너와 스크린샷은 다루지 않습니다.

**3. 확인하고 실행**

```
python3 build.py guide sly1    # 빈 칸과 구하는 곳 확인
python3 build.py sly1 --rom <내 게임 데이터 폴더> --zip
```

NRO 는 구하지 않아도 됩니다. `in/` 에 없으면 NaGaa95/ProjectCane 릴리스 0.5.0 에서 받아 sha256 을 확인하고 씁니다.

- 원 프로젝트: https://github.com/theclub654/ProjectCane
- 스위치 포트 소스: https://github.com/NaGaa95/ProjectCane
<!-- quick:end -->

PS2 슬라이 쿠퍼 1을 디컴파일한 네이티브 포트. 업스트림 [NaGaa95/ProjectCane](https://github.com/NaGaa95/ProjectCane) 0.5.0 의 `ProjectCane.nro` 를 쓴다.
원판은 게임 데이터를 앱이 처음 실행할 때 SD 카드의 ISO 를 골라 `sdmc:/switch/ProjectCane` 에 직접 풀어 준다. 이 저장소에는 NRO 도 데이터도 없다.

- 지원하는 ISO: 미국 `SCUS-971.98`, 유럽 `SCES-509.17`, 일본 `SCPS-150.36`
- 업스트림은 한국판(`SCKA_200.04`)을 거절한다. 그래서 `tools/sly1_extract/` 로 서버에서 ISO 를 미리 풀어 데이터를 폴더에 넣는다. 받으면 ISO 없이 바로 실행된다. 한국판은 미국판 구조가 아니라 일본판·PAL 쪽 구조라서 추출기 소스를 한국판용으로 고쳐 쓴다.
- 한국판은 한글을 자모 조각으로 저장한다. 추출할 때 원판 자모 글리프를 합쳐 완성형 글자를 폰트에 추가한다(`tools/sly1_extract/kr_font.h`).
- 상태: 기기 시험 전 (`planned`)

## 사용
`in/sly1.nro` 에 릴리스의 `ProjectCane.nro` 를 두고 (저장소에 없다) 풀어 둔 데이터와 함께 조립한다. 데이터 만드는 법은 `tools/sly1_extract/README.md` 에 있다.
```
python3 build.py sly1 --rom <풀어낸 폴더> --deploy <homebrew 폴더>
```
