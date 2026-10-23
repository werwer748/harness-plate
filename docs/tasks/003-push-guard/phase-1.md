# Phase 1: 푸시 훅

**목표**: 에이전트의 Bash 호출이 기본 브랜치로 푸시하면 plate의 훅이 막는다.

**테스트 먼저**: 예

**읽을 것**
- `plugins/plate/hooks/edit_guard.py` (셋업 판정, git 호출, 종료 코드 2로 막는 꼴)
- `plugins/plate/hooks/hooks.json` (훅을 거는 꼴과 스크립트가 없을 때의 처리)
- `tests/test_edit_guard.py` (훅 테스트의 꼴)
- `docs/TOOLS.md`의 "훅" (종료 코드, stderr가 에이전트에게 가는 꼴, 셸 꼴의 명령)
- `docs/ADR.md`의 ADR-019 (Python 3 표준 라이브러리와 unittest)
- https://code.claude.com/docs/en/hooks (Bash의 PreToolUse가 받는 입력)
- `docs/PRD.md` (목표), `docs/ARCHITECTURE.md` (기술 스택, 디렉터리 구조, 패턴과 규칙의 막는 장치)

**TODO**
- [x] 푸시 훅의 테스트가 생긴다. 막는 경우(기본 브랜치에 있는 채 대상 없이 하는 push, 기본 브랜치를 가리키는 push, 기본 브랜치를 지우는 push, 이어진 명령과 `git -C` 안의 push)와 막지 않는 경우(다른 브랜치, origin 밖 원격, 셋업 안 된 프로젝트)를 본다 (`tests/`)
- [x] 푸시 훅이 Bash 호출의 명령을 읽어 기본 브랜치로 가는 push면 종료 코드 2로 막고, 무엇을 왜 막았는지 stderr로 알린다 (`plugins/plate/hooks/` 아래)
- [x] hooks.json이 Bash의 PreToolUse에 푸시 훅을 건다 (`plugins/plate/hooks/hooks.json`)
- [x] PRD의 목표와 ARCHITECTURE의 기술 스택, 디렉터리 구조, 막는 장치가 푸시 훅을 적는다 (`docs/PRD.md`, `docs/ARCHITECTURE.md`)

**통과 조건**
- 완료 조건 1, 2, 3, 4가 참이다.
  - 확인: 완료 조건 1, 2, 3, 4의 확인을 모두 돌린다

## 한 일
- 푸시 훅의 테스트가 생긴다: 막는 경우(기본 브랜치에 있는 채 대상 없이 하는 push와 `2>&1 | tail` 꼴, `main`·`HEAD:main`·`x:refs/heads/main`·`+x:main`을 가리키는 push, `--delete`·`-d`·`:main`·`:refs/heads/main`으로 지우는 push, `&&`·`;`·`||`·줄바꿈으로 이어진 명령 안의 push, `git -C <폴더>` 안의 push와 그 폴더의 기본 브랜치)와 막지 않는 경우(다른 브랜치, origin 밖 원격, 셋업 안 된 프로젝트, push가 아닌 명령과 따옴표 안의 글, git 레포 밖, 명령이 없는 호출), 기본 브랜치를 origin의 HEAD → `main` → `master`로 고르는 것, hooks.json의 Bash 명령을 `sh -c`로 돌린 결과를 보는 테스트를 썼다. 프로젝트를 만드는 도우미는 `tests/test_edit_guard.py`의 `Project`, `GIT_ENV`를 가져다 쓴다 (`tests/test_push_guard.py`)
- 푸시 훅이 Bash 호출의 명령을 읽어 기본 브랜치로 가는 push면 종료 코드 2로 막고, 무엇을 왜 막았는지 stderr로 알린다: `shlex`로 명령을 `&&`, `||`, `;`, `|`, `&`, 괄호, 줄바꿈에서 나누고 리다이렉션과 그 대상(`2>&1`의 `2` 포함)을 뺀 뒤, `git [-C 폴더] push`면 그 폴더의 git 최상위가 셋업돼 있고(`edit_guard.py`의 `is_setup`, `git`을 가져다 쓴다) 원격이 origin일 때(대상 없는 push는 `branch.<b>.pushRemote` → `remote.pushDefault` → `branch.<b>.remote` → origin) refspec의 대상이나 지우는 브랜치가 기본 브랜치이거나, refspec 없이 기본 브랜치에 있으면 막는다. stderr는 막은 브랜치와 명령, 까닭(끝의 평가와 보고까지 가지 않은 변경이 기본 브랜치에 들어가지 않게 한다)과 할 일(다른 브랜치로 푸시하고 합치는 것은 사용자에게 맡긴다)이다 (`plugins/plate/hooks/push_guard.py`)
- hooks.json이 Bash의 PreToolUse에 푸시 훅을 건다: 편집 훅 뒤에 matcher `Bash`인 항목을 더했고, 명령은 편집 훅과 같은 꼴(스크립트 파일이 없으면 `python3`를 부르지 않고 0으로 끝난다)이다 (`plugins/plate/hooks/hooks.json`)
- PRD의 목표와 ARCHITECTURE의 기술 스택, 디렉터리 구조, 막는 장치가 푸시 훅을 적는다: PRD 목표의 훅이 막는 것에 "에이전트가 기본 브랜치에 하는 푸시"를 더했다. ARCHITECTURE의 기술 스택에 두 훅 스크립트 이름을, 디렉터리 구조에 `push_guard.py`와 `test_push_guard.py`와 hooks.json의 Bash 항목을, 막는 장치에 푸시 훅이 막는 것과 막지 않는 것을 적었다. 훅이 둘이 되어 "훅은 파일 편집 도구의 호출만 보고"를 "편집 훅(`edit_guard.py`)은 …"으로, `test_edit_guard.py`의 설명을 "편집 훅의 테스트"로 바꿨다 (`docs/PRD.md`, `docs/ARCHITECTURE.md`)
- 테스트 먼저
  - 실패: `python3 -m unittest discover -s tests` → `FAIL: test_push_to_default_branch (test_push_guard.BlockTest.test_push_to_default_branch)` 등 푸시 훅의 시험 20개가 모두 실패(`can't open file '.../plugins/plate/hooks/push_guard.py': [Errno 2] No such file or directory`, hooks.json 시험은 `AssertionError: 0 != 1 : Bash의 PreToolUse에 건 훅이 하나여야 한다`), `Ran 76 tests in 21.721s` / `FAILED (failures=50)`
  - 통과: `python3 -m unittest discover -s tests` → push_guard.py만 쓴 뒤 `FAILED (failures=3)`(hooks.json 시험 3개), hooks.json을 고친 뒤 `Ran 76 tests in 29.178s` / `OK`

