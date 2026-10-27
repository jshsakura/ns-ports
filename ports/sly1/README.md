# 슬라이 쿠퍼 1 (Sly Cooper and the Thievius Raccoonus)

PS2 슬라이 쿠퍼 1을 디컴파일한 네이티브 포트. 업스트림 [NaGaa95/ProjectCane](https://github.com/NaGaa95/ProjectCane) 0.5.0 의 `ProjectCane.nro` 를 쓴다.
게임 데이터는 앱이 처음 실행할 때 SD 카드의 ISO 를 골라 `sdmc:/switch/ProjectCane` 에 직접 풀어 준다. 그래서 이 저장소는 NRO 만 배포한다.

- 지원하는 ISO: 미국 `SCUS-971.98`, 유럽 `SCES-509.17`, 일본 `SCPS-150.36`
- 업스트림은 한국판(`SCKA_200.04`)을 거절한다. 이 포트는 `tools/sly1_kr_patch.py` 로 미국판 이름 세 곳을 한국판 이름으로 바꾼 NRO 를 쓴다. 한국판 실행파일의 `LEVELINFO`·사운드뱅크·해설 테이블이 미국판과 같은 오프셋에 같은 구조로 있는 것을 확인했다. 그래서 미국판 경로가 그대로 돈다는 가정이며, 기기에서 추출이 끝나고 한글로 뜨는지는 아직 확인하지 못했다.
- 상태: 기기 시험 전 (`planned`)

## 사용
릴리스의 `ProjectCane.nro` 를 한글판용으로 바꿔 `in/sly1.nro` 에 두고 (저장소에 없다) 조립한다.
```
python3 tools/sly1_kr_patch.py ProjectCane.nro ports/sly1/in/sly1.nro
```
```
python3 build.py sly1 --deploy <homebrew 폴더>
```
