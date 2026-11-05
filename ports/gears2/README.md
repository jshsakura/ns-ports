# 기어스 오브 워 2 (Gears of War 2)

<!-- quick:begin -->
## 필요한 파일과 명령어

**1. 받아서 둘 것**

| 놓을 위치 | 무엇 | 구하는 곳 |
| :--- | :--- | :--- |
| `ports/gears2/in/gears2-nx.nro` | 스위치용 NRO | 릴리스에 NRO 가 없다. https://github.com/VasilkovND/gears2-nx 의 INSTALL.md 대로 내 디스크로 직접 빌드한다 |
| `ports/gears2/in/data` | Xbox 360 소매판 디스크 game 폴더(default.xex, GearGame)와 gow2_shaders.dslib, shadercache_dksh.bin | gears2-nx 빌드가 내 디스크로 만든다 (--rom 으로 따로 줘도 된다) |
| `ports/gears2/icon.jpg` | 앱 아이콘 (256x256 JPEG) (선택) | 직접 구하거나 만든다. 없으면 NRO 에 든 아이콘을 그대로 쓴다 |

**2. 이미지**: 앱 아이콘(`icon.jpg`, 256x256 JPEG)만 쓰이고 없으면 NRO 의 기본 아이콘을 씁니다. 이미지는 저장소에 없으니 필요하면 직접 구해 위 위치에 두세요. 배너와 스크린샷은 다루지 않습니다.

**3. 확인하고 실행**

```
python3 build.py guide gears2    # 빈 칸과 구하는 곳 확인
python3 build.py gears2 --rom <내 게임 데이터 폴더> --zip
```

- 원 프로젝트: https://github.com/santiquiroz/gears-of-war-2-pc-port
- 스위치 포트 소스: https://github.com/VasilkovND/gears2-nx
<!-- quick:end -->

Xbox 360판을 [ReXGlue](https://github.com/rexglue/rexglue-sdk) 로 정적 리컴파일하고 deko3d 로 그리는 네이티브 포트.
업스트림 [VasilkovND/gears2-nx](https://github.com/VasilkovND/gears2-nx) v1.0.0 은 릴리스에 NRO 를 두지 않는다. 코드와 셰이더는 자기 디스크로 직접 빌드한다.

- 필요한 것: Xbox 360 소매판 디스크. 타이틀 업데이트는 지원하지 않는다
- 상태: 기기 시험 전 (`planned`)
- 한국어: 디스크에 `Coalesced_kor.bin` 과 `Startup_KOR.xxx` 가 들어 있지만 포트에서 한국어로 나오는지는 아직 확인하지 못했다

## 준비물
1. `in/gears2-nx.nro`: 업스트림 빌드 결과 `gow2/out/sw/gow2.nro` 의 이름을 바꾼 것
2. 게임 데이터 폴더: 아래 구조여야 한다
   ```
   <데이터 폴더>/
     game/                   디스크 내용 (default.xex, GearGame)
     gow2_shaders.dslib      내 디스크로 만든 셰이더
     shadercache_dksh.bin    내 디스크로 만든 셰이더 캐시
   ```
   빌드 방법은 업스트림 `INSTALL.md` 에 있다. 업스트림은 macOS 에서 검증했고 Linux 는 검증하지 않았다.

```
python3 build.py gears2 --rom <데이터 폴더> --deploy <homebrew 폴더>
```

## 실행 때 주의
- 앨범 애플릿 모드는 메모리가 모자라 안 된다. 게임 덮어쓰기(타이틀 시작 중 R 누르기)로 연다.
- CPU 오버클럭이 필요하다. 업스트림 실측은 CPU 1785 MHz, GPU 614.4 MHz, RAM 1600 MHz 에서 평균 27 fps, 기본 클럭에서 12~17 fps 다.
- FPS 표시는 ZL + ZR + 십자키 위다.
