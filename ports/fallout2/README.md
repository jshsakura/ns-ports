# 폴아웃 2 (Fallout 2)

<!-- quick:begin -->
## 필요한 파일과 명령어

**1. 받아서 둘 것**

| 놓을 위치 | 무엇 | 구하는 곳 |
| :--- | :--- | :--- |
| `ports/fallout2/in/fallout2.nro` | 스위치용 NRO | https://github.com/alexbatalov/fallout2-ce 의 릴리스를 받거나 직접 빌드 |
| `ports/fallout2/in/data` | master.dat, critter.dat (PC판 데이터) | 내가 가진 정품 데이터 (--rom <폴더> 로 따로 줘도 된다) |
| `ports/fallout2/icon.jpg` | 앱 아이콘 (256x256 JPEG) (선택) | 직접 구하거나 만든다. 없으면 NRO 에 든 아이콘을 그대로 쓴다 |

**2. 이미지**: 앱 아이콘(`icon.jpg`, 256x256 JPEG)만 쓰이고 없으면 NRO 의 기본 아이콘을 씁니다. 이미지는 저장소에 없으니 필요하면 직접 구해 위 위치에 두세요. 배너와 스크린샷은 다루지 않습니다.

**3. 확인하고 실행**

```
python3 build.py guide fallout2    # 빈 칸과 구하는 곳 확인
python3 build.py fallout2 --zip
```

- 스위치 포트 소스: https://github.com/alexbatalov/fallout2-ce
<!-- quick:end -->

폴아웃 2 커뮤니티 에디션(fallout2-ce) 기반. CP949 FreeType 한글 폰트 & 1,033개 한글 대화 연동 실기 검수 완료

- 엔진: fallout2-ce
- 필요한 것: master.dat, critter.dat (PC판 데이터)
- Required files: master.dat, critter.dat, fallout2.nro
- Korean text assets: data/text/korean/ (1,033+ dialog files)
- Korean fonts: fonts/korean/ (font.ini, font.ttf, zpix.ttf)
- Configuration: fallout2.cfg (language=korean)
- Status: Verified & 100% playable in Korean!

## 사용
`in/fallout2.nro` 에 빌드된 NRO 를 두고, 내 게임 데이터 폴더를 지정한다.
```
python3 build.py fallout2 --rom <게임 데이터 폴더> --zip          # 또는 --deploy <homebrew 폴더>
```
덮어쓸 설정 파일은 `overlay/` 에 있다. 게임 데이터와 NRO 는 저장소에 없다.
