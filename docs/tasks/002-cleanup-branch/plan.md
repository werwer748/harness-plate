# cleanup, plan, run이 cleanup 브랜치에서 일한다

## 목표
cleanup은 어느 브랜치에서 부르든 그 HEAD에서 `cleanup/<보고서 이름>`을 만들어 거기서만 커밋하고, 고른 발견이 없으면 그 브랜치의 PR이나 합침을 묻는다. plan은 `cleanup/…`에서 묻지 않고 `tasks/<이름>`을 갈라 tasks 머리에 `**보낼 곳**:` 줄을 적는다. run은 끝에서 그 tasks를 보낼 곳에 로컬로 합친 뒤, 그 브랜치로 기본 브랜치에 가는 PR이나 합침을 묻는다. 바뀐 동작은 PRD와 ARCHITECTURE에 맞춘다.

## 범위 밖
- setup과 context의 브랜치(커밋하지 않는다).
- run 1번의 "로컬 기본 브랜치의 앞선 커밋을 되돌릴지" 물음을 지우는 것.
- cleanup, plan, run을 헤드리스로 끝까지 돌리는 것.

## 완료 조건
1. cleanup이 브랜치를 이렇게 다룬다.
   - 절대 규칙: 보고서와 미룸은 `cleanup/<보고서 이름>`에만 커밋하고, 푸시는 고른 발견이 없을 때 승인받아 그 브랜치를 origin에 올릴 때만 한다. 묻는 자리는 6번과 그 PR·합침 물음이다.
   - 보고서를 쓰기 전: 지금 브랜치의 HEAD에서 그 브랜치를 묻지 않고 만들어 바꾼다. 같은 이름의 로컬 브랜치가 있으면 보고서 번호처럼 없는 번호를 붙인다.
   - 고른 발견이 없을 때: origin이 GitHub이면 그 브랜치를 푸시해 기본 브랜치로 가는 PR(본문은 보고서 파일)을 열지 묻는다. 그 밖이면 기본 브랜치에 합칠지 묻는다. 제목은 작은따옴표로, 본문은 `--body-file`로 넘긴다.
   - 확인: `grep -n -F 'cleanup/<' plugins/plate/skills/cleanup/SKILL.md` → 절대 규칙, 보고서를 쓰고 커밋하는 절, 고른 발견이 없을 때의 절에 저마다 한 줄 이상
   - 확인: `grep -n -e '브랜치를 만들거나 바꾸지 않는다' -e '^3\. \*\*푸시하지 않는다' plugins/plate/skills/cleanup/SKILL.md` → 절대 규칙 절에서는 아무것도 나오지 않음. 1·2라운드에 맡기는 글의 줄만 나와도 된다
   - 확인: `mktemp -d` 시험 레포(기본 브랜치 `main`, 커밋 하나)에서 본문의 브랜치 명령을 적힌 차례대로 세 갈래로 돌린다. 기대는 갈래마다 다음과 같다.
     - `main`에서 돌리면: 새 `cleanup/…`가 `main`의 HEAD에서 생긴다. `git rev-parse main`은 전과 같다.
     - `tasks/x`(커밋 하나 더)에서 돌리면: 새 `cleanup/…`가 `tasks/x`의 HEAD에서 생긴다. `main`은 전과 같다.
     - 같은 이름의 `cleanup/…`가 이미 있을 때 돌리면: 번호를 붙인 새 이름의 브랜치가 생기고, 옛 브랜치의 해시는 그대로다.
   - 돌리지 않음: cleanup은 에이전트 열두 개를 띄우고 묻는 스킬이고 PR은 GitHub이 있어야 해 헤드리스로 끝까지 돌리지 않는다
