# Phase 4: 맡기는 글과 고칠 꼴을 바로 넘기게 한다

**목표**: 작업 트리의 스킬 줄이 marketplace 매니페스트가 가리키는 한 곳만 고르고 옛 본문을 부르지 않게 하고, 고칠 phase와 고침 task가 걸리는 테스트와 조건 글을 넘기고, 양식을 읽는 법이 낱말에 한 번 있게 한다.

**테스트 먼저**: 아니오 — 스킬 본문(`.md`)과 그 글을 지키는 테스트, 맥락 문서만 바꾼다

**읽을 것**
- `plugins/plate/skills/run/SKILL.md` (`## 낱말`의 작업 트리의 스킬 줄과 표지 줄, 맡기는 글 다섯 자리: `## 4. 수행을 맡긴다`, `## 5. 확인을 맡긴다`, `## 7. task 회고를 맡긴다`, `### 코드 평가를 맡긴다`, `### 하네스 eval을 맡긴다`. 그리고 `## 8. 고칠 phase를 더한다`의 TODO·읽을 것 규칙과 꼴, `### 고침 task를 더한다`의 **고침 task의 꼴**과 두 파일의 꼴. 양식을 읽는 법 세 문장이 있는 다섯 자리: 8번, `### BACKLOG를 고친다`, `### 고침 task를 더한다`, `## PR을 연다`의 **PR 본문의 꼴**, `## `RUNLOG.md``)
- `.claude-plugin/marketplace.json` (이름 `plate`, `source` `./plugins/plate`)
- `docs/cleanup/2026-10-28.md` (보안-3, 성능-4, 기존 작업 정합성-3, 기존 작업 정합성-5, 유지보수성-12와 그 2라운드)
- `tests/test_skill_rules.py` (`RunRulesTest.test_51_marker_line_ends_every_hand_off_block`, `test_47_no_command_substitution_in_git_commands`, `CallerMarkerTest`)
- `plugins/plate/skills/phase/SKILL.md` (`## 6. 다섯 줄을 돌려준다`: 작업 트리의 스킬 줄로 run이 띄운 호출을 가르는 글)
- `docs/ARCHITECTURE.md` (`## 패턴과 규칙`의 스킬이 다른 스킬을 이름으로 부른다는 줄과 작업 트리의 스킬 줄 예외)

**TODO**
- [x] 낱말의 작업 트리의 스킬 줄이 바뀐다. `.claude-plugin/marketplace.json`이 있고 이름이 `plate`인 플러그인의 `source`가 있으면 그 `source` 아래의 `skills/{스킬 이름}/SKILL.md`만 `{경로}`로 고르고, 없으면 지금 규칙대로 고른다. 명령 치환 없이 읽는 법이 함께 적힌다 (`plugins/plate/skills/run/SKILL.md`)
- [x] 작업 트리의 스킬 줄을 붙일 때 맡기는 글이 이름으로 옛 본문을 불러 싣게 하지 않게 바뀐다. 표지 줄은 블록 끝에 그대로 남고, 작업 트리의 스킬 줄은 `작업 트리의 {경로}를 읽어 그 절차를 따른다.`로 시작하며, git diff는 맡길 때마다 다시 낸다. 맡기는 글 다섯 자리의 붙이는 규칙 글도 이에 맞는다 (`plugins/plate/skills/run/SKILL.md`)
- [x] 8번에, 문제의 글(또는 고칠 줄의 핵심 낱말)을 테스트 폴더에서 찾아 걸리는 테스트를 읽을 것과 그 TODO의 파일 목록에 넣는다는 규칙이 더해지고, 고칠 phase의 꼴에 그 자리가 보인다. **고침 task의 꼴**의 "8번과 같은 규칙" 줄이 이 규칙도 덮는다 (`plugins/plate/skills/run/SKILL.md`)
- [x] **고침 task의 꼴**의 마지막 완료 조건 규칙과 task 머리의 꼴이, 가리킨 tasks 완료 조건마다 그 조건의 글과 확인을 함께 옮기게 바뀐다 (`plugins/plate/skills/run/SKILL.md`)
- [x] 양식을 읽는 법 세 문장("아래 코드 블록 안쪽이 …의 꼴이다. 블록을 여닫는 줄은 옮기지 않는다. `{…}`는 …")이 낱말에 한 낱말로 한 번 적힌다. 다섯 자리는 그 낱말을 가리키는 짧은 줄로 바뀐다 (`plugins/plate/skills/run/SKILL.md`)
- [x] `RunRulesTest`에 완료 조건 4의 단언(작업 트리의 스킬 줄의 두 갈래, 8번의 테스트 폴더 찾기, 고침 task의 조건 글 옮기기, 양식 읽는 법이 한 번이고 다섯 자리가 가리킴)이 더해진다. 바뀐 글에 걸리는 기존 테스트는 바뀐 뒤의 글로 고친다 (`tests/test_skill_rules.py`)
- [x] ARCHITECTURE `## 패턴과 규칙`의 작업 트리의 스킬 줄 문장에, marketplace 매니페스트의 `source`로 좁힌다는 것과 그 줄을 붙이면 이름으로 옛 본문을 부르지 않는다는 것이 더해진다. `## 디렉터리 구조`의 `test_skill_rules.py` 줄에 새 테스트가 다루는 규칙이 더해진다 (`docs/ARCHITECTURE.md`)

