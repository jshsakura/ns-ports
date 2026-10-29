# 소닉 로보 블래스트 2 (Sonic Robo Blast 2)

<!-- quick:begin -->
## 필요한 파일과 명령어

**1. 받아서 둘 것**

| 놓을 위치 | 무엇 | 구하는 곳 |
| :--- | :--- | :--- |
| `ports/srb2/in/srb2switch22.nro` | 스위치용 NRO | https://github.com/P-AS/srb2-switch 의 릴리스를 받거나 직접 빌드 |
| `ports/srb2/in/data` | 자체 무료 풀버전 데이터 포함 | 내가 가진 정품 데이터 (--rom <폴더> 로 따로 줘도 된다) |
| `ports/srb2/icon.jpg` | 앱 아이콘 (256x256 JPEG) (선택) | 직접 구하거나 만든다. 없으면 NRO 에 든 아이콘을 그대로 쓴다 |

**2. 이미지**: 앱 아이콘(`icon.jpg`, 256x256 JPEG)만 쓰이고 없으면 NRO 의 기본 아이콘을 씁니다. 이미지는 저장소에 없으니 필요하면 직접 구해 위 위치에 두세요. 배너와 스크린샷은 다루지 않습니다.

**3. 확인하고 실행**

```
python3 build.py guide srb2    # 빈 칸과 구하는 곳 확인
python3 build.py srb2 --zip
```

- 스위치 포트 소스: https://github.com/P-AS/srb2-switch
<!-- quick:end -->

- 엔진: Sonic Team Junior (Doom Engine 3D 모드)
- 라이선스: 완전 무료 오픈소스 팬게임 풀버전
- 설치 경로: `sdmc:/switch/srb2/`
- 실행 파일: `srb2switch22.nro`
