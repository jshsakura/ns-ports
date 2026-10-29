# 커맨드 앤 컨커: 레드 얼럿 (C&C Red Alert)

<!-- quick:begin -->
## 필요한 파일과 명령어

**1. 받아서 둘 것**

| 놓을 위치 | 무엇 | 구하는 곳 |
| :--- | :--- | :--- |
| `ports/redalert/in/vanillara.nro` | 스위치용 NRO | https://github.com/TheAssemblyArmada/Vanilla-Conquer 의 릴리스를 받거나 직접 빌드 |
| `ports/redalert/in/data` | Red Alert CD1/CD2 .MIX 파일 | 내가 가진 정품 데이터 (--rom <폴더> 로 따로 줘도 된다) |
| `ports/redalert/icon.jpg` | 앱 아이콘 (256x256 JPEG) (선택) | 직접 구하거나 만든다. 없으면 NRO 에 든 아이콘을 그대로 쓴다 |

**2. 이미지**: 앱 아이콘(`icon.jpg`, 256x256 JPEG)만 쓰이고 없으면 NRO 의 기본 아이콘을 씁니다. 이미지는 저장소에 없으니 필요하면 직접 구해 위 위치에 두세요. 배너와 스크린샷은 다루지 않습니다.

**3. 확인하고 실행**

```
python3 build.py guide redalert    # 빈 칸과 구하는 곳 확인
python3 build.py redalert --zip
```

- 스위치 포트 소스: https://github.com/TheAssemblyArmada/Vanilla-Conquer
<!-- quick:end -->

레드얼럿 연합군(CD1)/소련군(CD2) 풀 리테일 데이터 연동 포트

- 엔진: Vanilla-Conquer (RA)
- 필요한 것: Red Alert CD1/CD2 .MIX 파일
- Required files: vanillara.nro, REDALERT.INI, REDALERT.MIX, CD1, CD2, keymap.keys
- Campaign support: Allied (CD1) and Soviet (CD2) dual campaign
- Status: Verified & 100% playable on Nintendo Switch!

## 사용
`in/vanillara.nro` 에 빌드된 NRO 를 두고, 내 게임 데이터 폴더를 지정한다.
```
python3 build.py redalert --rom <게임 데이터 폴더> --zip          # 또는 --deploy <homebrew 폴더>
```
덮어쓸 설정 파일은 `overlay/` 에 있다. 게임 데이터와 NRO 는 저장소에 없다.
