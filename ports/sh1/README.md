# 사일런트 힐 1 (Silent Hill 1)

<!-- quick:begin -->
## 필요한 파일과 명령어

필요한 것: PS1 사일런트 힐 1 롬 데이터
NRO: `ports/sh1/in/silent-hill.nro`

- 원 프로젝트: https://github.com/SlickAmogus/silent-hill-decomp
- 스위치 포트 소스: https://github.com/ChaykaDed/silent-hill-decomp-nx

```
python3 build.py check sh1    # 빈 칸 확인
python3 build.py sh1 --zip
```
<!-- quick:end -->

- **엔진/프로젝트**: PS1 사일런트 힐 C 디컴파일 네이티브
- **업스트림**: https://github.com/ChaykaDed/silent-hill-decomp-nx
- **버전**: v1.1.0
- **필요 에셋**: PS1 사일런트 힐 1 롬 데이터

```bash
python3 build.py sh1 --rom <게임 데이터 폴더> --deploy <homebrew 배포 폴더>
```
