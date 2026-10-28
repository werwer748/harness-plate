# 회고

## 회고 1

**확인**
- 작업 트리를 얻는 예로 든 `git stash create`는 추적하지 않는 새 파일을 넣지 않고 새 파일만 바뀌었으면 아무것도 내지 않아, 새 파일을 만드는 phase의 통과 조건이 이 예를 따르면 그 파일이 없는 트리를 본다. 예를 `cp -R` 사본으로 줄이거나 새 파일이 빠진다는 단서를 단다 (`plugins/plate/skills/plan/SKILL.md:249`)
  - `plugins/plate/skills/plan/SKILL.md`의 적는 규칙 "조건" 절(`**조건**`부터 다음 굵은 제목 앞까지)을 스크립트로 잘라 읽음 → `stash` 없음(False). 249줄의 예는 `작업 트리(예: \`cp -R\` 사본)`. `grep -rn stash README.md plugins tests docs/*.md` → 출력 없음. 통과
- tasks 완료 조건 1, 2, 3이 참이다.
  - "6. 초안을 보여 주고 승인받는다"와 적는 규칙 "조건", "결정" 절을 스크립트로 잘라 봄 → 6번에 `수행이 돌릴 확인에 \`HEAD\`가 있는지 본다`, `task 사이에 같은 글을 바꾸거나 인용하는 곳이 맞물리는지 본다`; 조건에 `phase의 통과 조건은 커밋 전의 작업 트리에서 돈다`, `지울 글을 본문에 있는 그대로 인용하고`, `실패할 테스트 이름을 기대로 적는다`; 결정에 `앞 task가 바꿀 글을 인용하면 바뀐 뒤의 글 그대로 적고` → 모두 True. 통과
  - `python3 -m unittest discover -s tests` → `Ran 164 tests in 17.713s`, 마지막 줄 `OK`. 통과
  - `mktemp -d` 사본에 `cp -R plugins tests`, `phase의 통과 조건은 커밋 전의 작업 트리에서 돈다` 개수 1, 빈 글로 바꾸고 사본에서 테스트 → `FAIL: test_55_checks_run_on_uncommitted_worktree (test_skill_rules.PlanRulesTest)`, `FAILED (failures=1)`. 통과
  - 새 사본, `지울 글을 본문에 있는 그대로 인용하고` 개수 1, 빈 글로 → `FAIL: test_56_mutation_checks_quote_text_and_name_test (test_skill_rules.PlanRulesTest)`, `FAILED (failures=1)`. 통과
  - 새 사본, `앞 task가 바꿀 글을 인용하면 바뀐 뒤의 글 그대로 적고` 개수 1, 빈 글로 → `FAIL: test_57_quote_earlier_task_text_as_changed (test_skill_rules.PlanRulesTest)`, `FAILED (failures=1)`. 통과
  - `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → `"version": "0.19.0",` 두 줄. 통과
  - `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
  - `docs/ARCHITECTURE.md` 39줄의 `test_skill_rules.py` 줄 → `통과 조건은 커밋 전 작업 트리에서 돎`, `지울 글 인용과 실패할 테스트 이름`, `앞 task가 바꿀 글을 바뀐 뒤 꼴로 인용`이 저마다 있음. `tests/test_skill_rules.py` 모듈 docstring의 plan 목록 `plan의 #37·#41·#46·#52·#53·#55·#56·#57` → #55·#56·#57 있음. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 164 tests`, `OK`. 통과

**남은 것**
- phase 1: 고친 것은 예를 지운 것뿐이라, 이 규칙을 따르는 계획이 `cp -R` 말고 다른 작업 트리 얻는 법을 고르면 그 법이 새 파일을 담는지는 본문이 말하지 않는다 → 문제 아님 (task 머리 목표·완료 조건 1은 "예를 `cp -R` 사본으로 줄이거나 단서를 단다"로 정했고 줄이는 쪽으로 됐다. 본문은 이제 새 파일을 담는 `cp -R`만 예로 들어, 새 파일이 빠지는 예를 권하는 결함은 남지 않는다. 다른 법을 고를 때의 안내는 이 task의 목표 밖이다)

**문제**
- 없음

**판정**: 통과
