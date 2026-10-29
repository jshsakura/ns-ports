# 바람의 지휘봉 HD (Wind Waker HD, SwitchWakerHD)

<!-- quick:begin -->
## 하는 법 (파일 두고 한 번에)

**내가 두는 것은 두 가지뿐입니다.**

| 내가 둘 곳 | 무엇을 | 어디서 구하나 |
| :--- | :--- | :--- |
| `ports/wwhd/in/data` | 내 Wii U 바람의 지휘봉 HD 덤프 폴더. 그 안에 `code` `content` `meta` 가 바로 보여야 함 (USA, 버전 0) | 내 Wii U 에서 추출. 큰 폴더라 `ln -s /내/덤프/경로 ports/wwhd/in/data` 로 링크해도 됨 |
| `ports/wwhd/in/patch` | 한글 패치 Ver 1.02 를 **압축 푼 폴더** 통째로 (안에 `windwakerHD` 폴더가 있음) | 패치 제작진 배포본 (아래 크레딧 참고). 원본 그대로 만들 거면 생략 |

```
python3 build.py wwhd --zip
```

**나머지는 프로그램이 알아서 만듭니다. 아래는 각각 어디서 나오는지입니다.**

| 필요한 것 | 어디서 나오나 |
| :--- | :--- |
| 한글 텍스트 pack (`permanent_2d_UsEnglish.pack`) | 한글 패치에서 꺼내지 않습니다. 이 저장소의 차이 패치(`patches/permanent_2d_UsEnglish.xdelta`)를 내 덤프의 원본 pack(`content/Common/Pack/permanent_2d_UsFrench.pack`)에 적용해 만듭니다 (`xdelta3` 필요) |
| `Title_00.szs` (타이틀 화면) | `in/patch` 폴더 안의 `windwakerHD/Layout/Title_00.szs` 를 찾아 씁니다. 이것만 한글 패치에서 꺼내옵니다 |
| `wwhd.nro` | `in/wwhd.nro` 가 없으면 GitHub 의 SwitchWakerHD 를 받아 내 덤프로 도커 빌드합니다 (몇 시간, git 과 docker 필요) |
| 게임 데이터 | 내 덤프(`in/data`)를 링크로 연결합니다. 복사하지 않습니다 |

빠진 게 있으면 어디에 뭘 두라고 말하고 멈춥니다. 끝나면 `ports/wwhd/dist/switch/wwhd/` 폴더를 SD 카드의 `switch/` 에 복사해 홈브루 메뉴에서 실행합니다.

이미 빌드한 NRO 가 있으면 `ports/wwhd/in/wwhd.nro` 로 두면 빌드를 건너뜁니다. 원본 그대로: `python3 build.py wwhd --variant original --zip`. 경로를 직접 주려면 `--rom <덤프 폴더>` 도 됩니다.

## 필요한 파일을 자세히

### 1) Wii U 덤프 폴더 (필수, 내가 구함) → `ports/wwhd/in/data`

내 Wii U 로 받은 바람의 지휘봉 HD 의 게임 파일입니다. 아래 모양이어야 합니다.

```
ports/wwhd/in/data/
├── code/       ← 안에 cking.rpx 가 있어야 함
├── content/    ← Common/Pack/permanent_2d_UsFrench.pack 등이 들어 있음
└── meta/
```

- 반드시 **미국판(USA), 버전 0** 입니다. 한글 pack 을 만드는 차이 패치가 이 판의 `permanent_2d_UsFrench.pack` 한 파일에 맞춰져 있어서, 다른 판이면 패치 적용이 실패합니다.
- 읽기만 합니다. 원본 파일을 수정하지 않고 하드링크로 연결합니다.
- 덤프를 이 모양으로 만드는 방법(복호화에 Wii U 공용키가 필요)은 [BUILD.md](BUILD.md) 1번에 있습니다. 키는 각자 콘솔에서 읽어야 해서 저장소에 적지 않습니다.

### 2) 한글 패치 폴더 (한글 판일 때만, 내가 구함) → `ports/wwhd/in/patch`

