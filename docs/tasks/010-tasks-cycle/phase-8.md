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
- [x] "tasks 끝" 절이 review 에이전트와 eval 에이전트를 서로 다른 새 에이전트로 띄운다. 둘 다 `docs/tasks/`를 비우기 전에 한다 (`plugins/plate/skills/run/SKILL.md`)
- [x] 전체 보고가 답글 하나에 코드 평가의 범주 등급과 게이트, 하네스 eval의 기준 등급, 소스 문제, 하네스 고칠 거리(plate 자체, 그 프로젝트만), 스킬로 만들 후보를 보인다
- [x] 보고 끝에 고칠 안(고침 task의 머리와 phase, 이슈로 올릴 것, BACKLOG로 미룰 것)을 함께 보이고 한 번에 묻는다. 고칠 곳을 말하면 고쳐 다시 보인다. 두 방식 모두 같다
- [x] 고치기로 한 것이 있으면 승인받은 안대로 같은 tasks에 고침 task(다음 번호)를 쓰고 커밋한다. 고침 task의 완료 조건에는 고칠 문제마다의 조건과 tasks 머리의 완료 조건이 들고, 같은 레일(phase, check, 회고)로 돌린다. 그 프로젝트만의 하네스 고칠 거리도 이 task에 든다. 고친 뒤에는 review와 eval을 다시 하지 않는다
- [x] plate 자체의 고칠 거리를 올리기로 했으면 `werwer748/harness-plate`에서 같은 이슈를 찾아, 있으면 "다시 나옴" 댓글을, 없으면 새 이슈를 단다. 이슈 주소를 보고에 적는다. 올리지 못하면 까닭과 올릴 글을 보인다
- [x] 미룬 소스 문제를 `docs/BACKLOG.md`에 항목마다 나온 tasks 이름과 함께 적는다. 이미 있는 항목이 다시 나오면 그 tasks를 더하고 보고에서 고치자고 제안한다. 세 번의 tasks 동안 다시 나오지 않은 항목은 지운다. 파일을 처음 만들 때 문서 지도에 행이 없으면 묻지 않고 더한다
- [x] 고침이 끝나거나 고칠 것이 없으면 `docs/tasks/` 아래를 `.gitkeep`만 남기고 지워 tasks 이름으로 시작하는 메시지로 커밋한다
- [x] 비운 뒤 기본 브랜치로 합칠지 묻는다. 합치기는 지금 절차(squash하지 않음, 충돌하면 되돌리고 알림, 합치면 브랜치를 지움)를 따른다
- [x] 보고 절이 새 흐름(통과한 phase, 회고와 끝의 판정, 이슈 주소, BACKLOG의 변경)에 맞는다

**통과 조건**
- run 본문이 TODO대로다
  - 확인: `plugins/plate/skills/run/SKILL.md`를 읽어 TODO 항목마다 그 동작이 적힌 곳을 찾는다
- 완료 조건 2 가운데 run 본문의 몫이 참이다
  - 확인: `grep -n "작업" plugins/plate/skills/run/SKILL.md`의 줄을 모두 읽어 tasks, task, phase를 가리키는 "작업"이 없다

