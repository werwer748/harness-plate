# Phase 1: plan 스킬이 계획을 `plan.md`와 `phase-N.md`로 쓴다

**목표**: plan 스킬이 머리를 `plan.md`에, phase마다의 계획을 `phase-N.md`에 쓰고, 결정을 한 줄로 적고, 다섯 범주에 드는 결정만 ADR 후보로 낸다.

**읽을 것**
- `plugins/plate/skills/plan/SKILL.md` (고칠 본문)
- `plugins/plate/skills/context/SKILL.md` ("ADR 항목" 절의 다섯 범주)
- `plugins/plate/skills/phase/SKILL.md` ("`phase-N.md`의 양식": 계획 네 항목 아래에 붙을 기록 다섯 절)

**TODO**
- [x] 쓰는 파일과 커밋에 드는 파일이 `plan.md`와 `phase-1.md`부터 `phase-N.md`까지다 (설명, 첫머리, 절대 규칙 3과 4, 7번, 8번)
- [x] 낱말이 바뀐다. 머리는 `plan.md`의 제목과 다섯 절이고, phase의 계획은 `phase-N.md`의 계획 네 항목이고, 끝나지 않은 작업은 `phase-N.md`가 남아 있는 작업 폴더다. 2번이 그 기준으로 찾는다
- [x] 추천안과 다른 안을 고르면 그 자리에서 이유를 한 번 묻는다 (5번)
- [x] 초안은 한 답글에 파일마다 경로를 붙여 모두 보여 준다. 다섯 범주에 드는 결정은 "ADR 후보"로 결정과 따로 보여 주고, 승인한 것만 ADR 항목을 더하는 TODO가 된다 (6번)
- [x] 양식이 둘이다: `plan.md`(제목과 다섯 절), `phase-N.md`(제목 `# Phase N: 이름`과 계획 네 항목)
- [x] 적는 규칙이 머리의 결정대로 바뀐다. 결정은 한 줄로 적고 "(추천안으로 정함)" 표시는 그대로 둔다. TODO에는 만들 것의 본문을 옮겨 적지 않는다. `docs/ADR.md`에 항목을 더하는 TODO는 승인받은 ADR 후보에만 생기고, 항목에 계획이나 작업 폴더를 적지 않는다
- [x] 고친 본문의 바뀐 절을 사용자에게 보여 주고 확인받는다

**통과 조건**
- 본문에 한 파일 시절의 기준이 없다.
  - 확인: `grep -cE '코드 블록 밖|phase 절|^## Phase' plugins/plate/skills/plan/SKILL.md` → 0
- ADR을 말하는 곳이 1번(표준 네 문서), 4번(어긋나는지 본다), ADR 후보의 규칙뿐이다.
  - 확인: `grep -n 'ADR' plugins/plate/skills/plan/SKILL.md`의 줄을 읽는다
- 본문에 도구 이름이 없다.
  - 확인: `grep -oiE 'claude(\.md)?|codex|grok' plugins/plate/skills/plan/SKILL.md | grep -vcx 'CLAUDE.md'` → 0
- 사용자가 고친 본문을 확인했다.
  - 확인: 바뀐 절을 적은 답글에 받은 답

## 한 일
- 쓰는 파일과 커밋에 드는 파일: 설명, 첫머리, 절대 규칙 3과 4, 7번, 8번이 "계획 파일"(`plan.md`와 `phase-1.md`부터 `phase-N.md`까지)을 말한다 (`plugins/plate/skills/plan/SKILL.md`)
- 낱말: 머리, phase, 끝나지 않은 작업을 고치고 "계획 파일"을 더했다. 2번이 `phase-N.md`가 있는지를 파일 이름으로 본다 (`plugins/plate/skills/plan/SKILL.md`)
- 추천안과 다른 안을 고르면 이유를 한 번 묻는다: 5번에 한 줄을 더했다 (`plugins/plate/skills/plan/SKILL.md`)
- 초안과 ADR 후보: 6번이 파일마다 경로를 붙여 모두 적고, 다섯 범주에 드는 결정을 "ADR 후보"로 따로 적는다 (`plugins/plate/skills/plan/SKILL.md`)
- 양식이 둘이다: "계획 파일의 양식" 절에 `plan.md`와 `phase-N.md`의 꼴을 두었다 (`plugins/plate/skills/plan/SKILL.md`)
- 적는 규칙: 결정, phase의 파일, TODO, ADR에 항목을 더하는 TODO의 규칙을 고쳤다 (`plugins/plate/skills/plan/SKILL.md`)
- 사용자 확인: 바뀐 글을 답글로 보여 주고 2026-10-13에 확인받았다

## 확인 결과
- 본문에 한 파일 시절의 기준이 없다.
  - `grep -cE '코드 블록 밖|phase 절|^## Phase' plugins/plate/skills/plan/SKILL.md` → 0. 통과
- ADR을 말하는 곳이 1번(표준 네 문서), 4번(어긋나는지 본다), ADR 후보의 규칙뿐이다.
  - `grep -n 'ADR' plugins/plate/skills/plan/SKILL.md` → 42행(1번), 60행(4번), 83행(6번), 91행(7번), 193행(적는 규칙). 뒤의 셋이 ADR 후보의 규칙이다. 통과
- 본문에 도구 이름이 없다.
  - `grep -oiE 'claude(\.md)?|codex|grok' plugins/plate/skills/plan/SKILL.md | grep -vcx 'CLAUDE.md'` → 0. 통과
- 사용자가 고친 본문을 확인했다.
  - 바뀐 글을 적은 답글에 "확인했어 괜찮네"라는 답을 받았다. 통과

## 계획과 달라진 점
- TODO에 없던 규칙 둘을 더했고 사용자가 확인했다. 이유를 받지 못한 결정은 "이유: 말하지 않음"으로 적는다. 사용자가 뺀 ADR 후보는 그 TODO를 지우고 초안을 다시 보여 준다.

## 남은 것
없음

## 하네스에서 걸린 것
없음
