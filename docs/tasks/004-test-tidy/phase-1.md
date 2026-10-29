# Phase 1: 테스트 도우미와 낡은 글을 정리한다

**목표**: 유지보수성-2·3·4·6이 고쳐진다.

**테스트 먼저**: 아니오 — 테스트를 리팩터링하고 시험 하나를 더할 뿐 코드의 동작을 바꾸지 않는다

**읽을 것**
- `docs/cleanup/2026-10-29.md` (유지보수성-2·3·4·6의 근거와 고치는 방향)
- `tests/test_cleanup_skill.py` (`section`, 앞머리 읽기, `block`)
- `tests/test_skill_rules.py` (`section`, `front_matter`, docstring)
- `tests/test_edit_guard.py` (`GuardTestCase`, `HooksJsonCommandTest`)
- `tests/test_push_guard.py` (`PushGuardTestCase`, `HooksJsonTest`)
- `tests/test_manifests.py`
- `plugins/plate/hooks/hooks.json`
- `docs/ARCHITECTURE.md`의 디렉터리 구조 절의 `tests/` 줄들

**TODO**
- [ ] `test_cleanup_skill.py`의 `section`과 앞머리 읽기가 지워지고 `test_skill_rules`의 `section`·`front_matter`를 불러 쓴다. 바뀐 `section`(펜스 길이를 맞추는 것)으로도 이 파일의 시험이 모두 통과하게 맞춘다 (`tests/test_cleanup_skill.py`)
- [ ] 두 훅 시험이 함께 쓰는 도우미(hooks.json에서 matcher로 명령을 골라 `sh -c`로 돌리는 것, 막음·통과 assert)가 `tests/hook_helpers.py`에 생기고, `HooksJsonCommandTest`가 `Edit`가 든 matcher로 명령을 고른다 (`tests/hook_helpers.py`, `tests/test_edit_guard.py`, `tests/test_push_guard.py`)
- [ ] `test_skill_rules.py`의 docstring이 파일이 하는 일의 일반 설명으로 바뀐다 (`tests/test_skill_rules.py`)
- [ ] `test_manifests.py`에 `test_descriptions_match`가 더해지고 docstring이 description도 견준다고 바뀐다 (`tests/test_manifests.py`)
- [ ] 디렉터리 구조 절에 `tests/hook_helpers.py` 줄이 더해지고, `test_manifests.py` 줄이 버전과 description을 견준다고 바뀐다 (`docs/ARCHITECTURE.md`)

**통과 조건**
- cleanup 시험이 도우미를 불러 쓴다(완료 조건 1).
  - 확인: `grep -n -e '^def section' -e '^def front_matter' tests/test_cleanup_skill.py` → 아무것도 나오지 않음
  - 확인: `grep -n 'from test_skill_rules import' tests/test_cleanup_skill.py` → 한 줄
- hooks.json 시험이 차례에 기대지 않고 도우미가 한 곳이다(완료 조건 2).
  - 확인: `grep -n -F '["PreToolUse"][0]' tests/test_edit_guard.py tests/test_push_guard.py` → 아무것도 나오지 않음
  - 확인: `grep -ln 'hook_helpers' tests/test_edit_guard.py tests/test_push_guard.py` → 두 파일
  - 확인: 작업 트리를 `cp -R`로 `mktemp -d` 사본에 옮기고, 사본의 `plugins/plate/hooks/hooks.json`에서 `PreToolUse`의 두 항목 차례를 바꿔 사본에서 `python3 -m unittest tests.test_edit_guard.HooksJsonCommandTest tests.test_push_guard.HooksJsonTest` → `OK`
- docstring이 일반 설명이다(완료 조건 3).
  - 확인: `python3 -c "import ast; print(ast.get_docstring(ast.parse(open('tests/test_skill_rules.py', encoding='utf-8').read())))"` → `release-prep`도 `#` 뒤에 숫자가 붙은 이슈 번호도 없다
- 매니페스트 description을 견준다(완료 조건 4).
  - 확인: `python3 -m unittest tests.test_manifests -v` → `test_descriptions_match`가 있고 `OK`
  - 확인: 작업 트리를 `cp -R`로 `mktemp -d` 사본에 옮기고, 사본의 `plugins/plate/.codex-plugin/plugin.json`의 description 끝에 `x`를 더해 사본에서 `python3 -m unittest tests.test_manifests` → 실패(`FAILED`)
- ARCHITECTURE가 맞다(완료 조건 6의 앞 두 줄).
  - 확인: `grep -n -e 'hook_helpers.py' -e 'test_manifests.py' docs/ARCHITECTURE.md` → 디렉터리 구조 절에 둘 다
- 테스트 묶음이 통과한다.
  - 확인: `python3 -m unittest discover -s tests` → 마지막 줄이 `OK`
