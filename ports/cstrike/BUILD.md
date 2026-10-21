# 카스 신형 빌드 통합 문서

작업 폴더는 `~/app/cstrike-modern/` 하나다. 소스는 `src/`, 참고물은 `ref/`, 산출물은 `out/`.
/tmp 에 두지 않는다. 배경과 현재 서버 상태는 `README.md`.

## 결론: 가능해 보인다 (2026-10-18 소스로 확인, 빌드는 아직 안 함)

신형 엔진(FWGS)에는 **공식 스위치 빌드**가 있고, 게임 로직은 `.so` 로 따로 로드한다(libsolder).
하프라이프가 그 구조다. 카스도 같은 구조로 만들면 된다.

| 조각 | 소스 | 산출물 |
|---|---|---|
| 엔진 + 메뉴 + 렌더러 | `src/xash3d-fwgs` (`--nswitch`) | `xash.nro`, `libmenu.so`, `libref_gl.so`, `filesystem_stdio.so` |
| 카스 서버 로직 | `src/cs16-client/3rdparty/ReGameDLL_CS` (Velaron 포크, android 브랜치 기준 ARM 빌드 존재) | `cs_nswitch_arm64.so` |
| 카스 클라이언트 | `src/cs16-client` (`cl_dll`) | `client_nswitch_arm64.so` |
| 봇 | `src/cs16-client/3rdparty/yapb` | yapb `.so` + 그래프(`scripts/yapb_graph_dl.py`) |
| 메뉴 UI | `src/cs16-client/3rdparty/mainui_cpp` | menu `.so` |
| .so 로더 | `libsolder` (fgsfdsfgs, 아직 안 받음) | 엔진이 링크 |

## 키보드가 되는 이유 (확인한 것)

- 신형 엔진 NRO(`half-life.nro`)에는 `SWITCH_StartTextInput` 등 67개 문자열이 있고, 서버의 구 카스 NRO(`switchports` v1.0.1)에는 0개다.
- 신형 엔진 빌드의 menu/텍스트 입력이 이 경로를 쓰는지는 빌드 후 기기에서 확인한다.

## 빌드 환경

- 툴체인: docker 이미지 `devkitpro/devkita64:latest` 가 **이미 로컬에 있다** (2.79GB). apt/download.devkitpro.org 는 막혀 있어 이 이미지를 쓴다.
- 엔진 빌드 절차의 정본: `src/xash3d-fwgs/scripts/gha/build_nswitch_docker.sh`, 의존성은 `deps_nswitch.sh`.
  핵심 환경: `-march=armv8-a+crc+crypto -mtune=cortex-a57 -mtp=soft -fPIC -ftls-model=local-exec`, `-D__SWITCH__`, `./waf configure -T release --nswitch`.
- 게임 .so 를 만드는 방식의 본보기: 같은 스크립트의 `build_hlsdk()` (hlsdk-portable 을 `./waf configure -T release --nswitch --disable-werror`).
  ReGameDLL_CS 는 CMake 라 같은 컴파일러 환경변수로 크로스 설정이 필요하다.
- 비교 본보기: cs16-client 의 PS Vita 빌드(`cmake --preset psvita-release`, `.github/workflows/build.yml`)가 콘솔 크로스의 선례다.

## 순서

1. libsolder 를 받아 컨테이너 안에서 빌드, 엔진을 `--nswitch` 로 빌드 (먼저 이 단계가 하프라이프와 같은 NRO 를 재현하는지 본다)
2. ReGameDLL_CS 를 aarch64 크로스로 빌드해 `cs_nswitch_arm64.so` 를 만든다 (**최대 미확인 항목**)
3. cs16-client 의 `cl_dll`, mainui, yapb 를 같은 방식으로 빌드
4. `out/cstrike-new/` 에 서버 폴더와 같은 레이아웃으로 조립 (기존 `cstrike/`, `valve/` 데이터 재사용)
5. 기기에서 시험: 시작, 멀티플레이 화면 텍스트 입력, 봇
6. 통과하면 서버 `homebrew/cstrike/` 에 올린다. **현재 `cstrike.nro` 와 `.orig` 는 지우지 않는다.** (홈브류 폴더 앱이라 합산 해시가 바뀌면 기기에 갱신으로 보인다)

## 주의

- 서버의 운영 파일은 기기 시험 전에는 건드리지 않는다.
- 기기 시험은 포워더로 한다 (hbmenu 앨범 모드는 메모리가 작아 의미 없음, `PORTS-VS-RETRO.md`).
- 크래시가 나면 보고서의 Module Id 와 NRO 헤더 0x40 빌드 ID 를 먼저 맞춘다.
- 모르는 것은 추측으로 적고 확인된 것과 구분한다.

## 진행 기록

- 2026-10-18 1단계 완료: `scripts/build-engine.sh` (docker devkita64)로 엔진 `--nswitch` 빌드 성공.
  `out/engine/` 에 xash.nro(12.5MB), libmenu.so, libref_gl.so, filesystem_stdio.so, valve/extras.pk3.
  xash.nro 에 swkbd 문자열 67개, `SWITCH_StartTextInput` 있음 (서버의 하프라이프 NRO 와 같은 계열).
  실행: `docker run --rm -e HOST_UID=$(id -u) -e HOST_GID=$(id -g) -v $PWD/src:/work -v $PWD/out:/work/out -v $PWD/scripts:/work/scripts -w /work devkitpro/devkita64:latest bash /work/scripts/build-engine.sh`
- 2026-10-18 2~4단계 완료 (빌드만, 기기 시험 전):
  `scripts/build-cs.sh` 로 cs16-client 전체(ReGameDLL_CS, 클라이언트, yapb)를 devkita64 에서 크로스 빌드.
  산출물 `out/cs/`: cs_nswitch_arm64.so(2.5MB), client_nswitch_arm64.so(1MB), yapb_nswitch_arm64.so(1.5MB).
  조립본 `out/overlay/` 는 서버의 `homebrew/cstrike/` 위에 덮어쓸 파일만 담았다 (게임 데이터 550MB 는 재사용):
  `xash.nro`, `libmenu.so`, `libref_gl.so`, `filesystem_stdio.so`, `valve/extras.pk3`,
  `cstrike/dlls/cs_nswitch_arm64.so`, `cstrike/cl_dlls/client_nswitch_arm64.so`, `cstrike/addons/yapb/bin/yapb_nswitch_arm64.so`.
  크로스 빌드를 위해 소스에 건 패치는 `patches/*.patch`, 툴체인은 `scripts/switch-toolchain.cmake`, 없는 헤더 shim 은 `scripts/shim/`, 엔진이 안 내보내는 libc 심볼 대체는 `scripts/switch_stubs.c`.
  미해결 심볼 검증: 엔진 elf(`src/xash3d-fwgs/build/engine/xash`)의 `nm -D --defined-only` 와 각 .so 의 `--undefined-only` 를 비교해 NRO 가 못 주는 것이 0개인 것까지 확인했다.

