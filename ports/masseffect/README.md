# 매스 이펙트 1 (Mass Effect)

<!-- quick:begin -->
## 필요한 파일과 명령어

필요한 것: Xbox 360판 매스 이펙트 1 게임 데이터
NRO: `ports/masseffect/in/masseffect-nx.nro`

- 스위치 포트 소스: https://github.com/nebadasSwifty/masseffect-nx

```
python3 build.py check masseffect    # 빈 칸 확인
python3 build.py masseffect --zip
```
<!-- quick:end -->

- **엔진/프로젝트**: Xbox 360 정적 리컴파일
- **업스트림**: https://github.com/nebadasSwifty/masseffect-nx
- **버전**: v0.2.1
- **필요 에셋**: Xbox 360판 매스 이펙트 1 게임 데이터

```bash
python3 build.py masseffect --rom <게임 데이터 폴더> --deploy <homebrew 배포 폴더>
```
