# Phase 1: 훅과 단위 테스트

**목표**: 플러그인의 Claude Code 훅이 코드 파일 편집을 완료 조건 1의 경우대로 막거나 통과시키고, `tests/`의 단위 테스트가 그것을 보인다.

**읽을 것**
- `plugins/plate/skills/plan/SKILL.md` (낱말 "테스트가 있는 프로젝트", 0번의 셋업 판단)
- `plugins/plate/skills/run/SKILL.md` (0번 대상 작업을 정하는 규칙, 낱말 "남은 첫 phase"·"끝나지 않은 작업")
- `plugins/plate/skills/phase/SKILL.md` (5번: phase가 끝날 때만 커밋한다)
- `plugins/plate/.claude-plugin/plugin.json`
- `docs/TOOLS.md` (Claude Code 절: `--plugin-dir`, 헤드리스 허용 목록의 `Bash(python3:*)`)

**TODO**
- [x] 완료 조건 1의 경우마다 상황을 만들고 결과를 단언하는 단위 테스트가 `tests/`에 생기고, 훅이 없는 상태에서 돌린 실패 출력이 기록에 남는다 (`tests/`)
- [x] 플러그인을 켜면 실리는 PreToolUse 훅이 파일 편집 도구의 호출을 보고 완료 조건 1의 경우대로 막거나 통과시킨다. 막을 때 에이전트가 받는 글에 까닭과 할 일(계획부터 / 실패하는 테스트부터 / 세 번째면 막힘으로 멈추고 까닭과 해결책을 적는다)이 있다 (`plugins/plate/hooks/`)
- [x] 단위 테스트가 모두 통과한다

**통과 조건**
- 완료 조건 1과 13이 참이다.
  - 확인: 완료 조건 1, 13의 확인을 모두 돌린다

## 한 일
- 완료 조건 1의 경우마다 상황을 만들고 결과를 단언하는 단위 테스트가 `tests/`에 생기고, 훅이 없는 상태에서 돌린 실패 출력이 기록에 남는다: 시험마다 임시 폴더에 git 프로젝트를 만들고 PreToolUse의 JSON을 훅에 주어 종료 코드(2는 막음, 0은 통과)와 stderr의 글을 단언하는 시험 31개를 썼다. setup 안 됨, 코드 파일이 아님(`.md`, `.worktrees/` 아래, 프로젝트 밖), 남은 phase 없음(테스트 있음/없음/git 아님, 끝난 작업만 있음, Write·NotebookEdit, 테스트 파일도 막힘), 테스트 먼저 "예"의 막음과 통과(커밋되지 않은 테스트 변경이 고침/새 파일/스테이징, 다른 변경만 있음, 앞 커밋의 테스트 변경, "아니오", 표시 없음, 테스트 없는 프로젝트, git 아님, 테스트 파일 꼴 여덟과 아닌 꼴 둘), 매니페스트의 테스트 명령, 지금 phase를 고르는 규칙, 세 번째 막음(같은 파일, 파일마다 셈, 계획이 바뀌면 다시 셈, 체크박스와 기록 절은 계획이 아님, 계획부터는 세지 않음)이다. 훅이 없을 때의 실패 출력은 "확인 결과"의 첫 항목에 있다 (`tests/test_edit_guard.py`)
- 플러그인을 켜면 실리는 PreToolUse 훅이 파일 편집 도구의 호출을 보고 완료 조건 1의 경우대로 막거나 통과시킨다: `hooks/hooks.json`이 `Edit|Write|MultiEdit|NotebookEdit`에 `python3 "${CLAUDE_PLUGIN_ROOT}/hooks/edit_guard.py"`를 건다. 스크립트는 Python 3 표준 라이브러리만 쓰고, 막을 때 종료 코드 2로 끝나며 stderr에 까닭과 할 일을 적는다. 계획부터는 "`plate:plan`으로 계획을 세우고 `plate:run`으로 실행한다", 테스트 먼저는 "실패하는 테스트부터 쓴다. 돌려 실패 출력을 기록에 남기고 그 뒤에 구현한다"와 테스트 파일의 꼴, 세 번째는 "더 시도하지 않는다. 상태를 막힘으로 하고 멈춘다. 막힌 까닭과 원하는 해결책을 `phase-N.md`의 \"남은 것\"과 \"하네스에서 걸린 것\"에 적는다"다. 막은 횟수는 git 폴더의 `plate-test-first.json`에 phase 파일마다 계획의 해시와 함께 둔다 (`plugins/plate/hooks/hooks.json`, `plugins/plate/hooks/edit_guard.py`)
- 단위 테스트가 모두 통과한다: 처음 돌렸을 때 30개가 통과하고 `test_checkbox_and_record_do_not_reset_count`가 실패했다. 기록 절을 덧붙이면 `## 한 일` 위에 빈 줄이 생겨 계획의 해시가 바뀌었기 때문이고, 해시하기 전에 계획 글 끝의 공백을 지워 고쳤다. 그 뒤 31개가 모두 통과했다. `/usr/bin/python3`(3.9.6)로도 31개가 통과했다 (`plugins/plate/hooks/edit_guard.py`)