## 한 일
- "tasks 끝" 절이 review 에이전트와 eval 에이전트를 서로 다른 새 에이전트로 띄운다. 둘 다 `docs/tasks/`를 비우기 전에 한다: "tasks 끝" 절에 파일만 보고 갈 곳을 정하는 표(`review.md` 없음 → 코드 평가, `eval.md` 없음 → 하네스 eval, 고침 task 있음 → 비운다, 그 밖 → 보고하고 묻는다)와 "코드 평가를 맡긴다", "하네스 eval을 맡긴다"(코드 평가 에이전트가 돌아온 뒤 그와 다른 새 에이전트, 넘길 글 한 줄)를 썼다. 절대 규칙 1·2, 낱말(코드 평가 에이전트, 하네스 eval 에이전트), 첫 단락, description에도 넣었다 (`plugins/plate/skills/run/SKILL.md`)
- 전체 보고가 답글 하나에 코드 평가의 범주 등급과 게이트, 하네스 eval의 기준 등급, 소스 문제, 하네스 고칠 거리(plate 자체, 그 프로젝트만), 스킬로 만들 후보를 보인다: "보고하고 묻는다"의 1~5 (`plugins/plate/skills/run/SKILL.md`)
- 보고 끝에 고칠 안(고침 task의 머리와 phase, 이슈로 올릴 것, BACKLOG로 미룰 것)을 함께 보이고 한 번에 묻는다. 고칠 곳을 말하면 고쳐 다시 보인다. 두 방식 모두 같다: "보고하고 묻는다"의 6과 그 아래(처음 안은 모두 고치고 올리는 것, tasks 일괄에서도 묻는다, 고칠 곳이면 고쳐 다시 묻는다, 아무것도 안 하겠다는 답, 고칠 것이 없으면 묻지 않는다). `RUNLOG.md`의 물은 자리에 `고칠지`를 더했다 (`plugins/plate/skills/run/SKILL.md`)
- 고치기로 한 것이 있으면 승인받은 안대로 같은 tasks에 고침 task(다음 번호)를 쓰고 커밋한다 …: "고침 task를 더한다"에 번호와 이름(`NNN-fixes`), task 목록에 줄 더하기, `plan: NNN-fixes 더함` 커밋, 3번으로 가서 같은 레일(수행, 확인, 회고, 8번의 고칠 phase)로 도는 것, "고침 task의 꼴"(완료 조건은 고칠 것마다 하나와 tasks 머리의 완료 조건을 가리키는 하나, 이 프로젝트만의 하네스 고칠 거리도 고칠 것에 든다)과 두 파일의 양식을 썼다. 고친 뒤 review와 eval을 다시 하지 않는 것은 "tasks 끝"의 표(고침 task가 있으면 비운다)와 그 아래 단락에 있다 (`plugins/plate/skills/run/SKILL.md`)
- plate 자체의 고칠 거리를 올리기로 했으면 `werwer748/harness-plate`에서 같은 이슈를 찾아 …: "이슈를 올린다"에 `gh issue list`/`view`로 찾기, 이 tasks 이름이 이미 있으면 다시 올리지 않기, `gh issue comment`(첫 줄 `다시 나옴`), `gh issue create`, 주소를 보고에, 올리지 못하면 까닭과 올릴 글을 보이고 멈추지 않는 것을 썼다. 낱말에 plate 저장소를 더했다 (`plugins/plate/skills/run/SKILL.md`)
- 미룬 소스 문제를 `docs/BACKLOG.md`에 …: "BACKLOG를 고친다"에 미룬 것 더하기와 다시 나오면 나온 tasks 더하기, 고치기로 한 것 지우기, 다시 나오지 않은 tasks가 셋이면 지우기, 같은 tasks를 두 번 세지 않기, 처음 만들 때 문서 지도에 묻지 않고 행 더하기, `<tasks 이름>: BACKLOG` 커밋과 파일 양식을 썼다. 다시 나온 항목을 고치자고 제안하는 것은 "보고하고 묻는다"의 3에 있다 (`plugins/plate/skills/run/SKILL.md`)
- 고침이 끝나거나 고칠 것이 없으면 `docs/tasks/` 아래를 `.gitkeep`만 남기고 지워 …: "비운다"에 남은 `RUNLOG.md` 줄의 먼저 커밋(`<tasks 이름>: RUNLOG`), `git rm -r`로 `.gitkeep` 밖을 지우기, `<tasks 이름>: 비움` 커밋을 썼다. 절대 규칙 5와 `RUNLOG.md` 절도 맞췄다 (`plugins/plate/skills/run/SKILL.md`)
- 비운 뒤 기본 브랜치로 합칠지 묻는다 …: "합친다"가 "비운다"에서 오게 하고 git 레포가 아니면 묻지 않게 했다. 절차(squash하지 않음, 충돌하면 `git merge --abort`, 합치면 브랜치를 지움)는 그대로 두었다. 비운 뒤라 `RUNLOG.md`가 없으므로 비운 뒤의 물음은 적지 않는다고 `RUNLOG.md` 절에 적고 물은 자리 목록에서 `합칠지`를 뺐다 (`plugins/plate/skills/run/SKILL.md`)
- 보고 절이 새 흐름 …에 맞는다: 10번에 코드 평가와 하네스 eval의 등급, 고침 task, 이슈와 댓글의 주소(올리지 못한 것 포함), `docs/BACKLOG.md`의 변경, 비운 커밋을 더했다 (`plugins/plate/skills/run/SKILL.md`)

## 확인 결과
- run 본문이 TODO대로다
  - `plugins/plate/skills/run/SKILL.md`를 읽고 `grep -n`으로 자리를 찾음 → TODO 1: 251행(비우기 전에), 253·263행(두 절), 절대 규칙 2. TODO 2: 275행(답글 하나에)과 그 아래 1~5. TODO 3: 6의 고칠 안, 289행(한 번에 묻고, tasks 일괄에서도 묻는다), 291행(고칠 곳). TODO 4: 339~402행(고침 task를 더한다, `plan: NNN-fixes 더함`, 고침 task의 꼴), 251행(다시 하지 않는다). TODO 5: 299~309행. TODO 6: 311~337행, 보고 3. TODO 7: 404~412행. TODO 8: 414~423행(squash, `merge --abort`, `branch -d`). TODO 9: 206~217행. 통과
