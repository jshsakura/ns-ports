# 소닉 더 헤지혹 2006 (Sonic 06 / MarathonRecomp)

<!-- quick:begin -->
## 필요한 파일과 명령어

필요한 것: Xbox 360판 소닉 06 디스크 데이터
NRO: `ports/marathon-recomp/in/MarathonRecomp.nro`

- 원 프로젝트: https://github.com/sonicnext-dev/MarathonRecomp
- 스위치 포트 소스: https://github.com/ChanseyIsTheBest/MarathonRecomp-NX

```
python3 build.py check marathon-recomp    # 빈 칸 확인
python3 build.py marathon-recomp --zip
```
<!-- quick:end -->

- **엔진/프로젝트**: MarathonRecomp (Xbox 360 정적 리컴파일)
- **업스트림**: https://github.com/ChanseyIsTheBest/MarathonRecomp-NX
- **버전**: v1.0.3
- **필요 에셋**: Xbox 360판 소닉 06 디스크 데이터

```bash
python3 build.py marathon-recomp --rom <게임 데이터 폴더> --deploy <homebrew 배포 폴더>
```