## 알려진 위험 (기기 시험에서 확인)

- `dlopen/dlsym` 등과 `access/unlink` 계열은 "없음" 으로 응답하는 임시 구현이다. 봇(yapb)의 그래프 로드, 게임 DLL 의 모듈 탐색이 이 때문에 막힐 수 있다.
- yapb 그래프 데이터(`addons/yapb/data/graph`)는 조립본에 아직 넣지 않았다 (`scripts/yapb_graph_dl.py` 가 받아 두었을 수 있음, 확인 필요).
- 메뉴는 cs16 의 mainui 가 아니라 엔진 기본 `libmenu.so` 를 쓴다. 카스 전용 메뉴가 필요하면 `BUILD_MAINUI=ON` 으로 따로 시도한다.
- 서버 운영 폴더에는 올리지 않았다. 기기 시험은 SD 에 `switch/cstrike-new/` 를 따로 만들어 서버 폴더 내용 + overlay 를 복사해서 한다.
- 2026-10-18 서버 업로드: `<homebrew>/cstrike-new/` (기존 `cstrike/` 는 그대로).
  엔진은 `GAMEDIR=cstrike ENGINE_OUT=engine-cstrike` 로 다시 빌드해 `-game` 인자 없이 카스가 뜨게 했다(`out/engine-cstrike/`).
  NRO 이름은 `cstrike-new.nro`, 게임 데이터는 기존 폴더에서 하드링크(`cp -al`)로 가져와 디스크를 더 쓰지 않는다.
  yapb 그래프 데이터는 아직 없어서 봇은 맵 정보 없이 시험된다.
  시험 결과가 좋으면 `cstrike/` 를 대체하고 `cstrike-new/` 를 지운다. 안 좋으면 `cstrike-new/` 만 지우면 된다.
- 2026-10-18 오후 수정판 (여전히 기기 구동 실패 보고를 받은 뒤, 원인은 아직 미확인):
  * dl* 임시 구현을 없애고 `shim/dlfcn.h` 가 엔진이 내보내는 `solder_dl*` 로 잇게 했다. ctype 은 엔진이 내보낸다(isdigit 만 stub). `_Unwind_Resume` stub 은 엔진 것을 가리므로 뺐다.
  * yapb(봇)는 inline detour(x86 전용)를 쓰므로 ARM 에서 불가. `-DNO_YAPB=ON` 으로 뺐다 => 이 빌드에는 봇이 없다 (옛 통짜 NRO 에는 있었음).
  * `scripts/make-nro.py` 로 NRO 의 ASET 을 교체: 아이콘은 옛 `cstrike.nro` 의 것(`ref/old-cstrike-icon.jpg`), 이름은 "Counter-Strike 1.6 실험판".
  * 서버 `homebrew/cstrike-new/` 를 갱신하고 `kinds.json` 에 port 로 등록, 서버 컨테이너를 재시작해 도구에서 포트로 옮겼다.
- 2026-10-18 진단용 로그: 엔진이 스위치에서 항상 `engine.log` 를 NRO 가 있는 폴더(`sdmc:/switch/cstrike-new/engine.log`)에 버퍼 없이 남긴다 (`patches/xash3d-fwgs.patch`).
  크래시 리포트가 없을 때 어디까지 실행됐는지 이 파일로 본다. 원인을 찾으면 이 패치는 유지해도 된다(로그는 가볍다).
- 2026-10-18 구동 실패 원인(기기 `fatal.log`: `Host_InitCommon: couldn't load gfx.wad`):
  엔진을 `--gamedir=cstrike` 로 빌드하면 엔진의 basedir(`host.default_gamedir`)까지 cstrike 가 되어 `valve/gfx.wad` 가 검색 경로에 안 들어간다.
  basedir 는 valve 로 두고(기본 빌드), `filesystem_engine.c` 의 FS_Init 에서 `-game` 이 없을 때 스위치는 `cstrike` 를 실행 게임으로 고르게 패치했다 (`patches/xash3d-fwgs.patch`).
  => 이 엔진은 `GAMEDIR` 없이 빌드한다 (`ENGINE_OUT=engine-cstrike` 만 지정).
- 2026-10-18 교체 완료: 서버 `homebrew/cstrike/` 를 새 엔진 빌드로 바꿨다 (기기에서 키보드 입력이 잘 되는 것을 확인한 뒤).
  * 해상도는 `cstrike/cstrike/config.cfg` 끝에 하프라이프와 같은 값(`width 1280`, `height 720`, `vid_mode "1280 720"`, `fullscreen 0`, `gl_widescreen_yfov 1`)을 덧붙였다. 효과는 기기에서 확인 전이다.
  * NRO 이름과 아이콘은 옛 항목의 것("카운터 스트라이크 1.6 (Counter-Strike 1.6)"). 옛 `cstrike.nro` 와 `.orig` 는 라이브러리 밖 `ref/old-nro/` 로 옮겨 두었다(되돌릴 때용).
  * `cstrike-new/` 폴더와 그 종류/미디어/바로가기 항목은 지웠다. 봇(yapb)은 이 빌드에 없다.
- 2026-10-18 화면 잘림(Switch Lite 에서 1080p 화면의 좌하단만 보임): `VID_SetMode` 에서 스위치는 저장된 width/height 를 무시하고 `appletGetOperationMode()` 로 휴대 1280x720, 독 1920x1080 을 고르게 패치했다 (`patches/xash3d-fwgs.patch`). config.cfg 의 해상도 값은 이제 쓰이지 않는다.
- 2026-10-18 화면 잘림 2차: 기기 `engine.log` 에 `Window mode: fullscreen desktop`, `Window size: 1920x1080` 이 찍혀 있었다. 크기를 1280x720 으로 요청해도 fullscreen desktop 이면 SDL 이 데스크톱 모드(1080p)를 쓴다.
  `VID_SetMode` 에서 스위치는 창 모드(windowed)로 고정하도록 추가 패치했다 (하프라이프 config 의 `fullscreen 0` 과 같은 방식). 기기의 옛 `video.cfg` 가 fullscreen 2 를 저장해 두었어도 덮어쓴다.
  로그에 `Error: native object "MenuFactory" is unavailable` 도 있다 (메뉴는 뜨므로 우선순위 낮음, 원인 미확인).
