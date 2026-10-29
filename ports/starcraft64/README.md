# 스타크래프트 64 (StarCraft 64 Recomp)

<!-- quick:begin -->
## 필요한 파일과 명령어

필요한 것: StarCraft 64 (USA) ROM (.z64)
NRO: `ports/starcraft64/in/starcraft64.nro`

- 스위치 포트 소스: https://github.com/gabryboy12-ai/StarCraft64-NX

```
python3 build.py check starcraft64    # 빈 칸 확인
python3 build.py starcraft64 --zip
```
<!-- quick:end -->

StarCraft 64 정적 리컴파일 네이티브 포트 + 한국어 번역 & HD 커스텀 베젤

- 엔진: StarCraft64-recomp
- 필요한 것: StarCraft 64 (USA) ROM (.z64)
- Required files: starcraft64.nro, rom.z64, bezel.rgba
- Korean translation pipeline: Verified via sc64-korean
- Features: Native 60fps static recompilation, Korean font/dialog, HD custom bezel
- Status: Verified & 100% playable on Nintendo Switch!

## 사용
`in/starcraft64.nro` 에 빌드된 NRO 를 두고, 내 게임 데이터 폴더를 지정한다.
```
python3 build.py starcraft64 --rom <게임 데이터 폴더> --zip          # 또는 --deploy <homebrew 폴더>
```
덮어쓸 설정 파일은 `overlay/` 에 있다. 게임 데이터와 NRO 는 저장소에 없다.
