# 동굴 이야기 (Cave Story, doukutsu-rs)

<!-- quick:begin -->
## 필요한 파일과 명령어

**1. 받아서 둘 것**

| 놓을 위치 | 무엇 | 구하는 곳 |
| :--- | :--- | :--- |
| `ports/doukutsu-rs/in/doukutsu-rs.nro` | 스위치용 빌드 NRO | - |
| `ports/doukutsu-rs/in/data` | Cave Story 게임 데이터 (data/) | - |
| `ports/doukutsu-rs/icon.jpg` | 앱 아이콘 (256x256 JPEG) (선택) | 직접 구하거나 만든다. 없으면 NRO 에 든 아이콘을 그대로 쓴다 |

**2. 이미지**: 앱 아이콘(`icon.jpg`, 256x256 JPEG)만 쓰이고 없으면 NRO 의 기본 아이콘을 씁니다. 이미지는 저장소에 없으니 필요하면 직접 구해 위 위치에 두세요. 배너와 스크린샷은 다루지 않습니다.

**3. 확인하고 실행**

```
python3 build.py guide doukutsu-rs    # 빈 칸과 구하는 곳 확인
python3 build.py doukutsu-rs --rom <내 게임 데이터 폴더> --zip
```

- 원 프로젝트: https://github.com/doukutsu-rs/doukutsu-rs
<!-- quick:end -->

개인 테스트 기록. 한국어화 여부는 아직 확인하지 않았다.
