# Phase 8: ADR을 정리하고 4단계를 닫는다

**목표**: `docs/ADR.md`에 프로젝트 수준의 결정만 남고 그것을 가리키는 곳이 맞으며, 4단계의 결과가 보고돼 있다.

**읽을 것**
- `docs/ADR.md` (33항목과 첫머리의 원장 설명)
- `plugins/plate/skills/context/SKILL.md` ("ADR 항목" 절의 다섯 범주)
- `docs/ARCHITECTURE.md`, `docs/PRD.md`, `docs/TOOLS.md`, `README.md`, `docs/tasks/004-context-rules/plan.md` (ADR 번호를 가리키는 곳)

**TODO**
- [ ] 33항목마다 무엇에 대한 결정인지와 남길지의 추천을 적은 표가 사용자에게 보여지고, 승인받은 것만 남는다. 번호는 다시 매기지 않는다 (`docs/ADR.md`)
- [ ] 남은 항목에 "원장" 줄이 없고 첫머리에 원장 설명이 없다 (`docs/ADR.md`)
- [ ] 남은 항목의 글 가운데 4단계에서 바뀐 것(통과한 phase에서 지우는 것, 끝나지 않은 작업의 기준, 회고를 거절했을 때, 브랜치와 worktree)이 지금 상태로 고쳐진다. 고칠 문장은 표와 함께 보여 주고 승인받는다 (`docs/ADR.md`)
- [ ] 4단계에서 정한 것 가운데 다섯 범주에 드는 것이 있으면 ADR 후보로 보여 주고 승인받은 것만 항목으로 더해진다. 계획을 쓸 때는 없다고 봤다 (`docs/ADR.md`)
- [ ] 지운 번호를 가리키던 곳이 고쳐진다 (`docs/ARCHITECTURE.md`, `docs/PRD.md`, `docs/TOOLS.md`, `README.md`, `docs/tasks/004-context-rules/plan.md`)
- [ ] 4단계의 결과를 보고하고 둘을 따로 확인받는다: `run`을 `main`에 병합하고 푸시할지, 5단계(검증) 질문 라운드를 열지

**통과 조건**
- 완료 조건 20이 참이다.
  - 확인: 완료 조건 20의 확인 둘을 돌려 기대와 같은지 본다
- 사용자가 표를 승인했고 보고를 받았다.
  - 확인: 표와 보고를 적은 답글에 받은 답
