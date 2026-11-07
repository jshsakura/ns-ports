# 마블 블래스트 플래티넘 (Marble Blast Platinum)

<!-- quick:begin -->
## 필요한 파일과 명령어

**1. 받아서 둘 것**

| 놓을 위치 | 무엇 | 구하는 곳 |
| :--- | :--- | :--- |
| `ports/mbplatinum/in/mbplatinum.nro` | 스위치용 NRO (선택) | 안 둬도 된다. 없으면 ChanseyIsTheBest/MBHaxe-Switch 릴리스 1.7.3s 에서 자동으로 받는다 |
| `ports/mbplatinum/in/data` | 자체 무료 풀버전 데이터 포함 (선택) | 안 둬도 된다. 릴리스의 switch.7z 를 받아 함께 넣는다 |
| `ports/mbplatinum/icon.jpg` | 앱 아이콘 (256x256 JPEG) (선택) | 직접 구하거나 만든다. 없으면 NRO 에 든 아이콘을 그대로 쓴다 |

**2. 이미지**: 앱 아이콘(`icon.jpg`, 256x256 JPEG)만 쓰이고 없으면 NRO 의 기본 아이콘을 씁니다. 이미지는 저장소에 없으니 필요하면 직접 구해 위 위치에 두세요. 배너와 스크린샷은 다루지 않습니다.

**3. 확인하고 실행**

```
python3 build.py guide mbplatinum    # 빈 칸과 구하는 곳 확인
python3 build.py mbplatinum --zip
```

NRO 는 구하지 않아도 됩니다. `in/` 에 없으면 ChanseyIsTheBest/MBHaxe-Switch 릴리스 1.7.3s 에서 받아 sha256 을 확인하고 씁니다.

게임 데이터도 구하지 않아도 됩니다. 릴리스에 든 `switch.7z` 를 받아 sha256 을 확인하고 풀어 넣습니다.

- 원 프로젝트: https://github.com/RandomityGuy/MBHaxe
- 스위치 포트 소스: https://github.com/ChanseyIsTheBest/MBHaxe-Switch
<!-- quick:end -->

3D 구슬 굴리기 게임 마블 블래스트 골드(2003)와 커뮤니티 확장판 플래티넘을 Haxe 로 다시 만든 [MBHaxe](https://github.com/RandomityGuy/MBHaxe) 의 스위치 포트.

- 업스트림: [ChanseyIsTheBest/MBHaxe-Switch](https://github.com/ChanseyIsTheBest/MBHaxe-Switch) 1.7.3s
- 상태: 기기 시험 전 (`planned`)
- 한국어: 지원하지 않는다

릴리스는 7z 하나(`switch.7z`)에 NRO 와 데이터를 함께 싣는다. 조립할 때 `mbplatinum/` 아래를 배포 폴더에 푼다. 7z 를 풀려면 조립하는 컴퓨터에 `7z` 명령이 있어야 한다. NRO 는 `sdmc:/switch/mbplatinum/` 에서 데이터를 찾으므로 폴더 이름이 id 와 같다.

```
python3 build.py mbplatinum --deploy <homebrew 폴더>
```
