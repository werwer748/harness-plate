# Phase 1: tasks 끝의 문제를 고친다

**목표**: task 머리의 완료 조건에 적힌 것을 모두 고친다.

**테스트 먼저**: 아니오 — 고칠 것이 모두 `plugins/plate/skills/run/SKILL.md`(.md)의 글이다

**읽을 것**
- `docs/tasks/review.md`의 `## 평가 1` 절
- `docs/tasks/eval.md`의 `## eval 1` 절
- `plugins/plate/skills/run/SKILL.md`
- `tests/test_skill_rules.py`
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/ADR.md`
- `docs/TOOLS.md`
- `docs/BACKLOG.md`

**TODO**
- [ ] 고침 task에서 뺀(또는 아무것도 고치지 않기로 한) 이 프로젝트만의 하네스 고칠 거리를 BACKLOG로 미룰 것으로 옮기는 길을 더한다. 그 동작을 적은 맥락 문서의 줄과 그 글을 지키는 테스트도 맞춘다 (`plugins/plate/skills/run/SKILL.md`, `docs/ARCHITECTURE.md`, `tests/test_skill_rules.py`)
- [ ] 처음 안에서 문턱을 넘었고 처리가 감수인 plate 자체의 고칠 거리가 어느 쪽으로 가는지(감수가 먼저) 적는다. 그 글을 지키는 테스트도 맞춘다 (`plugins/plate/skills/run/SKILL.md`, `tests/test_skill_rules.py`)

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다
