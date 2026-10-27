# Freeware batch 2 (2026-10-27)

Branch `feat/freeware-batch2`, PR #7. 프리웨어/자유 배포 에셋만 쓰는 네이티브 포트 6종.
전부 `planned`(기기 시험 전), 샵 종류(kinds)·소개글은 이 문서 초안을 4.3에서 반영한다.

## 등록 목록

| id | 폴더 | 게임 | 소스 | 데이터 라이선스 |
|---|---|---|---|---|
| `supertux2` | `ports/supertux2` | 슈퍼 턱스 2 | theheroGAC/SuperTux-Milestone-2-Multi-Console 1.00 (릴리스 NRO) | GPLv3, NRO 롬FS 내장(120MB) |
| `supertuxkart` | `ports/supertuxkart` | 슈퍼 턱스 카트 | supertuxkart/stk-code 공식 1.5 switch.zip | GPL / CC-BY-SA, 776MB |
| `hurrican` | `ports/hurrican` | 허리케인 | rsn8887/Hurrican v1.04-Switch 릴리스 ZIP | 프리웨어(Poke53280), 풀패키지 |
| `zelda3t` | `ports/zelda3t` | 젤다: 승리의 시간 | worthis/Zelda3T 2.3, 릴리스 없어 devkitPro 도커(devkita64)로 로컬 빌드 | 무료 팬게임(zeldaroth.fr 3부작 완결), 586MB |
| `doukutsu-rs` | `ports/doukutsu-rs` | 동굴이야기 | doukutsu-rs 1.0.0 switch NRO + Studio Pixel `dou_1006.zip` | 프리웨어 원본 데이터 동봉 |
| `0ad` | `ports/0ad` | 0 A.D. | souldbminerr/0ad-switch r28-nx1 + 공식 `0ad-0.28.0-unix-data.tar.xz` | GPL / CC-BY-SA, 3.4GB |

## 조립 노트

- SuperTuxKart: 공식 ZIP의 `stk-data`를 `data/`로 옮겨 NRO 옆에 두면 엔진의 `./data/` 탐색 분기(`src/io/file_manager.cpp`)로 재빌드 없이 실행된다. 원래 경로 `sdmc:/stk-data/`는 샵 폴더 구조와 안 맞음.
- 0 A.D.: 엔진이 `sdmc:/switch/0ad/data/mods/` 를 하드코딩(`Paths.cpp`)해서 폴더 id를 `0ad`로 했다. 데이터가 `public.zip` 중심이라 파일 수는 적다.
- Zelda3T: 업스트림에 릴리스 바이너리가 없어 `make -f Makefile.switch` 로 직접 빌드(NRO 10.6MB). 데이터는 저장소 동봉 `data/` 를 그대로 배치.
- doukutsu-rs: 프리웨어 판정 기준 `Doukutsu.exe` + 추출된 `data/` 를 NRO 와 같은 폴더에 두면 첫 실행에 인식.
- Hurrican: 버튼 재매핑 메뉴는 업스트림 제약으로 동작 안 함(조작은 기본 매핑 사용).

## 샵 소개글 초안 (4.3 전달용)

### supertux2
- ko: 오픈소스 플랫폼머의 대표주자 슈퍼 턱스 2가 데이터 전체가 내장된 단일 NRO로. 720p 패드 최적화.
- en: The beloved open-source jump'n'run lands on Switch as one self-contained NRO. Full Milestone 2 campaign, 720p, gamepad-tuned controls.

### supertuxkart
- ko: 100% 무료 오픈소스 카트 레이싱, 공식 스위치 빌드 1.5. 스토리 모드/그랑프리/로컬 멀티 전부 무료.
- en: A fully free open-source kart racer from the official 1.5 Switch build. Story mode, grand prix and local multiplayer included.

### hurrican
- ko: 터러칸 계보의 프리웨어 점프 앤 슛. 9스테이지, 7종 무기 업그레이드.
- en: A Turrican-inspired freeware run'n'gun. Nine stages, seven weapons, complete data included.

### zelda3t
- ko: 젤다 팬게임 3부작의 완결편. 오니 링크의 시작, 하일리아인의 귀환에 이어 마지막 이야기.
- en: The finale of the beloved Zelda fan trilogy. After Oni Link Begins and Return of the Hylian, Time to Triumph completes the saga on Switch.

### doukutsu-rs
- ko: 2004년 프리웨어 전설 동굴이야기가 Rust 재구현 엔진으로 부활. 원작 데이터 그대로.
- en: The 2004 freeware legend Cave Story reborn through the doukutsu-rs engine, original data included.

### 0ad
- ko: 고대 문명 실시간 전략 시뮬레이션, 완전 무료 오픈소스. 릴리스 28 풀 데이터 포함.
- en: A completely free open-source RTS of ancient civilizations. Release 28 with the full official data pack.

## 검토했으나 제외한 후보

| 후보 | 사유 |
|---|---|
| Velikolepny Vovochka (worthis) | 재구현 엔진은 MIT 이나 원작 `Data.dat`/`movi.dat` 재배포 불가 |
| Castlevania ReVamped (bshurikan) | GameMaker 래퍼, 팬 게임 APK 를 별도로 받아야 함 |
| Touhou thWWW (saekaze) | 데이터를 itch.io 에서 받는 구조, 재배포 권한 불명확 |
| Mari0 / Mari0 AE | 번들 에셋에 SMB 원본 립 포함 |
| WipEout rewrite (emuman100) | 재배포권 불명확한 소니/Studio Liverpool 에셋 |
| AM2R | 닌텐도 DMCA 이력 |
| SRB2Kart / Ring Racers | 조건에 맞는 유지되는 스위치 빌드를 못 찾음 |

## 기기 시험 체크리스트 (planned → active 승급용)

- [ ] supertux2: 기동, 사운드(SDL_mixer/Tremor), 세이브 `userdata/` 기록
- [ ] supertuxkart: 기동(`./data/` 인식), 레이스 1바퀴, 로컬 멀티
- [ ] hurrican: 기동, 튜토리얼 크래시 여부(v1.04 수정됨), 사운드
- [ ] zelda3t: 기동, 신규 게임 시작, 세이브
- [ ] doukutsu-rs: 기동, 프리웨어 데이터 인식(첫 실행 자동 추출)
- [ ] 0ad: 기동(로딩 시간), 메뉴→게임 진입, 메모리
