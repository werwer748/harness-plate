# Phase 2: 회고 1의 문제를 고친다

**목표**: 회고 1에서 나온 문제를 모두 고친다.

**테스트 먼저**: 아니오 — 고칠 것이 `plugins/plate/skills/run/SKILL.md`(.md)의 글뿐이다

**읽을 것**
- `docs/tasks/002-fixes/retro.md`의 `## 회고 1`부터 `## 회고 1`까지의 절
- `plugins/plate/skills/run/SKILL.md`
- `tests/test_skill_rules.py`
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/ADR.md`
- `docs/TOOLS.md`
- `docs/BACKLOG.md`

**TODO**
- [ ] run "BACKLOG를 고친다"에 고침 task가 고치기로 한 이 프로젝트만의 하네스 고칠 거리와 같은 뜻의 하네스 고칠 거리 절 항목을 지우는 줄이 없다(소스 문제의 `고치기로 한 소스 문제와 같은 뜻의 항목은 지운다`에 맞먹는 것). 이 task가 그 항목이 BACKLOG에 드는 길을 열어, 그런 항목이 다시 나와 고침 task로 가면 "그 밖의 항목"으로 다시 나오지 않은 tasks에 세어지고 고친 뒤에도 셋이 될 때까지 미룬 것으로 남는다. 그 줄을 더하고, 그 글을 지키는 테스트도 맞춘다 (`plugins/plate/skills/run/SKILL.md`, `tests/test_skill_rules.py`)

**통과 조건**
- 회고 1의 문제가 모두 고쳐졌다.
  - 확인: TODO에 넣은 문제마다 적힌 곳과 그 동작을 적은 맥락 문서와 README의 줄을 다시 읽거나 돌리고, 걸린 테스트를 돌린다
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다
