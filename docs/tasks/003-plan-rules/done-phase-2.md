# Phase 2: 6번 목록과 적는 규칙의 되풀이를 걷는다

**목표**: 6번 목록이 초안 전의 점검과 초안 뒤의 규칙으로 나뉘고, `**그 밖**` 절과 남은 결과 항목의 되풀이가 걷히고, 양식을 읽는 법이 낱말에 한 번 있다.

**테스트 먼저**: 아니오 — 스킬 본문(`.md`)과 그 글을 지키는 테스트, 맥락 문서만 바꾼다

**읽을 것**
- `plugins/plate/skills/plan/SKILL.md` (`## 낱말`, `## 2. 맥락 문서를 읽는다`, `## 5. 질문한다`의 "요청이나 맥락 문서에 답이 있으면 묻지 않는다", `## 6. 초안을 보여 주고 승인받는다`의 목록 전체, `## 계획 파일의 양식`의 첫 문단, `## 적는 규칙`의 **조건**에서 남은 결과 항목과 그다음의 작업 트리 항목, `**그 밖**`)
- `plugins/plate/skills/run/SKILL.md` (`## 낱말`: 앞 task 002-run-rules의 phase 4가 더한, 양식을 읽는 법 세 문장을 담은 낱말. 그 이름을 쓴다)
- `docs/cleanup/2026-10-28.md` (유지보수성-2, 유지보수성-4, 유지보수성-5, 유지보수성-12와 그 2라운드, 버린 것의 유지보수성-1·유지보수성-3)
- `tests/test_skill_rules.py` (`PlanRulesTest` 전체: 6번 절과 **조건**의 글을 단언하는 테스트들)

**TODO**
- [x] 6번 목록이 둘로 나뉜다. 앞 목록은 초안을 보여 주기 전의 점검으로, 목록 머리에 "초안을 보여 주기 전에"를 한 번 적고 항목마다의 같은 머리말을 뺀다. 뒤 목록은 초안 뒤의 규칙이다(미리 받은 승인, 고칠 곳, 분명하지 않은 답, 마지막 task까지 7번으로 가지 않음). 점검 항목의 글은 머리말 말고는 바꾸지 않는다 (`plugins/plate/skills/plan/SKILL.md`)
- [x] `## 적는 규칙`의 `**그 밖**` 절이 지워진다. 2번 첫 문단의 "문서 지도에 적힌 위치의 맥락 문서를 모두 읽는다"는 그대로 둔다 (`plugins/plate/skills/plan/SKILL.md`)
- [x] **조건**의 남은 결과 항목이 줄어든다. 본문 해시로 견주는 규칙의 두 글(`돌려 본 결과가 지금 본문의 것인지는 커밋 시각이 아니라 …로 견준다`, `` `HEAD:<경로>`와 견주지 않는다 ``)과 커밋 시각을 쓰지 않는 까닭은 남는다. `아래 규칙대로 통과 조건은 커밋 전의 작업 트리에서 돌아`로 시작하는 설명은 지워지고, 작업 트리 항목을 가리키는 짧은 말로 바뀐다 (`plugins/plate/skills/plan/SKILL.md`)
- [x] 양식을 읽는 법 세 문장이 `## 낱말`에 run과 같은 이름의 낱말로 한 번 적힌다. `## 계획 파일의 양식`의 첫 문단은 그 낱말을 가리키는 짧은 줄로 바뀐다 (`plugins/plate/skills/plan/SKILL.md`)
- [x] `PlanRulesTest`에 완료 조건 2의 네 단언(앞 목록 머리의 머리말과 두 목록, `**그 밖**` 없음, 남은 결과 항목의 지운 설명 없음, 양식 읽는 법이 한 번이고 낱말에 있으며 양식 절이 가리킴)이 더해진다. `## 디렉터리 구조`의 `test_skill_rules.py` 줄에 새 테스트가 다루는 규칙이 더해진다 (`tests/test_skill_rules.py`, `docs/ARCHITECTURE.md`)

