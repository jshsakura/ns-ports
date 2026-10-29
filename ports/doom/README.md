# GZDoom (Doom 1 & FreeDoom)

<!-- quick:begin -->
## 필요한 파일과 명령어

**1. 받아서 둘 것**

| 놓을 위치 | 무엇 | 구하는 곳 |
| :--- | :--- | :--- |
| `ports/doom/in/gzdoom_launcher.nro` | 스위치용 NRO | https://github.com/fgsfdsfgs/gzdoom 의 릴리스를 받거나 직접 빌드 |
| `ports/doom/in/data` | 자체 무료 IWAD 포함 (상용 IWAD 추가 지원) | 내가 가진 정품 데이터 (--rom <폴더> 로 따로 줘도 된다) |
| `ports/doom/icon.jpg` | 앱 아이콘 (256x256 JPEG) (선택) | 직접 구하거나 만든다. 없으면 NRO 에 든 아이콘을 그대로 쓴다 |

**2. 이미지**: 앱 아이콘(`icon.jpg`, 256x256 JPEG)만 쓰이고 없으면 NRO 의 기본 아이콘을 씁니다. 이미지는 저장소에 없으니 필요하면 직접 구해 위 위치에 두세요. 배너와 스크린샷은 다루지 않습니다.

**3. 확인하고 실행**

```
python3 build.py guide doom    # 빈 칸과 구하는 곳 확인
python3 build.py doom --zip
```

- 원 프로젝트: https://github.com/ZDoom/gzdoom
- 스위치 포트 소스: https://github.com/fgsfdsfgs/gzdoom
<!-- quick:end -->

- 엔진: GZDoom NX (fgsfdsfgs)
- 라이선스: 자유 배포 가능 (둠 1 셰어웨어 및 프리둠 Phase 1 & 2 완전 포함)
- 설치 경로: `sdmc:/switch/doom/`
- 실행 파일: `gzdoom_launcher.nro`
