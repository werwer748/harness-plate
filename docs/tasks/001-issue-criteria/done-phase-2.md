# Phase 2: run 본문이 "eval에만"을 어디에도 두지 않게 한다

**목표**: run의 tasks 끝이 "eval에만"인 하네스 고칠 거리를 보고에 보이되 고침 task, 이슈, BACKLOG, 감수 어디에도 두지 않는다.

**테스트 먼저**: 아니오 — 바뀌는 동작이 결과물인 마크다운(스킬 본문)의 것이다

**읽을 것**
- `plugins/plate/skills/eval/SKILL.md` ("기록의 양식"의 하네스 고칠 거리. phase 1이 더한 기준 줄)
- `plugins/plate/skills/run/SKILL.md` (낱말의 "하네스 고칠 거리", "보고하고 묻는다" 전체, "BACKLOG를 고친다", "고침 task를 더한다"의 "고침 task의 꼴")
- `tests/test_skill_rules.py` (`RunRulesTest.test_first_proposal_uses_threshold`, `test_project_only_fixes_deferred_to_backlog`, `test_backlog_three_sections`)

**TODO**
- [x] 앞 phase의 산출물(eval 양식의 기준 줄)에 대어 run이 읽는 칸의 이름을 맞춘다 (`plugins/plate/skills/run/SKILL.md`)
- [x] 낱말 "하네스 고칠 거리"에 eval이 고칠 거리마다 기준(넘음, eval에만)을 적고 "eval에만"인 것에는 처리와 문턱이 없다는 것이 더해진다 (`plugins/plate/skills/run/SKILL.md`)
- [x] "보고하고 묻는다" 4번에 고칠 거리마다 기준이 보이게 바뀌고, 6번 고칠 안의 감수할 것 뒤에 `- eval에만: 기준이 eval에만인 하네스 고칠 거리의 번호` 꼴의 줄이 더해진다 (`plugins/plate/skills/run/SKILL.md`)
- [x] 처음 안의 문단 맨 앞에 "eval에만"인 것은 갈래와 상관없이 eval에만에 두고 고침 task, 이슈, BACKLOG, 감수 어디에도 두지 않으며 감수와 문턱보다 먼저 가른다는 글이 더해지고, 그 뒤의 글이 기준을 넘은 것에만 걸리게 바뀐다 (`plugins/plate/skills/run/SKILL.md`)
- [x] 아무것도 고치지 않겠다는 답의 갈래에 eval에만에 둔 것은 그대로 eval에만에 둔다는 글이 더해진다 (`plugins/plate/skills/run/SKILL.md`)
- [x] "고침 task의 꼴"의 고칠 것이 기준을 넘고 처리가 감수가 아닌 이 프로젝트만의 하네스 고칠 거리로 바뀐다 (`plugins/plate/skills/run/SKILL.md`)
- [x] `RunRulesTest`에 `test_eval_only_goes_nowhere`가 더해진다. 6번에 eval에만 줄이 있고, 처음 안에서 eval에만의 글이 감수할 것의 글보다 앞서며, 고침 task의 꼴에 기준을 넘은 것만 드는지, "BACKLOG를 고친다"에 "eval에만"이 없는지 본다. 바뀐 글에 맞춰 위 세 테스트도 고친다 (`tests/test_skill_rules.py`)

**통과 조건**
- run 본문이 완료 조건 2를 이룬다.
  - 확인: `grep -n -e 'eval에만' plugins/plate/skills/run/SKILL.md`가 낱말, 보고하고 묻는다, 고침 task의 꼴의 줄을 낸다
  - 확인: `(cd tests && python3 -m unittest test_skill_rules.RunRulesTest.test_eval_only_goes_nowhere)`가 OK다
- 테스트가 모두 통과한다(완료 조건 6).
  - 확인: `python3 -m unittest discover -s tests`가 OK다

## 한 일
- 앞 phase의 산출물(eval 양식의 기준 줄)에 대어 run이 읽는 칸의 이름을 맞춘다: eval 양식의 `기준: {넘음 | eval에만}` 줄에 맞춰 run이 "기준"과 그 값 "넘음", "eval에만"으로 읽게 했다 (`plugins/plate/skills/run/SKILL.md`)
- 낱말 "하네스 고칠 거리": eval이 고칠 거리마다 먼저 기준(넘음, eval에만)을 적고, "eval에만"인 것에는 처리와 문턱이 없고 `eval.md`에만 남으며, 처리·문턱·이슈는 기준을 넘은 것에만 있다고 고쳤다 (`plugins/plate/skills/run/SKILL.md`)
- "보고하고 묻는다" 4번에 기준(넘음, eval에만)을 보이고 처리·문턱은 기준을 넘은 것에만 보이게 했고, 6번 고칠 안의 감수할 것 뒤에 `- eval에만: 기준이 eval에만인 하네스 고칠 거리의 번호` 줄을 더했다 (`plugins/plate/skills/run/SKILL.md`)
- 처음 안 문단 맨 앞에 "eval에만"인 것은 갈래와 상관없이 eval에만에 두고 고침 task, 이슈, BACKLOG, 감수 어디에도 두지 않으며 기준이 감수와 문턱보다 먼저이고 아래 글은 기준을 넘은 것에만 걸린다는 글을 더했고, "처음 안은 감수할 것과 eval에만을 빼고"로 고쳤다 (`plugins/plate/skills/run/SKILL.md`)
- 아무것도 고치지 않겠다는 갈래에 "eval에만에 둔 것은 그대로 eval에만에 둔다"를 더했다 (`plugins/plate/skills/run/SKILL.md`)
- "고침 task의 꼴"의 고칠 것을 "기준을 넘고 처리가 감수가 아닌 이 프로젝트만의 하네스 고칠 거리다. 기준이 eval에만인 것은 넣지 않는다"로 고쳤다 (`plugins/plate/skills/run/SKILL.md`)
- `RunRulesTest.test_eval_only_goes_nowhere`를 더했다(낱말, 4번, 6번 eval에만 줄과 감수할 것 뒤의 차례, 처음 안에서 eval에만 글이 감수할 것 글보다 앞섬, 아무것도 고치지 않는 갈래, 고침 task의 꼴, "BACKLOG를 고친다"에 "eval에만"이 없음). 위 세 테스트는 바뀐 글로도 통과해, `test_first_proposal_uses_threshold`에 4번의 바뀐 글(`기준을 넘은 plate 자체의 것은 문턱을 넘었는지`)을 보는 줄만 더했다 (`tests/test_skill_rules.py`)

