# 3D 핀볼: 스페이스 카뎃 (Space Cadet Pinball)

<!-- quick:begin -->
## 필요한 파일과 명령어

필요한 것: Windows 3D Pinball 사운드 및 테이블 데이터
NRO: `ports/space-cadet/in/SpaceCadetPinball.nro`

- 원 프로젝트: https://github.com/k4zmu2a/SpaceCadetPinball
- 스위치 포트 소스: https://github.com/averne/SpaceCadetPinball-NX

```
python3 build.py check space-cadet    # 빈 칸 확인
python3 build.py space-cadet --zip
```
<!-- quick:end -->

- **엔진/프로젝트**: SpaceCadetPinball C++ 역공학 네이티브
- **업스트림**: https://github.com/averne/SpaceCadetPinball-NX
- **버전**: v1.1.1-NX3
- **필요 에셋**: Windows 3D Pinball 사운드 및 테이블 데이터

```bash
python3 build.py space-cadet --rom <게임 데이터 폴더> --deploy <homebrew 배포 폴더>
```
