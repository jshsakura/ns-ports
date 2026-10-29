# 시저 3 (Caesar III / Julius)

<!-- quick:begin -->
## 필요한 파일과 명령어

필요한 것: Caesar 3 PC 설치 데이터
NRO: `ports/caesar3/in/caesar3.nro`

- 스위치 포트 소스: https://github.com/bvschaik/julius

```
python3 build.py check caesar3    # 빈 칸 확인
python3 build.py caesar3 --zip
```
<!-- quick:end -->

고전 도시 건설 시뮬레이션 Julius 오픈소스 엔진 + 공식 한국어 패치

- 엔진: Julius
- 필요한 것: Caesar 3 PC 설치 데이터
- Required files: julius.nro / caesar3.nro, korean-v2.555, C3 assets
- Features: High-res widescreen display, touch control, UI improvements, Korean text
- Status: Verified & 100% playable on Nintendo Switch!

## 사용
`in/caesar3.nro` 에 빌드된 NRO 를 두고, 내 게임 데이터 폴더를 지정한다.
```
python3 build.py caesar3 --rom <게임 데이터 폴더> --zip          # 또는 --deploy <homebrew 폴더>
```
덮어쓸 설정 파일은 `overlay/` 에 있다. 게임 데이터와 NRO 는 저장소에 없다.
