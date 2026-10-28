# 회고

## 회고 1

**확인**
- plan 본문에 #65의 해결이 제자리에 있고 기존 규칙과 한 항목으로 이어진다
  - `grep -cF '<글>' plugins/plate/skills/plan/SKILL.md`를 세 글(`값을 뽑아 견주는 확인은 뽑는 명령(또는 패턴)과 견주는 법을 적는다`, `적을 수 없으면 읽어서 견줄 자리를 적는다`, `값을 뽑아 견주는 확인에 뽑는 명령과 견주는 법이 있는지 본다`)마다 → `1`, `1`, `1`. 통과
  - `grep -F -- '- 확인은 돌릴 명령과 기대 결과를 우선한다.' plugins/plate/skills/plan/SKILL.md` → 한 줄, 그 줄에서 앞의 두 글이 저마다 `grep -cF`로 `1`. 통과
- 고친 글이 빠지면 실패하는 테스트가 있고, 모든 테스트가 통과한다
  - `python3 -m unittest discover -s tests` → `Ran 193 tests`, 마지막 줄 `OK`. 통과
  - `mktemp -d` 사본(`cp -R plugins tests`)에서 `값을 뽑아 견주는 확인은 뽑는 명령(또는 패턴)과 견주는 법을 적는다`가 `1`번 있음을 보고 빈 글로 바꿔 테스트를 돌림 → `FAIL: test_65_comparison_checks_name_extract_command (test_skill_rules.PlanRulesTest)`. 통과
  - 새 사본에서 `값을 뽑아 견주는 확인에 뽑는 명령과 견주는 법이 있는지 본다`(`1`번 있음)를 빈 글로 바꿔 테스트를 돌림 → `FAIL: test_65_comparison_checks_name_extract_command (test_skill_rules.PlanRulesTest)`. 통과
- 두 매니페스트의 버전이 0.20.0이고, 마켓플레이스가 유효하고, 테스트의 설명 글이 더한 규칙과 맞는다
  - `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → `"version": "0.20.0",` 두 줄. 통과
  - `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
  - `grep -c '값을 뽑아 견주는 확인' docs/ARCHITECTURE.md` → `1`, 그 줄이 `└── test_skill_rules.py` 줄. `sed -n '1,8p' tests/test_skill_rules.py`의 plan 목록에 `#65` 있음. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 193 tests`, `OK`. 통과

**남은 것**
- phase 1: 고친 규칙대로 plan이 초안을 적는지는 돌려 보지 않았다(task 머리의 `- 돌리지 않음` 줄대로) → 문제 아님 (task 머리·tasks 머리 완료 조건 1의 `- 돌리지 않음` 줄과 범위 밖 "plan의 고친 동작을 헤드리스 장면으로 돌리는 것"이 돌리지 않기로 정한 동작이다. 바뀐 본문 두 줄을 직접 읽어 기존 규칙과 6번 점검에 맞게 들어간 것을 봤다)

**문제**
- 없음

**판정**: 통과
