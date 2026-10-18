# Phase 9: 훅을 새 구조에 맞춘다

**목표**: 훅이 새 낱말로 막고, 없어진 `task/NNN-slug` 브랜치와 `.worktrees/` 규칙 없이 tasks 구조에서 돈다.

**테스트 먼저**: 예

**읽을 것**
- `plugins/plate/hooks/edit_guard.py` (지금의 훅)
- `tests/test_edit_guard.py` (지금의 훅 테스트. `test_task_branch_picks_its_task`, `test_non_code_files_pass`의 `.worktrees/` 줄)
- `plugins/plate/skills/plan/SKILL.md` (tasks 구조와 기록 파일)
- `plugins/plate/skills/run/SKILL.md` (브랜치 `tasks/<이름>`, `done-phase-N.md`)

**TODO**
- [x] 남은 phase가 있는 task가 없을 때 막는 글이 새 낱말(task)을 쓴다는 테스트가 생기고, 훅의 글이 그렇게 바뀐다 (`tests/test_edit_guard.py`, `plugins/plate/hooks/edit_guard.py`)
- [x] 브랜치와 상관없이 번호가 가장 작은 끝나지 않은 task를 지금 task로 본다는 테스트로 `test_task_branch_picks_its_task`가 바뀌고, 훅에서 `task/` 브랜치 규칙이 빠진다
- [x] `.worktrees/` 아래 파일을 코드 파일에서 빼는 규칙이 빠지고 `test_non_code_files_pass`의 그 줄이 그에 맞게 바뀐다
- [x] `done-phase-N.md`만 있는 task는 끝난 task로 본다는 테스트와 `docs/tasks/`의 파일(`plan.md`, `FRICTION.md`)이 task로 세어지지 않는다는 테스트가 더해진다. 지금 동작을 지키는 테스트라 처음부터 통과한다
- [x] 훅의 모듈 설명과 주석이 새 낱말을 쓴다

**통과 조건**
- 완료 조건 9가 참이다
  - 확인: 완료 조건 9의 확인을 모두 돌린다
- 완료 조건 15가 참이다
  - 확인: `python3 -m unittest discover -s tests` → 마지막 줄 `OK`
- 완료 조건 2 가운데 훅의 몫이 참이다
  - 확인: `grep -n "작업" plugins/plate/hooks/edit_guard.py`의 줄을 모두 읽어 tasks, task, phase를 가리키는 "작업"이 없다

