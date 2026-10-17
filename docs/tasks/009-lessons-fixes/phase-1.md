# Phase 1: 훅의 네 결함

**목표**: 훅이 테스트 실행 부산물, 하네스 기록 폴더, 계획 고침, 없는 스크립트를 바르게 다루고 이 레포가 `__pycache__/`를 거른다.

**테스트 먼저**: 예

**읽을 것**
- `plugins/plate/hooks/edit_guard.py` (코드 파일과 테스트 파일의 기준, 막은 횟수를 세는 `count_block`)
- `plugins/plate/hooks/hooks.json` (훅 명령)
- `tests/test_edit_guard.py` (시험 프로젝트를 만들고 훅에 JSON을 주는 틀)
- `docs/TOOLS.md`의 Claude Code 절 훅 묶음 (`${CLAUDE_PLUGIN_ROOT}`가 `--plugin-dir`의 폴더가 된다)
- code.claude.com/docs/en/hooks (명령은 `sh -c`로 돌고, `${CLAUDE_PLUGIN_ROOT}`는 글로 바뀌고 환경 변수로도 넘어간다. 2가 아닌 0이 아닌 종료 코드는 막지 않는다)
- `git show ec2f192:docs/LESSONS.md`의 하네스의 문제점 절에서 (008-tdd, phase 1)의 첫째·둘째 줄, (008-tdd, phase 3)의 첫째 줄, (008-tdd, phase 4)의 둘째 줄, (008-tdd, 검증 1)의 첫째 줄 (고칠 문제의 원문)

**TODO**
- [x] 커밋되지 않은 변경 가운데 `__pycache__/` 아래 파일과 `.pyc` 파일은 테스트 변경으로 세지 않는다. `.gitignore`가 없는 Python 프로젝트에서 테스트를 돌리기만 해서는 테스트 먼저 검사가 풀리지 않는다 (`plugins/plate/hooks/edit_guard.py`)
- [x] `docs/tasks/` 아래 파일은 코드 파일이 아니다. 문서 지도가 있고 남은 phase가 없는 프로젝트에서 `docs/tasks/.gitkeep`을 써도 막지 않는다 (`plugins/plate/hooks/edit_guard.py`)
- [x] 테스트 먼저로 막은 횟수는 그 phase의 계획 줄과 `plan.md`가 바뀌지 않은 동안 센다. `plan.md`만 바뀌어도(결정에 한 줄을 더해도) 다시 센다 (`plugins/plate/hooks/edit_guard.py`)
- [x] `hooks.json`의 명령은 스크립트 파일이 없으면 종료 코드 0으로 끝나고, 있으면 스크립트의 종료 코드로 끝난다 (`plugins/plate/hooks/hooks.json`)
- [x] 위 넷마다 그 상황을 만들고 막음이나 통과를 단언하는 테스트가 있다. `hooks.json`의 명령은 그 글을 `sh -c`로 돌려 본다 (`tests/test_edit_guard.py`)
- [x] 이 레포의 `.gitignore`가 `__pycache__/`를 거른다 (`.gitignore`)

**통과 조건**
- 완료 조건 1이 참이다.
  - 확인: 완료 조건 1의 확인을 모두 돌린다
- 완료 조건 2가 참이다.
  - 확인: 완료 조건 2의 확인을 돌린다