- 2026-10-18 한글판 1단계 (기기 확인 전):
  * 스위치 빌드는 `ui_language` 를 `koreana` 로 고정한다 (`FS_LoadVFSConfig`, 기기에 저장된 영어 vfs.cfg 도 무시).
  * 메뉴(`libmenu.so`, 엔진의 3rdparty/mainui)의 글자 판에 KS X 1001 한글 2350자를 추가했다 (`patches/mainui-ksx.patch`, `font/KsxTable.h`). 판은 자동으로 커진다.
  * 메뉴 글꼴 `gfx/fonts/FiraSans-Regular.ttf`, `tahoma.ttf` 를 한글 포함 글꼴(Gothic A1, OFL)로 `cstrike/gfx/fonts/` 에 덮었다.
  * 하프라이프 데이터의 `gameui_korean(a).txt`, `valve_korean(a).txt` 를 `valve/resource/` 에 복사했다. 게임 안 문구는 `cstrike/resource/cstrike_koreana.txt`.
  * 아직 안 한 것: 게임 안 HUD/채팅 글꼴(cs16-client), 한글 이름 입력 표시. 기기에서 메뉴를 먼저 확인한다.
- 2026-10-18 "메뉴가 여전히 영어" 보고의 재확인: 그 테스트 로그(14:26 시작, 14:31 붙여넣음)는 한글 빌드 업로드(14:38) 이전 것이다.
  기기는 14:40 에 23.9MB 갱신을 받았다(서버 도커 로그). 새 빌드 재시험과 새 engine.log 가 필요하다.
  메인 메뉴 버튼은 mainui 가 `GameUI_*` 토큰으로 그리므로 gameui_koreana.txt 만으로 한국어가 나와야 정상.
  mainui 고유 문구 사전 `resource/mainui_koreana.txt` 는 어디에도 없다(영어판도 없음) = 서브 메뉴 일부 문구는 영어로 남는다.
- 2026-10-18 데이터 한글패치 적용: 유저가 찾은 팬 한패(신형, CS:S 한국어 파일 기반 무전 보완)의 `titles.txt` 를
  UTF-8/CRLF 로 정리해 서버 `cstrike/titles.txt` 로 교체했다 (`ref/korean-patches/titles-ko-new.txt`, 원본 영어 백업 `ref/server-backups/titles.txt.orig-en`).
  `#Cstrike_TitlesTXT_*` 참조는 cs16-client 의 vgui_parser 가 ui_language=koreana 로 `cstrike_koreana.txt` 사전에서 푼다(토큰 존재 확인).
  구버전 패치 zip(허브 제작, `ref/korean-patches/old-ver/`)은 확인용으로만 보관.
- 2026-10-18 게임 안 HUD/채팅 한글 렌더링 = 엔진 TTF 글꼴 추가 (기기 확인 전):
  * 문제: HUD 글자는 엔진 `pfnDrawCharacter` → `creditsFont`(256글자 비트맵 .fnt) 로 그려져 한글 불가. 콘솔 글꼴도 같음.
  * 해결: 엔진 `cl_font.c` 에 stb_truetype(mainui 것과 같은 헤더)로 TTF 를 굽는 `FONT_TRUETYPE` 경로를 추가.
    시작 시 `cstrike/gfx/fonts/tahoma.ttf`(Gothic A1) 에서 ASCII + KS X 1001 2350자를 2048x1024 아틀라스로 1회 베이크(검은 1px 외곽선 포함).
    HUD 글꼴 16px(`cl_scrn.c`), 콘솔 글꼴 14+4n px(`console.c`).
  * UTF-8 경로: `Con_RunConsole` 에서 스위치는 con_charset=utf8, cl_charset=utf-8, hud_utf8=1 을 매 프레임 강제(기존 config.cfg 값 무시).
    `Con_UtfProcessCharForce` 는 코드페이지 없음(codepage 0)일 때 코드포인트를 그대로 돌려준다. 비트맵 글꼴엔 255 초과시 '?' 가드.
  * 클라이언트(cs16-client)는 수정 불필요: 바이트별 `pfnDrawCharacter` 호출을 엔진이 UTF-8 로 조립한다.
    길이 재기는 hud_textmode=0(기본)이면 엔진 콘솔 글꼴로 재므로 한글 폭도 정확.
  * 빌드/업로드: 엔진만 재빌드(15:10), ASET 이름/아이콘은 기존과 동일하게 make-nro.py 로 넣어 서버 `homebrew/cstrike/cstrike.nro` 교체.
    `patches/xash3d-fwgs.patch` 갱신(560줄). libmenu/libref_gl/filesystem_stdio 는 재빌드됐지만 서버에는 안 올렸다(변경 없음, 전송량 절약).
- 2026-10-18 mainui 한국어 사전 작성/배포: `resource/mainui_koreana.txt` 가 어디에도 없어(업스트림 번역 없음) 스켈레톤(_everything) 기준으로 272개 토큰을 번역해
  서버 `cstrike/resource/mainui_koreana.txt` 로 배포 (`ref/korean-patches/mainui_koreana.txt` 원본).
  토큰 키 = 영어 원문 또는 GameUI_*/StringsList_NNN. gameui_koreana.txt 가 못 덮는 GameUI 4개(PlayGame_Alt, RawInput, RawInputLabel, VSync)도 포함.
  StringsList_NNN 원문은 mainui MenuStrings.cpp 배열 주석(188,189,191,192,193,234,240,400,530)에서 확인했다.
- 2026-10-18 한글 이름 입력 조사 (코드 변경 불필요로 판명, 기기 확인 대기):
  * 스위치 SDL2 포트는 swkbdInline + SwkbdType_Normal(0) 로 키보드를 띄운다. 콘솔 시스템 언어가 한국어면 한글 자판 사용 가능.
  * 입력 흐름: SDL_TEXTINPUT(UTF-8) → SDLash_InputEvent 가 바이트별 CL_CharEvent (cl_charset=utf-8 강제 덕에 변환 없이 통과)
    → mainui CMenuField::Char 는 32 미만만 걸러내고 바이트를 그대로 쌓는다(UTF-8 커서 이동 인식도 있음). 렌더링은 KS X 패치가 들어간
    mainui 폰트(Gothic A1)라 한글 표시 가능. 게임 내 채팅 입력줄은 엔진 key_message 콘솔 글꼴(신규 TTF)로 그려진다.
  * 참고: PlayerSetup 이름 필드 iMaxLength=32 바이트 = 한글 약 10자. 짧으면 libmainui 재빌드로 늘릴 수 있다(보류, 기기 시험 후 일괄).
