# 회고

## 회고 1

**확인**
- 1. plan 본문에 세 이슈의 해결이 제자리에 있다
  - `tests/test_skill_rules.py`의 `section`·`part`로 `plugins/plate/skills/plan/SKILL.md`의 "6. 초안을 보여 주고 승인받는다", 적는 규칙 "조건", "결정"을 뽑아 여섯 글(조건: `phase의 통과 조건은 커밋 전의 작업 트리에서 돈다`, `지울 글을 본문에 있는 그대로 인용하고`, `실패할 테스트 이름을 기대로 적는다` / 결정: `앞 task가 바꿀 글을 인용하면 바뀐 뒤의 글 그대로 적고` / 6번: `수행이 돌릴 확인에 \`HEAD\`가 있는지 본다`, `task 사이에 같은 글을 바꾸거나 인용하는 곳이 맞물리는지 본다`)을 찾음 → `True True True True True True`. 조건 절 249줄에 `HEAD`를 풀거나 보는 확인은 작업 트리(`cp -R` 사본, `git stash create`)로 적고 원본 확인은 그 phase의 `phase-N.md`를 빼고 본다는 글도 있음 → `True`. 통과
- 2. 고친 규칙마다 글이 빠지면 실패하는 테스트가 있고, 모든 테스트가 통과한다
  - `python3 -m unittest discover -s tests` → `Ran 164 tests in 16.170s` / `OK`. 통과
  - `mktemp -d` 사본에 `cp -R plugins tests`, `phase의 통과 조건은 커밋 전의 작업 트리에서 돈다` → `count: 1`, 빈 글로 바꾼 뒤 사본에서 테스트 → `FAIL: test_55_checks_run_on_uncommitted_worktree (test_skill_rules.PlanRulesTest)` / `FAILED (failures=1)`. 통과
  - 새 사본, `지울 글을 본문에 있는 그대로 인용하고` → `count: 1`, `FAIL: test_56_mutation_checks_quote_text_and_name_test (test_skill_rules.PlanRulesTest)` / `FAILED (failures=1)`. 통과
  - 새 사본, `앞 task가 바꿀 글을 인용하면 바뀐 뒤의 글 그대로 적고` → `count: 1`, `FAIL: test_57_quote_earlier_task_text_as_changed (test_skill_rules.PlanRulesTest)` / `FAILED (failures=1)`. 통과
- 3. 두 매니페스트의 버전이 0.19.0이고, 마켓플레이스가 유효하고, 테스트의 설명 글이 더한 규칙과 맞는다
  - `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → `"version": "0.19.0",` 두 줄. 통과
  - `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
  - `docs/ARCHITECTURE.md`의 `test_skill_rules.py` 줄에서 "통과 조건은 커밋 전 작업 트리에서 돎", "지울 글 인용과 실패할 테스트 이름", "앞 task가 바꿀 글을 바뀐 뒤 꼴로 인용"을 찾음 → 셋 다 있음. `tests/test_skill_rules.py` 모듈 docstring → `plan의 #37·#41·#46·#52·#53·#55·#56·#57`. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 164 tests` / `OK`. 통과

**남은 것**
- phase 1: 6번에 더한 #55 점검 항목이 이웃 항목들처럼 "초안을 보여 주기 전에"로 시작하지 않는다 → 문제 아님 (TODO가 정한 글 그대로이고 뜻은 같은 목록 안에서 읽힌다. 문체의 일이라 넷 가운데 어디에도 걸리지 않는다)
- phase 1: 고친 규칙대로 plan이 초안을 적는지는 돌려 보지 않았다 → 문제 아님 (task 머리와 tasks 머리 완료 조건 1의 `- 돌리지 않음` 줄과 범위 밖이 돌리지 않기로 정한 동작이다)

**문제**
- plan 본문 안에서 이번에 더한 규칙과 그 위의 규칙이 서로 다른 것을 시킨다. 적는 규칙 "조건" 248줄(이번 task 전부터 있던 줄)은 돌려 본 결과가 지금 본문의 것인지를 "돌릴 때 적은 본문 해시(`git hash-object <경로>`)와 `git rev-parse HEAD:<경로>`로 견준다"고 `HEAD`를 보는 꼴을 시키는데, 이번에 더한 249줄은 "`HEAD`를 풀거나 보는 확인은 작업 트리…로 적고"라 하고 6번 102줄은 "수행이 돌릴 확인에 `HEAD`가 있는지 본다(예: … `HEAD`의 파일과 견준다)… 있으면 작업 트리로 보는 확인으로 고친다"라 해, 248줄대로 적은 확인을 6번이 고치라고 한다. 어느 쪽이 맞는지(248줄의 `HEAD:<경로>`가 예외인지, 작업 트리의 `git hash-object`로 바꿀지)가 본문에 없어 plan이 둘 가운데 하나를 묻지 않고 고른다 (`plugins/plate/skills/plan/SKILL.md`). 기준: 결함

**판정**: 문제 있음
