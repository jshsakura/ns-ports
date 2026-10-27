# 슬라이 쿠퍼 1 (Sly Cooper and the Thievius Raccoonus)

PS2 슬라이 쿠퍼 1을 디컴파일한 네이티브 포트. 업스트림 [NaGaa95/ProjectCane](https://github.com/NaGaa95/ProjectCane) 0.5.0 의 `ProjectCane.nro` 를 쓴다.
원판은 게임 데이터를 앱이 처음 실행할 때 SD 카드의 ISO 를 골라 `sdmc:/switch/ProjectCane` 에 직접 풀어 준다. 이 저장소에는 NRO 도 데이터도 없다.

- 지원하는 ISO: 미국 `SCUS-971.98`, 유럽 `SCES-509.17`, 일본 `SCPS-150.36`
- 업스트림은 한국판(`SCKA_200.04`)을 거절한다. 그래서 `tools/sly1_extract/` 로 서버에서 ISO 를 미리 풀어 데이터를 폴더에 넣는다. 받으면 ISO 없이 바로 실행된다. 한국판은 미국판 구조가 아니라 일본판·PAL 쪽 구조라서 추출기 소스를 한국판용으로 고쳐 쓴다.
- 상태: 기기 시험 전 (`planned`)

## 사용
`in/sly1.nro` 에 릴리스의 `ProjectCane.nro` 를 두고 (저장소에 없다) 풀어 둔 데이터와 함께 조립한다. 데이터 만드는 법은 `tools/sly1_extract/README.md` 에 있다.
```
python3 build.py sly1 --rom <풀어낸 폴더> --deploy <homebrew 폴더>
```
