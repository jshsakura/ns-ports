# The Legend of Zelda: A Link to the Past (zelda3-ko)

<!-- quick:begin -->
## 필요한 파일과 명령어

이 포트는 소스부터 빌드하거나 전용 레시피를 씁니다. 필요한 것: zelda3_assets.dat


- 스위치 포트 소스: https://github.com/snesrev/zelda3
<!-- quick:end -->

snesrev/zelda3 (`a23632a`) 의 스위치 빌드. 두 판이 있다.

- `original`: 업스트림 그대로.
- `ko`: `patches/zelda3-ko.patch` (한글 대사 렌더링: 16px 가변폭 글리프)를 얹은 판.

한글 글리프/대사 표는 한국어 패치에서 저장소 밖에서 만들어 `zelda3_assets.dat` 에 들어간다. 그 파일은 `--rom` 폴더에 직접 준비한다.
ROM 과 에셋은 저장소에 없다.

```
python3 build.py zelda3-ko --rom <zelda3_assets.dat 이 든 폴더> --variant ko --zip
python3 build.py zelda3-ko --rom <폴더> --variant original --deploy <homebrew 폴더>
```
빌드는 devkitPro 도커로 한다. 조립 결과에는 `zelda3.ini`(한글판은 `Language = ko`)가 함께 들어간다.
상태: 한글판 실기 확인 완료(메인테이너).
