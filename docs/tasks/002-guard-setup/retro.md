# 회고

## 회고 1

**확인**
- (완료 조건 1) 판정 스크립트는 바뀐 파일 목록에 워크플로 경로가 있으면 merge 대신 request를 낸다. close와 request는 그대로이고, 목록을 받지 않으면 지금과 같다.
  - `python3 -m unittest discover -s tests` → `Ran 104 tests in 18.178s`, 마지막 줄 `OK`. 통과
  - `tests/test_verdict.py`의 `ChangedFilesTest`를 읽음 → `test_workflow_path_turns_merge_into_request`(워크플로 경로가 든 목록이면 request), `test_workflow_path_keeps_close_and_request`(close 그대로, request 그대로), `test_no_list_or_no_workflow_path_is_unchanged`(목록 없음·빈 목록·워크플로 경로 없는 목록이면 merge, test fail이면 close)로 세 경우가 저마다 있다. 통과
- (완료 조건 2) 편집 훅은 아직 없는 `.github/CODEOWNERS`를 쓰는 것을 막지 않고, 이미 있는 것의 편집은 막는다.
  - `python3 -m unittest discover -s tests` → 마지막 줄 `OK`. 통과
  - `tests/test_edit_guard.py`를 읽음 → `PlanFirstTest.test_setup_writes_new_codeowners`와 `TestFirstTest.test_setup_writes_new_codeowners_in_test_first_phase`가 처음 쓰기(Write) 통과와, 커밋된 뒤 Edit·Write를 PLAN_FIRST·TEST_FIRST로 막음을 저마다 시험한다. 통과
- (완료 조건 3) setup이 CI 물음에 login을 보여 주고, CODEOWNERS를 결정대로 쓰거나 보고에 적고, ruleset 거는 법을 보고에 적고, 양식 워크플로가 바뀐 파일 목록을 넘긴다.
  - `plugins/plate/skills/setup/SKILL.md`의 2번 표 마지막 행(login을 보여 주고 CODEOWNERS 두 줄을 쓴다, 이미 있거나 login이 없으면 쓰지 않고 보고에 적는다), 3번 "CI 워크플로"의 CODEOWNERS 항목(승인·파일 없음·login 있음일 때만 `/.github/workflows/ @<login>`, `/.github/CODEOWNERS @<login>`), 4번의 CODEOWNERS 넣을 줄과 ruleset 거는 법(`gh api` 명령, Settings → Rules → Rulesets, 비공개 저장소 요금제, 유일한 코드 소유자 한계와 닫는 법), 양식 절의 설명과 verdict 잡(`gh pr diff "$PR" --name-only > changed-files.txt`, `verdict.py --changed-files changed-files.txt`)을 읽음 → 네 곳이 저마다 적는다. 통과
  - setup 4번 JSON과 `docs/TOOLS.md` 131줄 절의 JSON을 견줌 → `target: branch`, `conditions.ref_name.include: ["~DEFAULT_BRANCH"]`, `rules`의 `pull_request` 파라미터 다섯, `bypass_actors`(actor_id 5, RepositoryRole, pull_request)가 같다. `name`만 다르다. 통과
- (완료 조건 4) `docs/ARCHITECTURE.md`와 `docs/ADR.md`가 바뀐 동작과 맞는다.
  - `git show 807bfc6:docs/ARCHITECTURE.md`의 17·20·23·49줄이 지금 파일의 같은 줄과 같은 항목임을 보고, 지금 파일의 17줄(verdict.py의 `--changed-files`), 20줄(edit_guard 역할), 23줄(setup의 CODEOWNERS·ruleset 안내), 49줄(아직 없는 `plate-review.yml`·`.github/CODEOWNERS` 쓰기를 두 막음에서 뺀다), 51줄(PR의 CI: login, CODEOWNERS, ruleset 안내, 바뀐 파일 목록, ADR-023), 55줄(셋업), 74줄(verdict 잡)을 읽음 → 바뀐 동작과 어긋나지 않는다. 통과
  - `grep -n "ADR-023" -A3 docs/ADR.md` → 43줄 `### ADR-023`, 44~46줄에 결정, 이유, 트레이드오프. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 104 tests`, `OK`. 통과
- 테스트 먼저 기록: phase 1
  - `done-phase-1.md`의 "한 일" 테스트 먼저 항목 → 실패 출력(`AssertionError: 'merge' != 'request'`, `FAILED (failures=1)`) 뒤에 통과 출력(`Ran 17 tests`, `OK`)이 이 순서로 있다. 통과
- 테스트 먼저 기록: phase 2
  - `done-phase-2.md`의 "한 일" 테스트 먼저 항목 → 실패 출력(`FAILED (failures=2)`) 뒤에 통과 출력(`Ran 44 tests`, `OK`)이 이 순서로 있다. 통과

**문제**
- 없음

**판정**: 통과
