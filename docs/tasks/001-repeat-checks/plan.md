# plan과 retro가 되풀이되는 이름과 여러 입력의 경우를 본다

## 목표
plan의 초안 점검과 조건 규칙은 동작이 이름이나 번호로 찾으면 지난 tasks의 같은 이름이 남은 경우를, 입력을 받으면 둘 이상인 경우를 확인으로 덮게 한다. retro 4번은 결정이 정한 동작이라도 그런 경우에 목표를 해치면 "문제 아님"으로 닫지 않고 경계 밖으로 올린다. 테스트가 그 글들을 지킨다(#80).

## 범위 밖
- check, review, eval 본문을 고치는 것. 이슈 #80의 해결책은 plan과 retro만 든다.
- plan과 retro를 헤드리스로 끝까지 돌리는 것.

## 완료 조건
1. plan의 "6. 초안을 보여 주고 승인받는다"의 초안 전 점검 목록과 "적는 규칙"의 **조건**이 다음을 저마다 시킨다. 둘 다 "지난 tasks의 같은 이름"이라는 낱말을 쓴다.
   - 동작이 이름이나 번호(task 폴더 이름, phase 번호, 브랜치 이름, 보고서 이름 같은 것)로 커밋, 파일, 브랜치를 찾으면, 지난 tasks의 같은 이름이 남은 경우를 확인 하나로 덮는다.
   - 동작이 입력(파일, 줄, 항목)을 받으면, 둘 이상인 경우를 확인 하나로 덮는다.
   - 확인: `grep -n '지난 tasks의 같은 이름' plugins/plate/skills/plan/SKILL.md` → "6. 초안을 보여 주고 승인받는다"와 "적는 규칙"의 **조건**에 저마다 한 줄 이상. 그 줄들에 "둘 이상"도 있다
2. retro의 "4. task의 변경을 점검한다"가, 결정이나 완료 조건이 정한 동작이라도 지난 tasks의 같은 이름이 남은 경우나 입력이 둘 이상인 경우에 목표를 해치면 "문제 아님"으로 닫지 않고 5번에서 `경계 밖`으로 모으라고 한다. 기록의 "남은 것"에 그 꼴이 적혔을 때도 그렇다.
   - 확인: `grep -n '지난 tasks의 같은 이름' plugins/plate/skills/retro/SKILL.md` → "4. task의 변경을 점검한다"에 한 줄 이상. 그 줄에 `경계 밖`과 "둘 이상"이 있다
3. `tests/test_skill_rules.py`의 `PlanRulesTest`와 `RetroRulesTest`에 완료 조건 1·2의 글을 지키는 시험이 있고, 그 글을 지우면 실패한다.
   - 확인: `python3 -m unittest tests.test_skill_rules.PlanRulesTest tests.test_skill_rules.RetroRulesTest -v` → 새 시험 이름이 나오고 `OK`
   - 확인: 작업 트리를 `cp -R`로 `mktemp -d` 사본에 옮기고, 사본의 plan과 retro 본문에서 "지난 tasks의 같은 이름"이 든 줄을 지운 뒤 같은 명령을 돌린다 → 새 시험이 `FAIL`
   - 돌리지 않음: plan은 사용자에게 묻고 retro는 task 전체를 읽는 스킬이라, 고친 규칙대로 계획하고 회고하는지는 헤드리스로 끝까지 돌리지 않는다
4. ARCHITECTURE의 디렉터리 구조에 있는 `test_skill_rules.py` 줄이 새로 지키는 규칙을 적는다.
   - 확인: `grep -n 'test_skill_rules.py' docs/ARCHITECTURE.md` → 그 줄에 "지난 tasks의 같은 이름"이 있다
5. 테스트 묶음이 모두 통과한다(tasks 완료 조건 1).
   - 확인: `python3 -m unittest discover -s tests` → 마지막 줄이 `OK`

## 결정
- 이 task의 phase는 스킬 본문을 run이 넘긴 판으로 수행하고 확인한다. 고친 본문의 동작은 글과 그 글을 지키는 테스트로 보고, 헤드리스로 돌리지 않는다. 이유: AGENTS.md의 작업 규칙과 `docs/TOOLS.md`의 "세션 도중의 스킬 본문 고침" (추천안으로 정함)
