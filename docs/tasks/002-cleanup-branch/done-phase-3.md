# Phase 3: run이 보낼 곳으로 합친 뒤 PR이나 합침을 묻는다

**목표**: run이 tasks 머리의 `**보낼 곳**:` 줄대로 tasks를 그 브랜치에 합치고 그 브랜치의 PR이나 합침을 묻는다. 그 동작이 PRD, ARCHITECTURE, 테스트에 맞는다.

**테스트 먼저**: 아니오 — 스킬 본문(`.md`)과 그 글을 지키는 테스트, 맥락 문서만 고친다

**읽을 것**
- `plugins/plate/skills/run/SKILL.md`의 절대 규칙 5, 낱말의 "tasks 머리", "0. tasks를 본다", "tasks 끝"의 "비운다", "PR을 연다", "PR 본문의 꼴", "합친다", "10. 보고한다"
- `plugins/plate/skills/plan/SKILL.md`의 "계획 파일의 양식"의 tasks 머리 (phase 2가 더한 `**보낼 곳**:` 줄)
- `tests/test_skill_rules.py`의 `RunRulesTest` (0번 재개, PR, 합친다를 보는 시험)
- `docs/PRD.md`의 핵심 기능 8
- `docs/ARCHITECTURE.md`의 패턴과 규칙의 run 문단("run은 기본 브랜치(`origin`의 HEAD"로 시작하는 줄), 데이터 흐름의 "tasks 끝"
- `docs/ADR.md`, `docs/TOOLS.md`, `docs/BACKLOG.md`

**TODO**
- [x] 앞 phase의 산출물에 대어 조건을 맞춘다. phase 2가 고친 plan 양식에서 `**보낼 곳**:` 줄의 꼴과 자리를 읽고, run이 읽는 꼴을 그것과 같게 둔다 (`plugins/plate/skills/run/SKILL.md`)
- [x] "비운다" 뒤에 보낼 곳이 있으면 거기로 합치는 자리가 더해진다.
  - 보낼 곳은 비우기 전에 tasks 머리에서 읽어 둔다.
  - `tasks/<이름>`을 그 브랜치에 로컬로 합칠지 묻는다. squash하지 않고, 충돌하면 되돌리고, 합치면 `tasks/<이름>`을 지운다.
  - 합친 뒤 origin이 GitHub이면 "PR을 연다"를 그 브랜치를 머리로 해서 돈다. 그 밖이면 "합친다"를 그 브랜치를 합칠 브랜치로 해서 돈다.
  - 보낼 곳이 로컬에 없으면 합치지도 PR을 열지도 않고 그 이름을 알리고 10번으로 간다.
  - 그 줄이 없는 tasks는 지금과 같다.
  (`plugins/plate/skills/run/SKILL.md`)
- [x] 0번의 비운 뒤 재개가 보낼 곳이 있는 tasks에서도 같은 자리로 간다. `tasks/<이름>`에서 비운 뒤면 보낼 곳으로 합치는 자리로 간다. 보낼 곳 브랜치에서 그 tasks를 합친 뒤면 PR·합침으로 간다. 명령 치환 없이 한 명령씩 부른다 (`plugins/plate/skills/run/SKILL.md`)
- [x] 절대 규칙 5와 10번 보고가 맞는다. 푸시하는 브랜치에 보낼 곳이 들고, 보고에 보낼 곳으로 합쳤는지, 하지 않았으면 그 까닭이 더해진다 (`plugins/plate/skills/run/SKILL.md`)
- [x] 바뀐 글을 지키는 시험이 더해진다. 보낼 곳으로 합침, 보낼 곳이 없을 때, 재개, 절대 규칙 5를 본다. 바뀐 글을 지키던 기존 `RunRulesTest`의 단언도 새 글을 지킨다 (`tests/test_skill_rules.py`)
- [x] 맥락 문서가 맞는다. PRD 핵심 기능 8, ARCHITECTURE의 run 문단과 데이터 흐름의 "tasks 끝"이 보낼 곳으로 합친 뒤 PR·합침, 보낼 곳이 없을 때, 재개를 적는다 (`docs/PRD.md`, `docs/ARCHITECTURE.md`)

