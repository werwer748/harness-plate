# Phase 1: check와 retro에 "남은 것"의 판정을 넣는다

**목표**: check와 retro의 본문이 "남은 것"을 판정하고, eval의 낱말이 그와 맞는다.

**테스트 먼저**: 아니오 — `.md`(스킬 본문)만 고친다

**읽을 것**
- `plugins/plate/skills/check/SKILL.md` (고칠 스킬. 절대 규칙 3, 1~5번, 확인 절의 양식, 적는 규칙)
- `plugins/plate/skills/retro/SKILL.md` (고칠 스킬. 4번의 "남은 것" 줄, 회고 절의 양식, 적는 규칙)
- `plugins/plate/skills/eval/SKILL.md` (낱말 `done-phase-N.md`와 `retro.md`)
- `plugins/plate/skills/phase/SKILL.md` (기록 양식의 "남은 것"과 적는 규칙. 읽기만 한다)
- `gh issue view 31` (#31의 본문)

**TODO**
- [x] check의 절차에 "남은 것"을 보는 단계가 더해진다. 동작의 결함이나 돌려 보지 않은 위험을 적은 줄이 통과 조건이 보는 동작에 걸리면 "실패"로, 걸리지 않으면 "하네스에서 걸린 것"으로 옮긴다. 판정 줄도 이 단계의 실패를 센다 (`plugins/plate/skills/check/SKILL.md`)
- [x] check의 절대 규칙 3이 판정에 넣는 것에 그 단계를 더하도록 바뀌고, frontmatter의 description, 확인 절의 양식, 적는 규칙이 그 단계와 맞게 바뀐다 (`plugins/plate/skills/check/SKILL.md`)
- [x] retro 4번의 "남은 것" 줄이 부작용과 한계에 더해 동작의 결함과 돌려 보지 않은 위험도 보고 줄마다 문제인지 판정하도록 바뀐다 (`plugins/plate/skills/retro/SKILL.md`)
- [x] retro의 회고 절 양식에 "남은 것"의 줄마다 판정(문제 | 문제 아님과 까닭)을 적는 항목이 더해지고, 적는 규칙이 그 항목을 적는다 (`plugins/plate/skills/retro/SKILL.md`)
- [x] eval의 낱말 `done-phase-N.md`와 `retro.md`가 바뀐 확인 절과 회고 절의 항목과 맞게 바뀐다. 바꿀 것이 없으면 그대로 둔다 (`plugins/plate/skills/eval/SKILL.md`)

**통과 조건**
- 완료 조건 1이 참이다.
  - 확인: `plugins/plate/skills/check/SKILL.md`의 frontmatter의 description, 절대 규칙 3, 절차, 확인 절의 양식, 적는 규칙을 하나씩 읽어, "남은 것"의 결함·위험 줄이 통과 조건이 보는 동작에 걸리면 실패, 아니면 "하네스에서 걸린 것"이라는 것이 서로 어긋나지 않게 적혀 있다. 절대 규칙 3이 이것을 판정에 넣는 것으로 들지 않으면 실패
- 완료 조건 2가 참이다.
  - 확인: `plugins/plate/skills/retro/SKILL.md`의 4번, 회고 절의 양식, 적는 규칙을 하나씩 읽어, 부작용과 한계, 동작의 결함, 돌려 보지 않은 위험을 모아 줄마다 판정해 회고 절에 적는다는 것이 있다. 하나라도 빠지면 실패
- 완료 조건 3이 참이다.
  - 확인: `plugins/plate/skills/eval/SKILL.md`의 낱말 `done-phase-N.md`와 `retro.md`를 읽어 바뀐 두 절의 항목과 어긋나지 않는다

## 한 일
- check의 절차에 "남은 것"을 보는 단계가 더해진다: 5번 `기록의 "남은 것"을 본다`를 새로 두고, 결함·위험 줄이 통과 조건이 보는 동작에 걸리면 "실패", 걸리지 않으면 "하네스에서 걸린 것"으로 옮기게 했다. 뒤의 절 번호를 6~8번으로 밀고 판정 줄을 "2~5번"으로 바꿨다 (`plugins/plate/skills/check/SKILL.md`)
- check의 절대 규칙 3, description, 확인 절의 양식, 적는 규칙: 절대 규칙 3의 판정에 넣는 것에 "남은 것"의 결함·위험 줄 가운데 통과 조건이 보는 동작에 걸리는 줄을 더하고, description과 머리글에 그 단계를 적고, 양식에 "**남은 것**" 항목(테스트 먼저 기록과 실패 사이)을, 적는 규칙에 "남은 것" 항목의 줄, "실패"의 범위 "2~5번", 걸리지 않은 줄을 "하네스에서 걸린 것"에 "남은 것: …"으로 옮기는 줄을 더했다 (`plugins/plate/skills/check/SKILL.md`)
- retro 4번의 "남은 것" 줄: 부작용과 한계, 동작의 결함, 돌려 보지 않은 위험을 모두 모아 줄마다 넷에 대어 문제인지 판정하고, 판정을 회고 절의 "남은 것"에, 문제면 "문제"에도 적게 바꿨다 (`plugins/plate/skills/retro/SKILL.md`)
- retro 회고 절 양식과 적는 규칙: 양식의 "확인"과 "문제" 사이에 "**남은 것**" 항목(`phase {번호}: {줄} → {문제 | 문제 아님} ({까닭})`)을 더하고, 적는 규칙에 그 항목을 적는 줄을 더했다 (`plugins/plate/skills/retro/SKILL.md`)
- eval의 낱말: `done-phase-N.md`의 확인 절 항목에 "남은 것"을, `retro.md`의 회고 절 항목에 "남은 것"을 더했다 (`plugins/plate/skills/eval/SKILL.md`)

## 확인 결과
- 완료 조건 1이 참이다.
  - `plugins/plate/skills/check/SKILL.md`의 description(3줄), 절대 규칙 3(18줄), 5번(54~61줄), 판정(67줄), 확인 절 양식의 "남은 것"(104~105줄), 적는 규칙(122~126줄)을 읽음 → 모두 "결함·위험 줄이 통과 조건이 보는 동작에 걸리면 실패, 아니면 하네스에서 걸린 것"으로 같게 적혀 있고, 절대 규칙 3이 이 줄을 판정에 넣는 것으로 든다. 통과
- 완료 조건 2가 참이다.
  - `plugins/plate/skills/retro/SKILL.md`의 4번(77줄), 회고 절 양식의 "남은 것"(144~145줄), 적는 규칙(167줄)을 읽음 → 부작용과 한계, 동작의 결함, 돌려 보지 않은 위험을 모아 줄마다 판정(문제 | 문제 아님과 까닭)해 회고 절의 "남은 것"에 적는다는 것이 셋 모두에 있다. 통과
- 완료 조건 3이 참이다.
  - `plugins/plate/skills/eval/SKILL.md`의 낱말 `done-phase-N.md`(29줄)와 `retro.md`(30줄)를 읽음 → 확인 절은 "남은 것", "실패", "하네스에서 걸린 것", "판정", 회고 절은 "확인", "남은 것", "문제", "판정"으로 바뀐 두 양식의 항목과 어긋나지 않는다. 통과

## 계획과 달라진 점
없음

## 남은 것
- check의 5번을 넣으며 뒤 절 번호가 6~8번으로 밀렸다. 이 스킬 밖에서 check의 절 번호를 가리키는 곳은 `plugins/plate`에서 찾지 못했지만, run 스킬처럼 다른 스킬 본문은 이 phase에서 읽지 않았다
- retro 4번에 "돌려 보지 않은 위험은 그 동작을 task의 커밋이 바꾼 것에서 직접 읽거나 돌려 보고 판정한다"는 줄을 더했다. TODO가 적지 않은 판정 방법이라 회고가 이 줄을 계획보다 넓다고 볼 수 있다
- 바뀐 스킬은 에이전트가 기록을 읽고 판정하는 스킬이라 헤드리스로 돌려 보지 않았다(task 머리의 완료 조건 1, 2의 "돌리지 않음")

## 하네스에서 걸린 것
없음
