# 회고

## 회고 1

**확인**
- 1. cleanup이 브랜치를 이렇게 다룬다(절대 규칙, 보고서를 쓰기 전, 고른 발견이 없을 때)
  - `grep -n -F 'cleanup/<' plugins/plate/skills/cleanup/SKILL.md` → 17·18행(절대 규칙), 115·127행(5. 보고서를 쓰고 커밋한다), 149·153·154·155·161·163·165행(고른 발견이 없을 때), 그 밖에 10·52행. 통과
  - `grep -n -e '브랜치를 만들거나 바꾸지 않는다' -e '^3\. \*\*푸시하지 않는다' plugins/plate/skills/cleanup/SKILL.md` → 출력 없음(rc=1). 절대 규칙 절에서 아무것도 나오지 않음. 통과
  - `mktemp -d` 시험 레포(기본 브랜치 `main`, 빈 커밋 하나)에서 본문 5번의 명령(`git rev-parse --verify --quiet refs/heads/cleanup/<보고서 이름>` → 있으면 `-2`, `-3`을 같은 명령으로 봄 → `git switch -c {고른 이름}`)을 차례대로 돌림 → `main`에서: `cleanup/2026-10-29`가 `main`의 HEAD에서 생기고 `main` 해시 그대로. `tasks/x`(커밋 하나 더)에서: `cleanup/2026-10-29`가 `tasks/x`의 HEAD에서 생기고 `main` 그대로. `cleanup/2026-10-29`가 이미 있을 때: `cleanup/2026-10-29-2`가 생기고 옛 브랜치 해시 그대로. 통과
  - 돌리지 않음 줄: cleanup을 헤드리스로 끝까지 돌리지 않는다(완료 조건이 정한 대로). 해당 없음
- 2. plan이 `cleanup/…`에서 이렇게 한다(1번, 7번, 양식과 적는 규칙, 절대 규칙 4, 다른 갈래는 그대로)
  - `grep -n '보낼 곳' plugins/plate/skills/plan/SKILL.md` → 19(절대 규칙 4), 26(낱말), 55(1번), 139(7번), 170(계획 파일의 양식), 244(적는 규칙). 통과
  - `mktemp -d` 시험 레포의 `cleanup/x`(`main`보다 커밋 하나 앞섬)에서 본문 7번 차례대로 `git branch --show-current` → `cleanup/x`, `git rev-parse --verify --quiet refs/heads/tasks/fix` → 출력 없음(rc=1), `git switch -c tasks/fix` → `git merge-base --is-ancestor cleanup/x tasks/fix` 0, `git rev-parse main` 전과 같음. 통과
  - 같은 레포에 `tasks/old`를 만든 뒤 `git rev-parse --verify --quiet refs/heads/tasks/old` → 해시(rc=0). 본문 238행 "이름과 번호"는 새 tasks의 이름을 이 명령이 "아무것도 내지 않는" 것으로 고르므로 그 이름을 쓰지 않는다. 통과
  - 돌리지 않음 줄: plan을 헤드리스로 끝까지 돌리지 않는다. 해당 없음
- 3. run이 tasks 머리의 `**보낼 곳**:` 줄을 이렇게 다룬다(비운 뒤, PR이나 합침, 보낼 곳이 없을 때, 재개, 절대 규칙 5, 그 줄이 없는 tasks)
  - `grep -n '보낼 곳' plugins/plate/skills/run/SKILL.md` → 20(절대 규칙 5), 25·26(낱말), 69·71·73·75(0. tasks를 본다), 499·505(비운다), 507~519(보낼 곳으로 합친다), 523(PR을 연다), 564(합친다). 통과
  - 합칠 때: `mktemp -d` 레포에 `main` → `cleanup/x`(커밋 `c1`) → `tasks/y`(`y: plan`에 `**보낼 곳**: cleanup/x`가 든 plan.md, `y: 비움`)를 두고 `git rev-parse --verify --quiet refs/heads/cleanup/x`(rc=0) → `git switch cleanup/x` → `git merge --no-ff -m 'y: 보낼 곳으로 합침' tasks/y` → `git merge-base --is-ancestor tasks/y cleanup/x` 0, `git branch -d tasks/y`, `main` 해시 그대로. 통과
  - 보낼 곳이 없을 때: `cleanup/x`가 없는 새 레포에서 `git rev-parse --verify --quiet refs/heads/cleanup/x` → 출력 없음(rc=1). 본문 "보낼 곳으로 합친다" 1번대로 알리고 10번으로 가 `git switch`·`git merge`에 닿지 않음. 브랜치는 `main`, `tasks/y` 그대로. 통과
  - 재개할 때: 합치기 전 `tasks/y`에서 `git branch --show-current` → `tasks/y`, `git log -1 --format=%s` → `y: 비움`, `git show HEAD^:docs/tasks/plan.md`에 `**보낼 곳**: cleanup/x` → "보낼 곳으로 합친다"로 감. 합친 뒤 `cleanup/x`에서 `cleanup/x`, `y: 보낼 곳으로 합침`, `git show HEAD^2^:docs/tasks/plan.md` → `**이름**: y`, `**보낼 곳**: cleanup/x` → 0번의 "보낼 곳으로 합친 뒤의 재개"로 "PR을 연다"/"합친다"로 감. 통과
  - 돌리지 않음 줄: run을 헤드리스로 끝까지 돌리지 않는다. 해당 없음
