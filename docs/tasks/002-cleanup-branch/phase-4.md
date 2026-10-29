# Phase 4: 회고 1의 문제를 고친다

**목표**: 회고 1에서 나온 문제를 모두 고친다.

**테스트 먼저**: 아니오 — 고칠 문제가 `.md` 맥락 문서(`docs/ARCHITECTURE.md`)의 글 하나뿐이라 코드 파일의 동작을 바꾸지 않는다.

**읽을 것**
- `docs/tasks/002-cleanup-branch/retro.md`의 `## 회고 1`부터 `## 회고 1`까지의 절
- `docs/ARCHITECTURE.md`
- `plugins/plate/skills/cleanup/SKILL.md`
- `plugins/plate/skills/run/SKILL.md`
- `docs/PRD.md`
- `docs/ADR.md`
- `docs/TOOLS.md`
- `docs/BACKLOG.md`
- `docs/cleanup/`

**TODO**
- [ ] `docs/ARCHITECTURE.md` 54행 패턴과 규칙의 훅 문단이 "스킬마다의 푸시 규칙(phase, check, retro, review, eval, cleanup은 "푸시하지 않는다", run은 "PR을 연다"에서 승인받아 `tasks/<이름>`을 origin에 올릴 때만 푸시한다)"로 남아, 바뀐 cleanup 절대 규칙 3(고른 발견이 없을 때 승인받아 `cleanup/<보고서 이름>`을 푸시)과 run 절대 규칙 5(보낼 곳이 있으면 보낼 곳 브랜치를 푸시)와 어긋난다. 그 글을 바뀐 두 스킬의 절대 규칙과 맞게 고친다. 고칠 동작을 적은 맥락 문서와 README의 줄도 그 글과 맞춘다 (`docs/ARCHITECTURE.md`)

**통과 조건**
- 회고 1의 문제가 모두 고쳐졌다.
  - 확인: `docs/ARCHITECTURE.md`의 패턴과 규칙의 훅 문단에서 스킬마다의 푸시 규칙 글을 다시 읽어, cleanup이 고른 발견이 없을 때 승인받아 `cleanup/<보고서 이름>`을 푸시하는 것과 run이 보낼 곳이 있으면 보낼 곳 브랜치를 푸시하는 것이 `plugins/plate/skills/cleanup/SKILL.md`의 절대 규칙 3과 `plugins/plate/skills/run/SKILL.md`의 절대 규칙 5와 맞는다. `grep -n -F '"푸시하지 않는다"' docs/ARCHITECTURE.md`로 나온 줄에서 cleanup이 "푸시하지 않는다" 스킬 목록에 없다
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다