**통과 조건**
- 맡기는 글과 고칠 꼴이 완료 조건 4대로다. (완료 조건 4)
  - 확인: `python3 -m unittest discover -s tests`가 `OK`로 끝난다. 완료 조건 4의 단언을 하는 테스트와 `test_51_marker_line_ends_every_hand_off_block`, `CallerMarkerTest`가 그 안에 있다
  - 확인: `mktemp -d`로 만든 `<임시>/m`에 `git init`을 하고 첫 커밋을 넣는다. `.claude-plugin/marketplace.json`(이름 `plate`, `source` `./plugins/plate`)을 두고, 두 사본을 만든다: `plugins/plate/.claude-plugin/plugin.json`(이름 `plate`)과 `plugins/plate/skills/phase/SKILL.md`, 그리고 `vendor/copy/.claude-plugin/plugin.json`(이름 `plate`)과 `vendor/copy/skills/phase/SKILL.md`. 이 둘을 둘째 커밋에 넣는다. 낱말에 적은 고르는 법대로 첫 커밋과 HEAD 사이에서 `phase`의 경로를 고른다. `plugins/plate/skills/phase/SKILL.md` 하나만 나온다. `marketplace.json`과 `vendor/copy`를 지운 커밋을 넣고 첫 커밋과 그 HEAD 사이에서 다시 고르면 `plugins/plate/skills/phase/SKILL.md`가 나온다
  - 확인: ARCHITECTURE `## 패턴과 규칙`의 작업 트리의 스킬 줄 문장을 읽는다. marketplace 매니페스트의 `source`로 좁힌다는 것과 이름으로 옛 본문을 부르지 않는다는 것이 둘 다 있다
- 앞 phase가 이룬 규칙이 그대로다. 이 phase가 "PR을 연다"의 꼴과 `RUNLOG.md` 절을 고치기 때문이다. (완료 조건 1, 2, 3)
  - 확인: `python3 -m unittest discover -s tests`가 `OK`로 끝난다. 완료 조건 1·2·3의 테스트가 그 안에 있다
- 앞 task가 이룬 tasks 완료 조건 1과 3이 그대로다. (완료 조건 5)
  - 확인: `git grep -n 'TOOLS.md' -- plugins/`가 아무것도 내지 않는다
  - 확인: `git grep -nE '사용량.*TOOLS\.md|TOOLS\.md.*사용량' -- docs/PRD.md docs/ARCHITECTURE.md docs/ADR.md README.md AGENTS.md`가 아무것도 내지 않는다

