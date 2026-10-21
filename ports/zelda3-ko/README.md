# 젤다의 전설: 신들의 트라이포스 (A Link to the Past)

SNES 신들의 트라이포스 C 재구현 포트. 와이드스크린 16:9 60fps & 한국어 텍스트 지원

- 엔진: snes-zelda3
- 필요한 것: zelda3_assets.dat
- Required files: zelda3.nro, zelda3_assets.dat, zelda3.ini
- Features: Native 60fps C code execution, 16:9 widescreen, Korean translation
- Status: Verified & 100% playable in Korean!

## 사용
`in/zelda3.nro` 에 빌드된 NRO 를 두고, 내 게임 데이터 폴더를 지정한다.
```
python3 build.py zelda3-ko --rom <게임 데이터 폴더> --zip          # 또는 --deploy <homebrew 폴더>
```
덮어쓸 설정 파일은 `overlay/` 에 있다. 게임 데이터와 NRO 는 저장소에 없다.
