# Phase 1: retro의 고칠 쪽, 경계, 남은 것

**목표**: retro가 어긋남의 고칠 쪽을 적고, 경계 밖의 꼴을 `FRICTION.md`의 `경계 밖` 줄로 돌리고, `done-phase-N.md`의 "남은 것"을 점검에 대어 본다.

**테스트 먼저**: 아니오 — `.md`만 고친다

**읽을 것**
- `plugins/plate/skills/retro/SKILL.md` 전체
- `plugins/plate/skills/eval/SKILL.md`의 낱말 "`FRICTION.md`"와 `FRICTION.md`의 줄을 읽는 곳
- `git show c2a983c^:docs/tasks/003-push-guard/retro.md` (회고 1~6이 시험 밖 꼴을 결함으로 찾은 곳, 회고 5가 "한 일"의 부작용을 늦게 찾은 곳)
- `git show c2a983c^:docs/tasks/002-ci-workflow/retro.md` (고칠 쪽을 적지 않아 같은 예외를 두 번 오간 곳)
- `git show c2a983c^:docs/tasks/FRICTION.md` (11, 13, 19, 21, 23, 24, 26, 33줄)
- `docs/ARCHITECTURE.md`의 푸시 훅 문단 (맥락 문서가 약속하는 꼴의 경계를 정한 예)

**TODO**
- [ ] 4번에 생긴다. 문서와 코드(또는 계획과 코드)의 어긋남을 문제로 적을 때, task 머리와 tasks 머리의 목표와 결정에 비춰 어느 쪽을 고칠지와 그 근거를 적는다. 목표와 결정으로 가를 수 없으면 "고칠 쪽: 정하지 못함"과 까닭을 적는다 (`plugins/plate/skills/retro/SKILL.md`)
- [ ] 회고 절 양식의 "문제" 줄에 `고칠 쪽: {문서 | 코드 | 정하지 못함}`을 더하고, 적는 규칙에 어긋남이 아닌 문제에서는 이 칸을 적지 않는다고 적는다 (`plugins/plate/skills/retro/SKILL.md`)
- [ ] 4번에 생긴다. tasks 머리나 task 머리의 결정, 맥락 문서가 약속하는 꼴의 경계를 정했으면 "결함"은 그 경계 안에서만 찾는다. 경계 밖에서 찾은 꼴은 문제로 적지 않고 5번에서 `경계 밖`으로 모은다 (`plugins/plate/skills/retro/SKILL.md`)
- [ ] 5번의 갈래에 `경계 밖`(약속한 경계 밖에서 찾은 꼴과, 그 꼴을 약속에 넣을지 볼 까닭)을 더하고, `FRICTION.md` 줄 양식의 갈래를 `{문제 | 멈춤 | 스킬 후보 | 경계 밖}`으로 고친다 (`plugins/plate/skills/retro/SKILL.md`)
- [ ] 4번에 생긴다. `done-phase-N.md`마다 "남은 것"에 적힌 부작용과 한계를 넷에 대어 보고, 걸리면 문제로 적는다 (`plugins/plate/skills/retro/SKILL.md`)
- [ ] eval에서 `FRICTION.md`의 갈래를 늘어놓은 곳을 `경계 밖`이 든 넷으로 맞춘다. 등급 기준과 3번 표는 건드리지 않는다 (`plugins/plate/skills/eval/SKILL.md`)

**통과 조건**
- 완료 조건 1의 첫째 확인(retro 셋)이 참이다.
  - 확인: retro의 4번, 5번, 회고 절 양식, `FRICTION.md` 줄 양식, 적는 규칙을 읽어 셋을 하나씩 찾는다. 셋 모두 있어야 통과다
- 완료 조건 2가 참이다.
  - 확인: `grep -rn '스킬 후보' plugins/plate/skills docs/ARCHITECTURE.md`가 낸 줄을 하나씩 읽어, 넷을 늘어놓는 줄에는 모두 `경계 밖`이 있다
- 테스트가 모두 통과한다.
  - 확인: `python3 -m unittest discover -s tests`가 `OK`
