# 젤다의 전설: 오니 링크의 시작 (Zelda: OLB)

<!-- quick:begin -->
## 필요한 파일과 명령어

필요한 것: 자체 무료 데이터 포함
NRO: `ports/zelda-olb/in/ZeldaOLB.nro`

- 스위치 포트 소스: https://github.com/worthis/ZeldaOLB-new-engine

```
python3 build.py check zelda-olb    # 빈 칸 확인
python3 build.py zelda-olb --zip
```
<!-- quick:end -->

- **엔진/프로젝트**: C++ 네이티브 엔진
- **업스트림**: https://github.com/worthis/ZeldaOLB-new-engine
- **버전**: v1.1.1
- **필요 에셋**: 자체 무료 데이터 포함

```bash
python3 build.py zelda-olb --rom <게임 데이터 폴더> --deploy <homebrew 배포 폴더>
```
