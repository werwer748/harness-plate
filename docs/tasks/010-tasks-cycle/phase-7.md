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
- [ ] 낱말이 tasks, task, phase로 바뀌고 대상은 `docs/tasks/`의 tasks 하나다. tasks 머리가 없으면 plate의 plan 스킬(`plate:plan`)로 계획부터 하라고 안내하고 끝난다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] 시작 조건에서 계획 파일의 커밋과 커밋하지 않은 변경의 물음은 지금처럼 하고, 기본 브랜치이면 `tasks/<이름>` 브랜치를 만들어 바꾼다. worktree 처리가 빠진다
- [ ] 시작할 때 실행 방식(task 하나씩, tasks 일괄)을 묻는다. 다시 불렀을 때는 `RUNLOG.md`의 그 물음과 답으로 잇는다
- [ ] phase마다 수행 에이전트와 check 에이전트를 새로 띄운다. check가 통과면 `done-phase-N.md`로 이름을 바꿔 `NNN-slug: phase N 통과`로 커밋하고, 실패면 실패를 "고칠 문제"로 새 수행 에이전트에게 맡긴 뒤 다시 check를 맡긴다
- [ ] task의 phase가 모두 통과하면 retro 에이전트에게 task 회고를 맡긴다. 문제가 있으면 task 하나씩은 고칠 phase의 안을 보여 승인받고, tasks 일괄은 묻지 않고 고칠 phase를 더해 돌린다. 통과하면 task 하나씩은 다음 task로 갈지 묻고, tasks 일괄은 묻지 않고 간다
- [ ] 방식과 상관없이 막힘, 훅의 세 번째 막음, 계획이 틀림, 같은 phase의 check나 같은 task의 회고가 세 번 실패하면 그 자리에서 멈추고, 정해 둔 선택지 대신 원인(기록에 적힌 것)과 해결책을 보이고 논의한다. 합의한 해결책이 계획을 바꾸면 고칠 안을 보여 승인받는다
- [ ] 띄운 에이전트마다 돌아온 사용량으로 한 줄(역할, task와 phase, 토큰, 도구 호출, 시간), 사용자에게 물을 때마다 한 줄(물은 것, 답)을 `docs/tasks/RUNLOG.md`에 더한다. 파일이 없으면 만든다
- [ ] 모든 task의 회고가 통과하면 "tasks 끝" 절로 간다. 그 절은 phase 8이 쓰므로 여기서는 절의 제목과 자리만 둔다
- [ ] LESSONS, verify, worktree, 전체 지시가 본문에서 빠지고, 직접 고치는 파일 목록이 새 기록 파일에 맞는다
- [ ] description이 새 동작을 말한다

**통과 조건**
- run 본문이 TODO대로다
  - 확인: `plugins/plate/skills/run/SKILL.md`를 읽어 TODO 항목마다 그 동작이 적힌 곳을 찾는다
- 옛 흐름이 남지 않았다
  - 확인: `grep -n "LESSONS\|verify\|worktree\|전체 지시" plugins/plate/skills/run/SKILL.md` → 0줄
- 완료 조건 2 가운데 run 본문의 몫이 참이다
  - 확인: `grep -n "작업" plugins/plate/skills/run/SKILL.md`의 줄을 모두 읽어 tasks, task, phase를 가리키는 "작업"이 없다
