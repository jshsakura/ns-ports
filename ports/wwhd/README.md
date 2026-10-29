# 바람의 지휘봉 HD (Wind Waker HD, SwitchWakerHD)

<!-- quick:begin -->
## 필요한 파일과 명령어

**1. 받아서 둘 것**

| 놓을 위치 | 무엇 | 구하는 곳 |
| :--- | :--- | :--- |
| `ports/wwhd/in/wwhd.nro` | SwitchWakerHD 빌드 NRO | https://github.com/centollOS/SwitchWakerHD 를 직접 빌드 (BUILD.md) |
| `ports/wwhd/in/data` | 내 Wii U 바람의 지휘봉 HD 덤프 (code/ content/ meta/ 가 보이는 폴더) | 내 Wii U 에서 추출. 복사할 필요 없이 --rom <그 폴더> 로 알려 주면 된다 |
| `ports/wwhd/in/Title_00.szs` | 한글 패치의 타이틀 화면 레이아웃 (한글 판만) | 한글 패치 Ver 1.02 폴더의 windwakerHD/Layout/Title_00.szs (패치 제작진 배포) |
| `ports/wwhd/icon.jpg` | 앱 아이콘 (256x256 JPEG) (선택) | 직접 구하거나 만든다. 없으면 NRO 에 든 아이콘을 그대로 쓴다 |

**2. 이미지**: 앱 아이콘(`icon.jpg`, 256x256 JPEG)만 쓰이고 없으면 NRO 의 기본 아이콘을 씁니다. 이미지는 저장소에 없으니 필요하면 직접 구해 위 위치에 두세요. 배너와 스크린샷은 다루지 않습니다.

**3. 확인하고 실행**

```
python3 build.py guide wwhd    # 빈 칸과 구하는 곳 확인
python3 build.py wwhd --zip
```

- 스위치 포트 소스: https://github.com/centollOS/SwitchWakerHD
<!-- quick:end -->

WiiU 바람의 지휘봉 HD 를 스위치에서 네이티브로 구동하는 [centollOS/SwitchWakerHD](https://github.com/centollOS/SwitchWakerHD) 포트에, 한국어 패치 파일을 얹는 방법 가이드.

이 저장소는 방법을 안내할 뿐, NRO 나 한글 패치 산출물, 게임 데이터를 담지 않는다(클린룸). 아래 파일은 전부 사용자 소유분을 쓴다.

## 어떤 파일을 어디서 구해 어디에 두나

| # | 파일 | 어디서 | 어디에 |
| :-: | :--- | :--- | :--- |
| 1 | `wwhd.nro` | [SwitchWakerHD](https://github.com/centollOS/SwitchWakerHD) 를 직접 빌드 ([BUILD.md](BUILD.md)) | `ports/wwhd/in/wwhd.nro` |
| 2 | Wii U 덤프 폴더 | 내 Wii U 에서 추출 (`code/` `content/` `meta/` 가 보이는 폴더) | 옮기지 않는다. 명령에 `--rom <그 폴더>` 로 적는다 |
| 3 | `Title_00.szs` | 한글 패치 Ver 1.02 압축 안의 `windwakerHD/Layout/Title_00.szs` (패치 제작진 배포) | `ports/wwhd/in/Title_00.szs` (한글 판만) |

한글 pack(`permanent_2d_UsEnglish.pack`)은 따로 구하지 않는다. 조립할 때 이 저장소의 차이 패치
`patches/permanent_2d_UsEnglish.xdelta` 를 2번 덤프의 `content/Common/Pack/permanent_2d_UsFrench.pack` 에 적용해 만든다.
그래서 `xdelta3` 만 깔려 있으면 된다(예: `sudo apt install xdelta3`).

## 조립

```
python3 build.py guide wwhd                                                 # 빈 칸 확인
python3 build.py wwhd --rom /path/to/wwhd_dump --zip                        # 한글 판
python3 build.py wwhd --rom /path/to/wwhd_dump --variant original --zip     # 원본 그대로 (3번 불필요)
```

결과는 `ports/wwhd/dist/switch/wwhd/`(`wwhd.nro` + `game/`)와 zip 입니다. 폴더를 `sd:/switch/wwhd/` 로 복사해 홈브루 메뉴에서 실행합니다.

## 조립이 덤프에 쓰는 것

한글 pack 한 개가 두 언어 슬롯에 같은 내용으로 들어가서 게임 언어 설정과 상관없이 한글이 뜹니다(실기 검증된 배포본과 같은 구성).

| 만들어지는 파일 | 위치 |
| :--- | :--- |
| 한글 pack | `game/content/Common/Pack/permanent_2d_UsEnglish.pack` 와 `permanent_2d_JpJapanese.pack` |
| `Title_00.szs` | `game/content/Common/Layout/Title_00.szs` |

## 한글 패치 크레딧과 조건

한글 패치 `Ver 1.02` 는 게임큐브판 한글패치를 만든 Cocory 님의 도움으로, 샤이닝구포스, 닥스, 송키, nAtAs, 이로치레시람 님이 제작했다. 패치 안내문에 따르면 **상업적 사용은 금지**이고, 번역 오류 제보는 패치 제작진이 연 [번역 수정 시트](https://docs.google.com/spreadsheets/d/1lIJIghvEBiemGmxu5oDbOIM_3CeRSt0W0jgtOOYTDTw/edit#gid=0)로 받는다. 북미판(영문)과 일판 대응이다.

이 저장소의 `patches/permanent_2d_UsEnglish.xdelta` 는 이 패치의 한글 텍스트 작업물을 담고 있으므로, 위 조건(비상업)을 따르는 개인 사용만 전제로 한다. 제작진이 배포 방식에 이의가 있으면 이 파일을 내린다.