## 확인 결과
- 훅이 없는 상태의 실패 출력 (TODO 1)
  - `python3 -m unittest discover -s tests -v` → 31개 모두 `FAIL`. 끝 두 줄은 `Ran 31 tests in 4.000s`, `FAILED (failures=39)`(subTest 여덟을 따로 셌다). 실패마다 `AssertionError: '실패하는 테스트부터' not found in "…/python3: can't open file '/Users/gangjungi/Desktop/harness-plate/plugins/plate/hooks/edit_guard.py': [Errno 2] No such file or directory\n"`처럼 훅 파일이 없다는 글이 나왔다. 실패(훅이 없을 때 기대한 결과다)
- 완료 조건 1이 참이다.
  - `python3 -m unittest discover -s tests -v` → 마지막 줄 `OK`(`Ran 31 tests in 7.937s`). 통과
  - `tests/test_edit_guard.py`를 읽었다 → 경우마다 상황을 만들고 막음/통과와 알리는 글을 단언하는 시험이 있다. setup 안 됨 → 통과(`test_setup_not_done_passes`). 코드 파일이 아님 → 통과(`test_non_code_files_pass`). 남은 phase 없음 → 막고 "계획부터"와 "plate:plan"(`test_no_remaining_phase_blocks_code_file`, `test_finished_task_does_not_count`). 테스트 없는 프로젝트도 같다(`test_no_remaining_phase_blocks_in_project_without_tests`). 테스트 먼저 "예"이고 커밋되지 않은 테스트 변경 없음 → 테스트 파일이 아닌 코드 파일을 막고 "실패하는 테스트부터"(`test_blocks_code_without_test_change`, `test_other_uncommitted_change_does_not_count`, `test_test_change_committed_already_does_not_count`). 커밋되지 않은 테스트 변경 있음 → 통과(`test_modified_test_file_passes`, `test_new_untracked_test_file_passes`, `test_staged_test_file_passes`). "아니오" → 통과(`test_marker_no_passes`). 표시 없음 → 통과(`test_no_marker_passes`). 테스트 없는 프로젝트 → 통과(`test_project_without_tests_passes`). 고치는 파일이 테스트 파일 → 통과(`test_editing_test_file_passes`). 같은 phase의 계획이 바뀌지 않은 동안 같은 파일을 세 번째 막음 → "더 시도하지 않는다", "막힘", "까닭", "해결책"(`test_third_block_of_same_file_says_stop`, `test_count_is_per_file`, `test_plan_change_resets_count`, `test_checkbox_and_record_do_not_reset_count`). 통과
- 완료 조건 13이 참이다.
  - `python3 -m unittest discover -s tests` → 마지막 줄 `OK`. 통과

