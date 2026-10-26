# Phase 2: 규칙 준수 표에 run의 두 꼴을 더한다

**목표**: eval 3번의 규칙 준수 표가 run이 만드는 두 커밋 꼴을 보고, ARCHITECTURE가 바뀐 eval과 맞는다.

**테스트 먼저**: 아니오 — `.md`만 고친다

**읽을 것**
- `plugins/plate/skills/eval/SKILL.md`의 낱말 "더한 phase"와 3번의 규칙 준수
- `plugins/plate/skills/run/SKILL.md`에서 `plan: NNN-slug 수정`과 `NNN-slug: phase N 통과`로 커밋하는 곳 모두(넣는 파일을 대어 보려고)
- `git show c2a983c^:docs/tasks/FRICTION.md` (42줄)
- `docs/ARCHITECTURE.md`

**TODO**
- [ ] 3번 표에 두 행을 더한다. `plan: NNN-slug 수정`(만든 스킬 run, 넣어도 되는 파일: 더한 `phase-M.md`, 고친 계획 파일, `RUNLOG.md`)과 `NNN-slug: phase N 통과`(만든 스킬 run, 넣어도 되는 파일: 그 `phase-N.md`를 `done-phase-N.md`로 바꾼 이름 바꾸기와 `RUNLOG.md`). 넣어도 되는 파일은 run 본문에서 그 메시지로 커밋하는 곳마다 대어 보고 적는다 (`plugins/plate/skills/eval/SKILL.md`)
- [ ] 낱말 "더한 phase"가 바뀐 표와 어긋나지 않게 맞춘다 (`plugins/plate/skills/eval/SKILL.md`)
- [ ] `docs/ARCHITECTURE.md`에서 eval을 적은 줄이 바뀐 eval과 어긋나면 맞춘다 (`docs/ARCHITECTURE.md`)

**통과 조건**
- 완료 조건 1의 둘째, 셋째 확인이 참이다.
  - 확인: 3번 표를 읽어 두 행과 넣어도 되는 파일이 완료 조건 1에 적힌 대로 있다
  - 확인: `grep -n 'plan: NNN-slug 수정' plugins/plate/skills/eval/SKILL.md`가 낱말의 줄과 표의 줄을 둘 다 낸다
- 완료 조건 2가 참이다.
  - 확인: `grep -n 'plan: NNN-slug 수정\|phase N 통과' plugins/plate/skills/run/SKILL.md`가 낸 줄마다 넣는 파일이 eval 표의 같은 행에 모두 든다
- 완료 조건 3이 참이다.
  - 확인: `grep -n 'eval\|규칙 준수\|실패 양상' docs/ARCHITECTURE.md`가 낸 줄을 하나씩 읽어 어긋나는 줄이 없다
- phase 1이 이룬 완료 조건 1의 첫째 확인이 그대로 참이다.
  - 확인: phase 1의 통과 조건 확인을 다시 돌린다
- 테스트가 모두 통과한다.
  - 확인: `python3 -m unittest discover -s tests`가 `OK`
