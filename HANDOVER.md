# NS Ports Hub - 프로젝트 인수인계 및 운영 가이드 (HANDOVER.md)

> **최종 갱신일:** 2026-10-18  
> **저장소:** [jshsakura/ns-ports](https://github.com/jshsakura/ns-ports)  
> **핵심 목적:** 닌텐도 스위치(Horizon OS / Atmosphère) 100% 한국어화 네이티브 포트 및 홈브루 자동 빌드·배포 허브

---

## 1. 프로젝트 구조 및 저장소 맵

### 1.1 주요 저장소 및 작업 디렉토리
* **메인 허브 (Monorepo):** `/home/jshsakura/workspace/ns-ports` (Git: `main`)
* **골든아이 007 전용 빌더:** [jshsakura/goldeneye-007-switch](https://github.com/jshsakura/goldeneye-007-switch)
* **스타크래프트 64 리컴파일:** `/home/jshsakura/app/sc64-korean`
* **홈브루 포트 후보 원천 목록:** `/home/jshsakura/app/ports/LIST.md`
* **SCUMM 고전 한글화 원본:** `/home/jshsakura/app/scumm-sources/`
* **OOT SoH v9.3.0 한글 HD 에셋 보관소:** `/mnt/HDD-8TB-STRIPE/media3/game/switch/homebrew-archive/zelda-oot-soh-930-assets/`
* **MM 2S2H v5.0.1 HD 에셋 보관소:** `/mnt/HDD-8TB-STRIPE/media3/game/switch/homebrew-archive/zelda-mm-2s2h-assets/`
* **스위치 실기 배포 스토리지:** `/mnt/HDD-8TB-STRIPE/media3/game/switch/homebrew/`
  * CookingFoil 서버(`oc-cookingfoil`)와 `.cookingfoil.json`을 통해 직접 연동 및 서비스

---

## 2. 수록 포트 현황 (35종 전원 레시피 완비 & 오카리나/무쥬라/폴아웃 실기 검증 완료)

모든 포트는 `ports.json`에 메타데이터가 등록되어 있으며, `ports/<id>/recipe.py`를 통해 규격화된 빌드/배포 로직을 제공합니다.

> **🎯 실기 검증 완료 (Verified In-Game):**
> 현재 카탈로그 상단 핵심 라인업(**`ge007`, `zelda3-ko`, `zelda-oot-hd`, `zelda-mm-hd`, `devilutionx`, `half-life`, `fallout1`, `fallout2`**)은 실기에서 한국어 번역, 폰트 출력, 조작성 검증이 100% 완료되었습니다.
> *(※ `zelda-oot-hd`: Ship of Harkinian v9.3.0 C 네이티브 + 3.89GB Pretendard HD 한글 에셋 + Japanese(3) 기본 언어 세팅 완료)*
> *(※ `zelda-mm-hd`: 2 Ship 2 Harkinian v5.0.1 C 네이티브 + 2.95GB MM-Reloaded v11.0.3 HD + Title ID 05BC5D84DDD7A000 동기화 완료)*

| 카테고리 | 등록 포트 ID | 주요 특징 및 한글화 방식 |
| :--- | :--- | :--- |
| **N64 / SNES Recomp** | `ge007`, `zelda3-ko`, `zelda-oot-hd`, `zelda-mm-hd`, `starcraft64` | Fast3D CJK 글리프 캐시 패치, 60FPS 자이로 조준, SoH v9.3.0 한글 HD, 2S2H v5.0.1 HD, 16:9 와이드스크린 (상위 5종 실기 검증 완료) |
| **GoldSrc / FPS** | `half-life`, `cstrike`, `doom64` | 하프라이프 공식 한국어 풀더빙 음성(실기 검증 완료), CS 1.6 오프라인 봇/한국어 UI, Doom64EX |
| **CRPG / Classic PC** | `fallout1`, `fallout2`, `devilutionx` | fallout1/2-ce CJK/CP949 FreeType 한글 & 1,000+ 대화 번역(실기 검증 완료), 디아블로 1 fonts.mpq(검증 완료) |
| **RTS / Strategy** | `war1gus`, `wargus`, `cnc`, `redalert`, `fheroes2` | Stratagus 엔진 워크래프트 1 & 2 에셋 연동, C&C 타이베리안 던/레드얼럿 풀 FMV, HOMM2 공식 한국어 팩 |
| **Simulation / City Builder** | `caesar3`, `openrct2`, `openttd` | 나눔고딕 TTF 폰트 및 한국어 lng 연동, 720p/1080p 터치 조작 |
| **Racing / Xbox 360 Recomp** | `nfsmw` | ReXGlue 정적 리컴파일 NFS 모스트 원티드 한국판(`nfsmw-nx-kor.nro`). 기기 시험 전 |
| **Xbox 360 Recomp / MMO** | `dantes-inferno`, `ro` | 단테스 인페르노 TU2 + 한글패치 리눅스 적용 도구(`tools/dante_kr_patch.py`), 라그나로크 스위치 클라이언트(기동 확인) |
| **Action / PS2 Decomp** | `sly1` | ProjectCane 0.5.0. 앱이 SD 의 ISO 를 직접 풀며 미국/유럽/일본판만 받는다. 한국판(`SCKA_200.04`)은 거절. 기기 시험 전 |
| **Action / Platformer** | `jak1`, `jak2`, `jak3`, `sonic1`, `sonic2`, `sonic-cd`, `jazz`, `cannonball` | OpenGOAL 소니 공식 한국어 더빙/자막(Jak 2/3), RSDKv4 공식 한국어(Language=8), Jazz2 C++ 엔진, OutRun 아케이드 |
| **Fan Game / Roguelite** | `pokemon-survivor-burst`, `dragonball-z-rpg`, `wwhd` | mkxp-z 커스텀 루비 3.1 런타임, 바람의 지휘봉 HD 네이티브 환경 |

---

## 3. 핵심 규칙 및 클린룸 원칙 (Clean-Room Policy)

1. **저작권 보호 파일 Git 커밋 절대 금지**
   * 상용 게임의 원작 ROM (`.z64`), CD 이미지, MPQ, WAD, DAT, 상용 오디오/비디오 파일은 레포지토리에 절대 포함하지 않습니다.
   * 레시피(`recipe.py`)는 사용자가 합법적으로 소유한 데이터를 마운트하거나, 배포 디렉토리(`--deploy`)로 폰트 및 설정 파일(`config.ini`, `.cfg`)만 생성하여 배포합니다.
2. **패치 배포는 순수 차분 파일(BPS/XDelta)만 사용**
   * 골든아이 007처럼 원본 변형이 필요한 경우, `patches/*.bps` 형태의 순수 차분 패치 파일만 포함하고 내장 순수 파이썬 BPS 엔진(`bps.py`)으로 무결성 검증 후 패치합니다.
3. **CookingFoil 메타데이터 동기화**
   * 배포 폴더에는 항상 `.cookingfoil.json`이 유지되어야 스위치 클라이언트가 폴더 모드로 인식하고 올바르게 다운로드/설치합니다.

---

## 4. CLI 사용법 및 검증 루틴

### 4.1 포트 목록 및 상태 확인
```bash
python3 build.py --list
```

### 4.2 개별 포트 빌드 및 배포
```bash
# 기본 레시피 정보 및 의존성 확인
python3 build.py fallout1

# ROM 지정 빌드 (골든아이 등 패치 지원 포트)
python3 build.py ge007 --rom /path/to/baserom.j.z64 --zip

# 스위치 SD 카드 또는 배포 디렉토리로 즉시 설치
python3 build.py fallout2 --deploy /mnt/HDD-8TB-STRIPE/media3/game/switch/homebrew/
```

### 4.3 전체 35개 레시피 일괄 회귀 테스트
```bash
python3 -c '
import json, subprocess, sys
with open("ports.json") as f:
    ports = json.load(f)
failed = [p["id"] for p in ports if subprocess.run([sys.executable, "build.py", p["id"]], capture_output=True).returncode != 0]
if failed:
    print(f"Failed: {failed}")
    sys.exit(1)
print(f"All {len(ports)}/{len(ports)} recipes passed verification!")
'
```

---

## 5. 향후 추가 대상 및 최적화 후보 (Next Pipeline Candidates)

1. **✅ [배포 완료] 젤다 무쥬라의 가면 2S2H v5.0.1 C 네이티브 교체 (`zelda-mm-hd`)**
   - 2Ship2Harkinian 5.0.1 (Battler Bravo) 네이티브 바이너리 + MM-Reloaded v11.0.3 HD 에셋(2.95GB) 배포 완료.
   - Title ID `05BC5D84DDD7A000` NSP 포워더 동기화 및 60FPS 360도 카메라 완비.
2. **SCUMM 고전 명작 한글화 포트 (`/home/jshsakura/app/scumm-sources/`)**
   - 텐타클 최후의 날 (Day of the Tentacle CD)
   - 원숭이 섬의 비밀 1 (The Secret of Monkey Island)
   - 풀 스로틀 (Full Throttle)
3. **대형 3D PC/콘솔 이식작**
   - **`vcmi_nx`**: 히어로즈 오브 마이트 앤 매직 3 (HOMM3)
   - **`openmw`**: 엘더스크롤 3 모로윈드 (The Elder Scrolls III: Morrowind)
   - **`sh2-nx` / `sh3-nx` / `sh4-nx`**: 사일런트 힐 2, 3, 4 네이티브 포트
   - **`MarathonRecomp-NX`**: 소닉 더 헤지혹 2006 (Sonic '06)
   - **`ProjectCane`**: 슬라이 쿠퍼 1 (Sly Cooper)
   - **`Undertale-Yellow-NX`**: 언더테일 옐로우
4. **아케이드 / 세가 라인**
   * **`Virtual-On-NX`**: 버추얼 온
   * **`Daytona-NX-Modern`**: 데이토나 USA
   * **`VF2-NX-Modern`**: 버추어 파이터 2
