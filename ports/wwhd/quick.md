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