## 확인 결과
- 완료 조건 1, 2, 3, 4가 참이다.
  - 완료 조건 1: `python3 -m unittest discover -s tests` → `Ran 76 tests in 28.015s` / `OK`. 통과
  - 완료 조건 1: `tests/test_push_guard.py`를 읽음 → 대상 없는 push(`test_push_without_target_on_default_branch`, `test_push_head_while_on_default_branch`), 기본 브랜치를 가리키는 push(`test_push_to_default_branch`), 지우는 push의 `--delete`와 `:main` 꼴(`test_delete_default_branch`), `&&`·`;` 안의 push(`test_push_inside_chained_command`), `git -C` 안의 push와 그 폴더의 기본 브랜치(`test_push_inside_git_c_uses_that_folder`, `test_git_c_folder_has_its_own_default_branch`), 다른 브랜치(`test_push_to_other_branch`), origin 밖 원격(`test_push_to_remote_other_than_origin`), 셋업 안 된 프로젝트(`test_project_not_set_up`)가 있고, 막는 시험은 모두 종료 코드 2와 stderr의 "기본 브랜치"를 본다. 통과
  - 완료 조건 2: `python3 -c "import json; h=json.load(open('plugins/plate/hooks/hooks.json')); print([m['matcher'] for m in h['hooks']['PreToolUse']])"` → `['Edit|Write|MultiEdit|NotebookEdit', 'Bash']`. 통과
  - 완료 조건 2: hooks.json의 Bash 명령을 읽음 → `f="${CLAUDE_PLUGIN_ROOT}/hooks/push_guard.py"; [ -f "$f" ] || exit 0; exec python3 "$f"`로 편집 훅과 같은 꼴이고, `HooksJsonTest.test_missing_script_exits_zero`가 스크립트 없는 폴더에서 0을 본다. 통과
  - 완료 조건 3: `git diff -w -- docs/PRD.md docs/ARCHITECTURE.md`로 PRD의 목표, ARCHITECTURE의 기술 스택, 디렉터리 구조, 패턴과 규칙의 막는 장치를 읽음 → 네 곳 모두 푸시 훅을 적는다. 통과
  - 완료 조건 4: `python3 -m unittest discover -s tests` → `OK`(위와 같다). `git diff --stat HEAD -- tests/test_verdict.py plugins/plate/ci/` → 출력 없음(바뀌지 않음), `python3 -m unittest discover -s tests -p 'test_verdict.py'` → `Ran 14 tests` / `OK`. 통과
- 덧붙여 이 레포에서 훅을 직접 돌림: `git push origin main` → 종료 코드 2와 까닭, `git push -u origin tasks/pr-ci`와 tasks 브랜치에서의 `git push` → 0

## 계획과 달라진 점
- 없음

## 남은 것
- 없음

## 하네스에서 걸린 것
- 없음
