# 회고

## 회고 1

**확인**
- `tests/test_cleanup_skill.py`가 `section`과 앞머리 읽기를 `tests/test_skill_rules.py`에서 불러 쓰고, 자기 정의를 두지 않는다(유지보수성-2).
  - `grep -n -e '^def section' -e '^def front_matter' tests/test_cleanup_skill.py` → 출력 없음(rc=1). 통과
  - `grep -n 'from test_skill_rules import' tests/test_cleanup_skill.py` → `15:from test_skill_rules import front_matter, section  # noqa: E402` 한 줄. 통과
- 편집 훅의 hooks.json 시험이 matcher로 명령을 고르고, 두 훅 시험이 함께 쓰는 도우미가 `tests/hook_helpers.py` 한 곳에 있다(유지보수성-3).
  - `grep -n -F '["PreToolUse"][0]' tests/test_edit_guard.py tests/test_push_guard.py` → 출력 없음(rc=1). 통과
  - `grep -ln 'hook_helpers' tests/test_edit_guard.py tests/test_push_guard.py` → `tests/test_edit_guard.py`, `tests/test_push_guard.py` 두 파일. 통과
  - 작업 트리를 `cp -R`로 `mktemp -d` 사본에 옮기고 사본의 `plugins/plate/hooks/hooks.json`에서 `PreToolUse`를 뒤집어(matcher 차례 `['Bash', 'Edit|Write|MultiEdit|NotebookEdit']`) 사본에서 `python3 -m unittest tests.test_edit_guard.HooksJsonCommandTest tests.test_push_guard.HooksJsonTest` → `Ran 6 tests`, `OK`. 통과
- `tests/test_skill_rules.py`의 docstring이 파일이 하는 일을 적는다(유지보수성-4).
  - `python3 -c "import ast; print(ast.get_docstring(ast.parse(open('tests/test_skill_rules.py', encoding='utf-8').read())))"` → 스킬 본문의 규칙 글이 제 절에 있는지와 앞머리 한도를 본다는 세 줄. `release-prep`도 `#` 뒤 숫자도 없다. 통과
- 두 매니페스트의 description이 같은지 테스트가 보고, 한쪽만 바뀌면 실패한다(유지보수성-6).
  - `python3 -m unittest tests.test_manifests -v` → `test_descriptions_match (tests.test_manifests.DescriptionTest) ... ok`, `Ran 3 tests`, `OK`. 통과
  - `cp -R` 사본에서 `plugins/plate/.codex-plugin/plugin.json`의 description 끝에 `x`를 더해 사본에서 `python3 -m unittest tests.test_manifests` → `FAILED (failures=1)`. 통과
- 스킬 description 열 개가 저마다 400자 이하이고, 테스트가 400자 상한과 지금 지키는 글을 지킨다(성능-7).
  - `python3 -m unittest tests.test_skill_rules.DescriptionTest -v` → `test_description_at_most_400_chars ... ok`를 포함해 `Ran 6 tests`, `OK`. 통과
  - `claude plugin validate plugins/plate` → `✔ Validation passed`. 통과
  - 돌리지 않음 줄(스킬이 골라지는지 보는 시험): task 머리가 돌리지 않기로 정했다. 본 곳: 열 개 description의 길이를 직접 셌다(check 184, cleanup 321, context 216, eval 271, phase 207, plan 245, retro 280, review 308, run 306, setup 249자). 모두 `쓰지 않는다.`로 끝나고 run은 부르는 말 넷과 `계획이 없는 요청에는 쓰지 않는다`를, eval은 `"eval에만"`을 담는다
- `docs/ARCHITECTURE.md`의 디렉터리 구조가 바뀐 테스트와 맞다.
  - `grep -n -e 'hook_helpers.py' -e 'test_manifests.py' -e 'description 400자' docs/ARCHITECTURE.md` → 34행(`hook_helpers.py`), 39행(`test_manifests.py`, 버전과 description), 40행(`plate의 description 400자`). `## 디렉터리 구조`(9행)와 `## 패턴과 규칙`(44행) 사이라 셋 다 디렉터리 구조 절 안이다. 통과
- 테스트 묶음이 모두 통과하고 앞 task들의 시험이 그대로 돈다.
  - `python3 -m unittest discover -s tests` → `Ran 239 tests`, 마지막 줄 `OK`. 통과
  - `python3 -m unittest tests.test_verdict.BundleShapeTest tests.test_skill_rules.RunRulesTest.test_no_result_relaunch_limit tests.test_skill_rules.RunRulesTest.test_stop_line_grep_runs_on_fake_runlog -v` → `Ran 5 tests`, `OK`. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 239 tests`, `OK`. 통과

**남은 것**
- phase 1: `test_skill_rules.py` docstring은 한도를 "description과 name의 한도"로만 적고 숫자를 뺐다. 400자 상한은 phase 2가 정한다 → 문제 아님 (완료 조건 3은 tasks 이름과 이슈 번호가 없는 일반 설명만 요구하고, phase 2가 `DescriptionTest` 클래스 docstring과 ARCHITECTURE 40행에 400자를 적었다)
- phase 2: description이 짧아져 모델이 스킬을 고르는 판단이 바뀔 수 있고, 골라지는지 보는 시험은 돌리지 않았다 → 문제 아님 (task 머리 완료 조건 5의 `돌리지 않음` 줄이 돌리지 않기로 정한 동작이다. 부르는 말과 쓰지 않을 때의 글은 열 개 모두에 남아 있음을 직접 읽었다)
- phase 2: 줄인 description에서 빠진 세부(plan의 브랜치 물음 갈래, run의 기본 브랜치 되돌림 물음, review PR 모드의 네 범주)는 본문에만 있다 → 문제 아님 (task 머리 목표와 tasks 머리 결정이 description에 무엇을 내는지·언제 쓰는지·쓰지 않을 때만 두기로 했고, 범위 밖이 본문 절차를 바꾸지 않게 했다. 본문은 그대로다)

**문제**
- 없음

**판정**: 통과