## 한 일
- 낱말의 작업 트리의 스킬 줄: 한 덩어리 글을 갈래 넷(바꿨는지 보는 법, marketplace 매니페스트가 있을 때, 매니페스트가 없을 때, 붙이는 법)으로 나눴다. 매니페스트가 있고 `name`이 `plate`인 플러그인에 `source`가 있으면 `source`(앞 `./`, 끝 `/`를 뺀 폴더) 아래의 `skills/{스킬 이름}/SKILL.md` 하나만 보고, 다른 `plugin.json` 사본은 고르지 않는다. 없으면 지금 규칙(이름이 `plate`인 `.claude-plugin/plugin.json`을 둔 폴더)대로다. 매니페스트는 파일을 읽는 도구로 읽고 명령 치환을 쓰지 않는다고 적었다 (`plugins/plate/skills/run/SKILL.md`)
- 옛 본문을 부르지 않게: 작업 트리의 스킬 줄의 글을 `작업 트리의 {경로}를 읽어 그 절차를 따른다. 이름으로 스킬을 불러 그 본문을 싣지 않는다.`로 바꾸고, 붙이는 법에 "맡기는 글의 첫 줄(`plate의 … 스킬(…)을 불러 그 절차를 따른다.`)을 빼고 표지 줄 뒤에 붙인다"를 적었다. 바꿨는지는 맡길 때마다 git 명령을 다시 내어 본다고 적었다. 맡기는 글 다섯 자리(4번, 5번, 7번, 코드 평가, 하네스 eval)의 붙이는 규칙 글을 `맡길 때마다 낱말의 "작업 트리의 스킬 줄"대로 … 글의 첫 줄을 빼고 표지 줄 뒤에 작업 트리의 스킬 줄을 붙인다.`로 바꿨다. 코드 블록은 그대로 표지 줄로 끝난다 (`plugins/plate/skills/run/SKILL.md`)
- 8번의 테스트 찾기: "고칠 글을 지키는 테스트도 그 TODO에 넣는다" 항목을 더했다(문제의 글이나 핵심 낱말을 `tests/`, `test/`, `__tests__/`와 테스트 파일에서 `git grep -n -F '{낱말}' -- tests/`처럼 찾아 걸리는 테스트를 읽을 것과 TODO 파일 목록에 둔다). 고칠 phase의 꼴의 읽을 것·TODO·통과 조건 확인에 그 자리를 넣었다. **고침 task의 꼴**의 "8번과 같은 규칙" 줄을 "테스트 먼저, 읽을 것, TODO의 파일 목록(… 테스트 폴더에서 찾아 걸린 테스트)"으로 넓히고, 고침 task의 `phase-1.md` 꼴에도 그 자리를 넣었다 (`plugins/plate/skills/run/SKILL.md`)
- 고침 task의 조건 글: 마지막 완료 조건 규칙을 "가리킨 tasks 완료 조건마다 tasks 머리에 적힌 그 조건의 글과 확인을 함께 그대로 옮긴다"로 바꾸고, task 머리 꼴의 마지막 조건 아래에 `- tasks 완료 조건 {번호}: {…조건의 글…}`과 그 아래 `- 확인:`을 두었다 (`plugins/plate/skills/run/SKILL.md`)
- 양식을 읽는 법: 낱말에 `- **양식을 읽는 법**:` 한 항목으로 세 문장을 두고, 다섯 자리(8번, BACKLOG를 고친다, 고침 task를 더한다, PR을 연다, `RUNLOG.md`)의 세 문장을 `아래 코드 블록 안쪽이 …의 꼴이다. 낱말의 "양식을 읽는 법"대로 옮긴다(블록을 여닫는 줄과 `{…}`를 남기지 않는다).`로 바꿨다 (`plugins/plate/skills/run/SKILL.md`)
- `RunRulesTest`에 넷을 더했다: `test_worktree_skill_line_branches_and_no_old_body`, `test_fix_phase_finds_guarding_tests`, `test_fix_task_copies_condition_text`, `test_template_reading_rule_in_one_place`. 기존 테스트 가운데 바뀐 글에 걸려 고칠 것은 없었다 (`tests/test_skill_rules.py`)
- ARCHITECTURE: `## 패턴과 규칙`의 작업 트리의 스킬 줄 문장에 맡길 때마다 다시 본다는 것, marketplace 매니페스트의 `source` 한 곳으로 좁히고 없으면 `plugin.json` 규칙으로 고른다는 것, 붙이면 첫 줄을 빼 이름으로 옛 본문을 부르지 않는다는 것을 더했다. `## 디렉터리 구조`의 `test_skill_rules.py` 줄에 새 테스트의 규칙 넷을 더했다 (`docs/ARCHITECTURE.md`)

