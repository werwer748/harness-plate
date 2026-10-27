# Phase 2: 회고 1의 문제를 고친다

**목표**: 회고 1에서 나온 문제를 모두 고친다.

**테스트 먼저**: 아니오 — 고칠 문제가 `plugins/plate/skills/run/SKILL.md`(`.md`)의 본문뿐이라 코드 파일의 동작을 바꾸지 않는다

**읽을 것**
- `docs/tasks/003-base-branch/retro.md`의 `## 회고 1`부터 `## 회고 1`까지의 절
- `plugins/plate/skills/run/SKILL.md`
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/ADR.md`
- `docs/TOOLS.md`

**TODO**
- [ ] run 1번 3항목은 "그 브랜치가 이미 있으면 `git switch tasks/<이름>`으로 바꾼다"의 뒤에도 같은 물음을 하고 "그 커밋은 이미 `tasks/<이름>`에 들어 있어서 되돌려도 tasks 브랜치에 남는다"고 적는다. 그런데 브랜치를 새로 만들지 않고 이미 있는 브랜치로 바꾼 경우에는 로컬 기본 브랜치의 앞선 커밋이 tasks 브랜치에 없을 수 있다. `mktemp -d`에서 복제본에 `git branch tasks/y`를 먼저 만들고 `main`에 `plan: add task`를 커밋한 뒤 `git switch tasks/y`를 하자 `git log --oneline refs/remotes/origin/main..main`은 1개를 냈고 `git log tasks/y`에는 그 커밋이 없었다(진행 중인 tasks에 task를 더하는 계획을 기본 브랜치에서 커밋한 경우다). 이때 승인하면 `git branch -f`가 그 커밋을 어느 브랜치에도 없게 만들어, 결정의 이유 "커밋은 tasks 브랜치에 남는다"가 틀린다 (`plugins/plate/skills/run/SKILL.md`)

**통과 조건**
- 회고 1의 문제가 모두 고쳐졌다.
  - 확인: 문제마다 적힌 곳을 다시 읽거나 돌린다
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다
