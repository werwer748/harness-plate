# Phase 1: tasks 끝의 문제를 고친다

**목표**: task 머리의 완료 조건에 적힌 것을 모두 고친다.

**테스트 먼저**: 아니오 — `.md`와 `.gitignore`만 고쳐 테스트가 보는 코드의 동작이 바뀌지 않는다

**읽을 것**
- `docs/tasks/review.md`의 `## 평가 1` 절
- `docs/tasks/eval.md`의 `## eval 1` 절
- `plugins/plate/skills/run/SKILL.md`
- `.gitignore`
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/ADR.md`
- `docs/TOOLS.md`

**TODO**
- [ ] 작업 트리의 스킬 줄을 붙인 맡기는 글이 세션의 스킬과 작업 트리의 `SKILL.md`를 둘 다 "그 절차를 따른다"로 가리키고, 둘이 다를 때 작업 트리 쪽을 따르라는 말이 띄운 에이전트가 받는 글에 없다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] 로컬 설정 파일 `.claude/settings.local.json`이 커밋하지 않은 변경으로 잡혀 실행마다 묻게 된다. `.gitignore`에 그 파일을 더한다 (`.gitignore`)

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다
