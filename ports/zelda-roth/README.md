# 젤다의 전설: 하일리아인의 귀환 (Zelda: ROTH)

<!-- quick:begin -->
## 필요한 파일과 명령어

필요한 것: 자체 무료 데이터 포함
NRO: `ports/zelda-roth/in/ZeldaROTH.nro`

- 스위치 포트 소스: https://github.com/worthis/ZeldaROTH-new-engine

```
python3 build.py check zelda-roth    # 빈 칸 확인
python3 build.py zelda-roth --zip
```
<!-- quick:end -->

- **엔진/프로젝트**: C++ 네이티브 엔진
- **업스트림**: https://github.com/worthis/ZeldaROTH-new-engine
- **버전**: v1.1.4
- **필요 에셋**: 자체 무료 데이터 포함

```bash
python3 build.py zelda-roth --rom <게임 데이터 폴더> --deploy <homebrew 배포 폴더>
```
