# NX Ports Hub (nx-ports)

[![Platforms](https://img.shields.io/badge/platform-NX%20%7C%20Horizon%20OS%20(AArch64)-blue.svg)](https://github.com/jshsakura/nx-ports)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Ports](https://img.shields.io/badge/catalogued%20ports-30+-orange.svg)](ports.json)

NX(Horizon OS / Nintendo Switch) 환경을 위한 고전 명작 게임 **네이티브 홈브루 포트 통합 허브 & 레시피 컬렉션**입니다.

에뮬레이터를 통한 구동이 아닌, C/C++ 소스코드 디컴파일 및 역공학 프로젝트를 기반으로 포팅된 타이틀에 **한국어 번역 패치**와 **최신 1:1 카메라 자이로 조준(Motion Controls)**을 결합하여 완벽한 플레이 경험을 제공합니다.

---

## 🌟 핵심 특징

* **저작권 100% 안전 (Clean-room Rule)**
  * 원작 게임의 저작권 보호 대상(ROM, ISO, 상용 음원, 텍스처 등)을 일절 포함하지 않습니다.
  * 오픈소스 소스코드, 델타 패치(BPS), 오프라인 변환 레시피만을 제공합니다.
* **통합 원클릭 빌더 (`build.py`)**
  * 사용자가 소유한 정품 롬/데이터를 지정하면, 도커(`devkitpro/devkita64`)와 연동하여 자동으로 패치 적용 및 Switch NRO 패키징을 완료합니다.
* **CookingFoil 생태계 연동**
  * 자체 홈브루 서버인 [oc-cookingfoil](https://github.com/jshsakura/oc-cookingfoil)과 완벽하게 호환되는 메타데이터(`.cookingfoil.json`) 및 디렉토리 구조를 지원합니다.

---

## 🎮 포트 카탈로그 (Catalogued Ports)

| ID | 타이틀 | 카테고리 | 기반 엔진 | 한국어 | 자이로 | 레시피 상태 |
| :--- | :--- | :--- | :--- | :---: | :---: | :---: |
| **`ge007`** | **골든아이 007** | FPS / N64 | Fast3D PC Port (AArch64) | ✅ | ✅ | **[빌더 준비 완료](https://github.com/jshsakura/goldeneye-007-switch)** |
| **`zelda3-ko`** | **젤다: 신들의 트라이포스** | ARPG / SNES | zelda3 C re-implementation | ✅ | ➖ | 수록 완료 |
| **`sm64-hd`** | **슈퍼 마리오 64 HD** | Platformer / N64 | sm64-port (HD Texture pack) | ✅ | ✅ | 수록 완료 |
| **`zelda-oot-hd`** | **젤다: 시간의 오카리나 HD** | Action / N64 | Ship of Harkinian | ✅ | ✅ | 수록 완료 |
| **`zelda-mm-hd`** | **젤다: 무쥬라의 가면 HD** | Action / N64 | 2Ship2Harkinian | ✅ | ✅ | 수록 완료 |
| **`devilutionx`** | **디아블로 1 + 헬파이어** | ARPG / PC | DevilutionX | ✅ | ➖ | 수록 완료 |
| **`half-life`** | **하프라이프 1** | FPS / PC | Xash3D-FWGS (한국어 풀더빙) | ✅ | ✅ | 수록 완료 |
| **`cstrike`** | **카운터 스트라이크 1.6** | FPS / PC | CS16-client | ✅ | ✅ | 수록 완료 |
| **`fallout1`** | **폴아웃 1** | CRPG / PC | fallout1-ce | ✅ | ➖ | 수록 완료 |
| **`fallout2`** | **폴아웃 2** | CRPG / PC | fallout2-ce | ✅ | ➖ | 수록 완료 |
| **`cnc`** | **C&C: 타이베리안 던** | RTS / PC | Vanilla-Conquer (TD) | ✅ | ➖ | 수록 완료 |
| **`redalert`** | **C&C: 레드 얼럿** | RTS / PC | Vanilla-Conquer (RA) | ✅ | ➖ | 수록 완료 |
| **`war1gus`** | **워크래프트 1** | RTS / PC | Stratagus / War1gus | ➖ | ➖ | 수록 완료 |
| **`wargus`** | **워크래프트 2: BNE** | RTS / PC | Stratagus / Wargus | ✅ | ➖ | 수록 완료 |
| **`jak1`** | **잭 & 덱스터 1** | Platformer / PS2 | OpenGOAL | ➖ | ➖ | 수록 완료 |
| **`jak2`** | **잭 2** | Action / PS2 | OpenGOAL (한국어 음성) | ✅ | ➖ | 수록 완료 |
| **`jak3`** | **잭 3** | Action / PS2 | OpenGOAL (한국어 더빙/자막) | ✅ | ➖ | 수록 완료 |
| **`fheroes2`** | **히어로즈 오브 마이트 앤 매직 2** | TBS / PC | fheroes2 | ✅ | ➖ | 수록 완료 |
| **`caesar3`** | **시저 3** | Sim / PC | Julius (공식 한국어 패치) | ✅ | ➖ | 수록 완료 |
| **`openrct2`** | **롤러코스터 타이쿤 2** | Sim / PC | OpenRCT2 | ✅ | ➖ | 수록 완료 |
| **`openttd`** | **오픈 TTD** | Sim / PC | OpenTTD | ✅ | ➖ | 수록 완료 |
| **`doom64`** | **둠 64** | FPS / N64 | Doom64EX | ➖ | ✅ | 수록 완료 |
| **`starcraft64`**| **스타크래프트 64** | RTS / N64 | Title Takeover Forwarder | ➖ | ➖ | 수록 완료 |
| **`cannonball`** | **아웃런 (OutRun)** | Racing / Arcade | CannonBall (60FPS) | ➖ | ➖ | 수록 완료 |
| **`jazz`** | **재즈 잭래빗 2** | Platformer / PC | Jazz2-Native | ➖ | ➖ | 수록 완료 |
| **`sonic1`** | **소닉 더 헤지혹 1** | Platformer / Mobile | RSDKv4 Decomp | ➖ | ➖ | 수록 완료 |
| **`sonic2`** | **소닉 더 헤지혹 2** | Platformer / Mobile | RSDKv4 Decomp | ➖ | ➖ | 수록 완료 |
| **`sonic-cd`** | **소닉 CD** | Platformer / PC | RSDKv3 Decomp | ➖ | ➖ | 수록 완료 |
| **`pokemon-survivor-burst`** | **포켓몬 서바이버 버스트** | Fan Game | Custom Engine | ✅ | ➖ | 수록 완료 |
| **`dragonball-z-rpg`** | **드래곤볼 Z RPG** | Fan RPG | Custom | ✅ | ➖ | 수록 완료 |
| **`wwhd`** | **바람의 지휘봉 HD** | Action / GC | Custom Port | ✅ | ➖ | 수록 완료 |

---

## 🚀 사용법 (Getting Started)

### 1. 저장소 클론
```bash
git clone https://github.com/jshsakura/nx-ports.git
cd nx-ports
```

### 2. 지원 포트 목록 확인
```bash
python3 build.py --list
```

### 3. 특정 포트 빌드 (예: 골든아이 007)
사용자가 소유한 롬 파일을 넘겨주면, 한글화 BPS 패치 적용부터 사이드카 생성, NRO 컴파일, SD카드 배포판 생성까지 일괄 수행됩니다.

```bash
# 일본판 순정 롬 투입 (자동 한글 패치 + 빌드 + ZIP 패키징)
python3 build.py ge007 --rom /path/to/baserom.j.z64 --zip

# SD 카드 또는 CookingFoil 배포 디렉토리로 바로 복사
python3 build.py ge007 --rom /path/to/baserom.j.z64 --deploy /mnt/.../homebrew/
```

---

## ⚖️ 저작권 및 법적 고지 (Legal Notice)

* 본 저장소는 어떠한 형태의 저작권 보호 게임 바이너리(ROM, ISO, WAD, MPQ, 음원, 텍스처 등)도 호스팅하거나 배포하지 않습니다.
* 모든 빌드 과정은 최종 사용자가 합법적으로 소유한 정품 게임 미디어로부터 로컬 환경에서 직접 에셋을 추출하고 변환하도록 설계되었습니다.
* 닌텐도, 세가, 블리자드, 액티비전, 마이크로소프트, ID 소프트웨어 등 원작 권리사의 모든 지적 재산권을 존중합니다.
