# Phase 2: run, phase, retro가 `phase-N.md`를 계획과 기록의 자리로 쓴다

**목표**: 세 스킬이 phase의 계획을 `phase-N.md`에서 읽고, 기록과 회고를 그 아래에 덧붙이고, 통과하면 그 파일 하나를 지운다. 실행 중에 `plan.md`는 계획을 고칠 때 말고는 바뀌지 않는다.

**읽을 것**
- `plugins/plate/skills/run/SKILL.md`, `plugins/plate/skills/phase/SKILL.md`, `plugins/plate/skills/retro/SKILL.md` (고칠 본문)
- `plugins/plate/skills/plan/SKILL.md` (Phase 1에서 고친 낱말과 `phase-N.md`의 양식)

**TODO**
- [x] 세 스킬의 낱말이 plan 스킬과 같은 뜻이다. 머리는 `plan.md`, phase의 계획은 `phase-N.md`의 계획 네 항목, 끝나지 않은 작업은 `phase-N.md`가 남아 있는 작업 폴더, 남은 첫 phase는 번호가 가장 작은 `phase-N.md`다
- [x] run이 수행을 맡길지를 `phase-N.md`에 기록 절(`## 한 일`)이 있는지로 본다 (2번의 표)
- [x] run이 통과한 phase의 `phase-N.md`만 `git rm`하고(고쳤으면 `docs/LESSONS.md`와 `AGENTS.md`도) 한 커밋으로 넣는다. `plan.md`는 건드리지 않는다. git 레포가 아니면 지우지 않고 이름을 `done-phase-N.md`로 바꾼다 (절대 규칙 3, 6번)
- [x] run의 계획 커밋과 "계획을 고친다"가 `plan.md`와 `phase-N.md`의 계획 부분을 다루고, 0번과 "합친다"가 worktree에 `phase-N.md`가 남았는지로 본다 (설명, 첫머리, 절대 규칙 4와 5, 0번, 1번, "계획을 고친다", "합친다")
- [x] phase가 자기 `phase-N.md`의 계획 네 항목을 읽고, 그 파일의 체크박스를 고치고, 기록 다섯 절을 그 아래에 덧붙인다. `plan.md`와 계획 네 항목의 글은 고치지 않고 커밋에 `plan.md`가 들지 않는다 (설명, 첫머리, 절대 규칙 3, 낱말, 1번, 2번, 4번, 5번, 양식)
- [x] retro가 계획을 `phase-N.md`에서 읽고, 직접 불렸을 때의 대상을 `phase-N.md`로 찾는다 (낱말, 0번, 1번, 5번)
- [x] 고친 본문의 바뀐 절을 사용자에게 보여 주고 확인받는다

**통과 조건**
- 네 본문에 한 파일 시절의 기준이 없다.
  - 확인: `grep -cE '코드 블록 밖|\(통과\) Phase|phase 절' plugins/plate/skills/*/SKILL.md` → 모두 0
- 세 본문에 도구 이름이 없다.
  - 확인: `cat plugins/plate/skills/{run,phase,retro}/SKILL.md | grep -oiE 'claude(\.md)?|codex|grok' | grep -vcx 'CLAUDE.md'` → 0
- 스킬 여섯이 불린다.
  - 확인: `claude -p --plugin-dir plugins/plate --output-format stream-json --verbose`의 실행 기록의 init 줄(세션의 스킬 목록)에 `plate:setup`, `plate:context`, `plate:plan`, `plate:run`, `plate:phase`, `plate:retro`가 있다
- 사용자가 고친 본문을 확인했다.
  - 확인: 바뀐 절을 적은 답글에 받은 답

## 한 일
- 세 스킬의 낱말: 머리, `phase-N.md`, 끝나지 않은 작업, 남은 첫 phase를 plan 스킬과 같은 뜻으로 고쳤다 (`plugins/plate/skills/run/SKILL.md`, `plugins/plate/skills/phase/SKILL.md`, `plugins/plate/skills/retro/SKILL.md`)
- run이 수행을 맡길지 보는 기준: 2번 표의 첫 행을 "기록 절(`## 한 일`)이 없다"로 바꿨다 (`plugins/plate/skills/run/SKILL.md`)
- run이 통과한 phase를 지우는 것: 6번에서 `plan.md`의 절을 잘라 내는 단계를 없애고 `phase-N.md`만 `git rm`한다. git 레포가 아니면 이름을 `done-phase-N.md`로 바꾼다. 절대 규칙 3도 그 파일만 말한다 (`plugins/plate/skills/run/SKILL.md`)
- run의 계획 커밋, "계획을 고친다", 0번, "합친다": 계획 파일(`plan.md`, `phase-N.md`)을 다루고 worktree에 `phase-N.md`가 남았는지로 본다. 설명, 첫머리, 절대 규칙 4와 5도 고쳤다 (`plugins/plate/skills/run/SKILL.md`)
- phase: `plan.md`와 자기 `phase-N.md`만 읽고, 그 파일의 체크박스를 고치고, 계획 아래에 기록 다섯 절을 덧붙인다. 커밋에 `plan.md`를 넣지 않는다. 양식의 절 이름은 "기록의 양식"이고 제목 줄을 뺐다 (`plugins/plate/skills/phase/SKILL.md`)
- retro: 계획을 `phase-N.md`에서 읽고, 직접 불렸을 때의 대상을 번호가 가장 작은 `phase-N.md`로 찾는다 (`plugins/plate/skills/retro/SKILL.md`)
- 사용자 확인: 바뀐 글을 답글로 보여 주고 2026-10-13에 확인받았다

## 확인 결과
- 네 본문에 한 파일 시절의 기준이 없다.
  - `grep -cE '코드 블록 밖|\(통과\) Phase|phase 절' plugins/plate/skills/*/SKILL.md` → 여섯 파일 모두 0. 통과
- 세 본문에 도구 이름이 없다.
  - `cat plugins/plate/skills/{run,phase,retro}/SKILL.md | grep -oiE 'claude(\.md)?|codex|grok' | grep -vcx 'CLAUDE.md'` → 0. 통과
- 스킬 여섯이 불린다.
  - `claude -p "한 낱말로만 답한다: 확인" --plugin-dir plugins/plate --output-format stream-json --verbose`의 init 줄 → `skills`에 `plate:context`, `plate:phase`, `plate:plan`, `plate:retro`, `plate:run`, `plate:setup` (2.1.296). 통과
- 사용자가 고친 본문을 확인했다.
  - 바뀐 글을 적은 답글에 "확인했어 괜찮네"라는 답을 받았다. 통과

## 계획과 달라진 점
- TODO에 없던 것 넷을 더했고 사용자가 확인했다. run 절대 규칙 4가 지키는 것이 "머리와 통과 조건"에서 계획 전체로 넓어졌다. run 절대 규칙 5의 직접 고치는 파일에 `phase-N.md`가 들었다. run 1번의 계획 커밋은 한 번도 커밋되지 않은 계획 파일만 넣는다. "계획을 고친다"는 체크박스와 기록 절을 건드리지 않는다.
- 통과 조건이 스킬 목록을 "실행 기록 첫 줄"에서 본다고 적었으나 훅의 줄이 먼저 나와 init 줄에 있었다. 사용자의 승인을 받아 계획을 고쳤다(커밋 `739e9f5`).

## 남은 것
없음

## 하네스에서 걸린 것
없음
