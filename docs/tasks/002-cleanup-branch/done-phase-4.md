# Phase 4: 회고 1의 문제를 고친다

**목표**: 회고 1에서 나온 문제를 모두 고친다.

**테스트 먼저**: 아니오 — 고칠 문제가 `.md` 맥락 문서(`docs/ARCHITECTURE.md`)의 글 하나뿐이라 코드 파일의 동작을 바꾸지 않는다.

**읽을 것**
- `docs/tasks/002-cleanup-branch/retro.md`의 `## 회고 1`부터 `## 회고 1`까지의 절
- `docs/ARCHITECTURE.md`
- `plugins/plate/skills/cleanup/SKILL.md`
- `plugins/plate/skills/run/SKILL.md`
- `docs/PRD.md`
- `docs/ADR.md`
- `docs/TOOLS.md`
- `docs/BACKLOG.md`
- `docs/cleanup/`

**TODO**
- [x] `docs/ARCHITECTURE.md` 54행 패턴과 규칙의 훅 문단이 "스킬마다의 푸시 규칙(phase, check, retro, review, eval, cleanup은 "푸시하지 않는다", run은 "PR을 연다"에서 승인받아 `tasks/<이름>`을 origin에 올릴 때만 푸시한다)"로 남아, 바뀐 cleanup 절대 규칙 3(고른 발견이 없을 때 승인받아 `cleanup/<보고서 이름>`을 푸시)과 run 절대 규칙 5(보낼 곳이 있으면 보낼 곳 브랜치를 푸시)와 어긋난다. 그 글을 바뀐 두 스킬의 절대 규칙과 맞게 고친다. 고칠 동작을 적은 맥락 문서와 README의 줄도 그 글과 맞춘다 (`docs/ARCHITECTURE.md`)

**통과 조건**
- 회고 1의 문제가 모두 고쳐졌다.
  - 확인: `docs/ARCHITECTURE.md`의 패턴과 규칙의 훅 문단에서 스킬마다의 푸시 규칙 글을 다시 읽어, cleanup이 고른 발견이 없을 때 승인받아 `cleanup/<보고서 이름>`을 푸시하는 것과 run이 보낼 곳이 있으면 보낼 곳 브랜치를 푸시하는 것이 `plugins/plate/skills/cleanup/SKILL.md`의 절대 규칙 3과 `plugins/plate/skills/run/SKILL.md`의 절대 규칙 5와 맞는다. `grep -n -F '"푸시하지 않는다"' docs/ARCHITECTURE.md`로 나온 줄에서 cleanup이 "푸시하지 않는다" 스킬 목록에 없다
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다

## 한 일
- `docs/ARCHITECTURE.md` 54행 훅 문단의 스킬마다의 푸시 규칙 글을 바뀐 cleanup·run 절대 규칙과 맞게 고친다: 괄호 글을 "phase, check, retro, review, eval은 "푸시하지 않는다", cleanup은 고른 발견이 없을 때 승인받아 `cleanup/<보고서 이름>`을 origin에 올릴 때만, run은 "PR을 연다"에서 승인받아 `tasks/<이름>`을, 보낼 곳이 있는 tasks면 그 tasks를 합친 보낼 곳 브랜치를 origin에 올릴 때만 푸시한다"로 바꿈 (`docs/ARCHITECTURE.md`). README 20행의 "끝의 PR과 합침은 늘 `tasks/<이름>`을 다루므로"가 보낼 곳이 있는 tasks와 어긋나, 보낼 곳 줄이 있으면 비운 뒤 `tasks/<이름>`을 그 브랜치에 로컬로 합칠지 묻고 합친 뒤 그 브랜치로 PR이나 합침을 묻는다는 글을 더하고 "그 밖의 끝의 PR과 합침은 `tasks/<이름>`을 다루므로"로 고침 (`README.md`)