## 한 일
- 커밋되지 않은 변경 가운데 `__pycache__/` 아래 파일과 `.pyc` 파일은 테스트 변경으로 세지 않는다: `is_bytecode`를 더해 `has_uncommitted_test_change`가 그 파일을 뺀다 (`plugins/plate/hooks/edit_guard.py`)
- `docs/tasks/` 아래 파일은 코드 파일이 아니다: `is_code_file`이 `docs/tasks/`로 시작하는 경로를 뺀다. 상대 경로와 견주려고 `TASKS_DIR`을 `os.path.join("docs", "tasks")`에서 `"docs/tasks"`로 바꿨다 (`plugins/plate/hooks/edit_guard.py`)
- 테스트 먼저로 막은 횟수는 그 phase의 계획 줄과 `plan.md`가 바뀌지 않은 동안 센다: `count_block`이 해시하는 글에 그 작업 폴더의 `plan.md` 전체를 더한다. `plan.md`가 없으면 계획 줄만 해시한다 (`plugins/plate/hooks/edit_guard.py`)
- `hooks.json`의 명령은 스크립트 파일이 없으면 종료 코드 0으로 끝나고, 있으면 스크립트의 종료 코드로 끝난다: 명령을 `f="${CLAUDE_PLUGIN_ROOT}/hooks/edit_guard.py"; [ -f "$f" ] || exit 0; exec python3 "$f"`로 바꿨다 (`plugins/plate/hooks/hooks.json`)
- 위 넷마다 그 상황을 만들고 막음이나 통과를 단언하는 테스트가 있다: (가) `test_python_bytecode_is_not_a_test_change`, (나) `test_docs_tasks_files_are_not_code`, (다) `test_plan_md_change_resets_count`, (라) `HooksJsonCommandTest`의 둘(`test_missing_script_exits_zero`, `test_existing_script_exit_code_passes_through`)을 더했다. (라)는 `hooks.json`의 명령 글에서 `${CLAUDE_PLUGIN_ROOT}`를 폴더 경로로 바꾸고 같은 이름의 환경 변수도 주어 `sh -c`로 돌린다. 훅에 줄 JSON을 두 곳에서 쓰려고 `Project.edit`에서 `Project.payload`를 떼어 냈다 (`tests/test_edit_guard.py`)
- 이 레포의 `.gitignore`가 `__pycache__/`를 거른다: `.gitignore`를 새로 만들어 `__pycache__/` 한 줄을 적었다 (`.gitignore`)
- 테스트 먼저
  - 실패: `python3 -m unittest discover -s tests 2>&1 | grep -E '^(FAIL|ERROR|Ran|OK|FAILED)'` → `FAIL: test_missing_script_exits_zero`, `FAIL: test_docs_tasks_files_are_not_code`, `FAIL: test_python_bytecode_is_not_a_test_change`, `FAIL: test_plan_md_change_resets_count`, `Ran 36 tests in 9.697s`, `FAILED (failures=4)`. 단언의 글은 차례로 `2 != 0 : 통과해야 하는데 막았다: python3: can't open file '…/no-such-plugin/hooks/edit_guard.py'`, `` 2 != 0 : 통과해야 하는데 막았다: plate: 남은 phase가 있는 작업이 없어서 코드 파일을 고치지 않는다: `docs/tasks/.gitkeep` ``, `0 != 2 : 막아야 하는데 통과시켰다 (종료 코드 0)`, `'실패하는 테스트부터' not found in 'plate: 테스트 먼저 때문에 같은 파일을 세 번째 막았다: …'`
  - 통과: `python3 -m unittest discover -s tests -v` → 36개 모두 `ok`, `Ran 36 tests in 9.389s`, `OK`

## 확인 결과
- 완료 조건 1이 참이다.
  - `python3 -m unittest discover -s tests -v` → 마지막 줄 `OK` (`Ran 36 tests`). 통과
  - `tests/test_edit_guard.py`를 읽었다 → (가) `TestFirstTest.test_python_bytecode_is_not_a_test_change`가 `.gitignore` 없이 `tests/__pycache__/…pyc`, `tests/test_app.pyc`, `src/__pycache__/…pyc`를 만들고 `src/app.py` 편집이 테스트 먼저로 막히는 것을, 진짜 테스트 변경 뒤에는 통과하는 것을 단언한다. (나) `SetupAndCodeFileTest.test_docs_tasks_files_are_not_code`가 문서 지도가 있고 남은 phase가 없을 때 `docs/tasks/.gitkeep`의 Write가 통과하고(같은 상태의 `src/app.py`는 막힘), 테스트 먼저인 phase에서도 `docs/tasks/001-a/notes.txt`가 통과하는 것을 단언한다. (다) `ThirdBlockTest.test_plan_md_change_resets_count`가 두 번 막은 뒤 `plan.md`의 결정에만 한 줄을 더해 커밋하면 세 번째 편집이 멈춤 글이 아닌 테스트 먼저 글로 막히는 것을 단언한다. (라) `HooksJsonCommandTest`가 `hooks.json`의 명령 글을 `sh -c`로 돌려, 없는 플러그인 폴더면 막을 호출도 종료 코드 0, 있는 폴더면 스크립트의 2(막음)와 0(통과)이 그대로 나오는 것을 단언한다. 통과
- 완료 조건 2가 참이다.
  - `python3 -m unittest discover -s tests` 뒤 `git status --short --untracked-files=all | grep __pycache__` → 출력 없음(grep 종료 코드 1). `tests/__pycache__/`는 디스크에 있다. 통과

## 계획과 달라진 점
- 없음

## 남은 것
- 없음

