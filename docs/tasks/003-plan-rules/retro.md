# 회고

## 회고 1

**확인**
- 1. 더하는 경우가 이렇게 바뀐다. (신뢰성-4, 신뢰성-5)
  - `python3 -m unittest discover -s tests` → `Ran 190 tests` / `OK`. `python3 -m unittest -v tests.test_skill_rules`에 `test_no_adding_after_evaluation_started`(1번 절에 `` `docs/tasks/review.md`나 `docs/tasks/eval.md`가 있으면 ``과 "task로 더할지 묻지 않고 아무것도 쓰지 않고 끝난다"), `test_adding_reads_earlier_task_heads`(task 머리를 읽는 글, phase 파일을 읽지 않는 글, "내용은 읽지 않는다" 없음), `test_57_quote_earlier_task_text_as_changed`가 모두 `ok`. 통과
  - `docs/ARCHITECTURE.md` `## 데이터 흐름`의 계획 단계를 읽음 → "tasks가 진행 중이면 새 요청을 지금 tasks에 task로 더할지 묻고, 더하면 이미 있는 task 머리를 읽는다"와 "docs/tasks/review.md나 eval.md가 있어 tasks 끝의 평가가 시작된 tasks면 더할지 묻지 않고 더하지 않는다고 알리고 끝난다" 두 갈래가 있다. 통과
- 2. 6번 목록과 적는 규칙이 되풀이 없이 읽힌다. (유지보수성-2, 유지보수성-4, 유지보수성-5, 유지보수성-12)
  - `python3 -m unittest discover -s tests` → `OK`. `test_draft_list_split_before_and_after`, `test_no_other_part_in_writing_rules`, `test_remaining_results_item_points_to_worktree_item`, `test_template_reading_rule_in_one_place`(PlanRulesTest)와 `test_37_draft_check`, `test_41_conditions_from_earlier_phase_output`, `test_46_rerun_results_compared_by_body_hash`, `test_53_draft_check_for_run_scenes`, `test_55_checks_run_on_uncommitted_worktree`, `test_57_quote_earlier_task_text_as_changed`가 모두 `ok`. 통과
  - plan `## 2. 맥락 문서를 읽는다`의 첫 문단을 읽음 → "문서 지도에 적힌 위치의 맥락 문서를 모두 읽는다. 지도에 행이 더해져 있으면 그 문서도 읽는다."가 그대로 있다. 통과
- 3. 기존 규칙이 넓어지고, 나눠 가진 정의가 어긋나면 테스트가 잡는다. (기존 작업 정합성-1, 기존 작업 정합성-2, 유지보수성-6)
  - `python3 -m unittest discover -s tests` → `OK`. `test_rule_todo_finds_existing_lines_in_skills_and_code`, `test_command_examples_count_as_behavior`, `test_shared_definitions_match`가 `PlanRulesTest`에서 `ok`. 통과
  - `mktemp -d`의 `<임시>`에 `cp -R`로 작업 트리를 `<임시>/repo`에 베끼고, 사본 run 본문 57줄(`## 낱말`의 `- **테스트가 있는 프로젝트**:` 줄)만 `` `__tests__/` ``를 `` `spec/` ``로 바꿔(`git diff --stat` 한 줄) `python3 -m unittest tests.test_skill_rules` → `FAIL: test_shared_definitions_match (tests.test_skill_rules.PlanRulesTest)`, `Ran 59 tests`, `FAILED (failures=1)`. 통과
- 4. 앞 task가 이룬 tasks 완료 조건 1과 3이 이 task의 마지막 커밋에서도 참이다.
  - `python3 -m unittest discover -s tests` → `Ran 190 tests` / `OK`. 통과
  - `git grep -n 'TOOLS.md' -- plugins/` → 출력 없음(종료 코드 1). 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 190 tests in 17.262s` / `OK`. 통과

**남은 것**
- phase 1: `tests/test_skill_rules.py` 머리 docstring의 이슈 목록은 고치지 않았다 → 문제 아님 (task 머리와 phase 1 TODO가 docstring을 고치라고 하지 않았고, 새 테스트마다 주석에 cleanup 발견을 출처로 적었다. 넷 가운데 어디에도 걸리지 않는다)
- phase 2: 뒤 목록의 첫 항목 글("초안을 보여 주기 전에 받은 승인은 승인이 아니다")에 "초안을 보여 주기 전에"가 남는다 → 문제 아님 (완료 조건 2는 미리 받은 승인 규칙을 뒤 목록에 두라고 했고, 머리말을 한 번 적을 곳을 앞 목록 머리로 정했다. 그 항목은 점검이 아니라 승인 규칙의 글이다)
- phase 2: `test_template_reading_rule_in_one_place`가 `RunRulesTest`와 `PlanRulesTest`에 같은 이름으로 있다 → 문제 아님 (`python3 -m unittest -v tests.test_skill_rules`에서 두 클래스의 것이 저마다 `ok`로 돈다)
- phase 3: `test_shared_definitions_match`는 테스트 먼저의 기준과 task 폴더 번호의 핵심 글 밖의 문장이 한쪽에서만 바뀌면 잡지 못한다 → 문제 아님 (완료 조건 3이 그 둘은 "핵심 글이 두 본문에 다 있다"까지만 보게 정했다)
- phase 3: 넓힌 두 규칙대로 plan이 읽을 것과 확인을 쓰는지 돌려 보지 않았다 → 문제 아님 (task 머리 완료 조건 3의 `- 돌리지 않음:` 줄이 돌리지 않기로 정한 동작이다)

**문제**
없음

**판정**: 통과
