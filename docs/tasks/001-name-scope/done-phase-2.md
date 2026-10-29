# Phase 2: retro가 이번 task의 커밋만 보고 결정의 빈틈을 문제로 판정한다

**목표**: retro의 "task의 커밋"이 task 머리를 마지막으로 더한 커밋 뒤의 것만 센다. 결정이 정한 동작이 세 경우에서 목표를 해치면 retro가 문제(기준: 계획, 고칠 쪽: 계획)로 판정한다. 두 동작을 헤드리스 시험으로 본다.

**테스트 먼저**: 아니오 — `.md`인 스킬 본문만 고치고, 테스트는 그 글을 지키는 시험이라 코드 파일의 동작을 바꾸지 않는다

**읽을 것**
- `plugins/plate/skills/retro/SKILL.md` (낱말의 **task의 커밋**, "1. 읽는다", "4. task의 변경을 점검한다"의 `지난 tasks의 같은 이름` 줄과 경계 밖 문단, "5. tasks 끝에 볼 것을 모은다"의 **경계 밖**, 기록의 양식의 "고칠 쪽" 칸, 적는 규칙의 "고칠 쪽"과 경계 밖 줄)
- `docs/ARCHITECTURE.md` (패턴과 규칙의 훅 문단: 편집 훅이 task 머리 `plan.md`를 마지막으로 더하거나 지운 커밋 뒤에서 phase 커밋을 찾는 글. 디렉터리 구조의 `test_skill_rules.py` 줄)
- `docs/TOOLS.md` ("세션 도중의 스킬 본문 고침", "스킬을 헤드리스로 돌려 볼 때의 허용 목록", 한글 heredoc 줄)
- `tests/test_skill_rules.py` (`RetroRulesTest`)
- `docs/PRD.md`, `docs/ADR.md`, `docs/BACKLOG.md`

**TODO**
- [x] 낱말의 **task의 커밋**이 그 task 머리 `plan.md`를 마지막으로 더한 커밋 뒤의 커밋으로 좁혀진다. 그 커밋이 없으면 지금 꼴로 본다 (`plugins/plate/skills/retro/SKILL.md`)
- [x] 4번의 `지난 tasks의 같은 이름` 줄이 바뀐다. 결정이나 완료 조건이 정한 동작이 세 경우에서 목표를 해치면 "문제"에 기준 "계획", 고칠 쪽 "계획"으로 적는다. 기록의 "남은 것"에 그 꼴이 적힌 줄도 같다. 양식과 적는 규칙의 "고칠 쪽"에 "계획"이 더해진다. 경계 밖 문단과 5번의 **경계 밖**, 적는 규칙의 경계 밖 줄은 이 꼴을 빼게 맞춘다 (`plugins/plate/skills/retro/SKILL.md`)
- [x] 바뀐 두 글을 지키는 시험이 생긴다: `RetroRulesTest.test_80_task_commits_after_task_head`, `RetroRulesTest.test_80_decided_gap_is_plan_problem`. 옛 시험 `test_80_decided_behavior_with_repeated_names_goes_out_of_bounds`는 새 글을 지키게 바뀌거나 이 시험으로 갈음된다 (`tests/test_skill_rules.py`)
- [x] 완료 조건 2의 시험 레포 A와 완료 조건 3의 시험 레포 B를 scratchpad의 `mktemp -d`에 차린다. 두 레포에서 `claude -p "/plate:retro docs/tasks/001-x" --plugin-dir {이 저장소}/plugins/plate --permission-mode bypassPermissions --output-format json`을 돌리고, 결과와 그때의 `git hash-object plugins/plate/skills/retro/SKILL.md`를 기록에 남긴다(이 저장소의 파일은 바꾸지 않는다)
- [x] 디렉터리 구조의 `test_skill_rules.py` 줄에 두 규칙(`task 머리를 마지막으로 더한 커밋`, `고칠 쪽이 계획`)이 더해진다 (`docs/ARCHITECTURE.md`)

**통과 조건**
- 완료 조건 2가 참이다.
  - 확인: `grep -n -F '**task의 커밋**' plugins/plate/skills/retro/SKILL.md` → 그 줄에 `마지막으로 더한 커밋`이 있다
  - 확인: 시험 레포 A의 `docs/tasks/001-x/retro.md`에서 `grep -c 'old.txt'` → `0`, `grep -c 'new.txt'` → 1 이상
