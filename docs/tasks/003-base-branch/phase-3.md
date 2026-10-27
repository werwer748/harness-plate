# Phase 3: 회고 2의 문제를 고친다

**목표**: 회고 2에서 나온 문제를 모두 고친다.

**테스트 먼저**: 아니오 — 고칠 문제가 `docs/ARCHITECTURE.md`, `README.md`, `plugins/plate/skills/run/SKILL.md`(모두 `.md`)의 글뿐이라 코드 파일의 동작을 바꾸지 않는다

**읽을 것**
- `docs/tasks/003-base-branch/retro.md`의 `## 회고 1`부터 `## 회고 2`까지의 절
- `docs/ARCHITECTURE.md`
- `README.md`
- `plugins/plate/skills/run/SKILL.md`
- `docs/PRD.md`
- `docs/ADR.md`
- `docs/TOOLS.md`

**TODO**
- [ ] 완료 조건 4의 확인이 실패했다. phase 2가 앞선 커밋 가운데 tasks 브랜치에 없는 것이 있으면 묻지 않게 바꿨는데, `docs/ARCHITECTURE.md` "데이터 흐름"의 실행 줄과 `README.md` 표의 `run` 행, run의 frontmatter description은 여전히 "계획의 커밋이 로컬 기본 브랜치에만 있으면 … 되돌릴지 묻는다"고만 적는다. 이미 있던 tasks 브랜치로 바꾼 갈래에서는 계획의 커밋이 로컬 기본 브랜치에만 있어도 묻지 않는다. 고칠 쪽은 문서다 (`docs/ARCHITECTURE.md`, `README.md`, `plugins/plate/skills/run/SKILL.md`)

**통과 조건**
- 회고 2의 문제가 모두 고쳐졌다.
  - 확인: 문제마다 적힌 곳을 다시 읽거나 돌린다
- 앞선 회고 1의 문제가 고친 대로 그대로다.
  - 확인: 회고 1의 문제마다 적힌 재현을 모두 다시 돌린다
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다
