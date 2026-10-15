# Phase 8: ADR을 정리하고 4단계를 닫는다

**목표**: `docs/ADR.md`에 프로젝트 수준의 결정만 남고 그것을 가리키는 곳이 맞으며, 4단계의 결과가 보고돼 있다.

**읽을 것**
- `docs/ADR.md` (33항목과 첫머리의 원장 설명)
- `plugins/plate/skills/context/SKILL.md` ("ADR 항목" 절의 다섯 범주)
- `docs/ARCHITECTURE.md`, `docs/PRD.md`, `docs/TOOLS.md`, `README.md`, `docs/tasks/004-context-rules/plan.md` (ADR 번호를 가리키는 곳)

**TODO**
- [x] 33항목마다 무엇에 대한 결정인지와 남길지의 추천을 적은 표가 사용자에게 보여지고, 승인받은 것만 남는다. 번호는 다시 매기지 않는다 (`docs/ADR.md`)
- [x] 남은 항목에 "원장" 줄이 없고 첫머리에 원장 설명이 없다 (`docs/ADR.md`)
- [x] 남은 항목의 글 가운데 4단계에서 바뀐 것(통과한 phase에서 지우는 것, 끝나지 않은 작업의 기준, 회고를 거절했을 때, 브랜치와 worktree)이 지금 상태로 고쳐진다. 고칠 문장은 표와 함께 보여 주고 승인받는다 (`docs/ADR.md`)
- [x] 4단계에서 정한 것 가운데 다섯 범주에 드는 것이 있으면 ADR 후보로 보여 주고 승인받은 것만 항목으로 더해진다. 계획을 쓸 때는 없다고 봤다 (`docs/ADR.md`)
- [x] 지운 번호를 가리키던 곳이 고쳐진다 (`docs/ARCHITECTURE.md`, `docs/PRD.md`, `docs/TOOLS.md`, `README.md`, `docs/tasks/004-context-rules/plan.md`)
- [ ] 4단계의 결과를 보고하고 둘을 따로 확인받는다: `run`을 `main`에 병합하고 푸시할지, 5단계(검증) 질문 라운드를 열지

**통과 조건**
- 완료 조건 20이 참이다.
  - 확인: 완료 조건 20의 확인 둘을 돌려 기대와 같은지 본다
- 사용자가 표를 승인했고 보고를 받았다.
  - 확인: 표와 보고를 적은 답글에 받은 답

## 한 일
- ADR 33항목의 표(무엇에 대한 결정, 다섯 범주에 드는지, 추천, 지워도 내용이 남는 곳)를 사용자에게 보였고 사용자가 표대로 승인했다. 004, 005, 018을 남기고 30항목을 지웠다. 번호는 다시 매기지 않았다(`docs/ADR.md`).
- 남은 셋에서 "원장" 줄을, 첫머리에서 원장 설명 문단을 지웠다.
- 4단계에서 바뀐 글(통과한 phase 지우기, 끝나지 않은 작업의 기준, 회고 거절, 브랜치와 worktree)은 022, 025, 026에 있었고 남은 셋에는 없어 고친 문장이 없다.
- ADR 후보는 없다. 4단계에서 정한 것은 스킬의 동작이고 다섯 범주에서 새로 고른 것이 없다.
- 지운 번호를 가리키던 곳을 고쳤다. 괄호 속 번호만 지운 줄이 20(`docs/PRD.md` 7, `docs/ARCHITECTURE.md` 5, `docs/TOOLS.md` 4, `docs/tasks/004-context-rules/plan.md` 4), 글을 바꾼 곳이 5(`docs/TOOLS.md`의 시험 폴더 위치, 004 계획의 세 줄, `docs/LESSONS.md`에서 ADR-013과 스킬 본문의 갈림을 적은 줄 지움)다.

## 확인 결과
- 완료 조건 20
  - `grep -c '^- \*\*원장\*\*' docs/ADR.md` → 0. 통과
  - 지운 번호 30개마다 `grep -rn 'ADR-0NN' README.md docs/PRD.md docs/ARCHITECTURE.md docs/TOOLS.md docs/ADR.md docs/tasks/004-context-rules plugins/` → 001만 `plugins/plate/skills/setup/SKILL.md:194:### ADR-001: {결정 사항 (예: Next.js App Router 선택)}` 한 줄이 나오고 나머지는 출력 없음. 그 줄은 setup이 넣는 ADR 양식의 첫 항목 제목이라 이 레포의 ADR-001을 가리키지 않는다. 표와 함께 사용자에게 알렸다. 그 한 줄을 빼고 통과
  - `grep -n 'ADR-0' docs/LESSONS.md` → 출력 없음
- 사용자가 표를 승인했다. 보고는 이 기록을 커밋한 뒤의 답글에서 한다.

## 계획과 달라진 점
- 읽을 것과 TODO의 파일 목록에 없던 `docs/LESSONS.md`의 줄 하나를 지웠다. 표와 함께 승인받았다.

## 남은 것
- 4단계의 결과 보고와 두 확인(`run`을 `main`에 병합하고 푸시할지, 5단계 질문 라운드를 열지). 이 기록을 커밋한 뒤의 답글에서 한다.

## 하네스에서 걸린 것
- 완료 조건 20의 둘째 확인은 `plugins/`까지 보는데 setup의 ADR 양식에 `ADR-001`이 들어 있어, 001을 지우면 늘 한 줄이 나온다. 계획에 적는 확인 명령은 미리 돌려 보지 않는다는 규칙대로 적어서 계획을 쓸 때 잡히지 않았다.
- context 스킬의 "ADR 번호는 있는 번호 뒤에 잇는다"를 따르면 다음 항목은 ADR-019가 되어, 단계 기록(`docs/tasks/002-context`, `003-plan`, `005-run`)과 git 이력 속의 옛 ADR-019와 번호가 겹친다.
