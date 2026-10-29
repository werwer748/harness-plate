# Phase 1: tasks 끝의 문제를 고친다

**목표**: task 머리의 완료 조건에 적힌 것을 모두 고친다.

**테스트 먼저**: 아니오 — 고칠 것이 모두 `.md`(스킬 본문, 지침 파일, 맥락 문서)다

**읽을 것**
- `docs/tasks/review.md`의 `## 평가 1` 절
- `docs/tasks/eval.md`의 `## eval 1` 절
- `plugins/plate/skills/run/SKILL.md` ("보고하고 묻는다")
- `AGENTS.md` (작업 규칙)
- `tests/test_skill_rules.py` (`RunRulesTest.test_eval_only_goes_nowhere`)
- `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `docs/BACKLOG.md` (맥락 문서)

**TODO**
- [ ] run의 "보고하고 묻는다"가 "eval에만" 갈래를 끝까지 다룬다: 고칠 안이 모두 비는 경우(하네스 고칠 거리가 모두 eval에만이나 감수이고 소스 문제가 없을 때)와, 사용자가 eval에만인 것을 고치거나 올리자고 할 때 어디로 옮기는지를 적는다. 그 동작을 적은 ARCHITECTURE의 tasks 끝 줄과 그 글을 지키는 테스트도 맞춘다 (`plugins/plate/skills/run/SKILL.md`, `docs/ARCHITECTURE.md`, `tests/test_skill_rules.py`)
- [ ] 작업 규칙의 스킬 본문 tasks 줄 곁에, 헤드리스 시험을 두는 phase의 저장소 불변 확인은 `docs/tasks/RUNLOG.md`와 그 phase가 고치는 파일을 빼거나 phase 커밋 뒤에 돌린다고 통과 조건에 적는다는 줄이 더해진다 (`AGENTS.md`)
- [ ] "세션 도중의 스킬 본문 고침" 절에, 헤드리스 시험의 완료 조건을 본문 해시로 볼 때 그 본문을 뒤에서 고치는 phase(회고 뒤 더한 phase도)는 시험을 다시 돌려 새 해시를 기록에 남기고, 계획은 이것을 그 완료 조건 곁에 적는다는 줄이 더해진다 (`docs/TOOLS.md`)

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다
