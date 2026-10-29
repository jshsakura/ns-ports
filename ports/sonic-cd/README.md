# 소닉 CD (Sonic CD 2011)

<!-- quick:begin -->
## 필요한 파일과 명령어

**1. 받아서 둘 것**

| 놓을 위치 | 무엇 | 구하는 곳 |
| :--- | :--- | :--- |
| `ports/sonic-cd/in/scd2011.nro` | 스위치용 NRO | https://github.com/heyjoeway/Sonic-CD-11-Decompilation 의 릴리스를 받거나 직접 빌드 |
| `ports/sonic-cd/in/data` | Data.rsdk (Steam/모바일 리마스터 데이터) | 내가 가진 정품 데이터 (--rom <폴더> 로 따로 줘도 된다) |
| `ports/sonic-cd/icon.jpg` | 앱 아이콘 (256x256 JPEG) (선택) | 직접 구하거나 만든다. 없으면 NRO 에 든 아이콘을 그대로 쓴다 |

**2. 이미지**: 앱 아이콘(`icon.jpg`, 256x256 JPEG)만 쓰이고 없으면 NRO 의 기본 아이콘을 씁니다. 이미지는 저장소에 없으니 필요하면 직접 구해 위 위치에 두세요. 배너와 스크린샷은 다루지 않습니다.

**3. 확인하고 실행**

```
python3 build.py guide sonic-cd    # 빈 칸과 구하는 곳 확인
python3 build.py sonic-cd --zip
```

- 원 프로젝트: https://github.com/RSDKModding/RSDKv3-Decompilation
- 스위치 포트 소스: https://github.com/heyjoeway/Sonic-CD-11-Decompilation
<!-- quick:end -->

소닉 CD 2011 리마스터 네이티브 디컴파일 포트. 60fps 와이드스크린 & 테일즈 플레이

- 엔진: RSDKv3 Decomp
- 필요한 것: Data.rsdk (Steam/모바일 리마스터 데이터)
- Required files: scd2011.nro, Data.rsdk, settings.ini
- Features: 60fps 16:9 widescreen, US/JP Dual OST, Tails unlockable
- Status: Verified & 100% playable on Nintendo Switch!

## 사용
`in/scd2011.nro` 에 빌드된 NRO 를 두고, 내 게임 데이터 폴더를 지정한다.
```
python3 build.py sonic-cd --rom <게임 데이터 폴더> --zip          # 또는 --deploy <homebrew 폴더>
```
덮어쓸 설정 파일은 `overlay/` 에 있다. 게임 데이터와 NRO 는 저장소에 없다.