한글 패치 Ver 1.02 배포본을 압축 푼 폴더 통째입니다. 안에 `windwakerHD/Layout/Title_00.szs` 가 있어야 하고, 프로그램은 이 파일 **하나만** 꺼내 씁니다 (타이틀 화면 한글 이미지).

```
ports/wwhd/in/patch/
└── windwakerHD/
    └── Layout/Title_00.szs     ← 이것만 사용
```

한글 텍스트가 든 pack 은 패치 폴더에서 가져오지 않습니다. 이 저장소의 `patches/permanent_2d_UsEnglish.xdelta` 를 덤프의 `permanent_2d_UsFrench.pack` 에 적용해 만들어 냅니다.
원본 그대로 만들 거면(`--variant original`) 이 폴더는 필요 없습니다.

### 3) 프로그램이 알아서 만드는 것 (내가 구하지 않음)

| 만드는 것 | 방법 | 필요한 도구 |
| :--- | :--- | :--- |
| 한글 pack | xdelta 차이 패치를 덤프의 원본 pack 에 적용 | `xdelta3` (`sudo apt install xdelta3`) |
| `wwhd.nro` | `ports/wwhd/in/wwhd.nro` 가 없으면 SwitchWakerHD(커밋 9a57081)를 받아 내 덤프로 도커 빌드 | `git`, `docker`, 몇 시간, 디스크 여유 |
| 게임 데이터 연결 | 덤프를 하드링크로 연결(복사 아님) | 덤프와 같은 디스크여야 링크, 아니면 복사 |

NRO 는 구하는 파일이 아니라 위 덤프로 빌드해서 만드는 파일입니다. 절차는 라이브러리의 `wwhd.nro` 를 만들 때 실제로 돌린 것과 같습니다([BUILD.md](BUILD.md)). 이미 빌드한 `wwhd.nro` 가 있으면 `ports/wwhd/in/wwhd.nro` 로 두면 이 단계를 건너뜁니다.

### 4) 끝나면 나오는 것

```
ports/wwhd/dist/switch/wwhd/
├── wwhd.nro
└── game/         ← 덤프 + 한글 pack 2개(UsEnglish, JpJapanese) + Title_00.szs
```

`wwhd` 폴더를 SD 카드의 `switch/` 에 통째로 복사합니다. SD 카드에서는 `switch/wwhd/wwhd.nro` 와 `switch/wwhd/game/` 이 됩니다.

실행: 아무 게임 아이콘 위에서 **R 버튼을 누른 채** 시작해 홈브루 메뉴로 들어가서 wwhd 를 켭니다(앨범으로 들어가면 메모리가 모자랍니다). 첫 실행에는 셰이더를 기기에서 컴파일하느라 20분쯤 걸리고(독 권장, B 로 건너뜀) 이후에는 저장됩니다.
<!-- quick:end -->

WiiU 바람의 지휘봉 HD 를 스위치에서 네이티브로 구동하는 [centollOS/SwitchWakerHD](https://github.com/centollOS/SwitchWakerHD) 포트에, 한국어 패치 파일을 얹는 방법 가이드.

이 저장소는 방법을 안내할 뿐, NRO 나 한글 패치 산출물, 게임 데이터를 담지 않는다(클린룸). 아래 파일은 전부 사용자 소유분을 쓴다.

## 한글 패치 크레딧과 조건

한글 패치 `Ver 1.02` 는 게임큐브판 한글패치를 만든 Cocory 님의 도움으로, 샤이닝구포스, 닥스, 송키, nAtAs, 이로치레시람 님이 제작했다. 패치 안내문에 따르면 **상업적 사용은 금지**이고, 번역 오류 제보는 패치 제작진이 연 [번역 수정 시트](https://docs.google.com/spreadsheets/d/1lIJIghvEBiemGmxu5oDbOIM_3CeRSt0W0jgtOOYTDTw/edit#gid=0)로 받는다. 북미판(영문)과 일판 대응이다.

이 저장소의 `patches/permanent_2d_UsEnglish.xdelta` 는 이 패치의 한글 텍스트 작업물을 담고 있으므로, 위 조건(비상업)을 따르는 개인 사용만 전제로 한다. 제작진이 배포 방식에 이의가 있으면 이 파일을 내린다.
