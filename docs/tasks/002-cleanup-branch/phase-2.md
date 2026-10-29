# Phase 2: plan이 cleanup 브랜치에서 갈라 보낼 곳을 적는다

**목표**: plan이 `cleanup/…`에서 묻지 않고 `tasks/<이름>`을 갈라 tasks 머리에 `**보낼 곳**:` 줄을 적고, 그 동작이 ARCHITECTURE와 테스트에 맞는다.

**테스트 먼저**: 아니오 — 스킬 본문(`.md`)과 그 글을 지키는 테스트, 맥락 문서만 고친다

**읽을 것**
- `plugins/plate/skills/plan/SKILL.md`의 절대 규칙 4, 낱말의 "tasks 머리", "1. 진행 중인 tasks가 있는지 본다"의 브랜치 문단, "7. 쓰고 커밋한다", "계획 파일의 양식"의 tasks 머리, "적는 규칙"의 "이름과 번호"와 "tasks 머리"
- `plugins/plate/skills/cleanup/SKILL.md`의 보고서를 쓰기 전 브랜치를 맞추는 글 (phase 1이 더한, `cleanup/<보고서 이름>`을 만드는 글)
- `tests/test_skill_rules.py`의 `PlanRulesTest.test_commits_on_tasks_branch`
- `docs/ARCHITECTURE.md`의 패턴과 규칙의 plan 문단("plan은 git 레포이면 계획의 커밋을 `tasks/<이름>`에 넣는다"로 시작하는 줄), 데이터 흐름의 "계획"
- `docs/PRD.md`, `docs/ADR.md`, `docs/TOOLS.md`, `docs/BACKLOG.md`

**TODO**
- [ ] 앞 phase의 산출물에 대어 조건을 맞춘다. cleanup이 만드는 브랜치 이름의 꼴(`cleanup/<보고서 이름>`, 번호가 붙을 수 있다)을 phase 1이 고친 cleanup 본문에서 읽고, plan이 알아볼 꼴을 그것과 같게 둔다 (`plugins/plate/skills/plan/SKILL.md`)
- [ ] plan의 브랜치 글이 바뀐다.
  - 절대 규칙 4와 1번: `cleanup/…`이면 묻지 않는다.
  - 7번: 그 HEAD에서 `git switch -c tasks/<이름>`으로 만든다.
  - 다른 갈래(기본 브랜치, `tasks/<이름>`, 그 밖)는 그대로 둔다.
  (`plugins/plate/skills/plan/SKILL.md`)
- [ ] tasks 머리의 양식과 적는 규칙에 `**보낼 곳**: {그 cleanup 브랜치}` 줄이 더해진다. 이름 줄 아래에 두고, `cleanup/…`에서 갈랐을 때만 적고, 낱말의 "tasks 머리"도 맞춘다 (`plugins/plate/skills/plan/SKILL.md`)
- [ ] 바뀐 글을 지키는 시험이 된다. `PlanRulesTest.test_commits_on_tasks_branch`의 절대 규칙 4와 1번 단언이 새 글을 지키고, `cleanup/…`에서 묻지 않음과 보낼 곳 줄을 보는 시험이 더해진다 (`tests/test_skill_rules.py`)
- [ ] 맥락 문서가 맞는다. ARCHITECTURE의 plan 문단과 데이터 흐름의 "계획"이 `cleanup/…`에서 묻지 않고 갈라 보낼 곳을 적는다고 적는다 (`docs/ARCHITECTURE.md`)

**통과 조건**
- task 머리의 완료 조건 2가 참이다.
  - 확인: `grep -n '보낼 곳' plugins/plate/skills/plan/SKILL.md` → 절대 규칙, 1번, 7번, 계획 파일의 양식에 저마다 한 줄 이상
  - 확인: `mktemp -d` 시험 레포의 `cleanup/x`(`main`보다 커밋 하나 앞섬)에서 본문 7번의 브랜치 명령을 적힌 차례대로 돌린다. 기대: `git merge-base --is-ancestor cleanup/x tasks/<이름>`이 0이고 `git rev-parse main`이 전과 같다
  - 확인: 같은 레포에 로컬 `tasks/<이름>`이 이미 있을 때, 본문 "이름과 번호"의 이름 고르기(`git rev-parse --verify --quiet refs/heads/tasks/<이름>`)가 그 이름을 쓰지 않게 하는지 본문에서 읽는다
- task 머리의 완료 조건 1이 그대로다(phase 1이 이룬 cleanup 브랜치 글).
  - 확인: `grep -n -F 'cleanup/<' plugins/plate/skills/cleanup/SKILL.md` → 절대 규칙, 보고서를 쓰고 커밋하는 절, 고른 발견이 없을 때의 절에 저마다 한 줄 이상
- task 머리의 완료 조건 4 가운데 plan 쪽이 참이다.
  - 확인: `grep -n '보낼 곳' docs/ARCHITECTURE.md` → plan 문단과 데이터 흐름의 "계획"에 저마다 한 줄 이상
- 테스트가 통과한다.
  - 확인: `python3 -m unittest tests.test_skill_rules.PlanRulesTest -v` → `OK`, 새 시험 이름이 나온다
  - 확인: `python3 -m unittest discover -s tests` → 마지막 줄이 `OK`
