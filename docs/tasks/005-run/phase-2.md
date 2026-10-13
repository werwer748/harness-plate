# Phase 2: run, phase, retro가 `phase-N.md`를 계획과 기록의 자리로 쓴다

**목표**: 세 스킬이 phase의 계획을 `phase-N.md`에서 읽고, 기록과 회고를 그 아래에 덧붙이고, 통과하면 그 파일 하나를 지운다. 실행 중에 `plan.md`는 계획을 고칠 때 말고는 바뀌지 않는다.

**읽을 것**
- `plugins/plate/skills/run/SKILL.md`, `plugins/plate/skills/phase/SKILL.md`, `plugins/plate/skills/retro/SKILL.md` (고칠 본문)
- `plugins/plate/skills/plan/SKILL.md` (Phase 1에서 고친 낱말과 `phase-N.md`의 양식)

**TODO**
- [ ] 세 스킬의 낱말이 plan 스킬과 같은 뜻이다. 머리는 `plan.md`, phase의 계획은 `phase-N.md`의 계획 네 항목, 끝나지 않은 작업은 `phase-N.md`가 남아 있는 작업 폴더, 남은 첫 phase는 번호가 가장 작은 `phase-N.md`다
- [ ] run이 수행을 맡길지를 `phase-N.md`에 기록 절(`## 한 일`)이 있는지로 본다 (2번의 표)
- [ ] run이 통과한 phase의 `phase-N.md`만 `git rm`하고(고쳤으면 `docs/LESSONS.md`와 `AGENTS.md`도) 한 커밋으로 넣는다. `plan.md`는 건드리지 않는다. git 레포가 아니면 지우지 않고 이름을 `done-phase-N.md`로 바꾼다 (절대 규칙 3, 6번)
- [ ] run의 계획 커밋과 "계획을 고친다"가 `plan.md`와 `phase-N.md`의 계획 부분을 다루고, 0번과 "합친다"가 worktree에 `phase-N.md`가 남았는지로 본다 (설명, 첫머리, 절대 규칙 4와 5, 0번, 1번, "계획을 고친다", "합친다")
- [ ] phase가 자기 `phase-N.md`의 계획 네 항목을 읽고, 그 파일의 체크박스를 고치고, 기록 다섯 절을 그 아래에 덧붙인다. `plan.md`와 계획 네 항목의 글은 고치지 않고 커밋에 `plan.md`가 들지 않는다 (설명, 첫머리, 절대 규칙 3, 낱말, 1번, 2번, 4번, 5번, 양식)
- [ ] retro가 계획을 `phase-N.md`에서 읽고, 직접 불렸을 때의 대상을 `phase-N.md`로 찾는다 (낱말, 0번, 1번, 5번)
- [ ] 고친 본문의 바뀐 절을 사용자에게 보여 주고 확인받는다

**통과 조건**
- 네 본문에 한 파일 시절의 기준이 없다.
  - 확인: `grep -cE '코드 블록 밖|\(통과\) Phase|phase 절' plugins/plate/skills/*/SKILL.md` → 모두 0
- 세 본문에 도구 이름이 없다.
  - 확인: `cat plugins/plate/skills/{run,phase,retro}/SKILL.md | grep -oiE 'claude(\.md)?|codex|grok' | grep -vcx 'CLAUDE.md'` → 0
- 스킬 여섯이 불린다.
  - 확인: `claude -p --plugin-dir plugins/plate --output-format stream-json --verbose`의 실행 기록의 init 줄(세션의 스킬 목록)에 `plate:setup`, `plate:context`, `plate:plan`, `plate:run`, `plate:phase`, `plate:retro`가 있다
- 사용자가 고친 본문을 확인했다.
  - 확인: 바뀐 절을 적은 답글에 받은 답
