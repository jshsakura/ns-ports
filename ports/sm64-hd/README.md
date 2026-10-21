# 슈퍼 마리오 64 HD (Super Mario 64)

N64 슈퍼마리오 64 네이티브 포트 + 와이드스크린 60fps & HD 텍스처 팩

- 엔진: sm64ex-nx / Mupen64Plus-Next HD
- 필요한 것: N64 ROM (baserom.us.z64)
- Required files: sm64-hd.nro, game/Super Mario 64.z64, sm64-hd.opt
- Features: 16:9 widescreen 60fps, GlideN64 HD texture enhancements, Korean UI
- Status: Verified & 100% playable in Korean!

## 사용
`in/sm64-hd.nro` 에 빌드된 NRO 를 두고, 내 게임 데이터 폴더를 지정한다.
```
python3 build.py sm64-hd --rom <게임 데이터 폴더> --zip          # 또는 --deploy <homebrew 폴더>
```
덮어쓸 설정 파일은 `overlay/` 에 있다. 게임 데이터와 NRO 는 저장소에 없다.
