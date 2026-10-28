# Phase 3: 브랜치와 비운 뒤의 재개를 끝의 PR·합침에 잇는다

**목표**: 1번이 다른 브랜치에서 `tasks/<이름>`으로 바꿀지 묻고, 0번이 비운 뒤 다시 불린 실행을 PR·합침으로 보내고, "합친다"가 이 자리만의 물음과 `git switch` 실패 갈래를 갖는다.

**테스트 먼저**: 아니오 — 스킬 본문(`.md`)과 그 글을 지키는 테스트, 맥락 문서만 바꾼다

**읽을 것**
- `plugins/plate/skills/run/SKILL.md` (`## 0. tasks를 본다`, `## 1. 시작 조건을 본다`의 3번 tasks 브랜치, `### 비운다`, `## PR을 연다`, `## 합친다`, `## `RUNLOG.md``의 물은 자리 목록과 task에 걸리지 않는 물음 목록과 비운 뒤의 물음 규칙)
- `docs/cleanup/2026-10-28.md` (신뢰성-2, 신뢰성-3, 신뢰성-6과 그 2라운드)
- `plugins/plate/skills/eval/SKILL.md` (`## 낱말`의 "정해 둔 물음": 물은 자리를 run의 목록에서 읽는다)
- `tests/test_skill_rules.py` (`RunRulesTest`)
- `docs/ARCHITECTURE.md` (`## 패턴과 규칙`의 run 브랜치 줄, `## 데이터 흐름`의 실행 단계 브랜치 줄과 tasks 끝의 비움·PR·합침 줄)
- `docs/PRD.md` (핵심 기능 8의 PR 문장)
- `README.md` (스킬 표의 `run` 행, `## tasks 끝의 PR`)

**TODO**
- [x] 1번 tasks 브랜치 항목이 바뀐다. 지금 브랜치가 기본 브랜치도 `tasks/<이름>`도 아니면 지금 브랜치를 보여 주고, `tasks/<이름>`으로 바꿀지 묻고 멈춘다. 승인하면 그 브랜치를 만들거나 바꿔 잇고, 거절하면 `RUNLOG.md`에 물은 자리가 `브랜치`인 줄만 더하고 끝난다 (`plugins/plate/skills/run/SKILL.md`)
- [x] `RUNLOG.md` 절의 물은 자리 목록과 task에 걸리지 않는 물음 목록에 `브랜치`가 더해진다 (`plugins/plate/skills/run/SKILL.md`)
- [x] 0번에 갈래가 더해진다. tasks 머리가 없어도 지금 브랜치가 `tasks/<이름>`이고 마지막 커밋의 제목이 `<이름>: 비움`이면, 1번부터 하지 않고 origin에 따라 "PR을 연다"나 "합친다"로 간다. PR에 쓸 글(tasks 머리, `review.md`, `eval.md`, 고침 task 머리)은 그 비움 커밋의 부모에서 읽는다. 가르는 git 명령에는 명령 치환을 쓰지 않는다 (`plugins/plate/skills/run/SKILL.md`)
- [x] "합친다" 2번이 "1번의 물음대로"를 가리키지 않고, 이 자리만의 물음(커밋하지 않은 변경을 보여 주고 그대로 합칠지 묻는다. `RUNLOG.md`에 적지 않는다)을 직접 적게 바뀐다. 3번에 `git switch`가 실패하면 합치지 않고 실패한 명령과 오류를 보고에 적고 10번으로 간다는 갈래가 더해진다 (`plugins/plate/skills/run/SKILL.md`)
- [x] `RunRulesTest`에 세 규칙의 글과 두 목록의 `브랜치`를 보는 테스트가 더해진다 (`tests/test_skill_rules.py`)
- [x] 아래 줄에 저마다 다루는 갈래의 뜻이 더해진다. 갈래는 "기본 브랜치도 `tasks/<이름>`도 아니면 바꿀지 묻는다"와 "비운 뒤 다시 부르면 PR·합침으로 간다"이다. `docs/ARCHITECTURE.md` `## 디렉터리 구조`의 `test_skill_rules.py` 줄에는 새 테스트가 다루는 규칙이 더해진다 (`docs/ARCHITECTURE.md`, `README.md`, `docs/PRD.md`)
  - `docs/ARCHITECTURE.md`: `## 패턴과 규칙`의 run 브랜치 줄, `## 데이터 흐름`의 실행 단계 브랜치 줄과 tasks 끝 줄
  - `README.md`: 스킬 표의 `run` 행, `## tasks 끝의 PR`
  - `docs/PRD.md`: 핵심 기능 8의 PR 문장