- 4. 맥락 문서가 바뀐 동작과 맞다
  - `grep -n -F 'cleanup/<' docs/PRD.md docs/ARCHITECTURE.md` → PRD 19(핵심 기능 9), ARCHITECTURE 32(디렉터리 구조 cleanup 줄), 56(plan 문단), 95·98(데이터 흐름 정리 점검). 통과
  - `grep -n '보낼 곳' docs/PRD.md docs/ARCHITECTURE.md` → PRD 18(핵심 기능 8), ARCHITECTURE 56(plan 문단), 57(run 문단), 65(데이터 흐름 계획), 81·84(데이터 흐름 tasks 끝). 통과
- 5. 바뀐 글을 지키는 테스트가 있고, 옛 글을 지키던 테스트가 새 글을 지킨다
  - `python3 -m unittest tests.test_cleanup_skill tests.test_skill_rules -v` → `Ran 122 tests`, `OK`. `test_core_rules_present`, `test_commits_on_tasks_branch` ok, 새 시험 `test_commits_only_on_cleanup_branch`, `CleanupBranchTest`의 넷, `test_cleanup_branch_sends_back`, `test_send_to_*` 다섯이 나옴. 통과
- 6. 테스트 묶음이 모두 통과하고, 001이 고친 plan·retro 규칙이 그대로다
  - `python3 -m unittest discover -s tests` → `Ran 263 tests`, 마지막 줄 `OK`. 통과
  - `grep -n '지난 tasks의 같은 이름' plugins/plate/skills/plan/SKILL.md plugins/plate/skills/retro/SKILL.md` → plan 115(6. 초안을 보여 주고 승인받는다), 266(적는 규칙의 **조건**), retro 79(4. task의 변경을 점검한다). 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 263 tests`, `OK`. 통과

**남은 것**
- phase 1: `docs/ARCHITECTURE.md` 54행(패턴과 규칙의 훅 문단)의 cleanup "푸시하지 않는다"가 맞지 않는다 → 문제 (맥락 문서: 바뀐 cleanup 절대 규칙 3과 어긋남. 같은 줄의 run "`tasks/<이름>`을 origin에 올릴 때만 푸시한다"도 바뀐 run 절대 규칙 5와 어긋남)
- phase 1: 시험 레포의 갈래 시험은 본문 명령을 옮겨 돌린 것이고 cleanup을 헤드리스로 끝까지 돌리지 않았다 → 문제 아님 (task 머리 범위 밖 "cleanup, plan, run을 헤드리스로 끝까지 돌리는 것")
- phase 1: "고른 발견이 없을 때"의 합침에서 커밋하지 않은 변경이 있어도 묻지 않는다 → 문제 아님 (절대 규칙 4가 묻는 자리를 6번과 PR·합침 물음 둘로 정했고, 본문 2번이 변경을 건드리지 않고 `git switch`가 겹치면 실패해 합치지 않는다. 결정이 정한 것과 어긋나지 않음)
- phase 2: 더하는 경우에 cleanup 브랜치에서 부르면 7번에서 그 tasks의 `tasks/<이름>`으로 바꾸고 보낼 곳은 고치지 않는다 → 문제 아님 (경계 밖: 결정과 목표는 cleanup 브랜치에서 갈라진 새 tasks만 다룬다. 이때 cleanup 브랜치의 보고서 커밋이 어느 PR·합침에도 실리지 않는 꼴을 `FRICTION.md`에 경계 밖으로 적음)
- phase 2: ARCHITECTURE plan 문단의 이유에 적은 run의 보낼 곳 합침은 phase 3이 만든다 → 문제 아님 (phase 3이 run 본문에 "보낼 곳으로 합친다"를 더해 지금은 맞음)
- phase 2: 양식의 `**보낼 곳**:` 줄이 이름 줄 바로 아래라 마크다운으로 그리면 한 문단으로 이어 보인다 → 문제 아님 (run 0번과 낱말이 줄 단위로 읽어 동작에 걸리지 않고, 보이는 꼴은 취향에 든다)
- phase 3: 고친 run 본문을 헤드리스로 끝까지 돌리지 않았다 → 문제 아님 (task 머리 범위 밖)
- phase 3: 보낼 곳으로 합친 뒤 사람이 그 브랜치에 커밋을 더하면 0번이 재개로 보지 않는다 → 문제 아님 (결정은 합친 뒤 끊겼을 때의 재개만 정했고, `tasks/<이름>`의 `<이름>: 비움` 재개와 같은 판정이다. 사람이 커밋을 더한 브랜치는 사람이 보낸다)
- phase 3: 충돌로 `git merge --abort` 뒤 `git switch tasks/<이름>`이 실패하는 갈래가 본문에 없다 → 문제 아님 (되돌린 뒤 작업 트리는 4번에서 바꿀 수 있었던 상태 그대로라 돌아가는 바꿈이 실패할 길을 이 task의 커밋에서 찾지 못함)

**문제**
- `docs/ARCHITECTURE.md` 54행 패턴과 규칙의 훅 문단이 "스킬마다의 푸시 규칙(phase, check, retro, review, eval, cleanup은 "푸시하지 않는다", run은 "PR을 연다"에서 승인받아 `tasks/<이름>`을 origin에 올릴 때만 푸시한다)"로 남아, 바뀐 cleanup 절대 규칙 3(고른 발견이 없을 때 승인받아 `cleanup/<보고서 이름>`을 푸시)과 run 절대 규칙 5(보낼 곳이 있으면 보낼 곳 브랜치를 푸시)와 어긋난다 (`docs/ARCHITECTURE.md`). 기준: 맥락 문서. 고칠 쪽: 문서 (tasks 머리의 목표 "바뀐 동작은 맥락 문서와 맞춘다"와 결정 1·2·3)

**판정**: 문제 있음

## 회고 2

**확인**
- 1. cleanup이 브랜치를 이렇게 다룬다(절대 규칙, 보고서를 쓰기 전, 고른 발견이 없을 때)
  - `grep -n -F 'cleanup/<' plugins/plate/skills/cleanup/SKILL.md` → 17·18행(절대 규칙), 115·127행(5. 보고서를 쓰고 커밋한다), 149·153·154·155·161·163·165행(고른 발견이 없을 때), 그 밖에 10·52행. 통과
  - `grep -n -e '브랜치를 만들거나 바꾸지 않는다' -e '^3\. \*\*푸시하지 않는다' plugins/plate/skills/cleanup/SKILL.md` → 출력 없음(rc=1). 통과
  - `mktemp -d` 시험 레포(`main`, 빈 커밋 하나)에서 본문 5번의 이름 고르기(`git rev-parse --verify --quiet refs/heads/cleanup/<보고서 이름>`, 있으면 `-2`, `-3`)와 `git switch -c {고른 이름}`을 차례대로 돌림 → `main`에서: `cleanup/2026-10-29`가 `main`의 HEAD에서 생기고 `main` 해시 그대로. `tasks/x`(커밋 하나 더)에서: `cleanup/2026-10-29`가 `tasks/x`의 HEAD에서 생기고 `main` 그대로. 이미 있을 때: `cleanup/2026-10-29-2`가 생기고 옛 브랜치 해시 그대로. 통과
  - 돌리지 않음 줄: cleanup을 헤드리스로 끝까지 돌리지 않는다(완료 조건이 정한 대로). 해당 없음
- 2. plan이 `cleanup/…`에서 이렇게 한다(1번, 7번, 양식과 적는 규칙, 절대 규칙 4, 다른 갈래는 그대로)
  - `grep -n '보낼 곳' plugins/plate/skills/plan/SKILL.md` → 19(절대 규칙 4), 26(낱말), 55(1번), 139(7번), 170(계획 파일의 양식), 244(적는 규칙). 통과
  - `mktemp -d` 시험 레포의 `cleanup/x`(`main`보다 커밋 하나 앞섬)에서 7번 차례대로 `git branch --show-current` → `cleanup/x`, `git rev-parse --verify --quiet refs/heads/tasks/fix` → 출력 없음(rc=1), `git switch -c tasks/fix` → `git merge-base --is-ancestor cleanup/x tasks/fix` 0, `main` 해시 그대로. 통과
  - 같은 레포에 `tasks/old`를 만든 뒤 `git rev-parse --verify --quiet refs/heads/tasks/old` → 해시(rc=0). 본문 237행 "이름과 번호"는 이 명령이 아무것도 내지 않는 이름을 고르라 하므로 그 이름을 쓰지 않음을 읽음. 통과
  - 돌리지 않음 줄: plan을 헤드리스로 끝까지 돌리지 않는다. 해당 없음
- 3. run이 tasks 머리의 `**보낼 곳**:` 줄을 이렇게 다룬다(비운 뒤, PR이나 합침, 보낼 곳이 없을 때, 재개, 절대 규칙 5, 그 줄이 없는 tasks)
  - `grep -n '보낼 곳' plugins/plate/skills/run/SKILL.md` → 20(절대 규칙 5), 25·26(낱말), 69·71·73·75(0. tasks를 본다), 282(10번), 499·505(비운다), 507~519(보낼 곳으로 합친다), 523(PR을 연다), 564(합친다). 통과
  - 합칠 때: `mktemp -d` 레포에 `main` → `cleanup/x`(커밋 `c1`) → `tasks/y`(`y: plan`에 `**보낼 곳**: cleanup/x`가 든 plan.md, `y: 비움`)를 두고 `git rev-parse --verify --quiet refs/heads/cleanup/x`(rc=0) → `git switch cleanup/x` → `git merge --no-ff -m 'y: 보낼 곳으로 합침' tasks/y` → `git merge-base --is-ancestor tasks/y cleanup/x` 0, `main` 해시 그대로, `git branch -d tasks/y` 성공. 통과
  - 보낼 곳이 없을 때: `cleanup/x`를 지운 뒤 `git rev-parse --verify --quiet refs/heads/cleanup/x` → 출력 없음(rc=1). 본문 511행대로 알리고 10번으로 가 `git switch`·`git merge`에 닿지 않음. 통과
  - 재개할 때: 합치기 전 `tasks/y`에서 `git branch --show-current` → `tasks/y`, `git log -1 --format=%s` → `y: 비움`, `git show HEAD^:docs/tasks/plan.md`에 `**보낼 곳**: cleanup/x` → 71행대로 "보낼 곳으로 합친다"로 감. 합친 뒤 `cleanup/x`에서 `cleanup/x`, `y: 보낼 곳으로 합침`, `git show HEAD^2^:docs/tasks/plan.md` → `**이름**: y`, `**보낼 곳**: cleanup/x` → 73행의 보낼 곳으로 합친 뒤의 재개로 "PR을 연다"/"합친다"로 감. 통과
  - 돌리지 않음 줄: run을 헤드리스로 끝까지 돌리지 않는다. 해당 없음
- 4. 맥락 문서가 바뀐 동작과 맞다
  - `grep -n -F 'cleanup/<' docs/PRD.md docs/ARCHITECTURE.md` → PRD 19(핵심 기능 9), ARCHITECTURE 32(디렉터리 구조 cleanup 줄), 54(패턴과 규칙의 훅 문단), 56(plan 문단), 95·98(데이터 흐름 정리 점검). 통과
  - `grep -n '보낼 곳' docs/PRD.md docs/ARCHITECTURE.md` → PRD 18(핵심 기능 8), ARCHITECTURE 54(훅 문단), 56(plan 문단), 57(run 문단), 65(데이터 흐름 계획), 81·84(데이터 흐름 tasks 끝). 통과
- 5. 바뀐 글을 지키는 테스트가 있고, 옛 글을 지키던 테스트가 새 글을 지킨다
  - `python3 -m unittest tests.test_cleanup_skill tests.test_skill_rules -v` → `Ran 122 tests`, `OK`. `test_core_rules_present`, `test_commits_on_tasks_branch` ok, 새 시험 `test_commits_only_on_cleanup_branch`, `CleanupBranchTest`의 넷, `PlanRulesTest.test_cleanup_branch_sends_back`, `RunRulesTest.test_send_to_*` 다섯이 나옴. 통과
- 6. 테스트 묶음이 모두 통과하고, 001이 고친 plan·retro 규칙이 그대로다
  - `python3 -m unittest discover -s tests` → `Ran 263 tests`, 마지막 줄 `OK`. 통과
  - `grep -n '지난 tasks의 같은 이름' plugins/plate/skills/plan/SKILL.md plugins/plate/skills/retro/SKILL.md` → plan 115(6. 초안을 보여 주고 승인받는다), 266(적는 규칙의 **조건**), retro 79(4. task의 변경을 점검한다). 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 263 tests`, `OK`. 통과