**통과 조건**
- task 머리의 완료 조건 3이 참이다.
  - 확인: `grep -n '보낼 곳' plugins/plate/skills/run/SKILL.md` → 절대 규칙, 0번, "비운다", "PR을 연다", "합친다"에 저마다 한 줄 이상
  - 확인: `mktemp -d` 시험 레포에서 본문의 명령을 적힌 차례대로 세 갈래로 돌린다.
    - 합칠 때: `main` → `cleanup/x`(커밋 하나) → `tasks/y`(커밋 둘, 마지막 제목 `y: 비움`)를 두고 합치는 명령을 돌린다. 기대: `git merge-base --is-ancestor tasks/y cleanup/x`가 0이고 `main`의 해시가 그대로다.
    - 보낼 곳이 없을 때: `cleanup/x`를 지운 레포에서 있는지 보는 명령이 아무것도 내지 않는다. 기대: 그 갈래가 합치는 명령에 닿지 않는다.
    - 재개할 때: 합친 뒤의 `cleanup/x`에서 0번의 재개 판정에 쓰는 명령(브랜치, 마지막 커밋 제목)을 돌린다. 기대: 본문이 정한 PR·합침 자리로 가는 값이 나온다.
- task 머리의 완료 조건 1·2가 그대로다(phase 1·2가 이룬 글).
  - 확인: `grep -n -F 'cleanup/<' plugins/plate/skills/cleanup/SKILL.md` → 절대 규칙, 보고서를 쓰고 커밋하는 절, 고른 발견이 없을 때의 절에 저마다 한 줄 이상
  - 확인: `grep -n '보낼 곳' plugins/plate/skills/plan/SKILL.md` → 절대 규칙, 1번, 7번, 계획 파일의 양식에 저마다 한 줄 이상
- task 머리의 완료 조건 4, 5, 6이 참이다.
  - 확인: `grep -n -F 'cleanup/<' docs/PRD.md docs/ARCHITECTURE.md` → PRD 핵심 기능 9, ARCHITECTURE 디렉터리 구조의 cleanup 줄, plan 문단, 데이터 흐름의 "정리 점검"에 저마다 한 줄 이상
  - 확인: `grep -n '보낼 곳' docs/PRD.md docs/ARCHITECTURE.md` → PRD 핵심 기능 8, ARCHITECTURE의 plan 문단, run 문단, 데이터 흐름의 "계획"과 "tasks 끝"에 저마다 한 줄 이상
  - 확인: `python3 -m unittest tests.test_cleanup_skill tests.test_skill_rules -v` → `OK`. cleanup 브랜치, plan의 보낼 곳, run의 보낼 곳을 보는 새 시험 이름이 나온다
  - 확인: `grep -n '지난 tasks의 같은 이름' plugins/plate/skills/plan/SKILL.md plugins/plate/skills/retro/SKILL.md` → plan의 "6. 초안을 보여 주고 승인받는다"와 "적는 규칙"의 **조건**, retro의 "4. task의 변경을 점검한다"에 저마다 한 줄 이상
  - 확인: `python3 -m unittest discover -s tests` → 마지막 줄이 `OK`