**통과 조건**
- 브랜치와 재개가 완료 조건 3대로다. (완료 조건 3)
  - 확인: `python3 -m unittest discover -s tests`가 `OK`로 끝나고, 세 규칙과 두 목록의 `브랜치`를 보는 테스트가 그 안에 있다
  - 확인: `mktemp -d`로 만든 `<임시>/g`에 `git init`을 하고 `docs/tasks/plan.md`(첫 줄 `# 시험 tasks`, `**이름**: demo`)를 기본 브랜치에 커밋한다. `tasks/demo`로 바꿔 그 파일을 지우고, 제목이 `demo: 비움`인 커밋을 넣는다. 0번에 적은 가르는 명령을 그 폴더에서 돌린다. 지금 브랜치 `tasks/demo`, 마지막 커밋 제목 `demo: 비움`, 부모에서 읽은 tasks 머리의 첫 줄 `# 시험 tasks`가 나온다. 빈 커밋 `demo: RUNLOG`를 하나 더 넣고 다시 돌리면 마지막 커밋 제목이 `demo: 비움`이 아니다
  - 확인: 아래 다섯 곳을 저마다 읽는다. 저마다 그 줄이 다루는 갈래(브랜치 물음, 비운 뒤의 재개)를 담는다.
    - ARCHITECTURE `## 패턴과 규칙`의 run 브랜치 줄
    - `## 데이터 흐름`의 실행 단계 브랜치 줄
    - README 스킬 표의 `run` 행
    - README `## tasks 끝의 PR`
    - PRD 핵심 기능 8의 PR 문장
- 앞 phase가 이룬 규칙이 그대로다. 이 phase가 "PR을 연다"와 `RUNLOG.md` 절을 고치기 때문이다. (완료 조건 1, 2, 5)
  - 확인: `python3 -m unittest discover -s tests`가 `OK`로 끝난다. 완료 조건 1·2의 테스트가 그 안에 있다
  - 확인: `<임시>`에 `bin/gh`(받은 인자를 한 줄에 하나씩 `<임시>/args`에 덧붙이는 셸 스크립트, 실행 권한)를 둔다. 제목 `` `plate:plan`이 $(touch <임시>/pwned) 'x' "y" ``를 본문이 정한 넘기는 법대로 넣어 `gh issue list --search`, `gh issue create --title`, `gh pr create --title`의 명령 줄 셋을 `<임시>/run.sh`에 쓰고, `PATH=<임시>/bin:$PATH sh <임시>/run.sh`로 돌린다. `<임시>/args`에 그 제목과 바이트까지 같은 줄이 세 번 있고, `<임시>/pwned`가 없다
  - 확인: `git grep -n 'TOOLS.md' -- plugins/`가 아무것도 내지 않는다

## 한 일
- 1번 tasks 브랜치 항목: 지금 브랜치가 `tasks/<이름>`이면 그대로 실행하고, 기본 브랜치도 `tasks/<이름>`도 아니면 지금 브랜치를 보여 주고 `tasks/<이름>`으로 바꿀지 묻고 멈추게 했다. 답은 물은 자리 `브랜치`로 `RUNLOG.md`에 적고, 승인하면 만들거나 바꿔 잇고, 거절하면 실행하지 않고 그 줄만 더하고 끝난다. "기본 브랜치가 아니면 만들지 않고 지금 브랜치에서 실행한다"는 지웠다 (`plugins/plate/skills/run/SKILL.md`)
- `RUNLOG.md` 절의 물은 자리 목록과 task에 걸리지 않는 물음 목록에 `커밋하지 않은 변경` 뒤, `기본 브랜치` 앞에 `브랜치`를 더했다 (`plugins/plate/skills/run/SKILL.md`)
- 0번: tasks 머리가 없으면 `git branch --show-current`, `git log -1 --format=%s`, `git show HEAD^:docs/tasks/plan.md`를 따로 돌려 가르고, 지금 브랜치가 `tasks/<이름>`이고 마지막 커밋 제목이 `<이름>: 비움`이면 1번부터 하지 않고 origin에 따라 "PR을 연다"나 "합친다"로 가게 했다. PR에 쓸 글(고침 task 머리를 찾는 법까지)은 비움 커밋의 부모에서 읽는다. "PR을 연다"와 "합친다"의 첫 문장에 0번의 재개에서도 온다는 것을 더했다 (`plugins/plate/skills/run/SKILL.md`)
- "합친다": 2번을 이 자리만의 물음(파일 목록을 보여 주고 그대로 합칠지 묻고 멈춘다, `RUNLOG.md`에 적지 않는다, 거절하면 10번)으로 바꾸고, 3번에 `git switch {기본 브랜치}`가 실패하면 합치지 않고 실패한 명령과 오류를 보고에 적고 10번으로 가는 갈래를 더했다. 10번 보고의 합치지 않은 까닭에 `git switch`의 실패도 더했다 (`plugins/plate/skills/run/SKILL.md`)
- `RunRulesTest`에 `test_branch_question_when_not_default_or_tasks_branch`, `test_resume_after_clearing_goes_to_pr_or_merge`, `test_merge_has_own_question_and_switch_failure`, `test_branch_in_question_lists`를 더했다 (`tests/test_skill_rules.py`)
- 맥락 문서와 README: ARCHITECTURE `## 패턴과 규칙`의 run 브랜치 줄에 브랜치 물음과 비운 뒤의 재개·합침 물음을, `## 데이터 흐름`의 실행 단계에 브랜치 물음 줄을, tasks 끝에 재개 줄을, `## 디렉터리 구조`의 `test_skill_rules.py` 줄에 새 테스트가 다루는 규칙을 더했다. README 스킬 표 `run` 행에 두 갈래를, `## tasks 끝의 PR`에 두 갈래를 더했다. PRD 핵심 기능 8의 PR 문장 뒤에 두 갈래를 더했다 (`docs/ARCHITECTURE.md`, `README.md`, `docs/PRD.md`)

