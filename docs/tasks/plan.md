# plan 이슈 #65를 고친다

**이름**: compare-checks

## 요청
열린 GitHub 이슈 3개(#64, #65, #66 — 지난 cleanup-fixes tasks의 하네스 eval이 낸 plate 자체 고칠 거리)를 고친다. #64·#65는 plan 스킬의 적는 규칙(**조건**)과 6번 초안 점검, #66은 eval 스킬 `낱말`의 "정해 둔 물음" 정의. 1.0.0 릴리스 전에 열린 이슈를 모두 비우는 것이 목적이다.

## 목표
#65를 plan 본문 적는 규칙 "조건"의 기존 항목 `확인은 돌릴 명령과 기대 결과를 우선한다`와 6번 초안 점검에서 고치고, 고친 글이 빠지면 실패하는 테스트를 `tests/test_skill_rules.py`에 더한다. 버전은 0.20.0이 되고, `docs/ARCHITECTURE.md`의 `test_skill_rules.py` 줄과 테스트 모듈 docstring이 더한 규칙에 맞춰진다.

## 범위 밖
- #64, #66을 고치는 것. 지난 eval에서 등급에 영향이 없어 닫았다
- plan의 고친 동작을 헤드리스 장면으로 돌리는 것. plan은 사람에게 묻고 초안마다 승인받는 스킬이라 `돌리지 않음`으로 둔다
- plan 밖의 스킬을 고치는 것
- GitHub 이슈 #65를 닫는 것. PR이 머지된 뒤 닫는다
- 1.0.0을 내는 것

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
- task 하나, phase 하나로 한다. 이유: 고칠 곳이 plan 본문 한 파일과 그 테스트·문서뿐이다 (추천안으로 정함)
- #65의 글은 새 항목으로 두지 않고 기존 항목 `확인은 돌릴 명령과 기대 결과를 우선한다`에 이어 적는다. 6번에도 점검 한 줄을 더한다. 이유: 같은 대상(확인을 명령으로 적는 것)을 두 항목이 따로 시키지 않게 하고, 앞서 고친 이슈들처럼 초안 단계에서도 잡게 한다 (추천안으로 정함)
- 고친 글과 테스트 이름은 완료 조건 1·2에 적은 그대로 한다. 세 글은 plan 본문에 저마다 한 번만 나온다. 이유: 지울 글을 그대로 인용하고 실패할 테스트를 미리 적으려면 글과 이름이 계획에서 정해져야 한다 (추천안으로 정함)
- 버전은 0.20.0이다. 이유: 스킬 동작이 바뀌는 tasks마다 마이너를 올려 왔다
- run을 시작하기 전에 사용자가 plan 모드를 끄고 bypassPermissions로 둔다. 이유: `AGENTS.md`의 작업 규칙(`plugins/plate/skills/` 편집이 auto mode에서 막힌다)

## task 목록
- `001-compare-checks`: plan의 #65가 고쳐지고, 그 규칙 글의 테스트가 더해지고, 버전이 0.20.0이 된다
