# 맥오수 (McOsu)

<!-- quick:begin -->
## 필요한 파일과 명령어

**1. 받아서 둘 것**

| 놓을 위치 | 무엇 | 구하는 곳 |
| :--- | :--- | :--- |
| `ports/mcosu/in/McEngine.nro` | 스위치용 NRO (선택) | 안 둬도 된다. 없으면 McKay42/McOsu-NX 릴리스 v33.14 에서 자동으로 받는다 |
| `ports/mcosu/in/data` | 자체 무료 풀버전 데이터 포함 (선택) | 안 둬도 된다. 릴리스의 McOsu.zip 를 받아 함께 넣는다 |
| `ports/mcosu/icon.jpg` | 앱 아이콘 (256x256 JPEG) (선택) | 직접 구하거나 만든다. 없으면 NRO 에 든 아이콘을 그대로 쓴다 |

**2. 이미지**: 앱 아이콘(`icon.jpg`, 256x256 JPEG)만 쓰이고 없으면 NRO 의 기본 아이콘을 씁니다. 이미지는 저장소에 없으니 필요하면 직접 구해 위 위치에 두세요. 배너와 스크린샷은 다루지 않습니다.

**3. 확인하고 실행**

```
python3 build.py guide mcosu    # 빈 칸과 구하는 곳 확인
python3 build.py mcosu --zip
```

NRO 는 구하지 않아도 됩니다. `in/` 에 없으면 McKay42/McOsu-NX 릴리스 v33.14 에서 받아 sha256 을 확인하고 씁니다.

게임 데이터도 구하지 않아도 됩니다. 같은 릴리스의 `McOsu.zip` 를 받아 sha256 을 확인하고 풀어 넣습니다.

- 원 프로젝트: https://github.com/McKay42/McOsu
- 스위치 포트 소스: https://github.com/McKay42/McOsu-NX
<!-- quick:end -->

리듬 게임 osu!의 클라이언트 McOsu의 스위치 포트. 릴리스에 든 기본 곡을 함께 받고, 다른 비트맵은 Songs 폴더에 넣어 추가합니다.

- 업스트림: [McKay42/McOsu-NX](https://github.com/McKay42/McOsu-NX) v33.14
- 상태: 기기 시험 전 (`planned`)
- 한국어: 지원하지 않는다

릴리스 zip 에 NRO(`McEngine.nro`)와 기본 곡(`Songs/`), 설정(`cfg/`)이 함께 있다. 조립할 때 zip 의 `switch/McOsu/` 아래를 배포 폴더에 푼다. NRO 는 `sdmc:/switch/McOsu/` 를 찾는다. 이 저장소는 폴더를 `mcosu` 로 만드는데, SD 카드 파일 시스템이 대소문자를 가리지 않으므로 같은 폴더로 열릴 것으로 본다(기기에서 확인하지 않은 추정).

```
python3 build.py mcosu --deploy <homebrew 폴더>
```
