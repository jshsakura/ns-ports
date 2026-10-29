# 포켓몬 MMO (PokeMMO)

<!-- quick:begin -->
## 필요한 파일과 명령어

필요한 것: GBA/NDS 포켓몬 롬 (FireRed, Emerald, Platinum, Black/White)
NRO: `ports/pokemmo/in/pokemmo.nro`

- 스위치 포트 소스: https://github.com/Petit-Prince-dev/PokeMMO-NX

```
python3 build.py check pokemmo    # 빈 칸 확인
python3 build.py pokemmo --zip
```
<!-- quick:end -->

- **엔진/프로젝트**: PokeMMO-NX C++ 클라이언트
- **업스트림**: https://github.com/Petit-Prince-dev/PokeMMO-NX
- **버전**: v1.1.4
- **필요 에셋**: GBA/NDS 포켓몬 롬 (FireRed, Emerald, Platinum, Black/White)

```bash
python3 build.py pokemmo --rom <게임 데이터 폴더> --deploy <homebrew 배포 폴더>
```
