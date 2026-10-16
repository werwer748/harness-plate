# Phase 3: phase, retro, verify, run 본문

**목표**: 수행은 테스트 먼저 순서로 하고 기록하며, 회고와 검증은 그 기록을 보고, run은 다섯 항목과 훅의 세 번 막힘을 다룬다.

**읽을 것**
- `plugins/plate/skills/plan/SKILL.md` (phase 2가 바꾼 phase 양식: 테스트 먼저 줄의 꼴)
- `plugins/plate/skills/phase/SKILL.md`
- `plugins/plate/skills/retro/SKILL.md` (3번, 낱말, 1번, 5번)
- `plugins/plate/skills/verify/SKILL.md` (3번)
- `plugins/plate/skills/run/SKILL.md` (절대 규칙 4, 낱말, 3번의 "막힘", "계획을 고친다", "고칠 phase를 더한다")
- `plugins/plate/hooks/` (phase 1의 훅이 세 번째에 알리는 글)

**TODO**
- [ ] phase: 테스트 먼저 "예"인 phase는 실패하는 테스트를 먼저 쓰고 돌려 실패 출력을 기록에 남긴 뒤 구현하고, 통과 출력을 남긴다 (`plugins/plate/skills/phase/SKILL.md`)
- [ ] phase: 훅이 세 번째 막았다고 알리면 더 시도하지 않고 막힘으로 멈추고, 막힌 까닭과 원하는 해결책을 "남은 것"과 "하네스에서 걸린 것"에 적는다 (`plugins/plate/skills/phase/SKILL.md`)
- [ ] retro와 verify의 3번이 테스트 먼저 "예"인 phase의 기록에 실패 출력과 통과 출력이 있는지 보고, 없으면 문제로 적는다(기준: 계획) (`plugins/plate/skills/retro/SKILL.md`, `plugins/plate/skills/verify/SKILL.md`)
- [ ] run: 막힘이 훅의 세 번 막힘 때문이면 정해 둔 선택지 대신 막힌 까닭과 수행 에이전트의 해결책을 보여 주고 논의한다. 합의한 해결책이 계획을 바꾸는 것이면 안을 보여 주고 승인받아 계획 파일에 반영한 뒤 새 에이전트에게 맡기고, 아니면 멈춘다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] phase, retro, run 본문이 계획 다섯 항목에 맞고, run의 고칠 phase 양식에 테스트 먼저 줄이 생긴다 (`plugins/plate/skills/phase/SKILL.md`, `plugins/plate/skills/retro/SKILL.md`, `plugins/plate/skills/run/SKILL.md`)

**통과 조건**
- 완료 조건 4, 5, 6이 참이다.
  - 확인: 완료 조건 4, 5, 6의 확인을 모두 돌린다
