# Phase 1: tasks 끝의 문제를 고친다

**목표**: task 머리의 완료 조건에 적힌 것을 모두 고친다.

**테스트 먼저**: 아니오 — `AGENTS.md`와 `docs/TOOLS.md`의 `.md`만 고친다

**읽을 것**
- `docs/tasks/review.md`의 `## 평가 1` 절
- `docs/tasks/eval.md`의 `## eval 1` 절
- `AGENTS.md`
- `docs/TOOLS.md`
- `plugins/plate/skills/run/SKILL.md`의 낱말 "작업 트리의 스킬 줄"
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/ADR.md`
- `docs/BACKLOG.md`
- `docs/cleanup/`

**TODO**
- [ ] 스킬 본문을 고치는 tasks에서 수행·확인은 run이 넘긴 판의 본문을 따르고 고친 본문의 동작은 헤드리스 시험으로 본다는 규칙을 `AGENTS.md` 작업 규칙에 한 줄 더하고, 그 까닭(run의 작업 트리의 스킬 줄 때문에 한 phase 안에서도 수행과 확인의 판이 갈릴 수 있다)을 `docs/TOOLS.md`에 적는다 (`AGENTS.md`, `docs/TOOLS.md`)
- [ ] zsh에서 `=`로 시작하는 낱말이 확장되어 `echo ====`가 `not found`를 내니 구분 줄은 `echo '----'`처럼 쓴다는 것을 `docs/TOOLS.md`에 "셸의 `=` 확장"으로 적는다 (`docs/TOOLS.md`)

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다
