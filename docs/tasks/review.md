# 코드 평가

## 평가 1

**대상**
- 범위: `9215233`(main에서 갈라진 곳)부터 `6ae5e49`까지
- 결과물인 마크다운 절: `plugins/plate/skills/*/SKILL.md`
- 바뀐 코드 파일 4개, 새 줄 29줄, 잴 새 줄 23줄
  - `plugins/plate/.claude-plugin/plugin.json` +1
  - `plugins/plate/.codex-plugin/plugin.json` +1
  - `tests/test_skill_rules.py` +21
  - `plugins/plate/skills/plan/SKILL.md` +6 (결과물인 마크다운)

**잰 것**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 164 tests in 16.227s`, `OK`. 통과
- 커버리지: 측정 못함 — 명령 절이 커버리지 도구를 두지 않는다고 적고(ADR-024), `coverage` 모듈도 이 환경에 없다(`ModuleNotFoundError: No module named 'coverage'`)
- 중복: 측정 못함 — 명령 절이 중복 검사 도구를 두지 않고, `jscpd` 같은 도구도 이 환경에 없다
- 정적 분석: `python3 -m py_compile tests/test_skill_rules.py` → 오류 없음. `pyflakes`, `mypy`, `ruff`, `pylint`, `flake8`은 이 환경에 없어 돌리지 못했다
- 보안 검사: 측정 못함 — 명령 절이 보안 검사 도구를 두지 않고(의존성 목록도 없다), `semgrep`, `bandit`, `pip-audit`도 이 환경에 없다

**완료 조건**
- 1. plan 본문에 세 이슈의 해결이 제자리에 있다
  - `plugins/plate/skills/plan/SKILL.md`를 읽고 `grep -n -F`로 다섯 글의 줄을 절 머리(6번 90~116행, 적는 규칙 "결정" 229~235행, "조건" 236~260행)에 댔다 → `phase의 통과 조건은 커밋 전의 작업 트리에서 돈다` 249행("조건"), 같은 줄에 `HEAD`를 풀거나 보는 확인은 작업 트리로 적고 원본이 바뀌지 않았는지 보는 확인은 그 phase의 `phase-N.md`를 빼고 본다는 글, `수행이 돌릴 확인에 \`HEAD\`가 있는지 본다` 102행(6번), `지울 글을 본문에 있는 그대로 인용하고`와 `실패할 테스트 이름을 기대로 적는다` 250행("조건"), `앞 task가 바꿀 글을 인용하면 바뀐 뒤의 글 그대로 적고` 234행("결정"), `task 사이에 같은 글을 바꾸거나 인용하는 곳이 맞물리는지 본다` 103행(6번). 통과
  - 돌리지 않음 줄: plan은 사람에게 묻고 승인받는 스킬이라 돌리지 않음. 측정 못함(계획이 돌리지 않기로 정함)
- 2. 고친 규칙마다 글이 빠지면 실패하는 테스트가 있고, 모든 테스트가 통과한다
  - `python3 -m unittest discover -s tests` → 마지막 줄 `OK`. 통과
  - `mktemp -d` 사본에 `plugins`, `tests`를 `cp -R`, 글 `phase의 통과 조건은 커밋 전의 작업 트리에서 돈다`가 1번 있음을 보고 빈 글로 바꿔 테스트 → `FAIL: test_55_checks_run_on_uncommitted_worktree (test_skill_rules.PlanRulesTest)`. 통과
  - 새 사본에서 `지울 글을 본문에 있는 그대로 인용하고`(1번 있음)를 지움 → `FAIL: test_56_mutation_checks_quote_text_and_name_test (test_skill_rules.PlanRulesTest)`. 통과
  - 새 사본에서 `앞 task가 바꿀 글을 인용하면 바뀐 뒤의 글 그대로 적고`(1번 있음)를 지움 → `FAIL: test_57_quote_earlier_task_text_as_changed (test_skill_rules.PlanRulesTest)`. 통과
- 3. 두 매니페스트의 버전이 0.19.0이고, 마켓플레이스가 유효하고, 테스트의 설명 글이 더한 규칙과 맞는다
  - `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "0.19.0",`. 통과
  - `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
  - `docs/ARCHITECTURE.md` 39행의 `test_skill_rules.py` 줄을 읽음 → "통과 조건은 커밋 전 작업 트리에서 돎, 지울 글 인용과 실패할 테스트 이름, 앞 task가 바꿀 글을 바뀐 뒤 꼴로 인용"이 있다. `tests/test_skill_rules.py:3` docstring의 plan 목록에 `#55·#56·#57`이 있다. 통과

