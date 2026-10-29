# Phase 2: run의 계획 커밋 차례, 이슈 판정, 멈춤 grep 시험

**목표**: 신뢰성-8, 기존 작업 정합성-5·7이 고쳐진다.

**테스트 먼저**: 아니오 — 스킬 본문(`.md`)과 그 글을 지키는 테스트만 고친다

**읽을 것**
- `docs/cleanup/2026-10-29.md` (신뢰성-8, 기존 작업 정합성-5·7의 근거와 고치는 방향)
- `plugins/plate/skills/run/SKILL.md`의 "1. 시작 조건을 본다", "3. 갈 곳을 정한다"(`멈춤` 줄 grep), "이슈를 올린다", "PR을 연다"의 "PR 본문의 꼴" 절, 낱말의 "글을 넘기는 법"
- `docs/ARCHITECTURE.md`의 "패턴과 규칙" 절의 run 이슈·PR 문단("run은 기본 브랜치(`origin`의 HEAD…"로 시작하는 문단)과 디렉터리 구조의 `test_skill_rules.py` 줄
- `tests/test_skill_rules.py` (`RunRulesTest`의 `test_state_reading_and_stop_line_rows`, 이슈 글을 데이터로 보는 시험)
- `docs/TOOLS.md`의 "GitHub와 claude-code-action" 항목

**TODO**
- [x] 1번의 git 레포 셋의 차례가 커밋하지 않은 변경, tasks 브랜치, 계획의 커밋으로 바뀌고, 계획의 커밋이 정한 `tasks/<이름>`에 들어간다고 적힌다 (`plugins/plate/skills/run/SKILL.md`)
- [x] "이슈를 올린다" 2번이 `gh api user --jq .login`으로 얻은 login이 쓴 본문(`gh issue view {번호} --repo werwer748/harness-plate --json author,comments`의 `author.login`)과 댓글(`comments[].author.login`)에 tasks 이름이 있을 때만 올리지 않게 바뀐다. login을 얻지 못하면 이미 있지 않은 것으로 본다 (`plugins/plate/skills/run/SKILL.md`)
- [x] "PR 본문의 꼴"의 "올린 이슈"를 찾는 글이 같은 규칙을 따른다고 바뀐다 (`plugins/plate/skills/run/SKILL.md`)
- [x] `RunRulesTest.test_stop_line_grep_runs_on_fake_runlog`가 더해진다: 3번 본문에서 두 grep 명령을 뽑아, 다른 자리와 같은 자리의 `멈춤` 줄이 섞인 가짜 `RUNLOG.md`에 돌려 그 자리의 마지막 줄만 나오는지 본다 (`tests/test_skill_rules.py`)
- [x] 1번 차례와 이슈 판정의 글을 지키는 시험이 더해지거나 바뀐 글로 고쳐진다 (`tests/test_skill_rules.py`)
- [x] ARCHITECTURE의 run 이슈·PR 문단에 "이미 있음"을 `gh api user`의 login이 쓴 글로 좁힌다는 것이, `test_skill_rules.py` 줄에 새 시험이 더해진다 (`docs/ARCHITECTURE.md`)

**통과 조건**
- 계획 커밋이 브랜치 뒤다(완료 조건 2).
  - 확인: `grep -n -e '\*\*tasks 브랜치\.\*\*' -e '\*\*계획의 커밋\.\*\*' plugins/plate/skills/run/SKILL.md` → `tasks 브랜치`의 줄 번호가 더 작다
- 이슈 판정이 login의 글로 좁혀진다(완료 조건 3).
  - 확인: `grep -n 'gh api user' plugins/plate/skills/run/SKILL.md` → "이슈를 올린다"와 "PR 본문의 꼴"에 저마다 한 줄 이상
  - 확인: `gh api user --jq .login` → login 한 줄. `gh issue view 68 --repo werwer748/harness-plate --json author,comments --jq '.author.login'` → login 한 줄
- 멈춤 grep이 돈다(완료 조건 4).
  - 확인: `python3 -m unittest tests.test_skill_rules.RunRulesTest.test_stop_line_grep_runs_on_fake_runlog -v` → `OK`
  - 확인: 작업 트리를 `cp -R`로 `mktemp -d` 사본에 옮기고, 사본의 run 본문에서 ``grep '^- 물음 | 멈춤 | `NNN-slug` phase N 확인 ' docs/tasks/RUNLOG.md | tail -n 1``을 ``grep '^- 물음 | 멈춤 | `NNN-slug` phase N ' docs/tasks/RUNLOG.md | tail -n 1``로 바꿔 사본에서 그 시험 → 실패(`FAILED`)
- 앞 phase의 동작이 그대로다(완료 조건 1).
  - 확인: `python3 -m unittest tests.test_skill_rules.RunRulesTest.test_no_result_relaunch_limit -v` → `OK`
- 맥락 문서가 맞다(완료 조건 8의 뒤 절).
  - 확인: `grep -n 'gh api user' docs/ARCHITECTURE.md` → run 이슈·PR 문단에 한 줄 이상
- 테스트 묶음이 통과한다.
  - 확인: `python3 -m unittest discover -s tests` → 마지막 줄이 `OK`