**남은 것**
- phase 1: `docs/ARCHITECTURE.md` 54행(패턴과 규칙의 훅 문단)의 cleanup "푸시하지 않는다"가 맞지 않는다 → 문제 아님 (phase 4(`54801ec`)가 그 괄호 글을 "phase, check, retro, review, eval은 "푸시하지 않는다", cleanup은 고른 발견이 없을 때 승인받아 `cleanup/<보고서 이름>`을…, run은 … 보낼 곳이 있는 tasks면 그 tasks를 합친 보낼 곳 브랜치를 origin에 올릴 때만"으로 고쳐 cleanup 절대 규칙 3(18행), run 절대 규칙 5(20행)와 맞음을 읽음. `grep -n -F '"푸시하지 않는다"' docs/ARCHITECTURE.md`는 54행만 내고 그 목록에 cleanup이 없다)
- phase 1: 시험 레포의 갈래 시험은 본문 명령을 옮겨 돌린 것이고 cleanup을 헤드리스로 끝까지 돌리지 않았다 → 문제 아님 (task 머리 범위 밖 "cleanup, plan, run을 헤드리스로 끝까지 돌리는 것")
- phase 1: "고른 발견이 없을 때"의 합침에서 커밋하지 않은 변경이 있어도 묻지 않는다 → 문제 아님 (절대 규칙 4가 묻는 자리를 6번과 PR·합침 물음 둘로 정했고, `git switch`가 겹치면 실패해 합치지 않는다)
- phase 2: 더하는 경우에 cleanup 브랜치에서 부르면 7번에서 그 tasks의 `tasks/<이름>`으로 바꾸고 보낼 곳은 고치지 않는다 → 문제 아님 (경계 밖: 결정과 목표는 cleanup 브랜치에서 갈라진 새 tasks만 다룬다. 회고 1이 `FRICTION.md`에 경계 밖으로 적어 두었다)
- phase 2: ARCHITECTURE plan 문단의 이유에 적은 run의 보낼 곳 합침은 phase 3이 만든다 → 문제 아님 (run 본문 507행 "보낼 곳으로 합친다"가 있어 맞음)
- phase 2: 양식의 `**보낼 곳**:` 줄이 이름 줄 바로 아래라 마크다운으로 그리면 한 문단으로 이어 보인다 → 문제 아님 (run 0번과 낱말이 줄 단위로 읽어 동작에 걸리지 않고, 보이는 꼴은 취향에 든다)
- phase 3: 고친 run 본문을 헤드리스로 끝까지 돌리지 않았다 → 문제 아님 (task 머리 범위 밖)
- phase 3: 보낼 곳으로 합친 뒤 사람이 그 브랜치에 커밋을 더하면 0번이 재개로 보지 않는다 → 문제 아님 (결정은 합친 뒤 끊겼을 때의 재개만 정했고, `<이름>: 비움` 재개와 같은 판정이다)
- phase 3: 충돌로 `git merge --abort` 뒤 `git switch tasks/<이름>`이 실패하는 갈래가 본문에 없다 → 문제 아님 (되돌린 뒤 작업 트리는 4번에서 바꿀 수 있었던 상태 그대로라 돌아가는 바꿈이 실패할 길을 task의 커밋에서 찾지 못함)
- phase 4: 시험 레포의 갈래 시험은 본문의 브랜치 명령을 옮겨 돌린 것이고, cleanup·plan·run을 헤드리스로 끝까지 돌리지 않았다 → 문제 아님 (task 머리 범위 밖 "cleanup, plan, run을 헤드리스로 끝까지 돌리는 것")

**문제**
- 없음

**판정**: 통과