## 한 일
- 앞 phase의 산출물에 대어 조건을 맞춘다: plan 양식의 `**보낼 곳**: {그 cleanup 브랜치}` 줄(이름 줄 바로 아래)을 읽고, run 낱말의 "tasks 머리"에 그 줄을 더하고 새 낱말 "보낼 곳"(`**보낼 곳**: ` 뒤의 브랜치 이름)을 두었다 (`plugins/plate/skills/run/SKILL.md`)
- "비운다" 뒤에 보낼 곳으로 합치는 자리: "비운다"가 보낼 곳을 지우기 전에 읽어 두고, 있으면 새 절 "보낼 곳으로 합친다"로 간다. 그 절은 `git rev-parse --verify --quiet refs/heads/{보낼 곳}`(없으면 알리고 10번), 합칠지 물음, 커밋하지 않은 변경 물음, `git switch {보낼 곳}`, `git merge --no-ff -m '<이름>: 보낼 곳으로 합침' tasks/<이름>`, 충돌이면 `git merge --abort` 뒤 `git switch tasks/<이름>`, 합치면 `git branch -d tasks/<이름>`, 그다음 GitHub이면 보낼 곳을 푸시할 브랜치로 "PR을 연다", 아니면 보낼 곳을 합칠 브랜치로 "합친다"다. "PR을 연다"와 "합친다"는 `{푸시할 브랜치}`/`{합칠 브랜치}`로 두 경우를 받는다 (`plugins/plate/skills/run/SKILL.md`)
- 0번의 비운 뒤 재개: `tasks/<이름>`에서 비운 뒤면 `HEAD^:docs/tasks/plan.md`에 보낼 곳이 있을 때 "보낼 곳으로 합친다"로, cleanup 브랜치에서 마지막 커밋이 `<이름>: 보낼 곳으로 합침`이고 `git show HEAD^2^:docs/tasks/plan.md`의 이름·보낼 곳이 맞으면 보낼 곳으로 합친 뒤의 재개로 PR·합침으로 간다. 명령은 한 명령씩이다 (`plugins/plate/skills/run/SKILL.md`)
- 절대 규칙 5와 10번 보고: 푸시하는 브랜치에 보낼 곳을 더하고, 10번에 보낼 곳으로 합쳤는지와 그 합침 커밋, 않았으면 그 까닭(보낼 곳이 로컬에 없다와 그 이름, 거절, `git switch` 실패, 충돌)을 더했다. 1번 2의 "늘 `tasks/<이름>`을 푸시하고" 까닭 글에도 보낼 곳을 더했다 (`plugins/plate/skills/run/SKILL.md`)
- 바뀐 글을 지키는 시험: `RunRulesTest`에 `test_send_to_reads_plan_line`, `test_send_to_merge_after_clearing`, `test_send_to_missing_stops`, `test_send_to_resume`, `test_send_to_push_rule`을 더하고, `test_resume_after_clearing_goes_to_pr_or_merge`의 "PR을 연다"·"합친다" 단언을 새 글("0번의 비운 뒤의 재개나 보낼 곳으로 합친 뒤의 재개에서")로 고치고 "보낼 곳으로 합친다" 단언을 더했다 (`tests/test_skill_rules.py`)
- 맥락 문서: PRD 핵심 기능 8에 보낼 곳으로 합침, 없을 때, 재개를 더하고, ARCHITECTURE의 run 문단(합침, 없을 때, 재개, 푸시하는 브랜치)과 데이터 흐름 "tasks 끝"(비운 뒤 보낼 곳 줄, 재개)을 고쳤다 (`docs/PRD.md`, `docs/ARCHITECTURE.md`)

## 확인 결과
- 완료 조건 3: `grep -n '보낼 곳' plugins/plate/skills/run/SKILL.md`
  - → 줄 20(절대 규칙), 69·71·73·75(0번), 499·505(비운다), 523(PR을 연다), 564(합친다). 통과
- 완료 조건 3: 시험 레포 세 갈래 (`mktemp -d`, `main` → `cleanup/x` 커밋 하나 → `tasks/y` 커밋 둘, 마지막 `y: 비움`)
  - 합칠 때: `git rev-parse --verify --quiet refs/heads/cleanup/x`(해시 나옴) → `git switch cleanup/x` → `git merge --no-ff -m 'y: 보낼 곳으로 합침' tasks/y`(Merge made by the 'ort' strategy.) → `git merge-base --is-ancestor tasks/y cleanup/x` → 0, `git branch -d tasks/y` 뒤 저장한 해시로도 0, `git rev-parse main`이 전과 같음. 통과
  - 보낼 곳이 없을 때: `cleanup/x`가 없는 레포에서 `git rev-parse --verify --quiet refs/heads/cleanup/x` → 출력 없음(exit 1), 그 갈래는 `git switch`·`git merge`에 닿지 않고 브랜치는 `main`, `tasks/y` 그대로. 통과
  - 재개할 때: 합친 뒤의 `cleanup/x`에서 `git branch --show-current` → `cleanup/x`, `git log -1 --format=%s` → `y: 보낼 곳으로 합침`, `git show HEAD^2^:docs/tasks/plan.md`(plan.md를 둔 레포) → `**이름**: y`, `**보낼 곳**: cleanup/x` → 본문상 "보낼 곳으로 합친 뒤의 재개"로 PR·합침에 간다. 비운 뒤의 `tasks/y`에서는 `tasks/y`, `y: 비움`, `git show HEAD^:docs/tasks/plan.md`에 `**보낼 곳**: cleanup/x` → "보낼 곳으로 합친다"로 간다. 통과
- 완료 조건 1: `grep -n -F 'cleanup/<' plugins/plate/skills/cleanup/SKILL.md`
  - → 17·18(절대 규칙), 115·127(5. 보고서를 쓰고 커밋한다), 149~165(고른 발견이 없을 때). 통과
- 완료 조건 2: `grep -n '보낼 곳' plugins/plate/skills/plan/SKILL.md`
  - → 19(절대 규칙), 55(1번), 139(7번), 170(계획 파일의 양식). 통과
