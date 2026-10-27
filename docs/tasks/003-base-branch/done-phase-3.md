# Phase 3: 회고 2의 문제를 고친다

**목표**: 회고 2에서 나온 문제를 모두 고친다.

**테스트 먼저**: 아니오 — 고칠 문제가 `docs/ARCHITECTURE.md`, `README.md`, `plugins/plate/skills/run/SKILL.md`(모두 `.md`)의 글뿐이라 코드 파일의 동작을 바꾸지 않는다

**읽을 것**
- `docs/tasks/003-base-branch/retro.md`의 `## 회고 1`부터 `## 회고 2`까지의 절
- `docs/ARCHITECTURE.md`
- `README.md`
- `plugins/plate/skills/run/SKILL.md`
- `docs/PRD.md`
- `docs/ADR.md`
- `docs/TOOLS.md`

**TODO**
- [x] 완료 조건 4의 확인이 실패했다. phase 2가 앞선 커밋 가운데 tasks 브랜치에 없는 것이 있으면 묻지 않게 바꿨는데, `docs/ARCHITECTURE.md` "데이터 흐름"의 실행 줄과 `README.md` 표의 `run` 행, run의 frontmatter description은 여전히 "계획의 커밋이 로컬 기본 브랜치에만 있으면 … 되돌릴지 묻는다"고만 적는다. 이미 있던 tasks 브랜치로 바꾼 갈래에서는 계획의 커밋이 로컬 기본 브랜치에만 있어도 묻지 않는다. 고칠 쪽은 문서다 (`docs/ARCHITECTURE.md`, `README.md`, `plugins/plate/skills/run/SKILL.md`)

**통과 조건**
- 회고 2의 문제가 모두 고쳐졌다.
  - 확인: 문제마다 적힌 곳을 다시 읽거나 돌린다
- 앞선 회고 1의 문제가 고친 대로 그대로다.
  - 확인: 회고 1의 문제마다 적힌 재현을 모두 다시 돌린다
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다

## 한 일
- 완료 조건 4의 확인이 실패했다(데이터 흐름의 실행 줄, README의 `run` 행, run의 description이 좁힌 물음과 어긋남): 세 곳을 "계획의 커밋이 로컬 기본 브랜치에만 있고 그 커밋이 모두 tasks 브랜치에 있으면 … 되돌릴지 묻고, tasks 브랜치에 없는 커밋이 있으면 묻지 않고 그대로 둔다"로 고쳤다 (`docs/ARCHITECTURE.md` 59줄, `README.md` 10줄, `plugins/plate/skills/run/SKILL.md` 3줄)

## 확인 결과
- 회고 2의 문제가 모두 고쳐졌다.
  - 문제 1: `docs/ARCHITECTURE.md` 59줄, `README.md` 10줄, run 3줄을 다시 읽음 → 셋 다 앞선 커밋이 모두 tasks 브랜치에 있을 때만 묻고 없는 커밋이 있으면 묻지 않고 그대로 둔다고 적어 run 본문 66~73줄, "패턴과 규칙" 50줄과 같다. `grep -rn "로컬 기본 브랜치에만 있으면" README.md docs/ARCHITECTURE.md plugins/` → 아무것도 나오지 않음. 통과
  - 문제 2(계획의 목표와 완료 조건): `docs/tasks/003-base-branch/plan.md`의 목표와 완료 조건 1, `docs/tasks/plan.md`의 완료 조건 4를 읽음 → 커밋 a16be0f(`plan: 003-base-branch 수정`)에서 이미 "그 커밋이 모두 tasks 브랜치에 있을 때는 … 묻고, tasks 브랜치에 없는 커밋이 있으면 묻지 않고 그대로 둔다"로 고쳐져 있다. 통과
- 앞선 회고 1의 문제가 고친 대로 그대로다.
  - `mktemp -d`에서 `git branch tasks/y` → `main`에 빈 커밋 `plan: add task` → `git switch tasks/y` 뒤 `git log --oneline refs/remotes/origin/main..main` 1개, `git log --oneline tasks/y..main` 1개(묻지 않는 갈래), `git log main`에 `plan: add task` 있음, 임시 디렉터리 지움(`cleaned2`). 통과
- task 머리의 완료 조건이 모두 참이다.
  - 1의 첫 확인: `mktemp -d`에서 `git init -b main src`·빈 커밋, `git clone --bare`, `git clone`, `main`에 `plan: x`, `git switch -c tasks/x`, `git remote get-url origin`(주소 나옴), `git rev-parse --verify --quiet refs/remotes/origin/main`(해시 나옴), `git log --oneline refs/remotes/origin/main..main` → `before: 1`, `git log --oneline tasks/x..main` → `notin: 0`, `git branch -f main refs/remotes/origin/main` → `after: 0`, `mergebase-ok`, `git log tasks/x`에 `plan: x`, 지금 브랜치 `tasks/x`, `cleaned`. 통과
  - 1의 둘째 확인: 위 회고 1 재현과 같은 실행 → 두 알아보기가 둘 다 1개, 기본 브랜치에 커밋 남음, 임시 디렉터리 지움. 통과
  - 2: run 498줄 물은 자리 목록에 `기본 브랜치`, 499줄 task에 걸리지 않는 물음에 "기본 브랜치". 통과
  - 3: run 47줄 "원격 추적 ref(`origin/{기본 브랜치}`)가 아니라 로컬 기본 브랜치와의 merge-base(`git merge-base {기본 브랜치} HEAD`)", review 31줄 "`<기본 브랜치>`는 원격 추적 ref(`origin/<기본 브랜치>`)가 아니라 로컬 기본 브랜치다". 통과
  - 4: `docs/ARCHITECTURE.md` 50줄 "run은 기본 브랜치" 항목, 59줄 데이터 흐름의 실행 줄, `README.md` 10줄 `run` 행 → 모두 run 본문의 좁힌 물음과 어긋나지 않는다. 통과
  - 명령 절: 빌드 없음, 린트 없음, 테스트 `python3 -m unittest discover -s tests` → `Ran 104 tests in 17.496s`, `OK`. 통과

