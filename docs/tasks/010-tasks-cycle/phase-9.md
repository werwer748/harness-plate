# Phase 9: 훅을 새 구조에 맞춘다

**목표**: 훅이 새 낱말로 막고, 없어진 `task/NNN-slug` 브랜치와 `.worktrees/` 규칙 없이 tasks 구조에서 돈다.

**테스트 먼저**: 예

**읽을 것**
- `plugins/plate/hooks/edit_guard.py` (지금의 훅)
- `tests/test_edit_guard.py` (지금의 훅 테스트. `test_task_branch_picks_its_task`, `test_non_code_files_pass`의 `.worktrees/` 줄)
- `plugins/plate/skills/plan/SKILL.md` (tasks 구조와 기록 파일)
- `plugins/plate/skills/run/SKILL.md` (브랜치 `tasks/<이름>`, `done-phase-N.md`)

**TODO**
- [ ] 남은 phase가 있는 task가 없을 때 막는 글이 새 낱말(task)을 쓴다는 테스트가 생기고, 훅의 글이 그렇게 바뀐다 (`tests/test_edit_guard.py`, `plugins/plate/hooks/edit_guard.py`)
- [ ] 브랜치와 상관없이 번호가 가장 작은 끝나지 않은 task를 지금 task로 본다는 테스트로 `test_task_branch_picks_its_task`가 바뀌고, 훅에서 `task/` 브랜치 규칙이 빠진다
- [ ] `.worktrees/` 아래 파일을 코드 파일에서 빼는 규칙이 빠지고 `test_non_code_files_pass`의 그 줄이 그에 맞게 바뀐다
- [ ] `done-phase-N.md`만 있는 task는 끝난 task로 본다는 테스트와 `docs/tasks/`의 파일(`plan.md`, `FRICTION.md`)이 task로 세어지지 않는다는 테스트가 더해진다. 지금 동작을 지키는 테스트라 처음부터 통과한다
- [ ] 훅의 모듈 설명과 주석이 새 낱말을 쓴다

**통과 조건**
- 완료 조건 9가 참이다
  - 확인: 완료 조건 9의 확인을 모두 돌린다
- 완료 조건 15가 참이다
  - 확인: `python3 -m unittest discover -s tests` → 마지막 줄 `OK`
- 완료 조건 2 가운데 훅의 몫이 참이다
  - 확인: `grep -n "작업" plugins/plate/hooks/edit_guard.py`의 줄을 모두 읽어 tasks, task, phase를 가리키는 "작업"이 없다
