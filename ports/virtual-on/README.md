# 전뇌전기 버추얼 온 (Cyber Troopers Virtual-On)

<!-- quick:begin -->
## 필요한 파일과 명령어

필요한 것: MAME Model 2 von.zip 롬
NRO: `ports/virtual-on/in/Virtual-On.nro`

- 스위치 포트 소스: https://github.com/Thorhax/Virtual-On-NX

```
python3 build.py check virtual-on    # 빈 칸 확인
python3 build.py virtual-on --zip
```
<!-- quick:end -->

- **엔진/프로젝트**: Sega Model 2 정적 리컴파일 + 소프트웨어 래스터라이저
- **업스트림**: https://github.com/Thorhax/Virtual-On-NX
- **버전**: v1.2.0
- **필요 에셋**: MAME Model 2 von.zip 롬

```bash
python3 build.py virtual-on --rom <게임 데이터 폴더> --deploy <homebrew 배포 폴더>
```
