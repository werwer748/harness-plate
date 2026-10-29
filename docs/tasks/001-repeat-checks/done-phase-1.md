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
- [x] plan의 초안 전 점검 목록에 항목이 더해진다. 동작이 이름이나 번호로 커밋, 파일, 브랜치를 찾으면 지난 tasks의 같은 이름이 남은 경우를, 입력을 받으면 둘 이상인 경우를 확인 하나씩으로 덮었는지 보고, 없으면 더하게 한다 (`plugins/plate/skills/plan/SKILL.md`)
- [x] plan의 "적는 규칙"의 **조건**에 같은 뜻의 규칙이 더해진다. 기존의 "규칙이 다루는 경우마다"(명령 예에만 대던 것)와 같은 것을 시키고 동작 일반으로 넓힌다 (`plugins/plate/skills/plan/SKILL.md`)
- [x] retro 4번에 규칙이 더해진다. 결정이나 완료 조건이 정한 동작이라도 지난 tasks의 같은 이름이 남은 경우나 입력이 둘 이상인 경우에 목표를 해치면 "문제 아님"으로 닫지 않고 5번에서 `경계 밖`으로 모은다. 기록의 "남은 것" 줄 판정에도 걸린다 (`plugins/plate/skills/retro/SKILL.md`)
- [x] `PlanRulesTest`와 `RetroRulesTest`에 위 세 글을 제 절에서 지키는 시험이 더해지고, ARCHITECTURE의 `test_skill_rules.py` 줄에 그 규칙이 더해진다 (`tests/test_skill_rules.py`, `docs/ARCHITECTURE.md`)

**통과 조건**
- task 머리의 완료 조건 1~5가 참이다.
  - 확인: `grep -n '지난 tasks의 같은 이름' plugins/plate/skills/plan/SKILL.md plugins/plate/skills/retro/SKILL.md` → plan의 "6. 초안을 보여 주고 승인받는다"와 "적는 규칙"의 **조건**, retro의 "4. task의 변경을 점검한다"에 저마다 한 줄 이상. plan의 줄에 "둘 이상"이 있고, retro의 줄에 `경계 밖`과 "둘 이상"이 있다
  - 확인: `python3 -m unittest tests.test_skill_rules.PlanRulesTest tests.test_skill_rules.RetroRulesTest -v` → 새 시험 이름이 나오고 `OK`
  - 확인: 작업 트리를 `cp -R`로 `mktemp -d` 사본에 옮기고, 사본의 두 본문에서 "지난 tasks의 같은 이름"이 든 줄을 지운 뒤 같은 명령을 돌린다 → 새 시험이 `FAIL`
  - 확인: `grep -n 'test_skill_rules.py' docs/ARCHITECTURE.md` → 그 줄에 "지난 tasks의 같은 이름"이 있다
  - 확인: `python3 -m unittest discover -s tests` → 마지막 줄이 `OK`

## 한 일
- plan의 초안 전 점검 목록에 항목이 더해진다: "돌리는 확인을 둔 완료 조건마다 … 갈래" 항목 바로 뒤에, 동작이 이름이나 번호로 커밋, 파일, 브랜치를 찾으면 지난 tasks의 같은 이름이 남은 경우를, 입력(파일, 줄, 항목)을 받으면 둘 이상인 경우를 저마다 확인 하나로 덮었는지 보고 없으면 더하게 하는 항목을 더함 (`plugins/plate/skills/plan/SKILL.md`)
- plan의 "적는 규칙"의 **조건**에 같은 뜻의 규칙이 더해진다: 갈래 규칙 바로 뒤에 같은 두 경우를 덮으라는 줄을 더하고, 명령 예에만 대던 "규칙이 다루는 경우마다"를 동작 일반으로 넓힌 것이라고 적음 (`plugins/plate/skills/plan/SKILL.md`)
- retro 4번에 규칙이 더해진다: 경계 밖 문단 뒤에, 결정이나 완료 조건이 정한 동작이라도 지난 tasks의 같은 이름이 남은 경우나 입력이 둘 이상인 경우에 목표를 해치면 "문제 아님"으로 닫지 않고 5번에서 `경계 밖`으로 모으고, 기록의 "남은 것"에 그 꼴이 적힌 줄도 그렇다는 문단을 더함 (`plugins/plate/skills/retro/SKILL.md`)
- 테스트와 ARCHITECTURE: `PlanRulesTest.test_80_repeated_names_and_multiple_inputs_covered`(6번의 초안 전 점검 부분과 **조건**에서 "지난 tasks의 같은 이름"이 든 줄에 이름·번호, 커밋·파일·브랜치, 둘 이상, 확인 하나로가 있는지)와 `RetroRulesTest.test_80_decided_behavior_with_repeated_names_goes_out_of_bounds`(4번의 그 줄에 `경계 밖`, 둘 이상, "남은 것"이 있는지)를 더하고, ARCHITECTURE의 `test_skill_rules.py` 줄 괄호 끝에 이 규칙을 더함 (`tests/test_skill_rules.py`, `docs/ARCHITECTURE.md`)

