# 벌레공주 두 사람 (Mushihimesama Futari)

<!-- quick:begin -->
## 필요한 파일과 명령어

필요한 것: Xbox 360판 벌레공주 두 사람 게임 데이터
NRO: `ports/futari/in/futari-nx.nro`

- 스위치 포트 소스: https://github.com/ChanseyIsTheBest/futari-nx

```
python3 build.py check futari    # 빈 칸 확인
python3 build.py futari --zip
```
<!-- quick:end -->

- **엔진/프로젝트**: Xbox 360 정적 리컴파일
- **업스트림**: https://github.com/ChanseyIsTheBest/futari-nx
- **버전**: v1.0.0
- **필요 에셋**: Xbox 360판 벌레공주 두 사람 게임 데이터

```bash
python3 build.py futari --rom <게임 데이터 폴더> --deploy <homebrew 배포 폴더>
```
