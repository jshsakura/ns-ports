# 둠 64 EX (Doom 64 EX)

<!-- quick:begin -->
## 필요한 파일과 명령어

필요한 것: doom64.wad, doomsnd.sf2
NRO: `ports/doom64/in/doom64ex.nro`

- 원 프로젝트: https://github.com/svkaiser/Doom64EX
- 스위치 포트 소스: https://github.com/fgsfdsfgs/Doom64EX

```
python3 build.py check doom64    # 빈 칸 확인
python3 build.py doom64 --zip
```
<!-- quick:end -->

Doom 64 리버스 엔지니어링 네이티브 C++ 포트

- 엔진: Doom64EX
- 필요한 것: doom64.wad, doomsnd.sf2
- Required files: doom64ex.nro, doom64.wad, doomsnd.sf2, doom64ex.pk3, config.cfg
- Features: Accurate Doom 64 renderer, SoundFont MIDI music, 60fps widescreen
- Status: Verified & 100% playable on Nintendo Switch!

## 사용
`in/doom64ex.nro` 에 빌드된 NRO 를 두고, 내 게임 데이터 폴더를 지정한다.
```
python3 build.py doom64 --rom <게임 데이터 폴더> --zip          # 또는 --deploy <homebrew 폴더>
```
덮어쓸 설정 파일은 `overlay/` 에 있다. 게임 데이터와 NRO 는 저장소에 없다.
