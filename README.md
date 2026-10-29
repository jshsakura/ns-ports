# NS Korean Ports Hub (ns-ports)

[![Platforms](https://img.shields.io/badge/platform-NS%20%7C%20Horizon%20OS%20(AArch64)-blue.svg)](https://github.com/jshsakura/ns-ports)
[![Language](https://img.shields.io/badge/language-Korean%20(100%25)-red.svg)](README.md)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Ports](https://img.shields.io/badge/native%20ports-69-orange.svg)](ports.json)

**닌텐도 스위치(NS / Horizon OS)에서 오래된 게임을 한국어로 돌려 본 개인 포팅 테스트 기록**입니다.

제가 직접 해 본 방법과 결과를 적어 둔 것이라 서비스나 배포물이 아닙니다. 실기에서 확인한 포트는 상태 열에 확인됨(🎯)으로 표시했고, 나머지는 레시피만 정리했거나 확인 전입니다. 포트마다 어떤 파일을 어디에 어떤 이름으로 두었는지 배치표로 남겼고, 같은 방식으로 폴더를 묶는 작은 스크립트(`build.py`)를 곁들였습니다. 이 저장소에는 게임 데이터, NRO, 패치가 적용된 완성 데이터가 없고, 차이 패치만 들어 있습니다. 필요한 파일은 각자 합법적으로 구해야 합니다.

---

## 🌟 핵심 특징

* 📖 **한국어 포팅 방법 가이드**
  * `ports/<id>/README.md` 마다 준비물, 그 구하는 법, 파일 배치 경로와 파일명을 적어 둡니다.
  * 모든 포트가 한국어화된 것은 아닙니다. 아래 표의 한국어화 형태 열을 확인하세요.
* 🔧 **조립 스크립트 (`build.py` + 포트별 `recipe.py`)**
  * 배치표대로 파일을 두면 `sd:/switch/<id>/` 폴더로 묶는 정도를 합니다.
  * 포트에 따라 한글 pack 배치나 일부 변환이 레시피에 들어 있지만, 파일을 구해 주거나 번역해 주지는 않습니다.
  * 확인된 포트는 일부이고, 아래 표의 상태 열이 기준입니다.

| 구성 요소 | 하는 일 |
| :--- | :--- |
| `build.py` | 포트 조립, 새 포트 뼈대 생성(`new`), 목록(`--list`) |
| `ports/<id>/recipe.py` | 포트별 변환과 빌드 (예: `wwhd` 는 한글 pack 을 두 언어 슬롯에 배치) |
| `ports/<id>/slots.json` | 채워야 할 알맹이 칸 목록. `python3 build.py check <id>` 가 빈칸을 알려 주고, 빌드 전에도 자동 점검 |
| `tools/dante_kr_patch.py` | 단테스 인페르노 한글 패치 적용 |
| `tools/sly1_extract` | 슬라이 쿠퍼 1 한국판 디스크에서 게임 데이터 추출 |
| `tools/gen_install.py` | `ports.json` 으로 INSTALL.md 준비물 표 생성 |

* ⚖️ **저작권 클린룸 (Clean-room Rule)**
  * 원작의 저작권 보호 파일(ROM, ISO, 상용 음원, 패치가 적용된 완성 데이터 등)은 저장소에 담지 않습니다. 원본 없이는 쓸 수 없는 차이 패치(BPS 등)만 `ports/<id>/patches/` 에 둡니다.
  * 모든 준비와 조립은 사용자가 합법적으로 소유한 정품 데이터로 각자의 컴퓨터에서 이루어집니다.

---

## 🎮 포트 카탈로그 (하이라이트 34종)

> 전체 69종 목록은 `python3 build.py --list` 또는 [INSTALL.md](INSTALL.md) 의 포트별 준비물 표를 보십시오. ID 를 누르면 그 포트의 필요 파일과 명령어가 맨 위에 나옵니다.

| ID | 타이틀 | 장르 / 원작 | 한국어화 형태 | 자이로 | 구동 및 레시피 상태 |
| :--- | :--- | :--- | :--- | :---: | :---: |
| **[`ge007`](ports/ge007/README.md)** | **골든아이 007** | FPS / N64 | 100% 한글 자막 (v1.0 retrace) | ✅ | 🎯 **실기 검수 완료** ([빌더 준비 완료](https://github.com/jshsakura/goldeneye-007-switch)) |
| **[`zelda3-ko`](ports/zelda3-ko/README.md)** | **젤다: 신들의 트라이포스** | ARPG / SNES | C 디컴파일 60fps & 16:9 한글화 | ➖ | 🎯 **실기 검수 완료** |
| **[`zelda-oot-hd`](ports/zelda-oot-hd/README.md)** | **젤다: 시간의 오카리나 HD** | Action / N64 | SoH v9.3.0 + 한글 Pretendard HD | ✅ | 🎯 **실기 검수 완료** |
| **[`zelda-mm-hd`](ports/zelda-mm-hd/README.md)** | **젤다: 무쥬라의 가면 HD** | Action / N64 | 2S2H v5.0.1 + MM-Reloaded HD | ✅ | 🎯 **실기 배포 완료** |
| **[`devilutionx`](ports/devilutionx/README.md)** | **디아블로 1 + 헬파이어** | ARPG / PC | 한글 폰트 + 완벽 한글 자막 | ➖ | 🎯 **실기 검수 완료** |
| **[`half-life`](ports/half-life/README.md)** | **하프라이프 1** | FPS / PC | **공식 한국어 풀더빙 음성 & 자막** | ✅ | 🎯 **실기 검수 완료** |
| **[`cstrike`](ports/cstrike/README.md)** | **카운터 스트라이크 1.6** | FPS / PC | 한글 UI/입력/점수판 + 순정 영문판 | ✅ | 🔧 신형 엔진 빌드, 실기 확인 중 ([레시피](ports/cstrike)) |
| **[`fallout1`](ports/fallout1/README.md)** | **폴아웃 1** | CRPG / PC | fallout1-ce CJK 폰트 엔진 + 한글화 | ➖ | 🎯 **실기 검수 완료** |
| **[`fallout2`](ports/fallout2/README.md)** | **폴아웃 2** | CRPG / PC | fallout2-ce CP949 FreeType 한글 | ➖ | 🎯 **실기 검수 완료** |
| **[`cnc`](ports/cnc/README.md)** | **C&C: 타이베리안 던** | RTS / PC | C&C Gold 한글 폰트 & 미션 브리핑 | ➖ | 📦 레시피 수록 완료 |
| **[`redalert`](ports/redalert/README.md)** | **C&C: 레드 얼럿** | RTS / PC | 한글화 연합군/소련군 캠페인 | ➖ | 📦 레시피 수록 완료 |
| **[`war1gus`](ports/war1gus/README.md)** | **워크래프트 1: 오크와 인간** | RTS / PC | War1gus Stratagus 원작 에셋 연동 | ➖ | 📦 레시피 수록 완료 |
| **[`wargus`](ports/wargus/README.md)** | **워크래프트 2: BNE** | RTS / PC | 워크래프트 2 완벽 한글화 데이터 | ➖ | 📦 레시피 수록 완료 |
| **[`starcraft64`](ports/starcraft64/README.md)** | **스타크래프트 64 Recomp** | RTS / N64 | StarCraft 64 정적 리컴파일 한국어판 | ➖ | 📦 레시피 수록 완료 |
| **[`jak1`](ports/jak1/README.md)** | **잭 & 덱스터 (Jak 1)** | Action / PS2 | OpenGOAL 60fps 와이드스크린 | ➖ | 📦 레시피 수록 완료 |
| **[`jak2`](ports/jak2/README.md)** | **잭 2 (Jak II)** | Action / PS2 | **소니 공식 한국어 음성 더빙** | ➖ | 📦 레시피 수록 완료 |
| **[`jak3`](ports/jak3/README.md)** | **잭 3 (Jak 3)** | Action / PS2 | **소니 공식 한국어 음성 & 자막** | ➖ | 📦 레시피 수록 완료 |
| **[`fheroes2`](ports/fheroes2/README.md)** | **히어로즈 오브 마이트 앤 매직 2** | TBS / PC | fheroes2 공식 한국어 팩 지원 | ➖ | 📦 레시피 수록 완료 |
| **[`caesar3`](ports/caesar3/README.md)** | **시저 3 (Julius)** | Sim / PC | 시저 3 공식 한국어화 데이터 | ➖ | 📦 레시피 수록 완료 |
| **[`openrct2`](ports/openrct2/README.md)** | **롤러코스터 타이쿤 2** | Sim / PC | OpenRCT2 한글 폰트 & 자막 | ➖ | 📦 레시피 수록 완료 |
| **[`openttd`](ports/openttd/README.md)** | **오픈 TTD** | Sim / PC | OpenTTD 나눔고딕 한글 번역 | ➖ | 📦 레시피 수록 완료 |
| **[`sonic1`](ports/sonic1/README.md)** | **소닉 더 헤지혹 1 (2013)** | Platformer / RSDK | RSDKv4 디컴파일 공식 한국어(Lang=8) | ➖ | 📦 레시피 수록 완료 |
| **[`sonic2`](ports/sonic2/README.md)** | **소닉 더 헤지혹 2 (2013)** | Platformer / RSDK | RSDKv4 디컴파일 공식 한국어(Lang=8) | ➖ | 📦 레시피 수록 완료 |
| **[`sonic-cd`](ports/sonic-cd/README.md)** | **소닉 CD (2011)** | Platformer / RSDK | RSDKv3 디컴파일 60fps 와이드스크린 | ➖ | 📦 레시피 수록 완료 |
| **[`cannonball`](ports/cannonball/README.md)** | **아웃런 (Cannonball)** | Racing / Arcade | 60fps 아케이드 재구현 엔진 | ➖ | 📦 레시피 수록 완료 |
| **[`dantes-inferno`](ports/dantes-inferno/README.md)** | **단테스 인페르노** | Action / Xbox 360 Recomp | 정적 리컴파일 + 한글패치 적용 도구 | ✅ | 🧪 기기 시험 전 |
| **[`ro`](ports/ro/README.md)** | **라그나로크 온라인** | MMORPG / Client | 스위치 클라이언트 | ✅ | 🎯 기동 확인 |
| **[`sly1`](ports/sly1/README.md)** | **슬라이 쿠퍼 1** | Action / PS2 Decomp | 앱이 ISO를 직접 풀어 주는 네이티브 포트 (한국판 ISO 미지원) | ➖ | 🧪 기기 시험 전 |
| **[`nfsmw`](ports/nfsmw/README.md)** | **니드 포 스피드: 모스트 원티드** | Racing / Xbox 360 Recomp | 한국판(NTSC-K) 정적 리컴파일, 30fps | ✅ | 🧪 기기 시험 전 |
| **[`jazz`](ports/jazz/README.md)** | **재즈 잭래빗 2** | Platformer / PC | Jazz² Resurrection C++ 엔진 | ➖ | 📦 레시피 수록 완료 |
| **[`doom64`](ports/doom64/README.md)** | **둠 64 EX** | FPS / N64 | Doom64EX C++ 네이티브 포트 | ➖ | 📦 레시피 수록 완료 |
| **[`pokemon-survivor-burst`](ports/pokemon-survivor-burst/README.md)** | **포켓몬 서바이버 버스트** | Fan Game | mkxp-z 기반 팬게임, [변환 키트](https://github.com/jshsakura/psb-switch-kit) | ➖ | 📦 레시피 수록 완료 |
| **[`dragonball-z-rpg`](ports/dragonball-z-rpg/README.md)** | **드래곤볼 Z RPG** | Fan RPG | 한글 자막 지원 | ➖ | 📦 레시피 수록 완료 |
| **[`wwhd`](ports/wwhd/README.md)** | **바람의 지휘봉 HD** | Action / GC | 한글 패치 pack 적용 가이드 ([배치표](ports/wwhd/README.md)) | ➖ | 🎯 실기 검증 구성 재현 |

---

## 🚀 사용법 (Getting Started)

> 포트별 준비물은 [INSTALL.md](INSTALL.md), 한국어화 적용 방법은 각 포트 가이드(`ports/<id>/README.md`)를 보십시오.

### 1. 저장소 클론
```bash
git clone https://github.com/jshsakura/ns-ports.git
cd ns-ports
python3 build.py --list
```

### 2. 가이드대로 파일 배치 (예: 바람의 지휘봉 HD)
[ports/wwhd/README.md](ports/wwhd/README.md) 의 배치표대로 파일을 둡니다.

| 넣을 파일 | 위치 |
| :--- | :--- |
| SwitchWakerHD 빌드 NRO | `ports/wwhd/in/wwhd.nro` |
| 한글 패치의 `permanent_2d_UsEnglish.pack` | `ports/wwhd/in/permanent_2d_UsEnglish.pack` |
| 한글 패치의 `Title_00.szs` | `ports/wwhd/in/Title_00.szs` |

### 3. 조립
```bash
# --rom 에는 WiiU 덤프에서 content/ 가 보이는 폴더를 지정
python3 build.py wwhd --rom /path/to/wwhd_dump --zip                        # 한글 판
python3 build.py wwhd --rom /path/to/wwhd_dump --variant original --zip     # 원본 그대로
```
결과(`wwhd.nro` + `game/`)를 `sd:/switch/wwhd/` 로 복사해 홈브루 메뉴에서 실행합니다.

> 소스 빌드 포트(`cstrike`, `openrct2`, `zelda3-ko`, `ge007`)는 Docker(devkitPro) 로 NRO 를 직접 빌드합니다. 골든아이 007 은 전용 빌더 저장소([goldeneye-007-switch](https://github.com/jshsakura/goldeneye-007-switch))가 사용자의 일본판 `baserom.j.z64` 를 받아 BPS 한글 패치를 적용해 빌드합니다.

### 4. 내 파일로 바로 쓰기 (새 포트 만들기)
이미 빌드된 NRO 와 아이콘, 내 게임 데이터만 있으면 포트 뼈대가 바로 만들어집니다.

```bash
# 1) 뼈대 만들기 (ports/<id>/ 와 목록 항목이 생깁니다)
python3 build.py new mygame "내 게임 (My Game)" --nro /path/to/mygame.nro --icon /path/to/icon.jpg

# 2) 덮어쓸 파일(한글 사전, 설정 등)은 ports/mygame/overlay/ 에 같은 구조로 넣습니다

# 3) 내 게임 데이터와 합쳐 조립 (--zip 으로 압축)
python3 build.py mygame --rom /path/to/game-data
```

---

## ⚖️ 저작권 및 법적 고지 (Legal Notice)

* 본 저장소는 원작 게임의 저작권 보호 파일(ROM, ISO, WAD, MPQ, 음원, 텍스처 등)을 일절 포함하지 않습니다.
* 모든 빌드 과정은 최종 사용자가 합법적으로 소유한 정품 게임 미디어로부터 로컬 환경에서 직접 에셋을 추출하고, 합법적인 차분 패치(BPS)를 결합하도록 설계되었습니다.
* 각 게임의 지적 재산권은 원작 개발사 및 유통사에 귀속됩니다.
