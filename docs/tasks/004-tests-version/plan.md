# 버전 줄과 고친 규칙의 테스트를 더하고 0.17.0으로 올린다

## 목표
두 매니페스트의 버전 줄과 앞 task들이 고친 스킬 규칙을 시험하는 테스트가 `tests/`에 더해지고 `docs/BACKLOG.md`의 항목이 지워지며, 두 매니페스트의 버전이 0.17.0이 되고 맥락 문서와 README가 이 tasks가 바꾼 동작과 맞는다.

## 범위 밖
- 스킬 본문을 고치는 것. 앞 task들이 했다
- GitHub 이슈를 닫는 것
- 1.0.0으로 올리는 것

## 완료 조건
1. 두 매니페스트의 버전이 서로 다르면 실패하는 테스트와, 앞 task들이 고친 규칙(run의 #34·#35·#38·#40·#44, plan의 #37·#41, phase의 #42, eval의 #36)의 글이 본문에서 빠지면 실패하는 테스트가 `tests/`에 있다. 테스트는 표준 라이브러리의 `unittest`로 쓴다(ADR-019)
   - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
   - 확인: `mktemp -d`에 저장소를 복사해 `plugins/plate/.codex-plugin/plugin.json`의 버전만 `0.0.0`으로 바꾸고 그 복사본에서 테스트를 돌리면 마지막 줄이 `FAILED`로 시작한다
   - 확인: 새로 복사할 때마다 아래 넷 가운데 하나만 지우고 테스트를 돌리면, 넷 모두 마지막 줄이 `FAILED`로 시작한다: run 본문의 "7. task 회고를 맡긴다"에서 `RUNLOG.md`만 넣는 커밋의 글(#44), plan 본문의 적는 규칙 "조건"에서 갈래마다 확인을 두는 글(#37), phase 본문의 "1. 읽는다"에서 앞 phase 기록을 읽지 않는 글(#42), eval 본문의 "2."에서 `남은 것:` 줄의 글(#36)
2. `docs/BACKLOG.md`의 항목("바뀐 동작(버전 줄, 스킬 규칙)을 시험하는 테스트가 `tests/`에 없다")이 지워지고 `# BACKLOG` 줄만 남는다.
   - 확인: `docs/BACKLOG.md`를 읽어 `# BACKLOG` 줄 밖에 항목이 없다
3. 두 매니페스트의 버전이 0.17.0이고 마켓플레이스가 유효하다.
   - 확인: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json`의 두 줄이 모두 `0.17.0`
   - 확인: `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
4. 맥락 문서와 README가 이 tasks가 바꾼 동작과 새 테스트 파일과 맞는다(tasks 완료 조건 5).
   - 확인: `docs/ARCHITECTURE.md`의 "디렉터리 구조"의 `tests/` 아래에 새 테스트 파일이 저마다 한 줄로 있다
   - 확인: `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `README.md`를 문서마다 따로 읽어, run의 시작 권한 물음, `RUNLOG.md`의 커밋 자리, 회고가 계획을 바꾸게 할 때 멈추는 것, plan의 갈래마다 확인과 앞 phase 산출물에 기대는 조건, phase가 앞 phase 기록을 읽지 않는 것, eval의 `남은 것:` 줄, 새 테스트 파일과 어긋나는 줄이 없다. 하나라도 있으면 실패

## 결정
- 새 테스트 파일은 `tests/test_manifests.py`(두 매니페스트의 버전)와 `tests/test_skill_rules.py`(고친 규칙의 글)다 (추천안으로 정함)
- 버전은 0.17.0이다. PR 전에 main이 먼저 0.17.0 이상이 되면 PR에서 다음 마이너로 맞춘다. 이유: tasks 머리의 결정