## 확인 결과
- run 본문이 완료 조건 2를 이룬다.
  - `grep -n -e 'eval에만' plugins/plate/skills/run/SKILL.md` → 42(낱말), 346·353·355·360(보고하고 묻는다: 4번, 6번 eval에만 줄, 처음 안, 답의 갈래), 436(고침 task의 꼴)줄. 통과
  - `(cd tests && python3 -m unittest test_skill_rules.RunRulesTest.test_eval_only_goes_nowhere)` → `Ran 1 test` `OK`. 통과
- 테스트가 모두 통과한다(완료 조건 6).
  - `python3 -m unittest discover -s tests` → `Ran 205 tests` `OK`. 통과

## 계획과 달라진 점
- TODO에 없던 고침 하나: 아무것도 고치지 않겠다는 갈래의 "소스 문제와 plate 자체의 하네스 고칠 거리를 모두 BACKLOG로 미룰 것에"를 "기준을 넘은 plate 자체의 하네스 고칠 거리를 모두"로 고쳤다. 같은 줄에 더한 "eval에만에 둔 것은 그대로 eval에만에 둔다"와 "모두"가 부딪히지 않게 하려는 것이다. 같은 TODO 항목의 줄 안의 고침이다
- `test_backlog_three_sections`와 `test_project_only_fixes_deferred_to_backlog`는 바뀐 글로도 통과해 고치지 않았다

## 남은 것
- 같은 "아무것도 고치지 않겠다" 갈래의 "기준을 넘은 plate 자체의 하네스 고칠 거리를 모두 BACKLOG로"는 처리가 감수인 것도 글자로는 품는다(이 phase 전부터 있던 겹침으로, 같은 줄의 "감수할 것에 둔 것은 그대로 감수할 것에 둔다"가 가른다)
- run의 "보고하고 묻는다" 뒤의 동작은 헤드리스로 볼 수 없다(task 머리 완료 조건 2의 돌리지 않음)

## 하네스에서 걸린 것
- 없음

## 확인 1

**통과 조건**
- run 본문이 완료 조건 2를 이룬다.
  - `grep -n -e 'eval에만' plugins/plate/skills/run/SKILL.md` → 42(낱말 "하네스 고칠 거리"), 346·353·355·360(### 보고하고 묻는다: 4번, 6번 eval에만 줄, 처음 안, 아무것도 고치지 않는 갈래), 436(### 고침 task를 더한다의 고침 task의 꼴)줄. 통과
  - `(cd tests && python3 -m unittest test_skill_rules.RunRulesTest.test_eval_only_goes_nowhere)` → `Ran 1 test` `OK`. 통과
- 테스트가 모두 통과한다(완료 조건 6).
  - `python3 -m unittest discover -s tests` → `Ran 205 tests` `OK`. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 205 tests` `OK`. 통과

**남은 것**
- "아무것도 고치지 않겠다" 갈래의 "기준을 넘은 plate 자체의 하네스 고칠 거리를 모두 BACKLOG로"가 처리가 감수인 것도 글자로 품는다 → 감수와 BACKLOG 사이의 겹침이라 통과 조건이 보는 동작("eval에만"을 어디에도 두지 않음, 테스트 통과)에 걸리지 않는다. 하네스에서 걸린 것
- run의 "보고하고 묻는다" 뒤의 동작은 헤드리스로 볼 수 없다 → task 머리 완료 조건 2의 `- 돌리지 않음: run의 "보고하고 묻는다"는 사용자에게 묻고 멈추는 자리라 헤드리스로 끝까지 돌려도 고칠 안의 승인 뒤 동작을 볼 수 없다`가 돌리지 않기로 정한 동작이다. 하네스에서 걸린 것

**실패**
- 없음

**하네스에서 걸린 것**
- 남은 것: "아무것도 고치지 않겠다" 갈래의 "기준을 넘은 plate 자체의 하네스 고칠 거리를 모두 BACKLOG로"가 처리가 감수인 것도 글자로 품는다(같은 줄의 "감수할 것에 둔 것은 그대로 감수할 것에 둔다"가 가른다)
- 남은 것: run의 "보고하고 묻는다" 뒤의 동작은 헤드리스로 볼 수 없다(task 머리 완료 조건 2의 돌리지 않음)

**판정**: 통과
