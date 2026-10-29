# The Legend of Zelda: A Link to the Past (zelda3-ko)

<!-- quick:begin -->
## 필요한 파일과 명령어

**1. 받아서 둘 것**

| 놓을 위치 | 무엇 | 구하는 곳 |
| :--- | :--- | :--- |
| `ports/zelda3-ko/in/zelda3.nro` | snesrev/zelda3 Switch 빌드 NRO (선택) | 이 저장소가 Docker(devkitPro)로 직접 빌드해서 채운다. 따로 구할 필요 없다 |
| `ports/zelda3-ko/in/data/zelda3_assets.dat` | 내 롬에서 뽑은 에셋 파일 (한글 판은 한글 글리프 표가 들어간 것) | snesrev/zelda3 의 에셋 추출 도구로 내 롬에서 만든다. --rom <그 파일이 든 폴더> 로 알려 준다 |
| `ports/zelda3-ko/icon.jpg` | 앱 아이콘 (256x256 JPEG) (선택) | 직접 구하거나 만든다. 없으면 NRO 에 든 아이콘을 그대로 쓴다 |

**2. 이미지**: 앱 아이콘(`icon.jpg`, 256x256 JPEG)만 쓰이고 없으면 NRO 의 기본 아이콘을 씁니다. 이미지는 저장소에 없으니 필요하면 직접 구해 위 위치에 두세요. 배너와 스크린샷은 다루지 않습니다.

**3. 확인하고 실행**

```
python3 build.py guide zelda3-ko    # 빈 칸과 구하는 곳 확인
python3 build.py zelda3-ko --zip
```

- 스위치 포트 소스: https://github.com/snesrev/zelda3
<!-- quick:end -->

snesrev/zelda3 (`a23632a`) 의 스위치 빌드. 두 판이 있다.

- `original`: 업스트림 그대로.
- `ko`: `patches/zelda3-ko.patch` (한글 대사 렌더링: 16px 가변폭 글리프)를 얹은 판.

## 어떤 파일을 어디서 구해 어디에 두나

| # | 파일 | 어디서 | 어디에 |
| :-: | :--- | :--- | :--- |
| 1 | `zelda3.nro` | 구하지 않는다. 빌드 때 Docker(devkitPro)로 이 저장소가 소스를 받아 만든다 | `ports/zelda3-ko/in/zelda3.nro` (자동) |
| 2 | `zelda3_assets.dat` | 내 정품 롬에서 snesrev/zelda3 의 에셋 추출 도구로 만든다. 한글 판은 한글 글리프 표가 들어간 것이 필요하다 | 옮기지 않는다. 그 파일이 든 폴더를 `--rom` 으로 알려 준다 |

한글 글리프 표는 한국어 패치에서 저장소 밖에서 만들어 `zelda3_assets.dat` 에 넣은 것이라, 이 저장소에는 만드는 도구가 없다.
Docker 가 깔려 있어야 하고, 롬과 에셋은 저장소에 없다.

## 조립

```
python3 build.py zelda3-ko --rom <zelda3_assets.dat 이 든 폴더> --variant ko --zip
python3 build.py zelda3-ko --rom <폴더> --variant original --zip
python3 build.py zelda3-ko --rom <폴더> --skip-build --zip     # in/zelda3.nro 가 이미 있으면 빌드를 건너뛴다
```

조립 결과에는 `zelda3.ini`(한글 판은 `Language = ko`)가 함께 들어간다. 결과는 `ports/zelda3-ko/dist/switch/` 이다.
상태: 한글 판 실기 확인 완료(메인테이너).
