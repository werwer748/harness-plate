# Phase 3: 장면 C와 D를 돌린다

**목표**: 회고가 계획을 바꾸게 할 때 멈추는 것(#34, #38)과 고칠 phase의 TODO·통과 조건(#38)을 임시 복제본에서 돌려 `docs/TOOLS.md`에 남긴다.

**테스트 먼저**: 아니오 — 스킬을 돌려 보고 `.md`에 적는다

**읽을 것**
- `plugins/plate/skills/run/SKILL.md`의 "7. task 회고를 맡긴다", "8. 고칠 phase를 더한다", "멈춘다", "`RUNLOG.md`" 절 (phase 1이 고친 동작)
- `docs/TOOLS.md`의 "Claude Code" 절 (헤드리스 명령의 꼴, `--resume`, 허용 목록, phase 2가 더한 run 장면 A·B 절)

**TODO**
- [ ] 장면 C: 복제본에 phase가 모두 통과하고 `retro.md`의 마지막 회고 절이 "문제 있음"이며 그 문제가 task 머리의 완료 조건을 좁혀야 고칠 수 있는 작은 tasks(`RUNLOG.md`에 `tasks 일괄`)를 차리고 run을 부른다. 새 `phase-M.md`가 생기지 않고 출력이 원인과 해결책을 보이고 묻고 멈춘 것을 본다. `--resume`으로 답한 뒤 `RUNLOG.md`의 마지막 물음 줄의 물은 자리가 `멈춤`인지 본다 (임시 폴더)
- [ ] 장면 D: 새 복제본에 마지막 회고 절의 문제가 둘(README에 동작이 적힌 파일의 문제, 이미 `plan: NNN-slug 수정` 커밋으로 고친 문제)인 작은 tasks(`tasks 일괄`)를 차리고 run을 부른다. 새 `plan: NNN-slug 수정` 커밋의 `phase-M.md`를 `git show`로 읽어 앞의 문제의 TODO에 README 경로가 있고, 뒤의 문제는 TODO에 없고 통과 조건에 그 커밋 해시와 함께 있는지 본다 (임시 폴더)
- [ ] 결과가 run 본문의 결함을 보이면 `plugins/plate/skills/run/SKILL.md`를 고치고, 장면 C·D와 함께 장면 A(phase 하나가 남은 작은 tasks를 `--permission-mode plan`으로 부르면 에이전트 줄 없이 plan 모드를 알리며 묻고 멈춘다)와 장면 B(phase가 모두 통과하고 회고가 없는 작은 tasks를 tasks 일괄로 부르면 회고 커밋 뒤와 하네스 eval 커밋 뒤에 `RUNLOG.md`만 바꾼 커밋이 있고 "고칠지"에서 `git status --short`가 비었다)를 새 복제본에서 다시 돌고 phase 2의 절 아래에 다시 돈 결과를 더한다 (`plugins/plate/skills/run/SKILL.md`, `docs/TOOLS.md`)
- [ ] `docs/TOOLS.md`의 run 장면 A·B 절 뒤에 장면 C·D 절이 더해진다. task 머리의 결정에 적힌 필드를 장면마다 적는다 (`docs/TOOLS.md`)

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건 1~3의 확인을 모두 돌린다. 완료 조건 3의 장면 A~D는 그 조건에 적힌 기대로 본다
