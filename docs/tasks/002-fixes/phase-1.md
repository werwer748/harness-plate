# Phase 1: tasks 끝의 문제를 고친다

**목표**: task 머리의 완료 조건에 적힌 것을 모두 고친다.

**테스트 먼저**: 아니오 — 고칠 것이 스킬 본문(`.md`) 하나뿐이고 코드 파일의 동작을 바꾸지 않는다

**읽을 것**
- `docs/tasks/review.md`의 `## 평가 1` 절
- `docs/tasks/eval.md`의 `## eval 1` 절
- `plugins/plate/skills/plan/SKILL.md`
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/ADR.md`
- `docs/TOOLS.md`
- `docs/BACKLOG.md`

**TODO**
- [x] 작업 트리를 얻는 예로 든 `git stash create`는 추적하지 않는 새 파일을 넣지 않고 새 파일만 바뀌었으면 아무것도 내지 않아, 새 파일을 만드는 phase의 통과 조건이 이 예를 따르면 그 파일이 없는 트리를 본다. 예를 `cp -R` 사본으로 줄이거나 새 파일이 빠진다는 단서를 단다 (`plugins/plate/skills/plan/SKILL.md:249`)

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다

## 한 일
- 작업 트리를 얻는 예로 든 `git stash create`는 추적하지 않는 새 파일을 넣지 않고 새 파일만 바뀌었으면 아무것도 내지 않아, 새 파일을 만드는 phase의 통과 조건이 이 예를 따르면 그 파일이 없는 트리를 본다. 예를 `cp -R` 사본으로 줄이거나 새 파일이 빠진다는 단서를 단다 (`plugins/plate/skills/plan/SKILL.md:249`): 적는 규칙 "조건" 절의 예 `작업 트리(예: \`cp -R\` 사본, \`git stash create\`로 얻은 트리)로 적고`를 `작업 트리(예: \`cp -R\` 사본)로 적고`로 줄였다. 본문에 `stash`가 더 남지 않는다 (`plugins/plate/skills/plan/SKILL.md`)

## 확인 결과
- 완료 조건 1: 적는 규칙 "조건" 절이 작업 트리를 얻는 예로 `git stash create`를 단서 없이 들지 않는다
  - `grep -n stash plugins/plate/skills/plan/SKILL.md` → 출력 없음. "조건" 절(테스트의 `section`으로 `## 적는 규칙`을 자르고 `**조건**`부터 다음 굵은 제목 앞까지)에 `stash` 없음(False). 통과
- 완료 조건 2 / tasks 완료 조건 1: 다섯 글이 저마다 제 절에 있다
  - 스크래치 스크립트로 `6. 초안을 보여 주고 승인받는다` 절과 적는 규칙의 `**조건**`, `**결정**` 소절을 잘라 봄 → 6번에 `수행이 돌릴 확인에 \`HEAD\`가 있는지 본다` True, `task 사이에 같은 글을 바꾸거나 인용하는 곳이 맞물리는지 본다` True; 조건에 `phase의 통과 조건은 커밋 전의 작업 트리에서 돈다` True, `지울 글을 본문에 있는 그대로 인용하고` True, `실패할 테스트 이름을 기대로 적는다` True; 결정에 `앞 task가 바꿀 글을 인용하면 바뀐 뒤의 글 그대로 적고` True. 통과
- 완료 조건 2 / tasks 완료 조건 2: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
  - `python3 -m unittest discover -s tests` → `Ran 164 tests in 17.605s` / `OK`. 통과
- 완료 조건 2: `phase의 통과 조건은 커밋 전의 작업 트리에서 돈다`를 지운 사본
  - `mktemp -d`에 `cp -R plugins tests` 뒤 글 개수 1, 빈 글로 바꾸고 `python3 -m unittest discover -s tests` → `FAIL: test_55_checks_run_on_uncommitted_worktree (test_skill_rules.PlanRulesTest)`, `FAILED (failures=1)`. 통과
- 완료 조건 2: `지울 글을 본문에 있는 그대로 인용하고`를 지운 새 사본
  - 같은 방법, 글 개수 1 → `FAIL: test_56_mutation_checks_quote_text_and_name_test (test_skill_rules.PlanRulesTest)`, `FAILED (failures=1)`. 통과
- 완료 조건 2: `앞 task가 바꿀 글을 인용하면 바뀐 뒤의 글 그대로 적고`를 지운 새 사본
  - 같은 방법, 글 개수 1 → `FAIL: test_57_quote_earlier_task_text_as_changed (test_skill_rules.PlanRulesTest)`, `FAILED (failures=1)`. 통과
- 완료 조건 2 / tasks 완료 조건 3: 두 매니페스트 버전
  - `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → `"version": "0.19.0",` 두 줄. 통과
- 완료 조건 2 / tasks 완료 조건 3: 마켓플레이스 유효
  - `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
- 완료 조건 2 / tasks 완료 조건 3: ARCHITECTURE 줄과 docstring
  - `docs/ARCHITECTURE.md` 39줄의 `test_skill_rules.py` 줄에 `통과 조건은 커밋 전 작업 트리에서 돎`, `지울 글 인용과 실패할 테스트 이름`, `앞 task가 바꿀 글을 바뀐 뒤 꼴로 인용`이 저마다 있음. `tests/test_skill_rules.py` docstring의 plan 목록 `plan의 #37·#41·#46·#52·#53·#55·#56·#57`에 #55·#56·#57 있음. 통과

## 계획과 달라진 점
- 없음

## 남은 것
- 고친 것은 예를 지운 것뿐이라, 이 규칙을 따르는 계획이 `cp -R` 말고 다른 작업 트리 얻는 법을 고르면 그 법이 새 파일을 담는지는 본문이 말하지 않는다

## 하네스에서 걸린 것
- task 머리 완료 조건 2의 첫 확인이 "tasks 완료 조건 1에 백틱으로 적은 다섯 글"을 가리키는데 그 글이 task 머리에 옮겨 적혀 있지 않아, phase 스킬의 "tasks 머리는 읽지 않는다" 규칙을 어기고 `docs/tasks/plan.md`의 완료 조건 절을 읽었다. 그 절에는 백틱 글이 다섯이 아니라 여섯(6번의 두 글 포함) 있어 여섯을 모두 봤다. plan 적는 규칙 "phase를 나누는 기준" 2(phase가 써야 하는 tasks 머리의 정의는 task 머리에 적는다)를 계획이 지키지 않은 곳이다
