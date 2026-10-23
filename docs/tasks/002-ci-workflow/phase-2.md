# Phase 2: 회고 1의 문제를 고친다

**목표**: 회고 1에서 나온 문제를 모두 고친다.

**테스트 먼저**: 예

**읽을 것**
- `docs/tasks/002-ci-workflow/retro.md`의 `## 회고 1` 절
- `plugins/plate/skills/setup/SKILL.md`
- `plugins/plate/hooks/edit_guard.py`
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/ADR.md`
- `docs/TOOLS.md`

**TODO**
- [ ] 이미 셋업된 프로젝트(`AGENTS.md`에 문서 지도 구간이 있다)에서 setup을 다시 불러 CI 에이전트를 승인하면 워크플로를 쓰지 못한다. setup 3번의 "CI 워크플로"는 편집 훅을 피하려고 워크플로를 `AGENTS.md`보다 먼저 쓰게 하지만, 그 순서는 처음 셋업하는 프로젝트만 풀고, 문서 지도 구간이 이미 있으면 남은 phase가 없는 한 `edit_guard.py`의 `check`(209~214줄)가 `.github/workflows/plate-review.yml`의 Write를 막는다. 문서 지도 구간이 있는 git 레포를 만들고 그 Write의 훅 입력을 넣어 보니 "plate: 남은 phase가 있는 task가 없어서 코드 파일을 고치지 않는다: `.github/workflows/plate-review.yml`"과 종료 코드 2가 나왔다(문서 지도 구간이 없으면 0). setup 2번은 문서 지도 구간이 있는 프로젝트를 다시 부르는 경우를 다루므로, task 머리의 목표("승인하면 워크플로 파일을 쓰고")가 그 경우에 맞지 않고, setup 본문에 막혔을 때의 길이 없다 (`plugins/plate/skills/setup/SKILL.md`, `plugins/plate/hooks/edit_guard.py`)

**통과 조건**
- 회고 1의 문제가 모두 고쳐졌다.
  - 확인: 문제마다 적힌 곳을 다시 읽거나 돌린다
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다
