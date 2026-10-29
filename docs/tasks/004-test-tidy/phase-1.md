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
- [x] `test_cleanup_skill.py`의 `section`과 앞머리 읽기가 지워지고 `test_skill_rules`의 `section`·`front_matter`를 불러 쓴다. 바뀐 `section`(펜스 길이를 맞추는 것)으로도 이 파일의 시험이 모두 통과하게 맞춘다 (`tests/test_cleanup_skill.py`)
- [x] 두 훅 시험이 함께 쓰는 도우미(hooks.json에서 matcher로 명령을 골라 `sh -c`로 돌리는 것, 막음·통과 assert)가 `tests/hook_helpers.py`에 생기고, `HooksJsonCommandTest`가 `Edit`가 든 matcher로 명령을 고른다 (`tests/hook_helpers.py`, `tests/test_edit_guard.py`, `tests/test_push_guard.py`)
- [x] `test_skill_rules.py`의 docstring이 파일이 하는 일의 일반 설명으로 바뀐다 (`tests/test_skill_rules.py`)
- [x] `test_manifests.py`에 `test_descriptions_match`가 더해지고 docstring이 description도 견준다고 바뀐다 (`tests/test_manifests.py`)
- [x] 디렉터리 구조 절에 `tests/hook_helpers.py` 줄이 더해지고, `test_manifests.py` 줄이 버전과 description을 견준다고 바뀐다 (`docs/ARCHITECTURE.md`)

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

## 한 일
- `test_cleanup_skill.py`의 `section`과 앞머리 읽기가 지워지고 `test_skill_rules`의 `section`·`front_matter`를 불러 쓴다: 자기 `section` 정의를 지우고 `from test_skill_rules import front_matter, section`을 더했다. `test_name_is_cleanup`은 `front_matter("cleanup")`의 `name`·`description`을 본다. 바뀐 `section`(펜스 길이를 맞춤)으로 28개 시험이 모두 통과한다 (`tests/test_cleanup_skill.py`)
- 두 훅 시험의 공통 도우미가 `tests/hook_helpers.py`에 생기고 `HooksJsonCommandTest`가 `Edit`가 든 matcher로 명령을 고른다: `hook_helpers.py`에 `GIT_ENV`, `PLUGIN_ROOT`, `HOOKS_JSON`, `hook_command(tool)`(matcher에 도구가 든 항목이 하나가 아니면 실패), `run_hook_command(tool, plugin_root, stdin)`(`sh -c`로 돌림), `HookTestCase`(임시 폴더 `setUp`, `assertPassed`, `BLOCK_PHRASES`를 더해 보는 `assertBlocked`)를 두었다. `GuardTestCase`와 `PushGuardTestCase`가 `HookTestCase`를 잇고(푸시 쪽은 `BLOCK_PHRASES = (BLOCKED,)`), 두 `HooksJson` 시험의 `run_command`가 `run_hook_command("Edit"|"Bash", …)`를 부른다. 편집 쪽에 `test_command_runs_edit_guard`를 더했다 (`tests/hook_helpers.py`, `tests/test_edit_guard.py`, `tests/test_push_guard.py`)
- `test_skill_rules.py`의 docstring이 파일이 하는 일의 일반 설명으로 바뀐다: tasks 이름과 이슈 번호 목록을 빼고, 스킬 본문의 규칙 글이 제 절에 있는지와 앞머리 한도를 본다고 적었다 (`tests/test_skill_rules.py`)
- `test_manifests.py`에 `test_descriptions_match`가 더해지고 docstring이 description도 견준다고 바뀐다 (`tests/test_manifests.py`)
- 디렉터리 구조 절에 `tests/hook_helpers.py` 줄이 더해지고 `test_manifests.py` 줄이 버전과 description을 견준다고 바뀐다 (`docs/ARCHITECTURE.md`)

