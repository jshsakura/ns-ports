# 아웃런 (OutRun / Cannonball)

<!-- quick:begin -->
## 필요한 파일과 명령어

필요한 것: OutRun 아케이드 ROM 세트
NRO: `ports/cannonball/in/cannonball.nro`

- 스위치 포트 소스: https://github.com/Thorhax/Cannonball-NX-Modern

```
python3 build.py check cannonball    # 빈 칸 확인
python3 build.py cannonball --zip
```
<!-- quick:end -->

아웃런 아케이드 C++ 재구현 엔진 포트. 60fps & 와이드스크린 지원

- 엔진: Cannonball
- 필요한 것: OutRun 아케이드 ROM 세트
- Required files: cannonball.nro, config.xml, roms/, res/
- Features: 60fps smooth scrolling, widescreen display, custom soundtrack support
- Status: Verified & 100% playable on Nintendo Switch!

## 사용
`in/cannonball.nro` 에 빌드된 NRO 를 두고, 내 게임 데이터 폴더를 지정한다.
```
python3 build.py cannonball --rom <게임 데이터 폴더> --zip          # 또는 --deploy <homebrew 폴더>
```
덮어쓸 설정 파일은 `overlay/` 에 있다. 게임 데이터와 NRO 는 저장소에 없다.
