# 젤다의 전설: 무쥬라의 가면 HD (Majora's Mask)

<!-- quick:begin -->
## 필요한 파일과 명령어

**1. 받아서 둘 것**

| 놓을 위치 | 무엇 | 구하는 곳 |
| :--- | :--- | :--- |
| `ports/zelda-mm-hd/in/zelda-mm-hd.nro` | 2 Ship 2 Harkinian 5.0.1 Switch 빌드 NRO | https://github.com/2ship2harkinian/2ship2harkinian 의 Switch 빌드 |
| `ports/zelda-mm-hd/in/data/mm.o2r` | 내 정품 롬으로 2Ship 이 만든 mm.o2r | 내 롬을 2Ship2Harkinian(PC 판)에 넣어 생성 |
| `ports/zelda-mm-hd/in/data/2ship.o2r` | 2Ship 릴리스에 든 2ship.o2r | https://github.com/2ship2harkinian/2ship2harkinian/releases 의 압축 안 |
| `ports/zelda-mm-hd/in/data/mods/MM_Reloaded_v11.0.3_HD.o2r` | MM Reloaded v11.0.3 HD 텍스처 모드 (2.95GB) (선택) | MM Reloaded 배포처에서 직접 받는다. 없으면 HD 텍스처 없이 조립된다 |
| `ports/zelda-mm-hd/icon.jpg` | 앱 아이콘 (256x256 JPEG) (선택) | 직접 구하거나 만든다. 없으면 NRO 에 든 아이콘을 그대로 쓴다 |

**2. 이미지**: 앱 아이콘(`icon.jpg`, 256x256 JPEG)만 쓰이고 없으면 NRO 의 기본 아이콘을 씁니다. 이미지는 저장소에 없으니 필요하면 직접 구해 위 위치에 두세요. 배너와 스크린샷은 다루지 않습니다.

**3. 확인하고 실행**

```
python3 build.py guide zelda-mm-hd    # 빈 칸과 구하는 곳 확인
python3 build.py zelda-mm-hd --zip
```

- 스위치 포트 소스: https://github.com/2ship2harkinian/2ship2harkinian
<!-- quick:end -->

2 Ship 2 Harkinian v5.0.1 네이티브 포트에 60FPS 와이드스크린과 MM-Reloaded v11.0.3 HD 텍스처(2.95GB)를 얹은 구성. 실기에 올려 플레이한 기록이 있다.
NRO, o2r, 모드, 게임 데이터는 저장소에 없다. 아래 파일을 각자 구해서 둔다.

## 어떤 파일을 어디서 구해 어디에 두나

| # | 파일 | 어디서 | 어디에 |
| :-: | :--- | :--- | :--- |
| 1 | `zelda-mm-hd.nro` | [2Ship2Harkinian](https://github.com/2ship2harkinian/2ship2harkinian) 의 Switch 빌드 | `ports/zelda-mm-hd/in/zelda-mm-hd.nro` |
| 2 | `mm.o2r` | 내 정품 롬을 PC 판 2Ship2Harkinian 에 넣으면 만들어진다 | `ports/zelda-mm-hd/in/data/mm.o2r` |
| 3 | `2ship.o2r` | 2Ship2Harkinian 릴리스 압축 안 | `ports/zelda-mm-hd/in/data/2ship.o2r` |
| 4 | `MM_Reloaded_v11.0.3_HD.o2r` (선택) | MM Reloaded 배포처 | `ports/zelda-mm-hd/in/data/mods/MM_Reloaded_v11.0.3_HD.o2r` |

4번은 3GB 가까워서 복사하지 말고 심볼릭 링크로 둬도 된다. 없으면 HD 텍스처 없이 조립된다.
`overlay/2ship2harkinian.json` 은 이 저장소가 넣어 주며 대체 에셋(`AltAssets`)을 켠다.

## 조립

```
python3 build.py guide zelda-mm-hd      # 빈 칸 확인
python3 build.py zelda-mm-hd --zip      # in/data 를 게임 데이터로 사용
python3 build.py zelda-mm-hd --rom <데이터 폴더> --zip      # 다른 폴더를 쓸 때
```

결과는 `ports/zelda-mm-hd/dist/switch/zelda-mm-hd/` 와 zip 이고 `sd:/switch/zelda-mm-hd/` 로 복사해 실행한다.
