# 젤다의 전설: 시간의 오카리나 HD (Ocarina of Time)

<!-- quick:begin -->
## 필요한 파일과 명령어

**1. 받아서 둘 것**

| 놓을 위치 | 무엇 | 구하는 곳 |
| :--- | :--- | :--- |
| `ports/zelda-oot-hd/in/zelda-oot-hd.nro` | Ship of Harkinian 9.3.0 Switch 빌드 NRO | https://github.com/HarbourMasters/Shipwright 의 Switch 빌드 |
| `ports/zelda-oot-hd/in/data/oot.o2r` | 내 롬으로 SoH 가 만든 oot.o2r | 내 정품 롬을 SoH 에 넣어 생성 |
| `ports/zelda-oot-hd/in/data/soh.o2r` | SoH 릴리스에 든 soh.o2r | https://github.com/HarbourMasters/Shipwright/releases |
| `ports/zelda-oot-hd/in/data/mods/OoT_Reloaded_Korean_Pretendard_HD.o2r` | 한글 Pretendard HD 모드 (3.89GB) (한글 판만) | OoT Reloaded 한글 모드 배포처 (직접 확인) |
| `ports/zelda-oot-hd/icon.jpg` | 앱 아이콘 (256x256 JPEG) (선택) | 직접 구하거나 만든다. 없으면 NRO 에 든 아이콘을 그대로 쓴다 |

**2. 이미지**: 앱 아이콘(`icon.jpg`, 256x256 JPEG)만 쓰이고 없으면 NRO 의 기본 아이콘을 씁니다. 이미지는 저장소에 없으니 필요하면 직접 구해 위 위치에 두세요. 배너와 스크린샷은 다루지 않습니다.

**3. 확인하고 실행**

```
python3 build.py guide zelda-oot-hd    # 빈 칸과 구하는 곳 확인
python3 build.py zelda-oot-hd --rom <내 게임 데이터 폴더> --zip
```

- 스위치 포트 소스: https://github.com/HarbourMasters/Shipwright
<!-- quick:end -->

Ship of Harkinian v9.3.0 네이티브 포트에 60FPS 와이드스크린과 한글 Pretendard HD 모드(3.89GB)를 얹은 구성의 방법 가이드. 실기 검수 완료.

이 저장소는 NRO, o2r, 모드, 게임 데이터를 담지 않는다(클린룸). 아래 파일은 전부 사용자가 구해서 둔다.

## 파일 배치 (이름까지 정확히)

| 구할 것 | 넣을 위치 |
| :--- | :--- |
| Ship of Harkinian 9.3.0 Switch 빌드 NRO | `ports/zelda-oot-hd/in/zelda-oot-hd.nro` |
| `oot.o2r` (내 정품 롬으로 SoH 가 만든 것) | `ports/zelda-oot-hd/in/data/oot.o2r` |
| `soh.o2r` ([Ship of Harkinian 릴리스](https://github.com/HarbourMasters/Shipwright/releases)에 들어 있는 것) | `ports/zelda-oot-hd/in/data/soh.o2r` |
| OoT Reloaded 한글 Pretendard HD 모드 | `ports/zelda-oot-hd/in/data/mods/OoT_Reloaded_Korean_Pretendard_HD.o2r` |

모드가 3.89GB 라 복사하지 말고 심볼릭 링크나 하드링크로 둬도 된다. 비어 있는 칸은 `python3 build.py guide zelda-oot-hd` 로 확인한다.

## 조립

```
python3 build.py zelda-oot-hd --zip                      # 한글 판 (in/data 를 게임 데이터로 사용)
python3 build.py zelda-oot-hd --variant original --zip   # 모드와 한글 설정 없이 순정 SoH
python3 build.py zelda-oot-hd --rom <데이터 폴더>         # in/data 대신 다른 폴더를 쓸 때
```

결과는 `ports/zelda-oot-hd/dist/switch/zelda-oot-hd/` 이고 `sd:/switch/zelda-oot-hd/` 로 복사해 실행한다.
original 판은 `in/data/mods/` 를 비워 두면 모드 없이 조립된다.

## 한글판이 켜지는 원리

한글 판에는 `overlay-ko/shipofharkinian.json` 이 `shipofharkinian.json` 으로 들어간다.

| 설정 | 값 | 뜻 |
| :--- | :--- | :--- |
| `gSettings.Languages` | `3` | 일본어 슬롯(한글 모드가 이 슬롯을 한글로 대체) |
| `gSettings.TitleScreenTranslation` | `1` | 타이틀 화면 번역 |
| `gSettings.AltAssets` | `1` | 대체 에셋(HD 모드) 사용 |
| `gSettings.EnabledMods` | `OoT_Reloaded_Korean_Pretendard_HD` | `mods/` 의 이 파일을 활성화 |

자이로와 60FPS 는 SoH 빌드 자체 기능이다.
