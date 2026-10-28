# plan의 #65를 고친다

## 목표
plan 본문 적는 규칙 "조건"의 기존 항목 `확인은 돌릴 명령과 기대 결과를 우선한다`와 6번 초안 점검에 #65의 해결이 더해진다. 그 글이 빠지면 실패하는 테스트가 `tests/test_skill_rules.py`에 더해진다. 버전이 0.20.0이 되고, `docs/ARCHITECTURE.md`의 `test_skill_rules.py` 줄과 테스트 모듈 docstring이 맞춰진다.

## 범위 밖
- plan의 고친 동작을 헤드리스 장면으로 돌리는 것
- plan 밖의 스킬 본문을 고치는 것
- GitHub 이슈를 닫는 것

## 완료 조건
1. plan 본문에 #65의 해결이 제자리에 있고 기존 규칙과 한 항목으로 이어진다. 적는 규칙 "조건"의 `- 확인은 돌릴 명령과 기대 결과를 우선한다.`로 시작하는 항목에 `값을 뽑아 견주는 확인은 뽑는 명령(또는 패턴)과 견주는 법을 적는다`와 `적을 수 없으면 읽어서 견줄 자리를 적는다`가 있다. 6번 "초안을 보여 주기 전에 아래를 본다." 목록에 `값을 뽑아 견주는 확인에 뽑는 명령과 견주는 법이 있는지 본다`가 있다
   - 확인: `grep -cF '<글>' plugins/plate/skills/plan/SKILL.md`를 위 세 글마다 돌리면 저마다 `1`이다. 하나라도 `1`이 아니면 실패
   - 확인: `grep -F '- 확인은 돌릴 명령과 기대 결과를 우선한다.' plugins/plate/skills/plan/SKILL.md`가 내는 한 줄에 앞의 두 글이 모두 든다. 줄이 하나가 아니거나 한 글이라도 빠지면 실패
   - 돌리지 않음: plan은 사람에게 묻고 초안마다 승인을 받는 스킬이라, 고친 규칙대로 초안이 적히는지는 여러 턴의 답을 이어야 닿는다
2. 고친 글이 빠지면 실패하는 테스트가 있고, 모든 테스트가 통과한다
   - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
   - 확인: `mktemp -d`로 만든 폴더에 작업 트리의 `plugins`와 `tests`를 `cp -R`로 복사한다. 사본의 `plugins/plate/skills/plan/SKILL.md`에 글 `값을 뽑아 견주는 확인은 뽑는 명령(또는 패턴)과 견주는 법을 적는다`가 한 번 있는지 본다(없으면 실패). 그 글을 빈 글로 바꾸고 사본에서 `python3 -m unittest discover -s tests`를 돌리면 출력에 `FAIL: test_65_comparison_checks_name_extract_command` 줄이 있다
   - 확인: 같은 방법으로 새로 복사해 글 `값을 뽑아 견주는 확인에 뽑는 명령과 견주는 법이 있는지 본다`를 빈 글로 바꾸면 출력에 `FAIL: test_65_comparison_checks_name_extract_command` 줄이 있다
3. 두 매니페스트의 버전이 0.20.0이고, 마켓플레이스가 유효하고, 테스트의 설명 글이 더한 규칙과 맞는다
   - 확인: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json`의 두 줄이 모두 `0.20.0`
   - 확인: `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
   - 확인: `grep -c '값을 뽑아 견주는 확인' docs/ARCHITECTURE.md`가 `1` 이상이고 그 줄이 `test_skill_rules.py` 줄이다. `sed -n '1,8p' tests/test_skill_rules.py`의 plan 목록에 `#65`가 있다. 하나라도 아니면 실패

## 결정
- #65의 글은 새 항목으로 두지 않고 기존 항목 `확인은 돌릴 명령과 기대 결과를 우선한다`에 이어 적고, 6번에 점검 한 줄을 더한다. 이유: 같은 대상을 두 항목이 따로 시키지 않게 하고 초안 단계에서도 잡게 한다 (추천안으로 정함)
- 고친 글과 테스트 이름은 완료 조건 1·2에 적은 그대로 한다. 세 글은 plan 본문에 저마다 한 번만 나온다. 이유: 지울 글을 그대로 인용하고 실패할 테스트를 미리 적으려면 글과 이름이 계획에서 정해져야 한다 (추천안으로 정함)
- 버전은 0.20.0이다. 이유: 스킬 동작이 바뀌는 tasks마다 마이너를 올려 왔다