- 완료 조건 2 가운데 run 본문의 몫이 참이다
  - `grep -n "작업" plugins/plate/skills/run/SKILL.md` → 출력 없음(exit 1). 통과
- (덧붙여 돌림) `python3 -m unittest discover -s tests` → 마지막 줄 `OK`

## 계획과 달라진 점
- 없음

## 남은 것
- 없음

## 하네스에서 걸린 것
- phase 7이 쓴 `RUNLOG.md` 절의 물은 자리에 `합칠지`가 있었지만, 이 phase의 TODO대로면 합칠지는 `docs/tasks/`를 비운 뒤에 묻는다. 그때는 `RUNLOG.md`가 없고, 다시 만들면 완료 조건 6의 `ls -A docs/tasks` → `.gitkeep`만과 어긋난다. 그래서 비운 뒤의 물음은 적지 않게 고쳤다.
- "합친다"는 합칠 브랜치를 `tasks/<이름>`으로 정해 두었는데, 1번은 기본 브랜치가 아니면 브랜치를 만들지 않고 지금 브랜치에서 실행한다. 그 경우 `git merge tasks/<이름>`이 없는 브랜치를 가리킨다. TODO가 지금 절차를 따르라고 해서 고치지 않았다.

## 회고 1: 확인만

**확인**
- run 본문이 TODO대로다
  - `plugins/plate/skills/run/SKILL.md`를 읽어 TODO 항목마다 그 동작이 적힌 곳을 찾음 → TODO 1: "tasks 끝"의 표(244~249행), 251행(둘 다 `docs/tasks/`를 비우기 전에), "코드 평가를 맡긴다"(253~261행), "하네스 eval을 맡긴다"(263~271행, 코드 평가 에이전트와 다른 새 에이전트), 절대 규칙 2(17행). TODO 2: "보고하고 묻는다" 275행(답글 하나에)과 1~5(277~281행: 범주 등급과 게이트, 기준 등급, 소스 문제, plate 자체와 이 프로젝트만으로 나눈 하네스 고칠 거리, 스킬로 만들 후보). TODO 3: 6(282~285행: 고침 task의 머리와 `phase-1.md`, 이슈로 올릴 것, BACKLOG로 미룰 것), 289행(한 번에 묻고 tasks 일괄에서도 묻는다), 291행(고칠 곳을 말하면 고쳐 다시 보이고 묻는다), 242행(실행 방식과 상관없이 같다). TODO 4: "고침 task를 더한다"(339~347행: 다음 번호의 `NNN-fixes`, 승인받은 안대로 쓰고 `plan: NNN-fixes 더함` 커밋, 3번으로 가 phase·확인·회고의 같은 레일), "고침 task의 꼴"(351~352행: 이 프로젝트만의 하네스 고칠 거리가 들고, 고칠 것마다의 조건과 tasks 머리의 완료 조건을 가리키는 조건), 251행(고친 뒤 코드 평가와 하네스 eval을 다시 하지 않는다). TODO 5: "이슈를 올린다"(299~309행: `werwer748/harness-plate`에서 `gh issue list`/`view`로 찾기, 첫 줄 `다시 나옴` 댓글, `gh issue create`, 주소를 보고에, 올리지 못하면 까닭과 올릴 글). TODO 6: "BACKLOG를 고친다"(311~337행: 나온 tasks와 함께 적기, 다시 나오면 tasks 더하기, 다시 나오지 않은 tasks가 셋이면 지우기, 처음 만들 때 문서 지도에 묻지 않고 행 더하기), 279행(BACKLOG에 있던 것이면 고치자고 제안). TODO 7: "비운다"(404~412행: `.gitkeep` 밖을 `git rm -r`, `<tasks 이름>: 비움` 커밋), 297·341행(고칠 것이 없거나 고침 task가 없으면 비운다로 감). TODO 8: "합친다"(414~423행: 비운 뒤 묻기, squash하지 않음, 충돌하면 `git merge --abort`하고 알림, 합치면 `git branch -d`). 이 phase 앞 커밋(`59d560b^`)의 "합친다" 절과 견주어 1~6의 절차가 그대로임을 봄. TODO 9: 10번(206~217행: 이름을 바꾼 phase, 회고가 통과한 task, 코드 평가의 등급과 게이트, 하네스 eval의 등급, 고침 task, 이슈와 댓글의 주소, `docs/BACKLOG.md`의 변경, 비운 커밋). 통과
- 완료 조건 2 가운데 run 본문의 몫이 참이다
  - `grep -n "작업" plugins/plate/skills/run/SKILL.md` → 출력 없음(exit 1). 통과

**문제**
- 없음

**판정**: 통과
