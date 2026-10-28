# 회고

## 회고 1

**확인**
- 1. 이슈·PR 명령이 밖의 글과 따옴표에 안전하다(보안-1, 보안-2, 보안-4, 성능-5, 유지보수성-8)
  - `python3 -m unittest discover -s tests` → `Ran 181 tests` / `OK`. `tests/test_skill_rules.py`에 `test_issue_text_is_data_only`, `test_text_passing_rule_in_one_place`, `test_issue_list_filters_by_body_without_narrowing_limit`, `test_pr_question_shows_comment_text`가 있다. 통과
  - `mktemp -d`의 `<임시>/bin/gh`(인자마다 `printf '%s\n'`로 `<임시>/args`에 덧붙임, 실행 권한)를 두고, 제목 `` `plate:plan`이 $(touch <임시>/pwned) 'x' "y" ``를 낱말의 "글을 넘기는 법"대로(작은따옴표로 감싸고 안의 `'`를 `'\''`로) 넣은 `gh issue list --search`, `gh issue create --title`, `gh pr create --title` 세 줄을 `<임시>/run.sh`에 써서 `PATH=<임시>/bin:$PATH sh <임시>/run.sh` → `grep -cxF -f <임시>/title <임시>/args`가 `3`, `ls <임시>/pwned`가 `No such file or directory`. 통과
  - `docs/ARCHITECTURE.md` `## 패턴과 규칙` run PR 줄("PR을 열지 물을 때 댓글로 달 그 평가 절의 글을 함께 보여 준다"), `## 데이터 흐름` PR 줄("그 평가 절의 글을 물을 때 함께 보여 준다"), `README.md` `## tasks 끝의 PR`("PR을 열지 물으면서 댓글로 달 그 평가 절의 글을 함께 보여 준다")을 읽음 → 세 곳 모두 뜻을 담는다. 통과
- 2. 3번이 상태를 읽는 법을 정하고 행 판정이 이어진다(성능-3, 신뢰성-1, 신뢰성-7, 신뢰성-8, 기존 작업 정합성-4)
  - `python3 -m unittest discover -s tests` → `OK`. `test_state_tables_row_order`, `test_three_failure_resume_goes_to_fix_phase_for_retro`, `test_state_reading_and_stop_line_rows`, `test_runlog_reason_for_respawn`이 있다. 통과
  - 작업 트리를 `cp -R`로 `<임시>/repo`에 베끼고 사본 run 본문 3번 첫 표의 `| 확인 절이 없다 | 5번 |`과 `| 마지막 확인 절의 판정이 "통과"다 | 6번 |` 행의 자리를 바꿔 `python3 -m unittest tests.test_skill_rules` → `FAIL: test_state_tables_row_order (… table='| 남은 첫 phase의 상태 | 갈 곳 |')`, `FAILED (failures=1)`. 통과
  - `<임시>`에 (가)~(마) 시험 파일을 두고((라)는 `` ````markdown `` 블록 안에 백틱 셋 블록과 `**판정**: 통과`, `## 확인 9`를 넣음. (마)에는 같은 task의 다른 phase, 자리 없는 줄, 다른 task, `phase 12` 줄도 넣음), run 본문 117줄의 `awk -v h='확인'` 명령을 본문에서 뽑아 경로만 바꾸고(`retro.md`는 `h='회고'`) `멈춤` 줄 grep과 함께 `<임시>/run.sh`로 돌림 → (가) `확인 절 0, 마지막 판정 없음`, (나) `확인 절 2, 마지막 판정 **판정**: 통과`, (다) `회고 절 3, 마지막 판정 **판정**: 문제 있음`, (라) `확인 절 1, 마지막 판정 **판정**: 실패`, (마) `` - 물음 | 멈춤 | `001-a` phase 2 확인 3 | 다시 맡길지 | 답: 다시 맡긴다 `` 한 줄. 통과
  - `docs/ARCHITECTURE.md` `## 데이터 흐름` 끝 문단을 읽음 → "세 번 실패에서는 멈추고 원인과 해결책을 보여 논의한다"가 그대로 있고, "세 번 실패로 멈춘 뒤 다시 맡기기로 하면 그 답을 자리…와 함께 `RUNLOG.md`의 `멈춤` 줄에 남겨, 세션을 끊고 다시 불러도 … 같은 자리…로 간다"가 더해져 있다. 통과
