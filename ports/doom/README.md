# GZDoom (Doom 1 & FreeDoom)

<!-- quick:begin -->
## 필요한 파일과 명령어

**1. 받아서 둘 것**

| 놓을 위치 | 무엇 | 구하는 곳 |
| :--- | :--- | :--- |
| `ports/doom/in/gzdoom_launcher.nro` | 스위치용 NRO (선택) | 안 둬도 된다. 없으면 fgsfdsfgs/gzdoom 릴리스 nx4.11pre-2 에서 자동으로 받는다 |
| `ports/doom/in/data` | 자체 무료 IWAD 포함 (상용 IWAD 추가 지원) (선택) | 안 둬도 된다. 릴리스의 gzdoom_nx_10_4.10.zip, freedoom-0.13.0.zip 를 받아 함께 넣는다 |
| `ports/doom/icon.jpg` | 앱 아이콘 (256x256 JPEG) (선택) | 직접 구하거나 만든다. 없으면 NRO 에 든 아이콘을 그대로 쓴다 |

**2. 이미지**: 앱 아이콘(`icon.jpg`, 256x256 JPEG)만 쓰이고 없으면 NRO 의 기본 아이콘을 씁니다. 이미지는 저장소에 없으니 필요하면 직접 구해 위 위치에 두세요. 배너와 스크린샷은 다루지 않습니다.

**3. 확인하고 실행**

```
python3 build.py guide doom    # 빈 칸과 구하는 곳 확인
python3 build.py doom --zip
```

NRO 는 구하지 않아도 됩니다. `in/` 에 없으면 fgsfdsfgs/gzdoom 릴리스 nx4.11pre-2 에서 받아 sha256 을 확인하고 씁니다.

게임 데이터도 구하지 않아도 됩니다. 릴리스에 든 `gzdoom_nx_10_4.10.zip`, `freedoom-0.13.0.zip` 를 받아 sha256 을 확인하고 풀어 넣습니다.

- 원 프로젝트: https://github.com/ZDoom/gzdoom
- 스위치 포트 소스: https://github.com/fgsfdsfgs/gzdoom
<!-- quick:end -->

- 엔진: GZDoom NX (fgsfdsfgs)
- 라이선스: 자유 배포 가능. 조립할 때 프리둠 Phase 1 & 2(`freedoom1.wad`, `freedoom2.wad`)와 라이선스 고지를 freedoom 0.13.0 릴리스에서 받아 `gzdoom/iwads/` 에 넣는다. 둠 1 셰어웨어(`doom1.wad`)는 받을 고정 주소가 없어 넣지 않는다. 필요하면 직접 `gzdoom/iwads/` 에 둔다
- 설치 경로: `sdmc:/switch/doom/`
- 실행 파일: `gzdoom_launcher.nro`
