# 회고

## 회고 1

**확인**
- 1. 보고서 경로를 작업 트리의 `docs/cleanup/`만 보고 정해, 같은 날 합쳐지지 않은 cleanup 브랜치가 있을 때 기본 브랜치에서 다시 부르면 보고서 파일 이름이 같아 add/add 충돌이 나고 지난 보고서 읽기도 그 보고서를 놓친다
  - `mktemp -d` 시험 레포에서 `docs/cleanup/2026-10-29.md`를 커밋한 `cleanup/2026-10-29`를 합치지 않은 채 `main`으로 돌아가 본문 1번의 명령을 차례로 돌림(`ls docs/cleanup/2026-10-29.md`, `git for-each-ref --format='%(refname:short)' refs/heads/cleanup/`, `git cat-file -e cleanup/2026-10-29:docs/cleanup/2026-10-29.md`, `git cat-file -e cleanup/2026-10-29:docs/cleanup/2026-10-29-2.md`) → 작업 트리에 없음(rc 1), 목록 `cleanup/2026-10-29`, 첫 이름 rc 0(쓰임), `-2` rc 128(안 쓰임) → 새 경로 `docs/cleanup/2026-10-29-2.md`. 5번 `git rev-parse --verify --quiet refs/heads/cleanup/2026-10-29-2` → rc 1 → `cleanup/2026-10-29-2`. 두 브랜치를 차례로 `main`에 `git merge` → 둘 다 rc 0, `docs/cleanup/`에 두 파일, `git status --porcelain` 빈 출력. 통과
  - 본문 2번(`plugins/plate/skills/cleanup/SKILL.md` 72줄)을 읽음 → "아직 기본 브랜치에 합쳐지지 않은 cleanup 브랜치의 보고서도 지난 보고서로 본다", `git ls-tree --name-only {브랜치} docs/cleanup/`, `git show {브랜치}:{경로}`. 시험 레포에서 `git ls-tree --name-only cleanup/2026-10-29 docs/cleanup/` → `docs/cleanup/2026-10-29.md`. 통과
- 2. cleanup의 "기본 브랜치"·"GitHub 원격" 정의와 plan·cleanup의 "cleanup 브랜치" 정의가 같은지 지키는 시험이 있다
  - `python3 -m unittest -v tests.test_cleanup_skill.SharedDefinitionsTest` → 2개 OK. 통과
  - `cp -R` 사본 셋에서 cleanup 낱말의 "기본 브랜치" 줄(`` `origin` `` → `origin`), "GitHub 원격" 줄(`URL` → `주소`), "cleanup 브랜치" 줄(`` -2` `` → `` .2` ``)을 저마다 한 줄 바꿔 `python3 -m unittest tests.test_cleanup_skill.SharedDefinitionsTest` → 셋 모두 `FAILED (failures=1)`. 통과