## 계획과 달라진 점
- 계획이 정하지 않은 곳을 아래처럼 했다. 머리와 통과 조건은 바꾸지 않았다.
  - 요청은 훅을 "PreToolUse Edit/Write"로 적었다. 매처는 `Edit|Write|MultiEdit|NotebookEdit`로 했다. 결정의 "훅은 파일 편집 도구의 호출만 본다"에 드는 도구가 넷이기 때문이다. NotebookEdit의 경로는 `notebook_path`에서 읽는다.
  - git 레포가 아닌 프로젝트에서는 계획부터는 그대로 걸고 테스트 먼저 검사는 하지 않는다(통과). 결정이 테스트 변경을 "커밋되지 않은 변경"에서 보는데 git이 없으면 그것을 볼 수 없고, 막으면 테스트를 써도 풀리지 않기 때문이다.
  - "빌드 매니페스트에 테스트 명령이 있다"는 `package.json`의 `scripts.test`(npm이 처음 넣는 `no test specified` 글은 빼고)와 `Makefile`의 `test:` 대상만 본다. plan 스킬의 낱말이 예를 들지 않아 흔한 둘로 했다.
  - 테스트 파일은 결정의 꼴 가운데 `.md`가 아닌 것만 센다(테스트가 있는지, 커밋되지 않은 테스트 변경이 있는지 볼 때). `tests/README.md`만 바꾸고 구현을 통과시키지 않게 하는 것이다.
  - 지금 브랜치가 `task/NNN-slug`인데 그 작업에 남은 phase가 없으면 번호가 가장 작은 끝나지 않은 작업의 남은 첫 phase를 본다.
  - 프로젝트의 최상위는 훅 입력의 `cwd`가 든 git 레포의 최상위(git이 아니면 `cwd`)다. 그 밖의 파일은 통과시킨다.
  - 세 번을 셀 때 계획은 phase 파일에서 `## `로 시작하는 첫 줄 위의 글이고, 체크박스의 `[x]`와 글 끝의 공백은 계획의 변경으로 보지 않는다. 수행이 체크하고 기록 절을 덧붙이는 것만으로 다시 세지 않게 하는 것이다.

## 남은 것
- 없음

## 하네스에서 걸린 것
- 이 레포에는 `.gitignore`가 없어서 `python3 -m unittest discover -s tests`를 돌리면 `tests/__pycache__/test_edit_guard.cpython-313.pyc`가 추적되지 않는 파일로 남는다. 그 경로는 `tests/` 아래라 훅이 커밋되지 않은 테스트 변경으로 센다. 그래서 이 레포에서는 테스트를 한 번 돌린 뒤로 테스트 먼저 검사가 실제 테스트 변경 없이 통과한다(phase 1에는 테스트 먼저 표시가 없어 이번에는 걸리지 않았다). 이번에는 커밋 전에 그 폴더를 지웠다. `.gitignore`에 `__pycache__/`를 두는 것은 이 phase의 TODO에 없어서 하지 않았다.
- 훅 스크립트가 없으면 `python3`이 `can't open file`로 종료 코드 2를 낸다(훅이 없을 때 돌린 시험에서 봤다). Claude Code는 종료 코드 2를 막음으로 읽으므로, 훅의 경로가 틀리면 편집이 통과하지 않고 모두 그 글로 막힌다.

## 회고 1: 회고

