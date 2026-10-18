# NS Korean Ports Hub (ns-ports)

[![Platforms](https://img.shields.io/badge/platform-NS%20%7C%20Horizon%20OS%20(AArch64)-blue.svg)](https://github.com/jshsakura/ns-ports)
[![Language](https://img.shields.io/badge/language-Korean%20(100%25)-red.svg)](README.md)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Ports](https://img.shields.io/badge/native%20ports-31-orange.svg)](ports.json)

**닌텐도 스위치(NS / Horizon OS) 환경을 위한 명작 게임 한국어화(Korean) 네이티브 포트 전문 컬렉션**입니다.

모든 타이틀은 단순 에뮬레이션 구동이 아닌, C/C++ 소스코드 디컴파일 및 역공학 프로젝트를 기반으로 포팅되었으며, **완벽한 한국어 번역(자막/음성), 한글 폰트 렌더러(CJK/TTF), 모션 컨트롤(자이로 조준)**을 기본 탑재하고 있습니다.

---

## 🌟 핵심 특징

* 🇰🇷 **100% 한국어화 전용 포트**
  * 수록된 모든 게임은 한국어 자막, 공식 한국어 더빙, 유저 한국어화 패치 연동을 전제로 제작 및 관리됩니다.
  * 한글 폰트 깨짐/중복 렌더링 버그(골든아이 Fast3D 캐시 버그 등)를 자체 엔진 패치로 해결.
* ⚖️ **저작권 100% 클린룸 (Clean-room Rule)**
  * 원작 게임의 저작권 보호 대상(ROM, ISO, 상용 음원, 텍스처 등)을 일절 포함하지 않습니다.
  * 순정 정품 롬/데이터를 지정하면, 내장된 BPS/XDelta 패처가 자동으로 한글 롬을 생성하여 컴파일합니다.
* 🛠️ **원클릭 자동 빌더 (`build.py`)**
  * `python3 build.py <포트ID> --rom <파일>` 한 줄로 한글 패치 적용, 에셋 변환, Switch NRO 패키징까지 일괄 수행.
* 📦 **CookingFoil 생태계 완벽 호환**
  * 자체 홈브루 서버인 [oc-cookingfoil](https://github.com/jshsakura/oc-cookingfoil) 메타데이터(`.cookingfoil.json`) 자동 연동.

---

## 🎮 네이티브 포트 카탈로그 (31 Games)

| ID | 타이틀 | 장르 / 원작 | 한국어화 형태 | 자이로 | 구동 및 레시피 상태 |
| :--- | :--- | :--- | :--- | :---: | :---: |
| **`ge007`** | **골든아이 007** | FPS / N64 | 100% 한글 자막 (v1.0 retrace) | ✅ | 🎯 **실기 검수 완료** ([빌더 준비 완료](https://github.com/jshsakura/goldeneye-007-switch)) |
| **`zelda3-ko`** | **젤다: 신들의 트라이포스** | ARPG / SNES | C 디컴파일 60fps & 16:9 한글화 | ➖ | 🎯 **실기 검수 완료** |
| **`sm64-hd`** | **슈퍼 마리오 64 HD** | Platformer / N64 | 한글 폰트 + HD 고해상도 텍스처팩 | ✅ | 🎯 **실기 검수 완료** |
| **`zelda-oot-hd`** | **젤다: 시간의 오카리나 HD** | Action / N64 | SoH v9.3.0 + 한글 Pretendard HD | ✅ | 🎯 **실기 검수 완료** |
| **`zelda-mm-hd`** | **젤다: 무쥬라의 가면 HD** | Action / N64 | 와이드스크린 고해상도 & 한글 텍스트 | ✅ | 🎯 **실기 검수 완료** |
| **`devilutionx`** | **디아블로 1 + 헬파이어** | ARPG / PC | 한글 폰트 + 완벽 한글 자막 | ➖ | 🎯 **실기 검수 완료** |
| **`half-life`** | **하프라이프 1** | FPS / PC | **공식 한국어 풀더빙 음성 & 자막** | ✅ | 🎯 **실기 검수 완료** |
| **`cstrike`** | **카운터 스트라이크 1.6** | FPS / PC | 한글 폰트 & 한글 UI/라디오/봇 | ✅ | 📦 레시피 수록 완료 |
| **`fallout1`** | **폴아웃 1** | CRPG / PC | fallout1-ce CJK 폰트 엔진 + 한글화 | ➖ | 🎯 **실기 검수 완료** |
| **`fallout2`** | **폴아웃 2** | CRPG / PC | fallout2-ce CP949 FreeType 한글 | ➖ | 🎯 **실기 검수 완료** |
| **`cnc`** | **C&C: 타이베리안 던** | RTS / PC | C&C Gold 한글 폰트 & 미션 브리핑 | ➖ | 📦 레시피 수록 완료 |
| **`redalert`** | **C&C: 레드 얼럿** | RTS / PC | 한글화 연합군/소련군 캠페인 | ➖ | 📦 레시피 수록 완료 |
| **`war1gus`** | **워크래프트 1: 오크와 인간** | RTS / PC | War1gus Stratagus 원작 에셋 연동 | ➖ | 📦 레시피 수록 완료 |
| **`wargus`** | **워크래프트 2: BNE** | RTS / PC | 워크래프트 2 완벽 한글화 데이터 | ➖ | 📦 레시피 수록 완료 |
| **`starcraft64`** | **스타크래프트 64 Recomp** | RTS / N64 | StarCraft 64 정적 리컴파일 한국어판 | ➖ | 📦 레시피 수록 완료 |
| **`jak1`** | **잭 & 덱스터 (Jak 1)** | Action / PS2 | OpenGOAL 60fps 와이드스크린 | ➖ | 📦 레시피 수록 완료 |
| **`jak2`** | **잭 2 (Jak II)** | Action / PS2 | **소니 공식 한국어 음성 더빙** | ➖ | 📦 레시피 수록 완료 |
| **`jak3`** | **잭 3 (Jak 3)** | Action / PS2 | **소니 공식 한국어 음성 & 자막** | ➖ | 📦 레시피 수록 완료 |
| **`fheroes2`** | **히어로즈 오브 마이트 앤 매직 2** | TBS / PC | fheroes2 공식 한국어 팩 지원 | ➖ | 📦 레시피 수록 완료 |
| **`caesar3`** | **시저 3 (Julius)** | Sim / PC | 시저 3 공식 한국어화 데이터 | ➖ | 📦 레시피 수록 완료 |
| **`openrct2`** | **롤러코스터 타이쿤 2** | Sim / PC | OpenRCT2 한글 폰트 & 자막 | ➖ | 📦 레시피 수록 완료 |
| **`openttd`** | **오픈 TTD** | Sim / PC | OpenTTD 나눔고딕 한글 번역 | ➖ | 📦 레시피 수록 완료 |
| **`sonic1`** | **소닉 더 헤지혹 1 (2013)** | Platformer / RSDK | RSDKv4 디컴파일 공식 한국어(Lang=8) | ➖ | 📦 레시피 수록 완료 |
| **`sonic2`** | **소닉 더 헤지혹 2 (2013)** | Platformer / RSDK | RSDKv4 디컴파일 공식 한국어(Lang=8) | ➖ | 📦 레시피 수록 완료 |
| **`sonic-cd`** | **소닉 CD (2011)** | Platformer / RSDK | RSDKv3 디컴파일 60fps 와이드스크린 | ➖ | 📦 레시피 수록 완료 |
| **`cannonball`** | **아웃런 (Cannonball)** | Racing / Arcade | 60fps 아케이드 재구현 엔진 | ➖ | 📦 레시피 수록 완료 |
| **`jazz`** | **재즈 잭래빗 2** | Platformer / PC | Jazz² Resurrection C++ 엔진 | ➖ | 📦 레시피 수록 완료 |
| **`doom64`** | **둠 64 EX** | FPS / N64 | Doom64EX C++ 네이티브 포트 | ➖ | 📦 레시피 수록 완료 |
| **`pokemon-survivor-burst`** | **포켓몬 서바이버 버스트** | Fan Game | [한국어 홈브루 포트](https://github.com/jshsakura/psb-switch) | ➖ | 📦 레시피 수록 완료 |
| **`dragonball-z-rpg`** | **드래곤볼 Z RPG** | Fan RPG | 한글 자막 지원 | ➖ | 📦 레시피 수록 완료 |
| **`wwhd`** | **바람의 지휘봉 HD** | Action / GC | 젤다 바람의 지휘봉 한글 텍스처 | ➖ | 📦 레시피 수록 완료 |

---

## 🚀 사용법 (Getting Started)

### 1. 저장소 클론
```bash
git clone https://github.com/jshsakura/ns-ports.git
cd ns-ports
```

### 2. 한국어 지원 포트 목록 확인
```bash
python3 build.py --list
```

### 3. 포트 빌드 예시 (골든아이 007)
사용자가 소유한 일본판 순정 롬을 지정하면, **내장된 한국어 BPS 패치를 자동으로 적용**하여 한글판 NRO를 완성합니다.

```bash
# 일본판 순정 롬 투입 (자동 한글 패치 + 빌드 + ZIP 패키징)
python3 build.py ge007 --rom /path/to/baserom.j.z64 --zip

# 스위치 SD 카드 또는 CookingFoil 배포 폴더로 즉시 배포
python3 build.py ge007 --rom /path/to/baserom.j.z64 --deploy /mnt/.../homebrew/
```

---

## ⚖️ 저작권 및 법적 고지 (Legal Notice)

* 본 저장소는 원작 게임의 저작권 보호 파일(ROM, ISO, WAD, MPQ, 음원, 텍스처 등)을 일절 포함하지 않습니다.
* 모든 빌드 과정은 최종 사용자가 합법적으로 소유한 정품 게임 미디어로부터 로컬 환경에서 직접 에셋을 추출하고, 합법적인 차분 패치(BPS)를 결합하도록 설계되었습니다.
* 각 게임의 지적 재산권은 원작 개발사 및 유통사에 귀속됩니다.
