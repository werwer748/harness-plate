# Phase 4: 검증 1의 문제를 고친다

**목표**: 검증 1에서 나온 문제를 모두 고친다.

**읽을 것**
- `docs/tasks/007-harness-issues/verify.md`의 `## 검증 1` 절
- `plugins/plate/skills/run/SKILL.md`

**TODO**
- [ ] run 본문 0번의 worktree 갈래는 원래 자리에서 부르면 worktree 안의 작업 폴더에 닫힌 검증이 있을 때 바로 "합친다"로 가고, "합친다"는 `docs/LESSONS.md`로 옮기지 않는다. worktree의 세션에서 검증 에이전트가 `verify.md`를 커밋한 뒤 run이 "통과하면"의 1~3을 하기 전에 끊기고 원래 자리에서 `/plate:run NNN`을 부르면, 검증 절의 줄을 옮기지 않은 채 합치고 worktree와 브랜치를 지운다. 머리의 목표 "run이 닫힌 검증을 다시 만나도 LESSONS로 옮기기를 건너뛰지 않는다"가 이 갈래에서는 이뤄지지 않았다 (`plugins/plate/skills/run/SKILL.md` 49~51행)
- [ ] run 본문 "검증을 맡긴다"의 첫 갈래는 앞 세션이 1~3을 이미 했어도 "통과하면"의 1번부터 다시 옮기고, 이미 옮긴 줄인지는 `docs/LESSONS.md`의 같은 절에 같은 뜻의 줄이 있는지로만 가린다(247행). 그래서 옮긴 뒤 LESSONS에서 지운 줄은 다시 더해진다. 이 레포에서 지금 `/plate:run 006`을 부르면 이 작업이 완료 조건 7로 지운 `(006-verify, 검증 1)` 하네스의 문제점 세 줄과, 이 작업이 고친 첫 갈래의 결함을 적은 미룬 문제 한 줄이 LESSONS에 돌아오고, `/plate:run 004`를 부르면 `(004-context-rules, 검증 1)` 하네스의 문제점 세 줄이 돌아온다. 같은 162행의 "이미 옮긴 줄은 다시 더하지 않고"와 어긋난다 (`plugins/plate/skills/run/SKILL.md` 162행, 247행)

**통과 조건**
- 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다
