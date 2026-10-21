# 하프라이프 1 (Half-Life)

Xash3D 엔진 기반 하프라이프 1 네이티브 포트. 공식 한국어 풀더빙 음성 연동

- 엔진: Xash3D-FWGS
- 필요한 것: valve/ 폴더 (원작 PC 게임 데이터)
- Required files: half-life.nro, filesystem_stdio.so, libmenu.so, libref_gl.so
- Game data: valve/ (Half-Life), bshift/ (Blue Shift), gearbox/ (Opposing Force)
- Korean assets: Official Korean voice dubbing in valve/sound/ (sentences.txt, fvox, scientist)
- Features: Motion controls (gyro aim), 60fps, widescreen
- Status: Verified & 100% playable in Korean!

## 사용
`in/half-life.nro` 에 빌드된 NRO 를 두고, 내 게임 데이터 폴더를 지정한다.
```
python3 build.py half-life --rom <게임 데이터 폴더> --zip          # 또는 --deploy <homebrew 폴더>
```
덮어쓸 설정 파일은 `overlay/` 에 있다. 게임 데이터와 NRO 는 저장소에 없다.
