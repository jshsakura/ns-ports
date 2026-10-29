# 디아블로 1 (Diablo 1 + Hellfire)

<!-- quick:begin -->
## 필요한 파일과 명령어

필요한 것: DIABDAT.MPQ (원작 PC CD 데이터)
NRO: `ports/devilutionx/in/devilutionx.nro`

- 스위치 포트 소스: https://github.com/diasurgical/DevilutionX

```
python3 build.py check devilutionx    # 빈 칸 확인
python3 build.py devilutionx --zip
```
<!-- quick:end -->

디아블로 1 오픈소스 리버스 엔지니어링 포트. 한글 폰트 및 패드 조작 최적화

- 엔진: DevilutionX
- 필요한 것: DIABDAT.MPQ (원작 PC CD 데이터)
- Required files: diabdat.mpq, devilutionx.mpq, fonts.mpq (Korean), diablo.ini
- Status: Ready to play!

## 사용
`in/devilutionx.nro` 에 빌드된 NRO 를 두고, 내 게임 데이터 폴더를 지정한다.
```
python3 build.py devilutionx --rom <게임 데이터 폴더> --zip          # 또는 --deploy <homebrew 폴더>
```
덮어쓸 설정 파일은 `overlay/` 에 있다. 게임 데이터와 NRO 는 저장소에 없다.
