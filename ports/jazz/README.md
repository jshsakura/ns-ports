# 재즈 잭래빗 2 (Jazz² Resurrection)

<!-- quick:begin -->
## 필요한 파일과 명령어

필요한 것: 원작 PC 설치 데이터 (Source/)
NRO: `ports/jazz/in/jazz.nro`

- 스위치 포트 소스: https://github.com/deathkiller/jazz2

```
python3 build.py check jazz    # 빈 칸 확인
python3 build.py jazz --zip
```
<!-- quick:end -->

재즈 잭래빗 2 C++ 오픈소스 네이티브 엔진. 60fps 720p/1080p 지원

- 엔진: Jazz2-Native
- 필요한 것: 원작 PC 설치 데이터 (Source/)
- Required files: jazz.nro, Source/ (retail episodes), Cache/ (compiled assets)
- Features: Native C++ rewrite, 60fps, 720p/1080p widescreen, modern gamepad controls
- Status: Verified & 100% playable on Nintendo Switch!

## 사용
`in/jazz.nro` 에 빌드된 NRO 를 두고, 내 게임 데이터 폴더를 지정한다.
```
python3 build.py jazz --rom <게임 데이터 폴더> --zip          # 또는 --deploy <homebrew 폴더>
```
덮어쓸 설정 파일은 `overlay/` 에 있다. 게임 데이터와 NRO 는 저장소에 없다.
