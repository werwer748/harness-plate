# Phase 2: 회고 1의 문제를 고친다

**목표**: 회고 1에서 나온 문제를 모두 고친다.

**테스트 먼저**: 아니오 — 고칠 문제가 스킬 본문(`.md`) 하나만 고치고 코드 파일의 동작을 바꾸지 않는다

**읽을 것**
- `docs/tasks/001-plan-rules/retro.md`의 `## 회고 1` 절
- `plugins/plate/skills/plan/SKILL.md`
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/ADR.md`
- `docs/TOOLS.md`
- `docs/BACKLOG.md`

**TODO**
- [x] plan 본문 안에서 이번에 더한 규칙과 그 위의 규칙이 서로 다른 것을 시킨다. 적는 규칙 "조건" 248줄(이번 task 전부터 있던 줄)은 돌려 본 결과가 지금 본문의 것인지를 "돌릴 때 적은 본문 해시(`git hash-object <경로>`)와 `git rev-parse HEAD:<경로>`로 견준다"고 `HEAD`를 보는 꼴을 시키는데, 이번에 더한 249줄은 "`HEAD`를 풀거나 보는 확인은 작업 트리…로 적고"라 하고 6번 102줄은 "수행이 돌릴 확인에 `HEAD`가 있는지 본다(예: … `HEAD`의 파일과 견준다)… 있으면 작업 트리로 보는 확인으로 고친다"라 해, 248줄대로 적은 확인을 6번이 고치라고 한다. 어느 쪽이 맞는지(248줄의 `HEAD:<경로>`가 예외인지, 작업 트리의 `git hash-object`로 바꿀지)가 본문에 없어 plan이 둘 가운데 하나를 묻지 않고 고른다. 두 규칙이 같은 것을 시키도록 고친다. 고칠 동작을 적은 맥락 문서와 README의 줄도 맞춘다 (`plugins/plate/skills/plan/SKILL.md`)

**통과 조건**
- 회고 1의 문제가 모두 고쳐졌다.
  - 확인: TODO에 넣은 문제마다 적힌 곳과 그 동작을 적은 맥락 문서와 README의 줄을 다시 읽거나 돌린다
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다

## 한 일
- plan 본문 안의 248줄과 249줄·6번의 `HEAD` 충돌을 고친다: 적는 규칙 "조건"의 해시 견줌 글을 "돌릴 때 적은 본문 해시(`git hash-object <경로>`)와 확인할 때 작업 트리에서 다시 낸 `git hash-object <경로>`로 견준다. `HEAD:<경로>`와 견주지 않는다. 아래 규칙대로 통과 조건은 커밋 전의 작업 트리에서 돌아 `HEAD`에는 그 phase가 고친 본문이 없다."로 바꿔, 해시 견줌도 작업 트리를 보게 해 249줄·6번의 `HEAD` 점검과 같은 것을 시키게 했다 (`plugins/plate/skills/plan/SKILL.md`). 옛 글을 그대로 찾던 `test_46_rerun_results_compared_by_body_hash`를 새 글, `` `HEAD:<경로>`와 견주지 않는다 ``, `git rev-parse HEAD:`가 조건 절에 없음을 보게 고쳤다 (`tests/test_skill_rules.py`). 맥락 문서와 README에는 이 해시를 `HEAD`와 견준다는 줄이 없어(`grep -n '본문 해시\|HEAD' docs/ADR.md docs/PRD.md README.md docs/BACKLOG.md`, `docs/ARCHITECTURE.md`의 "돌려 본 결과를 본문 해시로 견줌") 고칠 줄이 없었다

## 확인 결과
- 회고 1의 문제가 모두 고쳐졌다.
  - `grep -n 'rev-parse HEAD' plugins/plate/skills/plan/SKILL.md` → 출력 없음. 조건 절의 해시 글이 작업 트리의 `git hash-object`와 견주고 `HEAD:<경로>`와 견주지 않는다고 적힌 것을 읽음. 맥락 문서·README의 해당 줄(위 grep, ARCHITECTURE 39줄의 "돌려 본 결과를 본문 해시로 견줌")이 새 글과 어긋나지 않음. 통과
- task 머리의 완료 조건이 모두 참이다.
  - 완료 조건 1: `section`·`part`로 뽑은 "조건"·"결정"·6번에서 여섯 글과 `cp -R` 사본·`phase-N.md`를 빼고 본다는 글 → `True True True True True True True`, 다섯 글 저마다 `grep -o -F … | wc -l` → 모두 `1`. 통과
  - 완료 조건 2: `python3 -m unittest discover -s tests` → `Ran 164 tests in 16.269s` / `OK`. 사본 셋(`mktemp -d`, `cp -R plugins tests`)에서 글마다 `count: 1` 뒤 빈 글로 바꿈 → `FAIL: test_55_checks_run_on_uncommitted_worktree (test_skill_rules.PlanRulesTest)`, `FAIL: test_56_mutation_checks_quote_text_and_name_test (test_skill_rules.PlanRulesTest)`, `FAIL: test_57_quote_earlier_task_text_as_changed (test_skill_rules.PlanRulesTest)` 저마다 `FAILED (failures=1)`. 통과
  - 완료 조건 3: `grep -h '"version"' …` → `"version": "0.19.0",` 두 줄. `claude plugin validate .` → `✔ Validation passed`. ARCHITECTURE의 `test_skill_rules.py` 줄에 세 규칙이 모두 있음(`grep -c` → `1`), 모듈 docstring → `plan의 #37·#41·#46·#52·#53·#55·#56·#57,`. 통과

## 계획과 달라진 점
- TODO는 `plugins/plate/skills/plan/SKILL.md`만 적었지만, 옛 글을 그대로 찾던 `tests/test_skill_rules.py`의 `test_46_rerun_results_compared_by_body_hash`도 고쳤다. 고치지 않으면 완료 조건 2의 모든 테스트 통과가 깨진다

## 남은 것
- 이미 `docs/TOOLS.md`에 적힌 지난 장면 기록과 다른 스킬 본문에는 `HEAD`와 해시를 견주는 글이 없어 고치지 않았다. 고친 규칙대로 plan이 초안을 적는지는 돌려 보지 않았다(task 머리 완료 조건 1의 `- 돌리지 않음` 줄과 같은 까닭)

## 하네스에서 걸린 것
- 없음
