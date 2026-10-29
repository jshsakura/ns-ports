# 히어로즈 오브 마이트 앤 매직 3 (VCMI)

<!-- quick:begin -->
## 필요한 파일과 명령어

필요한 것: HOMM3 Data 및 Maps 폴더
NRO: `ports/vcmi/in/vcmi.nro`

- 원 프로젝트: https://github.com/vcmi/vcmi
- 스위치 포트 소스: https://github.com/NaGaa95/vcmi_nx

```
python3 build.py check vcmi    # 빈 칸 확인
python3 build.py vcmi --zip
```
<!-- quick:end -->

- **엔진/프로젝트**: VCMI C++ 네이티브
- **업스트림**: https://github.com/vcmi/vcmi
- **버전**: 1.5.0-nx
- **필요 에셋**: HOMM3 Data 및 Maps 폴더

```bash
python3 build.py vcmi --rom <게임 데이터 폴더> --deploy <homebrew 배포 폴더>
```
