# Phase 1: tasks 끝의 문제를 고친다

**목표**: task 머리의 완료 조건에 적힌 것을 모두 고친다.

**테스트 먼저**: 아니오 — 고칠 동작은 `.md`인 스킬 본문(cleanup)이고, 더하는 테스트는 그 본문을 지키는 시험이라 코드 파일의 동작을 바꾸지 않는다.

**읽을 것**
- `docs/tasks/review.md`의 `## 평가 1` 절
- `docs/tasks/eval.md`의 `## eval 1` 절
- `plugins/plate/skills/cleanup/SKILL.md`
- `plugins/plate/skills/run/SKILL.md`
- `plugins/plate/skills/plan/SKILL.md`
- `plugins/plate/skills/retro/SKILL.md`
- `README.md`
- `tests/test_cleanup_skill.py`
- `tests/test_skill_rules.py`
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/ADR.md`
- `docs/TOOLS.md`
- `docs/BACKLOG.md`
- `docs/cleanup/`

**TODO**
- [x] 보고서 경로를 작업 트리의 `docs/cleanup/`만 보고 정해 합쳐지지 않은 같은 날의 cleanup 브랜치와 파일 이름이 겹치고 지난 보고서 읽기가 그 보고서를 놓친다. 고친 동작을 적은 맥락 문서와 README의 줄과 그 글을 지키는 테스트도 맞춘다 (`plugins/plate/skills/cleanup/SKILL.md`, `docs/PRD.md`, `docs/ARCHITECTURE.md`, `README.md`, `tests/test_cleanup_skill.py`)
- [x] cleanup의 "기본 브랜치"·"GitHub 원격" 정의가 run과 같은지, plan과 cleanup의 "cleanup 브랜치" 정의가 어긋나지 않는지 지키는 시험을 둔다 (`tests/test_cleanup_skill.py`, `tests/test_skill_rules.py`)
- [x] cleanup "고른 발견이 없을 때"의 합침 갈래와 run "보낼 곳으로 합친다"의 충돌 뒤 되돌림을 시험 레포에서 돌려 보고, #80의 retro 규칙을 헤드리스 시험으로 돌려 본다 (`tests/test_cleanup_skill.py`, `tests/test_skill_rules.py`)

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다

## 한 일
- 보고서 경로를 작업 트리의 `docs/cleanup/`만 보고 정해 합쳐지지 않은 같은 날의 cleanup 브랜치와 파일 이름이 겹치고 지난 보고서 읽기가 그 보고서를 놓친다. 고친 동작을 적은 맥락 문서와 README의 줄과 그 글을 지키는 테스트도 맞춘다: cleanup 1번이 작업 트리의 `docs/cleanup/`과 로컬 cleanup 브랜치마다(`git for-each-ref --format='%(refname:short)' refs/heads/cleanup/`, `git cat-file -e {브랜치}:docs/cleanup/{파일 이름}`) 그 파일이 있으면 쓰인 이름으로 보고 번호를 붙이게 했고, 2번이 로컬 cleanup 브랜치의 보고서(`git ls-tree --name-only {브랜치} docs/cleanup/`, `git show {브랜치}:{경로}`)도 지난 보고서로 보게 했다. PRD 핵심 기능 9, ARCHITECTURE 데이터 흐름의 정리 점검과 디렉터리 구조의 테스트 줄, README의 cleanup 행을 맞췄다. `ReportNameAcrossBranchesTest`(본문 글 둘과, 본문의 명령을 뽑아 시험 레포에서 같은 날 두 번 돌리고 두 브랜치를 차례로 main에 합치는 시험)를 더했다 (`plugins/plate/skills/cleanup/SKILL.md`, `docs/PRD.md`, `docs/ARCHITECTURE.md`, `README.md`, `tests/test_cleanup_skill.py`)
- cleanup의 "기본 브랜치"·"GitHub 원격" 정의가 run과 같은지, plan과 cleanup의 "cleanup 브랜치" 정의가 어긋나지 않는지 지키는 시험을 둔다: `SharedDefinitionsTest`(두 정의 줄이 run과 글자째 같은지, 두 본문의 cleanup 브랜치 줄이 `cleanup/<보고서 이름>`, `cleanup/<보고서 이름>-2`, "같은 이름의 로컬 브랜치"를 적는지)를 더했다. 시험 레포 도우미 `GitRepo`와 `git_commands`는 `tests/test_skill_rules.py`에 두고 cleanup 시험이 가져다 쓴다 (`tests/test_cleanup_skill.py`, `tests/test_skill_rules.py`)
- cleanup "고른 발견이 없을 때"의 합침 갈래와 run "보낼 곳으로 합친다"의 충돌 뒤 되돌림을 시험 레포에서 돌려 보고, #80의 retro 규칙을 헤드리스 시험으로 돌려 본다: `NoSelectionMergeTest`(합침 갈래의 `git switch {기본 브랜치}`, `git merge cleanup/<보고서 이름>`, `git merge --abort`, `git branch -d cleanup/<보고서 이름>`을 본문에서 뽑아 차례를 보고 충돌 없음·충돌 두 갈래로 돌림)와 `RunRulesTest.test_merge_to_target_conflict_restores_target`(보낼 곳으로 합친다의 다섯 명령을 본문에서 뽑아 충돌하는 갈래로 돌림)를 더했다. retro는 스크래치의 시험 레포(지난 tasks의 `001-report: phase 1` 커밋이 남고, 이번 task `001-report`가 결정대로 `git log --reverse`의 첫 줄을 골라 그 옛 커밋을 내는 `find_phase.sh`를 만든 레포)에서 `claude -p "/plate:retro docs/tasks/001-report" --plugin-dir /Users/hugo/Desktop/harness-plate/plugins/plate --permission-mode bypassPermissions --output-format json`으로 돌렸다(Claude Code 2.1.312, retro 본문 sha256 `aff04746d43734c45bd190c2fdb8cff8ffc3ebc5ef7f191b7b75b5b97473a8e8`) (`tests/test_cleanup_skill.py`, `tests/test_skill_rules.py`)

## 확인 결과
- 완료 조건 1: 보고서 경로가 합쳐지지 않은 같은 날의 cleanup 브랜치와 겹치지 않는다
  - `mktemp -d` 시험 레포에서 `docs/cleanup/2026-10-29.md`를 커밋한 `cleanup/2026-10-29`를 합치지 않은 채 main으로 돌아가 본문 1번의 명령을 차례로 돌림 → `ls docs/cleanup/2026-10-29.md`는 없음, `git for-each-ref …`는 `cleanup/2026-10-29`, `git cat-file -e cleanup/2026-10-29:docs/cleanup/2026-10-29.md`는 0(쓰임), `…-2.md`는 128(안 쓰임) → 새 보고서 `docs/cleanup/2026-10-29-2.md`. 5번 `git rev-parse --verify --quiet refs/heads/cleanup/2026-10-29-2` → rc 1, 빈 출력 → `cleanup/2026-10-29-2`. 두 브랜치를 차례로 main에 `git merge` → 둘 다 rc 0, `create mode … 2026-10-29.md`, `create mode … 2026-10-29-2.md`, `git status --porcelain` 빈 출력. 통과
  - 본문 2번을 읽음 → "아직 기본 브랜치에 합쳐지지 않은 cleanup 브랜치의 보고서도 지난 보고서로 본다", `git ls-tree --name-only {브랜치} docs/cleanup/`(시험 레포에서 `docs/cleanup/2026-10-29.md`를 냄). 통과
  - `python3 -m unittest -v tests.test_cleanup_skill.ReportNameAcrossBranchesTest` → 3개 ok. HEAD의 cleanup 본문으로 되돌린 `cp -R` 사본에서는 `FAILED (failures=6)`. 통과
- 완료 조건 2: 복사한 정의를 지키는 시험
  - `tests/test_cleanup_skill.py`의 `SharedDefinitionsTest` 두 시험 → ok. 통과
  - `cp -R` 사본에서 cleanup의 "기본 브랜치" 줄(`` `origin` `` → `origin`), "GitHub 원격" 줄(`URL` → `주소`), "cleanup 브랜치" 줄(`-2` → `.2`)을 저마다 한 줄씩 바꿔 `python3 -m unittest tests.test_cleanup_skill.SharedDefinitionsTest` → 세 번 모두 `FAILED (failures=1)`. 통과
- 완료 조건 3: 돌려 보는 확인
  - cleanup 합침 갈래: `NoSelectionMergeTest` → `test_merge_without_conflict` ok(main이 cleanup 브랜치의 끝 커밋을 품고, `git branch -d` 뒤 `git rev-parse --verify --quiet refs/heads/cleanup/2026-10-29`가 빈 출력), `test_merge_with_conflict_is_aborted` ok(`git merge`가 0이 아니고 `git merge --abort` 뒤 main 해시 그대로, 작업 트리 깨끗). 통과
  - run 보낼 곳으로 합친다: `RunRulesTest.test_merge_to_target_conflict_restores_target` → ok(충돌 뒤 `git merge --abort`, `git switch tasks/y`로 `cleanup/x`·`tasks/y`·`main` 해시 그대로, 지금 브랜치 `tasks/y`). 통과
  - retro 헤드리스 시험 → 결과 `판정: 통과`, `문제: 0개`. 시험 레포의 `docs/tasks/FRICTION.md`에 "`001-report` 경계 밖: tasks 머리의 결정(…)대로 `find_phase.sh`가 지난 tasks에 남은 같은 메시지의 커밋 `30d7843`…을 골라, 목표인 …(`cf1d587`)이 아닌 해시를 낸다"가 적히고 `001-report: 회고` 커밋은 `retro.md`, `FRICTION.md`만 바꿈. 그 경우를 `FRICTION.md`의 경계 밖으로 적었다. 통과
  - 저장소 불변: 시험 전후의 이 저장소 `git status --porcelain`이 같고(`diff`가 빈 출력, 남은 변경은 `docs/tasks/RUNLOG.md`와 이 phase가 고친 일곱 파일뿐) HEAD가 `1cd96c5` 그대로. 통과
  - 돌리지 않음 줄(plan 헤드리스): 계획대로 돌리지 않음
- 완료 조건 4: tasks 완료 조건 1~6
  - 1: `python3 -m unittest discover -s tests` → `Ran 271 tests`, 마지막 줄 `OK`. 통과
  - 2: `grep -n '지난 tasks의 같은 이름' …plan… …retro…` → plan:115(6번), plan:266(적는 규칙 **조건**), retro:79(4번). 통과. 그 줄을 `sed -i '' '/지난 tasks의 같은 이름/d'`로 지운 `cp -R` 사본에서 두 `test_80_…` 시험 → `FAILED (failures=4)`. 통과
  - 3: `grep -n -F 'cleanup/<' …cleanup/SKILL.md` → 절대 규칙 17·18줄, 5번 115·127줄, 고른 발견이 없을 때 149~165줄. 통과. 시험 레포 세 갈래 → main에서: 새 브랜치 HEAD가 main과 같음. `tasks/x`에서: `cleanup/2026-10-29`가 있어 `cleanup/2026-10-29-2`가 `tasks/x`의 HEAD에서 생김, main 그대로, 옛 브랜치 해시 그대로. 통과
  - 4: `grep -n '보낼 곳' …plan/SKILL.md` → 55줄(1번), 139줄(7번), 170줄(양식). 통과. 시험 레포 `cleanup/x`에서 `git rev-parse --verify --quiet refs/heads/tasks/y`(rc 1) → `git switch -c tasks/y` → `git merge-base --is-ancestor cleanup/x tasks/y` rc 0, main 그대로. 통과
  - 5: `grep -n '보낼 곳' …run/SKILL.md` → 0번 69~75줄, "비운다" 499·505줄, "PR을 연다" 523줄, "합친다" 564줄. 통과. 시험 레포 `cleanup/x`가 있을 때: `git switch cleanup/x`, `git merge --no-ff -m 'y: 보낼 곳으로 합침' tasks/y` → `git merge-base --is-ancestor tasks/y cleanup/x` rc 0, main 그대로. `cleanup/x`를 지운 레포에서 `git rev-parse --verify --quiet refs/heads/cleanup/x` → 빈 출력. 통과
  - 6: `grep -n -F 'cleanup/<' docs/PRD.md docs/ARCHITECTURE.md` → PRD 19, ARCHITECTURE 56(plan 문단), 95·98(정리 점검). 통과. `grep -n '보낼 곳' docs/PRD.md docs/ARCHITECTURE.md` → PRD 18, ARCHITECTURE 57(run 문단), 81·84(tasks 끝). 통과
  - 돌리지 않음 줄(plan·retro·cleanup·run 끝까지의 헤드리스): 계획대로 돌리지 않음

## 계획과 달라진 점
- TODO 1이 든 파일 밖에 `docs/ARCHITECTURE.md`의 디렉터리 구조 테스트 줄(`test_cleanup_skill.py`, `test_skill_rules.py`)도 고쳤다. tasks 완료 조건 6이 "테스트 목록 줄"을 맞추라고 하고, 새 시험이 그 줄의 설명 밖에 있어서다. TODO 1이 이미 `docs/ARCHITECTURE.md`를 들어 파일은 같다
- 시험 레포 도우미(`GitRepo`, `git_commands`)를 `tests/test_skill_rules.py`에 두었다. 두 시험 파일이 함께 쓰고 `test_cleanup_skill.py`가 이미 그 파일에서 가져다 쓰기 때문이다

## 남은 것
- 1번의 이름 고르기는 로컬 cleanup 브랜치만 본다. 로컬 브랜치를 지운 채 origin에만 남은 cleanup 브랜치(푸시하고 PR을 연 뒤 로컬을 지운 것)의 보고서는 보지 않아, 그 PR과 새 브랜치를 함께 합칠 때는 같은 경로 충돌이 날 수 있다
- 헤드리스 retro가 시험 레포의 `FRICTION.md`에 "plate:retro의 'task의 커밋' 낱말(메시지가 task 이름으로 시작하는 커밋)이 지난 tasks에 남은 같은 이름의 커밋까지 이 task의 커밋으로 잡는다"를 문제로 적었다. retro 본문 자체의 고칠 거리라 이 task의 범위 밖(plate 자체의 하네스 고칠 거리)이고 고치지 않았다
- 같은 헤드리스 retro는 "완료 조건의 확인(`| wc -l` → `1`)이 줄 수만 본다"를 시험 레포 계획의 문제로 적었다. 시험 레포에 일부러 둔 꼴이라 이 저장소의 문제가 아니다

## 하네스에서 걸린 것
- 완료 조건 3의 retro 헤드리스 시험에서 retro가 #80 규칙대로 그 경우를 `경계 밖`으로 적어 판정은 "통과"로 나왔다. 기대("회고 절의 문제나 `FRICTION.md`의 경계 밖")는 채웠지만, 목표를 해치는 결함이 회고 판정을 통과시키는 꼴이다
- 헤드리스 retro가 retro의 "task의 커밋" 낱말이 지난 tasks의 같은 이름 커밋을 잡는다고 짚었다. 같은 #80 꼴(이름으로 커밋을 찾음)이 retro 자신의 낱말에도 있다
