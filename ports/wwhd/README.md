# 바람의 지휘봉 HD (Wind Waker HD Decomp/Port)

바람의 지휘봉 네이티브 홈브루 구동 환경

- 엔진: Custom Port
- 필요한 것: 게임 데이터
- Required files: wwhd.nro, game/ (code/, content/, meta/)
- Features: 720p/1080p widescreen, Korean font & text
- Status: Verified & 100% playable on Nintendo Switch!

## 사용
`in/wwhd.nro` 에 빌드된 NRO 를 두고, 내 게임 데이터 폴더를 지정한다.
```
python3 build.py wwhd --rom <게임 데이터 폴더> --zip          # 또는 --deploy <homebrew 폴더>
```
덮어쓸 설정 파일은 `overlay/` 에 있다. 게임 데이터와 NRO 는 저장소에 없다.
