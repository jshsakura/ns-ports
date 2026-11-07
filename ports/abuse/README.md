# 어뷰즈 (Abuse)

<!-- quick:begin -->
## 필요한 파일과 명령어

**1. 받아서 둘 것**

| 놓을 위치 | 무엇 | 구하는 곳 |
| :--- | :--- | :--- |
| `ports/abuse/in/abuse.nro` | 스위치용 NRO (선택) | 안 둬도 된다. 없으면 capsterx-switch/abuse 릴리스 v0.8r3 에서 자동으로 받는다 |
| `ports/abuse/in/data` | 자체 무료 풀버전 데이터 포함 (선택) | 필요 없다. 게임 데이터가 NRO 안에 들어 있다 |
| `ports/abuse/icon.jpg` | 앱 아이콘 (256x256 JPEG) (선택) | 직접 구하거나 만든다. 없으면 NRO 에 든 아이콘을 그대로 쓴다 |

**2. 이미지**: 앱 아이콘(`icon.jpg`, 256x256 JPEG)만 쓰이고 없으면 NRO 의 기본 아이콘을 씁니다. 이미지는 저장소에 없으니 필요하면 직접 구해 위 위치에 두세요. 배너와 스크린샷은 다루지 않습니다.

**3. 확인하고 실행**

```
python3 build.py guide abuse    # 빈 칸과 구하는 곳 확인
python3 build.py abuse --zip
```

NRO 는 구하지 않아도 됩니다. `in/` 에 없으면 capsterx-switch/abuse 릴리스 v0.8r3 에서 받아 sha256 을 확인하고 씁니다.

- 스위치 포트 소스: https://github.com/capsterx-switch/abuse
<!-- quick:end -->

크랙 닷 컴의 1996년 런앤건 액션 어뷰즈의 스위치 포트. 공개된 원작 데이터가 NRO 안에 들어 있습니다.

- 업스트림: [capsterx-switch/abuse](https://github.com/capsterx-switch/abuse) v0.8r3
- 상태: 기기 시험 전 (`planned`)
- 한국어: 지원하지 않는다

원작 데이터는 퍼블릭 도메인으로 풀렸고, 이 포트는 그 데이터를 NRO 의 romfs(약 74MB)에 넣어 둔다. 릴리스 zip 에서 NRO 만 꺼내 쓴다. NRO 안의 버전 표기는 0.8r2 다.

```
python3 build.py abuse --deploy <homebrew 폴더>
```
