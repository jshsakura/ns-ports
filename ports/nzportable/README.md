# 나치 좀비: 포터블 (Nazi Zombies: Portable)

<!-- quick:begin -->
## 필요한 파일과 명령어

필요한 것: 자체 무료 데이터 포함 (독립 실행형)
NRO: `ports/nzportable/in/nzportable.nro`

- 스위치 포트 소스: https://github.com/nzp-team/nzportable

```
python3 build.py check nzportable    # 빈 칸 확인
python3 build.py nzportable --zip
```
<!-- quick:end -->

- **엔진/프로젝트**: Quake 기반 C++ 네이티브
- **업스트림**: https://github.com/nzp-team/nzportable
- **버전**: v2.0.0
- **필요 에셋**: 자체 무료 데이터 포함 (독립 실행형)

```bash
python3 build.py nzportable --rom <게임 데이터 폴더> --deploy <homebrew 배포 폴더>
```
