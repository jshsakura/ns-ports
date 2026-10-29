# 하프라이프 1 (Half-Life)

<!-- quick:begin -->
## 필요한 파일과 명령어

**1. 받아서 둘 것**

| 놓을 위치 | 무엇 | 구하는 곳 |
| :--- | :--- | :--- |
| `ports/half-life/in/half-life.nro` | 스위치용 NRO | https://github.com/FWGS/xash3d-fwgs 의 릴리스를 받거나 직접 빌드 |
| `ports/half-life/in/data` | valve/ 폴더 (원작 PC 게임 데이터) | 내가 가진 정품 데이터 (--rom <폴더> 로 따로 줘도 된다) |
| `ports/half-life/icon.jpg` | 앱 아이콘 (256x256 JPEG) (선택) | 직접 구하거나 만든다. 없으면 NRO 에 든 아이콘을 그대로 쓴다 |

**2. 이미지**: 앱 아이콘(`icon.jpg`, 256x256 JPEG)만 쓰이고 없으면 NRO 의 기본 아이콘을 씁니다. 이미지는 저장소에 없으니 필요하면 직접 구해 위 위치에 두세요. 배너와 스크린샷은 다루지 않습니다.

**3. 확인하고 실행**

```
python3 build.py guide half-life    # 빈 칸과 구하는 곳 확인
python3 build.py half-life --rom <내 게임 데이터 폴더> --zip
```

- 스위치 포트 소스: https://github.com/FWGS/xash3d-fwgs
<!-- quick:end -->

Xash3D 엔진 기반 하프라이프 1 네이티브 포트. 공식 한국어 풀더빙 음성 연동

- 엔진: Xash3D-FWGS
- 필요한 것: valve/ 폴더 (원작 PC 게임 데이터)
- Required files: half-life.nro, filesystem_stdio.so, libmenu.so, libref_gl.so
- Game data: valve/ (Half-Life), bshift/ (Blue Shift), gearbox/ (Opposing Force)
- Korean assets: Official Korean voice dubbing in valve/sound/ (sentences.txt, fvox, scientist)
- Features: Motion controls (gyro aim), 60fps, widescreen
- Status: Verified & 100% playable in Korean!

## 사용
`in/half-life.nro` 에 빌드된 NRO 를 두고, 내 게임 데이터 폴더를 지정한다.
```
python3 build.py half-life --rom <게임 데이터 폴더> --zip          # 또는 --deploy <homebrew 폴더>
```
덮어쓸 설정 파일은 `overlay/` 에 있다. 게임 데이터와 NRO 는 저장소에 없다.
