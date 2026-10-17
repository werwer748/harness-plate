# Phase 3: retro, verify, context의 규칙 충돌

**목표**: retro, verify, context 본문의 규칙 충돌이 풀리고, 회고·검증 절에 통과한 테스트 먼저 점검이 남는다.

**테스트 먼저**: 아니오 — 스킬 본문(`.md`)만 고친다

**읽을 것**
- `plugins/plate/skills/retro/SKILL.md` (1번, 3번, 4번, 회고 절의 양식, 적는 규칙)
- `plugins/plate/skills/verify/SKILL.md` (1번, 3번, 4번, 검증 절의 양식, 적는 규칙)
- `plugins/plate/skills/context/SKILL.md` (절대 규칙 5)
- `docs/TOOLS.md`의 Codex 절 "스킬"(본문에 다른 스킬을 이름으로만 적어도 그 `SKILL.md`를 연다)과 Claude Code 절 "실행 스킬의 판정에서 본 것"(에이전트는 프로젝트 밖의 파일을 읽지 못한다)
- `git show ec2f192:docs/LESSONS.md`의 하네스의 문제점 절에서 (007-harness-issues, 검증 1)의 셋째 줄, (008-tdd, phase 1)의 넷째 줄, (008-tdd, phase 3)의 다섯째 줄, (008-tdd, phase 5)의 첫째 줄과, 미룬 문제 절의 (004-context-rules, 검증 1) 줄 (고칠 문제의 원문)

**TODO**
- [ ] retro와 verify의 4번에서 다른 스킬의 본문이 그 phase(verify는 작업)의 커밋이 바꾼 파일이거나 계획의 읽을 것이면 1번대로 읽는다 (`plugins/plate/skills/retro/SKILL.md`, `plugins/plate/skills/verify/SKILL.md`)
- [ ] retro 3번에서 머리의 결정이나 완료 조건이 바꾸기로 한 맥락 문서의 줄과 어긋나는 것은 문제로 적지 않는다 (`plugins/plate/skills/retro/SKILL.md`)
- [ ] 회고 방식의 회고 절과 검증 절의 "확인"에, 테스트 먼저가 "예"인 phase이면 그 기록을 본 줄(본 곳, 실패 출력과 통과 출력이 순서대로 있는지, 통과 | 실패)이 통과해도 적힌다. 양식과 적는 규칙이 이에 맞다 (`plugins/plate/skills/retro/SKILL.md`, `plugins/plate/skills/verify/SKILL.md`)
- [ ] context의 절대 규칙 5에 다른 스킬을 이름으로 불러 도구가 그 스킬의 본문을 여는 것은 예외라는 것이 있다 (`plugins/plate/skills/context/SKILL.md`)

**통과 조건**
- 완료 조건 5가 참이다.
  - 확인: 완료 조건 5의 확인을 돌린다
- 완료 조건 6이 참이다.
  - 확인: 완료 조건 6의 확인을 돌린다
