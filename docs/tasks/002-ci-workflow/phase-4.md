# Phase 4: 회고 3의 문제를 고친다

**목표**: 회고 3에서 나온 문제를 모두 고친다.

**테스트 먼저**: 예

**읽을 것**
- `docs/tasks/002-ci-workflow/retro.md`의 `## 회고 3` 절
- `plugins/plate/hooks/edit_guard.py`
- `tests/test_edit_guard.py`
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/ADR.md`
- `docs/TOOLS.md`

**TODO**
- [ ] 이미 셋업된 프로젝트에서 남은 phase가 테스트 먼저일 때 setup을 다시 불러 CI 에이전트를 승인하면 워크플로를 쓰지 못한다. phase 3이 `edit_guard.py`의 CI 워크플로 예외(215~216줄)를 `if not tasks:`(214줄) 안으로 옮겨, 남은 phase가 있으면 새 `plate-review.yml`의 Write도 테스트 먼저 검사(219~229줄)를 받는다. 문서 지도 구간과 커밋된 `tests/test_x.py`가 있는 git 레포를 스크래치에 만들어 그 Write의 훅 입력을 넣어 보니, 남은 phase가 없으면 종료 코드 0, 테스트 먼저가 "아니오"인 `docs/tasks/001-a/phase-1.md`가 남아 있으면 0, "예"인 `phase-1.md`가 남아 있고 커밋되지 않은 테스트 변경이 없으면 "plate: 지금 phase(`docs/tasks/001-a/phase-1.md`)는 테스트 먼저다. …"와 2였다. setup이 워크플로를 쓸 수 있는지가 진행 중인 task의 phase 표시에 따라 갈리고, 막혔을 때 훅의 글은 실패하는 테스트를 먼저 쓰라고 하며 setup 본문에 그때의 길이 없다. 그래서 task 머리의 목표("승인하면 워크플로 파일을 쓰고")가 이 경우에 맞지 않고, 회고 1의 문제가 남은 phase가 있는 경우로 좁혀져 남는다. `docs/ARCHITECTURE.md` 46줄과 48줄은 예외를 남은 phase가 없을 때로 적어 코드와는 맞는다. 회고 2의 문제는 코드와 46줄 가운데 어느 쪽을 고칠지 적지 않았고, phase 3은 코드를 46줄에 맞췄다 (`plugins/plate/hooks/edit_guard.py`, `docs/ARCHITECTURE.md`)

**통과 조건**
- 회고 3의 문제가 모두 고쳐졌다.
  - 확인: 문제마다 적힌 곳을 다시 읽거나 돌린다
- 편집 훅이 task 머리의 결정대로, 아직 없는 `plate-review.yml`의 Write를 남은 phase가 없을 때, 테스트 먼저가 "아니오"인 phase가 남았을 때, "예"인 phase가 남았을 때 모두 통과시키고, 이미 있는 그 파일의 Edit·Write와 `other.yml`의 Write는 막는다. `docs/ARCHITECTURE.md`와 코드의 주석이 같은 범위를 적는다.
  - 확인: `python3 -m unittest discover -s tests`가 통과하고, `tests/test_edit_guard.py`를 읽어 이 경우마다 테스트가 있다
  - 확인: `docs/ARCHITECTURE.md`의 훅 설명과 PR의 CI 항목, `edit_guard.py`의 예외 주석을 읽는다
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다
