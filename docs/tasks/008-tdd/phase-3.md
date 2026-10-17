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
- [x] phase: 테스트 먼저 "예"인 phase는 실패하는 테스트를 먼저 쓰고 돌려 실패 출력을 기록에 남긴 뒤 구현하고, 통과 출력을 남긴다 (`plugins/plate/skills/phase/SKILL.md`)
- [x] phase: 훅이 세 번째 막았다고 알리면 더 시도하지 않고 막힘으로 멈추고, 막힌 까닭과 원하는 해결책을 "남은 것"과 "하네스에서 걸린 것"에 적는다 (`plugins/plate/skills/phase/SKILL.md`)
- [x] retro와 verify의 3번이 테스트 먼저 "예"인 phase의 기록에 실패 출력과 통과 출력이 있는지 보고, 없으면 문제로 적는다(기준: 계획) (`plugins/plate/skills/retro/SKILL.md`, `plugins/plate/skills/verify/SKILL.md`)
- [x] run: 막힘이 훅의 세 번 막힘 때문이면 정해 둔 선택지 대신 막힌 까닭과 수행 에이전트의 해결책을 보여 주고 논의한다. 합의한 해결책이 계획을 바꾸는 것이면 안을 보여 주고 승인받아 계획 파일에 반영한 뒤 새 에이전트에게 맡기고, 아니면 멈춘다 (`plugins/plate/skills/run/SKILL.md`)
- [x] phase, retro, run 본문이 계획 다섯 항목에 맞고, run의 고칠 phase 양식에 테스트 먼저 줄이 생긴다 (`plugins/plate/skills/phase/SKILL.md`, `plugins/plate/skills/retro/SKILL.md`, `plugins/plate/skills/run/SKILL.md`)

**통과 조건**
- 완료 조건 4, 5, 6이 참이다.
  - 확인: 완료 조건 4, 5, 6의 확인을 모두 돌린다

## 한 일
- phase: 테스트 먼저 "예"인 phase는 실패하는 테스트를 먼저 쓰고 돌려 실패 출력을 기록에 남긴 뒤 구현하고, 통과 출력을 남긴다: 2번에 테스트 먼저 "예"이면 테스트 파일이 아닌 코드를 고치기 전에 테스트를 쓰고 돌려 실패를 보고, 구현 뒤 통과를 보는 세 단계가 생겼다. 두 출력은 "한 일"의 테스트 먼저 항목(실패 줄, 통과 줄 순서)에 적고, 이어 하거나 고칠 때 그 줄은 지우지 않는다(양식, 적는 규칙, 4번) (`plugins/plate/skills/phase/SKILL.md`)
- phase: 훅이 세 번째 막았다고 알리면 더 시도하지 않고 막힘으로 멈추고, 막힌 까닭과 원하는 해결책을 "남은 것"과 "하네스에서 걸린 것"에 적는다: 2번에 그 규칙이 생겼고, 적는 규칙에서 그 줄을 "훅이 테스트 먼저 때문에 세 번째 막음:"으로 시작해 막힌 파일, 까닭, 해결책을 적게 했다. run이 이 줄로 알아본다 (`plugins/plate/skills/phase/SKILL.md`)
- retro와 verify의 3번이 테스트 먼저 "예"인 phase의 기록에 실패 출력과 통과 출력이 있는지 보고, 없으면 문제로 적는다(기준: 계획): 두 3번에 그 점검이 생겼고, verify는 지우기 전의 마지막 `phase-N.md`(지운 커밋의 부모, 아니면 `done-phase-N.md`)를 본다. 두 적는 규칙의 "계획" 기준에 테스트 먼저를 더했다 (`plugins/plate/skills/retro/SKILL.md`, `plugins/plate/skills/verify/SKILL.md`)
- run: 막힘이 훅의 세 번 막힘 때문이면 정해 둔 선택지 대신 막힌 까닭과 수행 에이전트의 해결책을 보여 주고 논의한다. 합의한 해결책이 계획을 바꾸는 것이면 안을 보여 주고 승인받아 계획 파일에 반영한 뒤 새 에이전트에게 맡기고, 아니면 멈춘다: 3번의 "막힘"이 둘로 갈렸다. "남은 것"에 "훅이 테스트 먼저 때문에 세 번째 막음:" 줄이 있으면 논의하고, 계획을 바꾸면 안을 승인받아 "계획을 고친다"의 3번대로 고친 뒤 새 에이전트에게 맡기고, 아니면 8번으로 간다. 그 밖의 막힘은 전과 같다 (`plugins/plate/skills/run/SKILL.md`)
- phase, retro, run 본문이 계획 다섯 항목에 맞고, run의 고칠 phase 양식에 테스트 먼저 줄이 생긴다: 세 본문의 "계획 네 항목"을 "다섯 항목(목표, 테스트 먼저, 읽을 것, TODO, 통과 조건)"으로 바꿨다. run의 고칠 phase 양식의 목표 아래에 `**테스트 먼저**: {예, 또는 아니오 — 이유}` 줄이 생기고, 1번에 동작을 바꾸는 문제가 있으면 "예"라는 규칙이 생겼다 (`plugins/plate/skills/phase/SKILL.md`, `plugins/plate/skills/retro/SKILL.md`, `plugins/plate/skills/run/SKILL.md`)

