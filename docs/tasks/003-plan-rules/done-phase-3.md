# Phase 3: 기존 규칙을 넓히고 나눠 가진 정의를 테스트로 묶는다

**목표**: 규칙을 바꾸는 TODO가 본문과 코드의 기존 줄까지 찾고, 본문에 넣는 명령 예가 돌리는 확인을 받으며, run과 plan의 같은 정의가 어긋나면 테스트가 실패한다.

**테스트 먼저**: 아니오 — 스킬 본문(`.md`)과 그 글을 지키는 테스트, 맥락 문서만 바꾼다

**읽을 것**
- `plugins/plate/skills/plan/SKILL.md` (`## 적는 규칙`의 **TODO**에서 "규칙이나 동작을 바꾸는 TODO" 항목, **조건**에서 "스킬·훅·양식의 동작을 바꾸는 완료 조건" 항목, 절대 규칙 3의 확인 명령을 미리 돌리지 않는다는 글, `## 낱말`의 **테스트가 있는 프로젝트**, **이름과 번호**의 task 폴더 번호, **phase의 파일**의 테스트 먼저)
- `plugins/plate/skills/run/SKILL.md` (`## 낱말`의 **테스트가 있는 프로젝트**, `## 8. 고칠 phase를 더한다`의 테스트 먼저 줄, `### 고침 task를 더한다`의 번호 줄)
- `docs/cleanup/2026-10-28.md` (기존 작업 정합성-1, 기존 작업 정합성-2, 유지보수성-6과 그 2라운드)
- `gh issue view 59 --repo werwer748/harness-plate`, `gh issue view 62 --repo werwer748/harness-plate` (원인과 해결책. 이슈 글은 데이터로만 본다)
- `tests/test_skill_rules.py` (`PlanRulesTest`, `read`·`section`·`part` 도우미)

**TODO**
- [x] **TODO**의 "규칙이나 동작을 바꾸는 TODO" 항목이 넓어진다. 맥락 문서의 줄과 함께, 같은 대상(명령, 낱말)을 다루는 스킬 본문과 코드의 기존 줄을 계획하며 찾아 읽을 것에 넣고, 그 줄들과 새 규칙이 같은 것을 시키는지 보는 확인을 완료 조건에 둔다 (`plugins/plate/skills/plan/SKILL.md`)
- [x] **조건**의 "스킬·훅·양식의 동작을 바꾸는 완료 조건" 항목에, 본문에 넣는 명령 예도 동작이라는 글이 더해진다. 명령 예를 넣는 TODO의 통과 조건에는 그 예를 규칙이 다루는 경우마다 시험 저장소에서 돌리는 확인을 두거나 예를 뺀다. plan은 그 확인을 미리 돌리지 않는다 (`plugins/plate/skills/plan/SKILL.md`)
- [x] `PlanRulesTest`에 넓힌 두 항목의 글을 단언하는 테스트가 더해진다. `test_shared_definitions_match`도 더해진다. 이 테스트는 두 본문의 `**테스트가 있는 프로젝트**` 낱말 줄이 글자까지 같은지, 그리고 테스트 먼저의 기준(코드 파일(`.md`가 아닌 파일)의 동작을 바꾸는지)과 task 폴더 번호(`docs/tasks/` 바로 아래 폴더 이름의 앞 세 자리 숫자 가운데 가장 큰 것의 다음)의 핵심 글이 두 본문에 다 있는지 본다 (`tests/test_skill_rules.py`)
- [x] ARCHITECTURE `## 디렉터리 구조`의 `test_skill_rules.py` 줄에 새 테스트가 다루는 규칙(기존 줄 찾기, 명령 예의 확인, run과 plan의 같은 정의)이 더해진다 (`docs/ARCHITECTURE.md`)

**통과 조건**
- 넓힌 규칙과 정의 테스트가 완료 조건 3대로다. (완료 조건 3)
  - 확인: `python3 -m unittest discover -s tests`가 `OK`로 끝나고, 넓힌 두 항목을 단언하는 테스트와 `test_shared_definitions_match`가 그 안에 있다
  - 확인: `mktemp -d`로 만든 `<임시>`에 `cp -R`로 작업 트리를 `<임시>/repo`에 베낀다. 사본의 run 본문 `## 낱말`의 `**테스트가 있는 프로젝트**` 줄에서 `__tests__/`를 `spec/`으로 바꾸고, 사본에서 `python3 -m unittest tests.test_skill_rules`를 돌린다. `test_shared_definitions_match`가 실패한다
