# 회고

## 회고 1

**확인**
- 1. run 1번의 tasks 브랜치 항목은 브랜치를 만들거나 바꾼 뒤, origin과 `origin/<기본 브랜치>`가 있고 로컬 기본 브랜치에 거기 없는 커밋이 있으면 그 커밋을 보여 주고 되돌릴지 묻는다. 승인하면 되돌리고, 거절하면 그대로 잇는다. 커밋은 tasks 브랜치에 남는다. 알아보는 명령과 되돌리는 명령이 본문에 적혀 있다.
  - `mktemp -d` 안에서 `git init -b main src`에 빈 커밋, `git clone --bare src remote.git`, `git clone remote.git c`, 복제본 `main`에 빈 커밋 `plan: x`를 더한 뒤 run 1번 3항목의 `git switch -c tasks/x`, `git remote get-url origin`, `git rev-parse --verify --quiet refs/remotes/origin/main`, `git log --oneline refs/remotes/origin/main..main`, `git branch -f main refs/remotes/origin/main`을 적힌 그대로 돌렸다 → origin 주소와 ref 해시가 나옴, 되돌리기 전 1개, 되돌린 뒤 0개, `git merge-base main tasks/x`가 `refs/remotes/origin/main`의 끝과 같음, `git log tasks/x`에 `plan: x`가 있음, 지금 브랜치 `tasks/x`, 임시 디렉터리 지움. 통과
- 2. run의 `RUNLOG.md` 절의 물은 자리 목록에 `기본 브랜치`가 있고, task에 걸리지 않는 물음으로 task 이름 자리에 "없음"을 적는다.
  - `plugins/plate/skills/run/SKILL.md`의 `RUNLOG.md` 절 → 물은 자리 목록 "`실행 방식`, `커밋하지 않은 변경`, `기본 브랜치`, …"와 task에 걸리지 않는 물음 "(실행 방식, 커밋하지 않은 변경, 기본 브랜치, 고칠지)"에 저마다 있다. 통과
- 3. run의 낱말 "작업 트리의 스킬 줄"과 review의 낱말 "갈라진 곳"이 로컬 기본 브랜치의 `git merge-base <기본 브랜치> HEAD`라고 적는다.
  - run 낱말 → "원격 추적 ref(`origin/{기본 브랜치}`)가 아니라 로컬 기본 브랜치와의 merge-base(`git merge-base {기본 브랜치} HEAD`)". review 낱말 → "`<기본 브랜치>`는 원격 추적 ref(`origin/<기본 브랜치>`)가 아니라 로컬 기본 브랜치다". 통과
