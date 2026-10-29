# 바람의 지휘봉 HD (Wind Waker HD, SwitchWakerHD)

<!-- quick:begin -->
## 필요한 파일과 명령어

| 넣을 위치 | 파일 |
| :--- | :--- |
| `ports/wwhd/in/wwhd.nro` | SwitchWakerHD 빌드 NRO |
| `ports/wwhd/in/Title_00.szs` | 한글 패치의 타이틀 화면 레이아웃 (한글 판만) |

- 스위치 포트 소스: https://github.com/centollOS/SwitchWakerHD

```
python3 build.py check wwhd    # 빈 칸 확인
python3 build.py wwhd --zip
```
<!-- quick:end -->

WiiU 바람의 지휘봉 HD 를 스위치에서 네이티브로 구동하는 [centollOS/SwitchWakerHD](https://github.com/centollOS/SwitchWakerHD) 포트에, 한국어 패치 파일을 얹는 방법 가이드.

이 저장소는 방법을 안내할 뿐, NRO 나 한글 패치 산출물, 게임 데이터를 담지 않는다(클린룸). 아래 파일은 전부 사용자 소유분을 쓴다.

## 준비물

1. **SwitchWakerHD 빌드 NRO**: 위 저장소의 릴리스 또는 직접 빌드한 `nro`
2. **WiiU 바람의 지휘봉 HD 덤프**: 추출해서 `code/`, `content/`, `meta/` 폴더가 보이는 상태
3. **한국어 패치 배포본**: 압축을 풀면 `windwakerHD/Pack/`, `windwakerHD/Layout/` 구조

## 파일 배치 (이름까지 정확히)

| 원본 파일 | 넣을 위치 |
| :--- | :--- |
| SwitchWakerHD 빌드 NRO | `ports/wwhd/in/wwhd.nro` |
| 패치의 `windwakerHD/Layout/Title_00.szs` | `ports/wwhd/in/Title_00.szs` |

한글 pack 은 이 저장소의 차이 패치 `patches/permanent_2d_UsEnglish.xdelta` 를 내 덤프의 `content/Common/Pack/permanent_2d_UsFrench.pack` 위에 적용해 조립 때 만든다(`xdelta3` 필요, 예: `sudo apt install xdelta3`). 원본 pack 은 패치 파일 안에 없고, USA v0 덤프의 UsFrench pack 이 있어야만 복원된다. 한글 패치 배포본의 pack 을 이미 갖고 있으면 `in/permanent_2d_UsEnglish.pack` 으로 두어도 되고, 그 파일이 우선이다.

패치 pack 하나로 조립 시 두 언어 슬롯(`permanent_2d_UsEnglish/JpJapanese.pack`)에
같은 내용이 들어가, 게임 내 언어 설정과 상관없이 한글이 뜬다(실기 검증된 배포본과 동일 구성).

## 조립

```
python3 build.py wwhd --rom /path/to/wwhd_dump --zip                        # 한글 판
python3 build.py wwhd --rom /path/to/wwhd_dump --variant original --zip     # 원본 그대로
```

`--rom` 에는 `content/` 가 보이는 덤프 루트를 지정한다. 결과는 `ports/wwhd/dist/switch/wwhd/`
(`wwhd.nro` + `game/`)이고, 이를 `sd:/switch/wwhd/` 로 복사해 홈브루 메뉴에서 실행한다.

## 한글 패치가 게임 데이터에 들어가는 위치

조립 시 아래 경로에 패치 파일이 기록된다. 수동으로 덤프에 적용할 때도 같은 규칙을 쓴다.

| `in/` 파일 | 조립 결과 경로 |
| :--- | :--- |
| `permanent_2d_UsEnglish.pack` | `game/content/Common/Pack/permanent_2d_UsEnglish.pack` |
| 같은 pack | `game/content/Common/Pack/permanent_2d_JpJapanese.pack` |
| `Title_00.szs` | `game/content/Common/Layout/Title_00.szs` |

덤프의 `content/Common/Pack/permanent_2d_EuEnglish.pack` 은 실기 검증본에 없는 파일이라 조립에서 제외한다.

## 한글 패치 크레딧과 조건

한글 패치 `Ver 1.02` 는 게임큐브판 한글패치를 만든 Cocory 님의 도움으로, 샤이닝구포스, 닥스, 송키, nAtAs, 이로치레시람 님이 제작했다. 패치 안내문에 따르면 **상업적 사용은 금지**이고, 번역 오류 제보는 패치 제작진이 연 [번역 수정 시트](https://docs.google.com/spreadsheets/d/1lIJIghvEBiemGmxu5oDbOIM_3CeRSt0W0jgtOOYTDTw/edit#gid=0)로 받는다. 북미판(영문)과 일판 대응이다.

이 저장소의 `patches/permanent_2d_UsEnglish.xdelta` 는 이 패치의 한글 텍스트 작업물을 담고 있으므로, 위 조건(비상업)을 따르는 개인 사용만 전제로 한다. 제작진이 배포 방식에 이의가 있으면 이 파일을 내린다.
