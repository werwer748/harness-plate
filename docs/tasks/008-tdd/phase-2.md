# Phase 2: plan 본문

**목표**: plan이 phase마다 테스트 먼저를 적고, 테스트 먼저인 phase가 있으면 엣지케이스를 논의할지 묻는다.

**읽을 것**
- `plugins/plate/skills/plan/SKILL.md` (5번, 계획 파일의 양식, 적는 규칙)

**TODO**
- [ ] phase 양식의 목표 바로 아래에 테스트 먼저 줄이 생겨 계획 항목이 다섯이 되고, 적는 규칙이 이를 따른다. "항목은 넷"이 본문에 남지 않는다 (`plugins/plate/skills/plan/SKILL.md`)
- [ ] 적는 규칙에 두 가지가 생긴다. 동작을 바꾸는 phase는 "예"다. "아니오"인 phase는 이유를 적고, 동작을 바꾸지 않는 phase(리팩터링)는 기존 테스트가 바꾼 뒤에도 모두 통과한다는 통과 조건을 둔다 (`plugins/plate/skills/plan/SKILL.md`)
- [ ] 5번에 엣지케이스 물음이 생긴다. 테스트 먼저인 phase가 있으면 논의할지 묻고, 후보를 먼저 내지 않는다. 논의하지 않으면 엣지케이스는 수행 에이전트가 정한다. 논의하면 후보를 선택지로 주거나 더할 케이스를 묻고, 고른 것은 그 phase의 TODO에 테스트로, 뺀 것은 범위 밖에 적는다 (`plugins/plate/skills/plan/SKILL.md`)

**통과 조건**
- 완료 조건 3이 참이다.
  - 확인: 완료 조건 3의 확인을 돌린다
