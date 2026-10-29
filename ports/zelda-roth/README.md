# 젤다의 전설: 하일리아인의 귀환 (Zelda: ROTH)

<!-- quick:begin -->
## 필요한 파일과 명령어

**1. 받아서 둘 것**

| 놓을 위치 | 무엇 | 구하는 곳 |
| :--- | :--- | :--- |
| `ports/zelda-roth/in/ZeldaROTH.nro` | ZeldaROTH NRO (게임 데이터는 자체 무료 데이터가 NRO 에 포함) | https://github.com/worthis/ZeldaROTH-new-engine 의 Switch 빌드 |
| `ports/zelda-roth/icon.jpg` | 앱 아이콘 (256x256 JPEG) (선택) | 직접 구하거나 만든다. 없으면 NRO 에 든 아이콘을 그대로 쓴다 |

**2. 이미지**: 앱 아이콘(`icon.jpg`, 256x256 JPEG)만 쓰이고 없으면 NRO 의 기본 아이콘을 씁니다. 이미지는 저장소에 없으니 필요하면 직접 구해 위 위치에 두세요. 배너와 스크린샷은 다루지 않습니다.

**3. 확인하고 실행**

```
python3 build.py guide zelda-roth    # 빈 칸과 구하는 곳 확인
python3 build.py zelda-roth --rom <내 게임 데이터 폴더> --zip
```

NRO 는 구하지 않아도 됩니다. `in/` 에 없으면 worthis/ZeldaROTH-new-engine 릴리스 1.1.4 에서 받아 sha256 을 확인하고 씁니다.

- 스위치 포트 소스: https://github.com/worthis/ZeldaROTH-new-engine
<!-- quick:end -->

ZeldaROTH 엔진(v1.1.4) 네이티브 포트. 게임 데이터는 자체 무료 데이터라 따로 구할 게임 파일이 없다.

## 어떤 파일을 어디서 구해 어디에 두나

| # | 파일 | 어디서 | 어디에 |
| :-: | :--- | :--- | :--- |
| 1 | `ZeldaROTH.nro` | [worthis/ZeldaROTH-new-engine](https://github.com/worthis/ZeldaROTH-new-engine) 의 Switch 빌드 | `ports/zelda-roth/in/ZeldaROTH.nro` |

## 조립

```
python3 build.py zelda-roth --zip
```

결과는 `ports/zelda-roth/dist/switch/` 와 zip 이고 `sd:/switch/` 로 복사해 실행한다.