## 확인 결과
- 맡기는 글과 고칠 꼴이 완료 조건 4대로다.
  - `python3 -m unittest discover -s tests` → `Ran 181 tests` `OK`. `-v`로 `test_worktree_skill_line_branches_and_no_old_body`, `test_fix_phase_finds_guarding_tests`, `test_fix_task_copies_condition_text`, `test_template_reading_rule_in_one_place`, `test_51_marker_line_ends_every_hand_off_block`, `test_51_direct_report_only_without_marker (CallerMarkerTest)`가 모두 `ok`. 통과
  - `mktemp -d`(`/var/folders/0j/cj37rxmj1mj73vhflqpgsxm00000gn/T/tmp.Oc6l0RSefJ`)의 `m`에 `git init`, 빈 첫 커밋 `e4cbeb7`, 둘째 커밋에 `.claude-plugin/marketplace.json`(`plate`, `./plugins/plate`)과 두 사본(`plugins/plate/…`, `vendor/copy/…`, 둘 다 `plugin.json` 이름 `plate`). 매니페스트를 읽어 `source` `./plugins/plate`를 얻고 `git diff --name-only e4cbeb7 HEAD`의 출력에서 `plugins/plate/skills/phase/SKILL.md`만 보니 → `plugins/plate/skills/phase/SKILL.md` 하나. (대조로 `plugin.json` 규칙만 쓰면 `vendor/copy/skills/phase/SKILL.md`까지 둘이 나온다.) `git rm -r .claude-plugin vendor/copy`로 셋째 커밋을 넣고 매니페스트가 없을 때의 갈래로 `e4cbeb7`과 HEAD 사이에서 다시 고르니 → `plugins/plate/skills/phase/SKILL.md`. 통과
  - `docs/ARCHITECTURE.md` 48줄을 읽음 → "marketplace 매니페스트의 `source` 아래의 `skills/{스킬 이름}/SKILL.md` 한 곳으로 좁히고"와 "이름으로 옛 본문을 부르지 않는다"가 둘 다 있다. 통과
- 앞 phase가 이룬 규칙이 그대로다.
  - `python3 -m unittest discover -s tests` → `OK`. 완료 조건 1(`test_issue_text_is_data_only`, `test_text_passing_rule_in_one_place`, `test_issue_list_filters_by_body_without_narrowing_limit`, `test_pr_question_shows_comment_text`), 2(`test_state_tables_row_order`, `test_three_failure_resume_goes_to_fix_phase_for_retro`, `test_state_reading_and_stop_line_rows`, `test_runlog_reason_for_respawn`), 3(`test_branch_question_when_not_default_or_tasks_branch`, `test_resume_after_clearing_goes_to_pr_or_merge`, `test_merge_has_own_question_and_switch_failure`, `test_branch_in_question_lists`)의 테스트가 모두 `ok`. 통과
- 앞 task가 이룬 tasks 완료 조건 1과 3이 그대로다.
  - `git grep -n 'TOOLS.md' -- plugins/` → 출력 없음(종료 코드 1). 통과
  - `git grep -nE '사용량.*TOOLS\.md|TOOLS\.md.*사용량' -- docs/PRD.md docs/ARCHITECTURE.md docs/ADR.md README.md AGENTS.md` → 출력 없음(종료 코드 1). 통과

## 계획과 달라진 점
- 없음

## 남은 것
- 작업 트리의 스킬 줄의 둘째 문장을 "불러 온 스킬의 본문과 다르면 이 파일을 따른다"에서 "이름으로 스킬을 불러 그 본문을 싣지 않는다"로 바꿨다. `docs/TOOLS.md` 48줄은 그 줄을 `작업 트리의 {경로}를 읽어 그 절차를 따른다. …`로 줄여 인용해 어긋나지 않지만, TOOLS.md를 고치는 것은 이 task의 범위 밖이라 건드리지 않았다
- 시험 저장소의 고르는 확인은 낱말에 적은 절차(매니페스트를 읽고 `source` 폴더 아래 경로만 diff 출력에서 찾는다)를 셸로 따라 한 것이다. 에이전트에게 실제로 맡기는 흐름(첫 줄을 빼고 붙인 글로 띄운 에이전트가 이름으로 스킬을 부르지 않는지)은 돌리지 않았다(task 머리의 돌리지 않음)

## 하네스에서 걸린 것
- 없음

## 확인 1