## 확인 결과
- cleanup 시험이 도우미를 불러 쓴다(완료 조건 1).
  - `grep -n -e '^def section' -e '^def front_matter' tests/test_cleanup_skill.py` → 출력 없음(rc=1). 통과
  - `grep -n 'from test_skill_rules import' tests/test_cleanup_skill.py` → `15:from test_skill_rules import front_matter, section  # noqa: E402` 한 줄. 통과
- hooks.json 시험이 차례에 기대지 않고 도우미가 한 곳이다(완료 조건 2).
  - `grep -n -F '["PreToolUse"][0]' tests/test_edit_guard.py tests/test_push_guard.py` → 출력 없음(rc=1). 통과
  - `grep -ln 'hook_helpers' tests/test_edit_guard.py tests/test_push_guard.py` → 두 파일. 통과
  - `cp -R . "$(mktemp -d)/r"` 사본에서 `PreToolUse`를 뒤집어(`['Bash', 'Edit|Write|MultiEdit|NotebookEdit']`) `python3 -m unittest tests.test_edit_guard.HooksJsonCommandTest tests.test_push_guard.HooksJsonTest` → `Ran 6 tests`, `OK`. 통과
- docstring이 일반 설명이다(완료 조건 3).
  - `python3 -c "import ast; …get_docstring…" | grep -n -e 'release-prep' -e '#[0-9]'` → 출력 없음(rc=1). 통과
- 매니페스트 description을 견준다(완료 조건 4).
  - `python3 -m unittest tests.test_manifests -v` → `test_descriptions_match (tests.test_manifests.DescriptionTest) ... ok`, `OK`. 통과
  - 사본의 `plugins/plate/.codex-plugin/plugin.json` description 끝에 `x`를 더해 `python3 -m unittest tests.test_manifests` → `FAILED (failures=1)`. 통과
- ARCHITECTURE가 맞다(완료 조건 6의 앞 두 줄).
  - `grep -n -e 'hook_helpers.py' -e 'test_manifests.py' docs/ARCHITECTURE.md` → 34행, 39행(디렉터리 구조 절, 9~42행). 통과
- 테스트 묶음이 통과한다.
  - `python3 -m unittest discover -s tests` → `Ran 238 tests`, 마지막 줄 `OK`. 통과

## 계획과 달라진 점
- 계획에 없던 `sys.path.insert(0, <tests 폴더>)`를 `test_edit_guard.py`, `test_push_guard.py`, `test_cleanup_skill.py`의 형제 모듈 import 앞에 두었다. 통과 조건의 `python3 -m unittest tests.test_edit_guard.HooksJsonCommandTest tests.test_push_guard.HooksJsonTest`는 저장소 루트에서 돌면 `tests/`가 `sys.path`에 없어, 고치기 전에도 `test_push_guard`의 `from test_edit_guard import …`가 `ModuleNotFoundError`로 실패했다. 대상·패턴·기대를 바꾸지 않고 시험 모듈이 그 명령으로도 import되게 했다.
- 편집 쪽 `HooksJsonCommandTest`에 `test_command_runs_edit_guard`(고른 명령이 `edit_guard.py`를 부르는지)를 더했다. matcher로 고른 명령이 맞는 훅인지 푸시 쪽과 같이 보려는 것이다.

## 남은 것
- `test_skill_rules.py` docstring은 한도를 "description과 name의 한도"로만 적고 숫자를 뺐다. 400자 상한은 phase 2가 정한다.

## 하네스에서 걸린 것
- 통과 조건의 hooks.json 시험 명령(`python3 -m unittest tests.test_edit_guard.HooksJsonCommandTest tests.test_push_guard.HooksJsonTest`)은 계획을 쓸 때 돌려 보지 않은 듯하다. 지금 저장소에서 그대로 돌리면 `test_push_guard`의 import 오류로 실패해, 시험 모듈에 `sys.path` 줄을 더해 돌게 했다.
