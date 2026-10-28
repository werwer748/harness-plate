# Phase 1: tasks 끝의 문제를 고친다

**목표**: task 머리의 완료 조건에 적힌 것을 모두 고친다.

**테스트 먼저**: 아니오 — 고칠 것이 스킬 본문(`.md`) 하나뿐이고 코드 파일의 동작을 바꾸지 않는다

**읽을 것**
- `docs/tasks/review.md`의 `## 평가 1` 절
- `docs/tasks/eval.md`의 `## eval 1` 절
- `plugins/plate/skills/plan/SKILL.md`
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/ADR.md`
- `docs/TOOLS.md`
- `docs/BACKLOG.md`

**TODO**
- [ ] 작업 트리를 얻는 예로 든 `git stash create`는 추적하지 않는 새 파일을 넣지 않고 새 파일만 바뀌었으면 아무것도 내지 않아, 새 파일을 만드는 phase의 통과 조건이 이 예를 따르면 그 파일이 없는 트리를 본다. 예를 `cp -R` 사본으로 줄이거나 새 파일이 빠진다는 단서를 단다 (`plugins/plate/skills/plan/SKILL.md:249`)

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다