## 확인 결과
- 회고 1의 문제가 모두 고쳐졌다.
  - `docs/ARCHITECTURE.md` 54행 훅 문단을 다시 읽음, `grep -n -F '"푸시하지 않는다"' docs/ARCHITECTURE.md` → 54행만 나오고 그 괄호 글의 "푸시하지 않는다" 목록은 phase, check, retro, review, eval. cleanup은 목록에 없고 "고른 발견이 없을 때 승인받아 `cleanup/<보고서 이름>`을 origin에 올릴 때만"이 cleanup 절대 규칙 3(18행)과, run의 "`tasks/<이름>`을, 보낼 곳이 있는 tasks면 그 tasks를 합친 보낼 곳 브랜치를"이 run 절대 규칙 5(20행)와 맞음. 통과
- task 머리의 완료 조건이 모두 참이다.
  - 1: `grep -n -F 'cleanup/<' plugins/plate/skills/cleanup/SKILL.md` → 17·18(절대 규칙), 115·127(5. 보고서를 쓰고 커밋한다), 149·153·154·155·161·163·165(고른 발견이 없을 때), 그 밖에 10·52. `grep -c -e '브랜치를 만들거나 바꾸지 않는다' -e '^3\. \*\*푸시하지 않는다' …cleanup/SKILL.md` → 0. 시험 레포(scratchpad의 `mktemp -d`, `main`에 빈 커밋 하나)에서 본문 5번의 이름 고르기(`git rev-parse --verify --quiet refs/heads/cleanup/<보고서 이름>` → 있으면 `-2`, `-3`)와 `git switch -c` → `main`에서 `cleanup/2026-10-29`가 `main` HEAD에서 생기고 `main` 그대로, `tasks/x`(커밋 하나 더)에서 `tasks/x` HEAD에서 생기고 `main` 그대로, 이미 있을 때 `cleanup/2026-10-29-2`가 생기고 옛 해시 그대로. 통과
  - 2: `grep -n '보낼 곳' plugins/plate/skills/plan/SKILL.md` → 19(절대 규칙 4), 55(1번), 139(7번), 170(양식), 244(적는 규칙), 26(낱말). 시험 레포 `cleanup/x`(`main`보다 커밋 하나 앞섬)에서 7번 차례대로 `git branch --show-current` → `cleanup/x`, `git rev-parse --verify --quiet refs/heads/tasks/fix` → 출력 없음 rc=1, `git switch -c tasks/fix` → `git merge-base --is-ancestor cleanup/x tasks/fix` 0, `main` 그대로. `tasks/old`를 만든 뒤 같은 명령 → 해시 rc=0이라 "이름과 번호"(238행, 아무것도 내지 않는 이름을 고른다)가 그 이름을 쓰지 않음을 본문에서 읽음. 통과
  - 3: `grep -n '보낼 곳' plugins/plate/skills/run/SKILL.md` → 20(절대 규칙 5), 69·71·73·75(0번), 499·505(비운다), 507~519(보낼 곳으로 합친다), 523(PR을 연다), 564(합친다). 시험 레포 `main` → `cleanup/x`(커밋 하나) → `tasks/y`(커밋 둘, 마지막 `y: 비움`): `git show HEAD^:docs/tasks/plan.md`에 `**보낼 곳**: cleanup/x`, `git rev-parse --verify --quiet refs/heads/cleanup/x` 해시, `git switch cleanup/x`, `git merge --no-ff -m 'y: 보낼 곳으로 합침' tasks/y` → `git merge-base --is-ancestor tasks/y cleanup/x` 0, `main` 그대로, `git branch -d tasks/y` 성공. 재개: `cleanup/x`에서 `git branch --show-current` → `cleanup/x`, `git log -1 --format=%s` → `y: 보낼 곳으로 합침`, `git show HEAD^2^:docs/tasks/plan.md` → 이름 `y`, 보낼 곳 `cleanup/x`라 73행의 "보낼 곳으로 합친 뒤의 재개"(PR·합침으로)에 듦. 보낼 곳 없음: `cleanup/x`를 지운 뒤 같은 확인 명령 → 출력 없음이라 1번에서 10번으로 가고 합치는 명령에 닿지 않음. 통과
  - 4: `grep -n -F 'cleanup/<' docs/PRD.md docs/ARCHITECTURE.md` → PRD 19(핵심 기능 9), ARCHITECTURE 32(디렉터리 구조 cleanup 줄), 54, 56(plan 문단), 95·98(데이터 흐름 정리 점검). `grep -n '보낼 곳' docs/PRD.md docs/ARCHITECTURE.md` → PRD 18(핵심 기능 8), ARCHITECTURE 54, 56(plan 문단), 57(run 문단), 65(데이터 흐름 계획), 81·84(tasks 끝). 통과
  - 5: `python3 -m unittest tests.test_cleanup_skill tests.test_skill_rules -v` → `OK`. 새 시험 `test_commits_only_on_cleanup_branch`, `CleanupBranchTest`의 넷, `PlanRulesTest.test_cleanup_branch_sends_back`, run의 보낼 곳 시험이 나옴. 통과
  - 6: `python3 -m unittest discover -s tests` → `Ran 263 tests`, `OK`. `grep -n '지난 tasks의 같은 이름' …plan/SKILL.md …retro/SKILL.md` → plan 115(6. 초안을 보여 주고 승인받는다), 266(적는 규칙), retro 79(4. task의 변경을 점검한다). 통과

