# Phase 1: tasks 끝의 문제를 고친다

**목표**: task 머리의 완료 조건에 적힌 것을 모두 고친다.

**테스트 먼저**: 예

**읽을 것**
- `docs/tasks/review.md`의 `## 평가 1` 절
- `docs/tasks/eval.md`의 `## eval 1` 절
- `plugins/plate/hooks/edit_guard.py`
- `plugins/plate/skills/phase/SKILL.md`
- `tests/test_edit_guard.py`
- `tests/hook_helpers.py`
- `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `docs/BACKLOG.md`, `docs/cleanup/2026-10-29.md`

**TODO**
- [ ] 다시 수행의 테스트 셈이 전체 역사에서 같은 제목의 커밋을 찾아, 지난 tasks의 같은 이름 phase 커밋이 테스트를 바꿨으면 이번 phase가 테스트를 바꾸지 않았어도 구현 편집을 통과시킨다. 갈라진 곳 뒤나 이 tasks의 계획 커밋 뒤의 커밋으로 좁힌다. 고친 뒤 ARCHITECTURE "막는 장치" 문단의 다시 수행 줄이 고친 동작과 맞게 한다 (`plugins/plate/hooks/edit_guard.py`, `docs/ARCHITECTURE.md`, `tests/test_edit_guard.py`)
- [ ] phase 본문의 새 구현 파일 옮기기가 파일이 여럿일 때 임시 자리를 잃거나 같은 이름끼리 덮이지 않게 하고, `git status --porcelain`이 다를 때 되살리는 법을 적는다 (`plugins/plate/skills/phase/SKILL.md`)
- [ ] `STOP`의 글이 "세 번째"를 손으로 적어 `STOP_COUNT`와 따로 노는 것을 상수에서 만들게 고친다. 그 글을 지키는 테스트(`tests/test_edit_guard.py:540`)도 고친 글을 지키게 한다 (`plugins/plate/hooks/edit_guard.py`, `tests/test_edit_guard.py`)
- [ ] phase 커밋에서 테스트 파일을 지우기만 한 경우를 다시 수행의 셈에서 빼는지 보는 시험을 더한다 (`tests/test_edit_guard.py`)
- [ ] 고친 코드에서 같은 뿌리의 꼴(같은 함수의 다른 입력, 앞서 막던 꼴)을 찾아 테스트로 남긴다 (`tests/test_edit_guard.py`)

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다
