# Phase 2: 회고 1의 문제를 고친다

**목표**: 회고 1에서 나온 문제를 모두 고친다.

**테스트 먼저**: 아니오 — `.md`만 고친다

**읽을 것**
- `docs/tasks/004-run-pr/retro.md`의 `## 회고 1` 절
- `plugins/plate/skills/run/SKILL.md`
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/ADR.md`
- `docs/TOOLS.md`

**TODO**
- [ ] `docs/ARCHITECTURE.md` 48줄(패턴과 규칙의 막는 장치 문단)은 "에이전트의 푸시를 막는 기본은 스킬마다의 '푸시하지 않는다' 규칙이고, 푸시 훅은 흔한 꼴을 한 번 더 막는다"고 적는데, 이 task가 run의 절대 규칙 5(`plugins/plate/skills/run/SKILL.md` 20줄)의 "푸시하지 않는다"를 "푸시는 'PR을 연다'에서 승인받아 `tasks/<이름>`을 origin에 올릴 때만 한다"로 바꿔 run에는 그 규칙이 없다. 49줄의 run 규칙은 이 푸시를 적지만 48줄은 고치지 않아 같은 문서의 두 줄이 어긋난다. phase 1의 TODO와 완료 조건 3이 ARCHITECTURE에서 run 규칙과 데이터 흐름만 가리켰다(`docs/ARCHITECTURE.md`).

**통과 조건**
- 회고 1의 문제가 모두 고쳐졌다.
  - 확인: 문제마다 적힌 곳을 다시 읽거나 돌린다
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다
