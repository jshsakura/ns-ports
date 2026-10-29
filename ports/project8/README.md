# 토니 호크 프로젝트 8 (Tony Hawk Project 8)

<!-- quick:begin -->
## 필요한 파일과 명령어

필요한 것: Xbox 360판 토니 호크 프로젝트 8 게임 데이터
NRO: `ports/project8/in/project8-sw.nro`

- 스위치 포트 소스: https://github.com/R-drg/project8-sw

```
python3 build.py check project8    # 빈 칸 확인
python3 build.py project8 --zip
```
<!-- quick:end -->

- **엔진/프로젝트**: Xbox 360 정적 리컴파일
- **업스트림**: https://github.com/R-drg/project8-sw
- **버전**: v1.0.0
- **필요 에셋**: Xbox 360판 토니 호크 프로젝트 8 게임 데이터

```bash
python3 build.py project8 --rom <게임 데이터 폴더> --deploy <homebrew 배포 폴더>
```
