# Phase 4: run의 옮김 기준, worktree 갈래, 고칠 phase 양식

**목표**: run이 LESSONS로 옮겼는지를 `verify.md`의 줄로 가리고, 원래 자리에서 worktree에 쓰지 않고, 고칠 phase가 문제마다의 확인과 맥락 문서를 갖는다.

**테스트 먼저**: 아니오 — 스킬 본문(`.md`)만 고친다

**읽을 것**
- `plugins/plate/skills/run/SKILL.md` (절대 규칙 5, 0번, "검증을 맡긴다"의 "통과하면"과 "고칠 phase를 더한다", "합친다", "`docs/LESSONS.md`" 절)
- `plugins/plate/skills/plan/SKILL.md`의 적는 규칙의 테스트 먼저 (phase 2가 바꾼 "예"의 기준)
- `docs/TOOLS.md`의 Claude Code 절 "실행 스킬의 판정에서 본 것"(원래 자리의 세션은 worktree 안의 git을 돌리지 못한다)과 "서브에이전트, 권한, worktree"
- `git show ec2f192:docs/LESSONS.md`의 하네스의 문제점 절에서 (007-harness-issues, phase 4)의 네 줄, (008-tdd, phase 3)의 둘째 줄과, 프로젝트에서 배운 것 절의 (007-harness-issues, phase 4) 첫째 줄 (고칠 문제의 원문)

**TODO**
- [ ] "통과하면" 1번이 옮긴 뒤 `verify.md`의 마지막 검증 절 아래에 `LESSONS로 옮겼다`를 적는다. 옮길 줄이 없거나 모두 겹쳐도 적는다. 절대 규칙 5의 직접 고치는 파일과 "통과하면" 3번의 커밋에 그 줄이 든다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] "`docs/LESSONS.md`" 절에서 이 작업의 검증 절의 줄을 옮겼는지는 그 줄이 있는지로 본다. git 레포가 아니어도 같다. `git log -S`의 기준과 `done-phase-N.md`로 보는 기준이 없고, 문서 지도 절에서 다른 위치로 읽는 곳의 목록이 이에 맞다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] 0번의 worktree 갈래에서 원래 자리는 worktree 안의 파일을 고치거나 커밋하지 않는다. worktree의 `verify.md`에 그 줄이 있으면 "합친다"로 가고, 닫힌 검증인데 그 줄이 없으면 그 worktree에서 세션을 열어 이 스킬을 부르라고 안내하고 끝난다. "합친다"의 0번에서 오는 갈래도 이에 맞다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] 고칠 phase 양식에서 테스트 먼저는 plan 적는 규칙과 같은 기준이고, 읽을 것에 문서 지도의 맥락 문서가 있고, 통과 조건에 검증 K의 문제가 모두 고쳐졌다는 조건(확인: 문제마다 적힌 곳을 다시 읽거나 돌린다)이 머리의 완료 조건과 함께 있다 (`plugins/plate/skills/run/SKILL.md`)

**통과 조건**
- 완료 조건 7이 참이다.
  - 확인: 완료 조건 7의 확인을 모두 돌린다
