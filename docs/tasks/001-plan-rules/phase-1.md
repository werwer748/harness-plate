# Phase 1: plan 본문과 테스트와 문서를 고친다

**목표**: plan 본문에 세 이슈의 해결이 더해지고, 그 규칙 글의 테스트가 더해지고, 버전과 `docs/ARCHITECTURE.md`의 테스트 줄이 맞춰진다.

**테스트 먼저**: 아니오 — 고치는 것은 스킬 본문(`.md`)이고, 더하는 테스트는 그 글이 있는지를 볼 뿐 코드의 동작을 바꾸지 않는다

**읽을 것**
- `plugins/plate/skills/plan/SKILL.md`의 "6. 초안을 보여 주고 승인받는다"와 적는 규칙의 "조건", "결정" 절 (고칠 자리)
- `gh issue view 55 --repo werwer748/harness-plate`, `gh issue view 56 --repo werwer748/harness-plate`, `gh issue view 57 --repo werwer748/harness-plate` (이슈마다의 원인과 해결책)
- `tests/test_skill_rules.py`의 모듈 docstring, `section`·`part` 도우미, `PlanRulesTest` (테스트의 꼴)
- `docs/ARCHITECTURE.md` 디렉터리 구조의 `test_skill_rules.py` 줄 (맞출 줄)
- `plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json` (버전 줄)

**TODO**
- [ ] 적는 규칙 "조건"에 #55의 해결이 더해진다: `phase의 통과 조건은 커밋 전의 작업 트리에서 돈다`, `HEAD`를 풀거나 보는 확인은 작업 트리(예: `cp -R` 사본, `git stash create`로 얻은 트리)로 적는다, 원본이 바뀌지 않았는지 보는 확인은 그 phase의 `phase-N.md`를 빼고 본다. 6번에 `수행이 돌릴 확인에 \`HEAD\`가 있는지 본다`로 시작하는 점검 항목이 더해진다 (`plugins/plate/skills/plan/SKILL.md`)
- [ ] 적는 규칙 "조건"에 #56의 해결이 더해진다: 글을 지우거나 바꿔 테스트가 실패하는지 보는 확인은 `지울 글을 본문에 있는 그대로 인용하고`(줄 하나면 그 줄 전체) `실패할 테스트 이름을 기대로 적는다` (`plugins/plate/skills/plan/SKILL.md`)
- [ ] 적는 규칙 "결정"에 #57의 해결이 더해진다: 결정이나 TODO가 `앞 task가 바꿀 글을 인용하면 바뀐 뒤의 글 그대로 적고` 앞 task가 더할 줄을 다시 덧붙이지 않는다. 6번에 `task 사이에 같은 글을 바꾸거나 인용하는 곳이 맞물리는지 본다`가 든 점검 항목이 더해진다. 완료 조건 1의 다섯 글은 본문에 저마다 한 번만 나온다 (`plugins/plate/skills/plan/SKILL.md`)
- [ ] `PlanRulesTest`에 세 테스트가 더해진다: `test_55_checks_run_on_uncommitted_worktree`(조건 절의 `phase의 통과 조건은 커밋 전의 작업 트리에서 돈다`와 6번의 `수행이 돌릴 확인에 \`HEAD\`가 있는지 본다`), `test_56_mutation_checks_quote_text_and_name_test`(조건 절의 `지울 글을 본문에 있는 그대로 인용하고`와 `실패할 테스트 이름을 기대로 적는다`), `test_57_quote_earlier_task_text_as_changed`(결정 절의 `앞 task가 바꿀 글을 인용하면 바뀐 뒤의 글 그대로 적고`와 6번의 `task 사이에 같은 글을 바꾸거나 인용하는 곳이 맞물리는지 본다`). 모듈 docstring의 plan 목록에 #55·#56·#57이 더해진다 (`tests/test_skill_rules.py`)
- [ ] 두 매니페스트의 버전이 0.18.0에서 0.19.0으로 바뀐다 (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)
- [ ] 디렉터리 구조의 `test_skill_rules.py` 줄의 규칙 목록에 세 규칙(통과 조건은 커밋 전 작업 트리에서 돎, 지울 글 인용과 실패할 테스트 이름, 앞 task가 바꿀 글을 바뀐 뒤 꼴로 인용)이 더해진다 (`docs/ARCHITECTURE.md`)

**통과 조건**
- 완료 조건 1이 참이다
  - 확인: `plugins/plate/skills/plan/SKILL.md`의 "6. 초안을 보여 주고 승인받는다"와 적는 규칙의 "조건", "결정" 절을 읽어, 완료 조건 1에 백틱으로 적은 다섯 글이 저마다 그 절에 있다. 하나라도 없으면 실패
- 완료 조건 2가 참이다
  - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
  - 확인: `mktemp -d`로 만든 폴더에 작업 트리의 `plugins`와 `tests`를 `cp -R`로 복사하고, 사본의 `plugins/plate/skills/plan/SKILL.md`에서 글 `phase의 통과 조건은 커밋 전의 작업 트리에서 돈다`가 한 번 있는지 본 뒤(없으면 실패) 그 글을 빈 글로 바꾸고 사본에서 `python3 -m unittest discover -s tests`를 돌리면 출력에 `FAIL: test_55_checks_run_on_uncommitted_worktree` 줄이 있다
  - 확인: 같은 방법으로 새로 복사해 글 `지울 글을 본문에 있는 그대로 인용하고`를 빈 글로 바꾸면 출력에 `FAIL: test_56_mutation_checks_quote_text_and_name_test` 줄이 있다
  - 확인: 같은 방법으로 새로 복사해 글 `앞 task가 바꿀 글을 인용하면 바뀐 뒤의 글 그대로 적고`를 빈 글로 바꾸면 출력에 `FAIL: test_57_quote_earlier_task_text_as_changed` 줄이 있다
- 완료 조건 3이 참이다
  - 확인: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json`의 두 줄이 모두 `0.19.0`
  - 확인: `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
  - 확인: `docs/ARCHITECTURE.md` 디렉터리 구조의 `test_skill_rules.py` 줄이 세 규칙을 저마다 담고, `tests/test_skill_rules.py`의 모듈 docstring의 plan 목록에 #55·#56·#57이 있다. 하나라도 없으면 실패
- 모든 스킬의 description이 1024자 이하다
  - 확인: `python3 -m unittest discover -s tests`의 `test_description_at_most_1024_chars`가 통과한다(위 `OK`에 든다)
