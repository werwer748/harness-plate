# 회고

## 회고 1

**확인**
- 스킬 본문을 고치는 tasks에서 phase의 수행과 확인은 run이 넘긴 판의 본문을 따르고, 고친 본문의 동작은 헤드리스 시험으로 본다는 규칙이 `AGENTS.md` 작업 규칙에 있고, 그 까닭이 `docs/TOOLS.md`에 있다
  - `grep -cF -e 'run이 넘긴 판' AGENTS.md` → `1`, `grep -cF -e '작업 트리의 스킬 줄' docs/TOOLS.md` → `2`. 통과
- zsh에서 `=`로 시작하는 낱말이 확장되니 구분 줄은 따옴표로 감싸거나 `=`로 시작하지 않게 쓴다는 것이 `docs/TOOLS.md`에 있다
  - ``grep -cF -e '`=` 확장' docs/TOOLS.md`` → `1`. 통과 (적힌 사실도 `zsh -c 'echo ===='`로 돌려 `zsh:1: === not found`, 종료 코드 1을 봄)
- tasks 완료 조건 4, 5가 참이다
  - `python3 -m unittest discover -s tests` → `Ran 198 tests`, 마지막 줄 `OK`. 통과
  - 다섯 시험을 저마다 `mktemp -d` 폴더에 `cp -R plugins tests`로 만든 새 사본에서 함. 다섯 글 모두 사본 파일에 `grep -cF -e` → `1`, 그 글을 빈 글로 바꾸고 사본에서 `python3 -m unittest discover -s tests`를 돌린 출력에 `FAIL: test_69_fix_check_command_and_record (test_skill_rules.PhaseRulesTest`, `FAIL: test_69_run_check_as_written (test_skill_rules.CheckRulesTest`, `FAIL: test_69_run_check_as_written (test_skill_rules.RetroRulesTest`, `FAIL: test_70_test_files_do_not_pick_default_table (test_skill_rules.ReviewRulesTest`, `FAIL: test_68_check_commands_run_as_written (test_skill_rules.PlanRulesTest`가 저마다 1줄. 통과
  - `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "0.21.0",`. 통과
  - `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
  - `docs/ARCHITECTURE.md`의 `test_skill_rules.py` 줄을 뽑아 `적힌 그대로 돌지 않는 확인 명령`, `테스트 파일도 빼고 표를 고름`, `읽기만 하는 확인 명령을 초안 점검에서 돌림`을 `grep -cF -e`로 봄 → `1`, `1`, `1`. 통과
  - `sed -n '1,8p' tests/test_skill_rules.py` → plan의 `#68`, phase의 `#69`, check의 `#69`, retro의 `#69`, review의 `#70`이 있음. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 198 tests`, `OK`. 통과

**남은 것**
- phase 1: 하네스 eval 고칠 거리 4의 해결책("그 phase 시작 때의 본문(커밋된 판)")과 task 머리 완료 조건 1의 "run이 넘긴 판"이 run이 작업 트리의 스킬 줄을 붙일 때 갈린다 → 문제 아님 (task 머리 완료 조건 1이 "run이 넘긴 판"으로 정했고, 완료 조건이 바꾸기로 한 줄과의 어긋남은 문제로 적지 않는다. `AGENTS.md`의 줄과 `docs/TOOLS.md`의 까닭은 서로 맞는다)

**문제**
- 없음

**판정**: 통과
