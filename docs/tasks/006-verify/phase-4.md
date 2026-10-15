# Phase 4: plan과 setup

**목표**: plan이 테스트가 있는 프로젝트의 완료 조건에 전체 테스트를 넣고, setup이 `AGENTS.md`에 규칙 구간을 넣는다.

**읽을 것**
- `plugins/plate/skills/plan/SKILL.md` (적는 규칙의 조건)
- `plugins/plate/skills/setup/SKILL.md` (문서 지도 구간과 표식, 다시 돌릴 때의 규칙)
- `~/plate-rail-test/bin/plancheck.py`, `~/plate-rail-test/bin/setupcheck.py`
- `~/plate-rail-test/run-all/` (plan-test의 시작 상태), `~/plate-rail-test/setup-fresh/`, `~/plate-rail-test/setup-remap/`, `~/plate-rail-test/answers/setup-*.md`

**TODO**
- [ ] plan이 테스트가 있는 프로젝트이면 완료 조건에 프로젝트 전체 테스트를 돌리는 조건을 넣는다 (`plugins/plate/skills/plan/SKILL.md`)
- [ ] setup이 `AGENTS.md`의 문서 지도 구간 뒤에 표식으로 감싼 규칙 구간을 넣는다. 규칙은 코드를 고치는 요청은 계획부터 하고 작업은 검증이 통과해야 끝난다는 것이다. 다시 돌리면 지도 구간처럼 표준 글만 맞추고, 구간이 없는 셋업된 프로젝트에서는 더하는 행을 표에 보여 주고 승인받는다 (`plugins/plate/skills/setup/SKILL.md`)
- [ ] `plancheck.py`가 `plan-test`를 판정하고 `setupcheck.py`가 규칙 구간을 본다 (`~/plate-rail-test/bin/`)
- [ ] 경우들을 헤드리스로 돌려 통과한다

**통과 조건**
- 완료 조건 12, 13이 참이다.
  - 확인: 완료 조건 12, 13의 확인을 돌린다
