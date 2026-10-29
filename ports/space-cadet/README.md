# 3D 핀볼: 스페이스 카뎃 (Space Cadet Pinball)

<!-- quick:begin -->
## 필요한 파일과 명령어

**1. 받아서 둘 것**

| 놓을 위치 | 무엇 | 구하는 곳 |
| :--- | :--- | :--- |
| `ports/space-cadet/in/SpaceCadetPinball.nro` | 스위치용 NRO (선택) | 안 둬도 된다. 없으면 averne/SpaceCadetPinball-NX 릴리스 Release_1.1.1-NX3 에서 자동으로 받는다 |
| `ports/space-cadet/in/data` | Windows 3D Pinball 사운드 및 테이블 데이터 | 내가 가진 정품 데이터 (--rom <폴더> 로 따로 줘도 된다) |
| `ports/space-cadet/icon.jpg` | 앱 아이콘 (256x256 JPEG) (선택) | 직접 구하거나 만든다. 없으면 NRO 에 든 아이콘을 그대로 쓴다 |

**2. 이미지**: 앱 아이콘(`icon.jpg`, 256x256 JPEG)만 쓰이고 없으면 NRO 의 기본 아이콘을 씁니다. 이미지는 저장소에 없으니 필요하면 직접 구해 위 위치에 두세요. 배너와 스크린샷은 다루지 않습니다.

**3. 확인하고 실행**

```
python3 build.py guide space-cadet    # 빈 칸과 구하는 곳 확인
python3 build.py space-cadet --rom <내 게임 데이터 폴더> --zip
```

NRO 는 구하지 않아도 됩니다. `in/` 에 없으면 averne/SpaceCadetPinball-NX 릴리스 Release_1.1.1-NX3 에서 받아 sha256 을 확인하고 씁니다.

- 원 프로젝트: https://github.com/k4zmu2a/SpaceCadetPinball
- 스위치 포트 소스: https://github.com/averne/SpaceCadetPinball-NX
<!-- quick:end -->

- **엔진/프로젝트**: SpaceCadetPinball C++ 역공학 네이티브
- **업스트림**: https://github.com/averne/SpaceCadetPinball-NX
- **버전**: v1.1.1-NX3
- **필요 에셋**: Windows 3D Pinball 사운드 및 테이블 데이터

```bash
python3 build.py space-cadet --rom <게임 데이터 폴더> --deploy <homebrew 배포 폴더>
```
