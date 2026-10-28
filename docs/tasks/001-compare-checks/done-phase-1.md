# Phase 1: plan 본문과 테스트와 문서를 고친다

**목표**: plan 본문에 #65의 해결이 더해지고, 그 규칙 글의 테스트가 더해지고, 버전과 `docs/ARCHITECTURE.md`의 테스트 줄이 맞춰진다.

**테스트 먼저**: 아니오 — 고치는 것은 스킬 본문(`.md`)이고, 더하는 테스트는 그 글이 있는지를 볼 뿐 코드의 동작을 바꾸지 않는다

**읽을 것**
- `plugins/plate/skills/plan/SKILL.md`의 "6. 초안을 보여 주고 승인받는다"와 적는 규칙의 "조건" 절. 고칠 자리는 `- 확인은 돌릴 명령과 기대 결과를 우선한다.`로 시작하는 항목이다
- `gh issue view 65 --repo werwer748/harness-plate` (원인과 해결책)
- `tests/test_skill_rules.py`의 모듈 docstring, `section`·`part` 도우미, `PlanRulesTest` (테스트의 꼴)
- `docs/ARCHITECTURE.md` 디렉터리 구조의 `test_skill_rules.py` 줄 (맞출 줄)
- `plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json` (버전 줄)

**TODO**
- [x] 적는 규칙 "조건"의 `- 확인은 돌릴 명령과 기대 결과를 우선한다.`로 시작하는 항목 끝에 #65의 해결이 이어 더해진다: `값을 뽑아 견주는 확인은 뽑는 명령(또는 패턴)과 견주는 법을 적는다`, `적을 수 없으면 읽어서 견줄 자리를 적는다`, 그리고 명령이 없으면 확인하는 쪽마다 다르게 짜 결과가 갈린다는 까닭. 새 항목을 따로 만들지 않는다 (`plugins/plate/skills/plan/SKILL.md`)
- [x] 6번 "초안을 보여 주기 전에 아래를 본다." 목록에 `값을 뽑아 견주는 확인에 뽑는 명령과 견주는 법이 있는지 본다`로 시작하는 점검 항목이 더해진다. 없으면 명령을 더하거나 읽어서 견줄 자리를 적는다는 것도 함께 적는다. 세 글은 본문에 저마다 한 번만 나온다 (`plugins/plate/skills/plan/SKILL.md`)
- [x] `PlanRulesTest`에 `test_65_comparison_checks_name_extract_command`가 더해진다. 적는 규칙 "조건" 절에 앞의 두 글이 있는지 보고, 6번 절에 점검 글이 있는지 본다. 모듈 docstring의 plan 목록에 #65가 더해진다 (`tests/test_skill_rules.py`)
- [x] 두 매니페스트의 버전이 0.19.0에서 0.20.0으로 바뀐다 (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)
- [x] 디렉터리 구조의 `test_skill_rules.py` 줄의 규칙 목록에 "plan의 값을 뽑아 견주는 확인이 뽑는 명령과 견주는 법을 적음"이 더해진다 (`docs/ARCHITECTURE.md`)

**통과 조건**
- 완료 조건 1이 참이다
  - 확인: `grep -cF '<글>' plugins/plate/skills/plan/SKILL.md`를 완료 조건 1의 세 글마다 돌리면 저마다 `1`이다. 하나라도 `1`이 아니면 실패
  - 확인: `grep -F '- 확인은 돌릴 명령과 기대 결과를 우선한다.' plugins/plate/skills/plan/SKILL.md`가 내는 한 줄에 `값을 뽑아 견주는 확인은 뽑는 명령(또는 패턴)과 견주는 법을 적는다`와 `적을 수 없으면 읽어서 견줄 자리를 적는다`가 모두 든다. 줄이 하나가 아니거나 한 글이라도 빠지면 실패
