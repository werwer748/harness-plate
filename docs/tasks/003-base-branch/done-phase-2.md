# Phase 2: 회고 1의 문제를 고친다

**목표**: 회고 1에서 나온 문제를 모두 고친다.

**테스트 먼저**: 아니오 — 고칠 문제가 `plugins/plate/skills/run/SKILL.md`(`.md`)의 본문뿐이라 코드 파일의 동작을 바꾸지 않는다

**읽을 것**
- `docs/tasks/003-base-branch/retro.md`의 `## 회고 1`부터 `## 회고 1`까지의 절
- `plugins/plate/skills/run/SKILL.md`
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/ADR.md`
- `docs/TOOLS.md`

**TODO**
- [x] run 1번 3항목은 "그 브랜치가 이미 있으면 `git switch tasks/<이름>`으로 바꾼다"의 뒤에도 같은 물음을 하고 "그 커밋은 이미 `tasks/<이름>`에 들어 있어서 되돌려도 tasks 브랜치에 남는다"고 적는다. 그런데 브랜치를 새로 만들지 않고 이미 있는 브랜치로 바꾼 경우에는 로컬 기본 브랜치의 앞선 커밋이 tasks 브랜치에 없을 수 있다. `mktemp -d`에서 복제본에 `git branch tasks/y`를 먼저 만들고 `main`에 `plan: add task`를 커밋한 뒤 `git switch tasks/y`를 하자 `git log --oneline refs/remotes/origin/main..main`은 1개를 냈고 `git log tasks/y`에는 그 커밋이 없었다(진행 중인 tasks에 task를 더하는 계획을 기본 브랜치에서 커밋한 경우다). 이때 승인하면 `git branch -f`가 그 커밋을 어느 브랜치에도 없게 만들어, 결정의 이유 "커밋은 tasks 브랜치에 남는다"가 틀린다 (`plugins/plate/skills/run/SKILL.md`)

**통과 조건**
- 회고 1의 문제가 모두 고쳐졌다.
  - 확인: 문제마다 적힌 곳을 다시 읽거나 돌린다
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다

## 한 일
- run 1번 3항목의 앞선 커밋 물음: 앞선 커밋이 나오면 `git log --oneline tasks/<이름>..{기본 브랜치}`로 그 커밋이 모두 tasks 브랜치에 있는지 먼저 보게 했다. 아무것도 내지 않을 때만 목록을 보여 주고 되돌릴지 묻고(승인·거절 항목은 그 아래로 옮겼다), 커밋을 내면 묻지 않고 되돌리지 않으며 목록과 함께 로컬 기본 브랜치를 그대로 두고 잇는다고 알린다. 그래서 "커밋은 tasks 브랜치에 남는다"가 물을 때마다 참이다 (`plugins/plate/skills/run/SKILL.md`)
- `docs/ARCHITECTURE.md` "패턴과 규칙"의 "run은 기본 브랜치" 항목에 "그 커밋이 모두 `tasks/<이름>`에 있으면" 묻고, tasks 브랜치에 없는 커밋이 있으면 묻지 않고 그대로 둔다는 것을 더했다 (`docs/ARCHITECTURE.md`)

## 확인 결과
- 회고 1의 문제가 모두 고쳐졌다.
  - `mktemp -d`에서 복제본 `main`을 원격과 맞춘 뒤 `git branch tasks/y`, `main`에 빈 커밋 `plan: add task`, `git switch tasks/y`를 하고 run 1번 3항목의 명령을 돌렸다 → `git log --oneline refs/remotes/origin/main..main`이 `d3e2bdf plan: add task`, `git log --oneline tasks/y..main`도 `d3e2bdf plan: add task`를 내서 본문대로면 묻지 않고 `git branch -f`를 하지 않는다. 그 커밋은 `main`에 남는다. `plugins/plate/skills/run/SKILL.md` 66~72줄을 다시 읽어 "남는다"는 글이 모두 tasks 브랜치에 있을 때의 물음에만 붙었다. 통과
- task 머리의 완료 조건이 모두 참이다.
  - 1: 같은 임시 디렉터리에서 `git init -b main src`, `git clone --bare src remote.git`, `git clone remote.git c`, `main`에 `plan: x` 뒤 `git switch -c tasks/x`, `git remote get-url origin`, `git rev-parse --verify --quiet refs/remotes/origin/main`, `git log --oneline refs/remotes/origin/main..main`, `git log --oneline tasks/x..main`, `git branch -f main refs/remotes/origin/main` → origin 주소와 ref 해시가 나옴, 되돌리기 전 1개, tasks에 없는 커밋 0개(묻는 갈래), 되돌린 뒤 0개, `git merge-base main tasks/x`가 원격 끝과 같음(`mergebase-ok`), `git log tasks/x`에 `plan: x`가 있음, 지금 브랜치 `tasks/x`, 임시 디렉터리 지움(`cleaned`). 통과
  - 2: `grep -n` → run 498줄 물은 자리 목록과 499줄 task에 걸리지 않는 물음에 저마다 `기본 브랜치`. 통과
  - 3: run 낱말 "작업 트리의 스킬 줄"(47줄) "원격 추적 ref(`origin/{기본 브랜치}`)가 아니라 로컬 기본 브랜치와의 merge-base", review 31줄 "`<기본 브랜치>`는 원격 추적 ref(`origin/<기본 브랜치>`)가 아니라 로컬 기본 브랜치다". 통과
  - 4: `docs/ARCHITECTURE.md` 50줄(고친 뒤)이 run 본문의 두 갈래와 같다. 59줄 실행 줄 "계획의 커밋이 로컬 기본 브랜치에만 있으면 … 되돌릴지 묻는다"와 `README.md` 표의 `run` 행 "계획의 커밋이 로컬 기본 브랜치에만 있으면 로컬 기본 브랜치를 origin의 것으로 되돌릴지" 묻는다는 글은 tasks 브랜치에도 있는 커밋을 두고 묻는 지금 본문과 어긋나지 않는다(로컬 기본 브랜치와 원격 사이에만 있는 커밋). 통과
  - 명령 절의 테스트: `python3 -m unittest discover -s tests` → `Ran 104 tests`, `OK`

## 계획과 달라진 점
- TODO가 적은 파일은 `plugins/plate/skills/run/SKILL.md`뿐이지만 `docs/ARCHITECTURE.md` 50줄도 고쳤다. 그 항목이 앞선 커밋이 있으면 늘 묻는다고 적혀 있어 고친 본문과 어긋나, 통과 조건(완료 조건 4)을 지키려면 맞춰야 했다

## 남은 것
- 이미 있던 tasks 브랜치로 바꿨고 기본 브랜치에 tasks 브랜치에 없는 커밋이 있으면, run은 알리기만 하고 그 커밋을 tasks 브랜치로 가져오지 않는다. 그 커밋이 계획 파일을 더한 것이면 tasks 브랜치의 작업 트리에 그 계획이 없을 수 있다. 가져오는 방법(합치기, cherry-pick)을 고르는 것은 이 task의 결정에 없어서 하지 않았다
- 에이전트가 묻고 알리는 부분은 돌리지 않았다(task 머리의 결정대로 셸로 재현되는 것만 돌렸다)

## 하네스에서 걸린 것
- 없음

## 확인 1

**통과 조건**
- 회고 1의 문제가 모두 고쳐졌다.
  - `mktemp -d`에서 `git init -b main src`(빈 커밋), `git clone --bare src remote.git`, `git clone remote.git c`, 복제본에 `git branch tasks/y`, `main`에 빈 커밋 `plan: add task`, `git switch tasks/y` 뒤 run 1번 3항목의 명령을 돌렸다 → `git remote get-url origin`과 `git rev-parse --verify --quiet refs/remotes/origin/main`이 값을 냄, `git log --oneline refs/remotes/origin/main..main`이 `b3af827 plan: add task`, `git log --oneline tasks/y..main`도 `b3af827 plan: add task`를 내서 본문(`plugins/plate/skills/run/SKILL.md` 70~72줄의 "커밋을 내면 묻지 않고 되돌리지 않는다")대로면 `git branch -f`를 하지 않아 그 커밋은 `main`에 남는다. "되돌려도 tasks 브랜치에 남는다"는 글은 `tasks/<이름>..{기본 브랜치}`가 아무것도 내지 않는 갈래(66~69줄)에만 붙어 있다. 통과
- task 머리의 완료 조건이 모두 참이다.
  - 1: 같은 임시 디렉터리에서 새 복제본 `main`에 빈 커밋 `plan: x`, `git switch -c tasks/x`, `git remote get-url origin`, `git rev-parse --verify --quiet refs/remotes/origin/main`, `git log --oneline refs/remotes/origin/main..main`, `git log --oneline tasks/x..main`, `git branch -f main refs/remotes/origin/main`을 적힌 그대로 돌렸다 → 되돌리기 전 1개, tasks에 없는 커밋 0개(묻는 갈래), 되돌린 뒤 0개, `git merge-base main tasks/x`가 `refs/remotes/origin/main`의 끝과 같음(`mergebase-ok`), `git log tasks/x`에 `35eb084 plan: x`, 지금 브랜치 `tasks/x`, 임시 디렉터리 지움(`cleaned`). 통과
  - 2: `plugins/plate/skills/run/SKILL.md` 498줄 물은 자리 목록 "`실행 방식`, `커밋하지 않은 변경`, `기본 브랜치`, …", 499줄 task에 걸리지 않는 물음 "(실행 방식, 커밋하지 않은 변경, 기본 브랜치, 고칠지)"에 저마다 있다. 통과
  - 3: run 낱말 "작업 트리의 스킬 줄" → "원격 추적 ref(`origin/{기본 브랜치}`)가 아니라 로컬 기본 브랜치와의 merge-base(`git merge-base {기본 브랜치} HEAD`)". review 31줄 "갈라진 곳" → "`<기본 브랜치>`는 원격 추적 ref(`origin/<기본 브랜치>`)가 아니라 로컬 기본 브랜치다". 통과
  - 4: `docs/ARCHITECTURE.md` 50줄 "run은 기본 브랜치" 항목 → 앞선 커밋이 모두 `tasks/<이름>`에 있으면 묻고, 없는 커밋이 있으면 묻지 않고 그대로 둔다, fetch 없음, origin·ref 없으면 묻지 않음이 run 본문과 같다. "데이터 흐름" 실행 줄 → 브랜치를 만들거나 바꾼 뒤 되돌릴지 묻고 그다음 실행 방식을 묻는 차례가 run 1번→2번과 같다. `README.md` 10줄 `run` 행 → 시작할 때 되돌릴지와 실행 방식을 묻는다는 요약이 본문과 어긋나지 않는다. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 104 tests in 16.735s`, `OK`. 통과

