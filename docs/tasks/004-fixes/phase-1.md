# Phase 1: tasks 끝의 문제를 고친다

**목표**: task 머리의 완료 조건에 적힌 것을 모두 고친다.

**테스트 먼저**: 아니오 — 고칠 것이 회귀 테스트를 더하는 것과 TOOLS.md 한 줄이고, 스킬 본문의 동작은 바꾸지 않아 먼저 실패할 테스트가 없다

**읽을 것**
- `docs/tasks/review.md`의 `## 평가 1` 절
- `docs/tasks/eval.md`의 `## eval 1` 절
- `plugins/plate/skills/run/SKILL.md`의 낱말 "글을 넘기는 법"과 3번 "상태를 읽는 법"
- `tests/test_skill_rules.py`
- `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `docs/BACKLOG.md`, `docs/cleanup/2026-10-28.md`

**TODO**
- [x] run 3번 "상태를 읽는 법"의 `awk` 명령을 본문에서 뽑아 시험 파일(코드 블록 속 판정 줄, TODO 속 `## 확인 1`, 판정 줄 없는 마지막 절)에 돌리는 테스트와, 낱말 "글을 넘기는 법"대로 따옴표·백틱·`$(…)`가 든 제목을 가짜 `gh`에 넘겨 한 인자로 그대로 닿고 치환이 돌지 않음을 보는 테스트를 더한다. `docs/ARCHITECTURE.md`에 테스트 설명이 있으면 그 줄도 맞춘다 (`tests/test_skill_rules.py`, `docs/ARCHITECTURE.md`)
- [x] `docs/TOOLS.md`의 `## Claude Code` 첫 목록에 "한글 본문을 `python3 -` heredoc으로 고치면 `SyntaxError: Non-UTF-8 code`로 깨질 수 있다. Edit 도구나 `python3 -c`, 파일로 쓴 스크립트를 쓴다"를 확인한 버전과 함께 한 줄로 더한다 (`docs/TOOLS.md`)

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다

## 한 일
- run 3번 "상태를 읽는 법"의 `awk` 명령 테스트와 "글을 넘기는 법"의 가짜 `gh` 테스트를 더한다: `RunRulesTest`에 두 테스트를 더했다. `test_state_reading_awk_runs_on_trap_files`는 3번 절에서 `awk -v h='확인' … docs/tasks/NNN-slug/phase-N.md` 줄을 뽑아 경로를 임시 파일로 바꿔 `sh -c`로 돌리고, 세 시험 파일(4백틱 블록 속 3백틱 줄·`## 확인 1`·판정 줄·`- [ ]`, TODO 속 `` `## 확인 1` ``, 기록 절 뒤의 체크 상자, 마지막 절 뒤 코드 블록 속 판정 줄, `h='회고'`의 retro)의 출력 한 줄을 글자까지 견준다. `test_text_passing_rule_survives_fake_gh`는 낱말의 "글을 넘기는 법"에서 바꾸는 글(`'\''`)과 예(`it's` → `'it'\''s'`)를 뽑아 예가 맞는지 보고, 본문의 `'{…}'`가 든 `gh issue list`·`gh issue create`·`gh pr create` 명령 셋에 백틱·`$(touch pwned)`·작은따옴표·큰따옴표·`$HOME`이 든 제목을 넣어 가짜 `gh`(인자를 JSON으로 적는 스크립트)로 돌리고, 제목이 한 인자로 그대로 닿고 `pwned`·`pwned2`가 생기지 않음을 본다. 표준 라이브러리 `json`, `os`, `shlex`, `subprocess`, `sys`, `tempfile`을 불러온다. `docs/ARCHITECTURE.md`의 `test_skill_rules.py` 줄 끝에 이 두 테스트의 설명을 더했다 (`tests/test_skill_rules.py`, `docs/ARCHITECTURE.md`)
- `docs/TOOLS.md`의 `## Claude Code` 첫 목록에 heredoc 한 줄을 더한다: `git clone` 줄 앞에 "한글 본문을 `python3 -` heredoc으로 고치면 `SyntaxError: Non-UTF-8 code`로 깨질 수 있다. Edit 도구나 `python3 -c`, 파일로 쓴 스크립트를 쓴다. 늘 깨지지는 않아 같은 꼴이 돈 때도 있다(2.1.312)."를 더했다. 버전은 이 세션의 `claude --version`(2.1.312)이고, 이 세션에서 `python3 - <<'EOF'`로 `print("한글")`을 돌리면 깨지지 않고 돌아서 "늘 깨지지는 않아"를 붙였다 (`docs/TOOLS.md`)