## 하네스에서 걸린 것
- 계획의 읽을 것(code.claude.com/docs/en/hooks)과 완료 조건 1의 (라)는 명령이 `sh -c`로 돈다고 보지만, 그 문서는 셸 꼴의 명령이 macOS와 Linux에서 `sh -c`, Windows에서는 Git Bash, Git Bash가 없으면 PowerShell로 돈다고 적는다(`shell` 필드로 고를 수 있다). 바꾼 명령(`f=…; [ -f "$f" ] || exit 0; exec python3 "$f"`)은 POSIX 셸 문법이라 PowerShell에서는 2가 아닌 코드로 끝나 막지 않고 훅이 돌지 않는다. 옛 명령(`python3 "…"`)은 PowerShell에서도 돌았다. 완료 조건대로 했고 시험은 이 Mac에서만 돌렸다.

## 회고 1: 회고

**확인**
- 완료 조건 1이 참이다.
  - `python3 -m unittest discover -s tests -v` → 36개 모두 `ok`, `Ran 36 tests in 9.370s`, 마지막 줄 `OK`. 통과
  - `tests/test_edit_guard.py`를 읽었다 → (가) `TestFirstTest.test_python_bytecode_is_not_a_test_change`가 `.gitignore` 없이 `tests/__pycache__/…pyc`, `tests/test_app.pyc`, `src/__pycache__/…pyc`를 만들고 `src/app.py` 편집이 테스트 먼저로 막히는 것을, `tests/test_app.py`를 바꾼 뒤에는 통과하는 것을 단언한다. (나) `SetupAndCodeFileTest.test_docs_tasks_files_are_not_code`가 문서 지도가 있고 남은 phase가 없을 때 `src/app.py`는 막히고 `docs/tasks/.gitkeep`의 Write는 통과하는 것을, 테스트 먼저인 phase에서 `docs/tasks/001-a/notes.txt`가 통과하는 것을 단언한다. (다) `ThirdBlockTest.test_plan_md_change_resets_count`가 두 번 막은 뒤 `plan.md`에만 결정 한 줄을 더해 커밋하면 세 번째 편집이 멈춤 글 없이 테스트 먼저 글로 막히는 것을 단언한다. (라) `HooksJsonCommandTest`가 `hooks.json`에서 명령 글을 읽어 `sh -c`로 돌리고, 없는 플러그인 폴더면 막을 호출도 0, 있는 폴더면 스크립트의 2와 0이 그대로 나오는 것을 단언한다. 통과
- 완료 조건 2가 참이다.
  - `python3 -m unittest discover -s tests` 뒤 `git status --short --untracked-files=all | grep __pycache__` → 출력 없음(grep 종료 코드 1). `tests/__pycache__/test_edit_guard.cpython-313.pyc`는 디스크에 있다. 통과

**문제**
- 없음

**배운 것**
- Claude Code 훅에서 `args`가 없는 명령(셸 꼴)은 macOS와 Linux에서 `sh -c`, Windows에서 Git Bash, Git Bash가 없으면 PowerShell로 돈다. `shell` 필드(`"bash"` | `"powershell"`)로 고를 수 있다. `args`를 주면 셸 없이 `command`를 실행 파일로 바로 띄운다(exec 꼴). 문서는 경로 자리표시가 든 훅에 exec 꼴을 권하지만, `python3`는 없는 스크립트를 받으면 2로 끝나므로(이 Mac의 Python 3.13.2에서 돌려 봄) exec 꼴로 바꾸면 스크립트가 없을 때 막게 된다. 출처: code.claude.com/docs/en/hooks의 "Exec form and shell form"과 command 훅의 `shell` 필드(2026-10-17에 읽음)

**하네스의 문제점**
- 계획의 완료 조건 1의 (라)와 이 phase의 읽을 것(code.claude.com/docs/en/hooks)은 훅 명령이 `sh -c`로 돈다고만 본다. 그 문서는 셸 꼴 명령이 Windows에서 Git Bash, 없으면 PowerShell로 돈다고 적는다. 바뀐 명령(`f=…; [ -f "$f" ] || exit 0; exec python3 "$f"`)은 POSIX 셸 문법인데, PowerShell에서 어떻게 끝나는지는 완료 조건도 시험도 다루지 않는다(시험은 이 Mac의 `sh`로만 돈다). 같은 전제가 완료 조건 8에도 있어, phase 5가 `docs/TOOLS.md`에 "명령은 `sh -c`로 돈다"를 그대로 적으면 Windows의 경우가 빠진다.

**판정**: 통과
