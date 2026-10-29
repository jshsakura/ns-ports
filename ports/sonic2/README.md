# 소닉 더 헤지혹 2 (Sonic 2 2013)

<!-- quick:begin -->
## 필요한 파일과 명령어

**1. 받아서 둘 것**

| 놓을 위치 | 무엇 | 구하는 곳 |
| :--- | :--- | :--- |
| `ports/sonic2/in/s22013.nro` | 스위치용 NRO | https://github.com/heyjoeway/Sonic-1-2-2013-Decompilation 의 릴리스를 받거나 직접 빌드 |
| `ports/sonic2/in/data` | Data.rsdk (모바일 2013 리마스터 데이터) | 내가 가진 정품 데이터 (--rom <폴더> 로 따로 줘도 된다) |
| `ports/sonic2/icon.jpg` | 앱 아이콘 (256x256 JPEG) (선택) | 직접 구하거나 만든다. 없으면 NRO 에 든 아이콘을 그대로 쓴다 |

**2. 이미지**: 앱 아이콘(`icon.jpg`, 256x256 JPEG)만 쓰이고 없으면 NRO 의 기본 아이콘을 씁니다. 이미지는 저장소에 없으니 필요하면 직접 구해 위 위치에 두세요. 배너와 스크린샷은 다루지 않습니다.

**3. 확인하고 실행**

```
python3 build.py guide sonic2    # 빈 칸과 구하는 곳 확인
python3 build.py sonic2 --zip
```

- 원 프로젝트: https://github.com/RSDKModding/RSDKv4-Decompilation
- 스위치 포트 소스: https://github.com/heyjoeway/Sonic-1-2-2013-Decompilation
<!-- quick:end -->

소닉 2 2013 리마스터 네이티브 디컴파일 포트. 공식 한국어(Language=8) 지원

- 엔진: RSDKv4 Decomp
- 필요한 것: Data.rsdk (모바일 2013 리마스터 데이터)
- Required files: s22013.nro, Data.rsdk, settings.ini
- Localization: Language=8 (Korean official UI & localization)
- Features: 60fps 16:9 widescreen, Hidden Palace Zone, Tails & Knuckles support
- Status: Verified & 100% playable on Nintendo Switch!

## 사용
`in/s22013.nro` 에 빌드된 NRO 를 두고, 내 게임 데이터 폴더를 지정한다.
```
python3 build.py sonic2 --rom <게임 데이터 폴더> --zip          # 또는 --deploy <homebrew 폴더>
```
덮어쓸 설정 파일은 `overlay/` 에 있다. 게임 데이터와 NRO 는 저장소에 없다.
