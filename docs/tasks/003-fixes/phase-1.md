# Phase 1: tasks 끝의 문제를 고친다

**목표**: task 머리의 완료 조건에 적힌 것을 모두 고친다.

**테스트 먼저**: 아니오 — 고칠 동작은 `.md`인 스킬 본문(cleanup)이고, 더하는 테스트는 그 본문을 지키는 시험이라 코드 파일의 동작을 바꾸지 않는다.

**읽을 것**
- `docs/tasks/review.md`의 `## 평가 1` 절
- `docs/tasks/eval.md`의 `## eval 1` 절
- `plugins/plate/skills/cleanup/SKILL.md`
- `plugins/plate/skills/run/SKILL.md`
- `plugins/plate/skills/plan/SKILL.md`
- `plugins/plate/skills/retro/SKILL.md`
- `README.md`
- `tests/test_cleanup_skill.py`
- `tests/test_skill_rules.py`
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/ADR.md`
- `docs/TOOLS.md`
- `docs/BACKLOG.md`
- `docs/cleanup/`

**TODO**
- [ ] 보고서 경로를 작업 트리의 `docs/cleanup/`만 보고 정해 합쳐지지 않은 같은 날의 cleanup 브랜치와 파일 이름이 겹치고 지난 보고서 읽기가 그 보고서를 놓친다. 고친 동작을 적은 맥락 문서와 README의 줄과 그 글을 지키는 테스트도 맞춘다 (`plugins/plate/skills/cleanup/SKILL.md`, `docs/PRD.md`, `docs/ARCHITECTURE.md`, `README.md`, `tests/test_cleanup_skill.py`)
- [ ] cleanup의 "기본 브랜치"·"GitHub 원격" 정의가 run과 같은지, plan과 cleanup의 "cleanup 브랜치" 정의가 어긋나지 않는지 지키는 시험을 둔다 (`tests/test_cleanup_skill.py`, `tests/test_skill_rules.py`)
- [ ] cleanup "고른 발견이 없을 때"의 합침 갈래와 run "보낼 곳으로 합친다"의 충돌 뒤 되돌림을 시험 레포에서 돌려 보고, #80의 retro 규칙을 헤드리스 시험으로 돌려 본다 (`tests/test_cleanup_skill.py`, `tests/test_skill_rules.py`)

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다