- 2026-10-18 게임패드 기본 배정 (기존 기기 설정은 건드리지 않는 방식):
  * 구조: SDL(Nintendo 배치 스왑, `joy_sdl2.c`) → 엔진 키(A_BUTTON 등) → config.cfg 의 bind. 스틱/트리거 축은 bind 없이 왼쪽=이동/오른쪽=시야.
  * 문제: 엔진이 키 기본 배정 테이블(`in_keys.c` keynames[])이 있어도 config.cfg 의 `unbindall` 이 게임패드 배정까지 지운다.
    지금 기기에서 버튼이 동작하는 건 옛 switchports 엔진이 기기 config.cfg 에 쓴 배정이 살아 있어서(서버 config.cfg 에는 버전 배정 없음).
  * 조치: `host.c` 에 NSWITCH 전용 블록. config/userconfig 실행 뒤 게임패드 배정이 하나도 없으면(신규 설치 등) 기본 배정 설치.
    기존 기기처럼 이미 배정이 있으면 아무 것도 안 함. 기본값:
    ZR=발사, ZL=보조발사, A=사용, B=점프, X=재장전, Y=앉기, R1=직전 무기(Q), L1=걷기,
    십자↑=수류탄(slot4), ↓=칼(slot3), ←/→=무기 앞뒤, START=메뉴, BACK=팀 변경.
  * 빌드/업로드: 엔진 재빌드, NRO 교체(md5 f7924122), `patches/xash3d-fwgs.patch` 갱신(596줄).
- 2026-10-18 TTF 빌드 시작 크래시 수정 (기기 보고 "시작하자마자 뒤짐"):
  * 원인: 콘솔 글꼴 TTF 로드가 `Con_Init` 시점(Host_Init 초반)에 돌면서 그때까지 할당되지 않은 `cls.mempool`(클라이언트 DLL 로드 뒤에 생김)으로 Mem_Calloc → 즉사.
  * 수정: TTF 전용 풀 `CL_TTFPool()`(lazy 생성)로 교체. 아틀라스 행 바꿈 후 바닥 초과 재검사 가드도 추가(미할당 cov 해제 실수는 제거).
  * 재빌드/업로드: NRO 교체(md5 569c265e), 패치 615줄.
- 2026-10-18 한글 "다 깨짐+겹침" 수정 (기기 보고, 21:36 로그):
  * 로그 확인: `valve_koreana/`, `cstrike_koreana/` 마운트 = 언어 고정 정상. 깨짐은 렌더링 문제.
  * 원인: HUD 글꼴(16px)과 콘솔 글꼴(14/18/22px)이 텍스처 이름을 공유(`*ttf_gfx/fonts/tahoma.ttf`).
    렌더러가 이름으로 텍스처를 캐시하므로 두 번째 글꼴이 첫 번째 아틀라스를 재사용 → 제 좌표를 남의 아틀라스에 대입 →
    로딩 화면/콘솔 글자가 엉키고 겹쳐 보임.
  * 수정: 텍스처 이름을 인스턴스+크기별 고유값(`*ttf_<ptr>_<px>`)으로. charHeight 에 외곽선+여백(+4px) 포함(줄 겹침 방지).
  * 재빌드/업로드: NRO 교체(md5 43a910c0), 패치 619줄.
- 2026-10-18 밤 기기 확인: **한글 렌더링 정상화 확인** (사용자 보고 "글씨깨짐 해결됐고"). 텍스처 이름 충돌이 원인이었음이 확정.
- 2026-10-18 글자 높낮이(베이스라인) 수정: 깨짐은 나았지만 들쭉날쭉하다는 보고.
  * 원인: 글리프마다 비트맵 박스 top 이 달라(내림꼴/받침 유무) 모든 박스를 줄 맨위에 맞춰 그려서 자모마다 높이가 틀어짐.
  * 수정: 글리프에 xoff/yoff(펜/베이스라인 기준 박스 오프셋) 저장, 폰트에 ascent 저장, 그릴 때 `y + ascent + yoff` 베이스라인 배치(좌우 lsb 오프셋도 반영).
  * NRO 교체(md5 e076ddcb), 패치 636줄.
- 2026-10-18 밤: **베이스라인 수정 기기 확인 완료** ("오케이 맞는다"). 한글 표시 3단계(깨짐→겹침→높낮이) 모두 해결.
- 2026-10-18 자체 서버 계획 (사용자 선택 "이 박스에 서버 구축"):
  * 이 박스 = 192.0.2.10(enp5s0), 스위치와 같은 LAN. 멀티 방식: 인터넷 탭은 FWGS 마스터 조회, 연결은 Xash3D 49 → GoldSrc 48 순서 시도, 커스텀 파일은 게임 내 UDP 수신(느림).
  * 구성: xash3d-fwgs 전용서버(linux x86_64, worktree `src/xash3d-fwgs-linux`) + ReGameDLL linux 빌드 + media3 게임 데이터(hardlink) + 즐겨찾기 주입(`favorite_servers.lst`, 형식 `"주소" "49"`, 48 은 무시됨에 주의).
  * 방화벽 검토(2026-10-18): ufw 비활성, INPUT ACCEPT. 공유기 NAT 로 외부 미노출. CS 서버는 **LAN IP 전용 바인딩 필수**(0.0.0.0 이면 Tailscale 망까지 열림). 도커 쓰면 `-p 192.0.2.10:27015:27015/udp`. 외부 공개는 공유기 포트포워딩 할 때만.
- 2026-10-18 자체 서버 가동 완료:
  * 빌드: 엔진 전용서버 = worktree `src/xash3d-fwgs-linux`(동일 커밋 03a396e, `./waf configure -T release -d -8`, 서브모듈 재 초기화 필요했음).
    ReGameDLL = `3rdparty/ReGameDLL_CS/build-linux/regamedll/cs_amd64.so` (`-DXASH_COMPAT=ON` 필수, 아니면 -m32 로 빌드됨).
  * 조립 `out/dedicated/`: xash + filesystem_stdio.so. media3 이 ZFS 라 하드링크 불가 -> `valve` 는 통째로 심볼릭 링크,
    `cstrike/` 는 실제 디렉터리에 대용량 하위 디렉터리만 심링크, 설정(config/server/mapcycle)은 실제 복사, `dlls/cs_amd64.so` 는 우리 빌드.
  * 가동: systemd 유저 서비스 `~/.config/systemd/user/cstrike-ded.service` (linger on = 재부팅 자동 시작, Restart=always).
    실행 인자: `xash -game cstrike +ip 192.0.2.10 +maxplayers 12 +map de_dust2`. UDP 192.0.2.10:27015 만 바인딩 확인(ss). hostname "집 카스 서버 (LAN)".
  * 즐겨찾기: 서버 데이터 `cstrike/favorite_servers.lst` 에 `"192.0.2.10:27015" "49"` 주입. 기기 갱신 후 즐겨찾기 탭에 뜸.
  * 운영: `systemctl --user start|stop|restart cstrike-ded`, 로그 `journalctl --user -u cstrike-ded -f`. rcon 미설정(필요시 server.cfg 에 rcon_password).
