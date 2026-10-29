# Phase 1: 편집 훅의 작은 고침 넷

**목표**: 성능-5·6, 신뢰성-10, 유지보수성-5가 편집 훅에서 고쳐진다.

**테스트 먼저**: 예

**읽을 것**
- `docs/cleanup/2026-10-29.md` (성능-5·6, 신뢰성-10, 유지보수성-5의 근거와 고치는 방향)
- `plugins/plate/hooks/edit_guard.py` (`check`, `is_code_file`, `has_tests`, `has_uncommitted_test_change`, `TEST_FIRST`, `TEST_DIRS`, `TEST_NAMES`)
- `tests/test_edit_guard.py` (지금의 시험 차림과 `.md` 시험)

**TODO**
- [x] `check`에서 경로가 `.md`로 끝나면 `git rev-parse`를 부르기 전에 통과시키는 갈래가 더해진다. `docs/tasks/` 아래 파일의 통과는 그대로다 (`plugins/plate/hooks/edit_guard.py`)
- [x] `check`의 테스트 먼저 검사에서 `has_uncommitted_test_change`가 `has_tests`보다 먼저 불린다 (`plugins/plate/hooks/edit_guard.py`)
- [x] `has_uncommitted_test_change`가 상태가 삭제뿐인 항목(`D`, ` D`)을 테스트 변경으로 세지 않게 바뀐다 (`plugins/plate/hooks/edit_guard.py`)
- [x] `TEST_FIRST`의 테스트 파일 설명 줄이 `TEST_DIRS`와 `TEST_NAMES`에서 만들어지게 바뀐다 (`plugins/plate/hooks/edit_guard.py`)
- [x] 위 넷을 지키는 시험이 더해진다: git이 PATH에 없어도 `.md` 편집이 통과한다, 테스트 파일 삭제만으로는 구현 편집이 막힌다, 막는 글에 상수의 이름들이 든다 (`tests/test_edit_guard.py`)

**통과 조건**
- `.md` 편집은 git 없이 통과한다(성능-5).
  - 확인: `command -v python3`로 얻은 경로를 써서 `env PATH=/nonexistent <python3 경로> plugins/plate/hooks/edit_guard.py`에 `{"tool_input": {"file_path": "README.md"}, "cwd": "<mktemp -d로 만든 셋업된 git 레포>"}`를 넣는다 → 종료 0
- 커밋하지 않은 테스트 변경을 먼저 본다(성능-6).
  - 확인: `grep -n -e 'has_uncommitted_test_change(root)' -e 'has_tests(root)' plugins/plate/hooks/edit_guard.py` → `check` 함수 안에서 `has_uncommitted_test_change`의 줄이 앞선다
- 테스트 파일 삭제만으로는 통과하지 않는다(신뢰성-10).
  - 확인: 셋업된 시험 레포(테스트 먼저 "예"인 `phase-1.md`, 커밋된 `tests/test_x.py`·`tests/test_y.py`·`src.py`)에서 `git rm tests/test_x.py`만 한 뒤 `src.py` 편집 JSON → 종료 2
- 막는 글이 상수에서 만들어진다(유지보수성-5).
  - 확인: `grep -c -F '`test_*`, `*_test.*`' plugins/plate/hooks/edit_guard.py` → `0`
  - 확인: `python3 -c "import sys; sys.path.insert(0, 'plugins/plate/hooks'); import edit_guard as g; print(all(n in g.TEST_FIRST for n in g.TEST_NAMES) and all(d in g.TEST_FIRST for d in g.TEST_DIRS))"` → `True`
- 테스트 묶음이 통과한다.
  - 확인: `python3 -m unittest discover -s tests` → 마지막 줄이 `OK`