## 확인 결과
- 브랜치와 재개가 완료 조건 3대로다
  - `python3 -m unittest discover -s tests` → `Ran 177 tests`, `OK`. `-v`로 `test_branch_question_when_not_default_or_tasks_branch`, `test_resume_after_clearing_goes_to_pr_or_merge`, `test_merge_has_own_question_and_switch_failure`, `test_branch_in_question_lists`가 `ok`. 통과
  - `mktemp -d`의 `<임시>/g`에 `git init -b main`, `docs/tasks/plan.md`(`# 시험 tasks`, `**이름**: demo`) 커밋, `git switch -c tasks/demo`, `git rm` 뒤 `demo: 비움` 커밋. 0번의 세 명령 → `tasks/demo`, `demo: 비움`, `# 시험 tasks`. `git commit --allow-empty -m 'demo: RUNLOG'` 뒤 다시 → `tasks/demo`, `demo: RUNLOG`(비움이 아니어서 재개 갈래로 가지 않는다). 통과
  - 다섯 곳을 읽음 → ARCHITECTURE `## 패턴과 규칙` run 줄(브랜치 물음과 비운 뒤 PR·합침), `## 데이터 흐름` 실행 단계 브랜치 줄(브랜치 물음), README `run` 행(두 갈래), README `## tasks 끝의 PR`(두 갈래), PRD 기능 8 PR 문장(두 갈래). 통과
- 앞 phase가 이룬 규칙이 그대로다
  - `python3 -m unittest discover -s tests` → `OK`. 완료 조건 1의 `test_issue_text_is_data_only`, `test_text_passing_rule_in_one_place`, `test_issue_list_filters_by_body_without_narrowing_limit`, `test_pr_question_shows_comment_text`와 완료 조건 2의 `test_state_tables_row_order`, `test_three_failure_resume_goes_to_fix_phase_for_retro`, `test_state_reading_and_stop_line_rows`, `test_runlog_reason_for_respawn`이 `ok`. 통과
  - `<임시>/bin/gh`(인자를 한 줄씩 `<임시>/args`에 덧붙임, 실행 권한)를 두고, 제목 `` `plate:plan`이 $(touch <임시>/pwned) 'x' "y" ``를 낱말의 "글을 넘기는 법"대로(작은따옴표로 감싸고 안의 `'`를 `'\''`로) 넣은 `gh issue list --search`, `gh issue create --title`, `gh pr create --title` 세 줄을 `<임시>/run.sh`에 써서 `PATH=<임시>/bin:$PATH sh <임시>/run.sh` → `grep -cxFf <임시>/title <임시>/args`가 `3`, `ls <임시>/pwned`가 `No such file or directory`. 통과
  - `git grep -n 'TOOLS.md' -- plugins/` → 출력 없음(종료 1). 통과

## 계획과 달라진 점
- 없음

## 남은 것
- 0번의 재개 갈래는 비움 커밋이 마지막 커밋일 때만 탄다. 비운 뒤 사람이 그 브랜치에 커밋을 더하면 재개하지 않고 "계획이 없다"로 끝난다(완료 조건이 정한 대로다)
- 재개에서 이미 PR을 연 브랜치로 다시 부르면 `gh pr create`가 실패해 지금 규칙대로 보고에 적는다(task 머리의 범위 밖)
- 1번에서 `tasks/<이름>`이 없을 때 승인하면 `git switch -c`가 지금(기본 브랜치가 아닌) 브랜치의 끝에서 갈라진다. 그 브랜치의 커밋도 tasks 브랜치에 든다
- eval 본문 `낱말`의 "정해 둔 물음" 목록에는 `브랜치`가 없다. eval은 run의 목록을 따른다고 적혀 있어 task 머리 범위 밖대로 고치지 않았다

## 하네스에서 걸린 것
- 없음
