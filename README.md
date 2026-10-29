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
| `ports/<id>/slots.json` | 채워야 할 알맹이 칸 목록. `python3 build.py guide <id>` 가 빈칸과 구하는 곳을 알려 주고, 빌드 전에도 자동 점검(없으면 `port.json` 과 `ports.json` 에서 만든다) |
| `tools/dante_kr_patch.py` | 단테스 인페르노 한글 패치 적용 |
| `tools/sly1_extract` | 슬라이 쿠퍼 1 한국판 디스크에서 게임 데이터 추출 |
| `tools/gen_install.py` | `ports.json` 으로 INSTALL.md 준비물 표 생성 |

* ⚖️ **저작권 클린룸 (Clean-room Rule)**
  * 원작의 저작권 보호 파일(ROM, ISO, 상용 음원, 패치가 적용된 완성 데이터 등)은 저장소에 담지 않습니다. 원본 없이는 쓸 수 없는 차이 패치(BPS 등)만 `ports/<id>/patches/` 에 둡니다.
  * 모든 준비와 조립은 사용자가 합법적으로 소유한 정품 데이터로 각자의 컴퓨터에서 이루어집니다.

---

## 🎮 포트 카탈로그 (전체 69종)

> 상태는 `ports.json` 의 `status` 를 그대로 옮긴 것이고 이 표는 `tools/gen_catalog.py` 가 만듭니다. 🎯 는 실기에서 확인한 것, 🟡 는 켜지는 것까지, 📦 는 레시피만 정리한 것, 🧪 는 아직 기기에서 안 해 본 것입니다. 빌더 저장소가 따로 있는 포트는 **빌더** 링크가 있습니다.