## 계획과 달라진 점
- 없음

## 남은 것
- 시험 레포의 갈래 시험은 본문의 브랜치 명령을 옮겨 돌린 것이고, cleanup·plan·run을 헤드리스로 끝까지 돌리지 않았다(task 머리 범위 밖).

## 하네스에서 걸린 것
- 없음

## 확인 1

**통과 조건**
- 회고 1의 문제가 모두 고쳐졌다.
  - `docs/ARCHITECTURE.md` 54행 훅 문단의 푸시 규칙 괄호 글, `plugins/plate/skills/cleanup/SKILL.md` 18행(절대 규칙 3), `plugins/plate/skills/run/SKILL.md` 20행(절대 규칙 5)을 읽음, `grep -n -F '"푸시하지 않는다"' docs/ARCHITECTURE.md` → 54행만 나옴. "푸시하지 않는다" 목록은 phase, check, retro, review, eval이고 cleanup은 없다. cleanup은 "고른 발견이 없을 때 승인받아 `cleanup/<보고서 이름>`을 origin에 올릴 때만"으로 절대 규칙 3과, run은 "`tasks/<이름>`을, 보낼 곳이 있는 tasks면 그 tasks를 합친 보낼 곳 브랜치를"로 절대 규칙 5와 맞음. 통과