**통과 조건**
- 6번 목록과 적는 규칙이 완료 조건 2대로다. (완료 조건 2)
  - 확인: `python3 -m unittest discover -s tests`가 `OK`로 끝난다. 완료 조건 2의 네 단언을 하는 테스트와 `test_37_draft_check`, `test_41_conditions_from_earlier_phase_output`, `test_46_rerun_results_compared_by_body_hash`, `test_53_draft_check_for_run_scenes`, `test_55_checks_run_on_uncommitted_worktree`, `test_57_quote_earlier_task_text_as_changed`가 그 안에 있다
  - 확인: plan `## 2. 맥락 문서를 읽는다`의 첫 문단을 읽어 "문서 지도에 적힌 위치의 맥락 문서를 모두 읽는다"가 그대로 있다
- 앞 phase가 이룬 더하는 경우의 규칙이 그대로다. 이 phase가 6번과 **결정**에 걸린 글을 고치기 때문이다. (완료 조건 1)
  - 확인: `python3 -m unittest discover -s tests`가 `OK`로 끝난다. 완료 조건 1의 테스트가 그 안에 있다
- 앞 task가 이룬 tasks 완료 조건 3이 그대로다. (완료 조건 4)
  - 확인: `git grep -n 'TOOLS.md' -- plugins/`가 아무것도 내지 않는다

## 한 일
- 6번 목록이 둘로 나뉜다: 번호 목록 뒤에 "초안을 보여 주기 전에 아래를 본다." 머리 아래 점검 목록과 "초안을 보여 준 뒤에는 아래를 따른다." 머리 아래 네 규칙(미리 받은 승인, 고칠 곳, 분명하지 않은 답, 마지막 task까지 7번으로 가지 않음)으로 나눴다. 점검 항목에서는 앞머리 "초안을 보여 주기 전에 "만 뺐고 글은 그대로다. 머리말이 없던 항목(`HEAD` 점검, 다른 phase 확인 가리킴, 다른 스킬의 낱말, ADR 후보)도 앞 목록에 든다 (`plugins/plate/skills/plan/SKILL.md`)
- `**그 밖**` 절이 지워진다: 두 줄과 굵은 머리를 지웠다. 2번 첫 문단은 그대로다 (`plugins/plate/skills/plan/SKILL.md`)
- **조건**의 남은 결과 항목이 줄어든다: `아래 규칙대로 통과 조건은 커밋 전의 작업 트리에서 돌아 `HEAD`에는 그 phase가 고친 본문이 없다.`를 `` `HEAD`에 그 phase가 고친 본문이 없는 까닭은 통과 조건이 작업 트리에서 돈다는 다음 항목에 있다. ``로 바꿨다. 본문 해시의 두 글과 커밋 시각을 쓰지 않는 까닭은 남았다 (`plugins/plate/skills/plan/SKILL.md`)
- 양식을 읽는 법이 낱말에 한 번 적힌다: `## 낱말` 끝에 run과 같은 이름 `**양식을 읽는 법**` 낱말을 더하고, `## 계획 파일의 양식` 첫 문단을 `아래 코드 블록 안쪽이 세 파일의 꼴이다. 낱말의 "양식을 읽는 법"대로 옮긴다.`로 바꿨다 (`plugins/plate/skills/plan/SKILL.md`)
- `PlanRulesTest`에 네 단언이 더해진다: `test_draft_list_split_before_and_after`, `test_no_other_part_in_writing_rules`, `test_remaining_results_item_points_to_worktree_item`, `test_template_reading_rule_in_one_place`를 더하고, `## 디렉터리 구조`의 `test_skill_rules.py` 줄에 네 규칙을 더했다 (`tests/test_skill_rules.py`, `docs/ARCHITECTURE.md`)