## 계획과 달라진 점
- 없음

## 남은 것
- run의 description이 919자에서 960자로 늘었다. 스킬 description의 1024자 한도 안이지만 남은 여유가 적다

## 하네스에서 걸린 것
- 통과 조건 "회고 2의 문제가 모두 고쳐졌다"에는 회고 2의 둘째 문제(계획의 글)도 드는데 TODO에는 첫째 문제만 있다. 둘째 문제는 고칠 phase를 더한 계획 커밋(a16be0f)이 이미 고쳤고, 절대 규칙 3 때문에 이 phase는 계획을 고칠 수 없어 읽어서 확인만 했다

## 확인 1

**통과 조건**
- 회고 2의 문제가 모두 고쳐졌다.
  - 문제 1: `docs/ARCHITECTURE.md` 59줄(데이터 흐름의 실행 줄), `README.md` 10줄(`run` 행), `plugins/plate/skills/run/SKILL.md` 3줄(description)을 읽음 → 셋 다 "계획의 커밋이 로컬 기본 브랜치에만 있고 그 커밋이 모두 tasks 브랜치에 있으면 … 되돌릴지 묻고, tasks 브랜치에 없는 커밋이 있으면 묻지 않고 그대로 둔다"고 적어 run 본문 66~71줄과 같다. `grep -rn "로컬 기본 브랜치에만 있으면" README.md docs/ARCHITECTURE.md plugins/` → 나온 것 없음(rc=1). 통과
  - 문제 2: `docs/tasks/003-base-branch/plan.md`의 목표와 완료 조건 1, `docs/tasks/plan.md`의 완료 조건 4를 읽음 → 셋 다 "그 커밋이 모두 tasks 브랜치에 있을 때는 … 묻고, tasks 브랜치에 없는 커밋이 있으면 묻지 않고 그대로 둔다"고 적는다(커밋 a16be0f). 통과
- 앞선 회고 1의 문제가 고친 대로 그대로다.
  - `mktemp -d`에서 bare 원격의 복제본 `d`에 `git branch tasks/y` → `main`에 빈 커밋 `plan: add task` → `git switch tasks/y` → `git log --oneline refs/remotes/origin/main..main` 1개, `git log --oneline tasks/y..main` 1개(묻지 않고 되돌리지 않는 갈래), `git log --oneline main`에 `plan: add task` 있음. 임시 디렉터리 지움(`cleaned`). 통과
- task 머리의 완료 조건이 모두 참이다.
  - 1의 첫 확인: `mktemp -d`에서 `git init -b main src`·빈 커밋, `git clone --bare`, `git clone`, 복제본 `main`에 `plan: x`, `git switch -c tasks/x`, `git remote get-url origin`(주소 나옴), `git rev-parse --verify --quiet refs/remotes/origin/main`(해시 나옴), `git log --oneline refs/remotes/origin/main..main` → 1개, `git log --oneline tasks/x..main` → 0개, `git branch -f main refs/remotes/origin/main` → 0개, `git merge-base main tasks/x`가 `refs/remotes/origin/main`과 같음(`mergebase-ok`), `git log tasks/x`에 `plan: x`, 지금 브랜치 `tasks/x`, 임시 디렉터리 지움. 통과
  - 1의 둘째 확인: 위 회고 1 재현과 같은 실행 → 두 알아보기 둘 다 1개, 그 뒤 기본 브랜치에 커밋 있음, 임시 디렉터리 지움. 통과
  - 2: run 498줄 물은 자리 목록에 `기본 브랜치`, 499줄 task에 걸리지 않는 물음에 "기본 브랜치". 통과
  - 3: run 47줄 "원격 추적 ref(`origin/{기본 브랜치}`)가 아니라 로컬 기본 브랜치와의 merge-base(`git merge-base {기본 브랜치} HEAD`)", review 31줄 "`<기본 브랜치>`는 원격 추적 ref(`origin/<기본 브랜치>`)가 아니라 로컬 기본 브랜치다". 통과
  - 4: `docs/ARCHITECTURE.md` 50줄 "run은 기본 브랜치" 항목, 59줄 데이터 흐름의 실행 줄, `README.md` 10줄 `run` 행을 읽음 → 모두 앞선 커밋이 모두 tasks 브랜치에 있을 때만 묻고 없는 커밋이 있으면 묻지 않고 그대로 둔다는 run 본문과 어긋나지 않는다. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 104 tests in 17.825s`, `OK`. 통과

**남은 것**
- 없음

**실패**
- 없음

**하네스에서 걸린 것**
- 기록의 "남은 것"의 줄(run의 description이 960자로 1024자 한도에 가깝다)은 동작의 결함이나 돌려 보지 않은 위험이 아니라 여유에 대한 메모여서 고르지 않았다(`wc -m`으로 960자를 봤다)

**판정**: 통과
