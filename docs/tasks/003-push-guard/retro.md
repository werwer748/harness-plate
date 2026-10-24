# 회고

## 회고 1

**확인**
- 셋업된 프로젝트에서 에이전트의 Bash 호출이 기본 브랜치로 푸시하면, 훅이 종료 코드 2로 막고 까닭을 stderr로 알린다. 막는 경우는 기본 브랜치에 있는 채 대상 없이 하는 push, 기본 브랜치를 가리키는 push, 기본 브랜치를 지우는 push(`--delete`, `:main` 꼴), `&&`나 `;`로 이어진 명령 안의 push, `git -C <폴더>` 안의 push(그 폴더의 기본 브랜치를 본다)다. 다른 브랜치로의 푸시, origin 밖 원격으로의 푸시, 셋업 안 된 프로젝트(`AGENTS.md`에 문서 지도 구간이 없다)의 푸시는 막지 않는다.
  - `python3 -m unittest discover -s tests` → `Ran 76 tests in 28.255s` / `OK`. 통과
  - `tests/test_push_guard.py`를 읽음 → 기본 브랜치에 있는 채 대상 없이 하는 push(`test_push_without_target_on_default_branch`의 `git push`, `git push origin`, `-u`, `--force`, `2>&1 | tail -5`, `test_push_head_while_on_default_branch`), 기본 브랜치를 가리키는 push(`test_push_to_default_branch`의 `main`, `HEAD:main`, `tasks/x:main`, `+tasks/x:main`, `tasks/x:refs/heads/main` 등), 지우는 push(`test_delete_default_branch`의 `--delete` 두 자리, `-d`, `:main`, `:refs/heads/main`), 이어진 명령 안의 push(`test_push_inside_chained_command`의 `&&`, `;`, 붙인 `;`, `||`, 줄바꿈), `git -C` 안의 push와 그 폴더의 기본 브랜치(`test_push_inside_git_c_uses_that_folder`, `test_git_c_folder_has_its_own_default_branch`는 `-C` 폴더의 기본 브랜치가 `trunk`일 때 `main`은 통과, `trunk`는 막음), 다른 브랜치(`test_push_to_other_branch`), origin 밖 원격(`test_push_to_remote_other_than_origin`), 셋업 안 된 프로젝트(`test_project_not_set_up`. `Project(setup=False)`는 `AGENTS.md`를 `# 지침`만으로 쓴다, `tests/test_edit_guard.py` 74줄)가 있다. 막는 시험은 `assertBlocked`로 종료 코드 2와 stderr의 "기본 브랜치"를 본다. `python3 -m unittest discover -s tests -p 'test_push_guard.py' -v` → 20개 모두 `ok`. 통과
- `plugins/plate/hooks/hooks.json`이 Bash의 PreToolUse에 푸시 훅을 건다. 스크립트 파일이 없으면 `python3`를 부르지 않고 0으로 끝나는 꼴은 `edit_guard.py`를 거는 것과 같다.
  - `python3 -c "import json; h=json.load(open('plugins/plate/hooks/hooks.json')); print([m['matcher'] for m in h['hooks']['PreToolUse']])"` → `['Edit|Write|MultiEdit|NotebookEdit', 'Bash']`. 통과
  - `plugins/plate/hooks/hooks.json`의 Bash 항목을 읽음 → `f="${CLAUDE_PLUGIN_ROOT}/hooks/push_guard.py"; [ -f "$f" ] || exit 0; exec python3 "$f"`로, 편집 훅의 명령과 스크립트 이름만 다르다. 같은 꼴을 없는 경로(`/nonexistent/hooks/push_guard.py`)로 `sh -c`에 돌리니 종료 코드 0. 통과
- `docs/PRD.md`의 목표와 `docs/ARCHITECTURE.md`의 기술 스택, 디렉터리 구조, 막는 장치가 푸시 훅을 적는다.
  - `docs/PRD.md`의 목표(4줄)와 `docs/ARCHITECTURE.md`의 기술 스택(5줄), 디렉터리 구조(19, 21, 34줄), 패턴과 규칙의 막는 장치(48줄)를 읽음 → PRD 목표에 "에이전트가 기본 브랜치에 하는 푸시", 기술 스택에 푸시 훅 `push_guard.py`, 디렉터리 구조에 hooks.json의 Bash 항목과 `push_guard.py`, `test_push_guard.py`, 막는 장치에 푸시 훅이 막는 것과 막지 않는 것, 사람의 푸시는 다루지 않는다는 것이 적혀 있다. 통과
