# Phase 3: 회고 2의 문제를 고친다

**목표**: 회고 2에서 나온 문제를 모두 고친다.

**테스트 먼저**: 예

**읽을 것**
- `docs/tasks/002-ci-workflow/retro.md`의 `## 회고 2` 절
- `plugins/plate/hooks/edit_guard.py`
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/ADR.md`
- `docs/TOOLS.md`

**TODO**
- [x] 편집 훅의 CI 워크플로 예외가 테스트 먼저의 막음도 건너뛴다. `docs/ARCHITECTURE.md` 46줄은 훅이 "`phase-N.md`가 있는 task가 없을 때의 코드 편집(setup이 아직 없는 `.github/workflows/plate-review.yml`을 쓰는 것은 빼고)과 테스트 먼저인 phase에서 테스트 변경 없는 구현 편집을 막는다"고 적어 예외를 남은 phase가 없을 때에만 두지만, `edit_guard.py`의 `check`는 그 예외(212~213줄)를 남은 phase를 보기(215줄) 전에 두어 테스트 먼저 검사(219~229줄)에도 닿지 않는다. 문서 지도 구간, 테스트 먼저가 "예"인 `phase-1.md`, 커밋된 `tests/test_x.py`가 있고 커밋되지 않은 테스트 변경이 없는 git 레포를 스크래치에 만들어 새 `plate-review.yml`의 Write를 넣어 보니 지금 훅은 종료 코드 0, 고치기 전의 훅(`d850595^`)은 "지금 phase(`docs/tasks/001-a/phase-1.md`)는 테스트 먼저다. …"와 2였다(`src/app.py`는 둘 다 2). 코드의 주석도 예외를 "남은 phase가 없어도" 다시 부른 setup이 처음 쓰는 것으로 적는다 (`plugins/plate/hooks/edit_guard.py`, `docs/ARCHITECTURE.md`)

**통과 조건**
- 회고 2의 문제가 모두 고쳐졌다.
  - 확인: 문제마다 적힌 곳을 다시 읽거나 돌린다
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다

## 한 일
- 편집 훅의 CI 워크플로 예외가 테스트 먼저의 막음도 건너뛴다: `check`에서 새 `.github/workflows/plate-review.yml`을 통과시키는 예외를 남은 phase를 보기 전에서 `if not tasks:` 안으로 옮겨, 남은 phase가 없을 때만 그 파일을 통과시키고 남은 phase가 있으면 다른 코드 파일처럼 테스트 먼저 검사를 받게 했다. 주석은 "남은 phase가 없을 때 setup을 다시 불러 처음 쓰는 것"으로 고쳤다 (`plugins/plate/hooks/edit_guard.py`). 테스트 먼저인 phase에서 새 `plate-review.yml`의 Write가 테스트 먼저로 막히는지 보는 테스트 `TestFirstTest.test_new_ci_workflow_blocks_without_test_change`를 더했다 (`tests/test_edit_guard.py`). 패턴과 규칙의 PR CI 항목의 "훅은 남은 phase가 없어도 아직 없는 이 파일을 쓰는 것은 막지 않아서"를 "없을 때"로 고쳐 46줄의 예외 범위와 맞췄다 (`docs/ARCHITECTURE.md`)
- 테스트 먼저
  - 실패: `python3 -m unittest tests.test_edit_guard.TestFirstTest.test_new_ci_workflow_blocks_without_test_change` → `FAIL: test_new_ci_workflow_blocks_without_test_change (tests.test_edit_guard.TestFirstTest.test_new_ci_workflow_blocks_without_test_change)` / `AssertionError: 0 != 2 : 막아야 하는데 통과시켰다 (종료 코드 0): ` / `Ran 1 test in 0.256s` / `FAILED (failures=1)`
  - 통과: `python3 -m unittest tests.test_edit_guard.TestFirstTest.test_new_ci_workflow_blocks_without_test_change` → `Ran 1 test in 0.363s` / `OK`

## 확인 결과
- 회고 2의 문제가 모두 고쳐졌다.
  - 회고 2의 경우를 스크래치 git 레포에 다시 만들어(문서 지도 구간, 커밋된 `tests/test_x.py`, 커밋되지 않은 테스트 변경 없음) 고친 훅에 PreToolUse JSON을 넣음 → 테스트 먼저가 "예"인 `docs/tasks/001-a/phase-1.md`가 있을 때 새 `plate-review.yml`의 Write는 "plate: 지금 phase(`docs/tasks/001-a/phase-1.md`)는 테스트 먼저다. …"와 종료 코드 2, `src/app.py`의 Edit도 같은 글과 2. 테스트 먼저가 "아니오"이면 새 `plate-review.yml`의 Write는 0. 남은 phase가 없으면 새 `plate-review.yml`의 Write는 0, `other.yml`의 Write와 `src/app.py`의 Edit는 "남은 phase가 있는 task가 없어서 …"와 2, 이미 있는 `plate-review.yml`의 Edit·Write는 2. 통과
  - `plugins/plate/hooks/edit_guard.py`의 `check`를 다시 읽음 → 예외(214~216줄)가 `if not tasks:` 안에 있고 주석이 "남은 phase가 없을 때 setup을 다시 불러 처음 쓰는 것"이다. `docs/ARCHITECTURE.md` 46줄(예외를 남은 phase가 없을 때에만 둔다)과 48줄("훅은 남은 phase가 없을 때 아직 없는 이 파일을 쓰는 것은 막지 않아서")이 코드와 같다. 통과
- task 머리의 완료 조건이 모두 참이다.
  - 완료 조건 1: `plugins/plate/skills/setup/SKILL.md`를 읽음 → 1번 24줄 "여섯 가지를 판정", 48줄 "GitHub 원격", 50줄 "plate 워크플로", 2번 63줄 승인 표의 행 "GitHub 원격이 있고 plate 워크플로가 없다 | CI 에이전트를 둘지. …", 3번 84줄 "CI 에이전트를 승인받았으면 … `.github/workflows/plate-review.yml`을 가져와 그 경로에 쓴다. 거절했으면 쓰지 않는다"(73줄 "아래에 적힌 것만 한다"), 4번 109줄 `claude setup-token`과 `gh secret set CLAUDE_CODE_OAUTH_TOKEN` 또는 Settings → Secrets and variables → Actions, 양식 절 294줄 `.github/workflows/plate-review.yml`. 통과
  - 완료 조건 2: 양식 절의 YAML 블록을 `awk`로 스크래치 파일에 뽑아 `ruby -ryaml`로 파싱함 → 트리거 `{"pull_request":{"types":["opened","synchronize","reopened"]}}`, `plugin_marketplaces` `https://github.com/werwer748/harness-plate.git`(with의 키는 `claude_code_oauth_token, github_token, plugin_marketplaces, plugins, prompt, claude_args`로 마켓플레이스 토큰 입력 없음), `plugins` `plate@harness-plate`, prompt `/plate:review PR 모드, 기준 브랜치: origin/${{ github.base_ref }}, 평가서 파일: ${{ runner.temp }}/plate-review.md`, 출력 `bundle: ${{ steps.review.outputs.structured_output }}`, `review` 권한 `{"contents":"read","pull-requests":"read"}`, `verdict`는 `needs: review`, 권한 `{"contents":"write","pull-requests":"write"}`, run에 판정 스크립트, `gh pr comment`, `gh pr merge "$PR" --merge --delete-branch --match-head-commit "$HEAD_SHA"`, `gh pr close "$PR"`. 통과
  - 완료 조건 2의 둘째 확인: 양식의 `python3 harness-plate/plugins/plate/ci/verdict.py`(`werwer748/harness-plate`를 `path: harness-plate`로 받은 자리)와 `docs/ARCHITECTURE.md` 17줄의 `plugins/plate/ci/verdict.py`가 같은 파일이고 입력은 둘 다 stdin의 등급 묶음 JSON 하나. `claude_args`를 `shlex`로 나눠 `--json-schema`를 `verdict.py`의 `COMMANDS`, `GRADES`에 `python3 -I`의 assert로 견줌 → `schema keys: ['build', 'coverage', 'lint', 'maintainability', 'reliability', 'security', 'test'] -> verdict.py와 같다`. `verdict` 잡의 run을 가짜 `gh`와 실제 `verdict.py`로 `bash --noprofile --norc -eo pipefail`에서 돌림 → 전부 A·커버리지 85.5는 댓글 뒤 `gh pr merge 7 --merge --delete-branch --match-head-commit abc`와 "판정: 자동 머지", 커버리지 `unmeasured`는 댓글만과 "판정: 머지 요청", 빌드 fail·보안 C는 댓글 뒤 `gh pr close 7`과 "판정: 닫기", 모두 종료 코드 0. 통과
  - 완료 조건 3: `docs/ARCHITECTURE.md`와 `docs/ADR.md`를 읽음 → 디렉터리 구조 17줄 `verdict.py`, 22줄 setup이 CI 워크플로 양식을 담는다, 패턴과 규칙 46줄 훅의 예외, 48줄 PR의 CI 항목(ADR-021), 데이터 흐름 52줄 셋업이 승인하면 `plate-review.yml`을 쓴다, 67~71줄 PR → review 잡 → verdict 잡. `docs/ADR.md` 33줄 ADR-021(결정, 이유, 트레이드오프). 통과
  - 명령 절의 테스트: `python3 -m unittest discover -s tests` → `Ran 55 tests in 16.822s` / `OK`. 통과

