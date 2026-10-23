# Phase 4: 회고 3의 문제를 고친다

**목표**: 회고 3에서 나온 문제를 모두 고친다.

**테스트 먼저**: 예

**읽을 것**
- `docs/tasks/002-ci-workflow/retro.md`의 `## 회고 3` 절
- `plugins/plate/hooks/edit_guard.py`
- `tests/test_edit_guard.py`
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/ADR.md`
- `docs/TOOLS.md`

**TODO**
- [x] 이미 셋업된 프로젝트에서 남은 phase가 테스트 먼저일 때 setup을 다시 불러 CI 에이전트를 승인하면 워크플로를 쓰지 못한다. phase 3이 `edit_guard.py`의 CI 워크플로 예외(215~216줄)를 `if not tasks:`(214줄) 안으로 옮겨, 남은 phase가 있으면 새 `plate-review.yml`의 Write도 테스트 먼저 검사(219~229줄)를 받는다. 문서 지도 구간과 커밋된 `tests/test_x.py`가 있는 git 레포를 스크래치에 만들어 그 Write의 훅 입력을 넣어 보니, 남은 phase가 없으면 종료 코드 0, 테스트 먼저가 "아니오"인 `docs/tasks/001-a/phase-1.md`가 남아 있으면 0, "예"인 `phase-1.md`가 남아 있고 커밋되지 않은 테스트 변경이 없으면 "plate: 지금 phase(`docs/tasks/001-a/phase-1.md`)는 테스트 먼저다. …"와 2였다. setup이 워크플로를 쓸 수 있는지가 진행 중인 task의 phase 표시에 따라 갈리고, 막혔을 때 훅의 글은 실패하는 테스트를 먼저 쓰라고 하며 setup 본문에 그때의 길이 없다. 그래서 task 머리의 목표("승인하면 워크플로 파일을 쓰고")가 이 경우에 맞지 않고, 회고 1의 문제가 남은 phase가 있는 경우로 좁혀져 남는다. `docs/ARCHITECTURE.md` 46줄과 48줄은 예외를 남은 phase가 없을 때로 적어 코드와는 맞는다. 회고 2의 문제는 코드와 46줄 가운데 어느 쪽을 고칠지 적지 않았고, phase 3은 코드를 46줄에 맞췄다 (`plugins/plate/hooks/edit_guard.py`, `docs/ARCHITECTURE.md`)

**통과 조건**
- 회고 3의 문제가 모두 고쳐졌다.
  - 확인: 문제마다 적힌 곳을 다시 읽거나 돌린다
- 편집 훅이 task 머리의 결정대로, 아직 없는 `plate-review.yml`의 Write를 남은 phase가 없을 때, 테스트 먼저가 "아니오"인 phase가 남았을 때, "예"인 phase가 남았을 때 모두 통과시키고, 이미 있는 그 파일의 Edit·Write와 `other.yml`의 Write는 막는다. `docs/ARCHITECTURE.md`와 코드의 주석이 같은 범위를 적는다.
  - 확인: `python3 -m unittest discover -s tests`가 통과하고, `tests/test_edit_guard.py`를 읽어 이 경우마다 테스트가 있다
  - 확인: `docs/ARCHITECTURE.md`의 훅 설명과 PR의 CI 항목, `edit_guard.py`의 예외 주석을 읽는다
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다

## 한 일
- 이미 셋업된 프로젝트에서 남은 phase가 테스트 먼저일 때 setup을 다시 불러 CI 에이전트를 승인하면 워크플로를 쓰지 못한다: 코드를 task 머리의 결정에 맞췄다. CI 워크플로 예외(아직 없는 `.github/workflows/plate-review.yml`이면 통과)를 `if not tasks:` 안에서 꺼내 `is_code_file`·`is_setup` 검사 바로 뒤, 남은 phase를 보기 전으로 옮겨 남은 phase가 있든 없든, 테스트 먼저든 아니든 통과시킨다. 이미 있으면 그 아래의 계획 먼저·테스트 먼저 막음을 그대로 받는다. 주석도 이 범위로 고쳤다 (`plugins/plate/hooks/edit_guard.py`). 테스트는 phase 3이 넣은 `TestFirstTest.test_new_ci_workflow_blocks_without_test_change`(테스트 먼저 "예"에서 새 파일의 Write를 막는다고 본 것)를 `test_setup_writes_new_ci_workflow_in_test_first_phase`로 바꿔, 테스트 먼저 "예"인 phase가 남았을 때 새 `plate-review.yml`의 Write는 통과, `other.yml`의 Write와 이미 있는 `plate-review.yml`의 Edit·Write는 테스트 먼저로 막는다고 보게 했고, 테스트 먼저 "아니오"인 phase가 남았을 때 새 파일의 Write가 통과하는 `test_setup_writes_new_ci_workflow_in_phase_without_test_first`를 더했다 (`tests/test_edit_guard.py`). `docs/ARCHITECTURE.md` 46줄은 예외를 "`phase-N.md`가 있는 task가 없을 때의 코드 편집" 괄호에서 꺼내 "setup이 아직 없는 `.github/workflows/plate-review.yml`을 쓰는 것은 두 막음에서 모두 뺀다"로, 48줄은 "훅은 아직 없는 이 파일을 쓰는 것을 남은 phase가 있든 없든, 테스트 먼저든 아니든 막지 않아서 … 이미 있는 이 파일의 편집과 다른 워크플로 파일은 다른 코드 파일처럼 막는다"로 고쳤다 (`docs/ARCHITECTURE.md`)
- 테스트 먼저
  - 실패: `python3 -m unittest tests.test_edit_guard.TestFirstTest.test_setup_writes_new_ci_workflow_in_test_first_phase tests.test_edit_guard.TestFirstTest.test_setup_writes_new_ci_workflow_in_phase_without_test_first` → `FAIL: test_setup_writes_new_ci_workflow_in_test_first_phase (tests.test_edit_guard.TestFirstTest.test_setup_writes_new_ci_workflow_in_test_first_phase)` / `` AssertionError: 2 != 0 : 통과해야 하는데 막았다: plate: 지금 phase(`docs/tasks/001-a/phase-1.md`)는 테스트 먼저다. 커밋되지 않은 변경에 테스트 파일이 없어서 테스트 파일이 아닌 코드 파일을 고치지 않는다: `.github/workflows/plate-review.yml` `` / `Ran 2 tests in 0.608s` / `FAILED (failures=1)`. "아니오"의 시험은 바뀌지 않는 동작이라 구현 전에도 통과했다
  - 통과: 같은 명령 → `Ran 2 tests in 1.027s` / `OK`

## 확인 결과
- 회고 3의 문제가 모두 고쳐졌다.
  - 회고 3의 재현을 스크래치(`/private/tmp/claude-501/-Users-gangjungi-Desktop-harness-plate/3eef7c5c-5f6a-4ba3-b7e6-8c6c3309866e/scratchpad/p4`)에 다시 만듦: 문서 지도 구간이 있는 `AGENTS.md`와 커밋된 `tests/test_x.py`가 있는 git 레포에 고친 훅으로 Write의 훅 입력을 넣음 → 남은 phase 없음: `plate-review.yml` 0, `other.yml` 2(계획 먼저). 테스트 먼저 "아니오"인 `docs/tasks/001-a/phase-1.md`: `plate-review.yml` 0. "예"인 `phase-1.md`, 커밋되지 않은 테스트 변경 없음: `plate-review.yml` 0, `other.yml` 2("plate: 지금 phase(`docs/tasks/001-a/phase-1.md`)는 테스트 먼저다. …"). `plate-review.yml`을 커밋해 둔 뒤 "예"에서 그 파일의 Edit 2, Write 2(테스트 먼저). setup이 워크플로를 쓸 수 있는지가 phase 표시에 따라 갈리지 않는다. `docs/ARCHITECTURE.md` 46줄, 48줄과 코드가 같은 범위를 적는다. 통과
- 편집 훅이 task 머리의 결정대로, 아직 없는 `plate-review.yml`의 Write를 남은 phase가 없을 때, 테스트 먼저가 "아니오"인 phase가 남았을 때, "예"인 phase가 남았을 때 모두 통과시키고, 이미 있는 그 파일의 Edit·Write와 `other.yml`의 Write는 막는다. `docs/ARCHITECTURE.md`와 코드의 주석이 같은 범위를 적는다.
  - `python3 -m unittest discover -s tests` → `Ran 56 tests in 17.499s` / `OK`. `tests/test_edit_guard.py`를 읽음 → 남은 phase 없음은 `PlanFirstTest.test_setup_writes_new_ci_workflow`(새 파일 Write 통과, `other.yml` Write와 이미 있는 파일의 Edit·Write는 계획 먼저로 막음), "예"는 `TestFirstTest.test_setup_writes_new_ci_workflow_in_test_first_phase`(새 파일 Write 통과, `other.yml` Write와 이미 있는 파일의 Edit·Write는 테스트 먼저로 막음), "아니오"는 `TestFirstTest.test_setup_writes_new_ci_workflow_in_phase_without_test_first`(새 파일 Write 통과). "아니오"인 phase에서는 이미 있는 파일과 `other.yml`의 편집이 다른 코드 파일처럼 통과하는 것이 지금의 동작이라(task 머리 결정의 "지금처럼 막는다") 막는 시험을 두지 않았다. 통과
  - `docs/ARCHITECTURE.md` 46줄("`phase-N.md`가 있는 task가 없을 때의 코드 편집과 테스트 먼저인 phase에서 테스트 변경 없는 구현 편집을 막는다. setup이 아직 없는 `.github/workflows/plate-review.yml`을 쓰는 것은 두 막음에서 모두 뺀다"), 48줄("훅은 아직 없는 이 파일을 쓰는 것을 남은 phase가 있든 없든, 테스트 먼저든 아니든 막지 않아서 … 이미 있는 이 파일의 편집과 다른 워크플로 파일은 다른 코드 파일처럼 막는다"), `edit_guard.py` 212~215줄의 예외와 주석("남은 phase가 있든 없든, 테스트 먼저든 아니든 통과시킨다. 이미 있으면 아래의 막음을 그대로 받는다")을 읽음 → 같은 범위다. 통과
- task 머리의 완료 조건이 모두 참이다.
  - 완료 조건 1: `plugins/plate/skills/setup/SKILL.md`를 읽음 → 1번 24줄 "여섯 가지를 판정", 48줄 GitHub 원격, 50줄 plate 워크플로, 2번 63줄 승인 표의 행 "GitHub 원격이 있고 plate 워크플로가 없다 | CI 에이전트를 둘지. …", 3번 73줄 "아래에 적힌 것만 한다", 84줄 "CI 에이전트를 승인받았으면 … `.github/workflows/plate-review.yml`을 가져와 그 경로에 쓴다. 거절했으면 쓰지 않는다", 4번 109줄 `CLAUDE_CODE_OAUTH_TOKEN`을 `claude setup-token`으로 만들어 `gh secret set`이나 Settings → Secrets and variables → Actions로 넣는 방법, 양식 절 294줄 `.github/workflows/plate-review.yml`. 통과
  - 완료 조건 2: 양식의 YAML 블록(298~372줄의 펜스 안)을 `awk`로 스크래치 `wf.yml`에 뽑아 `ruby -ryaml`로 파싱하고 `python3 -I`로 봄 → 트리거 `{"pull_request": {"types": ["opened", "synchronize", "reopened"]}}`, `review` 잡 권한 `{'contents': 'read', 'pull-requests': 'read'}`, 출력 `bundle: ${{ steps.review.outputs.structured_output }}`, `anthropics/claude-code-action@v1`의 with 키 `claude_code_oauth_token, github_token, plugin_marketplaces, plugins, prompt, claude_args`(마켓플레이스 토큰 없음), `plugin_marketplaces` `https://github.com/werwer748/harness-plate.git`, `plugins` `plate@harness-plate`, prompt `/plate:review PR 모드, 기준 브랜치: origin/${{ github.base_ref }}, 평가서 파일: ${{ runner.temp }}/plate-review.md`, `--json-schema`의 required 일곱 키와 `additionalProperties: False`, `verdict` 잡 `needs: review`, 권한 `{'contents': 'write', 'pull-requests': 'write'}`. 통과
  - 완료 조건 2: 양식의 `python3 harness-plate/plugins/plate/ci/verdict.py`(stdin으로 `$BUNDLE`)와 `docs/ARCHITECTURE.md` 17줄의 `plugins/plate/ci/verdict.py`를 견줌 → 같은 파일이고 입력은 stdin의 등급 묶음 JSON 하나. 스키마의 키와 enum을 `verdict.py` 4~9줄 docstring과 `COMMANDS`, `GRADES`에 대어 assert → "schema keys/enums match verdict.py docstring, COMMANDS, GRADES". `verdict` 잡의 run을 가짜 `gh`와 실제 `verdict.py`로 `bash --noprofile --norc -eo pipefail`에서 돌림 → 전부 A·커버리지 85.5: 종료 0, "판정: 자동 머지", `gh pr comment 7 --body-file comment.md` 뒤 `gh pr merge 7 --merge --delete-branch --match-head-commit abc`. 커버리지 `unmeasured`: 종료 0, "판정: 머지 요청", 댓글만. 빌드 fail·보안 C: 종료 0, "판정: 닫기", 댓글 뒤 `gh pr close 7`. 통과
  - 완료 조건 3: `docs/ARCHITECTURE.md`와 `docs/ADR.md`를 읽음 → 디렉터리 구조 16~17줄 `ci/verdict.py`, 22줄 setup이 CI 워크플로 양식을 담는다, 패턴과 규칙 46줄 훅의 예외, 48줄 PR의 CI 항목(ADR-021), 데이터 흐름 52줄 셋업이 승인하면 `.github/workflows/plate-review.yml`, 67~71줄 PR → review 잡 → verdict 잡. `docs/ADR.md` 33~36줄 ADR-021. 통과

## 계획과 달라진 점
- 없음

## 남은 것
- 없음

## 하네스에서 걸린 것
- 없음