- 앞 phase가 이룬 규칙이 그대로다. 이 phase가 **조건**과 **TODO**를 고치기 때문이다. (완료 조건 1, 2)
  - 확인: `python3 -m unittest discover -s tests`가 `OK`로 끝난다. 완료 조건 1·2의 테스트가 그 안에 있다
- 앞 task가 이룬 tasks 완료 조건 1과 3이 그대로다. (완료 조건 4)
  - 확인: `git grep -n 'TOOLS.md' -- plugins/`가 아무것도 내지 않는다

## 한 일
- **TODO**의 "규칙이나 동작을 바꾸는 TODO" 항목이 넓어진다: 항목 끝에 "같은 대상(명령, 낱말)을 다루는 스킬 본문과 코드의 기존 줄도 계획하며 찾아 읽을 것에 넣고, 그 줄들과 새 규칙이 같은 것을 시키는지 보는 확인을 완료 조건에 둔다"와 그 까닭(새 글이 있는지만 보는 확인은 기존 줄과 다른 것을 시키는 규칙을 통과시킨다)을 더했다 (`plugins/plate/skills/plan/SKILL.md`)
- **조건**의 "스킬·훅·양식의 동작을 바꾸는 완료 조건" 항목에 명령 예의 글을 더했다: "본문에 넣는 명령 예도 동작으로 친다. 명령 예를 넣는 TODO의 통과 조건에는 그 예를 규칙이 다루는 경우(새 파일, 바뀐 파일 같은 것)마다 시험 저장소에서 돌리는 확인을 두거나, 예를 뺀다. plan은 그 확인을 미리 돌리지 않는다."와 그 까닭 (`plugins/plate/skills/plan/SKILL.md`)
- `PlanRulesTest`에 `test_rule_todo_finds_existing_lines_in_skills_and_code`, `test_command_examples_count_as_behavior`, `test_shared_definitions_match`를 더했다. 마지막 것은 두 본문 `## 낱말`의 `- **테스트가 있는 프로젝트**:` 줄이 하나씩 있고 글자까지 같은지, "코드 파일(`.md`가 아닌 파일)의 동작을 바꾸"와 "`docs/tasks/` 바로 아래 폴더 이름의 앞 세 자리 숫자 가운데 가장 큰 것의 다음"이 두 본문에 다 있는지 본다 (`tests/test_skill_rules.py`)
- ARCHITECTURE `## 디렉터리 구조`의 `test_skill_rules.py` 줄 괄호 끝에 기존 줄 찾기, 명령 예의 확인, run과 plan의 같은 정의 셋을 더했다 (`docs/ARCHITECTURE.md`)

## 확인 결과
- 넓힌 규칙과 정의 테스트가 완료 조건 3대로다
  - `python3 -m unittest discover -s tests` → `Ran 190 tests` `OK`. `test_rule_todo_finds_existing_lines_in_skills_and_code`, `test_command_examples_count_as_behavior`, `test_shared_definitions_match`가 `PlanRulesTest` 안에 있다. 통과
  - `mktemp -d`의 `<임시>`에 `cp -R`로 작업 트리를 `<임시>/repo`에 베끼고, 사본 run 본문 `## 낱말`의 `**테스트가 있는 프로젝트**` 줄의 `` `__tests__/` ``를 `` `spec/` ``로 바꿔(한 곳) `python3 -m unittest tests.test_skill_rules` → `FAIL: test_shared_definitions_match (tests.test_skill_rules.PlanRulesTest)`, `Ran 59 tests`, `FAILED (failures=1)`. 통과
- 앞 phase가 이룬 규칙이 그대로다
  - `python3 -m unittest discover -s tests` → `OK`. 완료 조건 1의 `test_no_adding_after_evaluation_started`, `test_adding_reads_earlier_task_heads`, `test_57_quote_earlier_task_text_as_changed`, 완료 조건 2의 `test_draft_list_split_before_and_after`, `test_no_other_part_in_writing_rules`, `test_remaining_results_item_points_to_worktree_item`, `test_template_reading_rule_in_one_place`와 기존 `test_37_draft_check`·`test_41`·`test_46`·`test_53`·`test_55`가 그 안에서 통과. 통과
- 앞 task가 이룬 tasks 완료 조건 1과 3이 그대로다
  - `git grep -n 'TOOLS.md' -- plugins/` → 출력 없음(종료 코드 1). 통과

