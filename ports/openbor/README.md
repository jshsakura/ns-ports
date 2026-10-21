# OpenBOR (Switch)

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