## 확인 결과
- task 머리 완료 조건 1: 새 두 테스트가 run 본문에서 명령을 뽑아 임시 폴더에서 돌리고 전체가 `OK`, 바꾼 사본에서 실패
  - `python3 -m unittest tests.test_skill_rules -k awk_runs -k fake_gh -v` → 두 테스트 `ok`, `Ran 2 tests`, `OK`
  - `python3 -m unittest discover -s tests` → `Ran 192 tests in 17.182s`, `OK`
  - 스크래치 폴더에 `tests/`와 `plugins/`를 베낀 사본 셋에서 `python3 -m unittest tests.test_skill_rules`:
    - m1(`awk`의 `f != "" { next }`를 `f != "" { }`로) → `FAIL: test_state_reading_awk_runs_on_trap_files` 세 case, `FAILED (failures=3)`. 옛 테스트는 이 바꿈을 잡지 못한다
    - m2(`$0 ~ ("^## " h " [0-9]+$")`를 `$0 ~ ("## " h " [0-9]+")`로) → `FAIL: test_state_reading_awk_runs_on_trap_files (case='phase_with_traps')`와 `test_state_reading_and_stop_line_rows`, `FAILED (failures=2)`
    - m3(`'\''`와 예 `'it'\''s'`를 `\'`와 `'it\'s'`로) → `FAIL: test_text_passing_rule_survives_fake_gh` 세 template, `FAILED (failures=4)`
  - 통과
- task 머리 완료 조건 2: `grep -c 'Non-UTF-8' docs/TOOLS.md` → 1, `wc -c < docs/TOOLS.md` → 14527(≤ 15360). 통과
- task 머리 완료 조건 3 (tasks 완료 조건 1~4)
  - `python3 -m unittest discover -s tests` → `OK`(192개). 통과
  - `wc -c < docs/TOOLS.md` → 14527. 통과
  - 네 절 이름마다 `grep -c` → 1, 1, 1, 1. 통과
  - `grep -cE '/var/folders/|tmp\.[A-Za-z0-9]{6,}|장면 [A-Z]' docs/TOOLS.md` → 0. 통과
  - `git grep -n 'TOOLS.md' -- plugins/` → 출력 없음(종료 1). 통과
  - `git grep -nE '사용량.*TOOLS\.md|TOOLS\.md.*사용량' -- docs/PRD.md docs/ARCHITECTURE.md docs/ADR.md README.md AGENTS.md` → 출력 없음(종료 1). 통과
  - `grep -c '처리: plan으로 넘김' docs/cleanup/2026-10-28.md` → 29. 보고서에서 `처리: plan으로 넘김`이 붙은 발견 번호를 뽑고 세 task 머리(`001-tools-doc`, `002-run-rules`, `003-plan-rules`)의 `## 완료 조건`에서 발견 번호를 모으는 스크립트(스크래치 `c4.py`) → `29`, `29 True []`. 통과
  - 세 `retro.md`의 마지막 회고 절(`## 회고 1`)의 판정 → 셋 다 `**판정**: 통과`. 통과

## 계획과 달라진 점
- 없음

## 남은 것
- `test_text_passing_rule_survives_fake_gh`는 본문의 `'{…}'` 자리만 제목으로 채우고 다른 자리(`{기본 브랜치}`, `<이름>` 따위)는 `x`로 채운다. 본문·댓글의 `--body-file` 넘기기와 임시 파일 지우기는 돌려 보지 않는다
- `awk` 테스트는 이 macOS의 `/usr/bin/awk`(BSD awk)에서만 돌려 봤다. gawk·mawk에서의 동작은 보지 않았다
- `docs/TOOLS.md`의 heredoc 줄의 2.1.312는 이 세션의 버전이다. `002-run-rules` phase 1에서 깨졌을 때의 버전은 기록에 없어, 그때도 2.1.312였는지는 확인하지 못했다. 이 세션에서는 재현되지 않았다

## 하네스에서 걸린 것
- heredoc 줄의 확인한 버전을 적으려고, 읽을 것에 없는 `docs/tasks/002-run-rules/done-phase-1.md`의 해당 줄을 `grep`으로 한 줄 보고 그 커밋 시각을 `git log`로 봤다. 다른 task의 기록이라 앞 phase 기록 읽지 않음 규칙에는 들지 않지만, 계획의 읽을 것에 버전의 출처가 없었다

