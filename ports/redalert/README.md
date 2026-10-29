# 커맨드 앤 컨커: 레드 얼럿 (C&C Red Alert)

<!-- quick:begin -->
## 필요한 파일과 명령어

필요한 것: Red Alert CD1/CD2 .MIX 파일
NRO: `ports/redalert/in/vanillara.nro`

- 스위치 포트 소스: https://github.com/TheAssemblyArmada/Vanilla-Conquer

```
python3 build.py check redalert    # 빈 칸 확인
python3 build.py redalert --zip
```
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
