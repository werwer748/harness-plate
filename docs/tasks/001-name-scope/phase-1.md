# Phase 1: plan과 retro가 이름이 남을 수 있는 곳과 이름마다를 덮는다

**목표**: plan 6번·**조건**과 retro 4번의 "지난 tasks의 같은 이름" 규칙이 합쳐지지 않은 다른 브랜치(로컬과 origin)의 같은 이름과 한 동작이 만드는 이름마다도 덮고, 테스트가 그 글을 지킨다.

**테스트 먼저**: 아니오 — `.md`인 스킬 본문만 고치고, 테스트는 그 글을 지키는 시험이라 코드 파일의 동작을 바꾸지 않는다

**읽을 것**
- `plugins/plate/skills/plan/SKILL.md` ("6. 초안을 보여 주고 승인받는다"의 초안 전 점검과 "적는 규칙"의 **조건**에서 `지난 tasks의 같은 이름`이 든 줄)
- `plugins/plate/skills/retro/SKILL.md` ("4. task의 변경을 점검한다"에서 `지난 tasks의 같은 이름`이 든 줄)
- `tests/test_skill_rules.py` (`PlanRulesTest.test_80_repeated_names_and_multiple_inputs_covered`, `RetroRulesTest.test_80_decided_behavior_with_repeated_names_goes_out_of_bounds`)
- `docs/ARCHITECTURE.md` (디렉터리 구조의 `test_skill_rules.py` 줄)
- `docs/PRD.md`, `docs/ADR.md`, `docs/TOOLS.md`, `docs/BACKLOG.md`

**TODO**
- [ ] plan 6번의 초안 전 점검과 "적는 규칙"의 **조건**에서 `지난 tasks의 같은 이름`이 든 줄이 바뀐다. 이름이나 번호로 고르거나 찾는 동작마다 세 경우(지난 tasks의 같은 이름, 합쳐지지 않은 다른 브랜치(로컬과 origin)의 같은 이름, 한 동작이 만드는 이름마다)를 확인 하나씩으로 덮게 한다. 입력이 둘 이상인 경우의 글은 그대로 둔다 (`plugins/plate/skills/plan/SKILL.md`)
- [ ] retro 4번에서 `지난 tasks의 같은 이름`이 든 줄이 같은 세 경우를 들게 바뀐다 (`plugins/plate/skills/retro/SKILL.md`)
- [ ] 두 옛 시험이 새 글을 지키게 바뀌고, 시험 `PlanRulesTest.test_80_names_left_anywhere_covered`와 `RetroRulesTest.test_80_retro_names_left_anywhere`가 더해진다. 두 시험은 그 줄에 `지난 tasks의 같은 이름`, `합쳐지지 않은 다른 브랜치`, `이름마다`가 있는지 본다 (`tests/test_skill_rules.py`)
- [ ] 디렉터리 구조의 `test_skill_rules.py` 줄에서 #80 규칙을 적은 대목이 세 경우를 든다 (`docs/ARCHITECTURE.md`)

**통과 조건**
- 완료 조건 1이 참이다.
  - 확인: `grep -n '합쳐지지 않은 다른 브랜치' plugins/plate/skills/plan/SKILL.md plugins/plate/skills/retro/SKILL.md` → plan의 6번과 **조건**, retro 4번에 저마다 한 줄 이상이고, 그 줄마다 `지난 tasks의 같은 이름`과 `이름마다`가 함께 있다
  - 확인: 작업 트리의 `cp -R` 사본에서 `sed -i '' '/합쳐지지 않은 다른 브랜치/d' plugins/plate/skills/plan/SKILL.md plugins/plate/skills/retro/SKILL.md` 뒤 `python3 -m unittest tests.test_skill_rules.PlanRulesTest.test_80_names_left_anywhere_covered tests.test_skill_rules.RetroRulesTest.test_80_retro_names_left_anywhere` → `FAILED`
- 디렉터리 구조의 `test_skill_rules.py` 줄이 세 경우를 든다.
  - 확인: `grep -n -F 'test_skill_rules.py' docs/ARCHITECTURE.md` → 그 줄에 `합쳐지지 않은 다른 브랜치`가 있다
- 테스트 묶음이 모두 통과한다.
  - 확인: `python3 -m unittest discover -s tests` → 마지막 줄이 `OK`