## 확인 1

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 완료 조건 1: `python3 -m unittest tests.test_skill_rules -k awk_runs -k fake_gh -v` → 두 테스트 `ok`, `Ran 2 tests`, `OK`. `python3 -m unittest discover -s tests` → `Ran 192 tests`, `OK`. 스크래치 폴더에 `tests/`, `plugins/`, `docs/` 등을 베낀 사본 셋에서 run 본문을 바꿔 `python3 -m unittest tests.test_skill_rules`: m1(`f != "" { next }` → `f != "" { }`) → `test_state_reading_awk_runs_on_trap_files` 세 case 실패, `FAILED (failures=3)`. m2(`$0 ~ ("^## " h " [0-9]+$")` → `$0 ~ ("## " h " [0-9]+")`) → `test_state_reading_awk_runs_on_trap_files`(phase_with_traps)와 `test_state_reading_and_stop_line_rows` 실패, `FAILED (failures=2)`. m3(`'\''`와 예 `'it'\''s'`를 `\'`와 `'it\'s'`로) → `test_text_passing_rule_survives_fake_gh` 세 template과 `test_text_passing_rule_in_one_place` 실패, `FAILED (failures=4)`. 통과
  - 완료 조건 2: `grep -c 'Non-UTF-8' docs/TOOLS.md` → 1, `wc -c < docs/TOOLS.md` → 14527(≤ 15360). 통과
  - 완료 조건 3 / tasks 완료 조건 1: `python3 -m unittest discover -s tests` → `OK`. 통과
  - 완료 조건 3 / tasks 완료 조건 2: `wc -c < docs/TOOLS.md` → 14527. 네 절 이름마다 `grep -c` → 1, 1, 1, 1. `grep -cE '/var/folders/|tmp\.[A-Za-z0-9]{6,}|장면 [A-Z]' docs/TOOLS.md` → 0. 통과
  - 완료 조건 3 / tasks 완료 조건 3: `git grep -n 'TOOLS.md' -- plugins/` → 출력 없음(종료 1). `git grep -nE '사용량.*TOOLS\.md|TOOLS\.md.*사용량' -- docs/PRD.md docs/ARCHITECTURE.md docs/ADR.md README.md AGENTS.md` → 출력 없음(종료 1). 통과
  - 완료 조건 3 / tasks 완료 조건 4: `grep -c '처리: plan으로 넘김' docs/cleanup/2026-10-28.md` → 29. 보고서의 `- **{기준}-N**` 머리 아래 `처리: plan으로 넘김`이 붙은 번호 29개(중복 없음)와 세 task 머리(`001-tools-doc`, `002-run-rules`, `003-plan-rules`)의 `## 완료 조건`에서 모은 발견 번호 29개가 같다(차집합 없음). 세 `retro.md`의 마지막 회고 절 `## 회고 1`의 판정 → 셋 다 `**판정**: 통과`. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 192 tests in 17.172s`, `OK`. 통과

**남은 것**
- `test_text_passing_rule_survives_fake_gh`는 `--body-file` 넘기기와 임시 파일 지우기를 돌려 보지 않는다 → 완료 조건 1이 보는 것은 제목·검색어의 작은따옴표 넘기기이고 본문 넘기기는 보지 않아 걸리지 않는다. 하네스에서 걸린 것
- `awk` 테스트를 BSD awk에서만 돌려 봤다 → 완료 조건 1의 확인은 이 환경에서 테스트를 돌려 `OK`인지와 바꾼 사본에서 실패하는지이고, 다른 awk 구현은 보지 않아 걸리지 않는다. 하네스에서 걸린 것
- heredoc 줄의 2.1.312가 깨졌을 때의 버전인지 확인하지 못했다 → 완료 조건 2의 확인(`grep -c`, `wc -c`)이 보는 동작에 걸리지 않는다. 하네스에서 걸린 것

**실패**
- 없음

**하네스에서 걸린 것**
- 남은 것: `test_text_passing_rule_survives_fake_gh`는 본문·댓글의 `--body-file` 넘기기와 임시 파일 지우기를 돌려 보지 않는다
- 남은 것: `awk` 테스트는 macOS의 BSD awk에서만 돌려 봤고 gawk·mawk에서의 동작은 보지 않았다
- 남은 것: `docs/TOOLS.md`의 heredoc 줄의 2.1.312는 이 세션의 버전이고, `002-run-rules` phase 1에서 깨졌을 때의 버전인지는 확인하지 못했다(이 세션에서는 재현되지 않았다)
- 완료 조건 1의 "바꾼 사본에서 실패한다"는 확인이 명령으로 적혀 있지 않아, 확인하는 쪽이 바꿀 글과 사본의 꼴을 스스로 정해야 했다

**판정**: 통과