- 완료 조건 3이 참이다.
  - 확인: 시험 레포 B의 retro 결과의 첫 줄이 `판정: 문제 있음`이고, 그 `retro.md`의 "문제"에 `기준: 계획`과 `고칠 쪽: 계획`이 든 줄이 있다
  - 확인: 두 헤드리스 시험 전후로 이 저장소의 `git status --porcelain`이 `docs/tasks/RUNLOG.md`와 이 phase가 고친 파일을 빼면 같고, `git rev-parse HEAD`가 같다
  - 확인: 기록에 적은 retro 본문 해시가 작업 트리의 `git hash-object plugins/plate/skills/retro/SKILL.md`와 같다
- 두 시험이 글을 지킨다.
  - 확인: `cp -R` 사본에서 **task의 커밋** 줄의 `마지막으로 더한 커밋`을 지우면 `RetroRulesTest.test_80_task_commits_after_task_head`가 `FAILED`이고, `고칠 쪽: 계획`이 든 4번의 줄을 지우면 `RetroRulesTest.test_80_decided_gap_is_plan_problem`이 `FAILED`다
- 완료 조건 1이 그대로다(앞 phase가 이룬 조건의 파일을 고친다).
  - 확인: `grep -n '합쳐지지 않은 다른 브랜치' plugins/plate/skills/retro/SKILL.md` → 4번에 한 줄 이상이고, 그 줄에 `지난 tasks의 같은 이름`과 `이름마다`가 함께 있다
- 테스트 묶음이 모두 통과한다.
  - 확인: `python3 -m unittest discover -s tests` → 마지막 줄이 `OK`

## 한 일
- 낱말의 **task의 커밋**이 그 task 머리 `plan.md`를 마지막으로 더한 커밋 뒤의 커밋으로 좁혀진다: 정의 머리에 "그 task 머리 `plan.md`를 마지막으로 더한 커밋 뒤의 커밋 가운데"를 두고, 그 커밋을 찾는 명령 `git log -1 --diff-filter=A --format=%H -- <task 폴더>/plan.md`와 없으면 역사 전체에서 센다는 글, 까닭(비운 뒤 같은 task 이름을 다시 쓰는 tasks)을 더함 (`plugins/plate/skills/retro/SKILL.md`)
- 4번의 `지난 tasks의 같은 이름` 줄 등: 그 줄이 "`경계 밖`으로도 돌리지 않고 "문제"에 `기준: 계획`, `고칠 쪽: 계획`으로 적는다"와 근거(해치는 목표, 정한 결정이나 완료 조건)를 적게 바뀌고, "남은 것"의 그 꼴 줄은 판정이 "문제"가 됨. 경계 밖 문단에 그 꼴은 경계 밖으로 모으지 않는다는 줄, 5번 **경계 밖**에 그 꼴은 넣지 않고 **문제**로 모은다는 줄, 양식의 고칠 쪽 칸에 `계획`, 적는 규칙의 고칠 쪽 줄과 경계 밖 줄에 그 꼴의 예외를 더함 (`plugins/plate/skills/retro/SKILL.md`)
- 바뀐 두 글을 지키는 시험: `RetroRulesTest.test_80_task_commits_after_task_head`를 더하고, 옛 `test_80_decided_behavior_with_repeated_names_goes_out_of_bounds`를 `test_80_decided_gap_is_plan_problem`으로 갈음함(4번 줄의 새 글, 옛 "5번에서 `경계 밖`으로 모은다" 글이 없음, 경계 밖 문단·5번·양식·적는 규칙의 새 글을 봄) (`tests/test_skill_rules.py`)
- 시험 레포 A·B 헤드리스 시험: scratchpad의 `p2/setup.sh`로 `mktemp -d`의 `A.e4Lt`, `B.aa0s`에 차리고 두 레포에서 `claude -p "/plate:retro docs/tasks/001-x" --plugin-dir /Users/hugo/Desktop/harness-plate/plugins/plate --permission-mode bypassPermissions --output-format json`을 돌림. 그때의 retro 본문 해시 `git hash-object plugins/plate/skills/retro/SKILL.md` → `684f526efee0df1a7a919100a95275fc794d0592`
  - A의 차림: `init` → `plan: old-tasks`(001-x/plan.md 더함) → `001-x: phase 1`(old.txt, done-phase-1.md) → `001-x: 회고` → `old-tasks: tasks 비움` → `plan: new-tasks`(001-x/plan.md 다시 더함) → `001-x: phase 1`(new.txt, done-phase-1.md). 본문의 명령이 A에서 `004420d…`(`plan: new-tasks`)를 냄
  - A 결과: `판정: 통과`, `문제: 0개`. 회고 커밋 `0543fd8 001-x: 회고`
  - B의 차림: 합쳐지지 않은 `report/a`에 `reports/1.md`, main의 작업 트리에는 `reports/` 없음, task 머리의 목표 "새 보고서 이름이 다른 브랜치의 보고서와 겹치지 않는다", 결정 "`new_report.sh`는 작업 트리의 `reports/`만 보고 없는 번호를 고른다", 그 스크립트를 둔 `001-x: phase 1`과 `done-phase-1.md`
  - B 결과: `판정: 문제 있음`, `문제: 1개`. 회고 커밋 `e060b3e 001-x: 회고`. `retro.md` 17줄: "… `reports/1.md`와 같은 `reports/1.md`를 만든다 … 기준: 계획. 고칠 쪽: 계획 (해치는 목표: … 그 동작을 정한 것: task 머리의 결정 …)". `FRICTION.md`에 `경계 밖` 0줄