- task 머리의 완료 조건이 모두 참이다.
  - 1: `grep -n -F 'cleanup/<' plugins/plate/skills/cleanup/SKILL.md` → 17·18(절대 규칙), 115·127(5. 보고서를 쓰고 커밋한다), 149·153·154·155·161·163·165(고른 발견이 없을 때). `grep -n -e '브랜치를 만들거나 바꾸지 않는다' -e '^3\. \*\*푸시하지 않는다' plugins/plate/skills/cleanup/SKILL.md` → 출력 없음 rc=1. scratchpad의 `mktemp -d` 시험 레포(`main`, 빈 커밋 하나)에서 5번의 `git rev-parse --verify --quiet refs/heads/cleanup/<이름>`, `git switch -c`를 차례대로: `main`에서 → `cleanup/2026-10-29`가 `main` HEAD에서, `main` 그대로. `tasks/x`(커밋 하나 더)에서 → `tasks/x` HEAD에서, `main` 그대로. 이미 있을 때 → 첫 rev-parse가 해시를 내고 `-2`는 rc=1, `cleanup/2026-10-29-2`가 생기고 옛 해시 그대로. 통과
  - 2: `grep -n '보낼 곳' plugins/plate/skills/plan/SKILL.md` → 19(절대 규칙 4), 55(1번), 139(7번), 170(계획 파일의 양식), 244, 26. 시험 레포 `cleanup/x`(`main`보다 커밋 하나 앞섬)에서 `git branch --show-current` → `cleanup/x`, `git rev-parse --verify --quiet refs/heads/tasks/fix` → rc=1, `git switch -c tasks/fix` → `git merge-base --is-ancestor cleanup/x tasks/fix` 0, `main` 그대로. `tasks/old`가 있으면 같은 명령이 rc=0으로 무엇을 내고, 238행(이름과 번호)은 "아무것도 내지 않는" 이름을 고르라 하므로 그 이름을 쓰지 않음을 본문에서 읽음. 통과
  - 3: `grep -n '보낼 곳' plugins/plate/skills/run/SKILL.md` → 20(절대 규칙 5), 69·71·73·75(0번), 499·505(비운다), 523(PR을 연다), 564(합친다). 시험 레포 `main` → `cleanup/x`(커밋 하나) → `tasks/y`(커밋 둘, 마지막 `y: 비움`): `git show HEAD^:docs/tasks/plan.md` → `**보낼 곳**: cleanup/x`, `git rev-parse --verify --quiet refs/heads/cleanup/x` rc=0, `git switch cleanup/x`, `git merge --no-ff -m 'y: 보낼 곳으로 합침' tasks/y` → `git merge-base --is-ancestor tasks/y cleanup/x` 0, `main` 그대로, `git branch -d tasks/y` 성공. 재개: `git branch --show-current` → `cleanup/x`, `git log -1 --format=%s` → `y: 보낼 곳으로 합침`, `git show HEAD^2^:docs/tasks/plan.md` → 이름 `y`, 보낼 곳 `cleanup/x`라 73행(보낼 곳으로 합친 뒤의 재개 → PR을 연다/합친다)에 듦. 보낼 곳 없음: `cleanup/x`를 지운 뒤 같은 rev-parse → 출력 없음 rc=1이라 511행대로 10번으로 가고 합치는 명령에 닿지 않음. 통과
  - 4: `grep -n -F 'cleanup/<' docs/PRD.md docs/ARCHITECTURE.md` → PRD 19(핵심 기능 9), ARCHITECTURE 32(디렉터리 구조 cleanup 줄), 54, 56(plan 문단), 95·98(데이터 흐름 정리 점검). `grep -n '보낼 곳' docs/PRD.md docs/ARCHITECTURE.md` → PRD 18(핵심 기능 8), ARCHITECTURE 54, 56(plan 문단), 57(run 문단), 65(데이터 흐름 계획), 81·84(tasks 끝). 통과
  - 5: `python3 -m unittest tests.test_cleanup_skill tests.test_skill_rules -v` → `Ran 122 tests`, `OK`. `test_commits_only_on_cleanup_branch`, `CleanupBranchTest`의 넷, `PlanRulesTest.test_cleanup_branch_sends_back`, `RunRulesTest.test_send_to_*` 다섯이 나옴. 통과
  - 6: `python3 -m unittest discover -s tests` → `Ran 263 tests`, `OK`. `grep -n '지난 tasks의 같은 이름' plugins/plate/skills/plan/SKILL.md plugins/plate/skills/retro/SKILL.md` → plan 115(6. 초안을 보여 주고 승인받는다), 266(적는 규칙의 **조건**, 260행부터), retro 79(4. task의 변경을 점검한다). 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 263 tests`, `OK`. 통과

**남은 것**
- 시험 레포의 갈래 시험은 본문의 브랜치 명령을 옮겨 돌린 것이고, cleanup·plan·run을 헤드리스로 끝까지 돌리지 않았다 → 완료 조건 1·2·3의 `돌리지 않음` 줄(헤드리스로 끝까지 돌리지 않는다)이 돌리지 않기로 정한 동작의 돌려 보지 않은 위험. 하네스에서 걸린 것

**실패**
- 없음

**하네스에서 걸린 것**
- 남은 것: 시험 레포의 갈래 시험은 본문의 브랜치 명령을 옮겨 돌린 것이고, cleanup·plan·run을 헤드리스로 끝까지 돌리지 않았다(완료 조건 1·2·3의 `돌리지 않음` 줄).

**판정**: 통과
