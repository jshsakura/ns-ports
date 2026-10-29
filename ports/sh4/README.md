# 사일런트 힐 4: 더 룸 (Silent Hill 4)

<!-- quick:begin -->
## 필요한 파일과 명령어

필요한 것: 사일런트 힐 4 GOG PC판 설치본
NRO: `ports/sh4/in/sh4.nro`

- 스위치 포트 소스: https://github.com/72ak/sh4-nx

```
python3 build.py check sh4    # 빈 칸 확인
python3 build.py sh4 --zip
```
<!-- quick:end -->

- **엔진/프로젝트**: sh4-nx C 네이티브
- **업스트림**: https://github.com/72ak/sh4-nx
- **버전**: v0.1
- **필요 에셋**: 사일런트 힐 4 GOG PC판 설치본

```bash
python3 build.py sh4 --rom <게임 데이터 폴더> --deploy <homebrew 배포 폴더>
```
