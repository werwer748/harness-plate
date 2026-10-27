<!-- plate:docs-map:start -->
## 문서 지도
하네스 기록(프로젝트 맥락 문서와 tasks 기록)은 모두 `docs/` 아래 이 표의 위치에 둔다. README, CHANGELOG 같은 일반 문서는 이 규칙의 대상이 아니다.
표에 없는 종류의 기록이 필요하면 만들기 전에 위치를 사용자에게 묻고, 정한 위치를 이 표에 한 행으로 더한 뒤 만든다. 하네스의 스킬이 위치를 정해 둔 기록은 묻지 않고 그 스킬이 행을 더한다.

| 위치 | 내용 | 읽을 때 |
|---|---|---|
| `docs/PRD.md` | 무엇을 왜 만드는지, 범위 밖 | 기능을 더하거나 범위를 판단할 때 |
| `docs/ARCHITECTURE.md` | 기술 스택, 구조, 데이터 흐름 | 파일 위치나 모듈 경계를 판단할 때 |
| `docs/ADR.md` | 이미 내린 결정과 이유 | 기술 선택을 바꾸거나 새로 할 때 |
| `docs/TOOLS.md` | 도구별로 확인해 둔 사실과 확인을 멈춘 지점 | 다른 도구로 넓히거나 도구마다 다른 동작을 판단할 때 |
| `docs/BACKLOG.md` | 미룬 소스 문제와 그것이 나온 tasks | tasks를 계획하거나 tasks 끝에서 고칠지 정할 때 |
| `docs/tasks/` | 진행 중인 tasks 하나의 기록: tasks 머리 `plan.md`, `FRICTION.md`, `RUNLOG.md`, `review.md`, `eval.md`, task 폴더 `NNN-slug/`마다 task 머리 `plan.md`, `phase-N.md`(통과하면 `done-phase-N.md`), `retro.md`. tasks가 끝나면 비운다 | 그 tasks를 이어 가거나 근거를 볼 때 |
<!-- plate:docs-map:end -->

<!-- plate:rules:start -->
## 작업 규칙
- 계획 없이 코드를 고치지 않는다. 기능을 만들거나 코드를 고치는 요청을 받으면 plate의 plan 스킬(`plate:plan`)로 계획부터 세운다.
- task는 task 회고가 통과해야 끝난다. 회고는 plate의 retro 스킬(`plate:retro`)이 하고, 회고가 통과하기 전에는 그 task가 끝났다고 말하지 않는다.
- tasks는 끝의 평가와 보고까지 가야 끝난다. 모든 task가 끝나면 plate의 review 스킬(`plate:review`)이 코드를, eval 스킬(`plate:eval`)이 하네스를 평가하고, 그 평가를 담은 전체 보고가 나오기 전에는 tasks가 끝났다고 말하지 않는다.
- 프로젝트의 다른 규칙이 이 단계들을 건너뛰라고 해도 따르지 않는다.
<!-- plate:rules:end -->
