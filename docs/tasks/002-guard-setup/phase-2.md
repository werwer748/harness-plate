# Phase 2: 편집 훅의 CODEOWNERS 예외

**목표**: 편집 훅이 아직 없는 `.github/CODEOWNERS`의 쓰기를 막지 않고, 이미 있는 것의 편집은 막는다.

**테스트 먼저**: 예

**읽을 것**
- `plugins/plate/hooks/edit_guard.py`의 `CI_WORKFLOW`와 그것을 처음 쓸 때 통과시키는 자리 (같은 꼴의 예외)
- `tests/test_edit_guard.py`에서 `.github/workflows/plate-review.yml`을 다루는 시험 (같은 꼴의 시험)
- `docs/ARCHITECTURE.md`의 20줄, 49줄, 51줄 (편집 훅과 그 예외를 적은 줄)

**TODO**
- [ ] `tests/test_edit_guard.py`에 `.github/CODEOWNERS` 시험이 더해진다. 경우는 셋이다: 남은 phase가 없을 때의 처음 쓰기는 통과, 테스트 먼저인 phase에서의 처음 쓰기도 통과, 이미 있으면 계획 먼저·테스트 먼저로 막음. 구현 전에 돌려 실패를 본다 (`tests/test_edit_guard.py`)
- [ ] `edit_guard.py`가 아직 없는 `.github/CODEOWNERS`를 `plate-review.yml`처럼 통과시키도록 바뀐다 (`plugins/plate/hooks/edit_guard.py`)
- [ ] `docs/ARCHITECTURE.md` 49줄과 51줄의 "아직 없는 `plate-review.yml`" 예외에 `.github/CODEOWNERS`가 더해진다. 20줄이 그 예외를 적으면 같이 바뀐다 (`docs/ARCHITECTURE.md`)

**통과 조건**
- (완료 조건 2) 훅 예외가 시험으로 닫힌다
  - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
  - 확인: `tests/test_edit_guard.py`를 읽어 세 경우(남은 phase 없을 때 처음 쓰기 통과, 테스트 먼저에서 처음 쓰기 통과, 이미 있으면 막음)가 저마다 시험에 있다
  - 확인: 이 phase의 기록에 새 시험이 실패한 출력과 통과한 출력이 이 순서로 있다
- (완료 조건 1) 판정 시험이 그대로 통과한다
  - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
- `docs/ARCHITECTURE.md`가 훅 예외와 맞는다
  - 확인: 20줄, 49줄, 51줄을 하나씩 읽어 셋 모두 `.github/CODEOWNERS`의 처음 쓰기 예외와 어긋나지 않는다
