# 젤다의 전설: 시간의 오카리나 HD (Ocarina of Time)

Ship of Harkinian v9.3.0 C++ 네이티브 포트 + 60FPS 와이드스크린 + 한글 Pretendard HD 에셋(3.89GB) 실기 검수 완료

- 엔진: Ship of Harkinian v9.3.0
- 필요한 것: oot.o2r, soh.o2r, mods/OoT_Reloaded_Korean_Pretendard_HD.o2r, shipofharkinian.json
- Required files: zelda-oot-hd.nro, oot.o2r, soh.o2r, shipofharkinian.json
- HD Korean Mod: mods/OoT_Reloaded_Korean_Pretendard_HD.o2r (3.89 GB)
- Configuration: shipofharkinian.json (Languages=3 / Japanese Korean Mode)
- Status: Verified & 100% playable in Korean with 60FPS & Gyro!

## 사용
`in/zelda-oot-hd.nro` 에 빌드된 NRO 를 두고, 내 게임 데이터 폴더를 지정한다.
```
python3 build.py zelda-oot-hd --rom <게임 데이터 폴더> --zip          # 또는 --deploy <homebrew 폴더>
```
덮어쓸 설정 파일은 `overlay/` 에 있다. 게임 데이터와 NRO 는 저장소에 없다.
