# Phase 3: 회고 2의 문제를 고친다

**목표**: 회고 2에서 나온 문제를 모두 고친다.

**테스트 먼저**: 예

**읽을 것**
- `docs/tasks/002-ci-workflow/retro.md`의 `## 회고 2` 절
- `plugins/plate/hooks/edit_guard.py`
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/ADR.md`
- `docs/TOOLS.md`

**TODO**
- [ ] 편집 훅의 CI 워크플로 예외가 테스트 먼저의 막음도 건너뛴다. `docs/ARCHITECTURE.md` 46줄은 훅이 "`phase-N.md`가 있는 task가 없을 때의 코드 편집(setup이 아직 없는 `.github/workflows/plate-review.yml`을 쓰는 것은 빼고)과 테스트 먼저인 phase에서 테스트 변경 없는 구현 편집을 막는다"고 적어 예외를 남은 phase가 없을 때에만 두지만, `edit_guard.py`의 `check`는 그 예외(212~213줄)를 남은 phase를 보기(215줄) 전에 두어 테스트 먼저 검사(219~229줄)에도 닿지 않는다. 문서 지도 구간, 테스트 먼저가 "예"인 `phase-1.md`, 커밋된 `tests/test_x.py`가 있고 커밋되지 않은 테스트 변경이 없는 git 레포를 스크래치에 만들어 새 `plate-review.yml`의 Write를 넣어 보니 지금 훅은 종료 코드 0, 고치기 전의 훅(`d850595^`)은 "지금 phase(`docs/tasks/001-a/phase-1.md`)는 테스트 먼저다. …"와 2였다(`src/app.py`는 둘 다 2). 코드의 주석도 예외를 "남은 phase가 없어도" 다시 부른 setup이 처음 쓰는 것으로 적는다 (`plugins/plate/hooks/edit_guard.py`, `docs/ARCHITECTURE.md`)

**통과 조건**
- 회고 2의 문제가 모두 고쳐졌다.
  - 확인: 문제마다 적힌 곳을 다시 읽거나 돌린다
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다
