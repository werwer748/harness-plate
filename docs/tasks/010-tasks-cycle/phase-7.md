# Phase 7: run이 tasks의 task를 차례로 실행한다

**목표**: run이 실행 방식을 묻고, phase마다 수행과 check를 맡기고, 통과한 phase를 `done-phase-N.md`로 바꾸고, task 회고를 맡기며, 멈출 곳에서 멈춰 논의하고 `RUNLOG.md`를 남긴다.

**테스트 먼저**: 아니오 — `.md`만 고친다.

**읽을 것**
- `plugins/plate/skills/run/SKILL.md` (지금의 조율 절차)
- `plugins/plate/skills/plan/SKILL.md` (tasks 머리의 이름과 task 목록)
- `plugins/plate/skills/phase/SKILL.md` (넘길 글, 돌려주는 줄, 막힘·계획이 틀림·훅의 세 번째 막음)
- `plugins/plate/skills/check/SKILL.md` (넘길 글, 돌려주는 줄, 확인 절)
- `plugins/plate/skills/retro/SKILL.md` (넘길 글, 돌려주는 줄, `retro.md`)

**TODO**
- [x] 낱말이 tasks, task, phase로 바뀌고 대상은 `docs/tasks/`의 tasks 하나다. tasks 머리가 없으면 plate의 plan 스킬(`plate:plan`)로 계획부터 하라고 안내하고 끝난다 (`plugins/plate/skills/run/SKILL.md`)
- [x] 시작 조건에서 계획 파일의 커밋과 커밋하지 않은 변경의 물음은 지금처럼 하고, 기본 브랜치이면 `tasks/<이름>` 브랜치를 만들어 바꾼다. worktree 처리가 빠진다
- [x] 시작할 때 실행 방식(task 하나씩, tasks 일괄)을 묻는다. 다시 불렀을 때는 `RUNLOG.md`의 그 물음과 답으로 잇는다
- [x] phase마다 수행 에이전트와 check 에이전트를 새로 띄운다. check가 통과면 `done-phase-N.md`로 이름을 바꿔 `NNN-slug: phase N 통과`로 커밋하고, 실패면 실패를 "고칠 문제"로 새 수행 에이전트에게 맡긴 뒤 다시 check를 맡긴다
- [x] task의 phase가 모두 통과하면 retro 에이전트에게 task 회고를 맡긴다. 문제가 있으면 task 하나씩은 고칠 phase의 안을 보여 승인받고, tasks 일괄은 묻지 않고 고칠 phase를 더해 돌린다. 통과하면 task 하나씩은 다음 task로 갈지 묻고, tasks 일괄은 묻지 않고 간다
- [x] 방식과 상관없이 막힘, 훅의 세 번째 막음, 계획이 틀림, 같은 phase의 check나 같은 task의 회고가 세 번 실패하면 그 자리에서 멈추고, 정해 둔 선택지 대신 원인(기록에 적힌 것)과 해결책을 보이고 논의한다. 합의한 해결책이 계획을 바꾸면 고칠 안을 보여 승인받는다
- [x] 띄운 에이전트마다 돌아온 사용량으로 한 줄(역할, task와 phase, 토큰, 도구 호출, 시간), 사용자에게 물을 때마다 한 줄(물은 것, 답)을 `docs/tasks/RUNLOG.md`에 더한다. 파일이 없으면 만든다
- [x] 모든 task의 회고가 통과하면 "tasks 끝" 절로 간다. 그 절은 phase 8이 쓰므로 여기서는 절의 제목과 자리만 둔다
- [x] LESSONS, verify, worktree, 전체 지시가 본문에서 빠지고, 직접 고치는 파일 목록이 새 기록 파일에 맞는다
- [x] description이 새 동작을 말한다

**통과 조건**
- run 본문이 TODO대로다
  - 확인: `plugins/plate/skills/run/SKILL.md`를 읽어 TODO 항목마다 그 동작이 적힌 곳을 찾는다
- 옛 흐름이 남지 않았다
  - 확인: `grep -n "LESSONS\|verify\|worktree\|전체 지시" plugins/plate/skills/run/SKILL.md` → 0줄
- 완료 조건 2 가운데 run 본문의 몫이 참이다
  - 확인: `grep -n "작업" plugins/plate/skills/run/SKILL.md`의 줄을 모두 읽어 tasks, task, phase를 가리키는 "작업"이 없다

