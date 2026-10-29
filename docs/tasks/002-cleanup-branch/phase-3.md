# Phase 3: run이 보낼 곳으로 합친 뒤 PR이나 합침을 묻는다

**목표**: run이 tasks 머리의 `**보낼 곳**:` 줄대로 tasks를 그 브랜치에 합치고 그 브랜치의 PR이나 합침을 묻는다. 그 동작이 PRD, ARCHITECTURE, 테스트에 맞는다.

**테스트 먼저**: 아니오 — 스킬 본문(`.md`)과 그 글을 지키는 테스트, 맥락 문서만 고친다

**읽을 것**
- `plugins/plate/skills/run/SKILL.md`의 절대 규칙 5, 낱말의 "tasks 머리", "0. tasks를 본다", "tasks 끝"의 "비운다", "PR을 연다", "PR 본문의 꼴", "합친다", "10. 보고한다"
- `plugins/plate/skills/plan/SKILL.md`의 "계획 파일의 양식"의 tasks 머리 (phase 2가 더한 `**보낼 곳**:` 줄)
- `tests/test_skill_rules.py`의 `RunRulesTest` (0번 재개, PR, 합친다를 보는 시험)
- `docs/PRD.md`의 핵심 기능 8
- `docs/ARCHITECTURE.md`의 패턴과 규칙의 run 문단("run은 기본 브랜치(`origin`의 HEAD"로 시작하는 줄), 데이터 흐름의 "tasks 끝"
- `docs/ADR.md`, `docs/TOOLS.md`, `docs/BACKLOG.md`

**TODO**
- [ ] 앞 phase의 산출물에 대어 조건을 맞춘다. phase 2가 고친 plan 양식에서 `**보낼 곳**:` 줄의 꼴과 자리를 읽고, run이 읽는 꼴을 그것과 같게 둔다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] "비운다" 뒤에 보낼 곳이 있으면 거기로 합치는 자리가 더해진다.
  - 보낼 곳은 비우기 전에 tasks 머리에서 읽어 둔다.
  - `tasks/<이름>`을 그 브랜치에 로컬로 합칠지 묻는다. squash하지 않고, 충돌하면 되돌리고, 합치면 `tasks/<이름>`을 지운다.
  - 합친 뒤 origin이 GitHub이면 "PR을 연다"를 그 브랜치를 머리로 해서 돈다. 그 밖이면 "합친다"를 그 브랜치를 합칠 브랜치로 해서 돈다.
  - 보낼 곳이 로컬에 없으면 합치지도 PR을 열지도 않고 그 이름을 알리고 10번으로 간다.
  - 그 줄이 없는 tasks는 지금과 같다.
  (`plugins/plate/skills/run/SKILL.md`)
- [ ] 0번의 비운 뒤 재개가 보낼 곳이 있는 tasks에서도 같은 자리로 간다. `tasks/<이름>`에서 비운 뒤면 보낼 곳으로 합치는 자리로 간다. 보낼 곳 브랜치에서 그 tasks를 합친 뒤면 PR·합침으로 간다. 명령 치환 없이 한 명령씩 부른다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] 절대 규칙 5와 10번 보고가 맞는다. 푸시하는 브랜치에 보낼 곳이 들고, 보고에 보낼 곳으로 합쳤는지, 하지 않았으면 그 까닭이 더해진다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] 바뀐 글을 지키는 시험이 더해진다. 보낼 곳으로 합침, 보낼 곳이 없을 때, 재개, 절대 규칙 5를 본다. 바뀐 글을 지키던 기존 `RunRulesTest`의 단언도 새 글을 지킨다 (`tests/test_skill_rules.py`)
- [ ] 맥락 문서가 맞는다. PRD 핵심 기능 8, ARCHITECTURE의 run 문단과 데이터 흐름의 "tasks 끝"이 보낼 곳으로 합친 뒤 PR·합침, 보낼 곳이 없을 때, 재개를 적는다 (`docs/PRD.md`, `docs/ARCHITECTURE.md`)

**통과 조건**
- task 머리의 완료 조건 3이 참이다.
  - 확인: `grep -n '보낼 곳' plugins/plate/skills/run/SKILL.md` → 절대 규칙, 0번, "비운다", "PR을 연다", "합친다"에 저마다 한 줄 이상
  - 확인: `mktemp -d` 시험 레포에서 본문의 명령을 적힌 차례대로 세 갈래로 돌린다.
    - 합칠 때: `main` → `cleanup/x`(커밋 하나) → `tasks/y`(커밋 둘, 마지막 제목 `y: 비움`)를 두고 합치는 명령을 돌린다. 기대: `git merge-base --is-ancestor tasks/y cleanup/x`가 0이고 `main`의 해시가 그대로다.
    - 보낼 곳이 없을 때: `cleanup/x`를 지운 레포에서 있는지 보는 명령이 아무것도 내지 않는다. 기대: 그 갈래가 합치는 명령에 닿지 않는다.
    - 재개할 때: 합친 뒤의 `cleanup/x`에서 0번의 재개 판정에 쓰는 명령(브랜치, 마지막 커밋 제목)을 돌린다. 기대: 본문이 정한 PR·합침 자리로 가는 값이 나온다.
- task 머리의 완료 조건 1·2가 그대로다(phase 1·2가 이룬 글).
  - 확인: `grep -n -F 'cleanup/<' plugins/plate/skills/cleanup/SKILL.md` → 절대 규칙, 보고서를 쓰고 커밋하는 절, 고른 발견이 없을 때의 절에 저마다 한 줄 이상
  - 확인: `grep -n '보낼 곳' plugins/plate/skills/plan/SKILL.md` → 절대 규칙, 1번, 7번, 계획 파일의 양식에 저마다 한 줄 이상
- task 머리의 완료 조건 4, 5, 6이 참이다.
  - 확인: `grep -n -F 'cleanup/<' docs/PRD.md docs/ARCHITECTURE.md` → PRD 핵심 기능 9, ARCHITECTURE 디렉터리 구조의 cleanup 줄, plan 문단, 데이터 흐름의 "정리 점검"에 저마다 한 줄 이상
  - 확인: `grep -n '보낼 곳' docs/PRD.md docs/ARCHITECTURE.md` → PRD 핵심 기능 8, ARCHITECTURE의 plan 문단, run 문단, 데이터 흐름의 "계획"과 "tasks 끝"에 저마다 한 줄 이상
  - 확인: `python3 -m unittest tests.test_cleanup_skill tests.test_skill_rules -v` → `OK`. cleanup 브랜치, plan의 보낼 곳, run의 보낼 곳을 보는 새 시험 이름이 나온다
  - 확인: `grep -n '지난 tasks의 같은 이름' plugins/plate/skills/plan/SKILL.md plugins/plate/skills/retro/SKILL.md` → plan의 "6. 초안을 보여 주고 승인받는다"와 "적는 규칙"의 **조건**, retro의 "4. task의 변경을 점검한다"에 저마다 한 줄 이상
  - 확인: `python3 -m unittest discover -s tests` → 마지막 줄이 `OK`
