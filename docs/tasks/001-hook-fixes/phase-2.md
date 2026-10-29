# Phase 2: 다시 수행에서 그 phase 커밋의 테스트를 센다

**목표**: 신뢰성-1이 고쳐져, 확인 절이 있는 테스트 먼저 phase를 다시 수행할 때 그 phase의 커밋이 테스트를 바꿨으면 구현 편집이 통과한다.

**테스트 먼저**: 예

**읽을 것**
- `docs/cleanup/2026-10-29.md` (신뢰성-1의 근거와 고치는 방향)
- `plugins/plate/hooks/edit_guard.py` (`check`, `plan_lines`, `count_block`)
- `plugins/plate/skills/phase/SKILL.md`의 "2. TODO를 차례로 끝낸다" 절 (고칠 문제를 받은 수행의 테스트 먼저 규칙)
- `docs/ARCHITECTURE.md`의 "패턴과 규칙" 절의 "막는 장치" 문단 (편집 훅의 막음을 적은 줄)
- `tests/test_edit_guard.py`

**TODO**
- [x] `check`의 테스트 먼저 검사에, 지금 phase 파일에 `## 확인 N` 절(코드 블록 밖)이 있고 제목이 `NNN-slug: phase N`인 커밋이 테스트 파일(`.md`가 아닌 것)을 바꿨으면 통과시키는 갈래가 더해진다. 그 커밋이 없거나 테스트 파일을 바꾸지 않았으면 지금처럼 막는다 (`plugins/plate/hooks/edit_guard.py`)
- [x] 위 갈래의 시험이 더해진다: 커밋에 테스트가 있으면 통과, 커밋에 구현만 있으면 막음, 확인 절이 없는 첫 수행은 막음, 확인 절이 코드 블록 안에만 있으면 첫 수행으로 봄 (`tests/test_edit_guard.py`)
- [x] "막는 장치" 문단의 편집 훅 줄에, 다시 수행(확인 절이 있는 phase)에서는 그 phase 커밋의 테스트 변경도 센다는 것이 더해진다 (`docs/ARCHITECTURE.md`)

**통과 조건**
- 다시 수행의 세 갈래가 결정대로다(완료 조건 1).
  - 확인: 셋업된 시험 레포(테스트 먼저 "예"인 `docs/tasks/001-a/phase-1.md`)에서 `tests/test_x.py`를 고친 `001-a: phase 1` 커밋과 `## 확인 1` 절을 두고 `src.py` 편집 JSON → 종료 0. 그 커밋이 `src.py`만 바꾼 레포 → 종료 2. `## 확인 1` 절이 없는 레포 → 종료 2
- phase 스킬의 규칙(고칠 문제를 받으면 동작을 바꾸는 실패에만 테스트부터 쓴다)과 훅이 같은 것을 시킨다.
  - 확인: `plugins/plate/skills/phase/SKILL.md`의 "2. TODO를 차례로 끝낸다" 절의 그 줄과 새 갈래를 대어, 앞 수행이 테스트를 커밋한 다시 수행에서 테스트 없는 고침이 막히지 않는다
- ARCHITECTURE가 바뀐 동작을 적는다.
  - 확인: `grep -n '다시 수행' docs/ARCHITECTURE.md` → "막는 장치" 문단에 한 줄 이상
- 테스트 묶음이 통과한다.
  - 확인: `python3 -m unittest discover -s tests` → 마지막 줄이 `OK`

