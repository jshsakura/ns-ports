# 토치라이트 (Torchlight)

<!-- quick:begin -->
## 필요한 파일과 명령어

필요한 것: Xbox 360판 토치라이트 게임 데이터
NRO: `ports/torchlight/in/torchlight-nx.nro`

- 스위치 포트 소스: https://github.com/liartes/torchlight-nx

```
python3 build.py check torchlight    # 빈 칸 확인
python3 build.py torchlight --zip
```
<!-- quick:end -->

- **엔진/프로젝트**: Xbox 360 정적 리컴파일
- **업스트림**: https://github.com/liartes/torchlight-nx
- **버전**: v1.0.0
- **필요 에셋**: Xbox 360판 토치라이트 게임 데이터

```bash
python3 build.py torchlight --rom <게임 데이터 폴더> --deploy <homebrew 배포 폴더>
```
