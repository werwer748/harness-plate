# 회고

## 회고 1

**확인**
- tasks 완료 조건 2가 참이다
  - `plugins/plate/skills/plan/SKILL.md`를 읽음 → 적는 규칙 "조건"의 남은 결과 항목에 "돌려 본 결과가 지금 본문의 것인지는 커밋 시각이 아니라 돌릴 때 적은 본문 해시(`git hash-object <경로>`)와 `git rev-parse HEAD:<경로>`로 견준다"(#46), "phase의 파일"의 읽을 것 항목에 "앞 task의 변경에 기대면 이슈 번호만으로 가리키지 않고, 그 파일의 경로와 절 이름과 바뀐 글을 찾을 수 있게 적는다"(#52), "6. 초안을 보여 주고 승인받는다"에 돌려 보는 확인마다 차림이 앞 단계를 지나 기대한 자리에 닿는지, 기대가 해결 방식이 아니라 관찰할 결과로 적혔는지, 결정과 TODO가 같은 멈출 자리를 말하는지 보는 항목(#53)이 저마다 있다. 통과
- 1의 규칙마다 글이 빠지면 실패하는 테스트가 있고 모든 테스트가 통과한다
  - `python3 -m unittest discover -s tests` → `Ran 156 tests in 16.092s` / `OK`. 통과
  - `mktemp -d`에 `git archive HEAD`(86933b1)를 풀어 6번의 #53 점검 줄을 지우고 돌림 → `FAIL: test_53_draft_check_for_run_scenes (test_skill_rules.PlanRulesTest)` / `FAILED (failures=1)`. 다시 풀어 "조건"의 #46 해시 문장을 지우고 돌림 → `FAIL: test_46_rerun_results_compared_by_body_hash (test_skill_rules.PlanRulesTest)` / `FAILED (failures=1)`. 통과
- tasks 완료 조건 5의 plan 쪽이 참이다
  - `docs/ARCHITECTURE.md` 디렉터리 구조의 `test_skill_rules.py` 줄을 읽음 → 001의 run 규칙(시각·해시로 보는 파일을 고칠 때의 멈춤, git 명령에 명령 치환 없음, 계획 수정마다의 결정 줄, 표지 줄 `부른 쪽: plate:run`)과 이 task의 plan 규칙(본문 해시 견줌, 앞 task 변경을 절 이름과 바뀐 글로 가리키는 읽을 것, 차림·기대·결정과 TODO의 초안 점검)이 모두 있다. `docs/PRD.md` 핵심 기능 3과 `README.md` 9줄 `plan` 행은 plan을 요약만 하고 세 규칙과 어긋나는 줄이 없다. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 156 tests` / `OK`. 통과

**남은 것**
- phase 1: 테스트는 규칙 글이 제 절에 있는지만 본다. plan이 초안 점검에서 실제로 그 규칙대로 하는지는 돌려 보지 않았다 → 문제 아님 (task 머리 완료 조건 1의 `- 돌리지 않음` 줄과 tasks 머리 결정 "plan과 run은 `돌리지 않음`으로 둔다"가 돌리지 않기로 정한 동작이다)

**문제**
- 없음

**판정**: 통과
