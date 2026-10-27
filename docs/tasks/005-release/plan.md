# 버전을 0.15.0으로 올리고 문서를 맞춘다

## 목표
두 매니페스트의 버전이 0.15.0이 되고, 맥락 문서와 README가 이 tasks가 바꾼 동작과 맞는다.

## 범위 밖
- 스킬 본문을 고치는 것. 앞 task들이 했다
- GitHub 이슈를 닫는 것

## 완료 조건
1. 두 매니페스트의 버전이 0.15.0이고, 마켓플레이스가 유효하고, 테스트가 통과한다.
   - 확인: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json`의 두 줄이 모두 `0.15.0`
   - 확인: `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
   - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
2. 맥락 문서와 README가 이 tasks가 바꾼 동작과 맞는다. 바뀐 동작은 여섯이다: plan이 앞에서 고칠 파일을 줄 번호 대신 절 이름이나 항목 이름으로 가리킨다, plan이 동작을 바꾸는 완료 조건에 돌려 보는 확인이나 `- 돌리지 않음: {까닭}` 줄을 둔다, check와 retro가 수행의 "남은 것"을 판정한다, run이 로컬 기본 브랜치에만 있는 커밋을 알리고 되돌릴지 묻고 갈라진 곳은 로컬 기본 브랜치의 merge-base다, review가 결과물인 마크다운만 바뀐 tasks의 테스트 적절성을 완료 조건으로 매긴다, eval의 정해 둔 물음은 run의 물은 자리 가운데 `멈춤` 말고 모두다.
   - 확인: `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `README.md`를 문서마다 따로 읽어, 여섯 동작 가운데 어느 것과도 어긋나는 줄이 없다. 어긋나는 줄이 하나라도 있으면 실패

## 결정
- 버전은 0.15.0이다. 이유: 동작이 바뀌어 tasks마다 마이너를 올린다 (추천안으로 정함)