## 계획과 달라진 점
- 없음

## 남은 것
- 없음

## 하네스에서 걸린 것
- 없음

## 확인 1

**통과 조건**
- 회고 2의 문제가 모두 고쳐졌다.
  - 회고 2의 경우를 스크래치 git 레포에 만들어(문서 지도 구간, 커밋된 `tests/test_x.py`, `src/app.py`) 지금 훅, 고치기 전의 훅(`HEAD^`), 예외를 더하기 전의 훅(`d850595^`)에 PreToolUse JSON을 넣음 → 테스트 먼저가 "예"인 `docs/tasks/001-a/phase-1.md`가 있고 커밋되지 않은 테스트 변경이 없을 때 새 `plate-review.yml`의 Write는 지금 훅이 "plate: 지금 phase(`docs/tasks/001-a/phase-1.md`)는 테스트 먼저다. …"와 2(`HEAD^`는 0, `d850595^`는 2), `src/app.py`의 Edit와 `other.yml`의 Write도 2. 테스트 먼저가 "아니오"이거나 커밋되지 않은 테스트 변경이 있으면 새 `plate-review.yml`의 Write는 0. 남은 phase가 없으면 새 `plate-review.yml`의 Write는 0, `src/app.py`의 Edit와 `other.yml`의 Write는 "plate: 남은 phase가 있는 task가 없어서 …"와 2, 이미 있는 `plate-review.yml`의 Edit·Write는 2. 통과
  - `plugins/plate/hooks/edit_guard.py`의 `check`를 읽음 → 예외(215~216줄)가 `if not tasks:`(214줄) 안에 있어 테스트 먼저 검사(219~229줄)에 앞서지 않고, 주석은 "남은 phase가 없을 때 setup을 다시 불러 처음 쓰는 것"이다. `docs/ARCHITECTURE.md` 46줄(예외를 `phase-N.md`가 있는 task가 없을 때의 막음에만 둔다)과 48줄("훅은 남은 phase가 없을 때 아직 없는 이 파일을 쓰는 것은 막지 않아서")이 코드와 같다. `docs/tasks/` 밖의 `.md`와 `.py`에서 예외를 "남은 phase가 없어도"로 적은 곳을 `grep`으로 찾음 → 없다. 통과