<!-- catalog:begin -->
| ID | 타이틀 | 장르 / 원작 | 한글 | 자이로 | 상태 | 바로가기 |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| `devilutionx` | 디아블로 1 (Diablo 1 + Hellfire) | ARPG / PC | ✅ | ➖ | 🎯 실기 확인 | [가이드](ports/devilutionx/README.md) · [포트 소스](https://github.com/diasurgical/DevilutionX) |
| `fallout1` | 폴아웃 1 (Fallout 1) | CRPG / PC | ✅ | ➖ | 🎯 실기 확인 | [가이드](ports/fallout1/README.md) · [포트 소스](https://github.com/alexbatalov/fallout1-ce) |
| `fallout2` | 폴아웃 2 (Fallout 2) | CRPG / PC | ✅ | ➖ | 🎯 실기 확인 | [가이드](ports/fallout2/README.md) · [포트 소스](https://github.com/alexbatalov/fallout2-ce) |
| `ge007` | 골든아이 007 (GoldenEye 007) | FPS / N64 | ✅ | ✅ | 🎯 실기 확인 | [가이드](ports/ge007/README.md) · [레시피](ports/ge007/recipe.py) · [빌더 저장소](https://github.com/jshsakura/goldeneye-007-switch) |
| `half-life` | 하프라이프 1 (Half-Life) | FPS / PC | ✅ | ✅ | 🎯 실기 확인 | [가이드](ports/half-life/README.md) · [포트 소스](https://github.com/FWGS/xash3d-fwgs) |
| `zelda-mm-hd` | 젤다의 전설: 무쥬라의 가면 HD (Majora's Mask) | Action Adventure / N64 | ✅ | ✅ | 🎯 실기 확인 | [가이드](ports/zelda-mm-hd/README.md) · [포트 소스](https://github.com/2ship2harkinian/2ship2harkinian) |
| `zelda-oot-hd` | 젤다의 전설: 시간의 오카리나 HD (Ocarina of Time) | Action Adventure / N64 | ✅ | ✅ | 🎯 실기 확인 | [가이드](ports/zelda-oot-hd/README.md) · [포트 소스](https://github.com/HarbourMasters/Shipwright) |
| `zelda3-ko` | 젤다의 전설: 신들의 트라이포스 (A Link to the Past) | Action Adventure / SNES | ✅ | ➖ | 🎯 실기 확인 | [가이드](ports/zelda3-ko/README.md) · [레시피](ports/zelda3-ko/recipe.py) · [포트 소스](https://github.com/snesrev/zelda3) |
| `cstrike` | 카운터 스트라이크 1.6 (Counter-Strike 1.6) | FPS / PC | ✅ | ✅ | 🟡 기동 확인 | [가이드](ports/cstrike/README.md) · [빌드](ports/cstrike/BUILD.md) · [레시피](ports/cstrike/recipe.py) · [포트 소스](https://github.com/FWGS/xash3d-fwgs) |
| `pokemon-survivor-burst` | 포켓몬 서바이버 버스트 (Pokemon Survivor Burst) | Fan Game / Roguelite | ✅ | ➖ | 🟡 기동 확인 | [가이드](ports/pokemon-survivor-burst/README.md) · [빌더 저장소](https://github.com/jshsakura/psb-switch-kit) · [포트 소스](https://github.com/randygil/rgss-switch) · [원 프로젝트](https://github.com/white-axe/mkxp-z) |
| `ro` | 라그나로크 온라인 (RO Switch) | MMORPG / Client | ✅ | ➖ | 🟡 기동 확인 | [가이드](ports/ro/README.md) |
| `caesar3` | 시저 3 (Caesar III / Julius) | City Builder / PC | ✅ | ➖ | 📦 레시피 정리 | [가이드](ports/caesar3/README.md) · [포트 소스](https://github.com/bvschaik/julius) |
| `cannonball` | 아웃런 (OutRun / Cannonball) | Racing / Arcade | ➖ | ➖ | 📦 레시피 정리 | [가이드](ports/cannonball/README.md) · [포트 소스](https://github.com/Thorhax/Cannonball-NX-Modern) |
| `cnc` | 커맨드 앤 컨커: 타이베리안 던 (C&C 1) | RTS / PC | ✅ | ➖ | 📦 레시피 정리 | [가이드](ports/cnc/README.md) · [포트 소스](https://github.com/TheAssemblyArmada/Vanilla-Conquer) |
| `doom` | GZDoom (Doom 1 & FreeDoom) | FPS / Source Port | ➖ | ➖ | 📦 레시피 정리 | [가이드](ports/doom/README.md) · [포트 소스](https://github.com/fgsfdsfgs/gzdoom) · [원 프로젝트](https://github.com/ZDoom/gzdoom) |
| `doom64` | 둠 64 EX (Doom 64 EX) | FPS / N64 | ➖ | ➖ | 📦 레시피 정리 | [가이드](ports/doom64/README.md) · [포트 소스](https://github.com/fgsfdsfgs/Doom64EX) · [원 프로젝트](https://github.com/svkaiser/Doom64EX) |
| `dragonball-z-rpg` | 드래곤볼 Z RPG (Dragon Ball Z RPG) | RPG / Homebrew | ✅ | ➖ | 📦 레시피 정리 | [가이드](ports/dragonball-z-rpg/README.md) · [포트 소스](https://github.com/white-axe/mkxp-z) · [원 프로젝트](https://github.com/Ancurio/mkxp) |
| `fheroes2` | 히어로즈 오브 마이트 앤 매직 2 (fheroes2) | Turn-based Strategy / PC | ✅ | ➖ | 📦 레시피 정리 | [가이드](ports/fheroes2/README.md) · [포트 소스](https://github.com/ihhub/fheroes2) |
| `jak1` | 잭 & 덱스터: 구세계의 유산 (Jak and Daxter) | Action Adventure / PS2 | ➖ | ➖ | 📦 레시피 정리 | [가이드](ports/jak1/README.md) · [포트 소스](https://github.com/fildicio/jak-project-switch) |
| `jak2` | 잭 2 (Jak II) | Action Adventure / PS2 | ✅ | ➖ | 📦 레시피 정리 | [가이드](ports/jak2/README.md) · [포트 소스](https://github.com/fildicio/jak-project-switch) |
| `jak3` | 잭 3 (Jak 3) | Action Adventure / PS2 | ✅ | ➖ | 📦 레시피 정리 | [가이드](ports/jak3/README.md) · [포트 소스](https://github.com/fildicio/jak-project-switch) |
| `jazz` | 재즈 잭래빗 2 (Jazz² Resurrection) | Platformer / PC | ➖ | ➖ | 📦 레시피 정리 | [가이드](ports/jazz/README.md) · [포트 소스](https://github.com/deathkiller/jazz2) |
| `openbor` | OpenBOR (Streets of Rage X 등) | Beat'em up / Engine | ➖ | ➖ | 📦 레시피 정리 | [가이드](ports/openbor/README.md) · [포트 소스](https://github.com/SylphiaWindy/openbor) · [원 프로젝트](https://github.com/DCurrent/openbor) |
| `openrct2` | 롤러코스터 타이쿤 2 (OpenRCT2) | Simulation / PC | ✅ | ➖ | 📦 레시피 정리 | [가이드](ports/openrct2/README.md) · [레시피](ports/openrct2/recipe.py) · [포트 소스](https://github.com/Wander-Eule/OpenRCT2-Switch) · [원 프로젝트](https://github.com/OpenRCT2/OpenRCT2) |
| `openttd` | 오픈 TTD (OpenTTD) | Simulation / PC | ✅ | ➖ | 📦 레시피 정리 | [가이드](ports/openttd/README.md) · [포트 소스](https://github.com/rsn8887/OpenTTD) · [원 프로젝트](https://github.com/OpenTTD/OpenTTD) |
| `opentyrian` | 오픈 타이리안 (OpenTyrian) | Shoot'em up / Decomp | ➖ | ➖ | 📦 레시피 정리 | [가이드](ports/opentyrian/README.md) · [포트 소스](https://github.com/theflippedbit/opentyrian-nx) |
| `redalert` | 커맨드 앤 컨커: 레드 얼럿 (C&C Red Alert) | RTS / PC | ✅ | ➖ | 📦 레시피 정리 | [가이드](ports/redalert/README.md) · [포트 소스](https://github.com/TheAssemblyArmada/Vanilla-Conquer) |
| `sonic-cd` | 소닉 CD (Sonic CD 2011) | Platformer / Retro-Engine | ➖ | ➖ | 📦 레시피 정리 | [가이드](ports/sonic-cd/README.md) · [포트 소스](https://github.com/heyjoeway/Sonic-CD-11-Decompilation) · [원 프로젝트](https://github.com/RSDKModding/RSDKv3-Decompilation) |
| `sonic1` | 소닉 더 헤지혹 1 (Sonic 1 2013) | Platformer / Retro-Engine | ✅ | ➖ | 📦 레시피 정리 | [가이드](ports/sonic1/README.md) · [포트 소스](https://github.com/heyjoeway/Sonic-1-2-2013-Decompilation) · [원 프로젝트](https://github.com/RSDKModding/RSDKv4-Decompilation) |
| `sonic2` | 소닉 더 헤지혹 2 (Sonic 2 2013) | Platformer / Retro-Engine | ✅ | ➖ | 📦 레시피 정리 | [가이드](ports/sonic2/README.md) · [포트 소스](https://github.com/heyjoeway/Sonic-1-2-2013-Decompilation) · [원 프로젝트](https://github.com/RSDKModding/RSDKv4-Decompilation) |
| `space-cadet` | 3D 핀볼: 스페이스 카뎃 (Space Cadet Pinball) | Casual / Decomp | ➖ | ➖ | 📦 레시피 정리 | [가이드](ports/space-cadet/README.md) · [포트 소스](https://github.com/averne/SpaceCadetPinball-NX) · [원 프로젝트](https://github.com/k4zmu2a/SpaceCadetPinball) |
| `srb2` | 소닉 로보 블래스트 2 (Sonic Robo Blast 2) | Platformer / 3D Fangame | ➖ | ➖ | 📦 레시피 정리 | [가이드](ports/srb2/README.md) · [포트 소스](https://github.com/P-AS/srb2-switch) |
| `starcraft64` | 스타크래프트 64 (StarCraft 64 Recomp) | RTS / N64 | ✅ | ➖ | 📦 레시피 정리 | [가이드](ports/starcraft64/README.md) · [포트 소스](https://github.com/gabryboy12-ai/StarCraft64-NX) |
| `supermariowar` | 슈퍼 마리오 워 (Super Mario War) | Party / Platformer | ➖ | ➖ | 📦 레시피 정리 | [가이드](ports/supermariowar/README.md) · [포트 소스](https://github.com/retronx-team/supermariowar-nx) |
| `war1gus` | 워크래프트 1: 오크와 인간 (Warcraft: Orcs & Humans) | RTS / PC | ✅ | ➖ | 📦 레시피 정리 | [가이드](ports/war1gus/README.md) · [포트 소스](https://github.com/Thorhax/War1gus-NX-Modern) |
| `wargus` | 워크래프트 2: 배틀넷 에디션 (Warcraft 2) | RTS / PC | ✅ | ➖ | 📦 레시피 정리 | [가이드](ports/wargus/README.md) · [포트 소스](https://github.com/Thorhax/Wargus-NX-Modern) |
| `wwhd` | 바람의 지휘봉 HD (Wind Waker HD Decomp/Port) | Action Adventure / GC | ✅ | ➖ | 📦 레시피 정리 | [가이드](ports/wwhd/README.md) · [빌드](ports/wwhd/BUILD.md) · [레시피](ports/wwhd/recipe.py) · [포트 소스](https://github.com/centollOS/SwitchWakerHD) |
| `zelda-olb` | 젤다의 전설: 오니 링크의 시작 (Zelda: OLB) | Action RPG / Fan Game | ➖ | ➖ | 📦 레시피 정리 | [가이드](ports/zelda-olb/README.md) · [포트 소스](https://github.com/worthis/ZeldaOLB-new-engine) |
| `zelda-roth` | 젤다의 전설: 하일리아인의 귀환 (Zelda: ROTH) | Action RPG / Fan Game | ➖ | ➖ | 📦 레시피 정리 | [가이드](ports/zelda-roth/README.md) · [포트 소스](https://github.com/worthis/ZeldaROTH-new-engine) |
| `0ad` | 0 A.D. | RTS / PC | ➖ | ➖ | 🧪 기기 시험 전 | [가이드](ports/0ad/README.md) · [포트 소스](https://github.com/souldbminerr/0ad-switch) · [원 프로젝트](https://github.com/0ad/0ad) |
| `avp-gold` | 에일리언 대 프레데터: 골드 (AvP Gold) | FPS / Classic Native | ➖ | ➖ | 🧪 기기 시험 전 | [가이드](ports/avp-gold/README.md) · [포트 소스](https://github.com/Thorhax/AvP-Gold-NX-Modern) |
| `dantes-inferno` | 단테스 인페르노 (Dante's Inferno) | Action / Xbox 360 Recomp | ✅ | ➖ | 🧪 기기 시험 전 | [가이드](ports/dantes-inferno/README.md) · [포트 소스](https://github.com/VasilkovND/dantes-inferno-nx) |
| `daytona-usa` | 데이토나 USA (Daytona USA) | Racing / Model 2 Recomp | ➖ | ➖ | 🧪 기기 시험 전 | [가이드](ports/daytona-usa/README.md) · [포트 소스](https://github.com/Thorhax/Daytona-NX-Modern) |
| `doukutsu-rs` | 동굴 이야기 (Cave Story, doukutsu-rs) | Platformer / PC | ➖ | ➖ | 🧪 기기 시험 전 | [가이드](ports/doukutsu-rs/README.md) · [원 프로젝트](https://github.com/doukutsu-rs/doukutsu-rs) |
| `futari` | 벌레공주 두 사람 (Mushihimesama Futari) | Shooter / Xbox 360 Recomp | ➖ | ➖ | 🧪 기기 시험 전 | [가이드](ports/futari/README.md) · [포트 소스](https://github.com/ChanseyIsTheBest/futari-nx) |
| `hurrican` | Hurrican | Platformer / PC | ➖ | ➖ | 🧪 기기 시험 전 | [가이드](ports/hurrican/README.md) · [포트 소스](https://github.com/rsn8887/Hurrican) · [원 프로젝트](https://github.com/Uukrull/Hurrican) |
| `marathon-recomp` | 소닉 더 헤지혹 2006 (Sonic 06 / MarathonRecomp) | Action / Xbox 360 Recomp | ➖ | ➖ | 🧪 기기 시험 전 | [가이드](ports/marathon-recomp/README.md) · [포트 소스](https://github.com/ChanseyIsTheBest/MarathonRecomp-NX) · [원 프로젝트](https://github.com/sonicnext-dev/MarathonRecomp) |
| `masseffect` | 매스 이펙트 1 (Mass Effect) | RPG / Xbox 360 Recomp | ➖ | ➖ | 🧪 기기 시험 전 | [가이드](ports/masseffect/README.md) · [포트 소스](https://github.com/nebadasSwifty/masseffect-nx) |
| `nfsmw` | 니드 포 스피드: 모스트 원티드 (Need for Speed: Most Wanted) | Racing / Xbox 360 Recomp | ✅ | ➖ | 🧪 기기 시험 전 | [가이드](ports/nfsmw/README.md) · [포트 소스](https://github.com/StevensND/nfsmw-nx) |
| `nzportable` | 나치 좀비: 포터블 (Nazi Zombies: Portable) | FPS / Standalone | ➖ | ➖ | 🧪 기기 시험 전 | [가이드](ports/nzportable/README.md) · [포트 소스](https://github.com/nzp-team/nzportable) |
| `openmw` | 엘더스크롤 3: 모로윈드 (OpenMW) | RPG / Modern Native | ➖ | ➖ | 🧪 기기 시험 전 | [가이드](ports/openmw/README.md) · [포트 소스](https://github.com/fgsfdsfgs/openmw) · [원 프로젝트](https://github.com/OpenMW/openmw) |
| `pokemmo` | 포켓몬 MMO (PokeMMO) | MMORPG / Client | ✅ | ➖ | 🧪 기기 시험 전 | [가이드](ports/pokemmo/README.md) · [포트 소스](https://github.com/Petit-Prince-dev/PokeMMO-NX) |
| `project8` | 토니 호크 프로젝트 8 (Tony Hawk Project 8) | Sports / Xbox 360 Recomp | ➖ | ➖ | 🧪 기기 시험 전 | [가이드](ports/project8/README.md) · [포트 소스](https://github.com/R-drg/project8-sw) |
| `pvz` | 식물 대 좀비 (Plants vs. Zombies Portable) | Strategy / Decomp | ✅ | ➖ | 🧪 기기 시험 전 | [가이드](ports/pvz/README.md) · [포트 소스](https://github.com/HayatoG/PvZ-Portable) · [원 프로젝트](https://github.com/wszqkzqk/PvZ-Portable) |
| `sa2` | 소닉 어드벤처 2 (Sonic Adventure 2) | Action / Xbox 360 Recomp | ➖ | ➖ | 🧪 기기 시험 전 | [가이드](ports/sa2/README.md) · [포트 소스](https://github.com/ChanseyIsTheBest/sa2-nx) |
| `sh1` | 사일런트 힐 1 (Silent Hill 1) | Horror / PS1 Decomp | ➖ | ➖ | 🧪 기기 시험 전 | [가이드](ports/sh1/README.md) · [포트 소스](https://github.com/ChaykaDed/silent-hill-decomp-nx) · [원 프로젝트](https://github.com/SlickAmogus/silent-hill-decomp) |
| `sh2` | 사일런트 힐 2 (Silent Hill 2) | Horror / PC Native | ➖ | ➖ | 🧪 기기 시험 전 | [가이드](ports/sh2/README.md) · [포트 소스](https://github.com/cutarev/sh2-nx) |
| `sh3` | 사일런트 힐 3 (Silent Hill 3) | Horror / PC Native | ➖ | ➖ | 🧪 기기 시험 전 | [가이드](ports/sh3/README.md) · [포트 소스](https://github.com/cutarev/sh3-nx) |
| `sh4` | 사일런트 힐 4: 더 룸 (Silent Hill 4) | Horror / PC Native | ➖ | ➖ | 🧪 기기 시험 전 | [가이드](ports/sh4/README.md) · [포트 소스](https://github.com/72ak/sh4-nx) |
| `sly1` | 슬라이 쿠퍼 1 (Sly Cooper and the Thievius Raccoonus) | Action / PS2 Decomp | ➖ | ➖ | 🧪 기기 시험 전 | [가이드](ports/sly1/README.md) · [포트 소스](https://github.com/NaGaa95/ProjectCane) · [원 프로젝트](https://github.com/theclub654/ProjectCane) |
| `sonic-fighters` | 소닉 더 파이터즈 (Sonic the Fighters) | Fighting / Model 2 Recomp | ➖ | ➖ | 🧪 기기 시험 전 | [가이드](ports/sonic-fighters/README.md) · [포트 소스](https://github.com/boraeskicioglu/sonic_the_fighters_nx) |
| `supertux2` | SuperTux | Platformer / PC | ➖ | ➖ | 🧪 기기 시험 전 | [가이드](ports/supertux2/README.md) · [원 프로젝트](https://github.com/SuperTux/supertux) |
| `supertuxkart` | SuperTuxKart | Racing / PC | ➖ | ➖ | 🧪 기기 시험 전 | [가이드](ports/supertuxkart/README.md) · [원 프로젝트](https://github.com/supertuxkart/stk-code) |
| `torchlight` | 토치라이트 (Torchlight) | Action RPG / Xbox 360 Recomp | ➖ | ➖ | 🧪 기기 시험 전 | [가이드](ports/torchlight/README.md) · [포트 소스](https://github.com/liartes/torchlight-nx) |
| `undertale-yellow` | 언더테일 옐로우 (Undertale Yellow) | RPG / Decomp | ➖ | ➖ | 🧪 기기 시험 전 | [가이드](ports/undertale-yellow/README.md) · [포트 소스](https://github.com/NalienDev/Undertale-Yellow-NX) |
| `vcmi` | 히어로즈 오브 마이트 앤 매직 3 (VCMI) | Strategy / Modern Native | ➖ | ➖ | 🧪 기기 시험 전 | [가이드](ports/vcmi/README.md) · [포트 소스](https://github.com/NaGaa95/vcmi_nx) · [원 프로젝트](https://github.com/vcmi/vcmi) |
| `vf2` | 버추어 파이터 2 (Virtua Fighter 2) | Fighting / Model 2 Recomp | ➖ | ➖ | 🧪 기기 시험 전 | [가이드](ports/vf2/README.md) · [포트 소스](https://github.com/Thorhax/VF2-NX-Modern) |
| `virtual-on` | 전뇌전기 버추얼 온 (Cyber Troopers Virtual-On) | Arcade / Model 2 Recomp | ➖ | ➖ | 🧪 기기 시험 전 | [가이드](ports/virtual-on/README.md) · [포트 소스](https://github.com/Thorhax/Virtual-On-NX) |
| `zelda3t` | 젤다: 시간의 승리 (Zelda Time to Triumph) | ARPG / Fan Game | ➖ | ➖ | 🧪 기기 시험 전 | [가이드](ports/zelda3t/README.md) · [포트 소스](https://github.com/worthis/Zelda3T) · [원 프로젝트](https://github.com/worthis/Zelda3T) |
<!-- catalog:end -->

---

## 🚀 사용법 (Getting Started)

어느 포트든 같은 3단계입니다. 헤매지 않도록 무엇을 어디서 받아 어디에 둘지 명령 하나가 알려 줍니다.

```bash
git clone https://github.com/jshsakura/ns-ports.git && cd ns-ports
python3 build.py --list              # 포트 목록
python3 build.py guide <포트 ID>      # 1) 받아서 둘 것  2) 이미지 안내  3) 실행 명령
```

1. **받아서 둘 것**: `guide` 가 `ports/<id>/` 아래 빈 칸과 구하는 곳을 표로 보여 줍니다. NRO, 게임 데이터, 한글 패치 같은 파일을 각자 구해 그 위치에 둡니다. 포트 가이드(`ports/<id>/README.md`) 맨 위에도 같은 표가 있습니다.
2. **이미지**: 이 저장소에는 이미지가 없습니다. 앱 아이콘만 쓰이고(선택) `ports/<id>/icon.jpg` 에 **256x256 JPEG** 를 직접 구해 두면 적용됩니다. 안 두면 NRO 의 기본 아이콘이 나옵니다. 배너와 스크린샷은 다루지 않습니다.
3. **실행**: `python3 build.py <포트 ID> --zip`. 칸이 비어 있으면 실행 전에 같은 안내를 다시 보여 주고 멈춥니다. 결과는 `ports/<id>/dist/switch/<id>/` 와 zip 입니다. 폴더를 SD 카드 `sd:/switch/` 로 복사해 홈브루 메뉴에서 실행합니다.

예) 바람의 지휘봉 HD: [ports/wwhd/README.md](ports/wwhd/README.md)

```bash
python3 build.py guide wwhd
python3 build.py wwhd --rom /path/to/wwhd_dump --zip                        # 한글 판 (--rom 은 content/ 가 보이는 Wii U 덤프 루트)
python3 build.py wwhd --rom /path/to/wwhd_dump --variant original --zip     # 원본 그대로
```

> 소스 빌드 포트(`cstrike`, `openrct2`, `zelda3-ko`, `ge007`)는 Docker(devkitPro) 로 NRO 를 직접 빌드합니다. 골든아이 007 은 전용 빌더 저장소([goldeneye-007-switch](https://github.com/jshsakura/goldeneye-007-switch))가 사용자의 일본판 `baserom.j.z64` 를 받아 BPS 한글 패치를 적용해 빌드합니다.

### 내 파일로 새 포트 만들기
```bash
python3 build.py new mygame "내 게임 (My Game)" --nro /path/to/mygame.nro [--icon /path/to/icon.jpg]
python3 build.py guide mygame
python3 build.py mygame --rom /path/to/game-data --zip
```
덮어쓸 파일(한글 사전, 설정 등)은 `ports/mygame/overlay/` 에 같은 구조로 넣습니다.

---

## ⚖️ 저작권 및 법적 고지 (Legal Notice)

* 본 저장소는 원작 게임의 저작권 보호 파일(ROM, ISO, WAD, MPQ, 음원, 텍스처 등)을 일절 포함하지 않습니다.
* 모든 빌드 과정은 최종 사용자가 합법적으로 소유한 정품 게임 미디어로부터 로컬 환경에서 직접 에셋을 추출하고, 합법적인 차분 패치(BPS)를 결합하도록 설계되었습니다.
* 각 게임의 지적 재산권은 원작 개발사 및 유통사에 귀속됩니다.
