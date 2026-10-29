# 데이토나 USA (Daytona USA)

<!-- quick:begin -->
## 필요한 파일과 명령어

필요한 것: MAME Model 2 daytona.zip (Rev A) 롬
NRO: `ports/daytona-usa/in/Daytona.nro`

- 스위치 포트 소스: https://github.com/Thorhax/Daytona-NX-Modern

```
python3 build.py check daytona-usa    # 빈 칸 확인
python3 build.py daytona-usa --zip
```
<!-- quick:end -->

- **엔진/프로젝트**: Sega Model 2 정적 리컴파일
- **업스트림**: https://github.com/Thorhax/Daytona-NX-Modern
- **버전**: v1.1.0
- **필요 에셋**: MAME Model 2 daytona.zip (Rev A) 롬

```bash
python3 build.py daytona-usa --rom <게임 데이터 폴더> --deploy <homebrew 배포 폴더>
```