- 4. `docs/ARCHITECTURE.md`와 `README.md`가 run의 새 물음과 맞는다.
  - `docs/ARCHITECTURE.md` "패턴과 규칙"의 "run은 기본 브랜치" 항목 → 새 물음, fetch 없음, origin·ref 없으면 묻지 않음, 커밋은 tasks 브랜치에 남음이 run 본문과 같다. "데이터 흐름"의 실행 줄 → 브랜치를 만들거나 바꾼 뒤의 물음 다음에 실행 방식을 묻는 차례가 run 1번→2번과 같다. `README.md` 표의 `run` 행 → 시작할 때 새 물음과 실행 방식을 묻는다고 적혀 어긋나지 않는다. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 104 tests`, `OK`. 통과

**남은 것**
- phase 1: `git branch -f {기본 브랜치} refs/remotes/origin/{기본 브랜치}`는 기본 브랜치가 다른 worktree에 체크아웃돼 있으면 실패하고 본문이 다루지 않는다 → 문제 아님 (이 물음은 지금 브랜치가 기본 브랜치여서 tasks 브랜치로 바꾼 뒤에만 나온다. git은 한 브랜치를 두 worktree에 체크아웃하지 않으므로, 이 worktree가 기본 브랜치에 있었다면 다른 worktree에는 없다)
- phase 1: `git branch -f`로 되돌리면 로컬 기본 브랜치의 upstream이 `origin/<기본 브랜치>`로 잡힌다 → 문제 아님 (이번 회고에서도 `branch 'main' set up to track 'origin/main'.`이 나왔다. 되돌린 대상과 같은 원격 브랜치를 추적하게 될 뿐이고, 목표와 결정, 맥락 문서 어디에도 upstream을 두고 약속한 것이 없다)
- phase 1: 에이전트가 묻고 답하는 부분(목록을 보여 주는 것, `RUNLOG.md`의 `기본 브랜치` 줄)은 돌리지 않았다 → 문제 아님 (task 머리와 tasks 머리의 결정이 셸로 재현되는 것만 돌리기로 했다)

**문제**
- run 1번 3항목은 "그 브랜치가 이미 있으면 `git switch tasks/<이름>`으로 바꾼다"의 뒤에도 같은 물음을 하고 "그 커밋은 이미 `tasks/<이름>`에 들어 있어서 되돌려도 tasks 브랜치에 남는다"고 적는다. 그런데 브랜치를 새로 만들지 않고 이미 있는 브랜치로 바꾼 경우에는 로컬 기본 브랜치의 앞선 커밋이 tasks 브랜치에 없을 수 있다. `mktemp -d`에서 복제본에 `git branch tasks/y`를 먼저 만들고 `main`에 `plan: add task`를 커밋한 뒤 `git switch tasks/y`를 하자 `git log --oneline refs/remotes/origin/main..main`은 1개를 냈고 `git log tasks/y`에는 그 커밋이 없었다(진행 중인 tasks에 task를 더하는 계획을 기본 브랜치에서 커밋한 경우다). 이때 승인하면 `git branch -f`가 그 커밋을 어느 브랜치에도 없게 만들어, 결정의 이유 "커밋은 tasks 브랜치에 남는다"가 틀린다 (`plugins/plate/skills/run/SKILL.md`). 기준: 결함

**판정**: 문제 있음

## 회고 2

**확인**
- 1. run 1번의 tasks 브랜치 항목은 브랜치를 만들거나 바꾼 뒤, origin과 `origin/<기본 브랜치>`가 있고 로컬 기본 브랜치에 거기 없는 커밋이 있으면 그 커밋을 보여 주고 되돌릴지 묻는다. 승인하면 되돌리고, 거절하면 그대로 잇는다. 커밋은 tasks 브랜치에 남는다. 알아보는 명령과 되돌리는 명령이 본문에 적혀 있다.
  - `mktemp -d` 안에서 `git init -b main src`에 빈 커밋, `git clone --bare src remote.git`, `git clone remote.git c`, 복제본 `main`에 빈 커밋 `plan: x`를 더한 뒤 run 1번 3항목의 `git switch -c tasks/x`, `git remote get-url origin`, `git rev-parse --verify --quiet refs/remotes/origin/main`, `git log --oneline refs/remotes/origin/main..main`, `git log --oneline tasks/x..main`, `git branch -f main refs/remotes/origin/main`을 적힌 그대로 돌렸다 → origin 주소와 ref 해시가 나옴, 되돌리기 전 1개, tasks 브랜치에 없는 커밋 0개(묻는 갈래), 되돌린 뒤 0개, `git merge-base main tasks/x`가 `refs/remotes/origin/main`의 끝과 같음(`mergebase-ok`), `git log tasks/x`에 `plan: x`가 있음, 지금 브랜치 `tasks/x`, 임시 디렉터리 지움(`cleaned`). 통과
- 2. run의 `RUNLOG.md` 절의 물은 자리 목록에 `기본 브랜치`가 있고, task에 걸리지 않는 물음으로 task 이름 자리에 "없음"을 적는다.
  - `plugins/plate/skills/run/SKILL.md` 498줄 물은 자리 목록 "`실행 방식`, `커밋하지 않은 변경`, `기본 브랜치`, …"와 499줄 task에 걸리지 않는 물음 "(실행 방식, 커밋하지 않은 변경, 기본 브랜치, 고칠지)"에 저마다 있다. 통과
- 3. run의 낱말 "작업 트리의 스킬 줄"과 review의 낱말 "갈라진 곳"이 로컬 기본 브랜치의 `git merge-base <기본 브랜치> HEAD`라고 적는다.
  - run 47줄 → "원격 추적 ref(`origin/{기본 브랜치}`)가 아니라 로컬 기본 브랜치와의 merge-base(`git merge-base {기본 브랜치} HEAD`)". review 31줄 → "`<기본 브랜치>`는 원격 추적 ref(`origin/<기본 브랜치>`)가 아니라 로컬 기본 브랜치다". 통과
- 4. `docs/ARCHITECTURE.md`와 `README.md`가 run의 새 물음과 맞는다.
  - `docs/ARCHITECTURE.md` "패턴과 규칙"의 "run은 기본 브랜치" 항목 → 앞선 커밋이 모두 `tasks/<이름>`에 있으면 묻고, tasks 브랜치에 없는 커밋이 있으면 묻지 않고 그대로 둔다고 적어 run 본문 68~73줄과 같다. "데이터 흐름"의 실행 줄 → "계획의 커밋이 로컬 기본 브랜치에만 있으면 그 커밋을 보여 주고 로컬 기본 브랜치를 origin의 것으로 되돌릴지 묻는다". `README.md` 10줄 `run` 행 → "계획의 커밋이 로컬 기본 브랜치에만 있으면 로컬 기본 브랜치를 origin의 것으로 되돌릴지 … 묻고". 같은 임시 디렉터리에서 복제본에 `git branch tasks/y`, `main`에 빈 커밋 `plan: add task`, `git switch tasks/y`를 하자 `git log --oneline refs/remotes/origin/main..main`과 `git log --oneline tasks/y..main`이 둘 다 `plan: add task`를 냈다. 계획의 커밋이 로컬 기본 브랜치에만 있는데 run 본문은 이때 묻지 않으므로, 데이터 흐름의 실행 줄과 README의 `run` 행은 새 물음과 어긋난다. 실패
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 104 tests in 16.746s`, `OK`. 통과