## 한 일
- 1번의 git 레포 셋의 차례가 커밋하지 않은 변경, tasks 브랜치, 계획의 커밋으로 바뀌고, 계획의 커밋이 정한 `tasks/<이름>`에 들어간다고 적힌다: 셋의 번호와 차례를 바꾸고, 1번(커밋하지 않은 변경)이 한 번도 커밋되지 않은 계획 파일을 세지 않으며, 3번(계획의 커밋)이 "2번이 정한 `tasks/<이름>`에서 커밋한다"와 그 까닭을 적는다 (`plugins/plate/skills/run/SKILL.md`)
- "이슈를 올린다" 2번이 login이 쓴 본문과 댓글로 좁혀진다: `gh api user --jq .login`의 login, `gh issue view {번호} --repo werwer748/harness-plate --json author,comments`의 `author.login`(본문)·`comments[].author.login`(댓글), 다른 사람의 글은 이미 있음으로 보지 않음, login을 얻지 못하면 이미 있지 않은 것으로 봄을 적었다 (`plugins/plate/skills/run/SKILL.md`)
- "PR 본문의 꼴"의 "올린 이슈": "이슈를 올린다"의 2번처럼 `gh api user --jq .login`의 login이 쓴 본문이나 댓글에 tasks 이름이 있는 이슈의 주소만 쓰고, login을 얻지 못하면 없는 것으로 본다고 바꿨다 (`plugins/plate/skills/run/SKILL.md`)
- `RunRulesTest.test_stop_line_grep_runs_on_fake_runlog`를 더했다: 3번 본문에서 두 grep 명령을 정규식으로 뽑아 `NNN-slug`·`phase N `을 채우고, 다른 task·다른 phase(`phase 12`)·줄 머리가 아닌 줄·같은 phase의 다른 자리(`phase 2 수행`)·자리 없는 `멈춤` 줄이 섞인 가짜 `docs/tasks/RUNLOG.md`에서 그 자리의 마지막 줄만 나오는지 본다 (`tests/test_skill_rules.py`)
- 1번 차례와 이슈 판정의 글을 지키는 시험: `test_plan_commit_after_tasks_branch`(세 항목의 차례와 계획을 tasks 브랜치에 커밋하는 글), `test_issue_already_exists_only_by_login`(이슈를 올린다 2번과 PR 본문의 꼴의 login 글, 옛 글이 없음)을 더했다 (`tests/test_skill_rules.py`)
- ARCHITECTURE의 run 이슈·PR 문단에 "이미 있음"을 `gh api user`의 login이 쓴 본문·댓글로 좁힌다는 것과 1번의 새 차례를 더하고, `test_skill_rules.py` 줄에 새 시험 셋을 더했다 (`docs/ARCHITECTURE.md`)

## 확인 결과
- 계획 커밋이 브랜치 뒤다(완료 조건 2).
  - `grep -n -e '\*\*tasks 브랜치\.\*\*' -e '\*\*계획의 커밋\.\*\*' plugins/plate/skills/run/SKILL.md` → `89:2. **tasks 브랜치.**`, `96:3. **계획의 커밋.**`. 89 < 96. 통과
- 이슈 판정이 login의 글로 좁혀진다(완료 조건 3).
  - `grep -n 'gh api user' plugins/plate/skills/run/SKILL.md` → 376행("이슈를 올린다" 2번), 519행("PR 본문의 꼴"의 올린 이슈). 통과
  - `gh api user --jq .login` → `werwer748`. `gh issue view 68 --repo werwer748/harness-plate --json author,comments --jq '.author.login'` → `werwer748`. 통과
- 멈춤 grep이 돈다(완료 조건 4).
  - `python3 -m unittest tests.test_skill_rules.RunRulesTest.test_stop_line_grep_runs_on_fake_runlog -v` → `OK`. 통과
  - 작업 트리를 `cp -R`로 `mktemp -d` 사본에 옮기고 사본의 run 본문에서 phase grep을 ``grep '^- 물음 | 멈춤 | `NNN-slug` phase N ' docs/tasks/RUNLOG.md | tail -n 1``로 바꿔 같은 시험 → `FAILED (failures=1)`. 사본은 지웠다. 통과
- 앞 phase의 동작이 그대로다(완료 조건 1).
  - `python3 -m unittest tests.test_skill_rules.RunRulesTest.test_no_result_relaunch_limit -v` → `OK`. 통과
- 맥락 문서가 맞다(완료 조건 8의 뒤 절).
  - `grep -n 'gh api user' docs/ARCHITECTURE.md` → 56행(run 이슈·PR 문단). 통과
- 테스트 묶음이 통과한다.
  - `python3 -m unittest discover -s tests` → `Ran 233 tests`, 마지막 줄 `OK`. 통과

## 계획과 달라진 점
없음

## 남은 것
- 계획 파일을 커밋하지 않은 채 이미 있는 `tasks/<이름>`으로 `git switch`할 때, 그 브랜치에 같은 경로의 추적 파일이 있으면 switch가 실패할 수 있다. 본문은 이 실패 갈래를 따로 다루지 않는다(plan은 처음부터 tasks 브랜치에 커밋해 옛 계획이나 손으로 쓴 계획일 때만 난다)
- 이슈의 "이미 있음"을 login으로 좁혀, plate를 돌린 계정이 아닌 사람이 같은 tasks 이름을 적은 이슈에는 댓글을 한 번 더 달 수 있다(의도한 동작)

## 하네스에서 걸린 것
없음