- 3. 브랜치와 비운 뒤의 재개가 끝의 PR·합침에 이른다(신뢰성-2, 신뢰성-3, 신뢰성-6)
  - `python3 -m unittest discover -s tests` → `OK`. `test_branch_question_when_not_default_or_tasks_branch`, `test_resume_after_clearing_goes_to_pr_or_merge`, `test_merge_has_own_question_and_switch_failure`, `test_branch_in_question_lists`가 있다. 통과
  - `<임시>/g`에 `git init -b main`, `docs/tasks/plan.md`(`# 시험 tasks`, `**이름**: demo`) 커밋, `git switch -c tasks/demo`, `git rm` 뒤 `demo: 비움` 커밋. 0번의 세 명령 → `tasks/demo`, `demo: 비움`, `# 시험 tasks`. 빈 커밋 `demo: RUNLOG` 뒤 다시 → `tasks/demo`, `demo: RUNLOG`(재개 갈래로 가지 않는다). 통과
  - 다섯 곳을 읽음 → ARCHITECTURE `## 패턴과 규칙` run 브랜치 줄(브랜치 물음, 비운 뒤 PR·합침), `## 데이터 흐름` 실행 단계 브랜치 줄(브랜치 물음), README 스킬 표 `run` 행(두 갈래), README `## tasks 끝의 PR`(두 갈래), PRD 핵심 기능 8의 PR 문장(두 갈래). 통과
- 4. 맡기는 글과 고칠 꼴이 바로 넘어간다(보안-3, 성능-4, 기존 작업 정합성-3, 기존 작업 정합성-5, 유지보수성-12)
  - `python3 -m unittest discover -s tests` → `OK`. `test_worktree_skill_line_branches_and_no_old_body`, `test_fix_phase_finds_guarding_tests`, `test_fix_task_copies_condition_text`, `test_template_reading_rule_in_one_place`, `test_51_marker_line_ends_every_hand_off_block`, `CallerMarkerTest`가 있다. 통과
  - `<임시>/m`에 `git init`, 빈 첫 커밋 `ae7fbe2`, 둘째 커밋에 `.claude-plugin/marketplace.json`(`plate`, `./plugins/plate`)과 두 사본(`plugins/plate/…`, `vendor/copy/…`, 둘 다 `plugin.json` 이름 `plate`). 매니페스트를 읽어 `source` `./plugins/plate`를 얻고 `git diff --name-only ae7fbe2 {둘째 커밋}` 출력(다섯 경로, `vendor/copy/skills/phase/SKILL.md` 든다)에서 `plugins/plate/skills/phase/SKILL.md`만 고름 → 그 하나. `git rm -r .claude-plugin vendor/copy`로 셋째 커밋 뒤 이름이 `plate`인 `plugin.json`을 둔 폴더 규칙으로 `ae7fbe2`와 HEAD 사이에서 고름 → `plugins/plate/skills/phase/SKILL.md`. 통과
  - `docs/ARCHITECTURE.md` `## 패턴과 규칙`의 작업 트리의 스킬 줄 문장을 읽음 → "marketplace 매니페스트의 `source` 아래의 `skills/{스킬 이름}/SKILL.md` 한 곳으로 좁히고"와 "이름으로 옛 본문을 부르지 않는다"가 둘 다 있다. 통과