**남은 것**
- phase 1: `git branch -f {기본 브랜치} refs/remotes/origin/{기본 브랜치}`는 기본 브랜치가 다른 worktree에 체크아웃돼 있으면 실패하고 본문이 다루지 않는다 → 문제 아님 (이 물음은 지금 브랜치가 기본 브랜치여서 tasks 브랜치를 만들거나 바꾼 뒤에만 나온다. git은 한 브랜치를 두 worktree에 체크아웃하지 않으므로 다른 worktree에는 기본 브랜치가 없다)
- phase 1: `git branch -f`로 되돌리면 로컬 기본 브랜치의 upstream이 `origin/<기본 브랜치>`로 잡힌다 → 문제 아님 (이번에도 `branch 'main' set up to track 'origin/main'.`이 나왔다. 되돌린 대상과 같은 원격 브랜치를 추적할 뿐이고 목표, 결정, 맥락 문서에 upstream을 두고 약속한 것이 없다)
- phase 1: 에이전트가 묻고 답하는 부분(목록을 보여 주는 것, `RUNLOG.md`의 `기본 브랜치` 줄)은 돌리지 않았다 → 문제 아님 (task 머리와 tasks 머리의 결정이 셸로 재현되는 것만 돌리기로 했다)
- phase 2: 이미 있던 tasks 브랜치로 바꿨고 기본 브랜치에 tasks 브랜치에 없는 커밋이 있으면 run은 알리기만 하고 그 커밋을 tasks 브랜치로 가져오지 않아, 그 커밋이 계획 파일을 더한 것이면 tasks 브랜치의 작업 트리에 그 계획이 없을 수 있다 → 문제 아님 (위의 임시 디렉터리에서 `tasks/y`에 `plan: add task`가 없는 것을 봤다. 커밋을 tasks 브랜치로 가져오는 일은 목표와 결정이 정한 경계(앞선 커밋을 보여 주고 되돌릴지 묻는 것) 밖이고, 이 task 전에도 같았다. `FRICTION.md`에 경계 밖으로 적는다)
- phase 2: 에이전트가 묻고 알리는 부분은 돌리지 않았다 → 문제 아님 (task 머리의 결정대로다)

