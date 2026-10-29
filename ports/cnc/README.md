# 커맨드 앤 컨커: 타이베리안 던 (C&C 1)

<!-- quick:begin -->
## 필요한 파일과 명령어

필요한 것: C&C Gold .MIX 파일 및 영상 에셋
NRO: `ports/cnc/in/vanillatd.nro`

- 스위치 포트 소스: https://github.com/TheAssemblyArmada/Vanilla-Conquer

```
python3 build.py check cnc    # 빈 칸 확인
python3 build.py cnc --zip
```
<!-- quick:end -->

C&C 원작 엔진 복각 포트. GDI/NOD 캠페인 및 컷신 영상 지원

- 엔진: Vanilla-Conquer (TD)
- 필요한 것: C&C Gold .MIX 파일 및 영상 에셋
- Required files: vanillatd.nro, CONQUER.INI, keymap.keys, .MIX archive assets
- Campaign support: Full GDI and NOD campaigns with high quality FMV movies
- Status: Verified & 100% playable on Nintendo Switch!

## 사용
`in/vanillatd.nro` 에 빌드된 NRO 를 두고, 내 게임 데이터 폴더를 지정한다.
```
python3 build.py cnc --rom <게임 데이터 폴더> --zip          # 또는 --deploy <homebrew 폴더>
```
덮어쓸 설정 파일은 `overlay/` 에 있다. 게임 데이터와 NRO 는 저장소에 없다.