- 디렉터리 구조의 `test_skill_rules.py` 줄: 옛 "retro 4번이 … `경계 밖`으로 모음"을 "… 문제 아님으로도 `경계 밖`으로도 닫지 않고 고칠 쪽이 계획인 문제(기준: 계획)로 적음, retro의 task의 커밋이 그 task 머리를 마지막으로 더한 커밋 뒤의 것만 셈"으로 바꿈 (`docs/ARCHITECTURE.md`)

## 확인 결과
- 완료 조건 2가 참이다.
  - `grep -n -F '**task의 커밋**' plugins/plate/skills/retro/SKILL.md | grep -c '마지막으로 더한 커밋'` → `1`(31줄). 통과
  - 시험 레포 A의 `docs/tasks/001-x/retro.md`: `grep -c 'old.txt'` → `0`, `grep -c 'new.txt'` → `2`. 통과
- 완료 조건 3이 참이다.
  - 시험 레포 B의 결과(`result`)의 첫 줄 → `판정: 문제 있음`. `grep -n '기준: 계획' docs/tasks/001-x/retro.md` → 17줄("문제" 아래)에 `기준: 계획. 고칠 쪽: 계획`. 통과
  - 시험 전 `git status --porcelain` → 빈 출력, `git rev-parse HEAD` → `fecd691cd143967f4d03dd85640e3f730f3336bf`. 시험 뒤 `git status --porcelain` → ` M docs/ARCHITECTURE.md`, ` M plugins/plate/skills/retro/SKILL.md`, ` M tests/test_skill_rules.py`(모두 이 phase가 고친 파일), `git rev-parse HEAD` → `fecd691cd143967f4d03dd85640e3f730f3336bf`. 빼면 같다. 통과
  - 기록의 해시 `684f526efee0df1a7a919100a95275fc794d0592`와 작업 트리의 `git hash-object plugins/plate/skills/retro/SKILL.md` → `684f526efee0df1a7a919100a95275fc794d0592`. 같다. 통과
- 두 시험이 글을 지킨다.
  - `cp -R` 사본에서 `sed -i '' '/^- \*\*task의 커밋\*\*/s/마지막으로 더한 커밋//' plugins/plate/skills/retro/SKILL.md` 뒤 `python3 -m unittest tests.test_skill_rules.RetroRulesTest.test_80_task_commits_after_task_head` → `FAILED (failures=1)`. 통과
  - `cp -R` 사본에서 `sed -i '' '/지난 tasks의 같은 이름.*고칠 쪽: 계획/d' plugins/plate/skills/retro/SKILL.md`(4번의 그 줄만 지움, `고칠 쪽: 계획` 줄 2→1) 뒤 `python3 -m unittest tests.test_skill_rules.RetroRulesTest.test_80_decided_gap_is_plan_problem` → `FAIL: test_80_decided_gap_is_plan_problem`, `FAILED (failures=1)`. 통과
- 완료 조건 1이 그대로다.
  - `grep -n '합쳐지지 않은 다른 브랜치' plugins/plate/skills/retro/SKILL.md` → 79줄(4번) 한 줄, 그 줄에 `지난 tasks의 같은 이름`과 `이름마다`가 있다. 통과
- 테스트 묶음이 모두 통과한다.
  - `python3 -m unittest discover -s tests` → `Ran 274 tests`, 마지막 줄 `OK`. 통과

## 계획과 달라진 점
- 없음

## 남은 것
- 본문이 **task의 커밋**을 찾는 명령 `git log -1 --diff-filter=A … -- <task 폴더>/plan.md`는 task 머리가 이름 바꾸기로 들어온 경우(`git mv`로 다른 폴더에서 옮김)를 더한 것으로 치지 않을 수 있다. 시험 레포 A는 새로 더한 꼴만 보았다
- 헤드리스 시험은 레포 A·B를 한 번씩 돌렸다. 에이전트 판단이라 같은 차림에서 늘 같은 판정이 나는지는 보지 않았다

## 하네스에서 걸린 것
- 없음

