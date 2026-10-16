# Phase 1: verify, retro, plan의 규칙

**목표**: 검증과 회고는 직접 본 것만 하네스의 문제점으로 적고, 검증은 다른 작업의 커밋에서 이 작업 폴더의 변경을 보며, 계획은 낡은 결과와 앞 phase가 이룬 조건을 놓치지 않게 확인을 적는다.

**읽을 것**
- `docs/LESSONS.md` (하네스의 문제점 절의 `(006-verify, phase 1)`, `(006-verify, phase 2)`의 첫째~셋째, `(004-context-rules, 검증 1)`의 첫째·둘째, `(006-verify, 검증 1)`의 첫째. 이 phase가 고치는 일곱 줄)
- `plugins/plate/skills/verify/SKILL.md` (낱말 "작업의 커밋", 1번, 3번, 4번)
- `plugins/plate/skills/retro/SKILL.md` (4번)
- `plugins/plate/skills/plan/SKILL.md` ("적는 규칙"의 조건과 phase를 나누는 기준)
- `git show a4f21d7:docs/tasks/006-verify/phase-1.md` ("한 일"의 첫 줄: 다른 작업의 커밋을 빼는 규칙은 `005-run: phase 8`이 004의 `plan.md`를 고친 일 때문에 넣었다)
- `docs/tasks/004-context-rules/verify.md` (검증 1의 하네스의 문제점: 남은 결과를 읽는 확인, `9b0dfb6`이 점검에서 빠진 일)
- `docs/tasks/006-verify/verify.md` (검증 1의 하네스의 문제점 첫째: phase 5의 통과 조건)
- `docs/TOOLS.md` ("실행 스킬의 판정에서 본 것"의 "에이전트는 프로젝트 폴더 밖의 파일을 읽지 못한다", "5단계의 판정에서 본 것")

**TODO**
- [ ] verify 4번에 하네스의 문제점은 이번 검증에서 직접 읽거나 돌려서 본 것만 적는다는 규칙이 생긴다. 다른 스킬의 본문은 열지 않고 이름으로만 가리키며, 읽지 않은 파일과 이 스킬 밖의 하네스 동작은 짐작해 적지 않는다 (`plugins/plate/skills/verify/SKILL.md`)
- [ ] retro 4번에 같은 규칙이 생긴다 (`plugins/plate/skills/retro/SKILL.md`)
- [ ] verify의 "작업의 커밋"이 바뀐다. 수행·회고·통과·검증의 커밋은 작업 폴더의 파일을 함께 바꾸므로 메시지의 꼴과 관계없이 들고, 메시지가 다른 작업 폴더의 이름으로 시작하는 커밋은 빼지 않되 그 커밋에서는 이 작업 폴더의 변경만 본다. 1번과 3번이 이 정의대로 읽는다 (`plugins/plate/skills/verify/SKILL.md`)
- [ ] plan "적는 규칙"에 남은 결과를 읽는 확인의 규칙이 생긴다. 그런 확인에는 그 결과를 만든 뒤에 그 결과에 걸리는 파일이 바뀌지 않았는지 보는 명령을 함께 적는다 (`plugins/plate/skills/plan/SKILL.md`)
- [ ] plan "적는 규칙"에, 앞 phase가 이룬 완료 조건에 걸리는 파일을 뒤 phase가 고치면 뒤 phase의 통과 조건이 그 완료 조건도 번호로 가리킨다는 규칙이 생긴다 (`plugins/plate/skills/plan/SKILL.md`)

**통과 조건**
- 완료 조건 1, 2, 3이 참이다.
  - 확인: 완료 조건 1, 2, 3의 확인을 모두 돌린다