- 2026-10-18 심야: 자체 서버는 OCI(a1-ubuntu, ARM64, 공인 198.51.100.20) 로 이전하기로.
  이 박스의 cstrike-ded 서비스는 정지+해제. 빌드 산출물/레시피는 그대로 보관(x86_64 바이너리는 OCI 아키텍처가 달라 재활용 불가, BUILD.md 레시피로 OCI 에서 재빌드).
  이 박스 -> OCI ssh 는 공개키 미등록으로 불가. OCI 세션(pane 2.4)에 전달할 브리프는 사용자가 붙여넣기.
- 2026-10-18 심야 마무리: OCI 서버(aarch64) 가동 확인(A2S_INFO 응답: hostname "OpenCourse Server", de_dust2, cstrike).
  스위치 즐겨찾기를 `198.51.100.20:27015` "49" 로 교체(LAN 주소는 제거). 친구 접속 안내: 콘솔 connect 198.51.100.20 또는 서버 추가.
- 2026-10-18 심야 추가: OCI 서버 주소를 포트(엔진) 자체에 심음. host.c NSWITCH 블록에서 시작 시
  favorite_servers.lst 에 "198.51.100.20:27015" "49" 이 없으면 추가(즐겨찾기 탭에서 항상 바로 보임,
  게임이 파일을 다시 써도 다음 시작에 복구). NRO 교체.
- 2026-10-19 심야: OCI 접속 후 맵 로드 직전 사망(로그가 FS 재스캔에서 끊김) 원인 규명과 수정:
  * 규명 경로: 리눅스(x86_64)에 바닐라 클라이언트+cs16-client+freevgui 를 Xvfb 에 띄워 OCI 에 직접 재현.
    (필수 우회: SDL_ShowSimpleMessageBox 가 헤드리스에서 자식 프로세스 wait4 로 영구 대기 -> LD_PRELOAD 로 no-op. autoexec.cfg 는 실행 안 됨, userconfig.cfg 사용.)
  * 결과: 바다라 클라 = 인게임 진입 정상(데이터/서버 무결 확정). 내 패치 킨 클라도 진입 정상이지만
    접속 시 콘솔 글꼴 3종(14/18/22px, 한글 아틀라스 각 8MB)이 통짜 재베이크되는 것을 목격(FS 재스캔→cvar CHANGED→Con_InvalidateFonts).
    스위치는 이 재베이크 구간(맵 로드 중 24MB+ 할당/업로드)에서 죽는 것으로 판정.
  * 수정: TTF 글꼴은 FS/코드페이지 무관이므로 무효화/재스캔 대상에서 제외(Con_InvalidateFonts, CL_GetScreenInfo 의 hud_fontscale 경로).
    리눅스 검증: 접속 시 재베이크 소멸(시작 시 1회만), 인게임 한글 정상.
  * NRO 교체(md5 ef51199d), 패치 707줄. 리눅스 재현 환경은 out/client-test/ + worktree src/xash3d-fwgs-linux-client/ 보관.
- 2026-10-19 새벽: 접속 사망의 진짜 원인 = 기기 cstrike_downloads 의 옛 중국서버 커스텀 파일(재스캔 때 최우선 마운트로 원본을 덮음).
  사용자가 폴더 이름 바꾸니 인게임(팀선택)까지 진입 성공. 단 게임 중 화면 체커보드(사용자 확인 "어 맞어") + 이동 불가 보고.
  * 대응 1: 스위치 빌드에서 _downloads 폴더를 게임 폴더 "뒤"에 추가(원본 우선. 커스텀이 원본을 못 덮음).
  * 대응 2: 폰트 메모리 축소 = 콘솔 글꼴은 사용 중 크기 1개만 로드(기존 3개 전부) + 업로드 뒤 CPU 아틀라스 해제.
    VRAM 32MB->16MB, 상시 CPU 32MB->0. 리눅스 검증: 폰트 1회 로드, 인게임 진입, 스크린샷 체커보드 0%.
  * NRO 교체(md5 f70a0c09), 패치 765줄. 남은 확인: 인게임 화면(체커보드 여부), 팀 선택 후 이동.
- 2026-10-19 새벽: "홈브류 404/받지 못했습니다" 클라 오류 = OCI 정합검증 때 만든 `.cs-data-manifest.md5` 숨김파일이
  홈브류 폴더에 들어가 설치 목록에 섞인 것 때문으로 판정(점 시작 경로). ref/ 로 이동해 제거. 홈브류 폴더에는 점 파일 금지.
- 2026-10-19 새벽 마무리: 홈브류 갱신 실패(404) 해결 = 숨김파일 제거 후 정상. 원인은 목록 캐시:
  서버는 홈브류 폴더를 60초 주기로 재스캔하고 클라 목록도 주기 갱신이라 반영이 최대 1~2분 늦다.
  이제 기기에 f70a0c09(폰트 VRAM 축소 + 다운로드 폴더 우선순위) 배포 완료. 남은 기기 확인: 인게임 화면/팀선택/이동.