## 확인 결과
- 완료 조건 4, 5, 6이 참이다.
  - 완료 조건 4: `plugins/plate/skills/phase/SKILL.md`를 읽음 → 2번에 테스트 먼저 "예"이면 테스트를 먼저 쓰고 돌려 실패를 보고, 구현 뒤 통과를 보며, 두 명령과 출력을 "한 일"에 적는 규칙이 있다. 2번에 훅이 세 번째 막았다고 알리면 더 시도하지 않고 막힘으로 4번에 가서 까닭과 해결책을 "남은 것"과 "하네스에서 걸린 것"에 적는 규칙이 있다. 통과
  - 완료 조건 5: `plugins/plate/skills/retro/SKILL.md`와 `plugins/plate/skills/verify/SKILL.md`의 3번을 읽음 → 두 곳 모두 테스트 먼저 "예"인 phase의 기록에 실패 출력과 통과 출력이 이 순서로 있는지 보고 없으면 기준 "계획"의 문제로 적는 줄이 있다. 통과
  - 완료 조건 6: `grep -rn '네 항목\|항목은 넷' plugins/plate/skills` → 출력 없음(종료 코드 1). 통과
  - 완료 조건 6: `plugins/plate/skills/run/SKILL.md`의 3번과 "고칠 phase를 더한다"를 읽음 → 3번에 훅의 세 번째 막음이면 선택지 대신 까닭과 해결책을 보여 주고 논의하며, 계획을 바꾸면 안을 승인받아 고친 뒤 새 에이전트에게 맡기고 아니면 멈추는 규칙이 있다. 고칠 phase 양식의 목표 아래에 `**테스트 먼저**: {예, 또는 아니오 — 이유}` 줄이 있다. 통과

## 계획과 달라진 점
- 없음

## 남은 것
- 없음

## 하네스에서 걸린 것
- 계획의 결정("세 번은 같은 phase의 계획(기록 절 위의 항목)이 바뀌지 않은 동안 센다")과 run의 "계획을 고친다" 3번: 훅의 세 번째 막음 뒤 합의한 해결책이 `plan.md`만 고치면 `phase-N.md`의 계획 줄이 그대로라 훅의 횟수가 이어져, 새 에이전트가 처음 막힐 때 바로 세 번째 막음 알림을 받는다. 이 phase에서 고칠 일은 아니라 그대로 두었다
- plan 스킬의 적는 규칙("동작을 바꾸는 phase는 '예'다")은 테스트가 없는 프로젝트에도 걸려, 머리의 목표("테스트가 있는 프로젝트에서")보다 넓다. phase 스킬의 테스트 먼저 규칙은 표시만 보므로, 테스트가 없는 프로젝트의 "예"인 phase에서 TODO에 없는 테스트 틀을 세우게 할 수 있다