**통과 조건**
- 맡기는 글과 고칠 꼴이 완료 조건 4대로다. (완료 조건 4)
  - `python3 -m unittest discover -s tests` → `Ran 181 tests` `OK`. `-v`로 `test_worktree_skill_line_branches_and_no_old_body`, `test_fix_phase_finds_guarding_tests`, `test_fix_task_copies_condition_text`, `test_template_reading_rule_in_one_place`, `test_51_marker_line_ends_every_hand_off_block`, `test_51_direct_report_only_without_marker (CallerMarkerTest)`가 모두 `ok`. 네 테스트를 읽음: 낱말의 매니페스트 갈래와 없을 때의 갈래, 첫 줄을 빼는 붙이는 법과 다섯 맡기는 자리의 규칙 글, 8번의 테스트 폴더 찾기, 고침 task의 조건 글 옮기기, "블록을 여닫는 줄은 옮기지 않는다" 한 번과 다섯 자리의 가리키는 줄을 단언한다. 통과
  - `mktemp -d`(`/var/folders/0j/cj37rxmj1mj73vhflqpgsxm00000gn/T/tmp.u2QUWWGqaR`)의 `m`에 `git init`, 빈 첫 커밋, 둘째 커밋에 `.claude-plugin/marketplace.json`(`plate`, `./plugins/plate`)과 두 사본(둘 다 `plugin.json` 이름 `plate`). 낱말대로 매니페스트의 `source`에서 `plugins/plate/skills/phase/SKILL.md`만 `git diff --name-only {첫 커밋} HEAD` 출력에서 찾음 → 그 경로 하나(diff에는 `vendor/copy/skills/phase/SKILL.md`도 있으나 고르지 않음). `git rm -r .claude-plugin vendor/copy`로 셋째 커밋 뒤 매니페스트가 없을 때의 갈래(이름 `plate`인 `plugin.json`을 둔 폴더)로 다시 고름 → `plugins/plate/skills/phase/SKILL.md`. 통과
  - `docs/ARCHITECTURE.md` 48줄을 읽음 → "marketplace 매니페스트의 `source` 아래의 `skills/{스킬 이름}/SKILL.md` 한 곳으로 좁히고"와 "이름으로 옛 본문을 부르지 않는다"가 둘 다 있다. 통과
- 앞 phase가 이룬 규칙이 그대로다. (완료 조건 1, 2, 3)
  - `python3 -m unittest discover -s tests` → `OK`. 완료 조건 1(`test_issue_text_is_data_only`, `test_text_passing_rule_in_one_place`, `test_issue_list_filters_by_body_without_narrowing_limit`, `test_pr_question_shows_comment_text`), 2(`test_state_tables_row_order`, `test_three_failure_resume_goes_to_fix_phase_for_retro`, `test_state_reading_and_stop_line_rows`, `test_runlog_reason_for_respawn`), 3(`test_branch_question_when_not_default_or_tasks_branch`, `test_resume_after_clearing_goes_to_pr_or_merge`, `test_merge_has_own_question_and_switch_failure`, `test_branch_in_question_lists`)가 모두 `ok`. 통과
- 앞 task가 이룬 tasks 완료 조건 1과 3이 그대로다. (완료 조건 5)
  - `git grep -n 'TOOLS.md' -- plugins/` → 출력 없음(종료 코드 1). 통과
  - `git grep -nE '사용량.*TOOLS\.md|TOOLS\.md.*사용량' -- docs/PRD.md docs/ARCHITECTURE.md docs/ADR.md README.md AGENTS.md` → 출력 없음(종료 코드 1). 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 181 tests` `OK`. 통과

**남은 것**
- 에이전트에게 실제로 맡기는 흐름(첫 줄을 빼고 붙인 글로 띄운 에이전트가 이름으로 스킬을 부르지 않는지)은 돌리지 않았다 → 돌려 보지 않은 위험이고, task 머리 완료 조건 4의 `- 돌리지 않음: 에이전트에게 맡기는 흐름과 고칠 phase·고침 task를 쓰는 흐름은 회고와 tasks 끝의 평가가 있어야 돈다`가 돌리지 않기로 정한 동작이다. 하네스에서 걸린 것

**실패**
- 없음

**하네스에서 걸린 것**
- 남은 것: 에이전트에게 실제로 맡기는 흐름은 돌리지 않았다(task 머리 완료 조건 4의 `돌리지 않음` 줄)

**판정**: 통과