## 확인 결과
- 6번 목록과 적는 규칙이 완료 조건 2대로다. (완료 조건 2)
  - `python3 -m unittest discover -s tests` → `Ran 187 tests` … `OK`. `python3 -m unittest -v tests.test_skill_rules`에서 새 네 테스트와 `test_37_draft_check`, `test_41_conditions_from_earlier_phase_output`, `test_46_rerun_results_compared_by_body_hash`, `test_53_draft_check_for_run_scenes`, `test_55_checks_run_on_uncommitted_worktree`, `test_57_quote_earlier_task_text_as_changed`가 모두 `ok`. 통과
  - `grep -n -A2 '^## 2\. 맥락' plugins/plate/skills/plan/SKILL.md` → 첫 문단 "문서 지도에 적힌 위치의 맥락 문서를 모두 읽는다. 지도에 행이 더해져 있으면 그 문서도 읽는다." 그대로. 통과
- 앞 phase가 이룬 더하는 경우의 규칙이 그대로다. (완료 조건 1)
  - 같은 `python3 -m unittest discover -s tests` → `OK`. `test_no_adding_after_evaluation_started`, `test_adding_reads_earlier_task_heads`, `test_57_quote_earlier_task_text_as_changed`가 `ok`. 통과
- 앞 task가 이룬 tasks 완료 조건 3이 그대로다. (완료 조건 4)
  - `git grep -n 'TOOLS.md' -- plugins/` → 출력 없음(종료 코드 1). 통과

## 계획과 달라진 점
없음

## 남은 것
- 뒤 목록의 첫 항목 글("초안을 보여 주기 전에 받은 승인은 승인이 아니다")에 "초안을 보여 주기 전에"가 남는다. 점검 항목이 아니라 승인 규칙의 글이라 TODO대로 고치지 않았다. 그래서 새 테스트는 6번 절 전체가 아니라 앞 목록(두 머리 사이)에 그 머리말이 없는지를 본다
- `test_template_reading_rule_in_one_place`는 `RunRulesTest`와 `PlanRulesTest`에 같은 이름으로 있다. 클래스가 달라 둘 다 돈다

## 하네스에서 걸린 것
없음

## 확인 1

**통과 조건**
- 6번 목록과 적는 규칙이 완료 조건 2대로다. (완료 조건 2)
  - `python3 -m unittest discover -s tests` → `Ran 187 tests` … `OK`. `python3 -m unittest -v tests.test_skill_rules`에서 네 단언의 `test_draft_list_split_before_and_after`, `test_no_other_part_in_writing_rules`, `test_remaining_results_item_points_to_worktree_item`, `test_template_reading_rule_in_one_place`(PlanRulesTest)와 `test_37_draft_check`, `test_41_conditions_from_earlier_phase_output`, `test_46_rerun_results_compared_by_body_hash`, `test_53_draft_check_for_run_scenes`, `test_55_checks_run_on_uncommitted_worktree`, `test_57_quote_earlier_task_text_as_changed`가 모두 `ok`. 통과
  - plan `## 2. 맥락 문서를 읽는다`(55줄) → 첫 문단 "문서 지도에 적힌 위치의 맥락 문서를 모두 읽는다. 지도에 행이 더해져 있으면 그 문서도 읽는다."가 그대로 있다. 통과
- 앞 phase가 이룬 더하는 경우의 규칙이 그대로다. (완료 조건 1)
  - 같은 `python3 -m unittest discover -s tests` → `OK`. `test_no_adding_after_evaluation_started`, `test_adding_reads_earlier_task_heads`, `test_57_quote_earlier_task_text_as_changed`가 `ok`. 통과
- 앞 task가 이룬 tasks 완료 조건 3이 그대로다. (완료 조건 4)
  - `git grep -n 'TOOLS.md' -- plugins/` → 출력 없음(종료 코드 1). 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 187 tests`, `OK`. 통과

**남은 것**
없음

**실패**
없음

**하네스에서 걸린 것**
없음

**판정**: 통과
