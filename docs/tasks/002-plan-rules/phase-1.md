# Phase 1: plan 본문과 테스트와 문서를 고친다

**목표**: plan 본문의 세 이슈가 고쳐지고, 그 규칙 글의 테스트가 더해지고, `test_skill_rules.py` 줄이 맞춰진다.

**테스트 먼저**: 아니오 — 고치는 것은 스킬 본문(`.md`)이고, 더하는 테스트는 그 글이 있는지를 볼 뿐 코드의 동작을 바꾸지 않는다

**읽을 것**
- `plugins/plate/skills/plan/SKILL.md`의 "6. 초안을 보여 주고 승인받는다", 적는 규칙의 "조건"과 "phase의 파일" (고칠 자리)
- `gh issue view 46`, `gh issue view 52`, `gh issue view 53` (이슈마다의 원인과 해결책. #46은 plan의 "조건" 쪽만 이 task의 일이고, run 8번 쪽은 001이 고쳤다)
- `tests/test_skill_rules.py` (001이 더한 run 테스트(#46, #47, #48, #51)와 `section` 도우미의 꼴. 001은 이 파일의 모듈 docstring과 run 테스트들을 고쳤다)
- `docs/ARCHITECTURE.md` 디렉터리 구조의 `test_skill_rules.py` 줄 (001이 run 규칙을 더한 줄. 이 task가 plan 규칙을 더한다), `docs/PRD.md`의 3, `README.md`의 스킬 표의 `plan` 행

**TODO**
- [x] 적는 규칙 "조건"의 남은 결과를 읽는 확인 항목에, 돌려 본 결과가 지금 본문의 것인지는 커밋 시각이 아니라 돌릴 때 적은 본문 해시(`git hash-object`)와 `git rev-parse HEAD:<경로>`로 견준다는 글이 더해진다 (`plugins/plate/skills/plan/SKILL.md`)
- [x] 적는 규칙 "phase의 파일"의 읽을 것 항목에, 앞 task의 변경에 기대면 이슈 번호만으로 가리키지 않고 그 파일의 절 이름과 바뀐 글을 찾을 수 있게 적는다는 글이 더해진다 (`plugins/plate/skills/plan/SKILL.md`)
- [x] 6번의 점검 목록에, 돌려 보는 확인마다 차림이 앞 단계를 지나 기대한 자리에 닿는지, 기대가 해결 방식이 아니라 관찰할 결과로 적혔는지, 결정과 TODO가 같은 멈출 자리를 말하는지 보고, 아니면 고친다는 항목이 더해진다 (`plugins/plate/skills/plan/SKILL.md`)
- [x] 위 셋의 규칙 글이 제 절에 있는지 보는 테스트가 이슈마다 더해지고, 모듈 docstring의 이슈 목록에 plan의 #46, #52, #53이 더해진다 (`tests/test_skill_rules.py`)
- [x] 디렉터리 구조의 `test_skill_rules.py` 줄에 이번 plan 규칙(돌려 본 결과의 해시 견줌, 앞 task 변경의 읽을 것, 장면 확인의 초안 점검)이 더해지고, 001이 더한 run 규칙은 그대로 남는다 (`docs/ARCHITECTURE.md`)

**통과 조건**
- 완료 조건 1이 참이다
  - 확인: `plugins/plate/skills/plan/SKILL.md`의 "조건", "phase의 파일", "6. 초안을 보여 주고 승인받는다"를 읽어 #46, #52, #53의 해결이 task 머리 완료 조건 1의 글대로 저마다 적혀 있다. 하나라도 없으면 실패
- 완료 조건 2가 참이다
  - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
  - 확인: `mktemp -d`에 `git archive HEAD`를 풀어 plan 본문 6번에서 #53의 점검 글을 지우고 돌리면 실패한다. 다시 풀어 "조건"에서 #46의 해시 글을 지우고 돌리면 실패한다
- 완료 조건 3이 참이다
  - 확인: `docs/ARCHITECTURE.md` 디렉터리 구조의 `test_skill_rules.py` 줄이 001의 run 규칙과 이 task의 plan 규칙을 모두 담고, `docs/PRD.md`의 3과 `README.md`의 `plan` 행에 1의 세 규칙과 어긋나는 줄이 없다. 하나라도 어긋나면 실패

## 한 일
- 적는 규칙 "조건"의 남은 결과를 읽는 확인 항목에 해시 견줌 글: 그 항목 끝에 "돌려 본 결과가 지금 본문의 것인지는 커밋 시각이 아니라 돌릴 때 적은 본문 해시(`git hash-object <경로>`)와 `git rev-parse HEAD:<경로>`로 견준다"와 그 까닭(본문과 결과를 한 커밋에 넣지 못해 시각 견줌이 참이 될 수 없다)이 더해졌다 (`plugins/plate/skills/plan/SKILL.md`)
- 적는 규칙 "phase의 파일"의 읽을 것 항목에 앞 task 변경 글: "앞 task의 변경에 기대면 이슈 번호만으로 가리키지 않고, 그 파일의 경로와 절 이름과 바뀐 글을 찾을 수 있게 적는다"와 그 까닭이 더해졌다 (`plugins/plate/skills/plan/SKILL.md`)
- 6번 점검 목록에 돌려 보는 확인의 점검: 차림이 앞 단계를 지나 기대한 자리에 닿는지, 기대가 해결 방식이 아니라 관찰할 결과로 적혔는지, 결정과 TODO가 같은 멈출 자리를 말하는지 보고, 아니면 고친다는 항목이 "뒤 phase의 실행 조건" 항목 앞에 더해졌다 (`plugins/plate/skills/plan/SKILL.md`)
- 테스트: `PlanRulesTest`에 `test_46_rerun_results_compared_by_body_hash`("조건"), `test_52_earlier_task_changes_named_by_section_and_text`("phase의 파일"), `test_53_draft_check_for_run_scenes`(6번)가 더해지고, 모듈 docstring의 plan 이슈 목록이 `#37·#41·#46·#52·#53`이 됐다 (`tests/test_skill_rules.py`)
- ARCHITECTURE: 디렉터리 구조의 `test_skill_rules.py` 줄에 "돌려 본 결과를 본문 해시로 견줌, 앞 task 변경을 절 이름과 바뀐 글로 가리키는 읽을 것, 돌려 보는 확인의 차림·기대·결정과 TODO의 맞물림을 보는 초안 점검"이 더해졌고, 001의 run 규칙(시각·해시로 보는 파일을 고칠 때의 멈춤, git 명령에 명령 치환 없음, 계획 수정마다의 결정 줄, 표지 줄)은 그대로다 (`docs/ARCHITECTURE.md`)

## 확인 결과
- 완료 조건 1이 참이다
  - `plugins/plate/skills/plan/SKILL.md`의 "조건", "phase의 파일", "6. 초안을 보여 주고 승인받는다"를 읽음 → "조건"에 본문 해시(`git hash-object`)와 `git rev-parse HEAD:<경로>`로 견주는 글(#46), "phase의 파일" 읽을 것 항목에 이슈 번호만 적지 않고 절 이름과 바뀐 글을 찾을 수 있게 적는 글(#52), 6번에 차림·기대·결정과 TODO의 세 점검 글(#53)이 저마다 있다. 통과
- 완료 조건 2가 참이다
  - `python3 -m unittest discover -s tests` → `Ran 156 tests in 16.035s` / `OK`. 통과
  - 작업 트리의 스냅숏(`git stash create` → `948bf46`)을 `git archive`로 `mktemp -d`에 풀어 6번에서 #53의 점검 줄을 지우고 돌림 → `FAIL: test_53_draft_check_for_run_scenes (test_skill_rules.PlanRulesTest)` / `FAILED (failures=1)`. 다시 풀어 "조건"에서 #46의 해시 문장을 지우고 돌림 → `FAIL: test_46_rerun_results_compared_by_body_hash (test_skill_rules.PlanRulesTest)` / `FAILED (failures=1)`. 통과
- 완료 조건 3이 참이다
  - `docs/ARCHITECTURE.md` 39줄(`test_skill_rules.py` 줄)을 읽음 → 001의 run 규칙(#46 시각·해시로 보는 파일을 고칠 때의 멈춤, #47 명령 치환 없음, #48 결정 줄, #51 표지 줄)과 이 task의 plan 규칙(#46, #52, #53)이 모두 있다. `docs/PRD.md` 핵심 기능 3과 `README.md` 스킬 표의 `plan` 행을 읽음 → plan을 요약만 하고 세 규칙과 어긋나는 줄이 없다. 통과

## 계획과 달라진 점
- 통과 조건의 삭제 확인은 `git archive HEAD`로 적혀 있으나 수행 중에는 변경이 아직 커밋 전이라, 같은 내용인 작업 트리 스냅숏(`git stash create`의 커밋)을 `git archive`로 풀어 돌렸다. 커밋 뒤의 HEAD 트리와 내용이 같다

## 남은 것
- 테스트는 규칙 글이 제 절에 있는지만 본다. plan이 초안 점검에서 실제로 그 규칙대로 하는지는 돌려 보지 않았다(task 머리의 `- 돌리지 않음` 줄이 정한 것)

## 하네스에서 걸린 것
- 통과 조건이 `git archive HEAD`를 풀어 돌리라고 하지만, phase 스킬은 통과 조건을 돌린 뒤 커밋하므로 그 시점의 HEAD에는 이 phase의 변경이 없다. 작업 트리 스냅숏으로 대신했다

## 확인 1

**통과 조건**
- 완료 조건 1이 참이다
  - `plugins/plate/skills/plan/SKILL.md`를 읽음 → 적는 규칙 "조건"(245줄)에 커밋 시각이 아니라 본문 해시(`git hash-object <경로>`)와 `git rev-parse HEAD:<경로>`로 견준다는 글(#46), "phase의 파일"(276줄) 읽을 것 항목에 앞 task의 변경에 기대면 이슈 번호만으로 가리키지 않고 경로와 절 이름과 바뀐 글을 찾을 수 있게 적는다는 글(#52), "6. 초안을 보여 주고 승인받는다"(101줄)에 차림이 앞 단계를 지나 기대한 자리에 닿는지, 기대가 관찰할 결과로 적혔는지, 결정과 TODO가 같은 멈출 자리를 말하는지 본다는 글(#53)이 있다. 통과
- 완료 조건 2가 참이다
  - `python3 -m unittest discover -s tests` → `Ran 156 tests in 15.992s` / `OK`. 통과
  - `mktemp -d`에 `git archive HEAD`(580f722)를 풀어 6번의 #53 점검 줄을 지우고 돌림 → `FAIL: test_53_draft_check_for_run_scenes` / `FAILED (failures=1)`. 다시 풀어 "조건"의 #46 해시 문장 둘을 지우고 돌림 → `FAIL: test_46_rerun_results_compared_by_body_hash` / `FAILED (failures=1)`. 통과
- 완료 조건 3이 참이다
  - `docs/ARCHITECTURE.md` 39줄 → 001의 run 규칙(시각·해시로 보는 파일을 고칠 때의 멈춤, 명령 치환 없음, 계획 수정마다의 결정 줄, 표지 줄)과 이 task의 plan 규칙(본문 해시 견줌, 앞 task 변경을 절 이름과 바뀐 글로 가리키는 읽을 것, 차림·기대·결정과 TODO의 초안 점검)이 모두 있다. `docs/PRD.md` 핵심 기능 3과 `README.md` 9줄 `plan` 행은 plan을 요약만 하고 세 규칙과 어긋나는 줄이 없다. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 156 tests` / `OK`. 통과

**남은 것**
- 테스트는 규칙 글이 제 절에 있는지만 보고, plan이 초안 점검에서 실제로 그 규칙대로 하는지는 돌려 보지 않았다 → 돌려 보지 않은 위험이고 통과 조건(완료 조건 1)이 보는 동작에 걸리나, task 머리 완료 조건 1의 `- 돌리지 않음: plan은 사람에게 묻고 초안마다 승인을 받는 스킬이라, 초안 점검의 동작은 여러 턴의 답을 이어야 닿는다` 줄이 돌리지 않기로 정한 동작이다. 하네스에서 걸린 것

**실패**
- 없음

**하네스에서 걸린 것**
- 남은 것: plan이 초안 점검에서 실제로 새 규칙대로 하는지는 돌려 보지 않았다(task 머리 완료 조건 1의 `돌리지 않음` 줄이 정한 것)

**판정**: 통과
