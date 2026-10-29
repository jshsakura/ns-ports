# 소닉 더 파이터즈 (Sonic the Fighters)

<!-- quick:begin -->
## 필요한 파일과 명령어

필요한 것: MAME Model 2 sfight.zip 롬
NRO: `ports/sonic-fighters/in/sonic_the_fighters.nro`

- 스위치 포트 소스: https://github.com/boraeskicioglu/sonic_the_fighters_nx

```
python3 build.py check sonic-fighters    # 빈 칸 확인
python3 build.py sonic-fighters --zip
```
<!-- quick:end -->

- **엔진/프로젝트**: Sega Model 2 네이티브
- **업스트림**: https://github.com/boraeskicioglu/sonic_the_fighters_nx
- **버전**: v0.8.3
- **필요 에셋**: MAME Model 2 sfight.zip 롬

```bash
python3 build.py sonic-fighters --rom <게임 데이터 폴더> --deploy <homebrew 배포 폴더>
```