- tasks 완료 조건 1의 단위 테스트가 그대로 통과한다. 이 task도 `tests/`를 고친다.
  - `python3 -m unittest discover -s tests` → `OK`(위와 같다). `git diff --stat 5a7c002 HEAD -- tests/test_verdict.py plugins/plate/ci/` → 출력 없음. task의 커밋(`f8f219b`, `95de405`, `1ac403e`)이 바꾼 파일에 둘이 없다. `python3 -m unittest discover -s tests -p 'test_verdict.py'` → `Ran 14 tests` / `OK`. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 76 tests in 28.255s` / `OK`. 통과
- 테스트 먼저 기록: phase 1
  - `done-phase-1.md`의 "한 일"의 테스트 먼저 → 실패 출력(`push_guard.py`가 없어 푸시 훅의 시험 20개가 실패, `Ran 76 tests in 21.721s` / `FAILED (failures=50)`)이 먼저, 통과 출력(`push_guard.py`만 쓴 뒤 `FAILED (failures=3)`, hooks.json을 고친 뒤 `Ran 76 tests in 29.178s` / `OK`)이 뒤에 있다. 통과

**문제**
- 기본 브랜치를 이름으로 적지 않고 보내는 push를 막지 않는다. `git push --all origin`, `git push --mirror origin`, `git push origin 'refs/heads/*:refs/heads/*'`는 로컬의 기본 브랜치를 origin의 기본 브랜치로 보내는데, `push_guard.py`의 `push_args`(93~94줄)는 `--all`·`--mirror`를 다른 `--` 옵션처럼 넘기고, `blocked_branch`(166~167줄)는 refspec이 없으면 지금 브랜치만 보며, `target_branches`(136~146줄)는 `*`를 견주지 않는다. 스크래치에 origin(로컬 bare 레포)과 문서 지도 구간이 있는 레포를 만들고 로컬 `main`을 origin보다 한 커밋 앞서게 한 뒤 `tasks/x`에서 `git push --dry-run --porcelain --all origin`을 돌리니 `refs/heads/main:refs/heads/main 35caa9e..e7974f2`가 나왔고(`--mirror`도 같다), 같은 세 명령을 훅에 넣으니 모두 종료 코드 0이었다. task 머리의 목표("기본 브랜치에 푸시하면 plate의 훅이 막고")에 들지만 완료 조건 1이 이 꼴을 적지 않아 테스트도 없다 (`plugins/plate/hooks/push_guard.py`). 기준: 결함
- 기본 브랜치에 있는 채 태그만 보내는 push를 막는다. 기본 브랜치에서 `git push --tags`, `git push --tags origin`, `git push origin --tags`는 태그만 보내는데(같은 스크래치의 `main`에서 `git push --dry-run --porcelain --tags`가 `refs/tags/v1:refs/tags/v1 [new tag]`만 냈다), `push_args`가 `--tags`를 넘겨 refspec이 없는 것으로 보고 `blocked_branch`(167줄)가 "plate: 기본 브랜치(`main`)로 푸시하지 않는다"와 종료 코드 2로 막았다. 기본 브랜치로 가지 않는 push를 막고 까닭도 틀리게 알린다. `test_push_to_other_branch`의 `git push --tags origin`은 `tasks/x`에서만 돈다 (`plugins/plate/hooks/push_guard.py`, `tests/test_push_guard.py`). 기준: 결함
- 따옴표 없는 heredoc의 본문 줄을 명령으로 읽어 막는다. `segments`(30~54줄)는 줄바꿈을 명령의 경계로 나누고 `<<` 뒤에서는 구분자 낱말 하나만 빼서, 본문 줄을 따로 된 명령으로 본다. 같은 스크래치의 `tasks/x`에서 `cat > notes.md <<'EOF'`와 `git commit -F - <<'EOF'` 뒤의 본문에 `git push origin main` 줄이 있는 명령을 훅에 넣으니 둘 다 "plate: 기본 브랜치(`main`)로 푸시하지 않는다: `git push origin main`"과 종료 코드 2였다. push가 아닌 명령을 막는다. `git commit -m "$(cat <<'EOF' … EOF)"`처럼 따옴표 안의 heredoc은 0이었다 (`plugins/plate/hooks/push_guard.py`). 기준: 결함

**판정**: 문제 있음

## 회고 2

**확인**
- 셋업된 프로젝트에서 에이전트의 Bash 호출이 기본 브랜치로 푸시하면, 훅이 종료 코드 2로 막고 까닭을 stderr로 알린다. 막는 경우는 기본 브랜치에 있는 채 대상 없이 하는 push, 기본 브랜치를 가리키는 push, 기본 브랜치를 지우는 push(`--delete`, `:main` 꼴), `&&`나 `;`로 이어진 명령 안의 push, `git -C <폴더>` 안의 push(그 폴더의 기본 브랜치를 본다)다. 다른 브랜치로의 푸시, origin 밖 원격으로의 푸시, 셋업 안 된 프로젝트(`AGENTS.md`에 문서 지도 구간이 없다)의 푸시는 막지 않는다.
  - `python3 -m unittest discover -s tests` → `Ran 80 tests in 30.141s` / `OK`. 통과
  - `tests/test_push_guard.py`를 읽음 → 기본 브랜치에 있는 채 대상 없이 하는 push(`test_push_without_target_on_default_branch` 74줄, `test_push_head_while_on_default_branch` 102줄), 기본 브랜치를 가리키는 push(`test_push_to_default_branch` 86줄), 지우는 push(`test_delete_default_branch` 107줄의 `--delete` 두 자리, `-d`, `:main`, `:refs/heads/main`), 이어진 명령 안의 push(`test_push_inside_chained_command` 155줄의 `&&`, `;`, `||`, 줄바꿈), `git -C` 안의 push와 그 폴더의 기본 브랜치(`test_push_inside_git_c_uses_that_folder` 168줄, `test_git_c_folder_has_its_own_default_branch` 176줄), 다른 브랜치(`test_push_to_other_branch` 209줄), origin 밖 원격(`test_push_to_remote_other_than_origin` 240줄), 셋업 안 된 프로젝트(`test_project_not_set_up` 263줄)가 있다. 막는 시험은 `assertBlocked`로 종료 코드 2와 stderr의 "기본 브랜치"를 본다. `python3 -m unittest discover -s tests -p 'test_push_guard.py' -v` → 24개 모두 `ok`. 통과
- `plugins/plate/hooks/hooks.json`이 Bash의 PreToolUse에 푸시 훅을 건다. 스크립트 파일이 없으면 `python3`를 부르지 않고 0으로 끝나는 꼴은 `edit_guard.py`를 거는 것과 같다.
  - `python3 -c "import json; h=json.load(open('plugins/plate/hooks/hooks.json')); print([m['matcher'] for m in h['hooks']['PreToolUse']])"` → `['Edit|Write|MultiEdit|NotebookEdit', 'Bash']`. 통과
  - `plugins/plate/hooks/hooks.json` 9줄과 18줄을 읽음 → Bash 항목은 `f="${CLAUDE_PLUGIN_ROOT}/hooks/push_guard.py"; [ -f "$f" ] || exit 0; exec python3 "$f"`로 편집 훅의 명령과 스크립트 이름만 다르다. 그 명령을 `CLAUDE_PLUGIN_ROOT=/nonexistent`로 `sh -c`에 돌림 → 종료 코드 0. 통과
- `docs/PRD.md`의 목표와 `docs/ARCHITECTURE.md`의 기술 스택, 디렉터리 구조, 막는 장치가 푸시 훅을 적는다.
  - `docs/PRD.md`의 목표(4줄)와 `docs/ARCHITECTURE.md`의 기술 스택(5줄), 디렉터리 구조(19, 21, 34줄), 패턴과 규칙의 막는 장치(48줄)를 읽음 → PRD 목표에 "에이전트가 기본 브랜치에 하는 푸시", 기술 스택에 푸시 훅 `push_guard.py`, 디렉터리 구조에 hooks.json의 Bash 항목과 `push_guard.py`, `test_push_guard.py`, 막는 장치에 푸시 훅이 막는 것과 막지 않는 것, 사람의 푸시는 다루지 않는다는 것이 적혀 있다. 통과
- tasks 완료 조건 1의 단위 테스트가 그대로 통과한다. 이 task도 `tests/`를 고친다.
  - `python3 -m unittest discover -s tests` → `OK`(위와 같다). `git diff --stat 5a7c002 HEAD -- tests/test_verdict.py plugins/plate/ci/` → 출력 없음. task의 커밋(`f8f219b`부터 `22b4eec`까지 여덟)이 바꾼 파일에 둘이 없다. `python3 -m unittest discover -s tests -p 'test_verdict.py'` → `Ran 14 tests` / `OK`. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 80 tests in 30.141s` / `OK`. 통과
- 테스트 먼저 기록: phase 1
  - `done-phase-1.md`의 "한 일"의 테스트 먼저 → 실패 출력(`push_guard.py`가 없어 푸시 훅의 시험이 실패, `Ran 76 tests in 21.721s` / `FAILED (failures=50)`)이 먼저, 통과 출력(`Ran 76 tests in 29.178s` / `OK`)이 뒤에 있다. 통과
- 테스트 먼저 기록: phase 2
  - `done-phase-2.md`의 "한 일"의 테스트 먼저 → 실패 출력(`FAIL: test_push_after_heredoc …`, `FAIL: test_push_without_naming_default_branch …`, `FAIL: test_heredoc_body_is_not_a_command …`, `FAIL: test_push_only_tags_on_default_branch …`, `Ran 80 tests in 30.776s` / `FAILED (failures=22)`)이 먼저, 통과 출력(`Ran 80 tests in 32.095s` / `OK`)이 뒤에 있다. 통과

