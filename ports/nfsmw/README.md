# 니드 포 스피드: 모스트 원티드 (Need for Speed: Most Wanted)

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
