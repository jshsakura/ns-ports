# 식물 대 좀비 (Plants vs. Zombies Portable)

<!-- quick:begin -->
## 필요한 파일과 명령어

필요한 것: Plants vs. Zombies PC판 main.pak
NRO: `ports/pvz/in/pvz.nro`

- 원 프로젝트: https://github.com/wszqkzqk/PvZ-Portable
- 스위치 포트 소스: https://github.com/HayatoG/PvZ-Portable

```
python3 build.py check pvz    # 빈 칸 확인
python3 build.py pvz --zip
```
<!-- quick:end -->

- **엔진/프로젝트**: PvZ Portable C++ 네이티브
- **업스트림**: https://github.com/HayatoG/PvZ-Portable
- **버전**: 2026-07-02
- **필요 에셋**: Plants vs. Zombies PC판 main.pak

```bash
python3 build.py pvz --rom <게임 데이터 폴더> --deploy <homebrew 배포 폴더>
```