## 한 일
- 남은 phase가 있는 task가 없을 때 막는 글이 새 낱말(task)을 쓴다는 테스트가 생기고, 훅의 글이 그렇게 바뀐다: `test_plan_first_message_says_task`를 더해 막는 글에 "남은 phase가 있는 task가 없어서"가 있고 "작업"이 없는지 보고, 훅의 `PLAN_FIRST` 글을 "남은 phase가 있는 task가 없어서"로 바꿨다 (`tests/test_edit_guard.py`, `plugins/plate/hooks/edit_guard.py`)
- 브랜치와 상관없이 번호가 가장 작은 끝나지 않은 task를 지금 task로 본다는 테스트로 `test_task_branch_picks_its_task`가 바뀌고, 훅에서 `task/` 브랜치 규칙이 빠진다: 테스트 이름을 `test_branch_does_not_pick_task`로 바꾸고, `task/002-b`와 `tasks/x` 브랜치에서도 번호가 작은 001-a(테스트 먼저 아니오)가 지금 task라 통과하고, 더 작은 000-z(예)를 더하면 그것으로 막는지 본다. 훅의 `current_task`에서 브랜치를 읽는 줄을 빼고 인자를 `tasks` 하나로 줄였다 (`tests/test_edit_guard.py`, `plugins/plate/hooks/edit_guard.py`)
- `.worktrees/` 아래 파일을 코드 파일에서 빼는 규칙이 빠지고 `test_non_code_files_pass`의 그 줄이 그에 맞게 바뀐다: `is_code_file`에서 `.worktrees` 조건을 뺐고, 테스트의 그 줄을 `.worktrees/009-x/src/app.py`가 계획부터로 막힌다는 `assertBlocked`로 바꿨다 (`plugins/plate/hooks/edit_guard.py`, `tests/test_edit_guard.py`)
- `done-phase-N.md`만 있는 task는 끝난 task로 본다는 테스트와 `docs/tasks/`의 파일(`plan.md`, `FRICTION.md`)이 task로 세어지지 않는다는 테스트가 더해진다: `test_done_phase_only_task_is_finished`(done-phase-1.md, done-phase-2.md, retro.md만 있는 task → 계획부터로 막힘)와 `test_tasks_files_are_not_tasks`(`docs/tasks/`에 plan.md, FRICTION.md, RUNLOG.md만 있으면 계획부터로 막히고, 001-a를 더하면 001-a로 테스트 먼저가 막음)를 더했다. 계획대로 처음부터 통과했다 (`tests/test_edit_guard.py`)
- 훅의 모듈 설명과 주석이 새 낱말을 쓴다: 모듈 설명의 "남은 phase가 있는 작업"을 "task"로, `unfinished_tasks` 설명을 "끝나지 않은 task … `done-phase-N.md`만 있는 task는 끝난 task다"로, `current_task` 설명을 "끝나지 않은 task 가운데 번호가 가장 작은 것"으로 바꿨다. 23줄의 "작업 트리"는 git의 working tree라 그대로 뒀다 (`plugins/plate/hooks/edit_guard.py`)
- 테스트 먼저
  - 실패: `python3 -m unittest discover -s tests 2>&1 | grep -E "^(FAIL|ERROR|Ran|OK|FAILED)"` → `FAIL: test_branch_does_not_pick_task (test_edit_guard.CurrentPhaseTest.test_branch_does_not_pick_task) (branch='task/002-b')`, `FAIL: test_plan_first_message_says_task (test_edit_guard.PlanFirstTest.test_plan_first_message_says_task)`, `FAIL: test_non_code_files_pass (test_edit_guard.SetupAndCodeFileTest.test_non_code_files_pass)`, `Ran 39 tests in 14.802s`, `FAILED (failures=3)`
  - 통과: `python3 -m unittest discover -s tests 2>&1 | grep -E "^(FAIL|ERROR|Ran|OK|FAILED)"` → `Ran 39 tests in 13.471s`, `OK`

## 확인 결과
- 완료 조건 9가 참이다
  - `python3 -m unittest discover -s tests 2>&1 | tail -1` → `OK`. 통과
  - `grep -n 'task/\|\.worktrees' plugins/plate/hooks/edit_guard.py` → 출력 없음(종료 코드 1), 0줄. 통과
  - `grep -c 'done-phase' tests/test_edit_guard.py` → `3`. 통과
- 완료 조건 15가 참이다
  - `python3 -m unittest discover -s tests` → `Ran 39 tests`, 마지막 줄 `OK`. 통과
- 완료 조건 2 가운데 훅의 몫이 참이다
  - `grep -n "작업" plugins/plate/hooks/edit_guard.py` → `23:COUNT_FILE = "plate-test-first.json"  # git 폴더 안에 둔다. 작업 트리에 변경을 만들지 않는다` 한 줄. "작업 트리"는 git의 working tree를 가리키고 tasks, task, phase를 가리키지 않는다. 통과

## 계획과 달라진 점
- 없음

## 남은 것
- 없음

## 하네스에서 걸린 것
- 수행 스킬 2번은 "처음부터 통과하면 바뀔 동작을 보지 못하는 테스트이니 실패하게 고친다"고 하지만, TODO 4의 두 테스트는 계획이 "지금 동작을 지키는 테스트라 처음부터 통과한다"고 적었다. 바뀔 동작의 테스트가 아니라서 실패하게 고치지 않고 계획대로 두었다. 실패 출력은 바뀔 동작의 세 테스트로 남겼다