- 완료 조건 2가 참이다
  - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
  - 확인: `mktemp -d`로 만든 폴더에 작업 트리의 `plugins`와 `tests`를 `cp -R`로 복사한다. 사본의 `plugins/plate/skills/plan/SKILL.md`에 글 `값을 뽑아 견주는 확인은 뽑는 명령(또는 패턴)과 견주는 법을 적는다`가 한 번 있는지 본다(없으면 실패). 그 글을 빈 글로 바꾸고 사본에서 `python3 -m unittest discover -s tests`를 돌리면 출력에 `FAIL: test_65_comparison_checks_name_extract_command` 줄이 있다
  - 확인: 같은 방법으로 새로 복사해 글 `값을 뽑아 견주는 확인에 뽑는 명령과 견주는 법이 있는지 본다`를 빈 글로 바꾸면 출력에 `FAIL: test_65_comparison_checks_name_extract_command` 줄이 있다
- 완료 조건 3이 참이다
  - 확인: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json`의 두 줄이 모두 `0.20.0`
  - 확인: `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
  - 확인: `grep -c '값을 뽑아 견주는 확인' docs/ARCHITECTURE.md`가 `1` 이상이고 그 줄이 `test_skill_rules.py` 줄이다. `sed -n '1,8p' tests/test_skill_rules.py`의 plan 목록에 `#65`가 있다. 하나라도 아니면 실패
- 모든 스킬의 description이 1024자 이하다
  - 확인: `python3 -m unittest discover -s tests`의 `test_description_at_most_1024_chars`가 통과한다(위 `OK`에 든다)

## 한 일
- 적는 규칙 "조건"의 `- 확인은 돌릴 명령과 기대 결과를 우선한다.` 항목: 끝에 `값을 뽑아 견주는 확인은 뽑는 명령(또는 패턴)과 견주는 법을 적는다`(예: `grep -o`로 뽑아 정렬해 `diff`로 견줌), `적을 수 없으면 읽어서 견줄 자리를 적는다`, 명령 없이 적으면 수행·확인·코드 평가가 뽑는 법을 저마다 짜 결과가 갈린다는 까닭을 이어 적었다. 새 항목은 만들지 않았다 (`plugins/plate/skills/plan/SKILL.md`)
- 6번 "초안을 보여 주기 전에 아래를 본다." 목록: `HEAD` 점검 항목 앞에 `값을 뽑아 견주는 확인에 뽑는 명령과 견주는 법이 있는지 본다. 없으면 명령을 더하거나, 명령으로 뽑을 수 없으면 읽어서 견줄 자리를 적는다.`를 더했다 (`plugins/plate/skills/plan/SKILL.md`)
- `PlanRulesTest`에 `test_65_comparison_checks_name_extract_command`를 더하고 모듈 docstring의 plan 목록에 `#65`를 더했다 (`tests/test_skill_rules.py`)
- 두 매니페스트의 버전을 0.19.0에서 0.20.0으로 바꿨다 (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)
- 디렉터리 구조의 `test_skill_rules.py` 줄 규칙 목록 끝에 "plan의 값을 뽑아 견주는 확인이 뽑는 명령과 견주는 법을 적음"을 더했다 (`docs/ARCHITECTURE.md`)

## 확인 결과
- 완료 조건 1이 참이다
  - 세 글마다 `grep -cF '<글>' plugins/plate/skills/plan/SKILL.md` → 저마다 `1`. 통과
  - `grep -F -- '- 확인은 돌릴 명령과 기대 결과를 우선한다.' plugins/plate/skills/plan/SKILL.md` → 한 줄, 그 줄에 두 글이 저마다 `grep -cF`로 `1`. 통과
- 완료 조건 2가 참이다
  - `python3 -m unittest discover -s tests` → `Ran 193 tests in 17.015s` / 마지막 줄 `OK`. 통과
  - `mktemp -d` 사본(`cp -R plugins tests`)에서 `값을 뽑아 견주는 확인은 뽑는 명령(또는 패턴)과 견주는 법을 적는다`가 1번 있음을 보고 빈 글로 바꿔 돌림 → `FAIL: test_65_comparison_checks_name_extract_command (test_skill_rules.PlanRulesTest)`. 통과
  - 새 사본에서 `값을 뽑아 견주는 확인에 뽑는 명령과 견주는 법이 있는지 본다`(1번 있음)를 빈 글로 바꿔 돌림 → `FAIL: test_65_comparison_checks_name_extract_command (test_skill_rules.PlanRulesTest)`. 통과