2. plan이 `cleanup/…`에서 이렇게 한다.
   - 1번: `cleanup/…`이면 묻지 않고 2번으로 간다.
   - 7번: `cleanup/…`의 HEAD에서 `git switch -c tasks/<이름>`으로 만든다.
   - 양식과 적는 규칙: tasks 머리의 이름 줄 아래에 `**보낼 곳**: {그 cleanup 브랜치}` 줄을 적는다. `cleanup/…`에서 갈랐을 때만 적는다.
   - 절대 규칙 4: `cleanup/…`도 묻지 않는 브랜치에 든다.
   - 기본 브랜치, `tasks/<이름>`, 그 밖의 브랜치에서는 지금과 같다.
   - 확인: `grep -n '보낼 곳' plugins/plate/skills/plan/SKILL.md` → 절대 규칙, 1번, 7번, 계획 파일의 양식에 저마다 한 줄 이상
   - 확인: `mktemp -d` 시험 레포의 `cleanup/x`(`main`보다 커밋 하나 앞섬)에서 본문 7번의 브랜치 명령을 적힌 차례대로 돌린다. 기대: `git merge-base --is-ancestor cleanup/x tasks/<이름>`이 0이고 `git rev-parse main`이 전과 같다
   - 확인: 같은 레포에 로컬 `tasks/<이름>`이 이미 있을 때, 본문 "이름과 번호"의 이름 고르기(`git rev-parse --verify --quiet refs/heads/tasks/<이름>`)가 그 이름을 쓰지 않게 하는지 본문에서 읽는다
   - 돌리지 않음: plan은 초안마다 사용자에게 묻는 스킬이라 헤드리스로 끝까지 돌리지 않는다
3. run이 tasks 머리의 `**보낼 곳**:` 줄을 이렇게 다룬다.
   - 비운 뒤: 그 줄이 있으면 `tasks/<이름>`을 그 브랜치에 로컬로 합칠지 묻는다. squash하지 않고, 합치면 `tasks/<이름>`을 지운다.
   - 합친 뒤 PR이나 합침: origin이 GitHub이면 그 브랜치를 푸시해 기본 브랜치로 가는 PR을 열지 묻고, plate 워크플로가 없으면 평가 절을 댓글로 단다. 그 밖이면 그 브랜치를 기본 브랜치에 합칠지 묻는다.
   - 보낼 곳이 로컬에 없을 때(`git rev-parse --verify --quiet refs/heads/{보낼 곳}`이 아무것도 내지 않음): 합치지도 PR을 열지도 않고 알리고 10번으로 간다.
   - 비운 뒤 재개: 0번이 `tasks/<이름>`에서 비운 뒤면 보낼 곳으로 합치는 자리로 간다. 보낼 곳 브랜치에서 그 tasks를 합친 뒤면 PR·합침으로 간다.
   - 절대 규칙 5: 푸시하는 브랜치에 보낼 곳이 든다.
   - 그 줄이 없는 tasks는 지금과 같다.
   - 확인: `grep -n '보낼 곳' plugins/plate/skills/run/SKILL.md` → 절대 규칙, 0번, "비운다", "PR을 연다", "합친다"에 저마다 한 줄 이상
   - 확인: `mktemp -d` 시험 레포에서 본문의 명령을 적힌 차례대로 세 갈래로 돌린다.
     - 합칠 때: `main` → `cleanup/x`(커밋 하나) → `tasks/y`(커밋 둘, 마지막 제목 `y: 비움`)를 두고 합치는 명령을 돌린다. 기대: `git merge-base --is-ancestor tasks/y cleanup/x`가 0이고, `main`의 해시가 그대로다.
     - 보낼 곳이 없을 때: `cleanup/x`를 지운 레포에서 있는지 보는 명령이 아무것도 내지 않는다. 기대: 그 갈래가 합치는 명령에 닿지 않는다.
     - 재개할 때: 합친 뒤의 `cleanup/x`에서 0번의 재개 판정에 쓰는 명령(브랜치, 마지막 커밋 제목)을 돌린다. 기대: 본문이 정한 PR·합침 자리로 가는 값이 나온다.
   - 돌리지 않음: run은 에이전트를 띄우고 묻는 스킬이고 PR은 GitHub이 있어야 해 헤드리스로 끝까지 돌리지 않는다
