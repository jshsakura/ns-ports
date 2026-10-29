## 하는 법 (파일 두고 한 번에)

**내가 두는 것은 두 가지뿐입니다.**

| 내가 둘 곳 | 무엇을 | 어디서 구하나 |
| :--- | :--- | :--- |
| `ports/wwhd/in/data` | 내 Wii U 바람의 지휘봉 HD 덤프 폴더. 그 안에 `code` `content` `meta` 가 바로 보여야 함 (USA, 버전 0) | 내 Wii U 에서 추출. 큰 폴더라 `ln -s /내/덤프/경로 ports/wwhd/in/data` 로 링크해도 됨 |
| `ports/wwhd/in/patch` | 한글 패치 Ver 1.02 를 **압축 푼 폴더** 통째로 (안에 `windwakerHD` 폴더가 있음) | 패치 제작진 배포본 (아래 크레딧 참고). 원본 그대로 만들 거면 생략 |

```
python3 build.py wwhd --zip
```

**나머지는 프로그램이 알아서 만듭니다. 아래는 각각 어디서 나오는지입니다.**

| 필요한 것 | 어디서 나오나 |
| :--- | :--- |
| 한글 텍스트 pack (`permanent_2d_UsEnglish.pack`) | 한글 패치에서 꺼내지 않습니다. 이 저장소의 차이 패치(`patches/permanent_2d_UsEnglish.xdelta`)를 내 덤프의 원본 pack(`content/Common/Pack/permanent_2d_UsFrench.pack`)에 적용해 만듭니다 (`xdelta3` 필요) |
| `Title_00.szs` (타이틀 화면) | `in/patch` 폴더 안의 `windwakerHD/Layout/Title_00.szs` 를 찾아 씁니다. 이것만 한글 패치에서 꺼내옵니다 |
| `wwhd.nro` | `in/wwhd.nro` 가 없으면 GitHub 의 SwitchWakerHD 를 받아 내 덤프로 도커 빌드합니다 (몇 시간, git 과 docker 필요) |
| 게임 데이터 | 내 덤프(`in/data`)를 링크로 연결합니다. 복사하지 않습니다 |

빠진 게 있으면 어디에 뭘 두라고 말하고 멈춥니다. 끝나면 `ports/wwhd/dist/switch/wwhd/` 폴더를 SD 카드의 `switch/` 에 복사해 홈브루 메뉴에서 실행합니다.

이미 빌드한 NRO 가 있으면 `ports/wwhd/in/wwhd.nro` 로 두면 빌드를 건너뜁니다. 원본 그대로: `python3 build.py wwhd --variant original --zip`. 경로를 직접 주려면 `--rom <덤프 폴더>` 도 됩니다.
