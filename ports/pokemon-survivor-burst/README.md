# 포켓몬 서바이버 버스트 (Pokemon Survivor Burst)

<!-- quick:begin -->
## 필요한 파일과 명령어

**1. 받아서 둘 것**

| 놓을 위치 | 무엇 | 구하는 곳 |
| :--- | :--- | :--- |
| `ports/pokemon-survivor-burst/in/pokemon-survivor-burst.nro` | 스위치용 NRO | https://github.com/randygil/rgss-switch 의 릴리스를 받거나 직접 빌드 |
| `ports/pokemon-survivor-burst/in/data` | 원작자 배포본 게임 폴더 (Audio/, Data/, Fonts/, Graphics/, Plugins/, lib/) | 내가 가진 정품 데이터 (--rom <폴더> 로 따로 줘도 된다) |
| `ports/pokemon-survivor-burst/icon.jpg` | 앱 아이콘 (256x256 JPEG) (선택) | 직접 구하거나 만든다. 없으면 NRO 에 든 아이콘을 그대로 쓴다 |

**2. 이미지**: 앱 아이콘(`icon.jpg`, 256x256 JPEG)만 쓰이고 없으면 NRO 의 기본 아이콘을 씁니다. 이미지는 저장소에 없으니 필요하면 직접 구해 위 위치에 두세요. 배너와 스크린샷은 다루지 않습니다.

**3. 확인하고 실행**

```
python3 build.py guide pokemon-survivor-burst    # 빈 칸과 구하는 곳 확인
python3 build.py pokemon-survivor-burst --rom <내 게임 데이터 폴더> --zip
```

- 원 프로젝트: https://github.com/white-axe/mkxp-z
- 스위치 포트 소스: https://github.com/randygil/rgss-switch
<!-- quick:end -->

Pokémon Survivor Burst 9.0.3 을 [rgss-switch](https://github.com/randygil/rgss-switch) 0.1.0 (mkxp-z 2.4.2 + CRuby 3.1.7, Horizon 네이티브, GPLv2+)으로 스위치에서 돌린 개인 포트. 홈브류(hbmenu) 전용 NRO 이고 완성본이 내 라이브러리에서 돌고 있다.

게임 본체는 원작자가 배포한 팬게임이다. 이 저장소에는 게임 데이터도 원작 에셋도 NRO 도 없고, 원작자 배포본을 직접 받아 둔다는 전제로 실기에서 쓴 설정(`overlay/Game.ini`, `overlay/mkxp.json`)만 담았다.

## 구성 (완성본 기준)

`SD:/switch/pokemon-survivor-burst/` 안에 `pokemon-survivor-burst.nro`, `mkxp.json`, `Game.ini`, `soundfont.sf2`, `lib/`, `Data/`, `Graphics/`, `Audio/`, `Fonts/`, `Plugins/` (파일 약 6,260개, 약 0.91GiB). `mkxp.json` 은 `pack_psb.py` 로 층을 쌓아 생성했다.

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

## 변환 키트

변환 스크립트는 별도 공개 저장소 [jshsakura/psb-switch-kit](https://github.com/jshsakura/psb-switch-kit) 에 있다. 게임에서 파생된 파일이 하나도 없는 도구 모음이고, rgss-switch 의 `Empaquetar.ps1` 을 파이썬으로 옮긴 파생이라 라이선스는 이 저장소의 MIT 가 아니라 **GPLv2+** 이다(키트의 `LICENSE`, 크레딧은 `NOTICE.md`).

| 키트 안의 파일 | 하는 일 |
| :--- | :--- |
| `pack_psb.py` | 사용자가 푼 게임 폴더와 rgss-switch 를 묶어 `out/switch/pokemon-survivor-burst/` 를 만든다. 빌드 전에 `ruby -c` 와 심 행동 테스트를 돌려 실패하면 중단한다 |
| `widescreen_patch.py` | `Scripts.rxdata` 의 화면 폭 변경(원본 자동 보존) |
| `lib/nx-psb-fixes.rb` | 이름 입력의 게임패드 매핑과 스플래시·로드 화면 중앙 정렬 런타임 심 |
| `tests/nx_shims_test.rb` | 위 심의 행동 테스트 |

게임 본체와 rgss-switch 엔진(NRO 포함)은 이 저장소에도 키트에도 없고 각자 받는다(엔진은 [저장소 릴리스](https://github.com/randygil/rgss-switch/releases), 내가 쓴 것은 v0.1.0 이고 이후 v0.2.x 가 나왔지만 써 보지 않았다). 내 라이브러리의 완성본에는 키트에 없는 조정(타이틀 배경 교체, 성능 옵션, 엔티티 상한 등)이 더 들어 있으므로 키트 결과가 완성본과 똑같지는 않다.

### Ruby 가 필요한 이유

Ruby 는 스위치가 아니라 **변환하는 PC** 에만 필요하다(`sudo apt install ruby-full`).

- 게임이 RPG Maker XP(RGSS1)로 만든 Pokémon Essentials 계열 팬게임이라 스크립트가 전부 Ruby 다. rgss-switch 가 CRuby 3.1.7 을 품고 있어 스위치에서 그대로 돈다(`mkxp.json` 의 `rubyLoadpath: ["lib"]`, 게임 계열 `ruby31`).
- `lib/nx-psb-fixes.rb` 같은 런타임 심도 Ruby 이고, `mkxp.json` 의 `preloadScript` 로 부팅 때 먼저 읽힌다.
- `pack_psb.py` 는 빌드 전에 PC 의 Ruby 로 ① `lib/` 와 `Plugins/` 의 모든 `.rb` 를 `ruby -c` 로 문법 검사하고 ② `tests/nx_shims_test.rb` 로 RGSS 를 흉내 낸 스텁 위에서 심 동작을 검사한다. 하나라도 실패하면 빌드를 멈춘다. 문법 오류가 든 채로 기기에 올라가 재다운로드를 여러 번 한 일이 있어서 만든 관문이다.
- 알려진 함정: `class_eval` 블록 안의 `def` 에서는 클래스 상수가 렉시컬로 풀리지 않아 `self.class.const_get(:KEY)` 로 써야 한다. 조용한 `rescue` 가 `NameError` 를 삼키면 패치가 말없이 죽는다.
- 이 저장소를 준비한 컴퓨터에는 Ruby 가 없어 위 검사를 돌리지 못했다. 키트는 Ruby 없이 빌드를 시작하면 "ruby 없음" 으로 멈춘다.

## 와이드(16:9)

`Data/Scripts.rxdata` 의 `Settings::SCREEN_WIDTH` 를 512 에서 683 으로, `mkxp.json` 의 `defScreenW` 도 683 으로 바꿨다(683x384, 16:9). 바꾸는 스크립트는 키트의 `widescreen_patch.py` 이고 원본은 `.orig` 로 보존한다. `Scripts.rxdata` 는 게임 파일이라 이 저장소에 담지 않는다. 일부 Essentials 메뉴가 어긋나 보일 수 있다.

## 알려진 제약

- 온라인 기능(리더보드, Breach, 시즌)은 프로세스 생성을 쓰는데 스위치에 없어서 안 된다. 오프라인 플레이에는 영향이 없다.
- 진동 없음. 문자 입력은 화면 그리드 입력으로 대체된다.
- 후반 물결(적 280+, 투사체 240)에서 프레임이 떨어지는지는 직접 확인하지 못했다.
- NSP 로 설치하려면 PC 에서 rgss-switch 배포판의 `Empaquetar.ps1` 이 필요하다. 이 NRO 는 hbmenu 전용이다.
