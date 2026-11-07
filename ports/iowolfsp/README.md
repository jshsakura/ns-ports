# 리턴 투 캐슬 울펜슈타인 (Return to Castle Wolfenstein)

<!-- quick:begin -->
## 필요한 파일과 명령어

**1. 받아서 둘 것**

| 놓을 위치 | 무엇 | 구하는 곳 |
| :--- | :--- | :--- |
| `ports/iowolfsp/in/iowolfsp.nro` | 스위치용 NRO (선택) | 안 둬도 된다. 없으면 capsterx-switch/iortcw 릴리스 pre-release 에서 자동으로 받는다 |
| `ports/iowolfsp/in/data` | RTCW PC 정품 Main 폴더의 pak 파일(pak0.pk3, sp_pak1.pk3 등) | 내가 가진 정품 데이터 (--rom <폴더> 로 따로 줘도 된다) |
| `ports/iowolfsp/icon.jpg` | 앱 아이콘 (256x256 JPEG) (선택) | 직접 구하거나 만든다. 없으면 NRO 에 든 아이콘을 그대로 쓴다 |

**2. 이미지**: 앱 아이콘(`icon.jpg`, 256x256 JPEG)만 쓰이고 없으면 NRO 의 기본 아이콘을 씁니다. 이미지는 저장소에 없으니 필요하면 직접 구해 위 위치에 두세요. 배너와 스크린샷은 다루지 않습니다.

**3. 확인하고 실행**

```
python3 build.py guide iowolfsp    # 빈 칸과 구하는 곳 확인
python3 build.py iowolfsp --rom <내 게임 데이터 폴더> --zip
```

NRO 는 구하지 않아도 됩니다. `in/` 에 없으면 capsterx-switch/iortcw 릴리스 pre-release 에서 받아 sha256 을 확인하고 씁니다.

- 원 프로젝트: https://github.com/iortcw/iortcw
- 스위치 포트 소스: https://github.com/capsterx-switch/iortcw
<!-- quick:end -->

[iortcw](https://github.com/iortcw/iortcw) 싱글플레이 클라이언트의 스위치 네이티브 빌드.
업스트림 [capsterx-switch/iortcw](https://github.com/capsterx-switch/iortcw) 의 `pre-release` zip 에 든 `iowolfsp.nro` 를 쓴다.

- 필요한 것: RTCW PC 정품 게임 데이터
- 상태: 기기 시험 전 (`planned`)
- 한국어: 없음

## 포트 id 가 `iowolfsp` 인 이유
NRO 안에 설치 경로로 `sdmc:/switch/iowolfsp/` 가 들어 있다. 폴더 이름이 다르면 `main` 폴더를 찾지 못할 것으로 본다(바이너리에서 읽은 내용이고 기기에서 시험하지는 않았다). 그래서 조립 결과가 `switch/iowolfsp/` 로 나오도록 id 를 맞췄다.

## 준비물
게임 데이터 폴더는 아래 구조여야 한다.

```
<데이터 폴더>/
  main/
    pak0.pk3, sp_pak1.pk3 ...    RTCW PC 정품 Main 폴더의 파일
    mp_bin0.pk3                  릴리스 zip 의 switch/main
    mp_rend2_shaders0.pk3        릴리스 zip 의 switch/main
    sp_rend2_shaders0.pk3        릴리스 zip 의 switch/main
    autoexec.cfg                 릴리스 zip 의 switch/main (패드 설정)
```

```
python3 build.py iowolfsp --rom <데이터 폴더> --deploy <homebrew 폴더>
```

## 알아 둘 것
- 업스트림 기본 브랜치에서는 스위치용 코드를 찾지 못했다. 쓰는 NRO 는 릴리스 파일이고 소스로 다시 빌드할 수 있는지는 확인하지 못했다.
