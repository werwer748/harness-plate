# FRICTION

- `001-issue-criteria` 문제: plate:plan이 phase 4의 통과 조건 "시험이 이 저장소를 바꾸지 않았다"를 `git status --porcelain -- . ':!docs/tasks/001-issue-criteria/phase-4.md'`로 적어, plate:run이 수행 뒤 확인 전에 `docs/tasks/RUNLOG.md`에 줄을 더하는 것을 빼지 않았다. 그대로면 시험과 상관없이 확인이 실패할 것이라 실행 중 고칠 phase 물음으로 계획을 고쳤다(`47c67c2 plan: 001-issue-criteria 수정`, `docs/tasks/RUNLOG.md`의 물음 줄). 저장소 불변을 보는 확인을 쓸 때 실행이 그 사이에 쓰는 하네스 기록을 빼라는 것이 계획의 초안 점검에 없다
- `002-plan-branch` 문제: plate:plan의 초안 점검이 새 브랜치 규칙의 갈래를 "지금 브랜치가 무엇인가"로만 나눠, 새 tasks의 `<이름>`이 6번에서야 정해지는데 1번에서 지금 브랜치가 `tasks/<이름>`인지 가르게 한 순서의 어긋남을 잡지 못했다. 그 결과 다른 tasks의 브랜치(`tasks/old`)에서 새 tasks를 계획하는 장면이 1번과 7번 어디에도 들지 않는다(`plugins/plate/skills/plan/SKILL.md` 54줄, 137줄). 완료 조건 1의 확인은 글이 있는지(grep, 테스트의 `assertIn`)만 보고, 헤드리스 시험은 결정대로 두 장면만 돌려 이 장면은 phase 확인에서 걸리지 않았다
