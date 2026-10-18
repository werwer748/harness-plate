# Phase 1: plan을 tasks 구조로 바꾼다

**목표**: plan이 요청 하나를 tasks로 계획해 tasks 머리, task마다의 머리와 phase를 나눠 승인받고 한꺼번에 쓴다.

**테스트 먼저**: 아니오 — `.md`만 고친다.

**읽을 것**
- `plugins/plate/skills/plan/SKILL.md` (지금의 계획 절차, 머리와 phase의 양식, 적는 규칙)
- `docs/ARCHITECTURE.md` (스킬 본문을 쓰는 규칙: 도구 이름 대신 동작, 양식은 본문 안, 다른 스킬은 이름으로 부른다)
- `AGENTS.md` (문서 지도와 규칙 구간)

**TODO**
- [x] 낱말 절이 tasks, task, phase, tasks 머리, task 머리와 머리의 결정에 적힌 기록 파일을 정의하고, 통과한 phase가 `done-phase-N.md`로 바뀐다는 것도 든다. 본문에서 "작업"이 이 셋 가운데 하나를 가리키는 곳이 없어진다 (`plugins/plate/skills/plan/SKILL.md`)
- [x] `docs/tasks/plan.md`가 없으면 새 tasks를 계획하고, 있으면 지금 tasks에 task로 더할지 묻는다. 더하지 않으면 아무것도 쓰지 않고 끝나고, 더하면 tasks 머리의 task 목록과 새 task 폴더만 쓴다
- [x] 끝나지 않은 작업을 찾는 규칙과 worktree 안내가 빠진다
- [x] 0번에서 setup을 부른 뒤 1번의 "먼저 채울지 묻는다"를 건너뛰는 예외가 빠진다(setup이 끝 물음을 하지 않는다)
- [x] 승인이 둘로 나뉜다: tasks 머리 초안(task 목록 포함)을 보여 주고 멈춰 승인받은 뒤, task마다 그 task의 머리와 phase 초안을 보여 주고 멈춰 승인받는다. 모두 승인받은 뒤에 한꺼번에 쓰고 한 커밋으로 넣는다. 그 전에는 아무 파일도 쓰지 않는다
- [x] tasks 머리 양식(제목, 브랜치에 쓸 영어 소문자 이름, 요청·목표·범위 밖·완료 조건·결정·task 목록)과 task 머리 양식(제목, 목표·범위 밖·완료 조건·결정)이 생긴다. tasks 머리의 완료 조건이 비면 초안을 내지 않고 묻는다
- [x] task 폴더의 번호는 `docs/tasks/` 바로 아래 폴더 번호 가운데 가장 큰 것의 다음이고(비운 뒤에는 `001`), 이름은 지금 규칙(영어 소문자 낱말 1~3개)을 따른다
- [x] 완료 조건에 프로젝트 전체 테스트 조건을 넣던 규칙이 명령 절 규칙으로 바뀐다: `docs/ARCHITECTURE.md`에 명령 절(빌드, 린트, 테스트)이 없거나 비었으면 빌드 매니페스트와 코드에서 찾고, 못 찾으면 묻고, 첫 task의 첫 phase TODO에 그 절을 쓰는 일을 넣는다. task가 명령을 만들거나 바꾸면 그 task의 TODO에 명령 절을 고치는 일을 넣는다
- [x] 테스트 먼저, 엣지케이스 물음, ADR 후보, 질문 규칙, 조건 규칙, phase를 나누는 기준이 task 안의 phase에 그대로 통하고, "머리의 완료 조건" 같은 가리킴이 tasks 머리인지 task 머리인지 드러난다
- [x] 끝 물음이 새 세션에서 plate의 run 스킬(`plate:run`)을 부르라고 안내한다
- [x] description이 새 동작을 말한다

**통과 조건**
- plan 본문이 TODO대로 바뀌었다
  - 확인: `plugins/plate/skills/plan/SKILL.md`를 읽어 TODO 항목마다 그 동작이 적힌 곳을 찾는다
