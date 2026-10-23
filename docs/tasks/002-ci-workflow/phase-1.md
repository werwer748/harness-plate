# Phase 1: setup의 CI 워크플로

**목표**: setup이 GitHub 원격이 있는 프로젝트에 CI 워크플로를 둘지 묻고, 승인하면 양식대로 워크플로 파일을 쓰고 시크릿 등록 방법을 안내한다.

**테스트 먼저**: 아니오 — 스킬 본문과 문서(`.md`)만 고친다

**읽을 것**
- `plugins/plate/skills/setup/SKILL.md` (판정, 승인 표, 쓰는 일, 보고, 양식)
- `plugins/plate/skills/review/SKILL.md`의 PR 모드 절 (`001-ci-review`가 적은 부르는 꼴과 등급 묶음의 꼴)
- `docs/ARCHITECTURE.md`의 디렉터리 구조 (`001-ci-review`가 만든 판정 스크립트의 경로. 입력과 출력의 꼴은 그 스크립트에 있다)
- `plugins/plate/hooks/edit_guard.py` (셋업된 프로젝트에서 남은 phase가 없으면 `.md`가 아닌 파일의 편집을 막는다)
- https://code.claude.com/docs/en/github-actions (설정, 시크릿 이름과 `claude setup-token`, permissions, `plugin_marketplaces`와 `plugins`로 플러그인 스킬 부르기)
- https://raw.githubusercontent.com/anthropics/claude-code-action/main/action.yml (입력과 `structured_output`)
- `docs/ADR.md` (항목의 꼴)

**TODO**
- [x] setup의 1번이 GitHub 원격과 plate 워크플로가 있는지를 보고, 2번의 승인 표에 "GitHub 원격이 있고 plate 워크플로가 없다 → CI 에이전트를 둘지"가 더해진다 (`plugins/plate/skills/setup/SKILL.md`)
- [x] 승인하면 setup이 양식 절의 워크플로를 `.github/workflows/` 아래에 쓰고, 4번의 보고에 `CLAUDE_CODE_OAUTH_TOKEN` 시크릿 등록 방법(`claude setup-token`으로 토큰을 만들어 저장소 시크릿으로 넣는다)이 들어간다 (`plugins/plate/skills/setup/SKILL.md`)
- [x] 양식 절에 워크플로가 생긴다. PR이 열리거나 갱신될 때 돌고, 공개 마켓플레이스에서 plate를 받아 review의 PR 모드를 부르고, 등급 묶음을 구조화 출력으로 받는다. 다음 단계가 판정 스크립트를 돌려 평가서를 PR 댓글로 달고, 자동 머지면 merge commit으로 합치고 머리 브랜치를 지우며, 닫기면 PR을 닫는다. review 단계에는 저장소와 PR의 쓰기 권한이 없다 (`plugins/plate/skills/setup/SKILL.md`)
- [x] setup의 설명(description)과 ARCHITECTURE의 디렉터리 구조, 패턴과 규칙, 데이터 흐름이 CI 워크플로를 적는다 (`plugins/plate/skills/setup/SKILL.md`, `docs/ARCHITECTURE.md`)
- [x] ADR-021이 더해진다 (`docs/ADR.md`)

**통과 조건**
- 완료 조건 1, 2, 3이 참이다.
  - 확인: 완료 조건 1, 2, 3의 확인을 모두 돌린다

