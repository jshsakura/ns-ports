# 포켓몬 서바이버 버스트 (Pokemon Survivor Burst)

<!-- quick:begin -->
## 필요한 파일과 명령어

필요한 것: 원작자 배포본 게임 폴더 (Audio/, Data/, Fonts/, Graphics/, Plugins/, lib/)
NRO: `ports/pokemon-survivor-burst/in/pokemon-survivor-burst.nro`

- 원 프로젝트: https://github.com/white-axe/mkxp-z
- 스위치 포트 소스: https://github.com/randygil/rgss-switch

```
python3 build.py check pokemon-survivor-burst    # 빈 칸 확인
python3 build.py pokemon-survivor-burst --zip
```
<!-- quick:end -->

Pokémon Survivor Burst 9.0.3 을 [rgss-switch](https://github.com/randygil/rgss-switch) 0.1.0 (mkxp-z 2.4.2 + CRuby 3.1.7, Horizon 네이티브, GPLv2+)으로 스위치에서 돌린 개인 포트. 홈브류(hbmenu) 전용 NRO 이고 완성본이 내 라이브러리에서 돌고 있다.

게임 본체는 원작자가 배포한 팬게임이다. 이 저장소에는 게임 데이터도 원작 에셋도 NRO 도 없고, 원작자 배포본을 직접 받아 둔다는 전제로 실기에서 쓴 설정(`overlay/Game.ini`, `overlay/mkxp.json`)만 담았다.

## 구성 (완성본 기준)

`SD:/switch/pokemon-survivor-burst/` 안에 `pokemon-survivor-burst.nro`, `mkxp.json`, `Game.ini`, `soundfont.sf2`, `lib/`, `Data/`, `Graphics/`, `Audio/`, `Fonts/`, `Plugins/` (파일 약 6,260개, 약 0.91GiB). `mkxp.json` 은 `kit/pack_psb.py` 로 층을 쌓아 생성했다.

## 실행

스위치에서 아무 게임 아이콘 위에서 R 을 길게 눌러 hbmenu 를 연 뒤 실행한다. 앨범 단독 실행(애플릿 모드)은 메모리가 약 448MB 라 뜨지 않는다. 처음 켜면 20~40초 걸린다.

| 스위치 | RGSS | 게임 바인딩 |
| :--- | :--- | :--- |
| A / B | C / B | Use / Back |
| X | X | JumpUp |
| Y | A | Action |
| ZL / ZR | Y / Z | JumpDown / Special |

## 한국어

게임에 내장돼 있다(`fusion-poke-pixel-ko` 폰트 + `messages_korean_*.dat`). 따로 패치하지 않는다.

## 변환 키트 (`kit/`)

게임에서 파생된 파일이 하나도 없는 변환 스크립트 모음이다. 라이선스는 이 저장소의 MIT 가 아니라 **GPLv2+** 이고(`kit/LICENSE`, 크레딧은 `kit/NOTICE.md`), rgss-switch 의 `Empaquetar.ps1` 을 파이썬으로 옮긴 파생이라서 같은 조건으로 둔다.

| 파일 | 하는 일 |
| :--- | :--- |
| `kit/pack_psb.py` | 사용자가 푼 게임 폴더와 rgss-switch 를 묶어 `out/switch/pokemon-survivor-burst/` 를 만든다. 빌드 전에 `ruby -c` 와 심 행동 테스트를 돌려 실패하면 중단한다 |
| `kit/widescreen_patch.py` | `Scripts.rxdata` 의 화면 폭 변경(원본 자동 보존) |
| `kit/lib/nx-psb-fixes.rb` | 이름 입력의 게임패드 매핑과 스플래시·로드 화면 중앙 정렬 런타임 심 |
| `kit/tests/nx_shims_test.rb` | 위 심의 행동 테스트 |

사용법은 `kit/README.ko.md` 를 본다. 게임 본체와 rgss-switch 엔진(NRO 포함)은 이 저장소에도 키트에도 없고 각자 받는다(저장소 릴리스 페이지, 내가 쓴 것은 v0.1.0 이고 이후 v0.2.x 가 나왔지만 써 보지 않았다). 내 라이브러리의 완성본에는 이 키트에 없는 조정(타이틀 배경 교체, 성능 옵션, 엔티티 상한 등)이 더 들어 있으므로 키트 결과가 완성본과 똑같지는 않다.

## 와이드(16:9)

`Data/Scripts.rxdata` 의 `Settings::SCREEN_WIDTH` 를 512 에서 683 으로, `mkxp.json` 의 `defScreenW` 도 683 으로 바꿨다(683x384, 16:9). 바꾸는 스크립트는 `kit/widescreen_patch.py` 이고 원본은 `.orig` 로 보존한다. `Scripts.rxdata` 는 게임 파일이라 이 저장소에 담지 않는다. 일부 Essentials 메뉴가 어긋나 보일 수 있다.

## 알려진 제약

- 온라인 기능(리더보드, Breach, 시즌)은 프로세스 생성을 쓰는데 스위치에 없어서 안 된다. 오프라인 플레이에는 영향이 없다.
- 진동 없음. 문자 입력은 화면 그리드 입력으로 대체된다.
- 후반 물결(적 280+, 투사체 240)에서 프레임이 떨어지는지는 직접 확인하지 못했다.
- NSP 로 설치하려면 PC 에서 rgss-switch 배포판의 `Empaquetar.ps1` 이 필요하다. 이 NRO 는 hbmenu 전용이다.
