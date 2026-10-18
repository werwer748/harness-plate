# Phase 3: phase를 task 구조에 맞추고 check를 만든다

**목표**: 수행 에이전트가 task 머리와 자기 phase 파일로 수행하고, 새 check 스킬이 phase 하나를 따로 확인해 판정을 그 phase 파일에 남긴다.

**테스트 먼저**: 아니오 — `.md`만 고치고 만든다.

**읽을 것**
- `plugins/plate/skills/phase/SKILL.md` (지금의 수행 절차, 기록 다섯 절의 양식, 막힘과 계획이 틀림)
- `plugins/plate/skills/retro/SKILL.md` (지금의 "확인만" 방식과 회고 절의 양식. check가 이 확인을 이어받는다)
- `plugins/plate/skills/plan/SKILL.md` (phase 1이 바꾼 tasks 구조, task 머리 양식, 명령 절 규칙)
- `docs/ARCHITECTURE.md` (스킬 본문을 쓰는 규칙)

**TODO**
- [ ] phase의 낱말이 task 폴더, task 머리, phase로 바뀌고, 읽는 것이 task 머리와 넘겨받은 `phase-N.md`다 (`plugins/plate/skills/phase/SKILL.md`)
- [ ] phase가 넘겨받는 "고칠 문제"가 그 `phase-N.md`의 마지막 확인 절에 적힌 실패로 바뀌고, 회고 절을 가리키는 글이 없어진다
- [ ] check 스킬이 생긴다: task 폴더와 phase 번호를 받아 그 phase의 통과 조건 확인과 `docs/ARCHITECTURE.md` 명령 절의 빌드·린트·테스트를 직접 돌린다. 없는 명령은 "없음"으로 적는다. 테스트 먼저가 "예"이면 기록에 실패 출력과 통과 출력이 이 순서로 있는지 본다 (`plugins/plate/skills/check/SKILL.md`)
- [ ] check가 `phase-N.md` 끝에 확인 절(몇 번째인지, 확인마다 돌린 명령과 결과, 판정 통과 또는 실패)을 더하고 그 파일만 `NNN-slug: phase N 확인`으로 커밋한다. 고치지 않고 묻지 않으며, 판정과 실패 수와 기록 위치를 정해 둔 줄로 돌려준다
- [ ] 두 스킬의 description이 새 동작을 말한다

**통과 조건**
- 두 본문이 TODO대로다
  - 확인: 두 `SKILL.md`를 읽어 TODO 항목마다 그 동작이 적힌 곳을 찾는다
- phase 본문이 회고 절을 가리키지 않는다
  - 확인: `grep -n "회고" plugins/plate/skills/phase/SKILL.md` → 0줄
- 완료 조건 2 가운데 두 본문의 몫이 참이다
  - 확인: `grep -n "작업" plugins/plate/skills/phase/SKILL.md plugins/plate/skills/check/SKILL.md`의 줄을 모두 읽어 tasks, task, phase를 가리키는 "작업"이 없다