## 한 일
- setup의 1번이 GitHub 원격과 plate 워크플로가 있는지를 보고, 2번의 승인 표에 "GitHub 원격이 있고 plate 워크플로가 없다 → CI 에이전트를 둘지"가 더해진다: 1번의 판정을 네 가지에서 여섯 가지로 늘려 "GitHub 원격"(`git remote -v`에 URL이 `github.com`인 원격)과 "plate 워크플로"(`.github/workflows/` 아래에 `plate@harness-plate`가 적힌 파일)의 기준을 더했고, 2번의 승인을 다섯에서 여섯으로 늘려 표에 그 행을 더했다. 물을 때 워크플로가 하는 일과 시크릿이 있어야 돈다는 것을 함께 알린다 (`plugins/plate/skills/setup/SKILL.md`)
- 승인하면 setup이 양식 절의 워크플로를 `.github/workflows/` 아래에 쓰고, 4번의 보고에 `CLAUDE_CODE_OAUTH_TOKEN` 시크릿 등록 방법이 들어간다: 3번에 "CI 워크플로" 항목을 "양식 만들기"와 "`AGENTS.md`" 사이에 더했다. 승인받았으면 양식의 `.github/workflows/plate-review.yml`을 그 경로에 쓰고, 편집 훅 때문에 `AGENTS.md`를 고치기 전에 쓰며, 거절했으면 쓰지 않는다. 4번에 `claude setup-token`으로 토큰을 만들어 `gh secret set CLAUDE_CODE_OAUTH_TOKEN`이나 Settings → Secrets and variables → Actions로 넣는 방법과, 커밋해 올린 뒤부터 돈다는 줄을 더했다. 첫머리의 끝난 상태 문장에도 워크플로 파일을 더했다 (`plugins/plate/skills/setup/SKILL.md`)
- 양식 절에 워크플로가 생긴다: 양식 절 끝에 `.github/workflows/plate-review.yml`을 더했다. 트리거는 `pull_request`의 `opened`, `synchronize`, `reopened`다. `review` 잡(`contents: read`, `pull-requests: read`)이 `actions/checkout@v7`(`fetch-depth: 0`) 뒤에 `anthropics/claude-code-action@v1`을 `claude_code_oauth_token`, `github_token: ${{ github.token }}`(Claude 앱의 쓰기 토큰 대신 읽기 권한의 워크플로 토큰), `plugin_marketplaces: https://github.com/werwer748/harness-plate.git`, `plugins: plate@harness-plate`, prompt `/plate:review PR 모드, 기준 브랜치: origin/${{ github.base_ref }}, 평가서 파일: ${{ runner.temp }}/plate-review.md`, `claude_args`(`--add-dir`, `--allowedTools "Bash,Read,Write,Glob,Grep"`, 등급 묶음의 `--json-schema`)로 부르고, `structured_output`을 잡 출력 `bundle`로, 평가서를 아티팩트로 넘긴다. `verdict` 잡(`contents: write`, `pull-requests: write`, `needs: review`)이 `werwer748/harness-plate`를 받아 `python3 harness-plate/plugins/plate/ci/verdict.py`에 등급 묶음을 stdin으로 주고, "판정: {자동 머지 | 머지 요청 | 닫기}" 줄과 평가서를 `gh pr comment`로 달고, `merge`면 `gh pr merge --merge --delete-branch --match-head-commit`, `close`면 `gh pr close`를 한다. 액션의 판은 2026-10-23에 `gh api repos/<액션>/releases/latest`로 본 최신 주판(checkout v7.0.1, upload-artifact v7.0.2, download-artifact v8.0.2)을 썼다. 양식을 먼저 스크래치 파일로 써서 Ruby YAML로 파싱하고, `--json-schema`의 JSON을 파싱하고, `verdict` 잡의 `run`을 가짜 `gh`로 돌려 세 판정과 빈 묶음(실패로 끝남)을 봤다. GitHub에서 돌려 보지는 않았다(task 머리의 범위 밖, `005-publish-verify`). 돌려 봐야 아는 가정: `--add-dir`로 `runner.temp`에 평가서를 쓸 수 있다, `--json-schema`가 `anyOf`를 받는다, Claude 앱 없이 `github_token`만으로 액션이 돈다 (`plugins/plate/skills/setup/SKILL.md`)
- setup의 설명(description)과 ARCHITECTURE의 디렉터리 구조, 패턴과 규칙, 데이터 흐름이 CI 워크플로를 적는다: setup의 description에 CI 워크플로를 묻고 쓰고 시크릿 등록 방법을 적는 일을 더했고, 출처 절에 워크플로 양식이 따른 문서 둘을 더했다. ARCHITECTURE의 디렉터리 구조의 setup 줄에 CI 워크플로 양식을 담는다고 적고, 패턴과 규칙에 PR의 CI 항목(두 잡의 권한, 판정 스크립트, merge commit, `AGENTS.md`보다 먼저 쓰는 까닭, ADR-021)을 더하고, 데이터 흐름의 셋업 줄에 워크플로를 더하고 PR의 CI 흐름을 더했다 (`plugins/plate/skills/setup/SKILL.md`, `docs/ARCHITECTURE.md`)
- ADR-021이 더해진다: "PR의 CI는 review가 평가하고 워크플로가 판정 스크립트로 머지하거나 닫는다"를 task 머리의 결정 셋(평가와 판정의 분리, 토큰 없는 공개 마켓플레이스, merge commit)으로 적었다. 트레이드오프는 harness-plate의 공개, plate의 기본 브랜치를 그때그때 받는 것, PR 코드가 `review` 잡의 Claude 토큰을 읽을 수 있는 것, 사람 확인 없는 머지와 닫기, 워크플로 토큰의 머지가 다른 워크플로를 띄우지 않는 것, 토큰이 구독에 묶이는 것이다 (`docs/ADR.md`)

