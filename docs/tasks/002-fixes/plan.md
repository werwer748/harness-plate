# tasks 끝의 문제를 고친다

## 목표
tasks 끝의 코드 평가와 하네스 eval에서 고치기로 한 것을 모두 고친다.

## 범위 밖
- 코드 평가와 하네스 eval을 다시 하는 것
- plate 자체의 하네스 고칠 거리를 고치는 것. 이슈로 올리고 plate 저장소에서 고친다

## 완료 조건
1. 스킬 본문을 고치는 tasks에서 phase의 수행과 확인은 run이 넘긴 판(이름으로 부르면 세션에 실린 판, 작업 트리의 스킬 줄이 붙으면 작업 트리의 판)의 본문을 따르고, 고친 본문의 동작은 헤드리스 시험(작업 트리의 `--plugin-dir`)으로 본다는 규칙이 `AGENTS.md` 작업 규칙에 있고, 그 까닭이 `docs/TOOLS.md`에 있다 (`AGENTS.md`, `docs/TOOLS.md`)
   - 확인: `grep -cF -e 'run이 넘긴 판' AGENTS.md`가 `1`이고, `grep -cF -e '작업 트리의 스킬 줄' docs/TOOLS.md`가 `1` 이상이다
2. zsh에서 `=`로 시작하는 낱말이 확장되니 구분 줄은 따옴표로 감싸거나 `=`로 시작하지 않게 쓴다는 것이 `docs/TOOLS.md`에 있다 (`docs/TOOLS.md`)
   - 확인: ``grep -cF -e '`=` 확장' docs/TOOLS.md``가 `1` 이상이다
3. tasks 완료 조건 4, 5가 참이다.
   - tasks 완료 조건 4: 고친 글이 빠지면 실패하는 테스트가 있고, 모든 테스트가 통과한다
     - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
     - 확인: 아래 다섯 시험을 저마다 새 사본(`mktemp -d`로 만든 폴더에 작업 트리의 `plugins`와 `tests`를 `cp -R`로 복사한 것)에서 한다. 그 글이 사본의 파일에 한 번 있는지 보고(없으면 실패), 그 글을 빈 글로 바꾸고 사본에서 `python3 -m unittest discover -s tests`를 돌리면 출력에 그 테스트의 `FAIL:` 줄이 있다. phase 본문의 `고친 명령과 까닭을 "계획과 달라진 점"과 "하네스에서 걸린 것"에 적는다` → `FAIL: test_69_fix_check_command_and_record (test_skill_rules.PhaseRulesTest`, check 본문의 `적힌 명령, 고친 명령, 까닭을 "하네스에서 걸린 것"에 적는다` → `FAIL: test_69_run_check_as_written (test_skill_rules.CheckRulesTest`, retro 본문의 `적힌 명령, 고친 명령, 까닭을 "확인"의 결과에 적고 5번의 문제로 모은다` → `FAIL: test_69_run_check_as_written (test_skill_rules.RetroRulesTest`, review 본문의 `테스트 파일은 바뀐 동작이 아니라 그 근거라 표를 고를 때 세지 않는다` → `FAIL: test_70_test_files_do_not_pick_default_table (test_skill_rules.ReviewRulesTest`, plan 본문의 `읽기만 하는 확인 명령(파일이나 저장소를 바꾸지 않는 것)을 돌려 적힌 그대로 도는지 본다` → `FAIL: test_68_check_commands_run_as_written (test_skill_rules.PlanRulesTest`
   - tasks 완료 조건 5: 두 매니페스트의 버전이 0.21.0이고, 마켓플레이스가 유효하고, 문서와 테스트 설명이 바뀐 규칙과 맞는다
     - 확인: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json`의 두 줄이 모두 `0.21.0`
     - 확인: `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
     - 확인: `docs/ARCHITECTURE.md`의 `test_skill_rules.py` 줄에 `적힌 그대로 돌지 않는 확인 명령`, `테스트 파일도 빼고 표를 고름`, `읽기만 하는 확인 명령을 초안 점검에서 돌림`이 저마다 든다. 한 글이라도 빠지면 실패
     - 확인: `sed -n '1,8p' tests/test_skill_rules.py`의 목록에 plan의 `#68`, phase·check·retro의 `#69`, review의 `#70`이 있다. 하나라도 없으면 실패

## 결정
- 없음
