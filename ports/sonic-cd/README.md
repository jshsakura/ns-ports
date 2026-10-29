# 소닉 CD (Sonic CD 2011)

<!-- quick:begin -->
## 필요한 파일과 명령어

필요한 것: Data.rsdk (Steam/모바일 리마스터 데이터)
NRO: `ports/sonic-cd/in/scd2011.nro`

- 원 프로젝트: https://github.com/RSDKModding/RSDKv3-Decompilation
- 스위치 포트 소스: https://github.com/heyjoeway/Sonic-CD-11-Decompilation

```
python3 build.py check sonic-cd    # 빈 칸 확인
python3 build.py sonic-cd --zip
```
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
