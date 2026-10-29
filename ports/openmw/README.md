# 엘더스크롤 3: 모로윈드 (OpenMW)

<!-- quick:begin -->
## 필요한 파일과 명령어

필요한 것: Morrowind Data Files (Morrowind.esm 등)
NRO: `ports/openmw/in/openmw.nro`

- 원 프로젝트: https://github.com/OpenMW/openmw
- 스위치 포트 소스: https://github.com/fgsfdsfgs/openmw

```
python3 build.py check openmw    # 빈 칸 확인
python3 build.py openmw --zip
```
<!-- quick:end -->

- **엔진/프로젝트**: OpenMW C++ 네이티브
- **업스트림**: https://github.com/fgsfdsfgs/openmw
- **버전**: 0.46.0-nx4
- **필요 에셋**: Morrowind Data Files (Morrowind.esm 등)

```bash
python3 build.py openmw --rom <게임 데이터 폴더> --deploy <homebrew 배포 폴더>
```
