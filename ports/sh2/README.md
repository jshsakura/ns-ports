# 사일런트 힐 2 (Silent Hill 2)

<!-- quick:begin -->
## 필요한 파일과 명령어

필요한 것: 사일런트 힐 2 PC판(Enhanced Edition) 설치본
NRO: `ports/sh2/in/sh2.nro`

- 스위치 포트 소스: https://github.com/cutarev/sh2-nx

```
python3 build.py check sh2    # 빈 칸 확인
python3 build.py sh2 --zip
```
<!-- quick:end -->

- **엔진/프로젝트**: sh2-nx C 네이티브
- **업스트림**: https://github.com/cutarev/sh2-nx
- **버전**: v0.64
- **필요 에셋**: 사일런트 힐 2 PC판(Enhanced Edition) 설치본

```bash
python3 build.py sh2 --rom <게임 데이터 폴더> --deploy <homebrew 배포 폴더>
```