- 3. cleanup 합침 갈래, run 보낼 곳 합침의 충돌 되돌림, #80의 retro 규칙에 돌려 보는 확인이 있다
  - `mktemp -d` 시험 레포에서 cleanup "고른 발견이 없을 때"의 `git switch main`, `git merge cleanup/2026-10-29`, `git merge --abort`, `git branch -d cleanup/2026-10-29`를 차례로 → 충돌 없음: merge rc 0, `git merge-base --is-ancestor {끝 커밋} main` rc 0, 지운 뒤 `git rev-parse --verify --quiet refs/heads/cleanup/2026-10-29` rc 1 빈 출력. 충돌: merge rc 1, abort rc 0, `main` 해시 전과 같음, 작업 트리 깨끗. 통과
  - `mktemp -d` 시험 레포에서 run "보낼 곳으로 합친다"를 충돌 갈래로(`git rev-parse --verify --quiet refs/heads/cleanup/x` rc 0, `git switch cleanup/x`, `git merge --no-ff -m 'y: 보낼 곳으로 합침' tasks/y` rc 1, `git merge --abort`, `git switch tasks/y`) → `cleanup/x` 해시 전과 같음, `tasks/y` 남고 해시 같음, 지금 브랜치 `tasks/y`. 통과
  - 헤드리스 시험: 스크래치의 새 시험 레포(지난 tasks의 `605a74f 001-report: phase 1`이 남고, 이번 task `001-report`의 결정대로 `git log --reverse … | head -n 1`을 쓰는 `find_phase.sh`가 이번 `6b51435` 대신 `605a74f`를 냄)에서 `claude -p "/plate:retro docs/tasks/001-report" --plugin-dir /Users/hugo/Desktop/harness-plate/plugins/plate --permission-mode bypassPermissions --output-format json`(Claude Code 2.1.312, retro 본문 sha256 `aff04746d43734c45bd190c2fdb8cff8ffc3ebc5ef7f191b7b75b5b97473a8e8`) → `판정: 통과`, `문제: 0개`. 시험 레포 `docs/tasks/FRICTION.md`에 "`001-report` 경계 밖: … `sh find_phase.sh 001-report 1`이 이번 tasks의 수행 커밋 `6b51435`가 아니라 지난 tasks의 `605a74f`를 낸다. 목표(…)를 해치고 …"가 적힘. `001-report: 회고` 커밋은 `retro.md`, `FRICTION.md`만 바꿈. 그 경우를 `FRICTION.md`의 경계 밖으로 적었다. 통과
  - 저장소 불변(`docs/tasks/RUNLOG.md`와 phase가 고친 파일을 빼고 본다): 헤드리스 시험 전후의 이 저장소 `git status --porcelain`과 `git rev-parse HEAD`를 `diff` → 빈 출력(변경 없음, HEAD `fad1955` 그대로). 통과
  - 돌리지 않음(plan 헤드리스): 계획이 돌리지 않기로 정함. 돌리지 않음
