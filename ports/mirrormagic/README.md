# 미러 매직 (Mirror Magic)

<!-- quick:begin -->
## 필요한 파일과 명령어

**1. 받아서 둘 것**

| 놓을 위치 | 무엇 | 구하는 곳 |
| :--- | :--- | :--- |
| `ports/mirrormagic/in/mirrormagic.nro` | 스위치용 NRO (선택) | 안 둬도 된다. 없으면 rsn8887/rocksndiamonds 릴리스 1.15 에서 자동으로 받는다 |
| `ports/mirrormagic/in/data` | 자체 무료 풀버전 데이터 포함 (선택) | 안 둬도 된다. 릴리스의 mirrormagic_data.zip 를 받아 함께 넣는다 |
| `ports/mirrormagic/icon.jpg` | 앱 아이콘 (256x256 JPEG) (선택) | 직접 구하거나 만든다. 없으면 NRO 에 든 아이콘을 그대로 쓴다 |

**2. 이미지**: 앱 아이콘(`icon.jpg`, 256x256 JPEG)만 쓰이고 없으면 NRO 의 기본 아이콘을 씁니다. 이미지는 저장소에 없으니 필요하면 직접 구해 위 위치에 두세요. 배너와 스크린샷은 다루지 않습니다.

**3. 확인하고 실행**

```
python3 build.py guide mirrormagic    # 빈 칸과 구하는 곳 확인
python3 build.py mirrormagic --zip
```

NRO 는 구하지 않아도 됩니다. `in/` 에 없으면 rsn8887/rocksndiamonds 릴리스 1.15 에서 받아 sha256 을 확인하고 씁니다.

게임 데이터도 구하지 않아도 됩니다. 같은 릴리스의 `mirrormagic_data.zip` 를 받아 sha256 을 확인하고 풀어 넣습니다.

- 원 프로젝트: https://www.artsoft.org/mirrormagic/
- 스위치 포트 소스: https://github.com/rsn8887/rocksndiamonds
<!-- quick:end -->

거울로 레이저를 꺾는 퍼즐 게임 미러 매직의 스위치 포트. 무료 레벨과 그래픽, 소리를 릴리스에서 함께 받습니다.

- 업스트림: [rsn8887/rocksndiamonds](https://github.com/rsn8887/rocksndiamonds) 1.15
- 상태: 기기 시험 전 (`planned`)
- 한국어: 지원하지 않는다

록스 앤 다이아몬즈와 같은 릴리스에 있다. 조립할 때 `mirrormagic_data.zip` 의 `mirrormagic/` 아래를 배포 폴더에 푼다.

```
python3 build.py mirrormagic --deploy <homebrew 폴더>
```
