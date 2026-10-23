# Phase 2: 회고 1의 문제를 고친다

**목표**: 회고 1에서 나온 문제를 모두 고친다.

**테스트 먼저**: 예

**읽을 것**
- `docs/tasks/002-ci-workflow/retro.md`의 `## 회고 1` 절
- `plugins/plate/skills/setup/SKILL.md`
- `plugins/plate/hooks/edit_guard.py`
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/ADR.md`
- `docs/TOOLS.md`

**TODO**
- [x] 이미 셋업된 프로젝트(`AGENTS.md`에 문서 지도 구간이 있다)에서 setup을 다시 불러 CI 에이전트를 승인하면 워크플로를 쓰지 못한다. setup 3번의 "CI 워크플로"는 편집 훅을 피하려고 워크플로를 `AGENTS.md`보다 먼저 쓰게 하지만, 그 순서는 처음 셋업하는 프로젝트만 풀고, 문서 지도 구간이 이미 있으면 남은 phase가 없는 한 `edit_guard.py`의 `check`(209~214줄)가 `.github/workflows/plate-review.yml`의 Write를 막는다. 문서 지도 구간이 있는 git 레포를 만들고 그 Write의 훅 입력을 넣어 보니 "plate: 남은 phase가 있는 task가 없어서 코드 파일을 고치지 않는다: `.github/workflows/plate-review.yml`"과 종료 코드 2가 나왔다(문서 지도 구간이 없으면 0). setup 2번은 문서 지도 구간이 있는 프로젝트를 다시 부르는 경우를 다루므로, task 머리의 목표("승인하면 워크플로 파일을 쓰고")가 그 경우에 맞지 않고, setup 본문에 막혔을 때의 길이 없다 (`plugins/plate/skills/setup/SKILL.md`, `plugins/plate/hooks/edit_guard.py`)

**통과 조건**
- 회고 1의 문제가 모두 고쳐졌다.
  - 확인: 문제마다 적힌 곳을 다시 읽거나 돌린다
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다

## 한 일
- 이미 셋업된 프로젝트에서 setup을 다시 불러 CI 에이전트를 승인하면 워크플로를 쓰지 못한다: 편집 훅이 `.github/workflows/plate-review.yml`이 아직 없을 때는 남은 phase가 없어도 그 파일의 편집을 통과시키게 했다. `CI_WORKFLOW` 상수를 두고 `check`의 `is_code_file`·`is_setup` 검사 바로 뒤, 남은 phase를 보기 전에 "이 경로이고 파일이 없으면 통과"를 더했다. 이미 있는 그 파일의 Edit와 Write, 다른 워크플로 파일은 전과 같이 "계획부터 세운다"로 막는다. 훅의 시험에 `PlanFirstTest.test_setup_writes_new_ci_workflow`를 더했다(셋업됐고 남은 phase가 없는 프로젝트에서 새 `plate-review.yml`의 Write는 통과, `other.yml`의 Write는 막음, 파일을 커밋한 뒤 Edit와 Write는 막음). 막히지 않게 됐으니 setup 3번 "CI 워크플로"에서 훅을 피하려던 "`AGENTS.md`를 고치기 전에 쓴다"와 그 이유를 뺐다. `docs/ARCHITECTURE.md`의 패턴과 규칙에서 훅 설명(46줄)에 이 예외를 더하고, PR의 CI 항목(48줄)의 "`AGENTS.md`를 고치기 전에 쓴다(훅이 … 막는다)"를 "승인하면 쓴다. 훅은 남은 phase가 없어도 아직 없는 이 파일을 쓰는 것은 막지 않아서, 이미 셋업된 프로젝트에서 setup을 다시 불러도 쓴다"로 바꿨다 (`plugins/plate/hooks/edit_guard.py`, `tests/test_edit_guard.py`, `plugins/plate/skills/setup/SKILL.md`, `docs/ARCHITECTURE.md`)
- 테스트 먼저
  - 실패: `python3 -m unittest tests.test_edit_guard.PlanFirstTest.test_setup_writes_new_ci_workflow` → `` AssertionError: 2 != 0 : 통과해야 하는데 막았다: plate: 남은 phase가 있는 task가 없어서 코드 파일을 고치지 않는다: `.github/workflows/plate-review.yml` `` / `Ran 1 test in 0.175s` / `FAILED (failures=1)`
  - 통과: `python3 -m unittest tests.test_edit_guard.PlanFirstTest.test_setup_writes_new_ci_workflow` → `Ran 1 test in 0.601s` / `OK`

## 확인 결과
- 회고 1의 문제가 모두 고쳐졌다.
  - 회고가 돌린 것을 다시 돌렸다: 스크래치 폴더에 문서 지도 구간이 있는 `AGENTS.md`, `CLAUDE.md`, `docs/tasks/.gitkeep`만 커밋한 git 레포를 만들고 `{"cwd": …, "hook_event_name": "PreToolUse", "tool_name": "Write", "tool_input": {"file_path": "<레포>/.github/workflows/plate-review.yml"}}`를 고친 훅(`python3 plugins/plate/hooks/edit_guard.py`)에 넣음 → 출력 없이 종료 코드 0. 같은 입력을 고치기 전의 훅(`git show HEAD:plugins/plate/hooks/edit_guard.py`)에 넣음 → "plate: 남은 phase가 있는 task가 없어서 코드 파일을 고치지 않는다: `.github/workflows/plate-review.yml`"과 종료 코드 2. 고친 훅에서 `.github/workflows/other.yml`의 Write는 종료 코드 2, `plate-review.yml`을 만든 뒤의 Edit는 종료 코드 2. `plugins/plate/skills/setup/SKILL.md` 84줄을 다시 읽음 → "CI 에이전트를 승인받았으면 … `.github/workflows/plate-review.yml`을 가져와 그 경로에 쓴다. 거절했으면 쓰지 않는다." 처음 셋업하는 프로젝트든 다시 부른 프로젝트든 승인하면 쓰므로 task 머리의 목표와 맞다. 통과
- task 머리의 완료 조건이 모두 참이다.
  - 완료 조건 1: `plugins/plate/skills/setup/SKILL.md`를 `grep -n`으로 봄 → 1번 24줄 "여섯 가지를 판정", 48줄 "GitHub 원격"(`git remote -v`에 `github.com` 원격), 50줄 "plate 워크플로"(`.github/workflows/` 아래에 `plate@harness-plate`가 적힌 파일). 2번 63줄 `| GitHub 원격이 있고 plate 워크플로가 없다 | CI 에이전트를 둘지. … |`. 3번 84줄 승인받았으면 양식의 `.github/workflows/plate-review.yml`을 그 경로에 쓰고 거절했으면 쓰지 않는다. 4번 109줄 `CLAUDE_CODE_OAUTH_TOKEN`, `claude setup-token`, `gh secret set` 또는 Settings → Secrets and variables → Actions. 양식 절 294줄 `.github/workflows/plate-review.yml`. GitHub 원격이 없으면 표의 조건이 맞지 않아 묻지 않고, 3번은 승인받았을 때만 쓴다. 통과
  - 완료 조건 2(양식): 양식 절의 YAML 블록을 `python3 -I`로 스크래치 파일에 뽑아 `ruby -ryaml`로 파싱함 → 트리거 `{"pull_request":{"types":["opened","synchronize","reopened"]}}`, `plugin_marketplaces: https://github.com/werwer748/harness-plate.git`(토큰 입력 없음), `plugins: plate@harness-plate`, prompt `/plate:review PR 모드, 기준 브랜치: origin/${{ github.base_ref }}, 평가서 파일: ${{ runner.temp }}/plate-review.md`, `claude_args`에 일곱 키가 모두 required인 `--json-schema`, `review` 잡 출력 `bundle: ${{ steps.review.outputs.structured_output }}`, `review` 잡 권한 `{"contents":"read","pull-requests":"read"}`, `verdict` 잡은 `needs: review`, 권한 `{"contents":"write","pull-requests":"write"}`이고 run에 판정 스크립트, `gh pr comment "$PR" --body-file comment.md`, merge면 `gh pr merge "$PR" --merge --delete-branch --match-head-commit "$HEAD_SHA"`, close면 `gh pr close "$PR"`. 통과
  - 완료 조건 2(판정 스크립트): `docs/ARCHITECTURE.md` 17줄의 `plugins/plate/ci/verdict.py`와 양식의 `python3 harness-plate/plugins/plate/ci/verdict.py`(`werwer748/harness-plate`를 `path: harness-plate`로 받은 자리)를 견줌 → 같은 파일이고 입력은 둘 다 stdin의 등급 묶음 JSON 하나. `--json-schema`의 키와 값이 `verdict.py` docstring(4~9줄)과 같다. 묶음 셋을 `python3 plugins/plate/ci/verdict.py`에 넣음 → 전부 A·커버리지 85.5는 `merge`, 커버리지 `unmeasured`는 `request`, 빌드 fail·보안 C는 `close`. 통과
  - 완료 조건 3: `docs/ARCHITECTURE.md`를 `grep -n`으로 봄 → 디렉터리 구조 22줄 setup이 CI 워크플로(`.github/workflows/plate-review.yml`) 양식을 담는다, 패턴과 규칙 48줄 PR의 CI 항목(setup이 승인하면 쓴다, 두 잡의 권한, 판정 스크립트, merge commit, ADR-021), 데이터 흐름 52줄 셋업이 승인하면 `.github/workflows/plate-review.yml`, 67~71줄 PR → review 잡 → verdict 잡의 흐름. `docs/ADR.md` 33~36줄 ADR-021(결정, 이유, 트레이드오프). 통과