- 5. 앞 task가 이룬 tasks 완료 조건 1과 3이 이 task의 마지막 커밋에서도 참이다
  - `python3 -m unittest discover -s tests` → `Ran 181 tests` / `OK`. 통과
  - `git grep -n 'TOOLS.md' -- plugins/` → 출력 없음(종료 1). 통과
  - `git grep -nE '사용량.*TOOLS\.md|TOOLS\.md.*사용량' -- docs/PRD.md docs/ARCHITECTURE.md docs/ADR.md README.md AGENTS.md` → 출력 없음(종료 1). 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 181 tests in 16.609s` / `OK`. 통과

**남은 것**
- phase 1: 제목에 `$(`가 들면 작은따옴표 안이어도 헤드리스 권한 검사가 막을 수 있고 권한 검사 아래에서는 돌리지 않음 → 문제 아님 (막히면 승인을 묻는 것이고 셸에서는 치환이 일어나지 않음을 위 가짜 `gh` 장면으로 봤다. 넘기는 법은 task 머리 결정이 수행에 맡겼고, 실제 흐름은 완료 조건 1의 `돌리지 않음` 줄이 돌리지 않기로 정했다)
- phase 1: 밖의 사람이 댓글에 tasks 이름을 적어 "이슈를 올린다" 2번의 올림을 건너뛰게 하는 길이 남음 → 문제 아님 (tasks 머리 결정이 보안-1을 보고서의 고치는 방향 "데이터로만 본다는 줄을 더한다"대로 고치게 했고 완료 조건 1도 그 글만 본다. 경계 밖으로 `FRICTION.md`에 적는다)
- phase 1: 이슈를 실제로 올리고 PR을 여는 흐름은 돌리지 않음 → 문제 아님 (완료 조건 1의 `돌리지 않음` 줄)
- phase 2: awk 명령은 닫는 줄 끝에 공백이 붙은 코드 블록을 닫힌 것으로 보지 못한다 → 문제 아님 (check·retro 양식이 만드는 파일에는 그런 줄이 없고, 시험 파일 (가)~(라)와 이 task의 `done-phase-N.md`·양식 블록을 그대로 읽는다)
- phase 2: 세 번 실패로 멈춘 뒤 멈추기로 한 답은 자리 없이 적혀 다시 부르면 같은 자리에서 다시 멈춘다 → 문제 아님 (완료 조건 2가 정한 동작)
- phase 2: `멈춤` 줄의 자리와 에이전트 줄 끝 `다시 띄움:`이 eval의 셈에 걸리는지 돌려 보지 않음 → 문제 아님 (task 머리 범위 밖이 eval·retro는 `RUNLOG.md`의 꼴을 run에 맡긴다고 정했고, 새 꼴도 줄 머리 `- 물음 | 멈춤 | `와 task 이름 자리를 그대로 둔다)
- phase 3: 0번의 재개 갈래는 비움 커밋이 마지막 커밋일 때만 탄다 → 문제 아님 (완료 조건 3의 git 장면이 `demo: RUNLOG` 뒤에는 재개하지 않기를 기대한다)
- phase 3: 이미 PR을 연 브랜치로 다시 부르면 `gh pr create`가 실패한다 → 문제 아님 (task 머리 범위 밖)
- phase 3: 1번 브랜치 물음을 승인해 `tasks/<이름>`을 새로 만들면 지금 브랜치의 끝에서 갈라져 그 브랜치의 커밋이 tasks 브랜치에 든다 → 문제 아님 (1번의 1항이 계획의 커밋을 지금 브랜치에 넣으므로 거기서 갈라져야 계획이 tasks 브랜치에 든다. 물을 때 지금 브랜치를 보여 준다)
- phase 3: eval 본문 `낱말`의 "정해 둔 물음" 목록에 `브랜치`가 없다 → 문제 아님 (task 머리 범위 밖이 고치지 않는다고 정했다)
- phase 4: `docs/TOOLS.md` 48줄이 작업 트리의 스킬 줄을 줄여 인용한다 → 문제 아님 (48줄을 읽음: `작업 트리의 {경로}를 읽어 그 절차를 따른다. …`로 바뀐 둘째 문장과 어긋나지 않는다)
- phase 4: 에이전트에게 실제로 맡기는 흐름은 돌리지 않음 → 문제 아님 (완료 조건 4의 `돌리지 않음` 줄)

**문제**
- 없음

**판정**: 통과
