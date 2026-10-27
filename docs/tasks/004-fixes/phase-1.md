# Phase 1: tasks 끝의 문제를 고친다

**목표**: task 머리의 완료 조건에 적힌 것을 모두 고친다.

**테스트 먼저**: 아니오 — 테스트 이름과 docstring만 바꾸고 코드의 동작은 바꾸지 않는다

**읽을 것**
- `docs/tasks/review.md`의 `## 평가 1` 절
- `docs/tasks/eval.md`의 `## eval 1` 절
- `tests/test_skill_rules.py`
- `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `docs/BACKLOG.md`

**TODO**
- [ ] retro 5번 "멈춤"의 `권한`을 보는 테스트가 `test_49_stop_list_includes_permission`으로 이름 붙고 모듈 docstring의 retro 목록에도 #50이 없어, tasks 머리가 #50의 해결로 적은 규칙의 시험을 이슈 번호로 찾을 수 없다 (`tests/test_skill_rules.py`)

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다