## 한 일
- `check`에서 경로가 `.md`로 끝나면 `git rev-parse`를 부르기 전에 통과시키는 갈래가 더해진다: `file_path`(또는 `notebook_path`)가 대소문자 없이 `.md`로 끝나면 cwd·git을 보기 전에 `None`을 돌려준다. `docs/tasks/` 아래 `.md`가 아닌 파일은 지금처럼 `is_code_file`로 통과한다 (`plugins/plate/hooks/edit_guard.py`)
- `check`의 테스트 먼저 검사에서 `has_uncommitted_test_change`가 `has_tests`보다 먼저 불린다: 한 줄의 `or` 조건을 세 `if`로 나눠 `is_test_first` → `has_uncommitted_test_change` → `has_tests` 차례로 본다 (`plugins/plate/hooks/edit_guard.py`)
- `has_uncommitted_test_change`가 상태가 삭제뿐인 항목(`D`, ` D`)을 테스트 변경으로 세지 않게 바뀐다: 상태 두 칸을 `strip()`한 것이 `D`이면 경로를 넣지 않는다 (`plugins/plate/hooks/edit_guard.py`)
- `TEST_FIRST`의 테스트 파일 설명 줄이 `TEST_DIRS`와 `TEST_NAMES`에서 만들어지게 바뀐다: `sorted(TEST_DIRS)`와 `TEST_NAMES`를 백틱으로 감싸 `", "`로 잇는다. 폴더의 차례가 `__tests__/`, `test/`, `tests/`로 바뀌었다 (`plugins/plate/hooks/edit_guard.py`)
- 위 넷을 지키는 시험이 더해진다: `test_md_file_passes_without_git`(PATH=/nonexistent에서 `README.md`, `docs/notes.MD` 통과), `test_deleted_test_file_only_does_not_count`(`git rm`만 한 것과 작업 트리에서만 지운 것 모두 막음), `test_message_names_test_file_rules`(막는 글에 상수의 이름이 모두 들고, 훅 소스에 손으로 적은 목록이 없다). `Project.edit`에 `env` 인자를 더하고, 시험이 `edit_guard`에서 `TEST_DIRS`, `TEST_NAMES`를 불러온다 (`tests/test_edit_guard.py`)
- 테스트 먼저
  - 실패: `python3 -m unittest tests.test_edit_guard` → `FAIL: test_md_file_passes_without_git (tests.test_edit_guard.SetupAndCodeFileTest)`, `FAIL: test_deleted_test_file_only_does_not_count (tests.test_edit_guard.TestFirstTest)`, `FAIL: test_message_names_test_file_rules (tests.test_edit_guard.TestFirstTest)`, `Ran 47 tests in 6.762s`, `FAILED (failures=3)`
  - 통과: `python3 -m unittest tests.test_edit_guard` → `Ran 47 tests in 6.825s`, `OK`

## 확인 결과
- `.md` 편집은 git 없이 통과한다(성능-5).
  - scratchpad에 `mktemp -d`로 만든 셋업된 git 레포(`AGENTS.md`에 `<!-- plate:docs-map:start -->`, `tests/test_x.py`·`tests/test_y.py`·`src.py`, 테스트 먼저 "예"인 `docs/tasks/001-a/phase-1.md` 커밋)에 `printf '{"tool_input": {"file_path": "README.md"}, "cwd": "<레포>"}' | env PATH=/nonexistent $(command -v python3) plugins/plate/hooks/edit_guard.py` → `exit=0`. 통과
- 커밋하지 않은 테스트 변경을 먼저 본다(성능-6).
  - `grep -n -e 'has_uncommitted_test_change(root)' -e 'has_tests(root)' plugins/plate/hooks/edit_guard.py` → `130:def has_tests(root):`, `155:def has_uncommitted_test_change(root):`, `236:    if has_uncommitted_test_change(root):`, `238:    if not has_tests(root):`. `check`(201행부터) 안에서 236행이 238행보다 앞선다. 통과
- 테스트 파일 삭제만으로는 통과하지 않는다(신뢰성-10).
  - 같은 레포에서 `git rm -q tests/test_x.py`(상태 `D  tests/test_x.py`) 뒤 `src.py` 편집 JSON → stderr에 `TEST_FIRST` 글, `exit=2`. 통과
- 막는 글이 상수에서 만들어진다(유지보수성-5).
  - `grep -c -F '`test_*`, `*_test.*`' plugins/plate/hooks/edit_guard.py` → `0`. 통과
  - `python3 -c "import sys; sys.path.insert(0, 'plugins/plate/hooks'); import edit_guard as g; print(all(n in g.TEST_FIRST for n in g.TEST_NAMES) and all(d in g.TEST_FIRST for d in g.TEST_DIRS))"` → `True`. 통과
- 테스트 묶음이 통과한다.
  - `python3 -m unittest discover -s tests` → `Ran 210 tests in 17.149s`, 마지막 줄 `OK`. 통과

## 계획과 달라진 점
- 없음

## 남은 것
- `.md` 갈래는 넘겨받은 경로 글의 끝만 본다. `.md` 이름의 심볼릭 링크가 코드 파일을 가리키면 전에는 실제 경로로 갈랐지만 이제 통과한다. 그 반대(코드 이름의 링크가 `.md`를 가리킴)는 전처럼 실제 경로로 가른다.
- 삭제를 세지 않는 것은 상태가 `D `, ` D`인 항목뿐이다. `AD`, `MD`(스테이지한 뒤 작업 트리에서 지움)는 지금처럼 테스트 변경으로 센다.
- `TEST_FIRST`의 폴더 차례가 `sorted(TEST_DIRS)`라 `tests/`, `test/`, `__tests__/`에서 `__tests__/`, `test/`, `tests/`로 바뀌었다.
- 시험이 `edit_guard`를 불러와 `plugins/plate/hooks/__pycache__/`가 생길 수 있다. 이번 `git status`에는 잡히지 않았다.

## 하네스에서 걸린 것
- 없음
