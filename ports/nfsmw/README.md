# 니드 포 스피드: 모스트 원티드 (Need for Speed: Most Wanted)

<!-- quick:begin -->
## 필요한 파일과 명령어

**1. 받아서 둘 것**

| 놓을 위치 | 무엇 | 구하는 곳 |
| :--- | :--- | :--- |
| `ports/nfsmw/in/nfsmw.nro` | 스위치용 NRO (선택) | 안 둬도 된다. 없으면 StevensND/nfsmw-nx 릴리스 v1.0.0 에서 자동으로 받는다 |
| `ports/nfsmw/in/data` | Xbox 360 NTSC-K 디스크의 game_root 폴더와 셰이더 파일(nfsmw_shaders.nfsp) | 내가 가진 정품 데이터 (--rom <폴더> 로 따로 줘도 된다) |
| `ports/nfsmw/icon.jpg` | 앱 아이콘 (256x256 JPEG) (선택) | 직접 구하거나 만든다. 없으면 NRO 에 든 아이콘을 그대로 쓴다 |

**2. 이미지**: 앱 아이콘(`icon.jpg`, 256x256 JPEG)만 쓰이고 없으면 NRO 의 기본 아이콘을 씁니다. 이미지는 저장소에 없으니 필요하면 직접 구해 위 위치에 두세요. 배너와 스크린샷은 다루지 않습니다.

**3. 확인하고 실행**

```
python3 build.py guide nfsmw    # 빈 칸과 구하는 곳 확인
python3 build.py nfsmw --rom <내 게임 데이터 폴더> --zip
```

NRO 는 구하지 않아도 됩니다. `in/` 에 없으면 StevensND/nfsmw-nx 릴리스 v1.0.0 에서 받아 sha256 을 확인하고 씁니다.

- 스위치 포트 소스: https://github.com/StevensND/nfsmw-nx
<!-- quick:end -->

Xbox 360판을 [ReXGlue](https://github.com/rexglue/rexglue-sdk) 로 정적 리컴파일하고 NVK(Vulkan)로 그리는 네이티브 포트. 30fps, 오버클럭 없음.
업스트림 [StevensND/nfsmw-nx](https://github.com/StevensND/nfsmw-nx) v1.0.0 의 **`nfsmw-nx-kor.nro`**(NTSC-K 한국판)를 쓴다.
한국판 디스크의 한글 UI와 자막이 그대로 나오므로 따로 번역하지 않는다.

- 필요한 것: Xbox 360 한국판 디스크 (자기 것)
- 상태: 기기 시험 전 (`planned`)

## 준비물
1. `in/nfsmw.nro` : 릴리스의 `nfsmw-nx-kor.nro` (저장소에 없다. 받은 파일은 `~/app/ports/nfsmw/` 에 둔다)
2. 게임 데이터 폴더: 아래 구조여야 한다
   ```
   <데이터 폴더>/
     game_root/              디스크 내용 (default.xex, Movies, NFS)
     nfsmw_shaders.nfsp      내 디스크로 만든 셰이더
     nfsmw.toml              설정 (업스트림 설치 페이지가 만든다)
   ```
   `game_root` 와 셰이더는 업스트림 설치 페이지(브라우저에서만 처리되어 파일이 밖으로 나가지 않는다)가 만든 `nfsmw-nx.zip` 을 풀어 얻는다. NRO 만 이 저장소 것으로 바꿔 쓴다.

```
python3 build.py nfsmw --rom <데이터 폴더> --deploy <homebrew 폴더>
```

## 실행 때 주의
- 앨범 애플릿 모드는 메모리가 모자라 안 된다. 게임 덮어쓰기(타이틀 시작 중 R 누르기)나 포워더로 연다.
- 포워더는 **39비트 주소 공간**으로 만든다.
- 첫 레이스는 그래픽 파이프라인을 컴파일하느라 몇 초 끊긴다. 캐시가 SD 에 남아 다음부터는 매끄럽다.