## 확인 결과
- 완료 조건 1: setup의 승인 표에 "GitHub 원격이 있고 plate 워크플로가 없다 → CI 에이전트를 둘지"가 있고, 승인하면 양식대로 워크플로를 쓰고, 보고에 `CLAUDE_CODE_OAUTH_TOKEN` 시크릿 등록 방법이 있고, 거절하거나 GitHub 원격이 없으면 쓰지 않는다
  - `plugins/plate/skills/setup/SKILL.md`의 1번, 2번, 3번, 4번, 양식 절을 읽고 `grep -n`으로 줄을 봤다 → 24줄 "여섯 가지를 판정", 48줄 "GitHub 원격" 기준, 50줄 "plate 워크플로" 기준, 63줄 승인 표의 행 `| GitHub 원격이 있고 plate 워크플로가 없다 | CI 에이전트를 둘지. …`, 84줄 3번의 "CI 워크플로"(승인받았으면 양식을 그 경로에 쓰고, 거절했으면 쓰지 않는다), 109줄 4번의 `claude setup-token`과 `CLAUDE_CODE_OAUTH_TOKEN` 등록 방법, 294줄 양식 절의 `.github/workflows/plate-review.yml`. GitHub 원격이 없으면 표의 조건이 맞지 않아 묻지 않고, 3번은 승인받았을 때만 쓴다. 통과
- 완료 조건 2: 워크플로 양식의 트리거, 마켓플레이스와 플러그인 줄, prompt, `--json-schema`, 판정 단계, 단계마다의 permissions
  - 양식 절의 YAML 블록을 파이썬으로 뽑아(`extracted.yml`) 검증해 둔 스크래치 파일과 `cmp`로 견주고 → 같다. `ruby -ryaml`로 파싱해 → 트리거 `{"pull_request":{"types":["opened","synchronize","reopened"]}}`, `plugin_marketplaces: https://github.com/werwer748/harness-plate.git`, `plugins: plate@harness-plate`, prompt `/plate:review PR 모드, 기준 브랜치: origin/${{ github.base_ref }}, 평가서 파일: ${{ runner.temp }}/plate-review.md`, `review` 잡 출력 `bundle: ${{ steps.review.outputs.structured_output }}`, `review` 권한 `{"contents":"read","pull-requests":"read"}`, `verdict` 권한 `{"contents":"write","pull-requests":"write"}`와 `needs=review`, `verdict`의 run에 `gh pr comment`, `gh pr merge --merge --delete-branch`, `gh pr close`. `--json-schema`의 JSON을 `shlex`와 `json`으로 파싱해 → 일곱 키가 모두 required이고 `additionalProperties: false`다. `review` 잡에는 쓰기 권한이 없다. 통과
  - 양식이 부르는 판정 스크립트의 경로와 입력의 꼴을 `001-ci-review`가 만든 판정 스크립트와 견줬다 → `docs/ARCHITECTURE.md` 디렉터리 구조의 `plugins/plate/ci/verdict.py`(16~17줄)와 양식의 `harness-plate/plugins/plate/ci/verdict.py`(harness-plate를 `path: harness-plate`로 받은 자리)가 같은 파일이고, 입력은 둘 다 stdin의 등급 묶음 JSON 하나다. `--json-schema`의 키와 값을 `verdict.py` 4~9줄의 docstring(build·lint·test: pass, fail, none, unmeasured / coverage: 수, skipped, unmeasured / 세 등급: A~E, unjudged)에 대어 파이썬 assert로 견줘 → "schema keys and values match". `verdict` 잡의 `run`을 가짜 `gh`와 실제 `verdict.py`로 돌려 → 자동 머지 묶음은 `gh pr comment 7 --body-file comment.md` 뒤 `gh pr merge 7 --merge --delete-branch --match-head-commit abc`, coverage `unmeasured`는 댓글만, 보안 C와 빌드 fail은 댓글 뒤 `gh pr close 7`. 통과
