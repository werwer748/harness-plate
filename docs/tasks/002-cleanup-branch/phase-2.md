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
- [x] 앞 phase의 산출물에 대어 조건을 맞춘다. cleanup이 만드는 브랜치 이름의 꼴(`cleanup/<보고서 이름>`, 번호가 붙을 수 있다)을 phase 1이 고친 cleanup 본문에서 읽고, plan이 알아볼 꼴을 그것과 같게 둔다 (`plugins/plate/skills/plan/SKILL.md`)
- [x] plan의 브랜치 글이 바뀐다.
  - 절대 규칙 4와 1번: `cleanup/…`이면 묻지 않는다.
  - 7번: 그 HEAD에서 `git switch -c tasks/<이름>`으로 만든다.
  - 다른 갈래(기본 브랜치, `tasks/<이름>`, 그 밖)는 그대로 둔다.
  (`plugins/plate/skills/plan/SKILL.md`)
- [x] tasks 머리의 양식과 적는 규칙에 `**보낼 곳**: {그 cleanup 브랜치}` 줄이 더해진다. 이름 줄 아래에 두고, `cleanup/…`에서 갈랐을 때만 적고, 낱말의 "tasks 머리"도 맞춘다 (`plugins/plate/skills/plan/SKILL.md`)
- [x] 바뀐 글을 지키는 시험이 된다. `PlanRulesTest.test_commits_on_tasks_branch`의 절대 규칙 4와 1번 단언이 새 글을 지키고, `cleanup/…`에서 묻지 않음과 보낼 곳 줄을 보는 시험이 더해진다 (`tests/test_skill_rules.py`)
- [x] 맥락 문서가 맞는다. ARCHITECTURE의 plan 문단과 데이터 흐름의 "계획"이 `cleanup/…`에서 묻지 않고 갈라 보낼 곳을 적는다고 적는다 (`docs/ARCHITECTURE.md`)

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

## 한 일
- 앞 phase의 산출물에 대어 조건을 맞춘다: phase 1이 고친 cleanup 본문의 낱말 "cleanup 브랜치"(`cleanup/<보고서 이름>`, 있으면 `cleanup/<보고서 이름>-2`처럼 번호)를 읽고, plan 낱말에 같은 꼴의 "cleanup 브랜치"를 더해 이름이 `cleanup/`으로 시작하면 cleanup 브랜치로 본다고 적었다 (`plugins/plate/skills/plan/SKILL.md`)
- plan의 브랜치 글: 절대 규칙 4에 cleanup 브랜치에서도 묻지 않고 그 HEAD에서 `tasks/<이름>`을 만들거나 바꾸고 새 tasks면 `**보낼 곳**:` 줄에 적는다는 갈래를 더했다. 1번에 "cleanup 브랜치(`cleanup/…`)이면 묻지 않고 2번으로 간다"와 보낼 곳 문장을 더하고, 묻는 갈래를 "기본 브랜치도 cleanup 브랜치도 `tasks/<이름>`도 아니면"으로 바꿨다. 7번의 `git switch -c` 갈래에 cleanup 브랜치를 넣고, 보낼 곳이 승인받은 초안대로 든다는 것과 더하는 경우는 보낼 곳을 고치지 않는다는 문장을 더했다. 다른 갈래는 그대로다 (`plugins/plate/skills/plan/SKILL.md`)
- tasks 머리의 양식과 적는 규칙: 양식의 이름 줄 아래에 `**보낼 곳**: {그 cleanup 브랜치}`를, 적는 규칙 "tasks 머리"에 그 줄을 cleanup 브랜치에서 갈랐을 때만 이름 줄 바로 아래에 둔다는 항목을, 낱말 "tasks 머리"에 보낼 곳을 더했다 (`plugins/plate/skills/plan/SKILL.md`)
- 시험: `test_commits_on_tasks_branch`의 절대 규칙 4 단언을 둘로 나누고, 1번의 묻는 갈래와 "기본 브랜치이면 묻지 않고" 단언을 새 글에 맞췄다. 새 시험 `test_cleanup_branch_sends_back`이 낱말, 절대 규칙 4, 1번(묻는 글보다 앞), 7번, 양식, 적는 규칙의 cleanup 브랜치·보낼 곳 글과 cleanup 본문의 `-2` 꼴을 본다 (`tests/test_skill_rules.py`)
- 맥락 문서: ARCHITECTURE 패턴과 규칙의 plan 문단에 cleanup 브랜치 갈래와 보낼 곳 줄, 이유 한 문장을, 데이터 흐름 "계획"에 cleanup/… 갈래와 보낼 곳 줄을 더했다 (`docs/ARCHITECTURE.md`)

## 확인 결과
- task 머리의 완료 조건 2가 참이다.
  - `grep -n '보낼 곳' plugins/plate/skills/plan/SKILL.md` → 19(절대 규칙 4), 26(낱말), 55(1번), 139(7번), 170(양식), 244(적는 규칙). 통과
  - `mktemp -d` 시험 레포(`main` 커밋 하나, `cleanup/x` 커밋 하나 더)에서 `git branch --show-current` → `cleanup/x`, `git rev-parse --verify --quiet refs/heads/tasks/fix` → 출력 없음(종료 1), `git switch -c tasks/fix` → 전환. `git merge-base --is-ancestor cleanup/x tasks/fix` → 0, `git rev-parse main` → 전과 같음. 통과
  - 같은 레포에 `tasks/old`를 만든 뒤 `git rev-parse --verify --quiet refs/heads/tasks/old` → 해시 출력(종료 0). 본문 "이름과 번호"는 "새 tasks의 이름은 로컬에 같은 이름의 `tasks/<이름>` 브랜치가 없는 것으로 고른다(…이 아무것도 내지 않는다)"이므로 그 이름을 쓰지 않는다. 통과
- task 머리의 완료 조건 1이 그대로다.
  - `grep -n -F 'cleanup/<' plugins/plate/skills/cleanup/SKILL.md` → 17·18(절대 규칙), 115·127(5번 보고서를 쓰고 커밋), 149·153·154·155·161·163·165(고른 발견이 없을 때). 통과
- task 머리의 완료 조건 4 가운데 plan 쪽이 참이다.
  - `grep -n '보낼 곳' docs/ARCHITECTURE.md` → 56(plan 문단), 65(데이터 흐름 "계획"). 통과
- 테스트가 통과한다.
  - `python3 -m unittest tests.test_skill_rules.PlanRulesTest -v` → 24개 `OK`, `test_cleanup_branch_sends_back ... ok`. 통과
  - `python3 -m unittest discover -s tests` → 마지막 줄 `OK`. 통과

## 계획과 달라진 점
없음

## 남은 것
- 더하는 경우에 cleanup 브랜치에서 부르면 묻지 않고 7번에서 그 tasks의 `tasks/<이름>`으로 바꾼다(기본 브랜치에서와 같은 갈래). 보낼 곳은 새 tasks에만 적고 더하는 경우는 고치지 않는다.
- ARCHITECTURE plan 문단의 이유에 run이 보낼 곳에 합친다는 글을 넣었는데, run 쪽 동작은 phase 3이 만든다.
- 양식에서 `**보낼 곳**:` 줄이 이름 줄 바로 아래(빈 줄 없음)라 마크다운으로 그리면 한 문단으로 이어 보인다. 줄 단위로 읽는 데는 지장이 없다.

## 하네스에서 걸린 것
없음