- 끝나지 않은 작업과 worktree가 본문에 없다
  - 확인: `grep -n "worktree\|끝나지 않은 작업" plugins/plate/skills/plan/SKILL.md` → 0줄
- 완료 조건 2 가운데 plan 본문의 몫이 참이다
  - 확인: `grep -n "작업" plugins/plate/skills/plan/SKILL.md`의 줄을 모두 읽어 tasks, task, phase를 가리키는 "작업"이 없다

## 한 일
- 낱말 절이 tasks, task, phase, tasks 머리, task 머리와 머리의 결정에 적힌 기록 파일을 정의하고, 통과한 phase가 `done-phase-N.md`로 바뀐다는 것도 든다. 본문에서 "작업"이 이 셋 가운데 하나를 가리키는 곳이 없어진다: 낱말 절에 tasks(기록 파일 `plan.md`, `FRICTION.md`, `RUNLOG.md`, `review.md`, `eval.md`, task 폴더), task(`plan.md`, `phase-N.md`, `done-phase-N.md`, `retro.md`), phase(통과하면 실행이 `done-phase-N.md`로 바꾼다), tasks 머리, task 머리, 계획 파일, 명령 절을 정의했다. "작업"을 모두 tasks, task, phase로 바꿔 본문에 "작업"이 한 번도 남지 않는다 (`plugins/plate/skills/plan/SKILL.md`)
- `docs/tasks/plan.md`가 없으면 새 tasks를 계획하고, 있으면 지금 tasks에 task로 더할지 묻는다. 더하지 않으면 아무것도 쓰지 않고 끝나고, 더하면 tasks 머리의 task 목록과 새 task 폴더만 쓴다: 새 1번 "진행 중인 tasks가 있는지 본다"를 두고, 더하는 경우는 6번에서 task 목록 절만 보여 주고 7번에서 task 목록 절 끝에 줄만 더하게 했다. 커밋 메시지는 새 tasks면 `plan: <이름>`, 더하는 경우면 `plan: NNN-slug 더함`으로 정했다 (`plugins/plate/skills/plan/SKILL.md`)
- 끝나지 않은 작업을 찾는 규칙과 worktree 안내가 빠진다: 낱말의 정의, 2번의 찾는 규칙, 6번의 알림 줄, 8번의 보고 줄, 9번의 worktree 안내를 지웠다 (`plugins/plate/skills/plan/SKILL.md`)
- 0번에서 setup을 부른 뒤 1번의 "먼저 채울지 묻는다"를 건너뛰는 예외가 빠진다: 0번은 setup을 끝까지 따른 뒤 1번으로 돌아오기만 하고, 맥락 문서 단계(새 2번)의 채울지 물음은 예외 없이 돈다 (`plugins/plate/skills/plan/SKILL.md`)
- 승인이 둘로 나뉜다: 6번이 두 차례(tasks 머리 → task 목록의 차례대로 task마다 task 머리와 phase)로 나뉘고, 마지막 task의 초안까지 승인받기 전에는 7번으로 가지 않으며, 절대 규칙 1에 "모든 초안을 승인받기 전에는 아무 파일도 쓰지 않는다"를 더했다. 7번은 모두 쓴 뒤 한 커밋으로 넣는다. 앞서 승인받은 초안이 바뀌면 다시 보여 주고 승인받는다 (`plugins/plate/skills/plan/SKILL.md`)
- tasks 머리 양식과 task 머리 양식이 생긴다. tasks 머리의 완료 조건이 비면 초안을 내지 않고 묻는다: 양식 절에 tasks 머리(제목, `**이름**:` 줄, 여섯 절)와 task 머리(제목, 네 절)를 두고, 적는 규칙에 "완료 조건은 '없음'으로 적지 않는다"를, 5번에 "tasks 머리의 완료 조건을 적을 수 없으면 초안을 내지 않고 묻는다"를 넣었다 (`plugins/plate/skills/plan/SKILL.md`)
- task 폴더의 번호와 이름 규칙: 적는 규칙의 "이름과 번호"에 가장 큰 번호의 다음, 없으면(비운 뒤도) `001`, 여러 task는 차례대로 하나씩 늘린다, 이름은 영어 소문자 낱말 1~3개를 적었다. tasks 머리의 이름도 같은 꼴로 적었다 (`plugins/plate/skills/plan/SKILL.md`)
- 완료 조건에 프로젝트 전체 테스트 조건을 넣던 규칙이 명령 절 규칙으로 바뀐다: 그 규칙을 지우고, 3번에 명령 절이 없거나 적히지 않은 명령이 있으면 빌드 매니페스트와 코드에서 찾고 못 찾으면 5번에서 묻고 이번에 쓰는 첫 task의 첫 phase TODO에 그 절을 쓰는 일(찾은 명령과 답을 글에)을 넣게 했다. TODO 규칙에 "빌드, 린트, 테스트의 명령이 생기거나 바뀐다: 명령 절을 고친다"를 더했다 (`plugins/plate/skills/plan/SKILL.md`)
- 테스트 먼저, 엣지케이스 물음, ADR 후보, 질문 규칙, 조건 규칙, phase를 나누는 기준이 task 안의 phase에 그대로 통하고 가리킴이 드러난다: 엣지케이스의 뺀 것은 "그 phase가 든 task 머리의 범위 밖", ADR 후보는 그 결정을 이루는 task의 초안 뒤, 번호 가리킴은 "완료 조건 2"(task 머리)와 "tasks 완료 조건 2"(tasks 머리)로 나눴다. phase를 나누는 기준 2는 task 머리와 그 phase 파일만 읽는다로 바꾸고, task를 나누는 기준을 짧게 더했다 (`plugins/plate/skills/plan/SKILL.md`)
- 끝 물음이 새 세션에서 plate의 run 스킬(`plate:run`)을 부르라고 안내한다: 9번에서 번호를 넘기라는 글과 worktree 안내를 빼고 run을 부르라고만 안내한다 (`plugins/plate/skills/plan/SKILL.md`)
- description이 새 동작을 말한다: tasks로 계획, tasks 머리와 task 폴더, 두 차례 승인 뒤 한 커밋, 진행 중인 tasks에 더할지 묻기를 적었다. 트리거 예문 "작업 계획하자"는 "작업"이 tasks를 가리켜 뺐다 (`plugins/plate/skills/plan/SKILL.md`)

