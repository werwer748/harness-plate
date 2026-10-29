# Phase 2: 회고 1의 문제를 고친다

**목표**: 회고 1에서 나온 문제를 모두 고친다.

**테스트 먼저**: 아니오 — 고칠 것이 모두 `.md`(스킬 본문, 맥락 문서)다

**읽을 것**
- `docs/tasks/003-fixes/retro.md`의 `## 회고 1` 절
- `docs/ADR.md` (ADR-026의 결정)
- `docs/PRD.md` (핵심 기능 8번)
- `plugins/plate/skills/run/SKILL.md` ("보고하고 묻는다"의 "고칠 곳을 말하면" 줄과 "아무것도 고치지 않고 올리지 않겠다고 하면" 줄)
- `tests/test_skill_rules.py` (`RunRulesTest`에서 "고침 task에서 뺀 소스 문제와 이 프로젝트만의 하네스 고칠 거리는 BACKLOG로 미룰 것으로 옮긴다"와 "고침 task에 두었던 이 프로젝트만의 하네스 고칠 거리도 BACKLOG로 미룰 것에 둔다"를 보는 테스트)
- `docs/ARCHITECTURE.md`, `docs/TOOLS.md`, `docs/BACKLOG.md` (맥락 문서)

**TODO**
- [ ] ADR-026 결정과 PRD 8번이 run의 "보고하고 묻는다"와 `docs/ARCHITECTURE.md` 78줄에 더해진 두 동작(사용자가 고치거나 올리자고 하면 eval에만인 것을 갈래대로 옮긴다, 고칠 안이 모두 비면 묻지 않는다)을 적지 않아 "어디에도 두지 않는다"로 남는다. 두 문서의 그 줄이 고친 동작과 맞게 한다 (`docs/ADR.md`, `docs/PRD.md`)
- [ ] 사용자가 고침 task나 이슈로 올릴 것으로 옮긴 eval에만인 하네스 고칠 거리를 다시 빼거나 "아무것도 고치지 않겠다"고 하면, run "보고하고 묻는다"의 "뺀 것은 BACKLOG로 미룰 것으로 옮긴다"와 "고침 task에 두었던 이 프로젝트만의 하네스 고칠 거리도 BACKLOG로 미룰 것에 둔다"에 걸려 기준이 eval에만인 것이 BACKLOG로 간다. 기준이 eval에만인 것은 빼면 eval에만으로 돌아가게 한다. 그 동작을 적은 `docs/ARCHITECTURE.md`의 tasks 끝 줄과, 위 두 글을 지키는 테스트가 고친 글을 지키게 한다 (`plugins/plate/skills/run/SKILL.md`, `docs/ARCHITECTURE.md`, `tests/test_skill_rules.py`)

**통과 조건**
- 회고 1의 문제가 모두 고쳐졌다.
  - 확인: TODO에 넣은 문제마다 적힌 곳(ADR-026 결정, PRD 8번, run "보고하고 묻는다"의 두 줄)과 그 동작을 적은 `docs/ARCHITECTURE.md`의 tasks 끝 줄을 다시 읽고, 걸린 테스트(`python3 -m unittest discover -s tests`)를 돌린다
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다
