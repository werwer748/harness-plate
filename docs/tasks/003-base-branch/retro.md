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
