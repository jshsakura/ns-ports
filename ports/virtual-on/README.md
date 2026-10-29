# 전뇌전기 버추얼 온 (Cyber Troopers Virtual-On)

<!-- quick:begin -->
## 필요한 파일과 명령어

**1. 받아서 둘 것**

| 놓을 위치 | 무엇 | 구하는 곳 |
| :--- | :--- | :--- |
| `ports/virtual-on/in/Virtual-On.nro` | 스위치용 NRO | https://github.com/Thorhax/Virtual-On-NX 의 릴리스를 받거나 직접 빌드 |
| `ports/virtual-on/in/data` | MAME Model 2 von.zip 롬 | 내가 가진 정품 데이터 (--rom <폴더> 로 따로 줘도 된다) |
| `ports/virtual-on/icon.jpg` | 앱 아이콘 (256x256 JPEG) (선택) | 직접 구하거나 만든다. 없으면 NRO 에 든 아이콘을 그대로 쓴다 |

**2. 이미지**: 앱 아이콘(`icon.jpg`, 256x256 JPEG)만 쓰이고 없으면 NRO 의 기본 아이콘을 씁니다. 이미지는 저장소에 없으니 필요하면 직접 구해 위 위치에 두세요. 배너와 스크린샷은 다루지 않습니다.

**3. 확인하고 실행**

```
python3 build.py guide virtual-on    # 빈 칸과 구하는 곳 확인
python3 build.py virtual-on --zip
```

- 스위치 포트 소스: https://github.com/Thorhax/Virtual-On-NX
<!-- quick:end -->

- **엔진/프로젝트**: Sega Model 2 정적 리컴파일 + 소프트웨어 래스터라이저
- **업스트림**: https://github.com/Thorhax/Virtual-On-NX
- **버전**: v1.2.0
- **필요 에셋**: MAME Model 2 von.zip 롬

```bash
python3 build.py virtual-on --rom <게임 데이터 폴더> --deploy <homebrew 배포 폴더>
```
