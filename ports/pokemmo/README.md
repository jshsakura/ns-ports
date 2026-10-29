# 포켓몬 MMO (PokeMMO)

<!-- quick:begin -->
## 필요한 파일과 명령어

**1. 받아서 둘 것**

| 놓을 위치 | 무엇 | 구하는 곳 |
| :--- | :--- | :--- |
| `ports/pokemmo/in/pokemmo.nro` | 스위치용 NRO | https://github.com/Petit-Prince-dev/PokeMMO-NX 의 릴리스를 받거나 직접 빌드 |
| `ports/pokemmo/in/data` | GBA/NDS 포켓몬 롬 (FireRed, Emerald, Platinum, Black/White) | 내가 가진 정품 데이터 (--rom <폴더> 로 따로 줘도 된다) |
| `ports/pokemmo/icon.jpg` | 앱 아이콘 (256x256 JPEG) (선택) | 직접 구하거나 만든다. 없으면 NRO 에 든 아이콘을 그대로 쓴다 |

**2. 이미지**: 앱 아이콘(`icon.jpg`, 256x256 JPEG)만 쓰이고 없으면 NRO 의 기본 아이콘을 씁니다. 이미지는 저장소에 없으니 필요하면 직접 구해 위 위치에 두세요. 배너와 스크린샷은 다루지 않습니다.

**3. 확인하고 실행**

```
python3 build.py guide pokemmo    # 빈 칸과 구하는 곳 확인
python3 build.py pokemmo --zip
```

- 스위치 포트 소스: https://github.com/Petit-Prince-dev/PokeMMO-NX
<!-- quick:end -->

- **엔진/프로젝트**: PokeMMO-NX C++ 클라이언트
- **업스트림**: https://github.com/Petit-Prince-dev/PokeMMO-NX
- **버전**: v1.1.4
- **필요 에셋**: GBA/NDS 포켓몬 롬 (FireRed, Emerald, Platinum, Black/White)

```bash
python3 build.py pokemmo --rom <게임 데이터 폴더> --deploy <homebrew 배포 폴더>
```