**확인**
- 완료 조건 1과 13이 참이다.
  - 완료 조건 1: `python3 -m unittest discover -s tests -v` → 31개 모두 `ok`, 마지막 줄 `OK`(`Ran 31 tests in 9.193s`). 통과
  - 완료 조건 1: `tests/test_edit_guard.py`를 읽었다 → 경우마다 상황을 만들고 막음/통과와 알리는 글을 단언하는 시험이 있다. setup 안 됨(`test_setup_not_done_passes`), 코드 파일이 아님(`test_non_code_files_pass`), 남은 phase 없음에 "계획부터"와 "plate:plan"(`test_no_remaining_phase_blocks_code_file`), 테스트 없는 프로젝트도 같음(`test_no_remaining_phase_blocks_in_project_without_tests`), 테스트 먼저 "예"이고 테스트 변경 없음에 "실패하는 테스트부터"(`test_blocks_code_without_test_change`), 커밋되지 않은 테스트 변경 있음(`test_modified_test_file_passes`, `test_new_untracked_test_file_passes`, `test_staged_test_file_passes`), "아니오"(`test_marker_no_passes`), 표시 없음(`test_no_marker_passes`), 테스트 없는 프로젝트(`test_project_without_tests_passes`), 테스트 파일을 고침(`test_editing_test_file_passes`), 세 번째 막음에 "더 시도하지 않는다", "막힘", "까닭", "해결책"(`test_third_block_of_same_file_says_stop`)과 계획이 바뀌면 다시 셈(`test_plan_change_resets_count`). 통과
  - 완료 조건 13: `python3 -m unittest discover -s tests` → 마지막 줄 `OK`(`Ran 31 tests in 8.930s`). 통과

**문제**
- 없음

**배운 것**
- 이 레포에는 `.gitignore`가 없어서 테스트를 돌리면 `tests/__pycache__/`가 추적되지 않는 파일로 남는다. 커밋에 들지 않게 지워야 한다.
- 훅이 테스트 먼저로 막은 횟수는 git 폴더(`git rev-parse --absolute-git-dir`)의 `plate-test-first.json`에 남고 작업 트리에는 보이지 않는다. 같은 git 폴더에서 계획을 바꾸지 않고 다시 돌리면 앞의 횟수가 이어진다.

**하네스의 문제점**
- 머리의 결정 "테스트 파일은 `tests/`, `test/`, `__tests__/` 아래이거나 …"가 테스트를 돌려 생기는 파일을 거르지 않는다. 시험 프로젝트(테스트 먼저 "예", `.gitignore` 없음)에서 `src/app.py` 편집은 종료 코드 2로 막혔고, `tests/__pycache__/test_app.cpython-313.pyc`만 만든 뒤에는 종료 코드 0으로 통과했다. `.gitignore`가 없는 Python 프로젝트에서는 테스트를 한 번 돌리기만 해도 테스트 먼저 검사가 풀린다. 이 작업은 테스트 먼저 표시를 쓰지 않아 걸리지 않는다.
- 계획이 훅 스크립트를 열지 못할 때를 정하지 않았다. `python3 /nonexistent/edit_guard.py`는 `can't open file`을 내고 종료 코드 2로 끝나는데, 2는 훅이 막을 때 쓰는 코드다(`plugins/plate/hooks/edit_guard.py`의 머리글). `hooks.json`의 경로가 틀리면 `.md`를 포함한 모든 파일 편집이 그 글로 막힌다.
- plan 스킬의 낱말 "테스트가 있는 프로젝트"의 "빌드 매니페스트에 테스트 명령"이 예를 들지 않아, 수행이 `package.json`의 `scripts.test`와 `Makefile`의 `test:`만 보기로 정했다("계획과 달라진 점"). 테스트 파일 없이 다른 매니페스트에만 테스트 명령이 있는 프로젝트는 plan이 테스트 먼저 "예"를 적어도 훅이 검사하지 않는다.
- retro 스킬 3번의 "맥락 문서와 어긋나지 않는가"가 머리의 결정이 바꾸기로 한 맥락 문서를 가리지 않는다. 이 phase의 훅은 지금의 `docs/ARCHITECTURE.md`("훅은 두지 않는다")와 `docs/PRD.md`(범위 밖의 훅 줄)와 어긋나지만, 결정이 그 줄을 바꾸기로 했고 phase 4가 바꾼다. 이번에는 결정을 따라 문제로 적지 않았다.

**판정**: 통과
