# wwhd NRO 빌드

`build.py wwhd` 는 만들어진 NRO 를 받아 조립만 한다. NRO 는 [centollOS/SwitchWakerHD](https://github.com/centollOS/SwitchWakerHD)(내가 쓴 것은 커밋 9a57081)를 직접 빌드해 만든다. 릴리스 바이너리는 없다. 4코어 8GB aarch64 보드에서 한 절차다.

1. 내 Wii U 덤프(USA, title 0005000010143500, 버전 0, NUS 형식)를 풀어 `game/{code,content,meta}` 를 만든다(1018개). 복호화에는 Wii U 공용키가 필요하고, 키는 내 콘솔에서 읽는다. 키 값은 어디에도 적지 않는다.
2. 이 저장소의 한글 판을 쓸 거면 조립 단계(`build.py wwhd`)가 한글 pack 을 만들어 주므로 덤프에는 패치를 덮지 않아도 된다.
3. `python3 tools/switch/make_sd.py --game-dir <game> --jobs 2` 를 SwitchWakerHD 폴더에서 실행한다. `code/cking.rpx` 가 USA v0 인지 확인하고, PPC 를 C 로 재컴파일한 뒤 `devkitpro/devkita64:latest` 도커로 NRO 를 빌드한다(ninja 429단계). 결과는 `build/switch-dk/wwhd.nro` 이다.
4. 셰이더 캐시는 만들어지지 않는다. 첫 실행에 기기에서 컴파일하고(약 20분, 이후 저장, 독 권장, B 로 건너뜀) 이후 저장된다.

실행은 아무 게임 아이콘 위에서 R 을 길게 눌러 hbmenu 를 연 뒤 한다. 앨범 애플릿은 메모리가 모자란다. 게임은 `sdmc:/switch/wwhd/game/`, NRO 는 `sdmc:/switch/wwhd/wwhd.nro` 에 둔다.
