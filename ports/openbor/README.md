# OpenBOR (Switch)

<!-- quick:begin -->
## 필요한 파일과 명령어

**1. 받아서 둘 것**

| 놓을 위치 | 무엇 | 구하는 곳 |
| :--- | :--- | :--- |
| `ports/openbor/in/OpenBOR.nro` | 스위치용 NRO | https://github.com/SylphiaWindy/openbor 의 릴리스를 받거나 직접 빌드 |
| `ports/openbor/in/data` | OpenBOR .pak 게임 팩 | 내가 가진 정품 데이터 (--rom <폴더> 로 따로 줘도 된다) |
| `ports/openbor/icon.jpg` | 앱 아이콘 (256x256 JPEG) (선택) | 직접 구하거나 만든다. 없으면 NRO 에 든 아이콘을 그대로 쓴다 |

**2. 이미지**: 앱 아이콘(`icon.jpg`, 256x256 JPEG)만 쓰이고 없으면 NRO 의 기본 아이콘을 씁니다. 이미지는 저장소에 없으니 필요하면 직접 구해 위 위치에 두세요. 배너와 스크린샷은 다루지 않습니다.

**3. 확인하고 실행**

```
python3 build.py guide openbor    # 빈 칸과 구하는 곳 확인
python3 build.py openbor --zip
```

- 원 프로젝트: https://github.com/DCurrent/openbor
- 스위치 포트 소스: https://github.com/SylphiaWindy/openbor
<!-- quick:end -->

출처: [SylphiaWindy/openbor](https://github.com/SylphiaWindy/openbor) 릴리스 `switch-v26.0919.1` (2026-09-18).
2026-10-20 에 받아 `SHA256SUMS` 대조를 마쳤습니다(4개 모두 OK). 원문 안내는 `release/switch-v26.0919.1/RELEASE-NOTES.md` 에 있습니다.

RetroArch 코어가 아니라 각자 독립 NRO 로 도는 엔진입니다. 엔진마다 쓰는 팩이 다르고, 자기 NRO 옆의 `Paks/` 와 `Saves/` 를 씁니다. 설정 파일은 엔진끼리 호환되지 않습니다.

| NRO | 버전 | 용도 | SD 위치 | 팩 위치 |
|---|---|---|---|---|
| `OpenBOR.nro` | 3.0.7550 | 일반 OpenBOR 팩 (3.0 final) | `switch/openbor/` | `switch/openbor/Paks/` |
| `SoRX.nro` | 4.0.7785 | Streets of Rage X beta 35 | `switch/sorx/` | `switch/sorx/Paks/SORX.pak` |
| `FFLNS.nro` | 3.0.7184 | Final Fight LNS 전용 (일반 팩은 못 읽습니다) | `switch/fflns/` | `switch/fflns/Paks/` |
| `OpenBOR2018.nro` | 3.0.6432 | 2018 엔진(6428)용 모드 | `switch/openbor2018/` | `switch/openbor2018/Paks/` |

## 현재 상태

- 팩(게임 데이터)은 따로 준비해야 합니다.
- 이 릴리스 뒤에 나온 것: `sorx-switch-v7787`(SoRX beta 36, 2026-09-27), `fightforever-v6453`(2026-10-13, Latest).

## Build / 입수
Not built from source; the upstream release NROs are used as they are.
```
gh release download switch-v26.0919.1 -R SylphiaWindy/openbor -D in
cd in && sha256sum -c SHA256SUMS
python3 build.py openbor --rom <folder with your .pak files> --deploy <homebrew folder>
```