- 2026-10-19 새벽: "깨진 타일" 의 정체 = 터치 버튼 아이콘. 원인: extras.pk3 는 XASH3D_EXTRAS_PAK1/2 환경변수로만
  마운트되는데 스위치 플랫폼 초기화에 그 세팅이 없어 extras 전체(터치 아이콘 gfx/touch/*, 셸 그래픽, 폰트)가 누락됐음.
  수정: sys_nswitch.c NSwitch_Init 에서 setenv(XASH3D_EXTRAS_PAK1, "valve/extras.pk3") (Platform_Init 직후 FS_init 이라 시점 정확).
  사용자 요청 = 터치 아이콘을 끄지 말고 살릴 것. NRO 교체.
- 2026-10-19 새벽: 터치 버튼 스프라이트 2차 수정. cs16-client 터치 설정이 쓰는 touch/gfx/* 그림과
  touch/, touch_default/, touch_presets/, touch.cfg (cs16client-extras, 약 900KB) 를 서버 게임 데이터 cstrike/ 에 추가.
  엔진 extras.pk3 마운트(33d6dfff)와 별개로 cs16 고유 아이콘은 이 패키지에만 있었다.
- 2026-10-19 새벽: cs16client-extras 누락분 전량 보충(사용자 질문 "그 외에는 더 없었니?"):
  맵 4개(tr_*.bsp 훈련맵 5.2MB), sound/training/cstrain*.wav 25개(훈련 음성), media/(메뉴 UI 효과음 7개),
  userconfig.d/(cs16 기본 설정 + 터치 별칭), gfx/ 셸 그래픽(cs16 고유 bmp) + touch 일제(이전 항목).
  extras/sound 나머지는 기존 데이터에 포함 확인(차이 0). 누락분은 사실상 전부 "훈련 과정" 콘텐츠였음.
- 2026-10-20 팀 선택 글자가 비던 원인 = VGUI 한글 문제가 아니었다. 팀 선택/구매 메뉴는 `touch/*.cfg` 터치 버튼이라 엔진 `in_touch.c` 의
  `Touch_DrawCharacter` 가 `creditsFont.fontRc[]`(비트맵 글꼴 사각형 표)로 그리는데, 이 빌드는 creditsFont 를 TTF 로 바꿔 표가 비어 있었다(사각형 크기 0).
  * 수정: creditsFont 가 FONT_TRUETYPE 이면 `CL_DrawCharacter` 로 TTF 글리프를 그린다. 높이는 화면 너비의 1.75%(`TOUCH_TTF_TEXT_HEIGHT`, 추정값이라 기기에서 크기 확인 필요).
  * freevgui 는 스위치 빌드에 쓰이지 않는다(클라이언트에 vgui:: 심볼 0). 한글 VGUI 글꼴 작업은 불필요.
  * 서버 `homebrew/cstrike/cstrike.nro` 교체 (md5 4b464417, 이전 33d6dfff 는 `out/engine-cstrike/cstrike-final.nro` 에 보관). 패치 파일 재생성 완료(871줄).
  * 주의: 홈브류 폴더에 임시 점 파일을 두면 목록에 섞인다. 교체는 같은 폴더 안에서 점 없는 이름으로 복사 후 mv.
- 2026-10-20 기기 확인 보고 정리:
  * 터치 메뉴 문구가 영어였던 원인: `touch/*.cfg` 는 사전 조회 없이 글자를 그대로 그린다. `scripts/ko-touch.py` 가 공식 사전(cstrike_koreana.txt)으로 영문→한글 치환(23개 cfg), 단위/나라는 규칙으로 처리. 원본은 보존하고 출력 폴더에 쓴다.
  * 컨트롤러 버튼이 안 먹던 원인: config.cfg 첫 줄 `unbindall` 이 엔진 기본 게임패드 바인딩을 지우고 키보드만 다시 묶었다. `userconfig.cfg` 에 패드 매핑을 넣었다.
  * 터치 오버레이: 폰 프로필(36개)이 화면을 덮었다. `touch.cfg` 를 컨트롤러 기본으로 바꿔 구매/팀 변경/무전/채팅 2/명령 메뉴/봇 메뉴/편집 8개만 위쪽 가운데에 작게 둔다.
  * 자이로: `userconfig.cfg` 가 없는 변수(`joy_gyro`, `joy_gyro_sens` 등)를 써서 무시됐다(로그 Unknown command). 엔진 변수(`joy_gyro_enable`, `joy_gyro_pitch/yaw`)로 교체.
    엔진은 SDL 센서(`SDL_GameControllerHasSensor`)로만 자이로를 받는다. 이전 로그에 자이로 보정 줄이 없어 이 컨트롤러에서 센서가 안 잡혔을 가능성이 있다.
    joy_sdl2.c 에 `Active gamepad "<이름>": gyro yes/no` 로그를 추가했다. 서버 NRO 교체(진단용). 다음 engine.log 에서 확인한다.
- 2026-10-20 자이로/이름 저장 (서버 NRO md5 교체, 새 NRO `out/engine-cstrike/cstrike-nxgyro.nro`):
  * 기기 engine.log: `Active gamepad "Switch Controller": gyro no, 0 touchpads` => SDL 이 스위치 라이트 센서를 못 읽는다.
    `nswitch/sys_nswitch.c` 의 `NSwitch_PollGyro()` 가 libnx `hidGetSixAxisSensorStates` 로 직접 읽어 `Joy_GyroEvent` 에 넣는다(`Platform_RunEvents` 에서 매 프레임 호출). SDL 이 센서를 잡으면 SDL 우선.
    축과 단위는 추정이다: `joy_nx_gyro_pitch/yaw/roll`(x|y|z, 앞에 - 로 반전)와 `joy_nx_gyro_scale`(기본 2π, 회전/초 가정)을 userconfig.cfg 로 조정한다. 기기 확인 전.
  * 이름이 안 남던 원인: config.cfg 는 정상 종료(Host_Shutdown)에서만 저장되는데 스위치는 HOME 으로 닫으면 거기까지 안 간다. `CL_Connect_f` 에서 접속 직전에 `Host_WriteConfig()` 를 부른다.
  * 컨트롤러: 점프 B_BUTTON, 사용 A_BUTTON, 재장전 Y_BUTTON, 손전등 X_BUTTON. `_snd_mixahead` 0.2 (지직 소리 대응, 원인 미확정).
- 2026-10-20 터치 메뉴 한글이 `????` 로 나온 원인: 내가 넣은 터치 TTF 경로가 `CL_DrawCharacter` 에 코드포인트를 넘겼는데, 그 함수가 플래그 없이는 `number &= 255` 로 잘라 한글이 깨졌다(영어는 255 이하라 멀쩡).
  * 수정: `FONT_DRAW_CODEPOINT` 플래그를 추가해 이미 코드포인트면 자르지 않게 하고 `Touch_DrawCharacter` 가 그 플래그를 쓴다. 서버 NRO 교체(`out/engine-cstrike/cstrike-codepoint.nro`).
- 2026-10-20 터치 메뉴 번역 보강: 사전에 없는 맵 시나리오 설명/팀 소개/메뉴 단어는 `scripts/ko-touch.py` 의 MANUAL 표에 직접 번역해 넣었다.
  입력은 원본 영문(`cs16-client/3rdparty/cs16client-extras`)을 쓰고 사전은 서버 `resource/cstrike_koreana.txt` 를 넘긴다:
  `ko-touch.py <extras> <출력폴더> <cstrike_koreana.txt>` 후 바뀐 cfg 만 서버 `cstrike/touch*/` 에 복사. (`touch.cfg` 는 컨트롤러용으로 직접 만든 것이라 대상이 아니다.)
  남은 영문은 무기 이름(GALIL, FAMAS 등 고유 표기), 단위/구경, 안 쓰는 자리 표시 문구뿐. 이전에 `YOU HAVE ...` 규칙이 "You have to ..." 문장까지 잡아 "보유 금액 to ..." 로 깨뜨린 것도 고쳤다.
- 2026-10-20 한 줄짜리 터치 라벨을 칸 세로 가운데에 그리도록 `Touch_DrawText` 수정. NRO `cstrike-vcenter.nro`. 번역 검증 도구: `scripts/touch-fit.py`(넘침 계산), `scripts/touch-preview.py`(미리보기).
- 2026-10-20 센터프린트 한글 깨짐 수정(CL_DrawCenterPrint 에 FONT_DRAW_CODEPOINT, CL_DrawStringLen 폭 계산), 폰트 tahoma.ttf 를 Noto Sans CJK KR Bold 부분집합(KS X 1001+ASCII, 370KB)으로 교체(`ref/fontprev/NotoSansKR-Bold-sub.otf`), 자이로 감도 0.85 + 스코프 시야각 비례 감속 `joy_gyro_zoom 1.2`(in_joy.c, 최소 0.1배). NRO `cstrike-gyrozoom.nro`.
- 2026-10-20 메인 메뉴 배경(`gfx/shell/splash.bmp`, 원래 640x480)을 1280x720 으로 교체: 사용자가 준 병사 이미지를 높이 720 에 맞춰 오른쪽 기준으로 자르고 왼쪽을 어둡게 눌러 메뉴 글자가 읽히게 했다(`ref/new-splash-1280.png`, 원본은 `ref/old-splash.bmp`). 기하무늬 이미지와의 합성은 병사가 올리브색이라 크로마키가 안 먹어 보류.
- 2026-10-20 메인 메뉴 배경 3장(splash.bmp / splash2.bmp / splash3.bmp, 각 1280x720)에서 실행마다 하나를 무작위로 고르도록 `BackgroundBitmap.cpp` 수정(`patches/mainui.patch`). 원본 이미지는 `ref/*-1280.png`. NRO `cstrike-splash.nro`.
- 2026-10-20 메인 메뉴 버튼 시트 `gfx/shell/btns_main.bmp` 를 한글로 다시 구움: `scripts/ko-menu-btns.py <원본> <출력> <TTF>`(Gothic A1 Bold, 라벨 71개 x 3상태). 원본은 `ref/old-btns_main.bmp`. 제목 그림 `head_*.bmp` 와 `btn_*.bmp` 는 아직 영문.
- 2026-10-20 폰트를 나눔스퀘어 라운드 Bold 로 확정: 게임 안 `gfx/fonts/tahoma.ttf` 와 메뉴 버튼 시트 둘 다 교체(KS X 1001 누락 0). Gothic A1 원본은 시스템 폰트(/usr/local/share/fonts/korean)에 있음.
- 2026-10-20 글자 또렷하게: (1) 엔진 TTF 글리프 가장자리 대비 보정과 그리는 좌표 정수 스냅(cl_font.c), (2) mainui StbFont 가장자리 보정, (3) 메뉴 버튼 시트를 2배 해상도(312x52 칸, 8비트 팔레트)로 굽고 Btns.cpp 가 가로 156 의 배수를 배율로 인식(GetTexW 추가). 원본 156x26 시트도 그대로 동작한다. NRO cstrike-crisp.nro, libmenu.so 함께 교체.
- 2026-10-20 제목 그림 head_*.bmp 24개와 보조 버튼 btn_*.bmp 12개도 한글로 구움(`scripts/ko-menu-extra.py <원본> <출력> <TTF>`, 2배 해상도 8비트). 원본은 `ref/old-shell/`.
- 2026-10-20 NRO 아이콘 교체: 사용자가 준 CS 로고(노랑 바탕)를 256x256 으로 잘라 `ref/cstrike-icon.jpg`. make-nro.py 두 번째 인자로 사용. 원래 아이콘은 `ref/old-cstrike-icon.jpg`.
- 2026-10-20 메인 메뉴 설명문은 mainui 의 "Trebuchet MS" → `gfx/fonts/FiraSans-Regular.ttf` 를 쓴다(콘솔/HUD 는 tahoma.ttf). 이 파일이 옛 Gothic A1 그대로라 찌그러졌었다. 둘 다 나눔스퀘어 라운드 Bold 로 통일.
- 2026-10-20 splash 가 이미 있으면 항상 그것을 그리도록 `UpdatePreference` 수정(Steam 식 타일 배경이 우선하던 경우 대비). libmenu.so 교체.
- 2026-10-20 접속 중 콘솔 배경(로딩 화면)은 `gfx/shell/conback.bmp` 를 가장 먼저 찾는다. 엔진이 4:3(가로x0.75)로 늘려 그리고 아래쪽 720줄만 보이게 하므로 1280x960 에 16:9 그림을 아래 720줄에 놓고 위 240줄은 반사로 채웠다(`ref/conback-1280x960.png`). 이전엔 valve/gfx/conback.lmp 가 쓰였다.
- 2026-10-20 터치 메뉴 글자 크기 0.0175 → 0.0190, 한 줄 라벨을 가운데에서 줄 높이의 10% 위로 올림(글자 위쪽이 비어 보인다는 피드백). NRO cstrike-touchsize.nro.
- 2026-10-20 진단 로그(임시, 원인 확인 뒤 제거): cl_font.c CL_TTFLookup 의 '?' 대체 글리프 코드포인트, cl_game.c pfnDrawCharacter 의 비ASCII 호출. NRO cstrike-diag.nro. 클라이언트 DLL 의 draw_util.cpp Con_UtfProcessCharForce 는 코드페이지 1251/1252 가 아니면 '?' 를 돌려준다(폭 계산에만 쓰임, 그리기는 원본 바이트를 엔진에 넘김).
- 2026-10-20 메뉴 설명줄(PicButton/Action/Slider/CheckBox/Framework)을 흰색+검은 그림자 1px 로. 글자 전체 확대: HUD 16→18, 콘솔 14→16(+4n), 메뉴 SMALL 20→22, MED 26→28, CONSOLE 18→20. NRO cstrike-bigtext.nro.
- 2026-10-20 conback.bmp 를 컨테이너 풍경(ref/splash4-right-1280.png, 사용자 제공 1920x620 의 오른쪽 16:9)으로 교체. 병사는 자른다.
- 2026-10-20 메인 메뉴는 이전 모습이 낫다는 피드백으로 메뉴 글자 크기(SMALL 20, MED 26, CONSOLE 18)를 되돌림. 설명줄 흰색은 유지. 로딩 화면 conback 은 확정.
- 2026-10-20 정정: 메뉴 글자 크기는 키운 쪽이 좋다는 뜻이었다. SMALL 22, MED 28, CONSOLE 20 으로 다시 키움. 되돌리라던 것은 메인 메뉴 배경.
- 2026-10-20 진단 로그 제거(중앙 메시지 한글은 정상 확인). ClientScheme.res 의 모든 글꼴 tall 을 1.25배(Marlett 제외, 원본 ref/ClientScheme.orig.res). NRO cstrike-final.nro.
- 2026-10-20 메인 메뉴 배경을 사용자 제공 노란 배경 두 병사(1920x620 의 오른쪽 16:9, ref/splash-main-1280.png)로 통일. splash/splash2/splash3.bmp 를 같은 그림으로 덮음.
- 2026-10-20 conback.bmp 좌우 반전.
- 2026-10-20 채팅: 스위치 소프트웨어 키보드 확인 시 SDL_TEXTINPUT 직후 key_message 면 K_ENTER 를 보내 바로 전송(host_sdl2.c, XASH_NSWITCH). 한글 입력 확인용 임시 로그 'chat input: ...' 포함. NRO cstrike-chat.nro.
- 2026-10-20 메인 메뉴 배경 좌우 반전(splash*.bmp, 끝에 0 바이트 80/96/112 로 크기 변경해 재동기화).
- 2026-10-20 인게임 글자 추가 확대: HUD 18→22, 콘솔 16→20(+4n). NRO cstrike-bigger.nro.
- 2026-10-20 터치 글자 0.019→0.023 확대, 한 줄 라벨 위치를 cvar touch_text_lift(기본 0.1, userconfig.cfg 에서 0.22)로 조절. 계산상 글자는 가운데에 가깝게 나오지만 실기기에선 아래로 쏠려 보인다는 피드백이라 값을 기기에서 맞춘다. NRO cstrike-lift.nro.
- 2026-10-20 키보드 입력이 필드를 교체: SDL_TEXTINPUT 직전에 ctrl-c(필드 비우기)를 보냄(메뉴/채팅/콘솔, XASH_NSWITCH). 임시 로그 'keyboard input (dest, accept_utf8): 문자열'. NRO cstrike-kbd.nro.
- 2026-10-20 ZL(총기 모드 전환 등) 중앙 메시지 '???\????' 원인: CL_DrawCenterPrint 의 line 버퍼가 byte 라 코드포인트가 1바이트로 잘렸다. int 로 수정. NRO cstrike-cp.nro. (cl_dll message.cpp 경로의 폭탄 메시지는 원래 정상)
- 2026-10-20 STICK2(오른쪽 스틱 누름)를 +duck → +voicerecord 로. 앉기는 L1 이 이미 있다. 마이크/음성 동작은 기기 미검증.
- 2026-10-20 팀 선택 글자 겹침 원인: 한 줄 라벨 세로 가운데 정렬이 시나리오 제목처럼 키가 큰 영역(0.23~0.82)에도 적용돼 제목이 화면 가운데로 내려와 desc2 와 겹쳤다. 박스 높이가 줄 높이의 2.5배 미만일 때만 가운데 정렬. NRO cstrike-title.nro.
- 2026-10-20 마이크: SDL 스위치 드라이버에 캡처가 없어 voice.device_opened 가 false 였다(음성 안 보내짐). s_sdl2.c 에 libnx audin 백엔드(XASH_NSWITCH): 푸시 중에만 도는 스레드, 장치 샘플레이트/채널을 voice.samplerate 모노로 선형 변환해 voice.input_buffer 에 쌓음. 빌드만 확인, 기기 미검증. 정상이면 콘솔에 'Switch microphone ready (N Hz, M ch)'. NRO cstrike-mic.nro.
- 2026-10-20 플레이어 설정: 이름 칸 아래에 'X 버튼으로 한 글자씩 지울 수 있습니다' 안내(nameHint). 메뉴 입력칸은 이미 X=백스페이스(Utils.h IsBackspace).
- 2026-10-20 touch_text_lift 가 먼저 shift 를 0 으로 잘라서(박스 38px, 줄 29px 일 때 (38-29)/2 - 0.22*29 < 0) 값을 키워도 위치가 안 변했다. 클램프 제거, 값 0.33. NRO cstrike-lift2.nro.
- 2026-10-20 점수판: valve_koreana.txt 의 PlayerScore/Death/Ping 를 점수/사망/지연 으로 줄이고, 사전에 없던 Cstrike_HEALTH(체력)·Cstrike_ACCOUNT(돈) 추가(토큰이 그대로 보였다). TTF 글리프 advance 에 윤곽 2px 추가(글자끼리 붙던 자간). NRO cstrike-space.nro.
- 2026-10-20 이름 칸 안내문 '(X 버튼으로 지움, A 버튼으로 입력)'.
- 2026-10-20 콘솔/로딩 화면 글자 기본 20→15(+4n). 로딩 로그가 화면 절반을 차지한다는 피드백. NRO cstrike-con15.nro.
- 2026-10-20 touch_text_lift 0.33→0.42 (userconfig.cfg 만 교체).
- 2026-10-20 userconfig.cfg 값만 바꾸면 크기가 같아 쇼핑몰이 재동기화하지 않았다(0.22→0.33→0.42 모두 같은 길이). 주석 한 줄로 크기를 바꾸고 0.5 로 올림. 값 바꿀 때마다 파일 크기가 달라지게 할 것.
- 2026-10-20 libmenu.so 가 빌드마다 크기가 같을 수 있어(페이지 정렬) 쇼핑몰이 재동기화하지 않는다. 끝에 0 바이트 37개를 붙여 크기 변경. 앞으로 libmenu.so 를 올릴 때 크기가 직전과 달라야 한다.
- 2026-10-20 touch_text_lift 기본값을 코드에서 0.5 로, ARCHIVE 제거(config.cfg 에 옛 값이 저장돼 덮어쓰는 것 방지). userconfig.cfg 동기화에 의존하지 않는다. NRO cstrike-lift3.nro.
- 2026-10-20 점수판 열 간격 10→36px(scoreboard.cpp SCOREBOARD_COL_GAP). 클라이언트 빌드는 build-cs.sh 를 엔진 빌드와 같은 마운트(src→/work, out, scripts)로 돌리고 산출물은 src/build-cs/cl_dll/client_nswitch_arm64.so.

## 2026-10-20 점수판 열 겹침 원인
`gHUD.GetCharWidth` 가 `unsigned char` 를 받아 한글 코드(255 초과)가 잘려 엉뚱한 폭이 나왔다. 열 간격을 아무리 넓혀도 오른쪽 정렬 글자가 서로 붙던 이유다. `int` 로 받고 255 초과는 화면 밖에 그려 엔진이 돌려주는 폭을 쓴다.
- 2026-10-21 이름 칸 포커스 때 키보드 자동 열림 차단은 되돌렸다(사용자 요청). 터치로 열기는 유지.
- 2026-10-20 점수판: `pfnDrawCharacter` 에 y=-99999 이면 폭만 돌려주는 경로를 추가하고 `GetCharWidth` 가 255 초과 글자에 그걸 쓴다. 이름 열 폭을 키 문자열 대신 "MMMMMM" 폭으로, 열 간격은 28.
- 2026-10-20 입력칸을 터치(왼쪽 마우스)로 눌러도 키보드가 열리도록 `Field.cpp` KeyDown 수정.
- 2026-10-21 오버레이를 overlay-common / overlay-ko / overlay-en 으로 나누고 순정(영문)판 변형을 추가했다. 조립은 ../_template/register.py + port.json.
- 2026-10-21 공개용 순정판 압축본 스크립트 scripts/release-global.sh 추가(영문 userconfig, 개인 배경 제외, GPL 소스 패치 동봉).
- 2026-10-21 호스트 코드의 서버 주소 하드코딩을 없앴다. 엔진은 default_favorites.lst 의 서버를 즐겨찾기에 채워 넣는다(주소는 favorites.txt, 저장소에 올리지 않음).