## 한 일
- `check`의 테스트 먼저 검사에 다시 수행 갈래가 더해진다: phase 파일 전체 글에서 코드 블록(```` ``` ````/`~~~`) 밖의 `## 확인 N` 줄을 찾는 `has_check_section`과, 제목이 정확히 `NNN-slug: phase N`인 커밋마다 `git diff-tree --root -r --name-only --diff-filter=d`로 더하거나 바꾼 파일을 보아 테스트 파일(`.md`·`docs/tasks/` 아닌 것, 바이트코드 아닌 것)이 있는지 보는 `phase_commit_has_test_change`를 더했다. `check`는 커밋하지 않은 테스트 변경을 본 뒤, `has_tests` 앞에서 두 함수가 모두 참이면 통과시킨다. 커밋이 없거나 테스트를 바꾸지 않았으면 지금처럼 막는다 (`plugins/plate/hooks/edit_guard.py`)
- 위 갈래의 시험이 더해진다: `RerunTest` 여섯 시험 — 커밋에 테스트가 있으면 통과, 커밋에 구현만 있으면 막음, 커밋에 바이트코드와 `.md`만 있으면 막음, 다른 phase(`001-a: phase 10`)·다른 task(`002-b: phase 1`)의 커밋은 세지 않음, 확인 절이 없는 첫 수행은 막음, 확인 절이 코드 블록 안에만 있으면 첫 수행으로 봄 (`tests/test_edit_guard.py`)
- "막는 장치" 문단의 편집 훅 줄에, 테스트 변경이 무엇인지와 다시 수행에서는 그 phase 커밋의 테스트 변경도 센다는 것, 그 까닭(phase 스킬의 고칠 문제 규칙)을 더했다 (`docs/ARCHITECTURE.md`)
- 테스트 먼저
  - 실패: `python3 -m unittest tests.test_edit_guard.RerunTest` → `FAIL: test_phase_commit_with_test_change_passes (tests.test_edit_guard.RerunTest)` … `Ran 6 tests in 1.007s` / `FAILED (failures=1)`
  - 통과: `python3 -m unittest tests.test_edit_guard.RerunTest` → `Ran 6 tests in 1.030s` / `OK`

## 확인 결과
- 다시 수행의 세 갈래가 결정대로다(완료 조건 1).
  - `mktemp -d`로 만든 시험 레포 셋(`AGENTS.md`에 `<!-- plate:docs-map:start -->`, `tests/test_x.py`·`src.py` 커밋, `docs/tasks/001-a/plan.md`, `**테스트 먼저**: 예`인 `phase-1.md`)에 `{"tool_input": {"file_path": "<레포>/src.py"}, "cwd": "<레포>"}`를 넣음 → `tests/test_x.py`를 고친 `001-a: phase 1` 커밋과 `## 확인 1` 절: `exit=0`. 커밋이 `src.py`만 바꿈: `exit=2`. `## 확인 1` 절 없음: `exit=2`. 통과
- phase 스킬의 규칙과 훅이 같은 것을 시킨다.
  - `plugins/plate/skills/phase/SKILL.md` "2. TODO를 차례로 끝낸다"의 "고칠 문제를 넘겨받았으면 동작을 바꾸는 실패에만 테스트부터 쓴다"를 새 갈래에 대어 봄 → 고칠 문제를 받은 수행의 phase 파일에는 확인하는 쪽이 더한 `## 확인 N` 절이 있고, 첫 수행이 테스트를 커밋했으면(`NNN-slug: phase N`) 커밋하지 않은 테스트 변경이 없어도 구현 편집이 통과한다(위 레포 A, `test_phase_commit_with_test_change_passes`). 테스트 없는 고침이 막히지 않는다. 통과
- ARCHITECTURE가 바뀐 동작을 적는다.
  - `grep -n '다시 수행' docs/ARCHITECTURE.md` → `53:`의 "막는 장치" 문단 한 줄. 통과
- 테스트 묶음이 통과한다.
  - `python3 -m unittest discover -s tests` → `Ran 216 tests in 18.402s` / `OK`. 통과

## 계획과 달라진 점
- 없음

## 남은 것
- 같은 제목(`NNN-slug: phase N`)의 커밋이 여럿이면 어느 하나라도 테스트를 바꿨으면 센다. 고침 커밋(`NNN-slug: phase N 고침`)이 바꾼 테스트는 결정대로 세지 않는다.
- 다시 수행 갈래는 `git log` 전체를 훑으므로 이력이 긴 레포에서는 확인 절이 있는 phase의 막음마다 그만큼 느려진다. 확인 절이 없으면 git을 더 부르지 않는다.

## 하네스에서 걸린 것
- 없음