- 완료 조건 3: `docs/ARCHITECTURE.md`가 setup이 CI 워크플로를 쓰는 것과 PR의 CI 흐름을 적고, `docs/ADR.md`에 ADR-021이 있다
  - `docs/ARCHITECTURE.md`를 읽었다 → 디렉터리 구조 22줄 setup이 CI 워크플로 양식을 담는다, 패턴과 규칙 48줄 PR의 CI 항목, 데이터 흐름 52줄 셋업이 승인하면 `.github/workflows/plate-review.yml`을 쓴다, 67~71줄 PR → review 잡 → verdict 잡의 흐름. `docs/ADR.md` 33~36줄에 ADR-021(결정, 이유, 트레이드오프)이 있다. 통과

## 계획과 달라진 점
- 계획은 "PR이 열리거나 갱신될 때 돈다"였고, 트리거에 `reopened`도 넣었다. 까닭: CI가 닫은 PR을 고쳐 다시 열면 평가가 돌지 않는다.
- 계획에 없던 것 셋을 워크플로에 더했다. PR마다 `concurrency`의 `cancel-in-progress`(새 커밋이 오면 옛 평가가 판정하지 않게 한다), `gh pr merge`의 `--match-head-commit`(평가하지 않은 커밋을 합치지 않게 한다), 댓글 첫 줄의 "판정: …"(사용자가 PR이 왜 합쳐지거나 닫혔는지 댓글에서 본다)이다.
- 계획의 "다음 단계"는 같은 잡의 다음 스텝이 아니라 다른 잡(`verdict`)으로 했다. 까닭: GitHub Actions의 permissions는 잡마다 정해져서, 같은 잡이면 review에도 쓰기 권한이 간다. 평가서는 아티팩트로, 등급 묶음은 잡 출력으로 넘긴다.

## 남은 것
- 없음

## 하네스에서 걸린 것
- 편집 훅(`plugins/plate/hooks/edit_guard.py`)과 setup이 부딪힌다. 처음 셋업하는 프로젝트는 워크플로를 `AGENTS.md`보다 먼저 써서 피했다. 그러나 `AGENTS.md`에 문서 지도 구간이 이미 있는 프로젝트에서 setup을 다시 불러 CI 에이전트를 승인하면, 남은 phase가 없는 한 훅이 `.github/workflows/plate-review.yml`의 편집을 막고 "계획부터 세운다"고 알린다. 이 phase의 TODO는 setup 본문과 문서만 고치므로 훅은 손대지 않았다. 원하는 해결책: 훅이 setup이 쓰는 이 한 경로를 통과시키거나, 다시 부르는 setup의 길을 따로 정한다. 회고에서 논의할 거리다.
- 수행 스킬의 "다른 phase의 파일은 읽지 않는다"를 한 번 어겼다. ADR-021의 앞선 언급을 찾으려고 저장소 전체를 `grep`했더니 `005-publish-verify/phase-2.md`, `phase-3.md`, `001-ci-review/done-phase-2.md`의 줄이 결과에 섞여 나왔다. 그 내용은 이 phase의 일에 쓰지 않았다.
