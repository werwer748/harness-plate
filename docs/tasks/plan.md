# plan 이슈 3개를 고친다

**이름**: plan-check-rules

## 요청
열린 GitHub 이슈 3개(#55, #56, #57 — 지난 eval-issues tasks의 하네스 eval이 낸 plate 자체 고칠 거리, 모두 plan 스킬)를 고친다. 이 tasks 끝의 코드 평가 다섯 범주와 하네스 eval 여섯 기준이 모두 최소 B를 유지해야 한다. 지난 tasks에서 B 아래였던 것: eval 실패 양상 D(tasks 끝에서 잡힌 실패 1개 — 완료 조건의 "지울 글" 경계 미지정, 같은 유형 FM-1.1 3번 — phase 통과 조건의 `git archive HEAD`가 커밋 전이라 돌 수 없었음). 계획 자체가 이번 이슈들의 해결(통과 조건은 커밋 전 작업 트리에서 돈다, 지울 글은 그대로 인용하고 실패할 테스트 이름을 적는다, 앞 task가 바꿀 글은 바뀐 뒤 꼴로 인용한다)을 미리 지켜 같은 실패가 나지 않게 짜여야 한다.

## 목표
열린 이슈 3개(#55, #56, #57)를 plan 본문의 적는 규칙과 6번 초안 점검에서 고치고, 고친 규칙마다 글이 빠지면 실패하는 테스트를 `tests/test_skill_rules.py`에 더한다. 버전은 0.19.0이 되고, `docs/ARCHITECTURE.md`의 `test_skill_rules.py` 줄과 테스트 모듈 docstring이 더한 규칙에 맞춰진다.

## 범위 밖
- GitHub 이슈를 닫는 것. PR이 머지된 뒤 닫는다
- plan의 고친 동작을 헤드리스 장면으로 돌리는 것. plan은 사람에게 묻고 초안마다 승인받는 스킬이라 `돌리지 않음`으로 둔다
- 본문의 글을 지워 테스트 실패를 보는 확인을 스킬이나 스크립트로 만드는 것(지난 eval의 스킬로 만들 후보)
- plan 밖의 스킬(run, phase, check, retro, review, eval)을 고치는 것

## 완료 조건
1. plan 본문에 세 이슈의 해결이 제자리에 있다: #55(적는 규칙 "조건"에 `phase의 통과 조건은 커밋 전의 작업 트리에서 돈다`가 있고, `HEAD`를 풀거나 보는 확인은 작업 트리로 적고 원본이 바뀌지 않았는지 보는 확인은 그 phase의 `phase-N.md`를 빼고 본다는 글이 있고, 6번에 `수행이 돌릴 확인에 \`HEAD\`가 있는지 본다`가 있다), #56(적는 규칙 "조건"에 `지울 글을 본문에 있는 그대로 인용하고`와 `실패할 테스트 이름을 기대로 적는다`가 있다), #57(적는 규칙 "결정"에 `앞 task가 바꿀 글을 인용하면 바뀐 뒤의 글 그대로 적고`가 있고, 6번에 `task 사이에 같은 글을 바꾸거나 인용하는 곳이 맞물리는지 본다`가 있다)
   - 확인: `plugins/plate/skills/plan/SKILL.md`의 "6. 초안을 보여 주고 승인받는다"와 적는 규칙의 "조건", "결정" 절을 읽어, 위에 백틱으로 적은 다섯 글이 저마다 그 절에 있다. 하나라도 없으면 실패
   - 돌리지 않음: plan은 사람에게 묻고 초안마다 승인을 받는 스킬이라, 고친 규칙대로 초안이 적히는지는 여러 턴의 답을 이어야 닿는다
2. 고친 규칙마다 글이 빠지면 실패하는 테스트가 있고, 모든 테스트가 통과한다
   - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
   - 확인: `mktemp -d`로 만든 폴더에 작업 트리의 `plugins`와 `tests`를 `cp -R`로 복사하고, 사본의 `plugins/plate/skills/plan/SKILL.md`에서 글 `phase의 통과 조건은 커밋 전의 작업 트리에서 돈다`가 한 번 있는지 본 뒤(없으면 실패) 그 글을 빈 글로 바꾸고 사본에서 `python3 -m unittest discover -s tests`를 돌리면 출력에 `FAIL: test_55_checks_run_on_uncommitted_worktree` 줄이 있다
   - 확인: 같은 방법으로 새로 복사해 글 `지울 글을 본문에 있는 그대로 인용하고`를 빈 글로 바꾸면 출력에 `FAIL: test_56_mutation_checks_quote_text_and_name_test` 줄이 있다
   - 확인: 같은 방법으로 새로 복사해 글 `앞 task가 바꿀 글을 인용하면 바뀐 뒤의 글 그대로 적고`를 빈 글로 바꾸면 출력에 `FAIL: test_57_quote_earlier_task_text_as_changed` 줄이 있다
3. 두 매니페스트의 버전이 0.19.0이고, 마켓플레이스가 유효하고, 테스트의 설명 글이 더한 규칙과 맞는다
   - 확인: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json`의 두 줄이 모두 `0.19.0`
   - 확인: `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
   - 확인: `docs/ARCHITECTURE.md` 디렉터리 구조의 `test_skill_rules.py` 줄이 세 규칙(통과 조건은 커밋 전 작업 트리에서 돎, 지울 글 인용과 실패할 테스트 이름, 앞 task가 바꿀 글을 바뀐 뒤 꼴로 인용)을 저마다 담고, `tests/test_skill_rules.py`의 모듈 docstring의 plan 목록에 #55·#56·#57이 있다. 하나라도 없으면 실패

## 결정
- task 하나, phase 하나로 한다. 이유: 세 이슈가 모두 plan 본문 한 파일이고, task를 나누면 #57의 꼴(앞 task가 바꿀 글을 인용)이 생긴다 (추천안으로 정함)
- 세 규칙의 핵심 글(완료 조건 1에 백틱으로 적은 다섯 글)을 본문에 그대로 넣고, 테스트 이름은 완료 조건 2에 적은 셋으로 한다. 이유: 지울 글을 그대로 인용하고 실패할 테스트를 미리 적으려면(#56) 글과 이름이 계획에서 정해져야 한다 (추천안으로 정함)
- 글을 지워 보는 확인은 `git archive HEAD`가 아니라 작업 트리를 `cp -R`로 복사한 사본에서 돌린다. 이유: phase의 통과 조건은 커밋 전에 돌아 HEAD에 그 phase의 변경이 없다(#55) (추천안으로 정함)
- 버전은 0.19.0이다. PR 전에 main이 먼저 0.19.0 이상이 되면 PR에서 다음 마이너로 맞춘다. 이유: 스킬 동작이 바뀌는 tasks마다 마이너를 올려 왔다 (추천안으로 정함)
- run을 시작하기 전에 사용자가 plan 모드를 끄고 bypassPermissions로 둔다. 이유: `AGENTS.md`의 작업 규칙(`plugins/plate/skills/` 편집이 auto mode에서 막힌다)

## task 목록
- `001-plan-rules`: plan의 이슈 셋(#55, #56, #57)이 고쳐지고, 그 규칙 글의 테스트가 더해지고, 버전이 0.19.0이 된다