**범주**
- 신뢰성
  - 근거: `plugins/plate/skills/plan/SKILL.md:249` 작업 트리를 얻는 예로 `git stash create`로 얻은 트리를 든다. 이 명령은 추적하지 않는 새 파일을 넣지 않고, 바뀐 것이 새 파일뿐이면 아무것도 내지 않는다(시험 저장소에서 새 파일 하나만 두고 돌리니 `stash: []`, `git add` 뒤에야 트리에 `new.txt`가 들었다). 새 파일을 만드는 phase의 계획이 이 예를 따르면 통과 조건이 그 파일이 없는 트리를 본다 (기능, 낮음)
  - 등급: B — 가장 무거운 문제가 낮음
- 보안
  - 핫스팟: 없음. 바뀐 코드 파일 가운데 실행되는 것은 `tests/test_skill_rules.py`의 새 줄(`assertIn`, `assertNotIn`으로 본문 글을 보는 줄)뿐이고, 셸 실행, 밖의 입력, 비밀, 권한을 다루지 않는다
  - 근거: 새 줄 29줄을 모두 읽어 취약점이 없다고 봤다. 매니페스트 두 줄은 버전 값뿐이다
  - 등급: A — 문제 0개
- 유지보수성
  - 근거: 문제 없음. 새 테스트 셋(`tests/test_skill_rules.py:264-279`)은 같은 클래스의 앞 테스트(`test_52`, `test_53`)와 같은 꼴(`part(section(...))`로 절을 자르고 `assertIn`)과 이름 규칙(`test_<이슈>_<무엇>`)을 따르고, `test_46`의 고침(248-251행)은 본문의 바뀐 글과 맞물린다. plan 본문의 새 줄(102, 103, 234, 248-250행)은 주변 줄과 같은 꼴(규칙, 그 까닭)이고 6번의 다른 줄처럼 예를 괄호로 단다
  - 부채 비율: 0분 ÷ (29줄 × 30분) = 0%
  - 등급: A — 부채 비율 5% 이하
- 테스트 적절성
  - 근거: 커버리지는 측정 못함이라 판단만으로 매긴다
  - 근거: `tests/test_skill_rules.py:264-279` 세 이슈의 핵심 글 여섯을 제 절에서 본다. 완료 조건 2의 글 지우기 확인을 직접 돌려 셋 모두 해당 테스트가 실패함을 봤다
  - 근거: `tests/test_skill_rules.py:247-251` `test_46_rerun_results_compared_by_body_hash`이 바뀐 글을 보고 옛 글(`git rev-parse HEAD:`)이 없는지도 본다
  - 근거: `plugins/plate/skills/plan/SKILL.md:249`의 "원본이 바뀌지 않았는지 보는 확인은 그 phase의 `phase-N.md`를 빼고 본다"와 `:234`의 "앞 task가 더할 줄을 다시 덧붙이지 않는다"는 이 글을 보는 테스트가 없다. 규칙의 곁가지 글이다
  - 근거: plan의 고친 동작(초안이 고친 규칙대로 적히는지)은 tasks 머리 완료 조건 1의 `돌리지 않음` 줄로 돌리지 않았다
  - 등급: B — 테스트가 빠진 것은 규칙의 곁가지 글뿐이다
- 기능 적합성
  - 근거: 완료 조건 1 통과: 다섯 글이 저마다 제 절에 있다
  - 근거: 완료 조건 2 통과: 테스트 `OK`, 글 지우기 셋 모두 기대한 `FAIL:` 줄
  - 근거: 완료 조건 3 통과: 버전 0.19.0 둘, 검증 통과, ARCHITECTURE 줄과 docstring이 맞다
  - 등급: A — 완료 조건의 확인이 모두 통과한다

**Sonar way 게이트**
- 새 문제 0개: 1개. 실패
- 새 보안 핫스팟 모두 검토: 0/0. 통과
- 새 줄 커버리지 80% 이상: 측정 못함 (잴 새 줄 23줄)
- 새 줄 중복 3% 이하: 측정 못함 (잴 새 줄 23줄)
- 게이트: 실패

**소스 문제**
1. 작업 트리를 얻는 예로 든 `git stash create`는 추적하지 않는 새 파일을 넣지 않고 새 파일만 바뀌었으면 아무것도 내지 않아, 새 파일을 만드는 phase의 통과 조건이 이 예를 따르면 그 파일이 없는 트리를 본다. 예를 `cp -R` 사본으로 줄이거나 새 파일이 빠진다는 단서를 단다 (`plugins/plate/skills/plan/SKILL.md:249`). 범주: 신뢰성

**하네스에서 걸린 것**
- 이 프로젝트는 커버리지·중복·보안 검사 도구를 두지 않아(ADR-024) 잴 새 줄이 23줄로 20줄을 넘는데도 게이트의 커버리지와 중복이 측정 못함이다
- 완료 조건 1의 확인이 본문을 읽기만 하는 확인이고 plan의 동작은 `돌리지 않음`이라, 고친 규칙대로 초안이 적히는지는 이 평가에서도 보이지 않는다
