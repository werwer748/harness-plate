# 회고

## 회고 1

**확인**
- plan의 "6. 초안을 보여 주고 승인받는다"의 초안 전 점검 목록과 "적는 규칙"의 **조건**이 이름·번호로 찾는 동작은 지난 tasks의 같은 이름이 남은 경우를, 입력을 받는 동작은 둘 이상인 경우를 확인 하나로 덮게 한다
  - `grep -n '지난 tasks의 같은 이름' plugins/plate/skills/plan/SKILL.md` → 114행("6. 초안을 보여 주고 승인받는다", 101~135행 안, "초안을 보여 준 뒤에는" 앞의 점검 목록), 263행("적는 규칙"의 **조건**, 257행부터). 두 줄 모두 "둘 이상"이 있음(`grep -c` 2). 통과
- retro의 "4. task의 변경을 점검한다"가 결정이나 완료 조건이 정한 동작이라도 그 경우에 목표를 해치면 "문제 아님"으로 닫지 않고 5번에서 `경계 밖`으로 모으게 한다
  - `grep -n '지난 tasks의 같은 이름' plugins/plate/skills/retro/SKILL.md` → 79행("4. task의 변경을 점검한다", 64~84행 안). 그 줄에 `경계 밖`과 "둘 이상"이 있음(`grep -c` 1). 기록의 "남은 것"에 그 꼴이 적힌 줄도 그렇다는 글도 같은 줄에 있음. 통과
- `PlanRulesTest`와 `RetroRulesTest`에 완료 조건 1·2의 글을 지키는 시험이 있고, 그 글을 지우면 실패한다
  - `python3 -m unittest tests.test_skill_rules.PlanRulesTest tests.test_skill_rules.RetroRulesTest -v` → `test_80_repeated_names_and_multiple_inputs_covered ... ok`, `test_80_decided_behavior_with_repeated_names_goes_out_of_bounds ... ok`, `Ran 27 tests`, `OK`. 통과
  - `tmp=$(mktemp -d); cp -R . "$tmp/repo"` 뒤 사본의 plan·retro 본문에서 `grep -v '지난 tasks의 같은 이름'`으로 그 줄을 지우고(남은 수 0, 0) 같은 명령 → 새 시험 둘이 `FAIL`(plan 시험의 subTest `6`, `조건`과 본 시험, retro 시험), `FAILED (failures=4)`. 사본은 지움. 통과
  - 돌리지 않음: 고친 규칙대로 plan이 계획하고 retro가 회고하는지는 완료 조건의 `돌리지 않음` 줄대로 헤드리스로 돌리지 않음
- ARCHITECTURE의 디렉터리 구조에 있는 `test_skill_rules.py` 줄이 새로 지키는 규칙을 적는다
  - `grep -n 'test_skill_rules.py' docs/ARCHITECTURE.md` → 40행, 그 줄에 "지난 tasks의 같은 이름"이 있음(`grep -c` 1). 통과
- 테스트 묶음이 모두 통과한다
  - `python3 -m unittest discover -s tests` → `Ran 252 tests`, 마지막 줄 `OK`. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 252 tests`, `OK`. 통과

**남은 것**
- phase 1: retro의 회고 절 양식은 "남은 것" 판정 값을 `문제 | 문제 아님` 둘로 두어, 판정 칸에 무엇을 적을지는 까닭의 글로만 갈린다 → 문제 아님 (새 4번 문단이 "그 줄의 판정에는 까닭에 `경계 밖`을 적는다"고 정하고 양식의 까닭 칸이 그 자리를 두어, 판정 값을 늘리지 않아도 목표("경계 밖으로 올린다")가 선다. 범위·맥락 문서·결함에 걸리지 않는다)
- phase 1: 고친 본문대로 plan이 계획하고 retro가 회고하는지는 헤드리스로 돌리지 않았다 → 문제 아님 (task 머리 결정과 완료 조건 3의 `돌리지 않음` 줄이 정한 것이다. task의 커밋이 바꾼 plan 114·263행과 retro 79행을 직접 읽어 목표의 두 경우와 `경계 밖`으로 모음이 적혀 있음을 봄)

**문제**
없음

**판정**: 통과
