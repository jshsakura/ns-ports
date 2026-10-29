# 히어로즈 오브 마이트 앤 매직 2 (fheroes2)

<!-- quick:begin -->
## 필요한 파일과 명령어

**1. 받아서 둘 것**

| 놓을 위치 | 무엇 | 구하는 곳 |
| :--- | :--- | :--- |
| `ports/fheroes2/in/fheroes2.nro` | 스위치용 NRO | https://github.com/ihhub/fheroes2 의 릴리스를 받거나 직접 빌드 |
| `ports/fheroes2/in/data` | HOMM2 원작 게임 데이터 (HEROES2/DATA) | 내가 가진 정품 데이터 (--rom <폴더> 로 따로 줘도 된다) |
| `ports/fheroes2/icon.jpg` | 앱 아이콘 (256x256 JPEG) (선택) | 직접 구하거나 만든다. 없으면 NRO 에 든 아이콘을 그대로 쓴다 |

**2. 이미지**: 앱 아이콘(`icon.jpg`, 256x256 JPEG)만 쓰이고 없으면 NRO 의 기본 아이콘을 씁니다. 이미지는 저장소에 없으니 필요하면 직접 구해 위 위치에 두세요. 배너와 스크린샷은 다루지 않습니다.

**3. 확인하고 실행**

```
python3 build.py guide fheroes2    # 빈 칸과 구하는 곳 확인
python3 build.py fheroes2 --zip
```

- 스위치 포트 소스: https://github.com/ihhub/fheroes2
<!-- quick:end -->

HOMM2 최신 C++ 오픈소스 리메이크 엔진. 공식 한국어 팩 지원

- 엔진: fheroes2
- 필요한 것: HOMM2 원작 게임 데이터 (HEROES2/DATA)
- Required files: fheroes2.nro, fheroes2.cfg (lang = ko)
- Asset folders: anim/, data/, files/, maps/, music/
- Features: Complete engine rewrite in modern C++, 720p widescreen, Korean font
- Status: Verified & 100% playable on Nintendo Switch!

## 사용
`in/fheroes2.nro` 에 빌드된 NRO 를 두고, 내 게임 데이터 폴더를 지정한다.
```
python3 build.py fheroes2 --rom <게임 데이터 폴더> --zip          # 또는 --deploy <homebrew 폴더>
```
덮어쓸 설정 파일은 `overlay/` 에 있다. 게임 데이터와 NRO 는 저장소에 없다.
