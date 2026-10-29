# Phase 1: 편집 훅의 작은 고침 넷

**목표**: 성능-5·6, 신뢰성-10, 유지보수성-5가 편집 훅에서 고쳐진다.

**테스트 먼저**: 예

**읽을 것**
- `docs/cleanup/2026-10-29.md` (성능-5·6, 신뢰성-10, 유지보수성-5의 근거와 고치는 방향)
- `plugins/plate/hooks/edit_guard.py` (`check`, `is_code_file`, `has_tests`, `has_uncommitted_test_change`, `TEST_FIRST`, `TEST_DIRS`, `TEST_NAMES`)
- `tests/test_edit_guard.py` (지금의 시험 차림과 `.md` 시험)

**TODO**
- [ ] `check`에서 경로가 `.md`로 끝나면 `git rev-parse`를 부르기 전에 통과시키는 갈래가 더해진다. `docs/tasks/` 아래 파일의 통과는 그대로다 (`plugins/plate/hooks/edit_guard.py`)
- [ ] `check`의 테스트 먼저 검사에서 `has_uncommitted_test_change`가 `has_tests`보다 먼저 불린다 (`plugins/plate/hooks/edit_guard.py`)
- [ ] `has_uncommitted_test_change`가 상태가 삭제뿐인 항목(`D`, ` D`)을 테스트 변경으로 세지 않게 바뀐다 (`plugins/plate/hooks/edit_guard.py`)
- [ ] `TEST_FIRST`의 테스트 파일 설명 줄이 `TEST_DIRS`와 `TEST_NAMES`에서 만들어지게 바뀐다 (`plugins/plate/hooks/edit_guard.py`)
- [ ] 위 넷을 지키는 시험이 더해진다: git이 PATH에 없어도 `.md` 편집이 통과한다, 테스트 파일 삭제만으로는 구현 편집이 막힌다, 막는 글에 상수의 이름들이 든다 (`tests/test_edit_guard.py`)

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