## 한 일
- 낱말이 tasks, task, phase로 바뀌고 대상은 `docs/tasks/`의 tasks 하나다. tasks 머리가 없으면 plate의 plan 스킬(`plate:plan`)로 계획부터 하라고 안내하고 끝난다: 낱말 절을 tasks, tasks 머리, task, task 머리, phase, `done-phase-N.md`, `retro.md`, 남은 task, 지금 task, 남은 첫 phase, 실행 방식, 수행·확인·회고 에이전트로 다시 썼고, "0. tasks를 본다"가 `docs/tasks/plan.md`가 없으면 plan으로 안내하고 끝나며 task는 task 목록의 차례대로 실행한다 (`plugins/plate/skills/run/SKILL.md`)
- 시작 조건에서 계획 파일의 커밋과 커밋하지 않은 변경의 물음은 지금처럼 하고, 기본 브랜치이면 `tasks/<이름>` 브랜치를 만들어 바꾼다. worktree 처리가 빠진다: "1. 시작 조건을 본다"가 계획의 커밋(`plan: <이름>`), 커밋하지 않은 변경(남은 첫 phase의 `phase-N.md`와 `RUNLOG.md`는 세지 않는다), tasks 브랜치 셋이다. worktree 항목과 0번의 worktree 갈래를 지웠다 (`plugins/plate/skills/run/SKILL.md`)
- 시작할 때 실행 방식(task 하나씩, tasks 일괄)을 묻는다. 다시 불렀을 때는 `RUNLOG.md`의 그 물음과 답으로 잇는다: "2. 실행 방식을 정한다"가 `RUNLOG.md`에 물은 자리가 `실행 방식`인 줄이 있으면 마지막 줄의 답으로 잇고, 없으면 두 방식을 설명해 묻는다 (`plugins/plate/skills/run/SKILL.md`)
- phase마다 수행 에이전트와 check 에이전트를 새로 띄운다. check가 통과면 `done-phase-N.md`로 이름을 바꿔 `NNN-slug: phase N 통과`로 커밋하고, 실패면 실패를 "고칠 문제"로 새 수행 에이전트에게 맡긴 뒤 다시 check를 맡긴다: 4번(수행, TODO가 모두 체크됐고 마지막 확인 절이 실패일 때 `고칠 문제:` 줄을 붙인다), 5번(`plate:check`), 6번(`git mv`로 이름을 바꾸고 `NNN-slug: phase N 통과` 커밋)을 썼다. 5번의 실패는 묻지 않고 3번의 표로 돌아가 고치게 하고 다시 확인한다. 세션을 끊었다 다시 불러도 잇게, 3번의 표가 `phase-N.md`를 마지막으로 바꾼 커밋이 `NNN-slug: phase N 고침`이면 확인으로 보낸다 (`plugins/plate/skills/run/SKILL.md`)
- task의 phase가 모두 통과하면 retro 에이전트에게 task 회고를 맡긴다. 문제가 있으면 task 하나씩은 고칠 phase의 안을 보여 승인받고, tasks 일괄은 묻지 않고 고칠 phase를 더해 돌린다. 통과하면 task 하나씩은 다음 task로 갈지 묻고, tasks 일괄은 묻지 않고 간다: 7번(`plate:retro`), 8번(고칠 phase `# Phase M: 회고 K의 문제를 고친다`의 양식과 방식별 승인, `plan: NNN-slug 수정` 커밋), 9번(방식별로 다음 task로 잇는다)을 썼다. 3번의 task 표가 회고 K를 고친 `done-phase-M.md`가 있으면 회고를 다시 맡긴다 (`plugins/plate/skills/run/SKILL.md`)
- 방식과 상관없이 막힘, 훅의 세 번째 막음, 계획이 틀림, 같은 phase의 check나 같은 task의 회고가 세 번 실패하면 그 자리에서 멈추고, 정해 둔 선택지 대신 원인(기록에 적힌 것)과 해결책을 보이고 논의한다. 합의한 해결책이 계획을 바꾸면 고칠 안을 보여 승인받는다: "멈춘다" 절이 네 자리를 들고, 원인을 보인다(기록에서 옮긴다), 해결책을 낸다, 논의한다, 정한 대로 간다(계획을 바꾸면 안을 보여 승인받고 `plan: NNN-slug 수정` 커밋, 다시 맡기는 길, 멈춤)의 넷이다. 옛 "계획을 고친다" 절과 막힘의 선택지(다시 맡긴다 / 멈춘다)는 이 절로 합쳤다 (`plugins/plate/skills/run/SKILL.md`)
- 띄운 에이전트마다 돌아온 사용량으로 한 줄(역할, task와 phase, 토큰, 도구 호출, 시간), 사용자에게 물을 때마다 한 줄(물은 것, 답)을 `docs/tasks/RUNLOG.md`에 더한다. 파일이 없으면 만든다: "`RUNLOG.md`" 절에 에이전트 줄과 물음 줄의 양식, 물은 자리의 값(`실행 방식`, `커밋하지 않은 변경`, `고칠 phase`, `다음 task`, `멈춤`, `합칠지`)을 적었고, 4·5·7번이 돌아올 때마다 줄을 더하게 했다. 더한 줄은 이 스킬의 커밋(6번, 8번, "멈춘다")에 함께 넣어 git 이력에 남긴다 (`plugins/plate/skills/run/SKILL.md`)
- 모든 task의 회고가 통과하면 "tasks 끝" 절로 간다. 그 절은 phase 8이 쓰므로 여기서는 절의 제목과 자리만 둔다: `## tasks 끝` 절에 "남은 task가 없을 때 3번과 9번에서 온다." 한 줄만 두었다 (`plugins/plate/skills/run/SKILL.md`)
- LESSONS, verify, worktree, 전체 지시가 본문에서 빠지고, 직접 고치는 파일 목록이 새 기록 파일에 맞는다: 옛 "검증을 맡긴다", "`docs/LESSONS.md`" 절과 전체 지시의 갈래를 지웠다. "합친다" 절은 남기되 worktree와 검증을 빼고 `tasks/<이름>`을 기본 브랜치로 합치는 절차로 줄여 "tasks 끝에서 온다"로 했다. 절대 규칙 5가 계획 파일, 이름을 바꾸는 `phase-N.md`, `docs/tasks/RUNLOG.md`만 든다 (`plugins/plate/skills/run/SKILL.md`)
- description이 새 동작을 말한다: 실행 방식의 물음, `tasks/<이름>` 브랜치, 수행·확인·회고의 세 스킬, `done-phase-N.md`, 고칠 phase, 멈춤과 논의, `RUNLOG.md`, tasks 끝을 말한다 (`plugins/plate/skills/run/SKILL.md`)