## 확인 결과
- plan 본문이 TODO대로 바뀌었다
  - `plugins/plate/skills/plan/SKILL.md`를 읽어 항목마다 찾았다 → 낱말 23~29행(`done-phase-N.md`는 25행), 진행 중인 tasks 41~46행과 7번 103행, 0번 34~39행(예외 없음), 두 차례 승인 88~99행과 절대 규칙 1(16행), 양식 126행·153행과 완료 조건 203행·76행, 번호와 이름 194~199행, 명령 절 29행·58~62행·260행, 엣지케이스 86행·ADR 후보 95행·가리킴 227~228행·나누는 기준 230~245행·테스트 먼저 249행, 끝 물음 113~117행, description 3행. 통과
- 끝나지 않은 작업과 worktree가 본문에 없다
  - `grep -n "worktree\|끝나지 않은 작업" plugins/plate/skills/plan/SKILL.md` → 0줄. 통과
- 완료 조건 2 가운데 plan 본문의 몫이 참이다
  - `grep -n "작업" plugins/plate/skills/plan/SKILL.md` → 0줄(읽을 줄이 없어 tasks, task, phase를 가리키는 "작업"이 없다). 통과

## 계획과 달라진 점
- 없음

## 남은 것
- 없음

## 하네스에서 걸린 것
- 머리의 결정이 "명령 절"과 tasks 머리의 "브랜치에 쓸 이름"의 꼴(절 제목, 줄의 꼴)을 정하지 않아, 이 phase가 `## 명령` 절의 `- 빌드:`/`- 린트:`/`- 테스트:` 세 줄과 tasks 머리의 `**이름**:` 줄로 정했다. 명령 절을 읽는 check·retro·review와 이름을 읽는 run을 고치는 phase가 다른 꼴을 고르면 어긋난다. 여러 phase가 함께 쓰는 꼴이니 phase를 나누는 기준 2대로라면 머리에 있어야 했다

