# 언더테일 옐로우 (Undertale Yellow)

<!-- quick:begin -->
## 필요한 파일과 명령어

필요한 것: Undertale Yellow 무료 게임 데이터
NRO: `ports/undertale-yellow/in/UndertaleYellow.nro`

- 스위치 포트 소스: https://github.com/NalienDev/Undertale-Yellow-NX

```
python3 build.py check undertale-yellow    # 빈 칸 확인
python3 build.py undertale-yellow --zip
```
<!-- quick:end -->

- **엔진/프로젝트**: GameMaker 스위치 네이티브 디컴파일
- **업스트림**: https://github.com/NalienDev/Undertale-Yellow-NX
- **버전**: v1.0.0
- **필요 에셋**: Undertale Yellow 무료 게임 데이터

```bash
python3 build.py undertale-yellow --rom <게임 데이터 폴더> --deploy <homebrew 배포 폴더>
```
