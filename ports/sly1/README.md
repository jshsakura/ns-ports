# 슬라이 쿠퍼 1 (Sly Cooper and the Thievius Raccoonus)

<!-- quick:begin -->
## 필요한 파일과 명령어

필요한 것: 슬라이 쿠퍼 1 PS2 ISO (미국 SCUS-971.98, 유럽 SCES-509.17, 일본 SCPS-150.36 중 하나)
NRO: `ports/sly1/in/ProjectCane.nro`

- 원 프로젝트: https://github.com/theclub654/ProjectCane
- 스위치 포트 소스: https://github.com/NaGaa95/ProjectCane

```
python3 build.py check sly1    # 빈 칸 확인
python3 build.py sly1 --zip
```
<!-- quick:end -->

PS2 슬라이 쿠퍼 1을 디컴파일한 네이티브 포트. 업스트림 [NaGaa95/ProjectCane](https://github.com/NaGaa95/ProjectCane) 0.5.0 의 `ProjectCane.nro` 를 쓴다.
게임 데이터는 앱이 처음 실행할 때 SD 카드의 ISO 를 골라 `sdmc:/switch/ProjectCane` 에 직접 풀어 준다. 그래서 이 저장소는 NRO 만 배포한다.

- 지원하는 ISO: 미국 `SCUS-971.98`, 유럽 `SCES-509.17`, 일본 `SCPS-150.36`
- **한국판(`SCKA_200.04`)은 거절된다.** 설치기가 디스크 루트의 실행파일 이름으로 판을 가리는데 한국판 이름이 목록에 없다. 한국판을 받게 하려면 추출기의 지역 추가와 오프셋 확인이 필요하다.
- 상태: 기기 시험 전 (`planned`)

## 사용
`in/sly1.nro` 에 릴리스의 `ProjectCane.nro` 를 두고 (저장소에 없다) 조립한다.
```
python3 build.py sly1 --deploy <homebrew 폴더>
```
