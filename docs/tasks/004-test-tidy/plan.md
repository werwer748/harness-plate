# 테스트를 정리하고 스킬 description을 줄인다

## 목표
정리 점검 2026-10-29의 유지보수성-2·3·4·6(테스트 도우미의 중복과 자리 번호, 낡은 docstring, 매니페스트 description 견주기)과 성능-7(스킬 description 열 개를 저마다 400자 이하로)을 고친다.

## 범위 밖
- 두 매니페스트(`plugin.json`)의 description을 줄이는 것. 같은지만 본다.
- 스킬 본문(앞머리 아래)의 절차를 바꾸는 것.
- 테스트가 지키는 규칙의 글을 바꾸는 것.

## 완료 조건
1. `tests/test_cleanup_skill.py`가 `section`과 앞머리 읽기를 `tests/test_skill_rules.py`에서 불러 쓰고, 자기 정의를 두지 않는다(유지보수성-2).
   - 확인: `grep -n -e '^def section' -e '^def front_matter' tests/test_cleanup_skill.py` → 아무것도 나오지 않음
   - 확인: `grep -n 'from test_skill_rules import' tests/test_cleanup_skill.py` → 한 줄
2. 편집 훅의 hooks.json 시험이 matcher로 명령을 고르고, 두 훅 시험이 함께 쓰는 도우미(`hooks.json` 명령을 `sh -c`로 돌리는 것, 막음·통과 assert)가 `tests/hook_helpers.py` 한 곳에 있다(유지보수성-3).
   - 확인: `grep -n -F '["PreToolUse"][0]' tests/test_edit_guard.py tests/test_push_guard.py` → 아무것도 나오지 않음
   - 확인: `grep -ln 'hook_helpers' tests/test_edit_guard.py tests/test_push_guard.py` → 두 파일
   - 확인: 작업 트리를 `cp -R`로 `mktemp -d` 사본에 옮기고, 사본의 `plugins/plate/hooks/hooks.json`에서 `PreToolUse`의 두 항목 차례를 바꿔 사본에서 `python3 -m unittest tests.test_edit_guard.HooksJsonCommandTest tests.test_push_guard.HooksJsonTest` → `OK`
3. `tests/test_skill_rules.py`의 docstring이 특정 tasks와 이슈 목록이 아니라 파일이 하는 일(스킬 본문의 규칙 글이 제 절에 있는지와 앞머리 한도)을 적는다(유지보수성-4).
   - 확인: `python3 -c "import ast; print(ast.get_docstring(ast.parse(open('tests/test_skill_rules.py', encoding='utf-8').read())))"` → `release-prep`도 `#3`처럼 `#` 뒤에 숫자가 붙은 이슈 번호도 없다
4. 두 매니페스트의 description이 같은지 테스트가 보고, 한쪽만 바뀌면 실패한다(유지보수성-6).
   - 확인: `python3 -m unittest tests.test_manifests -v` → `test_descriptions_match`가 있고 `OK`
   - 확인: 작업 트리를 `cp -R`로 `mktemp -d` 사본에 옮기고, 사본의 `plugins/plate/.codex-plugin/plugin.json`의 description 끝에 `x`를 더해 사본에서 `python3 -m unittest tests.test_manifests` → 실패(`FAILED`)
5. 스킬 description 열 개가 저마다 400자 이하이고, 무엇을 내는지·언제 쓰는지·쓰지 않을 때만 적고, 테스트가 400자 상한과 지금 지키는 글(끝의 `쓰지 않는다.`, run의 부르는 말 넷과 `계획이 없는 요청에는 쓰지 않는다`, eval의 `"eval에만"`)을 지킨다(성능-7).
   - 확인: `python3 -m unittest tests.test_skill_rules.DescriptionTest -v` → `test_description_at_most_400_chars`가 있고 `OK`
   - 확인: `claude plugin validate plugins/plate` → `Validation passed`
   - 돌리지 않음: description이 바뀌면 모델이 스킬을 고르는 판단이 바뀔 수 있는데, 여러 요청 글로 스킬이 골라지는지 보는 시험은 대화형 세션이 있어야 해 돌리지 않는다
6. `docs/ARCHITECTURE.md`의 디렉터리 구조가 바뀐 테스트와 맞다: `tests/hook_helpers.py` 줄이 있고, `test_manifests.py` 줄이 description도 견준다고 적고, `test_skill_rules.py` 줄의 description 한도가 400자다.
   - 확인: `grep -n -e 'hook_helpers.py' -e 'test_manifests.py' -e 'description 400자' docs/ARCHITECTURE.md` → 셋 다 디렉터리 구조 절에 나온다
7. 테스트 묶음이 모두 통과하고 앞 task들의 시험이 그대로 돈다(tasks 완료 조건 1~4).
   - 확인: `python3 -m unittest discover -s tests` → 마지막 줄이 `OK`
   - 확인: `python3 -m unittest tests.test_verdict.BundleShapeTest tests.test_skill_rules.RunRulesTest.test_no_result_relaunch_limit tests.test_skill_rules.RunRulesTest.test_stop_line_grep_runs_on_fake_runlog -v` → `OK`

## 결정
- 두 훅 시험의 공통 도우미는 `tests/hook_helpers.py`에 둔다. 이름이 `test_`로 시작하지 않아 시험 찾기가 모듈 자체를 시험으로 돌리지 않는다. (추천안으로 정함)
- description은 열 개 모두 400자 이하로 줄이고 그 상한을 테스트로 지킨다. 이유: 한 기준으로 맞춰야 다시 불어나지 않는다.
