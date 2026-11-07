# 캐슬바니아 리뱀프드 (Castlevania ReVamped)

<!-- quick:begin -->
## 필요한 파일과 명령어

**1. 받아서 둘 것**

| 놓을 위치 | 무엇 | 구하는 곳 |
| :--- | :--- | :--- |
| `ports/cvrevamped_nx/in/cvrevamped_nx.nro` | 스위치용 NRO (선택) | 안 둬도 된다. 없으면 bshurikan/cvrevamped_nx 릴리스 v1.1.3 에서 자동으로 받는다 |
| `ports/cvrevamped_nx/in/data` | 자체 무료 풀버전 데이터 포함 (선택) | 안 둬도 된다. 릴리스의 cvrevamped-switch-release-v1.1.3.zip, CastlevaniaReVamped-switch-v1.1.3.apk 를 받아 함께 넣는다 |
| `ports/cvrevamped_nx/icon.jpg` | 앱 아이콘 (256x256 JPEG) (선택) | 직접 구하거나 만든다. 없으면 NRO 에 든 아이콘을 그대로 쓴다 |

**2. 이미지**: 앱 아이콘(`icon.jpg`, 256x256 JPEG)만 쓰이고 없으면 NRO 의 기본 아이콘을 씁니다. 이미지는 저장소에 없으니 필요하면 직접 구해 위 위치에 두세요. 배너와 스크린샷은 다루지 않습니다.

**3. 확인하고 실행**

```
python3 build.py guide cvrevamped_nx    # 빈 칸과 구하는 곳 확인
python3 build.py cvrevamped_nx --zip
```

NRO 는 구하지 않아도 됩니다. `in/` 에 없으면 bshurikan/cvrevamped_nx 릴리스 v1.1.3 에서 받아 sha256 을 확인하고 씁니다.

게임 데이터도 구하지 않아도 됩니다. 릴리스에 든 `cvrevamped-switch-release-v1.1.3.zip`, `CastlevaniaReVamped-switch-v1.1.3.apk` 를 받아 sha256 을 확인하고 풀어 넣습니다.

- 스위치 포트 소스: https://github.com/bshurikan/cvrevamped_nx
<!-- quick:end -->

Lv.4 Games 가 GameMaker 로 만든 무료 캐슬바니아 팬게임의 스위치 포트. 원작 롬은 필요 없다.

- 업스트림: [bshurikan/cvrevamped_nx](https://github.com/bshurikan/cvrevamped_nx) v1.1.3
- 상태: 기기 시험 전 (`planned`)
- 한국어: 지원하지 않는다

업스트림의 수동 설치(Method B)를 조립기가 그대로 한다.

| 넣는 것 | 어디서 |
| :--- | :--- |
| `cvrevamped_nx.nro`, `config.txt`, `gamecontrollerdb.txt`, `sdl2.txt` | 릴리스 zip 의 `cvrevamped_nx/` |
| `game.apk` | 릴리스의 스위치용 APK 를 이름만 바꿔서 |
| `libyoyo.so` | APK 의 `lib/arm64-v8a/libyoyo.so` |
| `assets/` | APK 의 `assets/`. 그 안의 `sdl2.txt` 는 릴리스 zip 의 것으로 덮는다(조작에 필요) |

NRO 는 `sdmc:/switch/cvrevamped_nx/` 를 찾으므로 id 에 밑줄이 들어간다. 업스트림은 `config.txt` 의 `input_profile 1` 을 그대로 두라고 한다.

```
python3 build.py cvrevamped_nx --deploy <homebrew 폴더>
```
