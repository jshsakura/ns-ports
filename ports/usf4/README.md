# 울트라 스트리트 파이터 4 (Ultra Street Fighter IV)

<!-- quick:begin -->
## 필요한 파일과 명령어

**1. 받아서 둘 것**

| 놓을 위치 | 무엇 | 구하는 곳 |
| :--- | :--- | :--- |
| `ports/usf4/in/usf4.nro` | 스위치용 NRO | https://github.com/Thorhax/usf4-nx/releases 의 v0.8.1 usf4.nro |
| `ports/usf4/in/data` | 업스트림 설치 페이지가 내 Xbox 360 디스크로 만든 game_root 폴더와 deko3d_glsl.bin | https://thorhax.github.io/usf4-nx-installer/ 에서 만든 usf4-nx.zip 을 풀어서 쓴다 (--rom 으로 따로 줘도 된다) |
| `ports/usf4/icon.jpg` | 앱 아이콘 (256x256 JPEG) (선택) | 직접 구하거나 만든다. 없으면 NRO 에 든 아이콘을 그대로 쓴다 |

**2. 이미지**: 앱 아이콘(`icon.jpg`, 256x256 JPEG)만 쓰이고 없으면 NRO 의 기본 아이콘을 씁니다. 이미지는 저장소에 없으니 필요하면 직접 구해 위 위치에 두세요. 배너와 스크린샷은 다루지 않습니다.

**3. 확인하고 실행**

```
python3 build.py guide usf4    # 빈 칸과 구하는 곳 확인
python3 build.py usf4 --rom <내 게임 데이터 폴더> --zip
```

NRO 는 구하지 않아도 됩니다. `in/` 에 없으면 Thorhax/usf4-nx 릴리스 v0.8.1 에서 받아 sha256 을 확인하고 씁니다.

- 스위치 포트 소스: https://github.com/Thorhax/usf4-nx
<!-- quick:end -->

Xbox 360판(타이틀 434307FC)을 [ReXGlue](https://github.com/rexglue/rexglue-sdk) 로 정적 리컴파일하고 deko3d 로 그리는 네이티브 포트.
업스트림 [Thorhax/usf4-nx](https://github.com/Thorhax/usf4-nx) v0.8.1 의 릴리스 `usf4.nro` 를 쓴다. 게임 파일과 셰이더는 업스트림 설치 페이지가 내 디스크로 만든다.

- 필요한 것: Xbox 360 디스크를 그대로 뜬 `.iso` (약 8.7GB). CCI, GOD, ZAR 같은 압축 이미지는 안 된다
- 상태: 기기 시험 전 (`planned`)
- 한국어: 포트에서 한국어 메뉴가 나오는지 확인하지 못했다
- 데이터 폴더 위치: NRO 는 자기가 놓인 폴더에서 데이터를 찾는다. 업스트림 기본 이름은 `usf4-nx` 이지만 이 저장소는 `usf4` 로 조립한다

## 준비물
1. `in/usf4.nro`: 릴리스의 `usf4.nro`
2. 게임 데이터 폴더: 설치 페이지(https://thorhax.github.io/usf4-nx-installer/)에서 만든 `usf4-nx.zip` 을 푼 폴더. 아래 구조여야 한다
   ```
   <데이터 폴더>/
     game_root/          디스크 내용 (Default.xex, archive, movie 등)
     deko3d_glsl.bin     내 디스크로 만든 셰이더
     LICENSES.txt        설치 페이지가 넣는 라이선스 고지
   ```
   설치 페이지는 브라우저 안에서만 돌고 게임 파일을 밖으로 보내지 않는다. 0.8.0 과 0.8.1 은 셰이더가 같아서 0.8.0 으로 만든 데이터를 그대로 써도 된다.

```
python3 build.py usf4 --rom <데이터 폴더> --deploy <homebrew 폴더>
```

## 실행 때 주의
- 앨범 애플릿 모드는 메모리가 모자라 안 된다. 게임 덮어쓰기(타이틀 시작 중 R 누르기)로 연다.
- 업스트림 실측으로는 CPU 1785 MHz, GPU 768 MHz 에서 대전이 60 fps 다(sys-clk 로 설정).
- 처음 가는 장면은 셰이더를 만드느라 잠깐 멈춘다. 만든 셰이더는 SD 카드의 `deko3d_shaders.bin` 에 남아 다음부터는 멈추지 않는다.
- 첫 실행 때 설정 파일 `usf4.toml` 이 생긴다. `usf4_button_icons` 를 `"xbox"` 로 바꾸면 버튼 표시가 Xbox 식으로 돌아간다.
