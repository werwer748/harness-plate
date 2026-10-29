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
- [ ] `check`의 테스트 먼저 검사에, 지금 phase 파일에 `## 확인 N` 절(코드 블록 밖)이 있고 제목이 `NNN-slug: phase N`인 커밋이 테스트 파일(`.md`가 아닌 것)을 바꿨으면 통과시키는 갈래가 더해진다. 그 커밋이 없거나 테스트 파일을 바꾸지 않았으면 지금처럼 막는다 (`plugins/plate/hooks/edit_guard.py`)
- [ ] 위 갈래의 시험이 더해진다: 커밋에 테스트가 있으면 통과, 커밋에 구현만 있으면 막음, 확인 절이 없는 첫 수행은 막음, 확인 절이 코드 블록 안에만 있으면 첫 수행으로 봄 (`tests/test_edit_guard.py`)
- [ ] "막는 장치" 문단의 편집 훅 줄에, 다시 수행(확인 절이 있는 phase)에서는 그 phase 커밋의 테스트 변경도 센다는 것이 더해진다 (`docs/ARCHITECTURE.md`)

**통과 조건**
- 다시 수행의 세 갈래가 결정대로다(완료 조건 1).
  - 확인: 셋업된 시험 레포(테스트 먼저 "예"인 `docs/tasks/001-a/phase-1.md`)에서 `tests/test_x.py`를 고친 `001-a: phase 1` 커밋과 `## 확인 1` 절을 두고 `src.py` 편집 JSON → 종료 0. 그 커밋이 `src.py`만 바꾼 레포 → 종료 2. `## 확인 1` 절이 없는 레포 → 종료 2
- phase 스킬의 규칙(고칠 문제를 받으면 동작을 바꾸는 실패에만 테스트부터 쓴다)과 훅이 같은 것을 시킨다.
  - 확인: `plugins/plate/skills/phase/SKILL.md`의 "2. TODO를 차례로 끝낸다" 절의 그 줄과 새 갈래를 대어, 앞 수행이 테스트를 커밋한 다시 수행에서 테스트 없는 고침이 막히지 않는다
- ARCHITECTURE가 바뀐 동작을 적는다.
  - 확인: `grep -n '다시 수행' docs/ARCHITECTURE.md` → "막는 장치" 문단에 한 줄 이상
- 테스트 묶음이 통과한다.
  - 확인: `python3 -m unittest discover -s tests` → 마지막 줄이 `OK`