## 확인 결과
- run 본문이 TODO대로다
  - `plugins/plate/skills/run/SKILL.md`를 읽어 TODO마다 찾음 → TODO 1: 낱말 절(22~42줄)과 0번(44~48줄). TODO 2: 1번(50~56줄). TODO 3: 2번(58~67줄). TODO 4: 4번(97~111줄), 5번(113~126줄), 6번(128~133줄), 3번의 phase 표(77~84줄). TODO 5: 7번(135~147줄), 8번(149~189줄), 9번(191~197줄), 3번의 task 표(88~93줄). TODO 6: "멈춘다"(211~228줄). TODO 7: "`RUNLOG.md`" 절(245~262줄)과 4·5·7번의 "돌아오면 `RUNLOG.md`에 그 에이전트의 줄을 더한다". TODO 8: "tasks 끝"(230~232줄). TODO 9: 절대 규칙 5(20줄)와 아래 grep. TODO 10: description(3줄). 통과
- 옛 흐름이 남지 않았다
  - `grep -n "LESSONS\|verify\|worktree\|전체 지시" plugins/plate/skills/run/SKILL.md` → 0줄. 통과
- 완료 조건 2 가운데 run 본문의 몫이 참이다
  - `grep -n "작업" plugins/plate/skills/run/SKILL.md` → 0줄. tasks, task, phase를 가리키는 "작업"이 없다. 통과

## 계획과 달라진 점
없음

## 남은 것
없음

## 하네스에서 걸린 것
- `plugins/plate/skills/eval/SKILL.md`의 "정해 둔 물음"은 실행 방식, task 회고 뒤의 물음, tasks 끝의 고칠지와 합칠지만 든다. run은 시작할 때 커밋하지 않은 변경이 있으면 묻고(이 phase에서 지금처럼 두었다) 그 줄을 `RUNLOG.md`에 `커밋하지 않은 변경`으로 남기는데, eval이 이 줄을 멈춤으로 셀 수 있다. 이 phase의 TODO 밖이라 eval은 고치지 않았다.
- task 하나씩에서 회고의 문제를 고칠 phase의 안을 사용자가 승인하지 않으면 run은 만들지 않고 보고로 끝난다. 옛 run에 있던 "남은 문제를 고치지 않기로 했다"처럼 문제를 남긴 채 task를 닫는 길은 계획에 없어 넣지 않았다. 다시 부르면 같은 안을 다시 묻는다.
- 이 phase는 0.9.1 복사본의 레일에서 돌아, 넘겨받은 글이 옛 낱말(`작업 폴더:`)이고 읽은 phase 스킬도 옛 판이다. 새 phase 스킬은 `task 폴더:`를 받으므로 새 run 본문은 그 낱말로 넘긴다.
