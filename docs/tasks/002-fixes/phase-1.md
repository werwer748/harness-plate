# Phase 1: tasks 끝의 문제를 고친다

**목표**: task 머리의 완료 조건에 적힌 것을 모두 고친다.

**테스트 먼저**: 아니오 — `AGENTS.md`와 `docs/TOOLS.md`의 `.md`만 고친다

**읽을 것**
- `docs/tasks/review.md`의 `## 평가 1` 절
- `docs/tasks/eval.md`의 `## eval 1` 절
- `AGENTS.md`
- `docs/TOOLS.md`
- `plugins/plate/skills/run/SKILL.md`의 낱말 "작업 트리의 스킬 줄"
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/ADR.md`
- `docs/BACKLOG.md`
- `docs/cleanup/`

**TODO**
- [x] 스킬 본문을 고치는 tasks에서 수행·확인은 run이 넘긴 판의 본문을 따르고 고친 본문의 동작은 헤드리스 시험으로 본다는 규칙을 `AGENTS.md` 작업 규칙에 한 줄 더하고, 그 까닭(run의 작업 트리의 스킬 줄 때문에 한 phase 안에서도 수행과 확인의 판이 갈릴 수 있다)을 `docs/TOOLS.md`에 적는다 (`AGENTS.md`, `docs/TOOLS.md`)
- [x] zsh에서 `=`로 시작하는 낱말이 확장되어 `echo ====`가 `not found`를 내니 구분 줄은 `echo '----'`처럼 쓴다는 것을 `docs/TOOLS.md`에 "셸의 `=` 확장"으로 적는다 (`docs/TOOLS.md`)

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다

## 한 일
- 스킬 본문을 고치는 tasks에서 수행·확인은 run이 넘긴 판의 본문을 따르고 고친 본문의 동작은 헤드리스 시험으로 본다는 규칙을 `AGENTS.md` 작업 규칙에 한 줄 더하고, 그 까닭을 `docs/TOOLS.md`에 적는다: `AGENTS.md` 작업 규칙의 "스킬 본문을 쓰는 tasks는 run을 시작하기 전에…" 줄 앞에 한 줄을 더함(이름으로 부르면 세션에 실린 판, 작업 트리의 스킬 줄이 붙으면 작업 트리의 판, 고친 본문의 동작은 헤드리스 시험으로 봄). `docs/TOOLS.md`의 "세션 도중의 스킬 본문 고침" 끝에 run이 맡길 때마다 바꿨는지 다시 보아 한 phase 안에서도 수행은 옛 판, 확인은 작업 트리의 스킬 줄이 가리키는 고친 판으로 돌 수 있다는 까닭을 한 줄로 더함 (`AGENTS.md`, `docs/TOOLS.md`)
- zsh에서 `=`로 시작하는 낱말이 확장되어 `echo ====`가 `not found`를 내니 구분 줄은 `echo '----'`처럼 쓴다는 것을 `docs/TOOLS.md`에 "셸의 `=` 확장"으로 적는다: Claude Code 절의 "스킬을 헤드리스로 돌려 볼 때의 허용 목록" 앞에 `**셸의 `=` 확장** (zsh, 2026-10-28)` 절을 더함. 오류 글은 `zsh -c 'echo ===='`를 돌려 나온 `zsh:1: === not found`를 그대로 적음 (`docs/TOOLS.md`)

## 확인 결과
- task 머리의 완료 조건이 모두 참이다.
  - 완료 조건 1: `grep -cF -e 'run이 넘긴 판' AGENTS.md` → `1`, `grep -cF -e '작업 트리의 스킬 줄' docs/TOOLS.md` → `2`. 통과
  - 완료 조건 2: ``grep -cF -e '`=` 확장' docs/TOOLS.md`` → `1`. 통과
  - 완료 조건 3(tasks 완료 조건 4): `python3 -m unittest discover -s tests` → `Ran 198 tests in 17.002s` / `OK`. 통과
  - 완료 조건 3(tasks 완료 조건 4): 다섯 시험을 저마다 `mktemp -d` 폴더에 `cp -R plugins tests`로 만든 새 사본에서 함. 다섯 글 모두 사본 파일에 `grep -cF -e` → `1`, 그 글을 `python3 -c`로 빈 글로 바꾸고 사본에서 `python3 -m unittest discover -s tests`를 돌린 출력에 `FAIL: test_69_fix_check_command_and_record (test_skill_rules.PhaseRulesTest`, `FAIL: test_69_run_check_as_written (test_skill_rules.CheckRulesTest`, `FAIL: test_69_run_check_as_written (test_skill_rules.RetroRulesTest`, `FAIL: test_70_test_files_do_not_pick_default_table (test_skill_rules.ReviewRulesTest`, `FAIL: test_68_check_commands_run_as_written (test_skill_rules.PlanRulesTest`가 저마다 1줄. 통과
  - 완료 조건 3(tasks 완료 조건 5): `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "0.21.0",`. 통과
  - 완료 조건 3(tasks 완료 조건 5): `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
  - 완료 조건 3(tasks 완료 조건 5): `docs/ARCHITECTURE.md`의 `test_skill_rules.py` 줄에 `적힌 그대로 돌지 않는 확인 명령`, `테스트 파일도 빼고 표를 고름`, `읽기만 하는 확인 명령을 초안 점검에서 돌림`을 `grep -cF -e`로 봄 → 저마다 `1`. 통과
  - 완료 조건 3(tasks 완료 조건 5): `sed -n '1,8p' tests/test_skill_rules.py` → `plan의 …#68`, `phase의 …#69`, `check의 …#69`, `retro의 …#69`, `review의 …#70`이 있음. 통과

## 계획과 달라진 점
없음

## 남은 것
- 하네스 eval의 고칠 거리 4는 해결책을 "그 phase 시작 때의 본문(커밋된 판)을 따른다"로 적었으나, task 머리 완료 조건 1이 "run이 넘긴 판"으로 정해 그대로 적었다. 둘은 run이 작업 트리의 스킬 줄을 붙일 때(앞 phase가 그 스킬을 고쳤을 때) 갈린다

## 하네스에서 걸린 것
없음

## 확인 1

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 완료 조건 1: `grep -cF -e 'run이 넘긴 판' AGENTS.md` → `1`, `grep -cF -e '작업 트리의 스킬 줄' docs/TOOLS.md` → `2`. 통과
  - 완료 조건 2: ``grep -cF -e '`=` 확장' docs/TOOLS.md`` → `1`. 통과
  - 완료 조건 3(tasks 완료 조건 4): `python3 -m unittest discover -s tests` → `Ran 198 tests` / 마지막 줄 `OK`. 통과
  - 완료 조건 3(tasks 완료 조건 4): 다섯 시험을 저마다 새 임시 폴더(Python `tempfile.mkdtemp`)에 작업 트리의 `plugins`와 `tests`를 복사한 사본에서 함. 다섯 글 모두 사본 파일에 1번씩 있음. 그 글을 빈 글로 바꾸고 사본에서 `python3 -m unittest discover -s tests`를 돌린 출력에 `FAIL: test_69_fix_check_command_and_record (test_skill_rules.PhaseRulesTest`, `FAIL: test_69_run_check_as_written (test_skill_rules.CheckRulesTest`, `FAIL: test_69_run_check_as_written (test_skill_rules.RetroRulesTest`, `FAIL: test_70_test_files_do_not_pick_default_table (test_skill_rules.ReviewRulesTest`, `FAIL: test_68_check_commands_run_as_written (test_skill_rules.PlanRulesTest`가 저마다 있음(시험마다 FAIL 1개). 통과
  - 완료 조건 3(tasks 완료 조건 5): `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "0.21.0",`. 통과
  - 완료 조건 3(tasks 완료 조건 5): `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
  - 완료 조건 3(tasks 완료 조건 5): `docs/ARCHITECTURE.md`의 `test_skill_rules.py` 줄을 `grep -F`로 뽑아 세 글을 저마다 `grep -cF -e`로 봄 → `1`, `1`, `1`. 통과
  - 완료 조건 3(tasks 완료 조건 5): `sed -n '1,8p' tests/test_skill_rules.py` → plan의 `#68`, phase의 `#69`, check의 `#69`, retro의 `#69`, review의 `#70`이 있음. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 198 tests`, `OK`. 통과

**남은 것**
- 없음

**실패**
- 없음

**하네스에서 걸린 것**
- 기록의 "남은 것" 줄(eval 고칠 거리 4의 해결책과 완료 조건 1의 "run이 넘긴 판"이 갈림)은 동작의 결함이나 돌려 보지 않은 위험이 아니라 계획과 eval 제안의 차이라 고르지 않음
- 완료 조건 3의 다섯 시험은 `mktemp -d`와 `cp -R` 대신 같은 일을 하는 Python의 `tempfile.mkdtemp`와 `shutil.copytree`로 새 사본을 만들어 함(대상, 패턴, 기대는 같음)

**판정**: 통과
