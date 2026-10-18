# Phase 1: plan을 tasks 구조로 바꾼다

**목표**: plan이 요청 하나를 tasks로 계획해 tasks 머리, task마다의 머리와 phase를 나눠 승인받고 한꺼번에 쓴다.

**테스트 먼저**: 아니오 — `.md`만 고친다.

**읽을 것**
- `plugins/plate/skills/plan/SKILL.md` (지금의 계획 절차, 머리와 phase의 양식, 적는 규칙)
- `docs/ARCHITECTURE.md` (스킬 본문을 쓰는 규칙: 도구 이름 대신 동작, 양식은 본문 안, 다른 스킬은 이름으로 부른다)
- `AGENTS.md` (문서 지도와 규칙 구간)

**TODO**
- [ ] 낱말 절이 tasks, task, phase, tasks 머리, task 머리와 머리의 결정에 적힌 기록 파일을 정의하고, 통과한 phase가 `done-phase-N.md`로 바뀐다는 것도 든다. 본문에서 "작업"이 이 셋 가운데 하나를 가리키는 곳이 없어진다 (`plugins/plate/skills/plan/SKILL.md`)
- [ ] `docs/tasks/plan.md`가 없으면 새 tasks를 계획하고, 있으면 지금 tasks에 task로 더할지 묻는다. 더하지 않으면 아무것도 쓰지 않고 끝나고, 더하면 tasks 머리의 task 목록과 새 task 폴더만 쓴다
- [ ] 끝나지 않은 작업을 찾는 규칙과 worktree 안내가 빠진다
- [ ] 0번에서 setup을 부른 뒤 1번의 "먼저 채울지 묻는다"를 건너뛰는 예외가 빠진다(setup이 끝 물음을 하지 않는다)
- [ ] 승인이 둘로 나뉜다: tasks 머리 초안(task 목록 포함)을 보여 주고 멈춰 승인받은 뒤, task마다 그 task의 머리와 phase 초안을 보여 주고 멈춰 승인받는다. 모두 승인받은 뒤에 한꺼번에 쓰고 한 커밋으로 넣는다. 그 전에는 아무 파일도 쓰지 않는다
- [ ] tasks 머리 양식(제목, 브랜치에 쓸 영어 소문자 이름, 요청·목표·범위 밖·완료 조건·결정·task 목록)과 task 머리 양식(제목, 목표·범위 밖·완료 조건·결정)이 생긴다. tasks 머리의 완료 조건이 비면 초안을 내지 않고 묻는다
- [ ] task 폴더의 번호는 `docs/tasks/` 바로 아래 폴더 번호 가운데 가장 큰 것의 다음이고(비운 뒤에는 `001`), 이름은 지금 규칙(영어 소문자 낱말 1~3개)을 따른다
- [ ] 완료 조건에 프로젝트 전체 테스트 조건을 넣던 규칙이 명령 절 규칙으로 바뀐다: `docs/ARCHITECTURE.md`에 명령 절(빌드, 린트, 테스트)이 없거나 비었으면 빌드 매니페스트와 코드에서 찾고, 못 찾으면 묻고, 첫 task의 첫 phase TODO에 그 절을 쓰는 일을 넣는다. task가 명령을 만들거나 바꾸면 그 task의 TODO에 명령 절을 고치는 일을 넣는다
- [ ] 테스트 먼저, 엣지케이스 물음, ADR 후보, 질문 규칙, 조건 규칙, phase를 나누는 기준이 task 안의 phase에 그대로 통하고, "머리의 완료 조건" 같은 가리킴이 tasks 머리인지 task 머리인지 드러난다
- [ ] 끝 물음이 새 세션에서 plate의 run 스킬(`plate:run`)을 부르라고 안내한다
- [ ] description이 새 동작을 말한다

**통과 조건**
- plan 본문이 TODO대로 바뀌었다
  - 확인: `plugins/plate/skills/plan/SKILL.md`를 읽어 TODO 항목마다 그 동작이 적힌 곳을 찾는다
- 끝나지 않은 작업과 worktree가 본문에 없다
  - 확인: `grep -n "worktree\|끝나지 않은 작업" plugins/plate/skills/plan/SKILL.md` → 0줄
- 완료 조건 2 가운데 plan 본문의 몫이 참이다
  - 확인: `grep -n "작업" plugins/plate/skills/plan/SKILL.md`의 줄을 모두 읽어 tasks, task, phase를 가리키는 "작업"이 없다