- 완료 조건 4: `grep -n -F 'cleanup/<' docs/PRD.md docs/ARCHITECTURE.md`
  - → PRD 19(핵심 기능 9), ARCHITECTURE 32(디렉터리 구조 cleanup 줄), 56(plan 문단), 95·98(데이터 흐름 정리 점검). 통과
- 완료 조건 4: `grep -n '보낼 곳' docs/PRD.md docs/ARCHITECTURE.md`
  - → PRD 18(핵심 기능 8), ARCHITECTURE 56(plan 문단), 57(run 문단), 65(데이터 흐름 계획), 81·84(데이터 흐름 tasks 끝). 통과
- 완료 조건 5: `python3 -m unittest tests.test_cleanup_skill tests.test_skill_rules -v`
  - → `Ran 122 tests`, `OK`. 새 시험 이름 `CleanupBranchTest`의 넷, `test_cleanup_branch_sends_back`, `test_send_to_*` 다섯이 나옴. 통과
- 완료 조건 6: `grep -n '지난 tasks의 같은 이름' plugins/plate/skills/plan/SKILL.md plugins/plate/skills/retro/SKILL.md`
  - → plan 115(6. 초안을 보여 주고 승인받는다), 266(적는 규칙의 **조건**, 260부터), retro 79(4. task의 변경을 점검한다). 통과
- 완료 조건 6: `python3 -m unittest discover -s tests`
  - → `Ran 263 tests`, 마지막 줄 `OK`. 통과

## 계획과 달라진 점
- TODO에 없던 run 1번 2(tasks 브랜치)의 까닭 글 "끝의 "PR을 연다"와 "합친다"는 늘 `tasks/<이름>`을 푸시하고"에 보낼 곳을 더했다. 같은 파일의 글이 바뀐 동작과 어긋나지 않게 하려는 것이다.
- 보낼 곳으로 합치는 자리를 "비운다" 안이 아닌 새 `## 보낼 곳으로 합친다` 절로 두었다. "PR을 연다"와 "합친다"와 같은 깊이로 두어 0번의 재개가 그 절 이름으로 가리키게 했다. 합침은 `--no-ff -m '<이름>: 보낼 곳으로 합침'`으로 정했다. 빨리 감기로 합쳐지면 합침 커밋이 없어 0번이 보낼 곳으로 합친 뒤의 재개를 가를 수 없어서다.

## 남은 것
- 고친 run 본문을 헤드리스로 끝까지 돌리지 않았다(task 머리의 범위 밖). 본문의 브랜치 명령만 시험 레포에서 돌렸다.
- 보낼 곳으로 합친 뒤의 재개는 보낼 곳 브랜치의 마지막 커밋이 그 합침 커밋일 때만 가른다. 합친 뒤 사람이 그 브랜치에 커밋을 더하면 재개로 보지 않고 "실행할 계획이 없다"로 끝난다.
- 충돌로 되돌린 뒤 `git switch tasks/<이름>`이 실패하는 경우의 갈래는 따로 적지 않았다.

## 하네스에서 걸린 것
- 셸 heredoc으로 넘긴 파이썬 스크립트 하나가 `SyntaxError: Non-UTF-8 code`로 돌지 않아, 같은 스크립트를 스크래치 파일로 써서 돌렸다. 계획이나 스킬의 문제는 아니다.

## 확인 1