## 확인 결과
- task 머리의 완료 조건 1~5가 참이다.
  - `grep -n '지난 tasks의 같은 이름' plugins/plate/skills/plan/SKILL.md plugins/plate/skills/retro/SKILL.md` → plan 114행(6번의 초안 전 점검 목록), plan 263행(적는 규칙의 **조건**), retro 79행(4번). plan의 두 줄에 "둘 이상", retro 줄에 `경계 밖`과 "둘 이상"이 있음. 통과
  - `python3 -m unittest tests.test_skill_rules.PlanRulesTest tests.test_skill_rules.RetroRulesTest -v` → `test_80_repeated_names_and_multiple_inputs_covered ... ok`, `test_80_decided_behavior_with_repeated_names_goes_out_of_bounds ... ok`, `Ran 27 tests`, `OK`. 통과
  - `tmp=$(mktemp -d); cp -R . "$tmp/repo"` 뒤 사본의 두 본문에서 `grep -v '지난 tasks의 같은 이름'`으로 그 줄을 지우고(남은 수 0) 같은 명령 → `test_80_repeated_names_and_multiple_inputs_covered ... FAIL`, `test_80_decided_behavior_with_repeated_names_goes_out_of_bounds ... FAIL`, `FAILED (failures=4)`(plan 시험의 subTest 둘과 본 시험). 사본은 지움. 통과
  - `grep -n 'test_skill_rules.py' docs/ARCHITECTURE.md` → 40행, 그 줄에 "지난 tasks의 같은 이름"이 있음(`grep -c` 1). 통과
  - `python3 -m unittest discover -s tests` → `Ran 252 tests`, 마지막 줄 `OK`. 통과

## 계획과 달라진 점
없음

## 남은 것
- retro의 회고 절 양식은 "남은 것" 판정 값을 `문제 | 문제 아님` 둘로 두고 있어 바꾸지 않았다(TODO 밖). 새 규칙은 그 줄의 판정 까닭에 `경계 밖`을 적고 5번에서 `경계 밖`으로 모으라고만 한다. 판정 값 자체에 `경계 밖`을 두지 않아, 회고하는 쪽이 판정 칸에 무엇을 적을지는 까닭의 글로만 갈린다.
- 고친 본문대로 plan이 계획하고 retro가 회고하는지는 헤드리스로 돌리지 않았다(task 머리의 결정과 "돌리지 않음" 줄대로). 테스트는 글이 제 절에 있는지만 본다.

## 하네스에서 걸린 것
없음

## 확인 1

**통과 조건**
- task 머리의 완료 조건 1~5가 참이다.
  - `grep -n '지난 tasks의 같은 이름' plugins/plate/skills/plan/SKILL.md plugins/plate/skills/retro/SKILL.md` → plan 114행("6. 초안을 보여 주고 승인받는다", 101~135행 안), plan 263행("적는 규칙"의 **조건**, 257~283행 안), retro 79행("4. task의 변경을 점검한다", 64~84행 안). plan의 두 줄에 "둘 이상"이 있고, retro 줄에 `경계 밖`과 "둘 이상"이 있다. 통과
  - `python3 -m unittest tests.test_skill_rules.PlanRulesTest tests.test_skill_rules.RetroRulesTest -v` → `test_80_repeated_names_and_multiple_inputs_covered ... ok`, `test_80_decided_behavior_with_repeated_names_goes_out_of_bounds ... ok`, `Ran 27 tests`, `OK`. 통과
  - `tmp=$(mktemp -d); cp -R . "$tmp/repo"` 뒤 사본의 plan·retro 본문에서 `grep -v '지난 tasks의 같은 이름'`으로 그 줄을 지우고(남은 수 0) 같은 명령 → 새 시험 둘이 `FAIL`, `FAILED (failures=4)`. 사본은 지움. 통과
  - `grep -n 'test_skill_rules.py' docs/ARCHITECTURE.md` → 그 줄에 "지난 tasks의 같은 이름"이 있다(`grep -c` 1). 통과
  - `python3 -m unittest discover -s tests` → `Ran 252 tests`, 마지막 줄 `OK`. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 252 tests`, `OK`. 통과

**남은 것**
- retro의 회고 절 양식이 "남은 것" 판정 값을 `문제 | 문제 아님` 둘로 두어, 판정 칸에 무엇을 적을지가 까닭의 글로만 갈린다 → 통과 조건(완료 조건 2)이 보는 것은 4번이 "문제 아님"으로 닫지 않고 5번에서 `경계 밖`으로 모으라고 하는지이고, 그 글은 있다. 양식의 판정 값은 TODO 밖이라 걸리지 않는다. 하네스에서 걸린 것
- 고친 본문대로 plan이 계획하고 retro가 회고하는지 헤드리스로 돌리지 않았다 → task 머리 완료 조건 3의 `- 돌리지 않음: plan은 사용자에게 묻고 retro는 task 전체를 읽는 스킬이라, 고친 규칙대로 계획하고 회고하는지는 헤드리스로 끝까지 돌리지 않는다` 줄이 돌리지 않기로 정한 동작이다. 하네스에서 걸린 것

**실패**
없음

**하네스에서 걸린 것**
- 남은 것: retro의 회고 절 양식의 "남은 것" 판정 값이 `문제 | 문제 아님` 둘뿐이라, 새 규칙의 `경계 밖`을 판정 칸에 어떻게 적을지가 까닭의 글로만 갈린다(`plugins/plate/skills/retro/SKILL.md`)
- 남은 것: 고친 plan·retro 본문의 동작은 헤드리스로 돌려 보지 않았다(task 머리 완료 조건 3의 `돌리지 않음` 줄)

**판정**: 통과