- 완료 조건 3이 참이다
  - `grep -h '"version"' …` → `"version": "0.20.0",` 두 줄. 통과
  - `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
  - `grep -c '값을 뽑아 견주는 확인' docs/ARCHITECTURE.md` → `1`, 그 줄이 `└── test_skill_rules.py` 줄. `sed -n '1,8p' tests/test_skill_rules.py`의 plan 목록 → `plan의 #37·#41·#46·#52·#53·#55·#56·#57·#65`. 통과
- 모든 스킬의 description이 1024자 이하다
  - `python3 -m unittest discover -s tests`가 `OK`이고 `test_description_at_most_1024_chars`의 FAIL/ERROR 줄 없음. 통과

## 계획과 달라진 점
없음

## 남은 것
- 고친 규칙대로 plan이 초안을 적는지는 돌려 보지 않았다(task 머리의 `- 돌리지 않음` 줄대로).

## 하네스에서 걸린 것
없음

## 확인 1

**통과 조건**
- 완료 조건 1이 참이다
  - 세 글마다 `grep -cF '<글>' plugins/plate/skills/plan/SKILL.md` → `1`, `1`, `1`. 통과
  - `grep -F -- '- 확인은 돌릴 명령과 기대 결과를 우선한다.' plugins/plate/skills/plan/SKILL.md` → 한 줄, 그 줄에 두 글이 저마다 `grep -cF`로 `1`. 통과
- 완료 조건 2가 참이다
  - `python3 -m unittest discover -s tests` → `Ran 193 tests in 16.846s` / 마지막 줄 `OK`. 통과
  - `mktemp -d` 사본(`cp -R plugins tests`)에서 `값을 뽑아 견주는 확인은 뽑는 명령(또는 패턴)과 견주는 법을 적는다`가 1번 있음을 보고 빈 글로 바꿔 돌림 → `FAIL: test_65_comparison_checks_name_extract_command (test_skill_rules.PlanRulesTest)`. 통과
  - 새 사본에서 `값을 뽑아 견주는 확인에 뽑는 명령과 견주는 법이 있는지 본다`(1번 있음)를 빈 글로 바꿔 돌림 → `FAIL: test_65_comparison_checks_name_extract_command (test_skill_rules.PlanRulesTest)`. 통과
- 완료 조건 3이 참이다
  - `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → `"version": "0.20.0",` 두 줄. 통과
  - `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
  - `grep -c '값을 뽑아 견주는 확인' docs/ARCHITECTURE.md` → `1`, 그 줄이 `└── test_skill_rules.py` 줄. `sed -n '1,8p' tests/test_skill_rules.py` → 3행 plan 목록에 `#65`. 통과
- 모든 스킬의 description이 1024자 이하다
  - `python3 -m unittest discover -s tests` → `OK`(`test_description_at_most_1024_chars` 포함, FAIL/ERROR 없음). 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 193 tests`, `OK`. 통과

**남은 것**
- 고친 규칙대로 plan이 초안을 적는지는 돌려 보지 않았다 → task 머리 완료 조건 1의 `- 돌리지 않음: plan은 사람에게 묻고 초안마다 승인을 받는 스킬이라, 고친 규칙대로 초안이 적히는지는 여러 턴의 답을 이어야 닿는다`가 돌리지 않기로 정한 동작이다. 하네스에서 걸린 것

**실패**
- 없음

**하네스에서 걸린 것**
- 남은 것: 고친 규칙대로 plan이 초안을 적는지는 돌려 보지 않았다(완료 조건 1의 `돌리지 않음` 줄이 정한 것)

**판정**: 통과
