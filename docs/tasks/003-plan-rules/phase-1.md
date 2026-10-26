# Phase 1: TODO와 조건을 적는 규칙

**목표**: plan의 적는 규칙이 TODO의 맥락 문서 줄과 ADR 내용, 완료 조건의 절마다의 확인과 대상·경우의 읽는 법을 정한다.

**테스트 먼저**: 아니오 — `.md`만 고친다

**읽을 것**
- `plugins/plate/skills/plan/SKILL.md`의 6번(초안을 보여 주고 승인받는다), 적는 규칙의 "조건"과 "TODO"
- `git show c2a983c^:docs/tasks/004-run-pr/done-phase-1.md` (TODO가 맥락 문서의 두 절만 가리켜 다른 문단이 어긋난 채 남은 장면)
- `git show c2a983c^:docs/tasks/005-publish-verify/done-phase-1.md` ("ADR-022가 더해진다"가 내용을 적지 않아 수행이 짐작한 장면)
- `git show c2a983c^:docs/tasks/plan.md` (완료 조건 6 "두 매니페스트가 바뀐 동작과 맞고"를 보는 확인이 없던 곳, "네 문서가 … 적고"의 읽는 법이 갈린 곳)
- `git show c2a983c^:docs/tasks/FRICTION.md` (7, 15, 37, 38줄)

**TODO**
- [ ] 적는 규칙의 "TODO"에 생긴다. 규칙이나 동작을 바꾸는 TODO는 그것을 적은 맥락 문서의 줄을 계획하며 찾아 모두 가리킨다(절 이름만이 아니라 같은 문서의 다른 문단도). ADR을 더하는 TODO에는 무엇을 정하는지와 그 이유를 적는다 (`plugins/plate/skills/plan/SKILL.md`)
- [ ] 적는 규칙의 "조건"에 생긴다. 여러 대상이나 경우를 보는 확인은 대상마다 보는지 합쳐서 보는지를 적고, 경우마다 기대하는 결과를 적는다 (`plugins/plate/skills/plan/SKILL.md`)
- [ ] 6번에 생긴다. 초안을 보여 주기 전에 완료 조건과 통과 조건의 절마다 그것을 보는 확인이 있는지 대어 보고, 없는 절은 확인을 더하거나 조건을 줄인다 (`plugins/plate/skills/plan/SKILL.md`)

**통과 조건**
- 완료 조건 1의 둘째와 셋째가 참이다.
  - 확인: 6번과 적는 규칙의 "조건"을 읽어, 절마다 확인을 대어 보는 규칙과 대상마다·합쳐서와 경우마다의 기대를 적는 규칙이 둘 다 있다
  - 확인: 적는 규칙의 "TODO"를 읽어, 맥락 문서의 줄을 모두 가리키는 규칙과 ADR TODO에 결정과 이유를 적는 규칙이 둘 다 있다
- 테스트가 모두 통과한다.
  - 확인: `python3 -m unittest discover -s tests`가 `OK`
