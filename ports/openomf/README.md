# 원 머스트 폴 2097 (One Must Fall: 2097)

<!-- quick:begin -->
## 필요한 파일과 명령어

**1. 받아서 둘 것**

| 놓을 위치 | 무엇 | 구하는 곳 |
| :--- | :--- | :--- |
| `ports/openomf/in/openomf.nro` | 스위치용 NRO (선택) | 안 둬도 된다. 없으면 Thorhax/OpenOMF-NX-Modern 릴리스 v0.8.7-nx 에서 자동으로 받는다 |
| `ports/openomf/in/data` | 자체 무료 풀버전 데이터 포함 (선택) | 안 둬도 된다. 릴리스의 openomf-switch-v0.8.7.zip 를 받아 함께 넣는다 |
| `ports/openomf/icon.jpg` | 앱 아이콘 (256x256 JPEG) (선택) | 직접 구하거나 만든다. 없으면 NRO 에 든 아이콘을 그대로 쓴다 |

**2. 이미지**: 앱 아이콘(`icon.jpg`, 256x256 JPEG)만 쓰이고 없으면 NRO 의 기본 아이콘을 씁니다. 이미지는 저장소에 없으니 필요하면 직접 구해 위 위치에 두세요. 배너와 스크린샷은 다루지 않습니다.

**3. 확인하고 실행**

```
python3 build.py guide openomf    # 빈 칸과 구하는 곳 확인
python3 build.py openomf --zip
```

NRO 는 구하지 않아도 됩니다. `in/` 에 없으면 Thorhax/OpenOMF-NX-Modern 릴리스 v0.8.7-nx 에서 받아 sha256 을 확인하고 씁니다.

게임 데이터도 구하지 않아도 됩니다. 릴리스에 든 `openomf-switch-v0.8.7.zip` 를 받아 sha256 을 확인하고 풀어 넣습니다.

- 원 프로젝트: https://github.com/omf2097/openomf
- 스위치 포트 소스: https://github.com/Thorhax/OpenOMF-NX-Modern
<!-- quick:end -->

1994년 로봇 대전 격투 게임 원 머스트 폴 2097을 재구현한 OpenOMF의 스위치 포트. 프리웨어로 풀린 원작 데이터를 릴리스에서 함께 받습니다.

- 업스트림: [Thorhax/OpenOMF-NX-Modern](https://github.com/Thorhax/OpenOMF-NX-Modern) v0.8.7-nx
- 상태: 기기 시험 전 (`planned`)
- 한국어: 지원하지 않는다

릴리스 zip 에 NRO 와 `resources/` 의 원작 데이터가 함께 있다. 원작은 1999년에 프리웨어로 풀렸다. 조립할 때 zip 의 `openomf/` 아래를 배포 폴더에 푼다. 업스트림은 게임 덮어쓰기(타이틀 시작 중 R 누르기)로 여는 것을 권한다.

```
python3 build.py openomf --deploy <homebrew 폴더>
```
