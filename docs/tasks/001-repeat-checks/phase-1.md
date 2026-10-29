# Phase 1: plan과 retro의 되풀이·여러 입력 규칙

**목표**: plan의 초안 점검과 조건 규칙, retro 4번이 지난 tasks의 같은 이름과 둘 이상의 입력을 다루고, 테스트와 ARCHITECTURE가 그것을 지킨다.

**테스트 먼저**: 아니오 — 스킬 본문(`.md`)과 그 글을 지키는 테스트만 고친다

**읽을 것**
- `plugins/plate/skills/plan/SKILL.md`의 "6. 초안을 보여 주고 승인받는다"와 "적는 규칙"의 **조건** (기존 규칙 "스킬·훅·양식의 동작을 바꾸는 완료 조건"과 "규칙이 다루는 경우마다"의 줄)
- `plugins/plate/skills/retro/SKILL.md`의 "4. task의 변경을 점검한다"와 "5. tasks 끝에 볼 것을 모은다" (`경계 밖`의 뜻)
- `tests/test_skill_rules.py`의 `PlanRulesTest`, `RetroRulesTest`와 도우미 `section`, `part`
- `docs/ARCHITECTURE.md`의 "디렉터리 구조"의 `test_skill_rules.py` 줄
- `gh issue view 80 --repo werwer748/harness-plate` (이슈 본문의 원인과 해결책)
- `docs/PRD.md`, `docs/ADR.md`, `docs/TOOLS.md`, `docs/BACKLOG.md`

**TODO**
- [ ] plan의 초안 전 점검 목록에 항목이 더해진다. 동작이 이름이나 번호로 커밋, 파일, 브랜치를 찾으면 지난 tasks의 같은 이름이 남은 경우를, 입력을 받으면 둘 이상인 경우를 확인 하나씩으로 덮었는지 보고, 없으면 더하게 한다 (`plugins/plate/skills/plan/SKILL.md`)
- [ ] plan의 "적는 규칙"의 **조건**에 같은 뜻의 규칙이 더해진다. 기존의 "규칙이 다루는 경우마다"(명령 예에만 대던 것)와 같은 것을 시키고 동작 일반으로 넓힌다 (`plugins/plate/skills/plan/SKILL.md`)
- [ ] retro 4번에 규칙이 더해진다. 결정이나 완료 조건이 정한 동작이라도 지난 tasks의 같은 이름이 남은 경우나 입력이 둘 이상인 경우에 목표를 해치면 "문제 아님"으로 닫지 않고 5번에서 `경계 밖`으로 모은다. 기록의 "남은 것" 줄 판정에도 걸린다 (`plugins/plate/skills/retro/SKILL.md`)
- [ ] `PlanRulesTest`와 `RetroRulesTest`에 위 세 글을 제 절에서 지키는 시험이 더해지고, ARCHITECTURE의 `test_skill_rules.py` 줄에 그 규칙이 더해진다 (`tests/test_skill_rules.py`, `docs/ARCHITECTURE.md`)

**통과 조건**
- task 머리의 완료 조건 1~5가 참이다.
  - 확인: `grep -n '지난 tasks의 같은 이름' plugins/plate/skills/plan/SKILL.md plugins/plate/skills/retro/SKILL.md` → plan의 "6. 초안을 보여 주고 승인받는다"와 "적는 규칙"의 **조건**, retro의 "4. task의 변경을 점검한다"에 저마다 한 줄 이상. plan의 줄에 "둘 이상"이 있고, retro의 줄에 `경계 밖`과 "둘 이상"이 있다
  - 확인: `python3 -m unittest tests.test_skill_rules.PlanRulesTest tests.test_skill_rules.RetroRulesTest -v` → 새 시험 이름이 나오고 `OK`
  - 확인: 작업 트리를 `cp -R`로 `mktemp -d` 사본에 옮기고, 사본의 두 본문에서 "지난 tasks의 같은 이름"이 든 줄을 지운 뒤 같은 명령을 돌린다 → 새 시험이 `FAIL`
  - 확인: `grep -n 'test_skill_rules.py' docs/ARCHITECTURE.md` → 그 줄에 "지난 tasks의 같은 이름"이 있다
  - 확인: `python3 -m unittest discover -s tests` → 마지막 줄이 `OK`
