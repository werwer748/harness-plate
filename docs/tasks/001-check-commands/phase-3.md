# Phase 3: plan이 확인 명령이 적힌 그대로 도는지 보고, 버전을 올린다 (#68)

**목표**: 완료 조건 3이 참이 되고, 완료 조건 4와 5가 task 전체에서 참이다.

**테스트 먼저**: 아니오 — 고치는 것은 스킬 본문(`.md`)과 매니페스트의 버전 줄이고, 더하는 테스트는 그 글이 있는지를 볼 뿐 코드의 동작을 바꾸지 않는다

**읽을 것**
- `gh issue view 68 --repo werwer748/harness-plate` (원인과 해결책)
- `plugins/plate/skills/plan/SKILL.md`의 "절대 규칙" 3, "6. 초안을 보여 주고 승인받는다"의 점검 목록(읽을 것에 적은 명령을 돌려 보는 항목, 값을 뽑아 견주는 확인 항목), 적는 규칙 "조건"의 `- 확인은 돌릴 명령과 기대 결과를 우선한다.`로 시작하는 항목과 명령 예를 다루는 항목("plan은 그 확인을 미리 돌리지 않는다")
- `tests/test_skill_rules.py`의 `PlanRulesTest`와 모듈 docstring
- `plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json` (버전 줄)
- `docs/ARCHITECTURE.md` 디렉터리 구조의 `test_skill_rules.py` 줄

**TODO**
- [ ] 절대 규칙 3의 옛 글이 완료 조건 3의 새 글로 바뀌고, 같은 항목의 "읽을 것에 적는 명령은 … 읽기만 하는 명령만 적고 돌린다"와 한 뜻으로 이어진다. 명령 예를 다루는 조건 항목의 "plan은 그 확인을 미리 돌리지 않는다"와도 어긋나지 않게 맞춘다(그 확인은 시험 저장소에 쓰는 확인이라 돌리지 않는 쪽에 든다) (`plugins/plate/skills/plan/SKILL.md`)
- [ ] 6번 점검 목록에 완료 조건 3의 세 글이 든 항목 하나가 더해진다. 옵션·문법 오류(`-`로 시작하는 패턴이 옵션으로 읽힌다, 따옴표가 어긋난다)가 나면 명령을 고친다는 것도 함께 적는다 (`plugins/plate/skills/plan/SKILL.md`)
- [ ] 적는 규칙 "조건"의 `- 확인은 돌릴 명령과 기대 결과를 우선한다.`로 시작하는 항목에 `확인 명령은 적힌 그대로 돌게 적는다`와 그 예(`-`로 시작하는 패턴은 `-e`나 `--` 뒤에 둔다)가 이어 더해진다. 새 항목을 따로 만들지 않는다 (`plugins/plate/skills/plan/SKILL.md`)
- [ ] `PlanRulesTest.test_68_check_commands_run_as_written`이 더해진다. 절대 규칙 절, 6번 절, 적는 규칙 "조건"에 완료 조건 3의 새 글이 있고 본문에 옛 글이 없는지 본다. 모듈 docstring의 plan 목록에 `#68`이 더해진다 (`tests/test_skill_rules.py`)
- [ ] 디렉터리 구조의 `test_skill_rules.py` 줄의 규칙 목록에 "plan이 읽기만 하는 확인 명령을 초안 점검에서 돌림"이 더해진다 (`docs/ARCHITECTURE.md`)
- [ ] 두 매니페스트의 버전이 0.20.0에서 0.21.0으로 바뀐다 (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)

**통과 조건**
- 완료 조건 3이 참이다
  - 확인: 옛 글 `완료 조건과 통과 조건에 적는 확인 명령은 미리 돌려 보지 않고 적는다`는 `grep -cF -e '<글>' plugins/plate/skills/plan/SKILL.md`로 `0`이고, 완료 조건 3의 새 글 다섯은 저마다 `1`이다
  - 확인: `grep -F -e '- 확인은 돌릴 명령과 기대 결과를 우선한다.' plugins/plate/skills/plan/SKILL.md`가 한 줄을 내고 그 줄에 `확인 명령은 적힌 그대로 돌게 적는다`가 든다
- 완료 조건 1과 2가 그대로 참이다(이 phase가 `tests/test_skill_rules.py`와 `docs/ARCHITECTURE.md`를 고친다)
  - 확인: 완료 조건 1과 2의 `grep -cF -e` 확인을 다시 돌려 같은 수(완료 조건 1의 글마다 `1`, review의 새 글 `3`, 옛 글 `0`, 정의 글과 `**테스트 파일**`과 5번의 두 글 저마다 `1`, ADR `1`)가 나온다
  - 확인: `git hash-object`로 낸 `plugins/plate/skills/check/SKILL.md`와 `plugins/plate/skills/review/SKILL.md`의 해시가 `done-phase-1.md`, `done-phase-2.md`의 "한 일"에 적힌 값과 같다
- 완료 조건 4가 참이다
  - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
  - 확인: 다섯 시험을 저마다 새 사본(`mktemp -d`로 만든 폴더에 작업 트리의 `plugins`와 `tests`를 `cp -R`로 복사한 것)에서 한다. 그 글이 사본의 파일에 한 번 있는지 보고, 빈 글로 바꿔 `python3 -m unittest discover -s tests`를 돌리면 출력에 그 줄로 시작하는 줄이 있다. phase 본문의 `고친 명령과 까닭을 "계획과 달라진 점"과 "하네스에서 걸린 것"에 적는다` → `FAIL: test_69_fix_check_command_and_record (test_skill_rules.PhaseRulesTest`, check 본문의 `적힌 명령, 고친 명령, 까닭을 "하네스에서 걸린 것"에 적는다` → `FAIL: test_69_run_check_as_written (test_skill_rules.CheckRulesTest`, retro 본문의 `적힌 명령, 고친 명령, 까닭을 "확인"의 결과에 적고 5번의 문제로 모은다` → `FAIL: test_69_run_check_as_written (test_skill_rules.RetroRulesTest`, review 본문의 `테스트 파일은 바뀐 동작이 아니라 그 근거라 표를 고를 때 세지 않는다` → `FAIL: test_70_test_files_do_not_pick_default_table (test_skill_rules.ReviewRulesTest`, plan 본문의 `읽기만 하는 확인 명령(파일이나 저장소를 바꾸지 않는 것)을 돌려 적힌 그대로 도는지 본다` → `FAIL: test_68_check_commands_run_as_written (test_skill_rules.PlanRulesTest`
- 완료 조건 5가 참이다
  - 확인: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json`의 두 줄이 모두 `0.21.0`
  - 확인: `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
  - 확인: `docs/ARCHITECTURE.md`의 `test_skill_rules.py` 줄에 `적힌 그대로 돌지 않는 확인 명령`, `테스트 파일도 빼고 표를 고름`, `읽기만 하는 확인 명령을 초안 점검에서 돌림`이 저마다 든다
  - 확인: `sed -n '1,8p' tests/test_skill_rules.py`에 plan의 `#68`, phase·check·retro의 `#69`, review의 `#70`이 있다