**문제**
- 줄 잇기(`\` 바로 뒤의 줄바꿈)를 명령의 경계로 읽는다. 셸은 `\`+줄바꿈을 지우고 한 명령으로 잇는데, `lexer`(39~44줄)는 그것을 줄바꿈 낱말 하나로 내고 `segments`(95줄)가 `SEPARATORS`에 든 낱말로 보아 명령을 나눈다. `segments('git push \\\n  origin main')`이 `[['git', 'push'], ['origin', 'main']]`을 냈다. 스크래치에 로컬 bare origin과 문서 지도 구간이 있는 레포를 만들고 `main`을 origin보다 한 커밋 앞서게 한 뒤, `tasks/x`에서 `git push \`(줄바꿈)`  origin main`을 훅에 넣으니 종료 코드 0이었고 같은 명령을 `git push --dry-run --porcelain`으로 bash에 돌리니 `refs/heads/main:refs/heads/main`이 나왔다. 거꾸로 `main`에서 `git push \`(줄바꿈)`  origin tasks/x`는 origin의 `main`을 바꾸지 않는데 종료 코드 2로 막았다 (`plugins/plate/hooks/push_guard.py`). 기준: 결함
- `#` 주석을 명령의 글로 읽는다. `lexer`가 `lex.commenters = ""`(43줄)로 주석을 두지 않고 `without_heredocs`(47~82줄)도 주석 안의 따옴표를 센다. 그래서 주석에 짝 없는 따옴표가 있으면 `lexer`가 `ValueError`를 내고 `segments`(89~90줄)가 빈 목록을 돌려 명령 전체를 통과시킨다. 같은 스크래치의 `tasks/x`에서 `# push it (it's ready)`(줄바꿈)`git push origin main`과 `echo "it's" # don't`(줄바꿈)`git push origin main`을 훅에 넣으니 둘 다 종료 코드 0이었고, bash의 `--dry-run --porcelain`은 둘 다 `refs/heads/main:refs/heads/main`을 냈다. 거꾸로 `echo hi # ; git push origin main`은 셸이 `#` 뒤를 주석으로 버려 푸시하지 않는데 종료 코드 2로 막았다 (`plugins/plate/hooks/push_guard.py`). 기준: 결함

**판정**: 문제 있음

## 회고 3

**확인**
- 셋업된 프로젝트에서 에이전트의 Bash 호출이 기본 브랜치로 푸시하면, 훅이 종료 코드 2로 막고 까닭을 stderr로 알린다. 막는 경우는 기본 브랜치에 있는 채 대상 없이 하는 push, 기본 브랜치를 가리키는 push, 기본 브랜치를 지우는 push(`--delete`, `:main` 꼴), `&&`나 `;`로 이어진 명령 안의 push, `git -C <폴더>` 안의 push(그 폴더의 기본 브랜치를 본다)다. 다른 브랜치로의 푸시, origin 밖 원격으로의 푸시, 셋업 안 된 프로젝트(`AGENTS.md`에 문서 지도 구간이 없다)의 푸시는 막지 않는다.
  - `python3 -m unittest discover -s tests` → `Ran 84 tests in 32.089s` / `OK`. 통과
  - `tests/test_push_guard.py`를 읽음 → 기본 브랜치에 있는 채 대상 없이 하는 push(`test_push_without_target_on_default_branch` 74줄, `test_push_head_while_on_default_branch` 102줄), 기본 브랜치를 가리키는 push(`test_push_to_default_branch` 86줄), 지우는 push(`test_delete_default_branch` 107줄의 `--delete` 두 자리, `-d`, `:main`, `:refs/heads/main`), 이어진 명령 안의 push(`test_push_inside_chained_command` 182줄의 `&&`, `;`, `||`, 줄바꿈), `git -C` 안의 push와 그 폴더의 기본 브랜치(`test_push_inside_git_c_uses_that_folder` 195줄, `test_git_c_folder_has_its_own_default_branch` 203줄), 다른 브랜치(`test_push_to_other_branch` 236줄), origin 밖 원격(`test_push_to_remote_other_than_origin` 267줄), 셋업 안 된 프로젝트(`test_project_not_set_up` 312줄)가 있다. 막는 시험은 `assertBlocked`로 종료 코드 2와 stderr의 "기본 브랜치"를 본다. `python3 -m unittest discover -s tests -p 'test_push_guard.py' -v` → `Ran 28 tests` / `OK`, 28개 모두 `ok`. 통과
- `plugins/plate/hooks/hooks.json`이 Bash의 PreToolUse에 푸시 훅을 건다. 스크립트 파일이 없으면 `python3`를 부르지 않고 0으로 끝나는 꼴은 `edit_guard.py`를 거는 것과 같다.
  - `python3 -c "import json; h=json.load(open('plugins/plate/hooks/hooks.json')); print([m['matcher'] for m in h['hooks']['PreToolUse']])"` → `['Edit|Write|MultiEdit|NotebookEdit', 'Bash']`. 통과
  - `plugins/plate/hooks/hooks.json` 9줄과 18줄을 읽음 → Bash 항목은 `f="${CLAUDE_PLUGIN_ROOT}/hooks/push_guard.py"; [ -f "$f" ] || exit 0; exec python3 "$f"`로 편집 훅의 명령과 스크립트 이름만 다르다. 그 명령을 `CLAUDE_PLUGIN_ROOT=/nonexistent`로 `sh -c`에 돌림 → 종료 코드 0. 통과
- `docs/PRD.md`의 목표와 `docs/ARCHITECTURE.md`의 기술 스택, 디렉터리 구조, 막는 장치가 푸시 훅을 적는다.
  - `docs/PRD.md`의 목표(4줄)와 `docs/ARCHITECTURE.md`의 기술 스택(5줄), 디렉터리 구조(19, 21, 34줄), 패턴과 규칙의 막는 장치(48줄)를 읽음 → PRD 목표에 "에이전트가 기본 브랜치에 하는 푸시", 기술 스택에 푸시 훅 `push_guard.py`, 디렉터리 구조에 hooks.json의 Bash 항목과 `push_guard.py`, `test_push_guard.py`, 막는 장치에 푸시 훅이 막는 것과 막지 않는 것, 사람의 푸시는 다루지 않는다는 것이 적혀 있다. 통과
- tasks 완료 조건 1의 단위 테스트가 그대로 통과한다. 이 task도 `tests/`를 고친다.
  - `python3 -m unittest discover -s tests` → `OK`(위와 같다). `git diff --stat 5a7c002 HEAD -- tests/test_verdict.py plugins/plate/ci/` → 출력 없음. task의 커밋(`f8f219b`부터 `8f1b3cd`까지)이 바꾼 파일에 둘이 없다. `python3 -m unittest discover -s tests -p 'test_verdict.py'` → `Ran 14 tests in 0.745s` / `OK`. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 84 tests in 32.089s` / `OK`. 통과
- 테스트 먼저 기록: phase 1
  - `done-phase-1.md`의 "한 일"의 테스트 먼저 → 실패 출력(`push_guard.py`가 없어 푸시 훅의 시험이 실패, `Ran 76 tests in 21.721s` / `FAILED (failures=50)`)이 먼저, 통과 출력(`Ran 76 tests in 29.178s` / `OK`)이 뒤에 있다. 통과
- 테스트 먼저 기록: phase 2
  - `done-phase-2.md`의 "한 일"의 테스트 먼저 → 실패 출력(`FAIL: test_push_after_heredoc …` 등, `Ran 80 tests in 30.776s` / `FAILED (failures=22)`)이 먼저, 통과 출력(`Ran 80 tests in 32.095s` / `OK`)이 뒤에 있다. 통과
- 테스트 먼저 기록: phase 3
  - `done-phase-3.md`의 "한 일"의 테스트 먼저 → 실패 출력(`FAIL: test_push_across_line_continuation …`, `FAIL: test_push_after_comment …`, `FAIL: test_comment_is_not_a_command …`, `FAIL: test_line_continuation_is_one_command …`, `Ran 84 tests in 33.904s` / `FAILED (failures=8)`)이 먼저, 통과 출력(`Ran 84 tests in 32.088s` / `OK`)이 뒤에 있다. 통과

**문제**
- `cd <폴더> &&`(또는 `;`) 뒤의 push를 그 폴더가 아니라 호출의 `cwd`에서 본다. `check`(239~249줄)는 호출의 `cwd`를 모든 단순 명령에 넘기고, `push_call`(120~139줄)은 `git -C`에서만 폴더를 바꾼다. 스크래치에 로컬 bare origin과 문서 지도 구간이 있는 레포 `proj`(`main`이 origin보다 앞서고 지금 브랜치는 `tasks/x`), 셋업 안 된 레포 `other`(`main`이 그 origin보다 앞선다), git 레포가 아닌 폴더 `plain`을 만들고, 명령마다 훅의 종료 코드와 같은 명령의 `git push`를 `git push --dry-run --porcelain`으로 바꿔 bash에 돌린 결과를 견줬다. `cwd`가 `plain`일 때 `cd <proj> && git push origin main`, `cd <proj> && git push origin HEAD:main`, `cd <proj>; git push origin :main`은 셋 다 훅 0이고 bash는 `refs/heads/main`을 바꾸거나 지웠다(`refs/heads/main:refs/heads/main`, `HEAD:refs/heads/main`, `:refs/heads/main [deleted]`). 거꾸로 `cwd`가 `proj`일 때 `cd <other> && git push origin main`은 셋업 안 된 프로젝트의 푸시인데 훅이 2로 막았다 (`plugins/plate/hooks/push_guard.py`). 기준: 결함
- 기본 브랜치에 있는 채 명령 치환으로 지금 브랜치를 적은 push를 막지 않는다. `target_refs`(201~211줄)는 `HEAD`, `@`만 지금 브랜치로 바꾸고, 따옴표 안의 `"$(git branch --show-current)"`는 그 글 그대로 `refs/heads/$(git branch --show-current)`로 본다. 따옴표가 없으면 `segments`가 `(`에서 명령을 나눠 대상이 `$`가 된다. 같은 스크래치의 `proj`를 `main`에 두고 `git push -u origin "$(git branch --show-current)"`와 `git push -u origin $(git rev-parse --abbrev-ref HEAD)`를 넣으니 둘 다 훅 0이었고 bash는 둘 다 `refs/heads/main:refs/heads/main`을 냈다. 같은 자리의 `git push origin HEAD`는 훅이 2로 막는다(`test_push_head_while_on_default_branch`도 같다) (`plugins/plate/hooks/push_guard.py`). 기준: 결함
- `"$( … )"` 안의 큰따옴표를 바깥 큰따옴표의 끝으로 읽어, 그 뒤의 따옴표가 어긋나면 명령 전체를 통과시킨다. 셸은 큰따옴표 안의 `$(`부터 따옴표를 새로 세는데 `without_non_commands`(48~94줄)와 `lexer`(40~45줄)는 안쪽의 `"`에서 바깥 따옴표를 닫는다. 그래서 `git commit -m "$(cat <<'EOF'`(줄바꿈)`Keep "don't" wording`(줄바꿈)`EOF`(줄바꿈)`)" && git push origin main`은 `don't`의 `'`가 닫히지 않은 따옴표로 읽혀 `segments`(99~102줄)가 빈 목록을 돌려준다. phase 3이 더한 주석 빼기는 같은 어긋남 위에서 `Close "issue #12" properly`의 `#12" properly`를 주석으로 지워 바깥 따옴표를 닫히지 않게 만들고, 같은 빈 목록이 된다(`without_non_commands`의 출력에서 `#12" properly`가 빠진 것을 봤다). 같은 스크래치의 `tasks/x`에서 두 명령은 지금의 훅에서 0이고 bash는 둘 다 `refs/heads/main:refs/heads/main`을 냈다. phase 1(`f8f219b`)과 phase 2(`5cdb2a0`)의 `push_guard.py`에 같은 명령을 넣으니 `issue #12` 쪽은 2로 막았고 `don't` 쪽은 0이었다. 안쪽 따옴표가 없는 `Fix #12`, 짝이 맞고 `#`·`'`가 없는 `Rename "foo" to "bar"`는 지금도 2다 (`plugins/plate/hooks/push_guard.py`). 기준: 결함

**판정**: 문제 있음

## 회고 4

**확인**
- 셋업된 프로젝트에서 에이전트의 Bash 호출이 기본 브랜치로 푸시하면, 훅이 종료 코드 2로 막고 까닭을 stderr로 알린다. 막는 경우는 기본 브랜치에 있는 채 대상 없이 하는 push, 기본 브랜치를 가리키는 push, 기본 브랜치를 지우는 push(`--delete`, `:main` 꼴), `&&`나 `;`로 이어진 명령 안의 push, `git -C <폴더>` 안의 push(그 폴더의 기본 브랜치를 본다)다. 다른 브랜치로의 푸시, origin 밖 원격으로의 푸시, 셋업 안 된 프로젝트(`AGENTS.md`에 문서 지도 구간이 없다)의 푸시는 막지 않는다.
  - `python3 -m unittest discover -s tests` → `Ran 87 tests in 39.379s` / `OK`. 통과
  - `tests/test_push_guard.py`를 읽음 → 기본 브랜치에 있는 채 대상 없이 하는 push(`test_push_without_target_on_default_branch` 80줄, `test_push_head_while_on_default_branch` 108줄), 기본 브랜치를 가리키는 push(`test_push_to_default_branch` 92줄), 지우는 push(`test_delete_default_branch` 113줄의 `--delete` 두 자리, `-d`, `:main`, `:refs/heads/main`), 이어진 명령 안의 push(`test_push_inside_chained_command` 188줄의 `&&`, `;`, 붙인 `;`, `||`, 줄바꿈), `git -C` 안의 push와 그 폴더의 기본 브랜치(`test_push_inside_git_c_uses_that_folder` 209줄, `test_git_c_folder_has_its_own_default_branch` 217줄), 다른 브랜치(`test_push_to_other_branch` 250줄), origin 밖 원격(`test_push_to_remote_other_than_origin` 281줄), 셋업 안 된 프로젝트(`test_project_not_set_up` 326줄)가 있다. 막는 시험은 `assertBlocked`(71줄)로 종료 코드 2와 stderr의 "기본 브랜치"를 본다. `python3 -m unittest discover -s tests -p 'test_push_guard.py' -v` → `Ran 31 tests in 16.817s` / `OK`, 31개 모두 `ok`. 통과
- `plugins/plate/hooks/hooks.json`이 Bash의 PreToolUse에 푸시 훅을 건다. 스크립트 파일이 없으면 `python3`를 부르지 않고 0으로 끝나는 꼴은 `edit_guard.py`를 거는 것과 같다.
  - `python3 -c "import json; h=json.load(open('plugins/plate/hooks/hooks.json')); print([m['matcher'] for m in h['hooks']['PreToolUse']])"` → `['Edit|Write|MultiEdit|NotebookEdit', 'Bash']`. 통과
  - `plugins/plate/hooks/hooks.json` 9줄과 18줄을 읽음 → Bash 항목은 `f="${CLAUDE_PLUGIN_ROOT}/hooks/push_guard.py"; [ -f "$f" ] || exit 0; exec python3 "$f"`로 편집 훅의 명령과 스크립트 이름만 다르다. 그 명령을 `CLAUDE_PLUGIN_ROOT=/nonexistent`로 `sh -c`에 돌림 → 종료 코드 0. 통과
- `docs/PRD.md`의 목표와 `docs/ARCHITECTURE.md`의 기술 스택, 디렉터리 구조, 막는 장치가 푸시 훅을 적는다.
  - `docs/PRD.md`의 목표(4줄)와 `docs/ARCHITECTURE.md`의 기술 스택(5줄), 디렉터리 구조(19, 21, 34줄), 패턴과 규칙의 막는 장치(48줄)를 읽음 → PRD 목표에 "에이전트가 기본 브랜치에 하는 푸시", 기술 스택에 푸시 훅 `push_guard.py`, 디렉터리 구조에 hooks.json의 Bash 항목과 `push_guard.py`, `test_push_guard.py`, 막는 장치에 푸시 훅이 막는 것, 막지 않는 것, 사람의 푸시는 다루지 않는다는 것, 셸 구문의 한계, 나누지 못한 명령의 막음이 적혀 있다. 통과
- tasks 완료 조건 1의 단위 테스트가 그대로 통과한다. 이 task도 `tests/`를 고친다.
  - `python3 -m unittest discover -s tests` → `OK`(위와 같다). `git diff --stat 5a7c002 HEAD -- tests/test_verdict.py plugins/plate/ci/`(`5a7c002`는 `f8f219b^`) → 출력 없음. `python3 -m unittest discover -s tests -p 'test_verdict.py'` → `Ran 14 tests in 0.732s` / `OK`. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 87 tests in 39.379s` / `OK`. 통과
- 테스트 먼저 기록: phase 1
  - `done-phase-1.md`의 "한 일"의 테스트 먼저 → 실패 출력(`push_guard.py`가 없어 푸시 훅의 시험이 실패, `Ran 76 tests in 21.721s` / `FAILED (failures=50)`)이 먼저, 통과 출력(`Ran 76 tests in 29.178s` / `OK`)이 뒤에 있다. 통과
- 테스트 먼저 기록: phase 2
  - `done-phase-2.md`의 "한 일"의 테스트 먼저 → 실패 출력(`FAIL: test_push_after_heredoc …`, `FAIL: test_push_without_naming_default_branch …` 등, `Ran 80 tests in 30.776s` / `FAILED (failures=22)`)이 먼저, 통과 출력(`Ran 80 tests in 32.095s` / `OK`)이 뒤에 있다. 통과
- 테스트 먼저 기록: phase 3
  - `done-phase-3.md`의 "한 일"의 테스트 먼저 → 실패 출력(`FAIL: test_push_across_line_continuation …`, `FAIL: test_push_after_comment …` 등, `Ran 84 tests in 33.904s` / `FAILED (failures=8)`)이 먼저, 통과 출력(`Ran 84 tests in 32.088s` / `OK`)이 뒤에 있다. 통과
- 테스트 먼저 기록: phase 4
  - `done-phase-4.md`의 "한 일"의 테스트 먼저 → 실패 출력(`FAIL: test_unsplit_command_with_push …` 두 subTest, `Ran 87 tests in 32.380s` / `FAILED (failures=2)`)이 먼저, 통과 출력(`Ran 87 tests in 33.222s` / `OK`)이 뒤에 있다. 통과

**문제**
- `"$( … )"` 안의 큰따옴표 사이에 `#`이 있는 한 줄 명령 뒤에 `&&`나 `;`로 이은 push를 막지 않는다. `without_non_commands`(53~99줄)는 `"$( … )"` 안쪽의 `"`에서 바깥 따옴표가 닫힌다고 읽고, 그 뒤 낱말 첫머리의 `#`(69~72줄)를 주석으로 보아 줄 끝까지 지운다. 지운 글에 `"`가 짝수 개면 남은 글의 따옴표 짝이 맞아 `segments`(102~123줄)가 None이 아닌 목록을 돌려주므로 phase 4가 더한 나누지 못한 명령의 막음(`check` 259~260줄)에 걸리지 않고, 뒤의 push는 지워진 채 통과한다. `git commit -m "$(echo "fix #1")" && git push origin main`을 넣으니 `without_non_commands`는 `git commit -m "$(echo "fix `를, `segments`는 `[['git', 'commit', '-m', '$(echo fix']]`를 냈다. 스크래치에 로컬 bare origin과 문서 지도 구간이 있는 레포(`main`이 origin보다 한 커밋 앞서고 지금 브랜치는 `tasks/x`)를 만들고, 이 명령과 `echo "$(echo "fix #1")" && git push origin main`, `echo "$(git log -1 --format="%h #%s")"; git push origin main`을 훅에 넣고 같은 명령의 `git push`를 `git push --dry-run --porcelain`으로 바꿔 bash에 돌리니, 셋 다 지금의 훅에서 0이고 bash는 셋 다 `refs/heads/main:refs/heads/main`을 냈다. phase 1(`f8f219b`)과 phase 2(`5cdb2a0`)의 훅은 셋 다 2로 막았고 phase 3(`8c3673b`)의 훅부터 0이다. 회고 3의 셋째 문제와 같은 오독 위에서 주석 빼기가 따옴표 짝을 맞추는 꼴이다. push는 명령 치환이나 다른 명령 안이 아니라 `&&`·`;`로 이어진 명령이고 대상도 글로 적혀 있어, task 머리 결정의 한계에 들지 않는다. 안쪽 따옴표가 없는 `git commit --allow-empty -m "fix #1" && git push origin main`과 `echo "$(echo "a")" && git push origin main`은 지금도 2다 (`plugins/plate/hooks/push_guard.py`). 기준: 결함

**판정**: 문제 있음

## 회고 5

**확인**
- 셋업된 프로젝트에서 에이전트의 Bash 호출이 기본 브랜치로 푸시하면, 훅이 종료 코드 2로 막고 까닭을 stderr로 알린다. 막는 경우는 기본 브랜치에 있는 채 대상 없이 하는 push, 기본 브랜치를 가리키는 push, 기본 브랜치를 지우는 push(`--delete`, `:main` 꼴), `&&`나 `;`로 이어진 명령 안의 push, `git -C <폴더>` 안의 push(그 폴더의 기본 브랜치를 본다)다. 다른 브랜치로의 푸시, origin 밖 원격으로의 푸시, 셋업 안 된 프로젝트(`AGENTS.md`에 문서 지도 구간이 없다)의 푸시는 막지 않는다.
  - `python3 -m unittest discover -s tests` → `Ran 89 tests in 34.017s` / `OK`. 통과
  - `tests/test_push_guard.py`를 읽음 → 기본 브랜치에 있는 채 대상 없이 하는 push(`test_push_without_target_on_default_branch` 90줄, `test_push_head_while_on_default_branch` 118줄), 기본 브랜치를 가리키는 push(`test_push_to_default_branch` 102줄), 지우는 push(`test_delete_default_branch` 123줄의 `--delete` 두 자리, `-d`, `:main`, `:refs/heads/main`), 이어진 명령 안의 push(`test_push_inside_chained_command` 198줄의 `&&`, `;`, 붙인 `;`, `||`, 줄바꿈), `git -C` 안의 push와 그 폴더의 기본 브랜치(`test_push_inside_git_c_uses_that_folder` 228줄, `test_git_c_folder_has_its_own_default_branch` 236줄), 다른 브랜치(`test_push_to_other_branch` 269줄), origin 밖 원격(`test_push_to_remote_other_than_origin` 300줄), 셋업 안 된 프로젝트(`test_project_not_set_up` 345줄)가 있다. 막는 시험은 `assertBlocked`(81줄)로 종료 코드 2와 stderr의 "기본 브랜치"를 본다. `python3 -m unittest discover -s tests -p 'test_push_guard.py' -v` → `Ran 33 tests in 18.749s` / `OK`, 33개 모두 `ok`. 통과
- `plugins/plate/hooks/hooks.json`이 Bash의 PreToolUse에 푸시 훅을 건다. 스크립트 파일이 없으면 `python3`를 부르지 않고 0으로 끝나는 꼴은 `edit_guard.py`를 거는 것과 같다.
  - `python3 -c "import json; h=json.load(open('plugins/plate/hooks/hooks.json')); print([m['matcher'] for m in h['hooks']['PreToolUse']])"` → `['Edit|Write|MultiEdit|NotebookEdit', 'Bash']`. 통과
  - `plugins/plate/hooks/hooks.json` 9줄과 18줄을 읽음 → 18줄의 Bash 항목은 `f="${CLAUDE_PLUGIN_ROOT}/hooks/push_guard.py"; [ -f "$f" ] || exit 0; exec python3 "$f"`로 9줄의 편집 훅과 스크립트 이름만 다르다. 그 명령을 `CLAUDE_PLUGIN_ROOT=/nonexistent`로 `sh -c`에 돌림 → 종료 코드 0. 통과
- `docs/PRD.md`의 목표와 `docs/ARCHITECTURE.md`의 기술 스택, 디렉터리 구조, 막는 장치가 푸시 훅을 적는다.
  - `docs/PRD.md`의 목표(4줄)와 `docs/ARCHITECTURE.md`의 기술 스택(5줄), 디렉터리 구조(19, 21, 34줄), 패턴과 규칙의 막는 장치(48줄)를 읽음 → PRD 목표에 "에이전트가 기본 브랜치에 하는 푸시", 기술 스택에 푸시 훅 `push_guard.py`, 디렉터리 구조에 hooks.json의 Bash 항목과 `push_guard.py`, `test_push_guard.py`, 막는 장치에 푸시 훅이 막는 것, 막지 않는 것, 사람의 푸시는 다루지 않는다는 것, 명령 치환을 따로 세는 것, 셸 구문의 한계, 나누지 못한 명령의 막음이 적혀 있다. 통과
- tasks 완료 조건 1의 단위 테스트가 그대로 통과한다. 이 task도 `tests/`를 고친다.
  - `python3 -m unittest discover -s tests` → `OK`(위와 같다). `git diff --stat 5a7c002 HEAD -- tests/test_verdict.py plugins/plate/ci/`(`5a7c002`는 `f8f219b^`)와 `git diff --stat -- tests/test_verdict.py plugins/plate/ci/` → 둘 다 출력 없음. `python3 -m unittest discover -s tests -p 'test_verdict.py'` → `Ran 14 tests in 0.728s` / `OK`. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 89 tests in 34.017s` / `OK`. 통과
- 테스트 먼저 기록: phase 1
  - `done-phase-1.md`의 "한 일"의 테스트 먼저 → 실패 출력(`push_guard.py`가 없어 푸시 훅의 시험이 실패, `Ran 76 tests in 21.721s` / `FAILED (failures=50)`)이 먼저, 통과 출력(`Ran 76 tests in 29.178s` / `OK`)이 뒤에 있다. 통과
- 테스트 먼저 기록: phase 2
  - `done-phase-2.md`의 "한 일"의 테스트 먼저 → 실패 출력(`FAIL: test_push_after_heredoc …`, `FAIL: test_push_without_naming_default_branch …` 등, `Ran 80 tests in 30.776s` / `FAILED (failures=22)`)이 먼저, 통과 출력(`Ran 80 tests in 32.095s` / `OK`)이 뒤에 있다. 통과
- 테스트 먼저 기록: phase 3
  - `done-phase-3.md`의 "한 일"의 테스트 먼저 → 실패 출력(`FAIL: test_push_across_line_continuation …`, `FAIL: test_push_after_comment …` 등, `Ran 84 tests in 33.904s` / `FAILED (failures=8)`)이 먼저, 통과 출력(`Ran 84 tests in 32.088s` / `OK`)이 뒤에 있다. 통과
- 테스트 먼저 기록: phase 4
  - `done-phase-4.md`의 "한 일"의 테스트 먼저 → 실패 출력(`FAIL: test_unsplit_command_with_push …` 두 subTest, `Ran 87 tests in 32.380s` / `FAILED (failures=2)`)이 먼저, 통과 출력(`Ran 87 tests in 33.222s` / `OK`)이 뒤에 있다. 통과
- 테스트 먼저 기록: phase 5
  - `done-phase-5.md`의 "한 일"의 테스트 먼저 → 실패 출력(`FAIL: test_push_after_substitution_with_quotes …`의 여섯 subTest와 `FAIL: test_substitution_with_quotes_without_push …`의 두 subTest, `Ran 89 tests in 33.345s` / `FAILED (failures=8)`)이 먼저, 통과 출력(`Ran 89 tests in 33.743s` / `OK`)이 뒤에 있다. 통과

**문제**
- 큰따옴표 안의 매개변수 확장 `"${ … }"`에서 안쪽 큰따옴표 사이에 `#`이 있는 한 줄 명령 뒤에 `&&`로 이은 push를 막지 않는다. 셸은 `"${X:-"fix #1"}"`의 안쪽 따옴표를 따로 세는데, `scan`은 `$(`와 백틱(75~81줄)만 따로 읽고 `${`는 따로 읽지 않아 안쪽의 `"`에서 바깥 따옴표가 닫힌다고 읽고(82~84줄), 그 뒤 낱말 첫머리의 `#`(89~92줄)를 주석으로 보아 줄 끝까지 지운다. 지운 글의 따옴표 짝이 맞아 `segments`(122~143줄)가 None이 아닌 목록을 돌려주므로 나누지 못한 명령의 막음(`check` 279~280줄)에 걸리지 않고, 뒤의 push는 지워진 채 통과한다. `echo "${X:-"fix #1"}" && git push origin main`을 넣으니 `without_non_commands`는 `echo "${X:-"fix `를, `segments`는 `[['echo', '${X:-fix']]`를 냈다. 스크래치에 로컬 bare origin과 문서 지도 구간이 있는 레포(`main`이 origin보다 한 커밋 앞서고 지금 브랜치는 `tasks/x`)를 만들고, 이 명령과 `git commit --allow-empty -m "${MSG:-"fix #1"}" && git push origin main`을 훅에 넣고 같은 명령의 `git push`를 `git push --dry-run --porcelain`으로 바꿔 bash에 돌리니, 둘 다 지금의 훅에서 0이고 bash는 둘 다 `refs/heads/main:refs/heads/main`을 냈다. phase 1(`f8f219b`)과 phase 2(`5cdb2a0`)의 훅은 둘 다 2로 막았고, phase 3(`8c3673b`)부터 phase 5(`fd12137`)까지의 훅은 0이다. 회고 4의 문제와 같은 오독(안쪽 따옴표를 바깥 것으로 읽고 주석 빼기가 짝을 맞춘다)이 phase 5가 따로 읽게 한 명령 치환 밖의 매개변수 확장에 남은 꼴이다. push는 `&&`로 이어진 명령이고 대상도 글로 적혀 있어, task 머리 결정의 한계(같은 호출의 `cd`·`pushd` 뒤, 명령 치환이나 변수로 적은 대상, 다른 명령이 감싼 push)에 들지 않는다. 안쪽에 `#`이 없는 `echo "${X:-"a"}" && git push origin main`은 지금도 2다 (`plugins/plate/hooks/push_guard.py`). 기준: 결함
- 산술 명령 `(( … << … ))` 뒤의 줄에 적은 push를 막지 않는다. 셸은 `(( ))` 안의 `<<`를 왼쪽 시프트로 읽는데, `scan`(95~102줄)은 따옴표 밖의 `<<`를 `((` 안이어도 heredoc의 시작으로 보고, 다음 줄바꿈에서(103~114줄) 구분자(`2`)와 같은 줄이 나올 때까지 뒤의 줄을 본문으로 건너뛴다. `(( x = 1 << 2 ))`(줄바꿈)`git push origin main`을 넣으니 `without_non_commands`는 `(( x = 1 << 2 ))\n`을, `segments`는 `[['x', '=']]`를 냈다. 같은 스크래치의 `tasks/x`에서 이 명령은 지금의 훅에서 0이고, bash는 `x`를 4로 두고 `--dry-run --porcelain`의 push가 `refs/heads/main:refs/heads/main`을 냈다. phase 1(`f8f219b`)의 훅은 2로 막았고, heredoc 빼기를 더한 phase 2(`5cdb2a0`)부터 phase 5(`fd12137`)까지의 훅은 0이다. phase 2의 기록(`done-phase-2.md`의 한 일)은 "산술 확장 `$((1<<2))`의 `<<`도 heredoc으로 읽어 그 뒤 줄을 건너뛴다"고 적었고, phase 5의 치환 읽기가 `$(( ))` 꼴은 고쳤지만(`echo $((1<<2))`(줄바꿈)`git push origin main`은 phase 2~4의 훅에서 0, 지금 2) `(( ))` 명령 꼴은 남았다. push는 줄바꿈으로 이어진 명령이고 대상도 글로 적혀 있어 task 머리 결정의 한계에 들지 않는다 (`plugins/plate/hooks/push_guard.py`). 기준: 결함

**판정**: 문제 있음

## 회고 6

**확인**
- 셋업된 프로젝트에서 에이전트의 Bash 호출이 기본 브랜치로 푸시하면, 훅이 종료 코드 2로 막고 까닭을 stderr로 알린다. 막는 경우는 기본 브랜치에 있는 채 대상 없이 하는 push, 기본 브랜치를 가리키는 push, 기본 브랜치를 지우는 push(`--delete`, `:main` 꼴), `&&`나 `;`로 이어진 명령 안의 push, `git -C <폴더>` 안의 push(그 폴더의 기본 브랜치를 본다)다. 다른 브랜치로의 푸시, origin 밖 원격으로의 푸시, 셋업 안 된 프로젝트(`AGENTS.md`에 문서 지도 구간이 없다)의 푸시는 막지 않는다.
  - `python3 -m unittest discover -s tests` → `Ran 89 tests in 34.377s` / `OK`. 통과
  - `tests/test_push_guard.py`를 읽음 → 기본 브랜치에 있는 채 대상 없이 하는 push(`test_push_without_target_on_default_branch` 90줄, `test_push_head_while_on_default_branch` 118줄), 기본 브랜치를 가리키는 push(`test_push_to_default_branch` 102줄), 지우는 push(`test_delete_default_branch` 123줄의 `--delete` 두 자리, `-d`, `:main`, `:refs/heads/main`), 이어진 명령 안의 push(`test_push_inside_chained_command` 198줄의 `&&`, `;`, 붙인 `;`, `||`, 줄바꿈), `git -C` 안의 push와 그 폴더의 기본 브랜치(`test_push_inside_git_c_uses_that_folder` 228줄, `test_git_c_folder_has_its_own_default_branch` 236줄), 다른 브랜치(`test_push_to_other_branch` 269줄), origin 밖 원격(`test_push_to_remote_other_than_origin` 300줄), 셋업 안 된 프로젝트(`test_project_not_set_up` 345줄)가 있다. 막는 시험은 `assertBlocked`(81줄)로 종료 코드 2와 stderr의 "기본 브랜치"를 본다. `python3 -m unittest discover -s tests -p 'test_push_guard.py' -v` → `Ran 33 tests in 18.298s` / `OK`, 33개 모두 `ok`. 통과
- `plugins/plate/hooks/hooks.json`이 Bash의 PreToolUse에 푸시 훅을 건다. 스크립트 파일이 없으면 `python3`를 부르지 않고 0으로 끝나는 꼴은 `edit_guard.py`를 거는 것과 같다.
  - `python3 -c "import json; h=json.load(open('plugins/plate/hooks/hooks.json')); print([m['matcher'] for m in h['hooks']['PreToolUse']])"` → `['Edit|Write|MultiEdit|NotebookEdit', 'Bash']`. 통과
  - `plugins/plate/hooks/hooks.json`을 읽음 → 18줄의 Bash 항목은 `f="${CLAUDE_PLUGIN_ROOT}/hooks/push_guard.py"; [ -f "$f" ] || exit 0; exec python3 "$f"`로 9줄의 편집 훅과 스크립트 이름만 다르다. 그 명령을 `CLAUDE_PLUGIN_ROOT=/nonexistent`로 `sh -c`에 돌림 → `exit=0`. 통과
- `docs/PRD.md`의 목표와 `docs/ARCHITECTURE.md`의 기술 스택, 디렉터리 구조, 막는 장치가 푸시 훅을 적는다.
  - `docs/PRD.md`의 목표(4줄)와 `docs/ARCHITECTURE.md`의 기술 스택(5줄), 디렉터리 구조(19, 21, 34줄), 패턴과 규칙의 막는 장치(48줄)를 읽음 → PRD 목표에 "에이전트가 기본 브랜치에 하는 푸시", 기술 스택에 푸시 훅 `push_guard.py`, 디렉터리 구조에 hooks.json의 Bash 항목과 `push_guard.py`, `test_push_guard.py`, 막는 장치에 푸시 훅이 막는 것, 막지 않는 것, 사람의 푸시는 다루지 않는다는 것, heredoc·주석·줄 잇기와 명령 치환의 읽기, 나누지 못한 명령의 막음, 약속하는 꼴은 거기까지이고 그 밖의 셸 구문(매개변수 확장, 산술 명령 같은)은 결함으로 보지 않는다는 것이 적혀 있다. 통과
- tasks 완료 조건 1의 단위 테스트가 그대로 통과한다. 이 task도 `tests/`를 고친다.
  - `python3 -m unittest discover -s tests` → `OK`(위와 같다). `git diff --stat f8f219b^ HEAD -- tests/test_verdict.py plugins/plate/ci/`와 `git diff --stat -- tests/test_verdict.py plugins/plate/ci/` → 둘 다 출력 없음. `python3 -m unittest discover -s tests -p 'test_verdict.py'` → `Ran 14 tests in 0.783s` / `OK`. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 89 tests in 34.377s` / `OK`. 통과
- 테스트 먼저 기록: phase 1
  - `done-phase-1.md`의 "한 일"의 테스트 먼저 → 실패 출력(`Ran 76 tests in 21.721s` / `FAILED (failures=50)`)이 먼저, 통과 출력(`Ran 76 tests in 29.178s` / `OK`)이 뒤에 있다. 통과
- 테스트 먼저 기록: phase 2
  - `done-phase-2.md`의 "한 일"의 테스트 먼저 → 실패 출력(`Ran 80 tests in 30.776s` / `FAILED (failures=22)`)이 먼저, 통과 출력(`Ran 80 tests in 32.095s` / `OK`)이 뒤에 있다. 통과
- 테스트 먼저 기록: phase 3
  - `done-phase-3.md`의 "한 일"의 테스트 먼저 → 실패 출력(`Ran 84 tests in 33.904s` / `FAILED (failures=8)`)이 먼저, 통과 출력(`Ran 84 tests in 32.088s` / `OK`)이 뒤에 있다. 통과
- 테스트 먼저 기록: phase 4
  - `done-phase-4.md`의 "한 일"의 테스트 먼저 → 실패 출력(`Ran 87 tests in 32.380s` / `FAILED (failures=2)`)이 먼저, 통과 출력(`Ran 87 tests in 33.222s` / `OK`)이 뒤에 있다. 통과
- 테스트 먼저 기록: phase 5
  - `done-phase-5.md`의 "한 일"의 테스트 먼저 → 실패 출력(`FAIL: test_push_after_substitution_with_quotes …`, `FAIL: test_substitution_with_quotes_without_push …`, `Ran 89 tests in 33.345s` / `FAILED (failures=8)`)이 먼저, 통과 출력(`Ran 89 tests in 33.743s` / `OK`)이 뒤에 있다. 통과

**문제**
- 기본 브랜치를 `heads/<이름>`으로 적은 push를 막지 않는다. git은 refspec의 이름을 `refs/<이름>` 규칙으로도 풀어 `heads/main`을 `refs/heads/main`으로 읽는데, `target_refs`(227~237줄)는 `refs/`로 시작하지 않는 대상에 `refs/heads/`를 붙여(237줄) `refs/heads/heads/main`으로 견준다. 스크래치에 로컬 bare origin과 문서 지도 구간이 있는 레포(`main`이 origin보다 한 커밋 앞서고 지금 브랜치는 `tasks/x`)를 만들고 `git push origin heads/main`, `git push origin tasks/x:heads/main`, `git push origin :heads/main`, `git push origin --delete heads/main`을 훅에 넣으니 넷 다 0이었고, 같은 명령의 `git push`를 `git push --dry-run --porcelain`으로 바꿔 bash에 돌리니 앞의 둘은 `refs/heads/main:refs/heads/main`과 `refs/heads/tasks/x:refs/heads/main`을, 뒤의 둘은 `:refs/heads/main [deleted]`를 냈다. phase 1(`f8f219b`)의 훅도 0이다. 완료 조건 1의 "기본 브랜치를 가리키는 push"와 "기본 브랜치를 지우는 push"에 들고, 셸 구문이 아니라 git의 refspec이라 task 머리 다섯째 결정의 약속 밖("그 밖의 셸 구문")에 들지 않는다 (`plugins/plate/hooks/push_guard.py`). 기준: 결함
- 기본 브랜치에 있는 채 `--repo`로 origin 밖 원격을 적은 push를 막는다. `git push --repo=<원격>`은 위치 인자의 `<repository>`와 같은데, `push_args`(168~196줄)는 `--repo=…`를 다른 `--` 옵션처럼 넘기고(184~185줄) `--repo <원격>`은 값을 건너뛰기만 해서(28줄, 182~183줄), `blocked_branch`가 원격을 설정의 `origin`으로 보고(259줄) 대상이 없으니 기본 브랜치에 있다는 까닭으로 막는다(265줄). 같은 스크래치에 bare 원격 `fork`를 더하고 `main`에서 `git push --repo=fork`와 `git push --repo fork`를 훅에 넣으니 둘 다 "plate: 기본 브랜치(`main`)로 푸시하지 않는다"와 종료 코드 2였고, bash의 `--dry-run --porcelain`은 둘 다 `fork.git`으로만 `refs/heads/main:refs/heads/main [new branch]`를 냈다. 같은 자리의 `git push fork`는 0이다(`test_push_to_remote_other_than_origin`도 같다). phase 1(`f8f219b`)의 훅도 2다. 완료 조건 1의 "origin 밖 원격으로의 푸시는 막지 않는다"에 들고 셸 구문이 아니다 (`plugins/plate/hooks/push_guard.py`). 기준: 결함

**판정**: 문제 있음