- 명령 절의 테스트: `python3 -m unittest discover -s tests` → `Ran 54 tests in 15.311s` / `OK`. 통과

## 계획과 달라진 점
- TODO가 고칠 곳으로 적은 파일은 `plugins/plate/skills/setup/SKILL.md`와 `plugins/plate/hooks/edit_guard.py`이고, 실제로는 `tests/test_edit_guard.py`(테스트 먼저)와 `docs/ARCHITECTURE.md`의 두 줄(46줄, 48줄)도 고쳤다. 까닭: ARCHITECTURE의 두 줄이 "훅이 막으니 `AGENTS.md`보다 먼저 쓴다"를 적고 있어 고친 훅의 동작과 맞지 않게 됐다.

## 남은 것
없음

## 하네스에서 걸린 것
없음

## 확인 1

**통과 조건**
- 회고 1의 문제가 모두 고쳐졌다.
  - 스크래치 폴더에 문서 지도 구간(`<!-- plate:docs-map:start -->`)이 있는 `AGENTS.md`, `CLAUDE.md`, `docs/tasks/.gitkeep`만 커밋한 git 레포를 만들고, `{"cwd": …, "hook_event_name": "PreToolUse", "tool_name": "Write", "tool_input": {"file_path": "<레포>/.github/workflows/plate-review.yml"}}`를 `python3 plugins/plate/hooks/edit_guard.py`에 넣음 → 출력 없이 종료 코드 0. 같은 입력을 고치기 전의 훅(`git show d850595^:plugins/plate/hooks/edit_guard.py`)에 넣음 → "plate: 남은 phase가 있는 task가 없어서 코드 파일을 고치지 않는다: `.github/workflows/plate-review.yml`"과 종료 코드 2. 고친 훅에서 `.github/workflows/other.yml`의 Write는 종료 코드 2, `plate-review.yml`을 만든 뒤의 Edit와 Write는 둘 다 종료 코드 2. `plugins/plate/skills/setup/SKILL.md` 84줄 "CI 워크플로"를 읽음 → 승인받았으면 양식의 `.github/workflows/plate-review.yml`을 그 경로에 쓰고 거절했으면 쓰지 않는다. 훅을 피하는 순서("`AGENTS.md`를 고치기 전에 쓴다")는 본문에 남아 있지 않다(`grep -n "먼저 쓴\|고치기 전\|편집 훅"` → 없음). 처음 셋업이든 다시 부른 셋업이든 승인하면 쓰므로 task 머리의 목표와 맞다. 통과
