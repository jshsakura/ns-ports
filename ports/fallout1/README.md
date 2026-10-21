# 폴아웃 1 (Fallout 1)

폴아웃 1 커뮤니티 에디션 기반. 한국어 패치 및 스위치 컨트롤러 지원

- 엔진: fallout1-ce
- 필요한 것: master.dat, critter.dat (PC판 데이터)
- Required files: master.dat, critter.dat, fallout1.nro
- Korean text assets: data/text/korean/ (1,500+ dialog files)
- Korean fonts: fonts/korean/ (font.ini, font.ttf, zpix.ttf)
- Status: Verified & 100% playable in Korean!

## 사용
`in/fallout1.nro` 에 빌드된 NRO 를 두고, 내 게임 데이터 폴더를 지정한다.
```
python3 build.py fallout1 --rom <게임 데이터 폴더> --zip          # 또는 --deploy <homebrew 폴더>
```
덮어쓸 설정 파일은 `overlay/` 에 있다. 게임 데이터와 NRO 는 저장소에 없다.
