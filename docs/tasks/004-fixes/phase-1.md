# Phase 1: tasks 끝의 문제를 고친다

**목표**: task 머리의 완료 조건에 적힌 것을 모두 고친다.

**테스트 먼저**: 아니오 — 테스트 이름과 docstring만 바꾸고 코드의 동작은 바꾸지 않는다

**읽을 것**
- `docs/tasks/review.md`의 `## 평가 1` 절
- `docs/tasks/eval.md`의 `## eval 1` 절
- `tests/test_skill_rules.py`
- `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `docs/BACKLOG.md`

**TODO**
- [x] retro 5번 "멈춤"의 `권한`을 보는 테스트가 `test_49_stop_list_includes_permission`으로 이름 붙고 모듈 docstring의 retro 목록에도 #50이 없어, tasks 머리가 #50의 해결로 적은 규칙의 시험을 이슈 번호로 찾을 수 없다 (`tests/test_skill_rules.py`)

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다

## 한 일
- retro 5번 "멈춤"의 `권한`을 보는 테스트가 `test_49_stop_list_includes_permission`으로 이름 붙고 모듈 docstring의 retro 목록에도 #50이 없어, tasks 머리가 #50의 해결로 적은 규칙의 시험을 이슈 번호로 찾을 수 없다 (`tests/test_skill_rules.py`): 테스트 이름을 `test_50_stop_list_includes_permission`으로 바꾸고, 모듈 docstring의 retro 목록을 `retro의 #49·#50·#51`로 고쳤다. 테스트 본문은 그대로다 (`tests/test_skill_rules.py`)

## 확인 결과
- task 머리의 완료 조건이 모두 참이다.
  - 완료 조건 1: `tests/test_skill_rules.py`를 읽음 → retro 5번 "멈춤"의 `권한`을 보는 테스트가 `RetroRulesTest.test_50_stop_list_includes_permission`이고, 모듈 docstring에 `retro의 #49·#50·#51`이 있다. 통과
  - 완료 조건 2, `python3 -m unittest discover -s tests` → `Ran 161 tests in 16.232s`, 마지막 줄 `OK`. 통과
  - 완료 조건 2, `mktemp -d`에 `git archive HEAD`를 풀고 run 본문의 첫 `부른 쪽: plate:run` 줄(4번의 맡기는 글, 130행)을 지우고 돌림 → `FAIL: test_51_marker_line_ends_every_hand_off_block (test_skill_rules.RunRulesTest) (heading='4. 수행을 맡긴다')`, `FAILED (failures=1)`. 다시 풀어 retro 5번의 #49 해결 글(앞 공백부터 " 다만 확인 절 … 회고 절의 \"문제\"가 갈린다."까지)을 지우고 돌림 → `FAIL: test_49_friction_problem_only_for_remaining_lines_judged_problem (test_skill_rules.RetroRulesTest)`, `FAILED (failures=1)`. 같은 두 확인을 이 phase의 변경을 담은 `git stash create`의 트리(`11cbc53`)로도 돌림 → 같은 두 실패. 통과
  - 완료 조건 2, `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "0.18.0",`. 통과
  - 완료 조건 2, `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
  - 완료 조건 2, `docs/PRD.md`의 7, `docs/ARCHITECTURE.md`의 "패턴과 규칙" 맡기는 글 문단(48행)과 run 문단(54행), 디렉터리 구조의 `test_skill_rules.py` 줄(39행), `README.md`의 `run` 행(10행)을 따로 읽음 → 해시로 보는 파일을 고칠 때의 멈춤, 계획 수정의 결정 줄, 맡기는 글의 표지 줄이 모두 적혀 있고, 디렉터리 구조의 줄은 규칙을 이슈 번호 없이 이름으로 적어 이번 이름 바꿈과 어긋나지 않는다. 어긋나는 줄 없음. 통과

## 계획과 달라진 점
- 없음

## 남은 것
- 없음

## 하네스에서 걸린 것
- 완료 조건 2의 `git archive HEAD` 확인은 커밋 전에 도므로 HEAD에 이 phase의 변경이 없다. 이번 변경은 run·retro 본문을 건드리지 않아 결과가 같지만, 같은 확인을 `git stash create` 트리로도 돌려 보탰다