## 확인 1

**통과 조건**
- 완료 조건 2가 참이다.
  - `grep -n -F '**task의 커밋**' plugins/plate/skills/retro/SKILL.md` → 31줄 하나, 그 줄에 `마지막으로 더한 커밋`이 있다. 통과
  - 기록의 `p2/setup.sh A`로 scratchpad의 새 `mktemp -d`(`c2/A.B2ai`)에 시험 레포 A를 다시 차리고 `claude -p "/plate:retro docs/tasks/001-x" --plugin-dir /Users/hugo/Desktop/harness-plate/plugins/plate --permission-mode bypassPermissions --output-format json`을 돌림 → 결과 `판정: 통과`, 회고 커밋 `1d67718 001-x: 회고`. 그 `docs/tasks/001-x/retro.md`에서 `grep -c 'old.txt'` → `0`, `grep -c 'new.txt'` → `2`. 통과
- 완료 조건 3이 참이다.
  - 같은 방법으로 시험 레포 B(`c2/B.eOlG`)에서 retro를 돌림 → 결과의 첫 줄 `판정: 문제 있음`. `grep -n '기준: 계획' docs/tasks/001-x/retro.md` → 17줄("**문제**" 아래)에 `기준: 계획. 고칠 쪽: 계획`. 통과
  - 두 헤드리스 시험 전후로 이 저장소의 `git status --porcelain`(전후 모두 ` M docs/tasks/RUNLOG.md`만) → `diff`로 같음, `git rev-parse HEAD`(전후 모두 `a900428b5ce1eed115f0b6ef9413267822595f75`, phase 커밋 뒤) → 같음. 통과
  - `git hash-object plugins/plate/skills/retro/SKILL.md` → `684f526efee0df1a7a919100a95275fc794d0592`, 기록의 해시와 같다. 통과
- 두 시험이 글을 지킨다.
  - `cp -R` 사본에서 `sed -i '' '/^- \*\*task의 커밋\*\*/s/마지막으로 더한 커밋//' plugins/plate/skills/retro/SKILL.md`(본문의 `마지막으로 더한 커밋` 1→0) 뒤 `python3 -m unittest tests.test_skill_rules.RetroRulesTest.test_80_task_commits_after_task_head` → `FAILED (failures=1)`. 통과
  - `cp -R` 사본에서 `sed -i '' '/지난 tasks의 같은 이름.*고칠 쪽: 계획/d' plugins/plate/skills/retro/SKILL.md`(4번의 79줄만 지워짐, `고칠 쪽: 계획` 줄 79·92 → 91) 뒤 `python3 -m unittest tests.test_skill_rules.RetroRulesTest.test_80_decided_gap_is_plan_problem` → `FAILED (failures=1)`. 통과
- 완료 조건 1이 그대로다.
  - `grep -n '합쳐지지 않은 다른 브랜치' plugins/plate/skills/retro/SKILL.md` → 79줄 하나(4번: 64~84줄), 그 줄에 `지난 tasks의 같은 이름`과 `이름마다`가 함께 있다. 통과
- 테스트 묶음이 모두 통과한다.
  - `python3 -m unittest discover -s tests` → `Ran 274 tests`, 마지막 줄 `OK`. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 274 tests`, `OK`. 통과

**남은 것**
- task 머리가 `git mv`로 들어온 경우 `git log -1 --diff-filter=A`가 그것을 더한 커밋으로 치지 않을 수 있다 → 통과 조건(완료 조건 2)이 보는 동작은 시험 레포 A의 새로 더한 task 머리이고 이름 바꾸기 꼴은 보지 않는다. 걸리지 않는다. 하네스에서 걸린 것
- 헤드리스 시험을 한 번씩 돌려 같은 차림에서 늘 같은 판정이 나는지 보지 않았다 → 통과 조건은 시험 레포 A·B에서 돌린 retro의 결과를 본다. 확인에서 새로 차린 레포로 다시 돌려 같은 결과를 얻었고, 되풀이마다 같은지는 통과 조건이 보지 않는다. 걸리지 않는다. 하네스에서 걸린 것

**실패**
- 없음

**하네스에서 걸린 것**
- 남은 것: retro 본문의 task 머리를 더한 커밋을 찾는 명령(`git log -1 --diff-filter=A … -- <task 폴더>/plan.md`)은 `git mv`로 들어온 task 머리를 더한 것으로 치지 않을 수 있다(그때 역사 전체에서 센다)
- 남은 것: 헤드리스 시험은 에이전트 판단이라 되풀이마다 같은 판정이 나는지는 보지 않았다(수행 한 번, 확인 한 번 모두 같은 판정)

**판정**: 통과
