# 단테스 인페르노 (Dante's Inferno)

Xbox 360판(유럽판 + Title Update 2)을 [ReXGlue](https://github.com/rexglue/rexglue-sdk) 로 정적 리컴파일하고 deko3d 로 그리는 네이티브 포트.
업스트림 [VasilkovND/dantes-inferno-nx](https://github.com/VasilkovND/dantes-inferno-nx) v1.1.0 (코드, 셰이더, NRO 는 모두 자기 디스크로 컴퓨터에서 만든다).
이 저장소에는 NRO, 셰이더, 게임 데이터, 번역 데이터가 없다.

- 상태: 기기 시험 전 (`planned`). 한글판 데이터 검증까지만 했다.

## 준비물 (자기 것)
| 파일 | 설명 |
|---|---|
| `in/dantes-inferno-nx.nro` | 업스트림 INSTALL.md 대로 만든 NRO |
| `dante_shaders.dslib`, `shadercache_dksh.bin` | 같은 방법으로 만든 셰이더 |
| `game/` | `bigfile0.viv`, `bigfile1.viv`, `default.xex`, `default.xexp`(TU2) 등 |

위 셋(셰이더 2개와 `game/`)을 한 폴더에 둔 것이 `--rom` 에 넘기는 데이터 폴더다.

## 한글판 만들기
한글패치는 비공식 팬 패치(번역과 폰트는 PS3 한글패치 제작자들의 작업물)라서 이 저장소에 넣지 않는다.
Windows 에서는 패치의 `.cmd` 를 실행하면 되고, 리눅스에서는 그 `.cmd` 를 그대로 읽는 도구가 있다.
원본은 건드리지 않고 사본을 만든다. 원본과 결과는 SHA-256 으로 검증한다(지원 원본: 유럽판 TU2 영문).

```
python3 tools/dante_kr_patch.py --cmd DantesInferno_Switch_KR_v1.0.cmd --game <영문 game 폴더> --out <한글판 game 폴더>
```
패치 뒤 `bigfile0.viv` 는 3,321,966,592 바이트, `bigfile1.viv` 는 2,823,608,320 바이트여야 한다.
게임 언어는 **영어**로 둔다. 한글이 영어 자리에 들어 있다.

## 조립
```
python3 build.py dantes-inferno --rom <데이터 폴더> --deploy <homebrew 폴더>
```

## 실행 때 주의
- 오버클럭(특히 GPU)을 권장한다. 처음 보는 장면에서는 셰이더를 만드느라 잠깐 끊긴다.
- 홈 화면 아이콘이 필요하면 업스트림 방식대로 포워더를 따로 만든다(타이틀 ID 는 업스트림 문서 참조).
- 문제가 생기면 SD 카드의 `switch/dantes-inferno-nx/logs/` 최근 로그를 본다.
