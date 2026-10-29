# Phase 2: run 본문이 "eval에만"을 어디에도 두지 않게 한다

**목표**: run의 tasks 끝이 "eval에만"인 하네스 고칠 거리를 보고에 보이되 고침 task, 이슈, BACKLOG, 감수 어디에도 두지 않는다.

**테스트 먼저**: 아니오 — 바뀌는 동작이 결과물인 마크다운(스킬 본문)의 것이다

**읽을 것**
- `plugins/plate/skills/eval/SKILL.md` ("기록의 양식"의 하네스 고칠 거리. phase 1이 더한 기준 줄)
- `plugins/plate/skills/run/SKILL.md` (낱말의 "하네스 고칠 거리", "보고하고 묻는다" 전체, "BACKLOG를 고친다", "고침 task를 더한다"의 "고침 task의 꼴")
- `tests/test_skill_rules.py` (`RunRulesTest.test_first_proposal_uses_threshold`, `test_project_only_fixes_deferred_to_backlog`, `test_backlog_three_sections`)

**TODO**
- [ ] 앞 phase의 산출물(eval 양식의 기준 줄)에 대어 run이 읽는 칸의 이름을 맞춘다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] 낱말 "하네스 고칠 거리"에 eval이 고칠 거리마다 기준(넘음, eval에만)을 적고 "eval에만"인 것에는 처리와 문턱이 없다는 것이 더해진다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] "보고하고 묻는다" 4번에 고칠 거리마다 기준이 보이게 바뀌고, 6번 고칠 안의 감수할 것 뒤에 `- eval에만: 기준이 eval에만인 하네스 고칠 거리의 번호` 꼴의 줄이 더해진다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] 처음 안의 문단 맨 앞에 "eval에만"인 것은 갈래와 상관없이 eval에만에 두고 고침 task, 이슈, BACKLOG, 감수 어디에도 두지 않으며 감수와 문턱보다 먼저 가른다는 글이 더해지고, 그 뒤의 글이 기준을 넘은 것에만 걸리게 바뀐다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] 아무것도 고치지 않겠다는 답의 갈래에 eval에만에 둔 것은 그대로 eval에만에 둔다는 글이 더해진다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] "고침 task의 꼴"의 고칠 것이 기준을 넘고 처리가 감수가 아닌 이 프로젝트만의 하네스 고칠 거리로 바뀐다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] `RunRulesTest`에 `test_eval_only_goes_nowhere`가 더해진다. 6번에 eval에만 줄이 있고, 처음 안에서 eval에만의 글이 감수할 것의 글보다 앞서며, 고침 task의 꼴에 기준을 넘은 것만 드는지, "BACKLOG를 고친다"에 "eval에만"이 없는지 본다. 바뀐 글에 맞춰 위 세 테스트도 고친다 (`tests/test_skill_rules.py`)

**통과 조건**
- run 본문이 완료 조건 2를 이룬다.
  - 확인: `grep -n -e 'eval에만' plugins/plate/skills/run/SKILL.md`가 낱말, 보고하고 묻는다, 고침 task의 꼴의 줄을 낸다
  - 확인: `(cd tests && python3 -m unittest test_skill_rules.RunRulesTest.test_eval_only_goes_nowhere)`가 OK다
- 테스트가 모두 통과한다(완료 조건 6).
  - 확인: `python3 -m unittest discover -s tests`가 OK다
