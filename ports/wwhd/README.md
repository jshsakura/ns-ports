# 바람의 지휘봉 HD (Wind Waker HD, SwitchWakerHD)

<!-- quick:begin -->
## 하는 법

1. 한글 패치(Ver 1.02) 압축을 풀고 `windwakerHD/Layout/Title_00.szs` 를 `ports/wwhd/in/Title_00.szs` 로 복사한다. (원본 그대로 만들 거면 생략)
2. 실행한다.

```
python3 build.py wwhd --rom <Wii U 덤프 폴더> --zip
```

`<Wii U 덤프 폴더>` 는 `code/` `content/` `meta/` 가 바로 보이는 폴더다(USA, 버전 0). 옮기지 않고 경로만 주면 된다.

이 한 줄이 알아서 하는 일: `xdelta3` 로 한글 pack 만들기, `wwhd.nro` 가 없으면 SwitchWakerHD 를 받아 도커로 빌드하기(몇 시간, git 과 docker 필요), 게임 데이터 연결, zip 만들기.
결과는 `ports/wwhd/dist/switch/wwhd/` 이고 SD 카드의 `switch/` 에 복사해 홈브루 메뉴에서 실행한다.

이미 빌드한 NRO 가 있으면 `ports/wwhd/in/wwhd.nro` 로 두면 빌드를 건너뛴다. 원본 그대로: `--variant original`. 앱 아이콘을 바꾸려면 256x256 JPEG 를 `ports/wwhd/icon.jpg` 로 둔다(선택).
<!-- quick:end -->

WiiU 바람의 지휘봉 HD 를 스위치에서 네이티브로 구동하는 [centollOS/SwitchWakerHD](https://github.com/centollOS/SwitchWakerHD) 포트에, 한국어 패치 파일을 얹는 방법 가이드.

이 저장소는 방법을 안내할 뿐, NRO 나 한글 패치 산출물, 게임 데이터를 담지 않는다(클린룸). 아래 파일은 전부 사용자 소유분을 쓴다.

## 한글 패치 크레딧과 조건

한글 패치 `Ver 1.02` 는 게임큐브판 한글패치를 만든 Cocory 님의 도움으로, 샤이닝구포스, 닥스, 송키, nAtAs, 이로치레시람 님이 제작했다. 패치 안내문에 따르면 **상업적 사용은 금지**이고, 번역 오류 제보는 패치 제작진이 연 [번역 수정 시트](https://docs.google.com/spreadsheets/d/1lIJIghvEBiemGmxu5oDbOIM_3CeRSt0W0jgtOOYTDTw/edit#gid=0)로 받는다. 북미판(영문)과 일판 대응이다.

이 저장소의 `patches/permanent_2d_UsEnglish.xdelta` 는 이 패치의 한글 텍스트 작업물을 담고 있으므로, 위 조건(비상업)을 따르는 개인 사용만 전제로 한다. 제작진이 배포 방식에 이의가 있으면 이 파일을 내린다.
