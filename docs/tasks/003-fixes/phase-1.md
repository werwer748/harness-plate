# Phase 1: tasks 끝의 문제를 고친다

**목표**: task 머리의 완료 조건에 적힌 것을 모두 고친다.

**테스트 먼저**: 아니오 — 고칠 것은 결과물인 마크다운(plan·run 본문)의 동작을 헤드리스로 돌려 보는 확인이고, 코드 파일의 동작을 바꾸지 않는다

**읽을 것**
- `docs/tasks/review.md`의 `## 평가 1` 절
- `docs/tasks/eval.md`의 `## eval 1` 절
- `plugins/plate/skills/plan/SKILL.md`
- `plugins/plate/skills/run/SKILL.md`
- `tests/test_skill_rules.py`
- `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `docs/BACKLOG.md`, `docs/cleanup/`

**TODO**
- [ ] plan 6번·**조건**의 세 경우 규칙과 run 8번의 고칠 쪽 계획에서의 멈춤에 돌려 보는 확인이 없고, grep·단위 시험과 `돌리지 않음` 줄만 있다. 헤드리스 시험으로 두 규칙을 돌려 결과를 기록에 남기고, 고칠 동작을 적은 맥락 문서의 줄과 그 글을 지키는 테스트도 맞춘다 (`plugins/plate/skills/plan/SKILL.md`, `plugins/plate/skills/run/SKILL.md`, `docs/TOOLS.md`, `tests/test_skill_rules.py`)

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다