- task 머리의 완료 조건이 모두 참이다.
  - 완료 조건 1: `plugins/plate/skills/setup/SKILL.md`를 읽음 → 1번 24줄 "여섯 가지를 판정", 48줄 "GitHub 원격"(`git remote -v`에 `github.com` 원격), 50줄 "plate 워크플로"(`.github/workflows/` 아래에 `plate@harness-plate`가 적힌 파일), 2번 63줄 승인 표의 행 "GitHub 원격이 있고 plate 워크플로가 없다 | CI 에이전트를 둘지. …", 3번 73줄 "아래에 적힌 것만 한다"와 84줄 "CI 에이전트를 승인받았으면 … `.github/workflows/plate-review.yml`을 가져와 그 경로에 쓴다. 거절했으면 쓰지 않는다", 4번 109줄 `claude setup-token`, `gh secret set CLAUDE_CODE_OAUTH_TOKEN`, Settings → Secrets and variables → Actions, 양식 절 294줄 `.github/workflows/plate-review.yml`. 통과
  - 완료 조건 2의 첫째 확인: 양식 절의 YAML 블록을 `awk`로 스크래치 파일에 뽑아 `ruby -ryaml`로 파싱함 → 트리거 `{"pull_request":{"types":["opened","synchronize","reopened"]}}`, `plugin_marketplaces` `https://github.com/werwer748/harness-plate.git`(with의 키는 `claude_code_oauth_token, github_token, plugin_marketplaces, plugins, prompt, claude_args`로 마켓플레이스 토큰 입력이 없다), `plugins` `plate@harness-plate`, prompt `/plate:review PR 모드, 기준 브랜치: origin/${{ github.base_ref }}, 평가서 파일: ${{ runner.temp }}/plate-review.md`, 출력 `bundle: ${{ steps.review.outputs.structured_output }}`, `claude_args`에 `--json-schema`, `review` 권한 `{"contents":"read","pull-requests":"read"}`, `verdict`는 `needs: review`, 권한 `{"contents":"write","pull-requests":"write"}`, run에 판정 스크립트, `gh pr comment "$PR" --body-file comment.md`, `gh pr merge "$PR" --merge --delete-branch --match-head-commit "$HEAD_SHA"`, `gh pr close "$PR"`. 통과
  - 완료 조건 2의 둘째 확인: 양식의 `python3 harness-plate/plugins/plate/ci/verdict.py`(`werwer748/harness-plate`를 `path: harness-plate`로 받은 자리)와 `docs/ARCHITECTURE.md` 16~17줄의 `plugins/plate/ci/verdict.py`가 같은 파일이고, 입력은 둘 다 stdin의 등급 묶음 JSON 하나다. `claude_args`를 `shlex`로 나눠 `--json-schema`를 `verdict.py`의 `COMMANDS`, `GRADES`와 docstring의 값에 `python3 -I`의 assert로 견줌 → `schema keys: ['build', 'coverage', 'lint', 'maintainability', 'reliability', 'security', 'test'] -> verdict.py와 같다`. `verdict` 잡의 run을 가짜 `gh`와 실제 `verdict.py`로 `bash --noprofile --norc -eo pipefail`에서 돌림 → 전부 pass·A·커버리지 85.5는 `gh pr comment 7 --body-file comment.md` 뒤 `gh pr merge 7 --merge --delete-branch --match-head-commit abc`와 "판정: 자동 머지", 커버리지 `unmeasured`는 댓글만과 "판정: 머지 요청", 빌드 fail·보안 C는 댓글 뒤 `gh pr close 7`과 "판정: 닫기", 모두 종료 코드 0. 통과
  - 완료 조건 3: `docs/ARCHITECTURE.md`와 `docs/ADR.md`를 읽음 → 디렉터리 구조 16~17줄 `ci/verdict.py`, 22줄 setup이 CI 워크플로 양식을 담는다, 패턴과 규칙 46줄 훅의 예외, 48줄 PR의 CI 항목(ADR-021), 데이터 흐름 52줄 셋업이 승인하면 `plate-review.yml`을 쓴다, 67~71줄 PR → review 잡 → verdict 잡. `docs/ADR.md` 33~36줄 ADR-021(결정, 이유, 트레이드오프). 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 55 tests in 16.812s` / `OK`. 통과

**테스트 먼저 기록**
- "한 일"의 "테스트 먼저" → 실패 출력(`FAIL: test_new_ci_workflow_blocks_without_test_change …` / `AssertionError: 0 != 2 : 막아야 하는데 통과시켰다 (종료 코드 0): ` / `FAILED (failures=1)`)이 먼저, 통과 출력(`Ran 1 test in 0.363s` / `OK`)이 그다음에 있다. 스크래치에 고치기 전의 훅(`git show HEAD^:plugins/plate/hooks/edit_guard.py`)과 지금의 `tests/`를 두고 그 테스트를 돌림 → `FAILED (failures=1)`, 저장소에서는 위 테스트 명령에서 `OK`. 통과

**실패**
- 없음

**하네스에서 걸린 것**
- 없음

**판정**: 통과