- task 머리의 완료 조건이 모두 참이다.
  - 완료 조건 1: `plugins/plate/skills/setup/SKILL.md` 19~111줄과 294줄을 읽음 → 1번 24줄 여섯 가지 판정, 48줄 "GitHub 원격"(`git remote -v`에 `github.com` 원격), 50줄 "plate 워크플로"(`.github/workflows/` 아래에 `plate@harness-plate`가 적힌 파일). 2번 승인 표 63줄 `| GitHub 원격이 있고 plate 워크플로가 없다 | CI 에이전트를 둘지. … |`. 3번 84줄 승인받았으면 양식대로 쓰고 거절했으면 쓰지 않는다. 4번 109줄 `CLAUDE_CODE_OAUTH_TOKEN`, `claude setup-token`, `gh secret set` 또는 Settings → Secrets and variables → Actions. 양식 절 294줄 `.github/workflows/plate-review.yml`. GitHub 원격이 없으면 표의 조건이 맞지 않아 묻지 않고 3번은 승인받았을 때만 쓴다. 통과
  - 완료 조건 2(양식): 양식 절의 YAML 블록(73줄)을 `awk`로 스크래치 파일에 뽑아 `ruby -ryaml`로 파싱함 → 트리거 `{"pull_request":{"types":["opened","synchronize","reopened"]}}`, `plugin_marketplaces: https://github.com/werwer748/harness-plate.git`(마켓플레이스에 토큰 입력 없음), `plugins: plate@harness-plate`, prompt `/plate:review PR 모드, 기준 브랜치: origin/${{ github.base_ref }}, 평가서 파일: ${{ runner.temp }}/plate-review.md`, `review` 잡 출력 `bundle: ${{ steps.review.outputs.structured_output }}`, `review` 잡 권한 `{"contents":"read","pull-requests":"read"}`. `claude_args`를 `shlex`로 나눠 `--json-schema`를 파싱함 → 일곱 키 모두 required, `additionalProperties: false`. `verdict` 잡은 `needs: review`, 권한 `{"contents":"write","pull-requests":"write"}`, `werwer748/harness-plate`를 `path: harness-plate`로 checkout. 통과
  - 완료 조건 2(판정 스크립트): `docs/ARCHITECTURE.md` 17줄 `plugins/plate/ci/verdict.py`와 양식의 `python3 harness-plate/plugins/plate/ci/verdict.py`를 견줌 → 같은 파일이고 입력은 둘 다 stdin의 등급 묶음 JSON 하나. `--json-schema`의 키와 enum을 `verdict.py` docstring(4~9줄)과 `COMMANDS`, `GRADES`에 대어 봄 → 같다. `verdict` 잡의 run을 가짜 `gh`와 실제 `verdict.py`로 `bash --noprofile --norc -eo pipefail`에서 돌림 → 전부 A·커버리지 85.5는 `gh pr comment 7 --body-file comment.md` 뒤 `gh pr merge 7 --merge --delete-branch --match-head-commit abc`와 댓글 첫 줄 "판정: 자동 머지", 커버리지 `unmeasured`는 댓글만과 "판정: 머지 요청", 빌드 fail·보안 C는 댓글 뒤 `gh pr close 7`과 "판정: 닫기", 모두 종료 코드 0. 통과
  - 완료 조건 3: `docs/ARCHITECTURE.md`를 읽음 → 디렉터리 구조 22줄 setup이 CI 워크플로(`.github/workflows/plate-review.yml`) 양식을 담는다, 패턴과 규칙 48줄 PR의 CI 항목(setup이 승인하면 쓴다, 두 잡의 권한, 판정 스크립트, merge commit, ADR-021), 데이터 흐름 52줄 셋업이 승인하면 `.github/workflows/plate-review.yml`, 그 아래 PR → review 잡 → verdict 잡의 흐름. `docs/ADR.md` 33~36줄 ADR-021(결정, 이유, 트레이드오프). 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 54 tests in 15.553s` / `OK`. 통과

**테스트 먼저 기록**
- "한 일"의 "테스트 먼저" → 실패 출력(`AssertionError: 2 != 0 : 통과해야 하는데 막았다: …` / `FAILED (failures=1)`)이 먼저, 통과 출력(`Ran 1 test in 0.601s` / `OK`)이 그다음에 있다. 고치기 전의 훅을 넣은 스크래치 복사본에서 `python3 -m unittest tests.test_edit_guard.PlanFirstTest.test_setup_writes_new_ci_workflow`를 돌림 → `FAILED (failures=1)`로 기록의 실패 출력과 맞다. 통과

**실패**
- 없음

**하네스에서 걸린 것**
- 없음

**판정**: 통과