**통과 조건**
- task 머리의 완료 조건 3이 참이다.
  - `grep -n '보낼 곳' plugins/plate/skills/run/SKILL.md` → 20(절대 규칙 5), 69·71·73·75(0. tasks를 본다), 499·505(### 비운다), 523(## PR을 연다), 564(## 합친다). 통과
  - `mktemp -d` 시험 레포, 합칠 때: `main` → `cleanup/x`(커밋 `c1`) → `tasks/y`(커밋 `y: plan`, `y: 비움`, plan.md에 `**보낼 곳**: cleanup/x`)에서 본문 "보낼 곳으로 합친다"의 `git rev-parse --verify --quiet refs/heads/cleanup/x`(해시, exit 0) → `git switch cleanup/x` → `git merge --no-ff -m 'y: 보낼 곳으로 합침' tasks/y`(Merge made by the 'ort' strategy.) → `git merge-base --is-ancestor tasks/y cleanup/x` exit 0 → `git branch -d tasks/y` 삭제됨, `git rev-parse main`이 전과 같음. 통과
  - 보낼 곳이 없을 때: `cleanup/x`가 없는 새 `mktemp -d` 레포(`main`, `tasks/y`의 `y: 비움`)에서 `git rev-parse --verify --quiet refs/heads/cleanup/x` → 출력 없음, exit 1. 본문 1번대로 그 갈래는 알리고 10번으로 가 `git switch`·`git merge`에 닿지 않음. 브랜치는 `main`, `tasks/y` 그대로. 통과
  - 재개할 때: 합친 뒤의 `cleanup/x`에서 `git branch --show-current` → `cleanup/x`, `git log -1 --format=%s` → `y: 보낼 곳으로 합침`, `git show HEAD^2^:docs/tasks/plan.md` → `**이름**: y`, `**보낼 곳**: cleanup/x`. 본문 0번의 "보낼 곳으로 합친 뒤의 재개"(이름이 같고 보낼 곳이 지금 브랜치) → "PR을 연다"/"합친다"로 감. 합치기 전 `tasks/y`에서도 `tasks/y`, `y: 비움`, `git show HEAD^:docs/tasks/plan.md`에 보낼 곳 줄 → "보낼 곳으로 합친다"로 감. 통과
- task 머리의 완료 조건 1·2가 그대로다.
  - `grep -n -F 'cleanup/<' plugins/plate/skills/cleanup/SKILL.md` → 17·18(절대 규칙), 115·127(5. 보고서를 쓰고 커밋한다), 149·153~165(고른 발견이 없을 때). 통과
  - `grep -n '보낼 곳' plugins/plate/skills/plan/SKILL.md` → 19(절대 규칙 4), 55(1번), 139(7번), 170(계획 파일의 양식). 통과
- task 머리의 완료 조건 4, 5, 6이 참이다.
  - `grep -n -F 'cleanup/<' docs/PRD.md docs/ARCHITECTURE.md` → PRD 19(핵심 기능 9), ARCHITECTURE 32(디렉터리 구조 cleanup 줄), 56(plan 문단), 95·98(데이터 흐름 정리 점검). 통과
  - `grep -n '보낼 곳' docs/PRD.md docs/ARCHITECTURE.md` → PRD 18(핵심 기능 8), ARCHITECTURE 56(plan 문단), 57(run 문단), 65(데이터 흐름 계획), 81·84(데이터 흐름 tasks 끝). 통과
  - `python3 -m unittest tests.test_cleanup_skill tests.test_skill_rules -v` → `Ran 122 tests`, `OK`. `CleanupBranchTest` 넷, `test_cleanup_branch_sends_back`, `test_send_to_*` 다섯이 나옴. 통과
  - `grep -n '지난 tasks의 같은 이름' plugins/plate/skills/plan/SKILL.md plugins/plate/skills/retro/SKILL.md` → plan 115(6. 초안을 보여 주고 승인받는다), 266(적는 규칙의 **조건**, 260부터), retro 79(4. task의 변경을 점검한다). 통과
  - `python3 -m unittest discover -s tests` → `Ran 263 tests`, 마지막 줄 `OK`. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 263 tests`, `OK`. 통과

**남은 것**
- 고친 run 본문을 헤드리스로 끝까지 돌리지 않았다 → 완료 조건 3의 `- 돌리지 않음: run은 에이전트를 띄우고 묻는 스킬이고 PR은 GitHub이 있어야 해 헤드리스로 끝까지 돌리지 않는다`가 돌리지 않기로 정한 동작. 하네스에서 걸린 것
- 합친 뒤 사람이 보낼 곳에 커밋을 더하면 재개로 보지 않는다 → 통과 조건의 재개 갈래는 합친 직후의 `cleanup/x`만 보므로 걸리지 않음. 하네스에서 걸린 것
- 충돌로 되돌린 뒤 `git switch tasks/<이름>`이 실패하는 갈래를 적지 않았다 → 통과 조건의 세 갈래(합침, 없음, 재개)는 충돌을 보지 않아 걸리지 않음. 하네스에서 걸린 것

**실패**
- 없음

**하네스에서 걸린 것**
- 남은 것: 고친 run 본문을 헤드리스로 끝까지 돌리지 않았다(완료 조건 3의 `돌리지 않음` 줄).
- 남은 것: 보낼 곳으로 합친 뒤 사람이 그 브랜치에 커밋을 더하면 0번이 재개로 보지 않고 "실행할 계획이 없다"로 끝난다.
- 남은 것: 충돌로 `git merge --abort` 뒤 `git switch tasks/<이름>`이 실패하는 갈래가 본문에 없다.

**판정**: 통과
