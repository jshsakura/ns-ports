# 카운터 스트라이크 1.6 스위치 포트 (신형 Xash3D FWGS)

신형 엔진(FWGS)과 cs16-client 로 만든 스위치용 카스. 한글 입력과 표시, 터치/게임패드/자이로 조작,
푸시투토크를 넣었다. 빌드 절차와 변경 내역은 `BUILD.md`.

## 폴더
| 경로 | 내용 |
|---|---|
| `patches/` | 업스트림 소스에 얹는 패치(xash3d-fwgs, mainui, cs16-client, regamedll, yapb) |
| `overlay-common/` | 모든 판에 덮는 파일(`userconfig.cfg`, 배경, 터치 설정, `ClientScheme.res`) |
| `overlay-ko/` | 한글판에만 덮는 파일(한글 사전, 폰트, 메뉴 이미지, 한글 터치 문구) |
| `overlay-en/` | 순정(영문)판용 원본 터치 문구 |
| `port.json` | 조립 프로필(판 `ko`, `en`) |
| `scripts/` | 빌드, 한글 이미지와 문구 생성 도구 |
| `ref/` | 원본 이미지와 게임 데이터 md5 목록 |
| `favorites.example.txt` | 즐겨찾기 서버 예시 |
| `src/` `out/` `logs/` | 받은 소스, 산출물, 로그(저장소에 올리지 않음) |

## 소스 받기
업스트림 커밋에 `patches/*.patch` 를 적용한다.
- `FWGS/xash3d-fwgs` 03a396e (+ `FWGS/mainui_cpp` bb47191 서브모듈)
- `Velaron/cs16-client` 9778fec (+ ReGameDLL_CS 7be9d59, yapb 4967a22)
- `fgsfdsfgs/libsolder` 36e5f31

## 빌드와 조립 (007 포트와 같은 방식)
```
python3 build.py cstrike --rom <내 cstrike/valve 데이터 폴더>                  # 한글판을 dist/switch/ 에 조립
python3 build.py cstrike --rom <데이터> --variant original --zip                      # 순정(영문)판 + zip
python3 build.py cstrike --rom <데이터> --deploy <homebrew 폴더>                # 쇼핑몰 폴더에 바로 반영
python3 build.py cstrike --skip-build --dry-run                                # 빌드 생략, 바꿀 파일만 보기
```
1. 업스트림을 고정 커밋으로 `ports/cstrike/src/` 에 받아 `patches/` 를 적용한다(처음 한 번).
2. devkitPro 도커에서 엔진과 게임 코드를 빌드한다. 도커가 필요하다.
3. 바이너리, `overlay-*`, 내 게임 데이터(하드링크)를 합쳐 조립한다.
4. `--deploy` 를 주고 설정에 서버 주소와 토큰이 있으면 폴더 재스캔과 종류(port) 지정까지 서버 API 로 한다.

옵션은 `ns-ports.config.json` 에 적어 둘 수 있다(`ns-ports.config.example.json` 참고, 저장소에 올리지 않는다).
우선순위는 명령줄, 환경 변수, 설정 파일, 프로필 순이다. 토큰은 설정 파일에 쓰지 않고 `token_file` 이 가리키는 파일에서 읽는다.
같은 크기인데 내용이 바뀐 파일은 끝에 여분을 붙여 쇼핑몰이 새로 받게 한다(아래 함정).
`--data`(= `--rom`) 는 다른 판이 덮어쓴 파일을 가져오지 않는다.

## 즐겨찾기 서버
`favorites.example.txt` 를 `favorites.txt` 로 복사해 한 줄에 `주소:포트` 로 적고 `register.py` 를 돌리면
`cstrike/default_favorites.lst` 가 만들어지고, 게임이 시작할 때 이 목록의 서버를 즐겨찾기에 없으면 채워 넣는다(사용자가 지운 것도 다시 들어온다).
기기에서 추가한 즐겨찾기는 쇼핑몰 업데이트 때 이 목록으로 덮일 수 있다.

## 게임 데이터
이 저장소에는 게임 데이터가 없다. 정품 `cstrike/`, `valve/` 데이터를 쇼핑몰 폴더에 두고 `overlay-*` 와 산출물을 덮는다.
원본 파일 목록은 `ref/cs-data-manifest.md5`.

## 쇼핑몰 동기화 함정: 같은 크기로 바꾼 파일이 기기에 안 받아진다 (2026-10-20)

폴더 설치형 홈브류의 파일을 같은 크기로 교체하면 기기에 새 내용이 안 내려갈 수 있다.
앱 hash 가 같으면 기기는 "설치됨"으로 보고 동기화를 시작하지 않는다. 서버의 sha256 캐시 키가
`크기:mtime:inode` 라서 복사 도구로 덮어쓰면 옛 해시가 계속 나가는 것으로 추정한다(서버에서 재현하지는 않았다).
서버에 `ctimeMs` 를 키에 넣어 달라고 요청해 두었다. 그때까지는 `register.py` 가 크기를 바꿔 준다.
올린 뒤에는 기기에서 새 파일을 실제로 받았는지 먼저 확인한다.

## 공개용 순정판 (레딧 등)
`scripts/release-global.sh` 가 `out/release/cstrike-switch-global.zip` 을 만든다. 게임 데이터, 개인 배경 이미지, 한글 파일은 넣지 않고
영문 설명(`release/README-global.txt`)과 패치(`source/`)를 함께 담는다. 쇼핑몰에는 올리지 않는다.

## Third-party assets
- `overlay-ko/cstrike/gfx/fonts/*.ttf` are NanumSquareRound (Naver Nanum fonts, SIL Open Font License 1.1), stored under the file names the engine looks for.
- Touch button icons are generic drawings made for this port. App icons are not redistributed; link them with `icon_url` / `downloads`.
- Menu background and loading screen (SteamGridDB heroes, not stored in this repository; `port.json` `art` has the links and sha256): by F R A N K Z E B (hero/152895) and Asterdenpa (hero/123728).
