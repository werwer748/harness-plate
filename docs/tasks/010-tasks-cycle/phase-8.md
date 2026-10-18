# Phase 8: run이 tasks 끝을 잇는다

**목표**: 모든 task가 끝나면 run이 review와 eval을 맡겨 전체 보고를 하고, 고칠지 한 번에 묻고, 고침, 이슈, BACKLOG, 비우기, 합치기까지 잇는다.

**테스트 먼저**: 아니오 — `.md`만 고친다.

**읽을 것**
- `plugins/plate/skills/run/SKILL.md` (phase 7이 바꾼 본문, "tasks 끝" 절의 자리, 지금의 합치기 절차)
- `plugins/plate/skills/review/SKILL.md` (넘길 글, 돌려주는 줄, `review.md`)
- `plugins/plate/skills/eval/SKILL.md` (넘길 글, 돌려주는 줄, `eval.md`, 하네스 고칠 거리와 이슈 글)
- `plugins/plate/skills/plan/SKILL.md` (task 머리와 phase의 양식. 고침 task의 안에 쓴다)
- `plugins/plate/skills/retro/SKILL.md` (task 회고)

**TODO**
- [ ] "tasks 끝" 절이 review 에이전트와 eval 에이전트를 서로 다른 새 에이전트로 띄운다. 둘 다 `docs/tasks/`를 비우기 전에 한다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] 전체 보고가 답글 하나에 코드 평가의 범주 등급과 게이트, 하네스 eval의 기준 등급, 소스 문제, 하네스 고칠 거리(plate 자체, 그 프로젝트만), 스킬로 만들 후보를 보인다
- [ ] 보고 끝에 고칠 안(고침 task의 머리와 phase, 이슈로 올릴 것, BACKLOG로 미룰 것)을 함께 보이고 한 번에 묻는다. 고칠 곳을 말하면 고쳐 다시 보인다. 두 방식 모두 같다
- [ ] 고치기로 한 것이 있으면 승인받은 안대로 같은 tasks에 고침 task(다음 번호)를 쓰고 커밋한다. 고침 task의 완료 조건에는 고칠 문제마다의 조건과 tasks 머리의 완료 조건이 들고, 같은 레일(phase, check, 회고)로 돌린다. 그 프로젝트만의 하네스 고칠 거리도 이 task에 든다. 고친 뒤에는 review와 eval을 다시 하지 않는다
- [ ] plate 자체의 고칠 거리를 올리기로 했으면 `werwer748/harness-plate`에서 같은 이슈를 찾아, 있으면 "다시 나옴" 댓글을, 없으면 새 이슈를 단다. 이슈 주소를 보고에 적는다. 올리지 못하면 까닭과 올릴 글을 보인다
- [ ] 미룬 소스 문제를 `docs/BACKLOG.md`에 항목마다 나온 tasks 이름과 함께 적는다. 이미 있는 항목이 다시 나오면 그 tasks를 더하고 보고에서 고치자고 제안한다. 세 번의 tasks 동안 다시 나오지 않은 항목은 지운다. 파일을 처음 만들 때 문서 지도에 행이 없으면 묻지 않고 더한다
- [ ] 고침이 끝나거나 고칠 것이 없으면 `docs/tasks/` 아래를 `.gitkeep`만 남기고 지워 tasks 이름으로 시작하는 메시지로 커밋한다
- [ ] 비운 뒤 기본 브랜치로 합칠지 묻는다. 합치기는 지금 절차(squash하지 않음, 충돌하면 되돌리고 알림, 합치면 브랜치를 지움)를 따른다
- [ ] 보고 절이 새 흐름(통과한 phase, 회고와 끝의 판정, 이슈 주소, BACKLOG의 변경)에 맞는다

**통과 조건**
- run 본문이 TODO대로다
  - 확인: `plugins/plate/skills/run/SKILL.md`를 읽어 TODO 항목마다 그 동작이 적힌 곳을 찾는다
- 완료 조건 2 가운데 run 본문의 몫이 참이다
  - 확인: `grep -n "작업" plugins/plate/skills/run/SKILL.md`의 줄을 모두 읽어 tasks, task, phase를 가리키는 "작업"이 없다