**문제**
- 완료 조건 4의 확인이 실패했다. phase 2가 앞선 커밋 가운데 tasks 브랜치에 없는 것이 있으면 묻지 않게 바꿨는데, `docs/ARCHITECTURE.md` "데이터 흐름"의 실행 줄과 `README.md` 표의 `run` 행, run의 frontmatter description은 여전히 "계획의 커밋이 로컬 기본 브랜치에만 있으면 … 되돌릴지 묻는다"고만 적는다. 이미 있던 tasks 브랜치로 바꾼 갈래에서는 계획의 커밋이 로컬 기본 브랜치에만 있어도 묻지 않는다 (`docs/ARCHITECTURE.md`, `README.md`, `plugins/plate/skills/run/SKILL.md`). 기준: 확인 실패. 고칠 쪽: 문서 (tasks 머리와 task 머리의 결정의 이유 "커밋은 tasks 브랜치에 남는다"를 지키려면 그 갈래에서 묻지 않는 본문이 맞고, `docs/ARCHITECTURE.md` "패턴과 규칙" 항목은 이미 그렇게 적는다)
- task 머리의 목표와 완료 조건 1, tasks 머리의 완료 조건 4는 "로컬 기본 브랜치에 origin의 기본 브랜치에 없는 커밋이 있으면 그 커밋을 보여 주고 … 되돌릴지 묻는다"고 적는데, run 본문(`plugins/plate/skills/run/SKILL.md` 73줄)은 그 커밋 가운데 tasks 브랜치에 없는 것이 있으면 묻지 않는다. phase 2가 회고 1의 문제를 고치며 물음의 조건을 좁혔지만 계획은 그대로다 (`docs/tasks/003-base-branch/plan.md`, `docs/tasks/plan.md`). 기준: 계획. 고칠 쪽: 문서 (같은 결정의 이유 "커밋은 tasks 브랜치에 남는다"는 그 갈래에서 묻지 않아야만 참이다)

**판정**: 문제 있음

## 회고 3

**확인**
- 1. run 1번의 tasks 브랜치 항목은 브랜치를 만들거나 바꾼 뒤, origin과 `origin/<기본 브랜치>`가 있고 로컬 기본 브랜치에 거기 없는 커밋이 있고 그 커밋이 모두 `tasks/<이름>`에 있으면 그 커밋을 보여 주고 되돌릴지 묻는다. 승인하면 되돌리고, 거절하면 그대로 잇는다. `tasks/<이름>`에 없는 커밋이 있으면 묻지 않고 되돌리지 않고 알린다. 커밋은 tasks 브랜치에 남는다. 알아보는 명령과 되돌리는 명령이 본문에 적혀 있다.
  - `mktemp -d` 안에서 `git init -b main src`에 빈 커밋, `git clone --bare src remote.git`, `git clone remote.git c`, 복제본 `main`에 빈 커밋 `plan: x`를 더한 뒤 run 1번 3항목의 `git switch -c tasks/x`, `git remote get-url origin`, `git rev-parse --verify --quiet refs/remotes/origin/main`, `git log --oneline refs/remotes/origin/main..main`, `git log --oneline tasks/x..main`, `git branch -f main refs/remotes/origin/main`을 적힌 그대로 돌렸다 → origin 주소와 ref 해시가 나옴, 되돌리기 전 1개, tasks 브랜치에 없는 커밋 0개(묻는 갈래), 되돌린 뒤 0개, `git merge-base main tasks/x`가 `refs/remotes/origin/main`의 끝과 같음(`mergebase-ok`), `git log tasks/x`에 `plan: x`가 있음, 지금 브랜치 `tasks/x`. 통과
  - 같은 임시 디렉터리에 복제본 `d`를 만들어 `git branch tasks/y`, `main`에 빈 커밋 `plan: add task`, `git switch tasks/y` 뒤 두 알아보기 명령을 적힌 그대로 돌렸다 → `refs/remotes/origin/main..main` 1개, `tasks/y..main` 1개(묻지 않는 갈래), 그 뒤 `git log --oneline main`에 `plan: add task`가 있음. 임시 디렉터리 지움(`cleaned`). 통과
