# Phase 1: run과 review에 로컬 기본 브랜치를 다루는 글을 넣는다

**목표**: run 1번이 앞선 커밋을 알리고 되돌릴지 묻고, 두 스킬의 낱말과 맥락 문서, README가 그와 맞는다.

**테스트 먼저**: 아니오 — `.md`(스킬 본문과 문서)만 고친다

**읽을 것**
- `plugins/plate/skills/run/SKILL.md` (고칠 스킬. frontmatter의 description, 낱말 "기본 브랜치"와 "작업 트리의 스킬 줄", 1번의 "tasks 브랜치", `RUNLOG.md` 절)
- `plugins/plate/skills/review/SKILL.md` (낱말 "기본 브랜치"와 "갈라진 곳")
- `docs/ARCHITECTURE.md` ("패턴과 규칙"에서 "run은 기본 브랜치"로 시작하는 항목, "데이터 흐름"의 실행 줄)
- `README.md` (표의 `run` 행)
- `docs/TOOLS.md`의 "Claude Code" 절에서 run의 시험 폴더가 셋업 커밋과 계획 커밋을 로컬 `main`에 둔 채 tasks 브랜치를 가른 일을 적은 줄 (이 문제가 처음 드러난 곳)
- `gh issue view 29` (#29의 본문)

**TODO**
- [x] run 1번의 "tasks 브랜치" 항목에, 브랜치를 만들거나 바꾼 뒤 origin과 `origin/<기본 브랜치>`가 있고 로컬 기본 브랜치에 거기 없는 커밋이 있으면 그 커밋을 보여 주고 로컬 기본 브랜치를 `origin/<기본 브랜치>`로 되돌릴지 묻는 글이 더해진다. 알아보는 명령, 되돌리는 명령, 승인과 거절 뒤의 길, 커밋이 tasks 브랜치에 남는다는 것, `git fetch`를 하지 않는다는 것이 함께 적힌다 (`plugins/plate/skills/run/SKILL.md`)
- [x] run의 `RUNLOG.md` 절의 물은 자리 목록과 task에 걸리지 않는 물음의 목록에 `기본 브랜치`가 더해진다 (`plugins/plate/skills/run/SKILL.md`)
- [x] run의 낱말 "작업 트리의 스킬 줄"과 review의 낱말 "갈라진 곳"이 로컬 기본 브랜치(원격 추적 ref가 아님)의 `git merge-base <기본 브랜치> HEAD`라고 밝히도록 바뀐다 (`plugins/plate/skills/run/SKILL.md`, `plugins/plate/skills/review/SKILL.md`)
- [x] run의 frontmatter의 description이 새 물음과 어긋나면 맞게 바뀐다 (`plugins/plate/skills/run/SKILL.md`)
- [x] `docs/ARCHITECTURE.md`의 "패턴과 규칙"에서 "run은 기본 브랜치"로 시작하는 항목과 "데이터 흐름"의 실행 줄에 새 물음이 더해지고, `README.md`의 표의 `run` 행이 새 물음과 어긋나면 맞게 바뀐다 (`docs/ARCHITECTURE.md`, `README.md`)

**통과 조건**
- 완료 조건 1이 참이다.
  - 확인: `mktemp -d` 안에 bare 원격과 그 복제본을 만들고, 복제본의 기본 브랜치에 원격에 없는 커밋 하나를 더한 뒤 run 1번에 적힌 브랜치 만들기, 알아보기, 되돌리기 명령을 적힌 그대로 돌린다. 되돌리기 전에는 알아보기가 커밋 1개를, 되돌린 뒤에는 0개를 내고, 되돌린 뒤 `git merge-base <기본 브랜치> tasks/<이름>`이 원격 기본 브랜치의 끝이고, `git log tasks/<이름>`에 그 커밋이 있다. 하나라도 다르면 실패. 임시 디렉터리는 지운다
- 완료 조건 2가 참이다.
  - 확인: `plugins/plate/skills/run/SKILL.md`의 `RUNLOG.md` 절을 읽어 물은 자리 목록과 task에 걸리지 않는 물음의 목록에 저마다 `기본 브랜치`가 있다
- 완료 조건 3이 참이다.
  - 확인: run의 낱말 "작업 트리의 스킬 줄"과 review의 낱말 "갈라진 곳"을 읽어 둘 다 로컬 기본 브랜치의 merge-base라고 적는다. 하나라도 없으면 실패
- 완료 조건 4가 참이다.
  - 확인: `docs/ARCHITECTURE.md`의 "패턴과 규칙"에서 "run은 기본 브랜치"로 시작하는 항목과 "데이터 흐름"의 실행 줄, `README.md`의 표의 `run` 행을 하나씩 읽어 새 물음과 어긋나지 않는다

## 한 일
- run 1번의 "tasks 브랜치" 항목에 앞선 커밋을 알리고 되돌릴지 묻는 글: 브랜치를 만들거나 바꾼 뒤 `git remote get-url origin`과 `git rev-parse --verify --quiet refs/remotes/origin/{기본 브랜치}`로 견줄 것이 있는지 보고(`git fetch`는 하지 않는다), `git log --oneline refs/remotes/origin/{기본 브랜치}..{기본 브랜치}`로 알아보고, 커밋이 있으면 보여 주고 되돌릴지 묻는 글과, 승인하면 `git branch -f {기본 브랜치} refs/remotes/origin/{기본 브랜치}`, 거절하면 그대로 잇는 두 길, 커밋이 tasks 브랜치에 남는다는 것을 더했다 (`plugins/plate/skills/run/SKILL.md`)
- run의 `RUNLOG.md` 절: 물은 자리 목록과 task에 걸리지 않는 물음 목록에 `기본 브랜치`를 더했다 (`plugins/plate/skills/run/SKILL.md`)
- 두 낱말: run의 "작업 트리의 스킬 줄"에 갈라진 곳이 원격 추적 ref가 아니라 로컬 기본 브랜치와의 merge-base(`git merge-base {기본 브랜치} HEAD`)라는 문장을, review의 "갈라진 곳"에 `<기본 브랜치>`가 원격 추적 ref가 아니라 로컬 기본 브랜치이고 원격보다 앞서 있어도 로컬의 것으로 잡는다는 문장을 더했다 (`plugins/plate/skills/run/SKILL.md`, `plugins/plate/skills/review/SKILL.md`)
- run의 description: "`tasks/<이름>` 브랜치에서" 뒤에 "(계획의 커밋이 로컬 기본 브랜치에만 있으면 로컬 기본 브랜치를 origin의 것으로 되돌릴지 묻는다)"를 더했다 (`plugins/plate/skills/run/SKILL.md`)
- 맥락 문서와 README: ARCHITECTURE "패턴과 규칙"의 "run은 기본 브랜치" 항목에 새 물음(fetch 없음, origin이나 ref가 없으면 묻지 않음, 커밋은 tasks 브랜치에 남음)을 더하고, "데이터 흐름"의 실행 줄을 브랜치를 만들거나 바꾼 뒤의 새 물음 → 실행 방식 물음의 차례로 고쳤다. README 표의 `run` 행에 새 물음을 더했다 (`docs/ARCHITECTURE.md`, `README.md`)

## 확인 결과
- 완료 조건 1이 참이다.
  - `mktemp -d` 안에서 `git init -b main src`에 빈 커밋을 넣고 `git clone --bare src remote.git`, `git clone remote.git c`를 만든 뒤 복제본의 `main`에 빈 커밋 `plan: x`를 더하고, run 1번에 적힌 대로 `git switch -c tasks/x`, `git remote get-url origin`, `git rev-parse --verify --quiet refs/remotes/origin/main`, `git log --oneline refs/remotes/origin/main..main`, `git branch -f main refs/remotes/origin/main`을 돌렸다 → 되돌리기 전 `before: 1`, 되돌린 뒤 `after: 0`, `git merge-base main tasks/x`가 원격 기본 브랜치의 끝과 같음(`merge-base=remote tip OK`), `git log tasks/x`에 그 커밋이 있음(`plan commit in tasks/x OK`), 임시 디렉터리 지움(`cleaned`). 통과
- 완료 조건 2가 참이다.
  - `plugins/plate/skills/run/SKILL.md`의 `RUNLOG.md` 절 → 물은 자리 목록 "`실행 방식`, `커밋하지 않은 변경`, `기본 브랜치`, …"와 task에 걸리지 않는 물음 "(실행 방식, 커밋하지 않은 변경, 기본 브랜치, 고칠지)"에 저마다 있다. 통과
- 완료 조건 3이 참이다.
  - run의 "작업 트리의 스킬 줄" → "갈라진 곳은 원격 추적 ref(`origin/{기본 브랜치}`)가 아니라 로컬 기본 브랜치와의 merge-base(`git merge-base {기본 브랜치} HEAD`)다". review의 "갈라진 곳" → "`<기본 브랜치>`는 원격 추적 ref(`origin/<기본 브랜치>`)가 아니라 로컬 기본 브랜치다". 통과
- 완료 조건 4가 참이다.
  - `docs/ARCHITECTURE.md`의 "run은 기본 브랜치" 항목 → 새 물음과 그 조건(fetch 없음, origin·ref 없으면 묻지 않음, 커밋은 tasks 브랜치에 남음)이 run 본문과 맞다. "데이터 흐름"의 실행 줄 → 브랜치를 만들거나 바꾼 뒤의 물음 다음에 실행 방식을 묻는 차례로 run 1번→2번과 맞다. `README.md` 표의 `run` 행 → 시작할 때 새 물음과 실행 방식을 묻는다고 적혀 어긋나지 않는다. 통과

## 계획과 달라진 점
- 없음

## 남은 것
- `git branch -f {기본 브랜치} refs/remotes/origin/{기본 브랜치}`는 기본 브랜치가 다른 worktree에 체크아웃돼 있으면 실패한다. 본문은 그 경우를 다루지 않는다
- 확인에서 `git branch -f`가 `branch 'main' set up to track 'origin/main'.`을 냈다. 원격 추적 ref로 되돌리면 그 브랜치의 upstream이 `origin/<기본 브랜치>`로 잡힌다(이미 그랬던 복제본에서는 바뀌는 것이 없다)
- 에이전트가 묻고 답하는 부분(목록을 보여 주는 것, `RUNLOG.md`의 `기본 브랜치` 줄)은 돌리지 않았다. task 머리의 결정대로다

## 하네스에서 걸린 것
- 확인을 처음 돌릴 때 bare 원격에 `git push -q origin main`으로 첫 커밋을 넣으려 하자 plate의 푸시 훅(`push_guard.py`)이 기본 브랜치로의 푸시라며 막았다. 임시 디렉터리의 원격이어도 막는다. `git clone --bare`로 원격을 만들어 푸시 없이 돌렸다. 통과 조건의 확인 글은 원격을 어떻게 채우는지 적지 않아서, 다음 확인도 같은 훅에 걸릴 수 있다