**남은 것**
- 이미 있던 tasks 브랜치로 바꿨고 기본 브랜치에 tasks 브랜치에 없는 커밋이 있으면, run은 알리기만 하고 그 커밋을 tasks 브랜치로 가져오지 않는다 → 통과 조건(회고 1의 문제, 완료 조건 1~4)이 보는 동작은 되돌릴 때 커밋이 tasks 브랜치에 남는지이고, 그 커밋을 가져오는 일은 목표와 결정에 없어 걸리지 않는다. 하네스에서 걸린 것
- 에이전트가 묻고 알리는 부분은 돌리지 않았다 → task 머리의 결정("셸로 재현되는 것만 돌린다")대로 통과 조건의 확인이 셸 명령만 보므로 걸리지 않는다. 하네스에서 걸린 것

**실패**
- 없음

**하네스에서 걸린 것**
- 남은 것: 이미 있던 tasks 브랜치로 바꿨고 기본 브랜치에 tasks 브랜치에 없는 커밋(예: 진행 중인 tasks에 task를 더한 계획의 커밋)이 있으면 run은 알리기만 하고 가져오지 않아, tasks 브랜치의 작업 트리에 그 계획이 없을 수 있다. 가져오는 방법(합치기, cherry-pick)은 이 task의 결정에 없다
- 남은 것: 에이전트가 묻고 알리는 부분(목록을 보여 주는 것, `RUNLOG.md`의 `기본 브랜치` 줄)은 돌리지 않았다

**판정**: 통과
