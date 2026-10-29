# 라그나로크 온라인 (RO Switch)

<!-- quick:begin -->
## 필요한 파일과 명령어

**1. 받아서 둘 것**

| 놓을 위치 | 무엇 | 구하는 곳 |
| :--- | :--- | :--- |
| `ports/ro/in/ragnarok.nro` | 스위치용 NRO | 직접 빌드한 NRO |
| `ports/ro/in/data` | 라그나로크 클라이언트 데이터(data.grf, rdata.grf)와 접속 설정(login.ini) | 내가 가진 정품 데이터 (--rom <폴더> 로 따로 줘도 된다) |
| `ports/ro/icon.jpg` | 앱 아이콘 (256x256 JPEG) (선택) | 직접 구하거나 만든다. 없으면 NRO 에 든 아이콘을 그대로 쓴다 |

**2. 이미지**: 앱 아이콘(`icon.jpg`, 256x256 JPEG)만 쓰이고 없으면 NRO 의 기본 아이콘을 씁니다. 이미지는 저장소에 없으니 필요하면 직접 구해 위 위치에 두세요. 배너와 스크린샷은 다루지 않습니다.

**3. 확인하고 실행**

```
python3 build.py guide ro    # 빈 칸과 구하는 곳 확인
python3 build.py ro --rom <내 게임 데이터 폴더> --zip
```
<!-- quick:end -->

스위치용 라그나로크 클라이언트(`ragnarok.nro`). 실기 폴더에 풀 배포되어 돌아가는 구성을 레시피로 옮겼다.
NRO 와 게임 데이터는 저장소에 없다. 업스트림 주소는 아직 확인하지 못했다.

- 필요한 것: 클라이언트 데이터 `data.grf`, `rdata.grf` (자기 것), 접속 설정 `login.ini`
- 상태: `boot-ok` (실기에서 기동 확인)

## 폴더 구성
```
<homebrew>/ro/
  ragnarok.nro
  DATA.INI          [Data] 1=rdata.grf 2=data.grf  (overlay/ 가 만든다)
  data.grf, rdata.grf, BGM/, login.ini   내 게임 데이터 (--rom 으로 지정)
```
`login.ini` 는 접속할 서버 정보라서 저장소에 두지 않는다. 내 데이터 폴더에 넣어 둔다.

## 사용
`in/ragnarok.nro` 가 없으면 이미 배포된 `<homebrew>/ro/ragnarok.nro` 를 그대로 쓴다.
```
python3 build.py ro --rom <내 데이터 폴더> --deploy <homebrew 폴더>
```
