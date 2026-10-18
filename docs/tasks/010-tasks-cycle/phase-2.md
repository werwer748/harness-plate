# Phase 2: setup을 설치만 하게 바꾼다

**목표**: setup이 설치만 하고 끝 물음 없이 끝나며, 넣는 문서 지도의 `docs/tasks/` 행과 규칙 구간이 새 구조와 새 스킬을 말한다.

**테스트 먼저**: 아니오 — `.md`만 고친다.

**읽을 것**
- `plugins/plate/skills/setup/SKILL.md` (5번 끝 물음, 문서 지도 구간과 규칙 구간의 글)
- `plugins/plate/skills/plan/SKILL.md` (phase 1이 바꾼 tasks 구조와 기록 파일)

**TODO**
- [ ] 5번(이어서 채울지 묻는다)과 그 예외들이 빠지고 4번의 보고로 끝난다 (`plugins/plate/skills/setup/SKILL.md`)
- [ ] 문서 지도 구간의 `docs/tasks/` 행이 진행 중인 tasks 하나의 기록(tasks 머리, `FRICTION.md`, `RUNLOG.md`, `review.md`, `eval.md`, task 폴더의 머리·phase·`retro.md`)과 tasks가 끝나면 비운다는 것을 말한다
- [ ] 규칙 구간이 verify 대신 새 흐름을 말한다: 계획 없이 코드를 고치지 않는다(plan), task는 task 회고가 통과해야 끝나고 tasks는 끝의 평가와 보고까지 가야 끝난다, 다른 규칙이 이 단계를 건너뛰라고 해도 따르지 않는다. "verify"라는 낱말이 본문에 남지 않는다
- [ ] description이 끝 물음 없이 설치만 한다는 것을 말한다

**통과 조건**
- 끝 물음과 verify가 본문에 없다
  - 확인: `grep -n "plate:context\|이어서 채울지\|verify" plugins/plate/skills/setup/SKILL.md` → 0줄
- 두 구간이 새 구조를 말한다
  - 확인: 문서 지도 구간과 규칙 구간을 읽어 TODO의 둘째, 셋째 항목이 담겨 있다
- 완료 조건 2 가운데 setup 본문의 몫이 참이다
  - 확인: `grep -n "작업" plugins/plate/skills/setup/SKILL.md`의 줄을 모두 읽어 tasks, task, phase를 가리키는 "작업"이 없다