## 회고 1: 회고

**확인**
- plan 본문이 TODO대로 바뀌었다
  - `plugins/plate/skills/plan/SKILL.md`를 읽어 TODO 항목마다 찾았다 → 낱말 23~29행(`done-phase-N.md`는 25행), 진행 중인 tasks 1번 41~46행과 6번 92행·7번 103행, 0번 38행(채울지 건너뛰는 예외 없음), 두 차례 승인 88~99행과 절대 규칙 1(16행), tasks 머리 양식 126~151행과 task 머리 양식 153~170행, 빈 완료 조건 76행·203행, 번호와 이름 194~199행, 명령 절 29행·62행·260행(옛 "전체 테스트 조건" 규칙 없음), 엣지케이스 83행·86행, ADR 후보 95행, 가리킴 227~228행, 나누는 기준 230~244행, 끝 물음 117행, description 3행. 통과
- 끝나지 않은 작업과 worktree가 본문에 없다
  - `grep -n "worktree\|끝나지 않은 작업" plugins/plate/skills/plan/SKILL.md` → 0줄(종료 코드 1). 통과
- 완료 조건 2 가운데 plan 본문의 몫이 참이다
  - `grep -n "작업" plugins/plate/skills/plan/SKILL.md` → 0줄(종료 코드 1). 읽을 줄이 없어 tasks, task, phase를 가리키는 "작업"이 없다. 통과

**문제**
- 없음

**배운 것**
- 명령 절의 꼴은 plan 본문 29행이 정했다: `docs/ARCHITECTURE.md`의 `## 명령` 절에 `- 빌드: …`, `- 린트: …`, `- 테스트: …` 세 줄이고 없는 명령은 "없음"이다. tasks 머리의 브랜치 이름은 제목 아래 `**이름**: …` 줄이다(131행). 맥락 문서와 010 `plan.md`에는 이 꼴이 없다. 명령 절을 읽거나 쓰는 뒤 phase(check, retro, review, 이 레포의 명령 절을 쓰는 phase 12)와 이름을 읽는 run은 이 꼴을 따라야 어긋나지 않는다.

**하네스의 문제점**
- 010 `plan.md`의 결정이 여러 phase가 함께 쓰는 꼴(명령 절의 절 제목과 줄, tasks 머리의 이름 줄)을 정하지 않았다. 이 계획을 쓴 plan 스킬의 "phase를 나누는 기준" 2(여러 phase가 함께 쓰는 정의는 머리에 적는다)에 걸리고, phase 1이 꼴을 골랐다("하네스에서 걸린 것"). phase 3, 4, 5, 7은 plan 본문을 읽을 것에 두어 그 꼴을 볼 수 있지만, 이 레포의 명령 절을 쓰는 phase 12의 읽을 것에는 plan 본문도 check 본문도 없어 완료 조건 10의 "명령 절이 하나 있고"를 다른 꼴로 채울 수 있다 (`docs/tasks/010-tasks-cycle/phase-12.md`).
- 진행 중인 tasks에 더하는 경우 새 요청 글이 계획 파일 어디에도 남지 않는다. 7번은 tasks 머리의 task 목록 절 말고는 고치지 않고(103행), task 머리 양식에는 요청 절이 없다(153~170행, 010 `plan.md` 결정의 task 머리 네 절). 새 tasks에서 요청 글을 그대로 남기는 규칙(204행)이 더하는 경우에는 통하지 않는다. TODO와 결정대로라 문제로 적지 않았다.

**판정**: 통과
