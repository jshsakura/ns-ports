# 버추어 파이터 2 (Virtua Fighter 2)

<!-- quick:begin -->
## 필요한 파일과 명령어

필요한 것: MAME Model 2 vf2.zip 롬
NRO: `ports/vf2/in/VF2.nro`

- 스위치 포트 소스: https://github.com/Thorhax/VF2-NX-Modern

```
python3 build.py check vf2    # 빈 칸 확인
python3 build.py vf2 --zip
```
<!-- quick:end -->

- **엔진/프로젝트**: Sega Model 2 정적 리컴파일
- **업스트림**: https://github.com/Thorhax/VF2-NX-Modern
- **버전**: v1.1.0
- **필요 에셋**: MAME Model 2 vf2.zip 롬

```bash
python3 build.py vf2 --rom <게임 데이터 폴더> --deploy <homebrew 배포 폴더>
```