- 4. tasks 완료 조건 1~6이 참이다
  - tasks 1: `python3 -m unittest discover -s tests` → `Ran 271 tests`, 마지막 줄 `OK`. 통과
  - tasks 2: `grep -n '지난 tasks의 같은 이름' plugins/plate/skills/plan/SKILL.md plugins/plate/skills/retro/SKILL.md` → plan 115줄("6. 초안을 보여 주고 승인받는다", 102~136줄), plan 266줄("적는 규칙"의 **조건**, 260줄 아래), retro 79줄("4. task의 변경을 점검한다", 64~84줄). 통과
  - tasks 2: 그 줄을 `sed -i '' '/지난 tasks의 같은 이름/d'`로 지운 `cp -R` 사본에서 `python3 -m unittest discover -s tests -k test_80`(시험은 `tests/test_skill_rules.py`) → `FAILED (failures=4)`. 통과
  - tasks 2 돌리지 않음(plan·retro 끝까지의 헤드리스): 계획이 돌리지 않기로 정함. 돌리지 않음
  - tasks 3: `grep -n -F 'cleanup/<' plugins/plate/skills/cleanup/SKILL.md` → 절대 규칙 17·18줄, "5. 보고서를 쓰고 커밋한다" 115·127줄, "고른 발견이 없을 때" 149·153·154·155·161·163·165줄. 통과
  - tasks 3: `mktemp -d` 시험 레포 세 갈래 → `main`에서: `git rev-parse --verify --quiet refs/heads/cleanup/2026-10-29` rc 1, `git switch -c cleanup/2026-10-29`의 HEAD가 `main`과 같고 `main` 해시 그대로. `tasks/x`에서(같은 이름이 있음): `…cleanup/2026-10-29` rc 0, `…-2` rc 1 → `cleanup/2026-10-29-2`가 `tasks/x`의 HEAD에서 생김, `main` 해시 그대로, 옛 `cleanup/2026-10-29` 해시 그대로. 통과
  - tasks 3 돌리지 않음(cleanup 끝까지의 헤드리스): 계획이 돌리지 않기로 정함. 돌리지 않음
  - tasks 4: `grep -n '보낼 곳' plugins/plate/skills/plan/SKILL.md` → 55줄("1. 진행 중인 tasks가 있는지 본다"), 139줄("7. 쓰고 커밋한다"), 170줄("계획 파일의 양식"). 통과
  - tasks 4: `mktemp -d` 시험 레포 `cleanup/x`에서 `git branch --show-current` → `cleanup/x`, `git rev-parse --verify --quiet refs/heads/tasks/y` rc 1, `git switch -c tasks/y` → `git merge-base --is-ancestor cleanup/x tasks/y` rc 0, `main` 해시 그대로. 통과
  - tasks 4 돌리지 않음(plan 끝까지의 헤드리스): 계획이 돌리지 않기로 정함. 돌리지 않음
  - tasks 5: `grep -n '보낼 곳' plugins/plate/skills/run/SKILL.md` → "0. tasks를 본다" 69·71·73·75줄, "비운다" 499·505줄, "PR을 연다" 523줄, "합친다" 564줄. 통과
  - tasks 5: `mktemp -d` 시험 레포 → `cleanup/x`가 있을 때 `git rev-parse --verify --quiet refs/heads/cleanup/x` rc 0, `git switch cleanup/x`, `git merge --no-ff -m 'y: 보낼 곳으로 합침' tasks/y` rc 0, `git merge-base --is-ancestor tasks/y cleanup/x` rc 0, `main` 해시 그대로. `cleanup/x`를 지운 뒤 `git rev-parse --verify --quiet refs/heads/cleanup/x` → rc 1, 빈 출력(합치기 명령에 닿지 않음). 통과
  - tasks 5 돌리지 않음(run 끝까지의 헤드리스, PR): 계획이 돌리지 않기로 정함. 돌리지 않음
  - tasks 6: `grep -n -F 'cleanup/<' docs/PRD.md docs/ARCHITECTURE.md` → PRD 19줄(핵심 기능 9), ARCHITECTURE 56줄(plan 문단), 95·98줄(데이터 흐름의 정리 점검). 통과
  - tasks 6: `grep -n '보낼 곳' docs/PRD.md docs/ARCHITECTURE.md` → PRD 18줄(핵심 기능 8), ARCHITECTURE 57줄(run 문단), 81·84줄(데이터 흐름의 tasks 끝). 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 271 tests in 25.775s`, `OK`. 통과

**남은 것**
- phase 1: 1번의 이름 고르기는 로컬 cleanup 브랜치만 본다. 로컬 브랜치를 지운 채 origin에만 남은 cleanup 브랜치의 보고서는 보지 않아, 그 PR과 새 브랜치를 함께 합칠 때 같은 경로 충돌이 날 수 있다 → 문제 아님 (`경계 밖`: 완료 조건 1과 cleanup 낱말의 "cleanup 브랜치"가 정한 경계는 로컬 cleanup 브랜치이고 "고른 발견이 없을 때"의 PR 갈래도 로컬 브랜치를 지우지 않는다. 보고서 이름으로 파일을 찾는 동작에서 같은 이름이 origin에만 남은 경우라 retro 4번대로 경계 밖으로 모은다)
- phase 1: 헤드리스 retro가 retro의 "task의 커밋" 낱말이 지난 tasks에 남은 같은 이름의 커밋까지 이 task의 커밋으로 잡는다고 적었다 → 문제 아님 (범위: task 머리 범위 밖 "plate 자체의 하네스 고칠 거리를 고치는 것"에 들고, 이 task가 바꾼 동작이 아니다. 이번 헤드리스 시험에서도 같은 것이 재현돼 하네스 문제로 `FRICTION.md`에 모은다)
- phase 1: 헤드리스 retro가 "완료 조건의 확인(`| wc -l` → `1`)이 줄 수만 본다"를 시험 레포 계획의 문제로 적었다 → 문제 아님 (시험 레포에 일부러 둔 꼴이고 이 저장소의 변경이 아니다)

**문제**
- 없음

**판정**: 통과