- 2. run의 `RUNLOG.md` 절의 물은 자리 목록에 `기본 브랜치`가 있고, task에 걸리지 않는 물음으로 task 이름 자리에 "없음"을 적는다.
  - `plugins/plate/skills/run/SKILL.md` 498줄 물은 자리 목록 "`실행 방식`, `커밋하지 않은 변경`, `기본 브랜치`, …"와 499줄 task에 걸리지 않는 물음 "(실행 방식, 커밋하지 않은 변경, 기본 브랜치, 고칠지)"에 저마다 있다. 통과
- 3. run의 낱말 "작업 트리의 스킬 줄"과 review의 낱말 "갈라진 곳"이 로컬 기본 브랜치의 `git merge-base <기본 브랜치> HEAD`라고 적는다.
  - run 47줄 → "원격 추적 ref(`origin/{기본 브랜치}`)가 아니라 로컬 기본 브랜치와의 merge-base(`git merge-base {기본 브랜치} HEAD`)". review 31줄 → "`<기본 브랜치>`는 원격 추적 ref(`origin/<기본 브랜치>`)가 아니라 로컬 기본 브랜치다". 통과
- 4. `docs/ARCHITECTURE.md`와 `README.md`가 run의 새 물음과 맞는다.
  - `docs/ARCHITECTURE.md` 50줄 "run은 기본 브랜치" 항목 → 앞선 커밋이 모두 `tasks/<이름>`에 있으면 묻고 tasks 브랜치에 없는 커밋이 있으면 묻지 않고 그대로 둔다고 적어 run 본문 67~71줄과 같다. 59~60줄 데이터 흐름의 실행 줄 → 브랜치를 만들거나 바꾼 뒤 같은 두 갈래를 적고 그다음 실행 방식을 묻는 차례가 run 1번→2번과 같다. `README.md` 10줄 `run` 행 → 같은 두 갈래를 적는다. 위 `tasks/y` 갈래(계획의 커밋이 로컬 기본 브랜치에만 있고 tasks 브랜치에 없음)도 세 곳 모두 "묻지 않고 그대로 둔다"에 든다. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 104 tests in 16.921s`, `OK`. 통과

**남은 것**
- phase 1: `git branch -f {기본 브랜치} refs/remotes/origin/{기본 브랜치}`는 기본 브랜치가 다른 worktree에 체크아웃돼 있으면 실패하고 본문이 다루지 않는다 → 문제 아님 (이 물음은 지금 브랜치가 기본 브랜치여서 tasks 브랜치를 만들거나 바꾼 뒤에만 나온다. git은 한 브랜치를 두 worktree에 체크아웃하지 않으므로 다른 worktree에는 기본 브랜치가 없다)
- phase 1: `git branch -f`로 되돌리면 로컬 기본 브랜치의 upstream이 `origin/<기본 브랜치>`로 잡힌다 → 문제 아님 (이번에도 `branch 'main' set up to track 'origin/main'.`이 나왔다. 되돌린 대상과 같은 원격 브랜치를 추적할 뿐이고 목표, 결정, 맥락 문서에 upstream을 두고 약속한 것이 없다)
- phase 1: 에이전트가 묻고 답하는 부분(목록을 보여 주는 것, `RUNLOG.md`의 `기본 브랜치` 줄)은 돌리지 않았다 → 문제 아님 (task 머리와 tasks 머리의 결정이 셸로 재현되는 것만 돌리기로 했다)
- phase 2: 이미 있던 tasks 브랜치로 바꿨고 기본 브랜치에 tasks 브랜치에 없는 커밋이 있으면 run은 알리기만 하고 그 커밋을 tasks 브랜치로 가져오지 않는다 → 문제 아님 (목표와 결정이 정한 경계 밖이다. `FRICTION.md`에 이미 `경계 밖` 줄이 있다)
- phase 2: 에이전트가 묻고 알리는 부분은 돌리지 않았다 → 문제 아님 (task 머리의 결정대로다)
- phase 3: run의 description이 919자에서 960자로 늘어 1024자 한도에 여유가 적다 → 문제 아님 (`sed -n '3p' … | wc -m`으로 960자를 봤다. 한도 안이고, 목표, 결정, 맥락 문서에 걸리지 않는다)

**문제**
- 없음

**판정**: 통과