4. 맥락 문서가 바뀐 동작과 맞다.
   - PRD 핵심 기능 9: cleanup 브랜치와 고른 발견이 없을 때의 PR·합침
   - PRD 핵심 기능 8: 보낼 곳이 있는 tasks의 끝
   - ARCHITECTURE의 디렉터리 구조: cleanup 줄
   - ARCHITECTURE의 패턴과 규칙: plan 문단(`cleanup/…`에서 묻지 않고 보낼 곳을 적는다), run 문단(보낼 곳으로 합친 뒤 PR·합침, 보낼 곳이 없을 때, 재개)
   - ARCHITECTURE의 데이터 흐름: 계획, tasks 끝, 정리 점검
   - 확인: `grep -n -F 'cleanup/<' docs/PRD.md docs/ARCHITECTURE.md` → PRD 핵심 기능 9, ARCHITECTURE의 디렉터리 구조 cleanup 줄, plan 문단, 데이터 흐름의 정리 점검에 저마다 한 줄 이상
   - 확인: `grep -n '보낼 곳' docs/PRD.md docs/ARCHITECTURE.md` → PRD 핵심 기능 8, ARCHITECTURE의 plan 문단, run 문단, 데이터 흐름의 계획과 tasks 끝에 저마다 한 줄 이상
5. 바뀐 글을 지키는 테스트가 있고, 옛 글을 지키던 테스트가 새 글을 지킨다.
   - 고칠 옛 시험: `tests/test_cleanup_skill.py`의 `AbsoluteRulesTest.test_core_rules_present`(규칙 3의 "푸시하지 않는다"), `tests/test_skill_rules.py`의 `PlanRulesTest.test_commits_on_tasks_branch`(절대 규칙 4와 1번의 브랜치 글)
   - 확인: `python3 -m unittest tests.test_cleanup_skill tests.test_skill_rules -v` → `OK`. cleanup 브랜치, plan의 보낼 곳, run의 보낼 곳을 보는 새 시험 이름이 나온다
6. 테스트 묶음이 모두 통과하고(tasks 완료 조건 1), 001이 고친 plan·retro 규칙이 그대로다(tasks 완료 조건 2).
   - 확인: `python3 -m unittest discover -s tests` → 마지막 줄이 `OK`
   - 확인: `grep -n '지난 tasks의 같은 이름' plugins/plate/skills/plan/SKILL.md plugins/plate/skills/retro/SKILL.md` → plan의 "6. 초안을 보여 주고 승인받는다"와 "적는 규칙"의 **조건**, retro의 "4. task의 변경을 점검한다"에 저마다 한 줄 이상

## 결정
- cleanup은 어느 브랜치에서 부르든 그 HEAD에서 `cleanup/<보고서 이름>`을 묻지 않고 만들어, 거기에 보고서와 미룸을 커밋한다. 이유: 작업의 종류를 불문하고 main에서 작업이 이루어지는 경우를 방지해야 하고, 작업 중인 브랜치에서 바로 점검하고 싶을 때가 있다.
- plan은 `cleanup/…`에서 묻지 않고 그 HEAD에서 `tasks/<이름>`을 만들고 tasks 머리에 `**보낼 곳**:` 줄을 적는다. run은 끝에서 그 tasks를 보낼 곳에 로컬로 합친 뒤, 그 브랜치로 기본 브랜치에 가는 PR 하나(GitHub이 아니면 합침 하나)를 묻는다. 이유: 사용자가 cleanup 브랜치까지를 cleanup 작업의 완료로 보고 최종 PR이나 머지를 정하기로 했고, PR과 CI 평가는 기본 브랜치로 가는 하나뿐이다.
- 고른 발견이 없으면 cleanup이 그 자리에서 PR이나 합침을 묻는다. PR의 본문은 그 보고서 파일이다. 이유: run의 끝과 같은 모양으로 cleanup 작업이 끝난다. 본문은 추천안으로 정함
- 보낼 곳 브랜치가 로컬에 없으면 run은 합치지도 PR을 열지도 않고 알린 뒤 보고로 끝난다. 이유: 사람이 정한 뒤 다시 부르면 비운 뒤 재개로 같은 자리부터 잇는다.
- 이 task의 phase는 스킬 본문을 run이 넘긴 판으로 수행하고 확인한다. 고친 본문의 동작은 본문의 명령을 시험 저장소에서 돌려 본다. 이유: AGENTS.md의 작업 규칙과 `docs/TOOLS.md`의 "세션 도중의 스킬 본문 고침" (추천안으로 정함)
