# Phase 7: 회고 6의 문제를 고친다

**목표**: 회고 6에서 나온 문제를 모두 고친다.

**테스트 먼저**: 아니오 — task 머리의 결정대로 훅을 고치지 않고 `docs/ARCHITECTURE.md`만 고친다

**읽을 것**
- `docs/tasks/003-push-guard/retro.md`의 `## 회고 6` 절
- `plugins/plate/hooks/push_guard.py`
- `tests/test_push_guard.py`
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/ADR.md`
- `docs/TOOLS.md`

**TODO**
- [x] 훅을 고치지 않고 약속 밖의 꼴로 적는다(task 머리의 결정). `docs/ARCHITECTURE.md`의 막는 장치에서 푸시 훅의 약속을 `tests/test_push_guard.py`의 시험이 다루는 꼴로 고쳐 적고, 그 밖의 셸 구문과 git의 표기는 약속하지 않는다고 적고, `heads/<이름>`으로 적은 대상을 약속 밖의 예로 든다. 문제: 기본 브랜치를 `heads/<이름>`으로 적은 push를 막지 않는다. git은 refspec의 이름을 `refs/<이름>` 규칙으로도 풀어 `heads/main`을 `refs/heads/main`으로 읽는데, `target_refs`(227~237줄)는 `refs/`로 시작하지 않는 대상에 `refs/heads/`를 붙여(237줄) `refs/heads/heads/main`으로 견준다. 스크래치에 로컬 bare origin과 문서 지도 구간이 있는 레포(`main`이 origin보다 한 커밋 앞서고 지금 브랜치는 `tasks/x`)를 만들고 `git push origin heads/main`, `git push origin tasks/x:heads/main`, `git push origin :heads/main`, `git push origin --delete heads/main`을 훅에 넣으니 넷 다 0이었고, 같은 명령의 `git push`를 `git push --dry-run --porcelain`으로 바꿔 bash에 돌리니 앞의 둘은 `refs/heads/main:refs/heads/main`과 `refs/heads/tasks/x:refs/heads/main`을, 뒤의 둘은 `:refs/heads/main [deleted]`를 냈다. phase 1(`f8f219b`)의 훅도 0이다. 완료 조건 1의 "기본 브랜치를 가리키는 push"와 "기본 브랜치를 지우는 push"에 들고, 셸 구문이 아니라 git의 refspec이라 task 머리 다섯째 결정의 약속 밖("그 밖의 셸 구문")에 들지 않는다 (`plugins/plate/hooks/push_guard.py`, `docs/ARCHITECTURE.md`)
- [x] 훅을 고치지 않고 약속 밖의 꼴로 적는다(task 머리의 결정). 같은 글에 `--repo`로 적은 원격을 약속 밖의 예로 든다. 문제: 기본 브랜치에 있는 채 `--repo`로 origin 밖 원격을 적은 push를 막는다. `git push --repo=<원격>`은 위치 인자의 `<repository>`와 같은데, `push_args`(168~196줄)는 `--repo=…`를 다른 `--` 옵션처럼 넘기고(184~185줄) `--repo <원격>`은 값을 건너뛰기만 해서(28줄, 182~183줄), `blocked_branch`가 원격을 설정의 `origin`으로 보고(259줄) 대상이 없으니 기본 브랜치에 있다는 까닭으로 막는다(265줄). 같은 스크래치에 bare 원격 `fork`를 더하고 `main`에서 `git push --repo=fork`와 `git push --repo fork`를 훅에 넣으니 둘 다 "plate: 기본 브랜치(`main`)로 푸시하지 않는다"와 종료 코드 2였고, bash의 `--dry-run --porcelain`은 둘 다 `fork.git`으로만 `refs/heads/main:refs/heads/main [new branch]`를 냈다. 같은 자리의 `git push fork`는 0이다(`test_push_to_remote_other_than_origin`도 같다). phase 1(`f8f219b`)의 훅도 2다. 완료 조건 1의 "origin 밖 원격으로의 푸시는 막지 않는다"에 들고 셸 구문이 아니다 (`plugins/plate/hooks/push_guard.py`, `docs/ARCHITECTURE.md`)

**통과 조건**
- 회고 6의 문제가 모두 고쳐졌다. 두 문제는 `docs/ARCHITECTURE.md`의 막는 장치에 약속 밖의 꼴로 적힌 것이 고친 것이다.
  - 확인: 문제마다 적힌 곳을 다시 읽거나 돌린다
- `docs/ARCHITECTURE.md`의 막는 장치가 푸시 훅의 약속을 `tests/test_push_guard.py`의 시험이 다루는 꼴로 적고, 그 밖의 셸 구문과 git의 표기는 약속하지 않는다고 적는다. 약속 밖의 꼴은 이 phase의 통과를 가르지 않는다.
  - 확인: `docs/ARCHITECTURE.md`의 막는 장치를 읽어 task 머리의 결정과 견준다
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다

## 한 일
- 훅을 고치지 않고 약속 밖의 꼴로 적는다(task 머리의 결정). `heads/<이름>`으로 적은 대상: `docs/ARCHITECTURE.md`의 막는 장치(48줄)에서 "푸시 훅이 막는다고 약속하는 꼴은 여기까지 적은 것뿐이고, 그 밖의 셸 구문은 약속하지 않는다"를 "푸시 훅이 막는다고, 또는 막지 않는다고 약속하는 꼴은 `tests/test_push_guard.py`의 시험이 다루는 꼴뿐이고, 여기까지 적은 막는 것과 막지 않는 것도 그 꼴로 읽는다. 그 밖의 셸 구문과 git의 표기는 약속하지 않는다"로 고치고, 결함으로 보지 않는 예에 "`heads/<이름>`으로 적은 대상(git은 `refs/heads/<이름>`으로 읽는데 훅은 막지 않는다)"을 git의 표기로 더했다. 훅과 테스트는 고치지 않았다 (`docs/ARCHITECTURE.md`)
- 훅을 고치지 않고 약속 밖의 꼴로 적는다(task 머리의 결정). `--repo`로 적은 원격: 같은 글의 git의 표기 예에 "`--repo`로 적은 원격(훅은 원격을 origin으로 보고 기본 브랜치에서는 막는다)"을 더했다 (`docs/ARCHITECTURE.md`)

## 확인 결과
- 회고 6의 문제가 모두 고쳐졌다. 두 문제는 `docs/ARCHITECTURE.md`의 막는 장치에 약속 밖의 꼴로 적힌 것이 고친 것이다.
  - 스크래치에 로컬 bare `origin.git`, `fork.git`과 문서 지도 구간이 있는 레포(`main`이 origin보다 한 커밋 앞서고 지금 브랜치 `tasks/x`)를 만들어 훅에 넣음 → `git push origin heads/main`, `git push origin tasks/x:heads/main`, `git push origin :heads/main`, `git push origin --delete heads/main` 넷 다 0. 같은 명령의 `git push --dry-run --porcelain` → `refs/heads/main:refs/heads/main`, `refs/heads/tasks/x:refs/heads/main`, `:refs/heads/main [deleted]` 둘. `main`에서 `git push --repo=fork`, `git push --repo fork` → 둘 다 2, `git push fork` → 0. 같은 둘의 `--dry-run --porcelain` → 둘 다 `fork.git`으로 `refs/heads/main:refs/heads/main [new branch]`. 회고 6에 적힌 대로 훅은 그대로이고, `docs/ARCHITECTURE.md` 48줄이 두 꼴을 결함으로 보지 않는 git의 표기 예로 적는다. 통과
- `docs/ARCHITECTURE.md`의 막는 장치가 푸시 훅의 약속을 `tests/test_push_guard.py`의 시험이 다루는 꼴로 적고, 그 밖의 셸 구문과 git의 표기는 약속하지 않는다고 적는다. 약속 밖의 꼴은 이 phase의 통과를 가르지 않는다.
  - `docs/ARCHITECTURE.md` 48줄을 읽어 task 머리의 여섯째 결정과 견줌 → "막는다고, 또는 막지 않는다고 약속하는 꼴은 `tests/test_push_guard.py`의 시험이 다루는 꼴뿐", 앞에 적은 막는 것과 막지 않는 것(완료 조건 1의 경우와 같다)도 그 꼴로 읽는다는 것, "그 밖의 셸 구문과 git의 표기는 약속하지 않는다", 예로 `heads/<이름>`으로 적은 대상과 `--repo`로 적은 원격, 결함으로 보지 않는다는 것이 있다. 다섯째 결정의 heredoc·주석·줄 잇기, 명령 치환의 읽기, 나누지 못한 명령의 막음도 그대로 있다. 통과
- task 머리의 완료 조건이 모두 참이다.
  - 완료 조건 1: `python3 -m unittest discover -s tests` → `Ran 89 tests in 34.455s` / `OK`. `tests/test_push_guard.py`를 읽음 → 대상 없이 하는 push(`test_push_without_target_on_default_branch` 90줄), 기본 브랜치를 가리키는 push(`test_push_to_default_branch` 102줄), 지우는 push(`test_delete_default_branch` 123줄의 `--delete`, `:main`), 이어진 명령 안의 push(`test_push_inside_chained_command` 198줄의 `&&`, `;`), `git -C` 안의 push(`test_push_inside_git_c_uses_that_folder` 228줄, `test_git_c_folder_has_its_own_default_branch` 236줄), 다른 브랜치(`test_push_to_other_branch` 269줄), origin 밖 원격(`test_push_to_remote_other_than_origin` 300줄), 셋업 안 된 프로젝트(`test_project_not_set_up` 345줄)가 있다. `python3 -m unittest discover -s tests -p 'test_push_guard.py'` → `Ran 33 tests in 18.283s` / `OK`. 통과
  - 완료 조건 2: `python3 -c "import json; h=json.load(open('plugins/plate/hooks/hooks.json')); print([m['matcher'] for m in h['hooks']['PreToolUse']])"` → `['Edit|Write|MultiEdit|NotebookEdit', 'Bash']`. `plugins/plate/hooks/hooks.json` 18줄의 명령은 9줄의 편집 훅과 스크립트 이름만 다른 `[ -f "$f" ] || exit 0` 꼴이고, 그 명령을 `CLAUDE_PLUGIN_ROOT=/nonexistent`로 `sh -c`에 돌림 → `exit=0`. 통과
  - 완료 조건 3: `docs/PRD.md` 4줄의 목표("에이전트가 기본 브랜치에 하는 푸시"), `docs/ARCHITECTURE.md`의 기술 스택 5줄(`push_guard.py`), 디렉터리 구조 19, 21, 34줄, 막는 장치 48줄을 읽음 → 모두 푸시 훅을 적는다. 통과
  - 완료 조건 4: `python3 -m unittest discover -s tests` → `OK`(위와 같다). `git diff --stat f8f219b^ HEAD -- tests/test_verdict.py plugins/plate/ci/`와 `git diff --stat -- tests/test_verdict.py plugins/plate/ci/` → 둘 다 출력 없음. `python3 -m unittest discover -s tests -p 'test_verdict.py'` → `Ran 14 tests in 0.746s` / `OK`. 통과

## 계획과 달라진 점
없음

## 남은 것
없음

## 하네스에서 걸린 것
없음

## 확인 1

**통과 조건**
- 회고 6의 문제가 모두 고쳐졌다. 두 문제는 `docs/ARCHITECTURE.md`의 막는 장치에 약속 밖의 꼴로 적힌 것이 고친 것이다.
  - 스크래치에 로컬 bare `origin.git`, `fork.git`과 문서 지도 구간이 있는 레포(`main`이 origin보다 한 커밋 앞서고 지금 브랜치 `tasks/x`)를 만들어 훅에 넣음 → `git push origin heads/main`, `git push origin tasks/x:heads/main`, `git push origin :heads/main`, `git push origin --delete heads/main` 넷 다 0. 같은 명령의 `git push --dry-run --porcelain` → `refs/heads/main:refs/heads/main`, `refs/heads/tasks/x:refs/heads/main`, `:refs/heads/main [deleted]` 둘. `main`에서 `git push --repo=fork`, `git push --repo fork` → 둘 다 2와 "plate: 기본 브랜치(`main`)로 푸시하지 않는다", `git push fork` → 0. 같은 셋의 `--dry-run --porcelain` → 모두 `fork.git`으로 `refs/heads/main:refs/heads/main [new branch]`. 회고 6에 적힌 동작 그대로이고, `git show --stat HEAD`(phase 7 커밋 `955d6cb`)는 `docs/ARCHITECTURE.md`와 `phase-7.md`만 바꿨다(훅과 테스트는 그대로). `docs/ARCHITECTURE.md` 48줄이 "`heads/<이름>`으로 적은 대상(git은 `refs/heads/<이름>`으로 읽는데 훅은 막지 않는다), `--repo`로 적은 원격(훅은 원격을 origin으로 보고 기본 브랜치에서는 막는다) 같은 git의 표기에서 놓치거나 잘못 막는 것은 결함으로 보지 않는다"로 두 꼴을 약속 밖에 적는다. 통과
- `docs/ARCHITECTURE.md`의 막는 장치가 푸시 훅의 약속을 `tests/test_push_guard.py`의 시험이 다루는 꼴로 적고, 그 밖의 셸 구문과 git의 표기는 약속하지 않는다고 적는다. 약속 밖의 꼴은 이 phase의 통과를 가르지 않는다.
  - `docs/ARCHITECTURE.md` 48줄을 읽어 task 머리의 다섯째, 여섯째 결정과 견줌 → "푸시 훅이 막는다고, 또는 막지 않는다고 약속하는 꼴은 `tests/test_push_guard.py`의 시험이 다루는 꼴뿐이고, 여기까지 적은 막는 것과 막지 않는 것도 그 꼴로 읽는다. 그 밖의 셸 구문과 git의 표기는 약속하지 않는다", 예로 매개변수 확장·산술 명령과 `heads/<이름>`·`--repo`, 결함으로 보지 않는다는 것, heredoc·주석·줄 잇기, 명령 치환의 읽기, 나누지 못한 명령의 막음, 기본은 스킬의 "푸시하지 않는다" 규칙이라는 것이 있다. 결정과 어긋나는 곳 없음. 통과
- task 머리의 완료 조건이 모두 참이다.
  - 완료 조건 1: `python3 -m unittest discover -s tests` → `Ran 89 tests in 34.129s` / `OK`. `tests/test_push_guard.py`를 읽음 → 대상 없이 하는 push(`test_push_without_target_on_default_branch` 90줄), 기본 브랜치를 가리키는 push(`test_push_to_default_branch` 102줄), 지우는 push(`test_delete_default_branch` 123줄의 `--delete`, `-d`, `:main`, `:refs/heads/main`), 이어진 명령 안의 push(`test_push_inside_chained_command` 198줄의 `&&`, `;`), `git -C` 안의 push와 그 폴더의 기본 브랜치(228줄, 236줄), 다른 브랜치(`test_push_to_other_branch` 269줄), origin 밖 원격(`test_push_to_remote_other_than_origin` 300줄), 셋업 안 된 프로젝트(`test_project_not_set_up` 345줄)가 있고, `assertBlocked`가 종료 코드 2와 stderr의 "기본 브랜치"를 본다. `python3 -m unittest discover -s tests -p 'test_push_guard.py'` → `Ran 33 tests in 18.305s` / `OK`. 통과
  - 완료 조건 2: `python3 -c "import json; h=json.load(open('plugins/plate/hooks/hooks.json')); print([m['matcher'] for m in h['hooks']['PreToolUse']])"` → `['Edit|Write|MultiEdit|NotebookEdit', 'Bash']`. `plugins/plate/hooks/hooks.json` 18줄은 9줄과 스크립트 이름만 다른 `[ -f "$f" ] || exit 0; exec python3 "$f"` 꼴이고, 그 명령을 `CLAUDE_PLUGIN_ROOT=/nonexistent`로 `sh -c`에 돌림 → `exit=0`. 통과
  - 완료 조건 3: `docs/PRD.md` 4줄의 목표("에이전트가 기본 브랜치에 하는 푸시"), `docs/ARCHITECTURE.md`의 기술 스택 5줄(`push_guard.py`), 디렉터리 구조 19, 21, 34줄, 막는 장치 48줄을 읽음 → 모두 푸시 훅을 적는다. 통과
  - 완료 조건 4: `python3 -m unittest discover -s tests` → `OK`(위와 같다). `git diff --stat f8f219b^ HEAD -- tests/test_verdict.py plugins/plate/ci/`와 `git diff --stat -- tests/test_verdict.py plugins/plate/ci/` → 둘 다 출력 없음. `python3 -m unittest discover -s tests -p 'test_verdict.py'` → `Ran 14 tests in 0.741s` / `OK`. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 89 tests in 34.129s` / `OK`. 통과

**실패**
- 없음

**하네스에서 걸린 것**
- 없음

**판정**: 통과
