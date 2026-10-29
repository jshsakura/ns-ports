# 소닉 어드벤처 2 (Sonic Adventure 2)

<!-- quick:begin -->
## 필요한 파일과 명령어

필요한 것: Xbox 360판 소닉 어드벤처 2 게임 데이터
NRO: `ports/sa2/in/sa2-nx.nro`

- 스위치 포트 소스: https://github.com/ChanseyIsTheBest/sa2-nx

```
python3 build.py check sa2    # 빈 칸 확인
python3 build.py sa2 --zip
```
<!-- quick:end -->

- **엔진/프로젝트**: Xbox 360 정적 리컴파일
- **업스트림**: https://github.com/ChanseyIsTheBest/sa2-nx
- **버전**: v1.0.1
- **필요 에셋**: Xbox 360판 소닉 어드벤처 2 게임 데이터

```bash
python3 build.py sa2 --rom <게임 데이터 폴더> --deploy <homebrew 배포 폴더>
```
