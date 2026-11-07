# 브로그 (Brogue CE)

<!-- quick:begin -->
## 필요한 파일과 명령어

**1. 받아서 둘 것**

| 놓을 위치 | 무엇 | 구하는 곳 |
| :--- | :--- | :--- |
| `ports/brogue/in/brogue.nro` | 스위치용 NRO (선택) | 안 둬도 된다. 없으면 capsterx-switch/BrogueCE 릴리스 v1.9.2-r2 에서 자동으로 받는다 |
| `ports/brogue/in/data` | 자체 무료 풀버전 데이터 포함 (선택) | 필요 없다. 게임 데이터가 NRO 안에 들어 있다 |
| `ports/brogue/icon.jpg` | 앱 아이콘 (256x256 JPEG) (선택) | 직접 구하거나 만든다. 없으면 NRO 에 든 아이콘을 그대로 쓴다 |

**2. 이미지**: 앱 아이콘(`icon.jpg`, 256x256 JPEG)만 쓰이고 없으면 NRO 의 기본 아이콘을 씁니다. 이미지는 저장소에 없으니 필요하면 직접 구해 위 위치에 두세요. 배너와 스크린샷은 다루지 않습니다.

**3. 확인하고 실행**

```
python3 build.py guide brogue    # 빈 칸과 구하는 곳 확인
python3 build.py brogue --zip
```

NRO 는 구하지 않아도 됩니다. `in/` 에 없으면 capsterx-switch/BrogueCE 릴리스 v1.9.2-r2 에서 받아 sha256 을 확인하고 씁니다.

- 원 프로젝트: https://github.com/tmewett/BrogueCE
- 스위치 포트 소스: https://github.com/capsterx-switch/BrogueCE
<!-- quick:end -->

던전 탐험 로그라이크 브로그 커뮤니티 에디션의 스위치 포트. 게임 데이터가 NRO 안에 들어 있어 따로 구할 것이 없습니다.

- 업스트림: [capsterx-switch/BrogueCE](https://github.com/capsterx-switch/BrogueCE) v1.9.2-r2
- 상태: 기기 시험 전 (`planned`)
- 한국어: 지원하지 않는다

오픈소스 로그라이크라 게임 데이터가 NRO 의 romfs 안에 들어 있다. 릴리스 zip 에서 NRO 만 꺼내 쓴다.

```
python3 build.py brogue --deploy <homebrew 폴더>
```