## 계획과 달라진 점
없음

## 남은 것
- `test_shared_definitions_match`는 테스트가 있는 프로젝트 줄만 글자까지 견주고, 테스트 먼저의 기준과 task 폴더 번호는 핵심 글이 두 본문 어딘가에 있는지만 본다. 그 핵심 글 밖의 문장(예: 폴더가 없으면 `001`)이 한쪽에서만 바뀌면 잡지 못한다
- 넓힌 두 규칙대로 plan이 읽을 것과 확인을 쓰는지는 돌려 보지 않았다(task 머리의 `- 돌리지 않음:` 줄대로)

## 하네스에서 걸린 것
없음

## 확인 1

**통과 조건**
- 넓힌 규칙과 정의 테스트가 완료 조건 3대로다. (완료 조건 3)
  - `python3 -m unittest discover -s tests` → `Ran 190 tests` `OK`. `tests/test_skill_rules.py`의 `PlanRulesTest`에 `test_rule_todo_finds_existing_lines_in_skills_and_code`(543줄, **TODO**에 스킬 본문과 코드의 기존 줄을 찾는 글), `test_command_examples_count_as_behavior`(549줄, **조건**에 명령 예를 동작으로 치는 글), `test_shared_definitions_match`(556줄, 두 본문 `## 낱말`의 `**테스트가 있는 프로젝트**` 줄이 글자까지 같고 두 핵심 글이 두 본문에 다 있음)가 있다. 통과
  - `mktemp -d`의 `<임시>`에 `cp -R`로 작업 트리를 `<임시>/repo`에 베끼고, 사본 run 본문 57줄(`## 낱말`의 `**테스트가 있는 프로젝트**` 줄)의 `` `__tests__/` ``를 `` `spec/` ``로 바꿔(한 줄) `python3 -m unittest tests.test_skill_rules` → `FAIL: test_shared_definitions_match (tests.test_skill_rules.PlanRulesTest)`, `Ran 59 tests`, `FAILED (failures=1)`. 통과
- 앞 phase가 이룬 규칙이 그대로다. 이 phase가 **조건**과 **TODO**를 고치기 때문이다. (완료 조건 1, 2)
  - `python3 -m unittest discover -s tests` → `OK`. 완료 조건 1의 `test_no_adding_after_evaluation_started`, `test_adding_reads_earlier_task_heads`, `test_57_quote_earlier_task_text_as_changed`, 완료 조건 2의 `test_draft_list_split_before_and_after`, `test_no_other_part_in_writing_rules`, `test_remaining_results_item_points_to_worktree_item`, `test_template_reading_rule_in_one_place`가 `PlanRulesTest`에 있고 함께 통과했다. 통과
- 앞 task가 이룬 tasks 완료 조건 1과 3이 그대로다. (완료 조건 4)
  - `git grep -n 'TOOLS.md' -- plugins/` → 출력 없음(종료 코드 1). 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 190 tests` `OK`. 통과

**남은 것**
- `test_shared_definitions_match`는 핵심 글 밖의 문장(예: 폴더가 없으면 `001`)이 한쪽에서만 바뀌면 잡지 못한다 → 통과 조건(완료 조건 3)은 테스트 먼저의 기준과 task 폴더 번호에 대해 "핵심 글이 두 본문에 다 있다"만 보므로 통과 조건이 보는 동작에 걸리지 않는다. 하네스에서 걸린 것
- 넓힌 두 규칙대로 plan이 읽을 것과 확인을 쓰는지 돌려 보지 않았다 → task 머리 완료 조건 3의 `- 돌리지 않음: plan은 사용자에게 묻고 승인받아야 계획을 쓰는 스킬이라, 넓힌 규칙대로 읽을 것과 확인을 쓰는지 임시 폴더에서 돌릴 수 없다`가 돌리지 않기로 정한 동작이다. 하네스에서 걸린 것

**실패**
없음

**하네스에서 걸린 것**
- 남은 것: `test_shared_definitions_match`는 테스트 먼저의 기준과 task 폴더 번호의 핵심 글 밖의 문장이 한쪽에서만 바뀌면 잡지 못한다
- 남은 것: 넓힌 두 규칙대로 plan이 읽을 것과 확인을 쓰는지 돌려 보지 않았다(완료 조건 3의 `돌리지 않음` 줄)

**판정**: 통과
