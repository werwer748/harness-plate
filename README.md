# harness-plate

레일 하네스 `plate`의 플러그인 레포다. 지금은 스킬이 열 있다.

| 스킬 | 하는 일 |
|---|---|
| `setup` | 프로젝트에 하네스 문서의 위치 기준을 세운다. GitHub 원격이 있고 plate 워크플로가 없으면 CI 워크플로를 둘지 묻고, 그 밖에는 묻지 않는다. CI를 두면 `.github/CODEOWNERS`가 없을 때 그것을 쓰고(이미 있거나 GitHub login을 얻지 못하면 넣을 줄을 알린다), 기본 브랜치에 ruleset 거는 법을 보고에 알린다. 설치만 하고 끝난다 |
| `context` | 셋업이 만든 문서의 남은 칸을 저장소 스캔과 질문으로 채운다 |
| `plan` | 요청 하나를 tasks로 계획해 `docs/tasks/`에 tasks 머리 `plan.md`와, task 폴더 `NNN-slug/`마다 task 머리 `plan.md`와 phase마다의 `phase-N.md`로 쓰고 한 커밋으로 넣는다 |
| `run` | 계획된 tasks를 phase 하나씩 실행한다. 시작할 때 실행 방식(task 하나씩, tasks 일괄)을 묻고, 수행, 확인, 회고, 평가를 저마다 새 에이전트에게 맡기고, tasks 끝에서 보고하고 고칠지 묻고, 기본 브랜치로 가는 PR을 열지(GitHub 원격이 없으면 합칠지) 묻는다 |
| `phase` | 계획의 phase 하나를 수행하고 한 일의 기록을 `phase-N.md`에 덧붙인다. `run`이 띄운 에이전트가 부른다 |
| `check` | 수행이 끝난 phase 하나의 통과 조건과 빌드·린트·테스트를 돌려 `phase-N.md`에 확인 절을 더한다. `run`이 띄운 에이전트가 부른다 |
| `retro` | phase가 모두 통과한 task 하나를 회고해 task 폴더의 `retro.md`와 `docs/tasks/FRICTION.md`에 적는다. `run`이 띄운 에이전트가 부른다 |
| `review` | 모든 task가 끝난 tasks에서 바뀐 코드를 다섯 범주로 A~E로 평가해 `docs/tasks/review.md`에 적는다. `run`이 띄운 에이전트가 부르고, CI 워크플로가 PR마다 PR 모드로 부른다 |
| `eval` | 모든 task가 끝난 tasks에서 하네스가 어떻게 돌았는지 여섯 기준으로 A~E로 평가해 `docs/tasks/eval.md`에 적는다. `run`이 띄운 에이전트가 부른다 |
| `cleanup` | 저장소를 여섯 기준(보안, 성능, 신뢰성, 유지보수성, 기능 적합성, 기존 작업 정합성)마다 새 에이전트가 따로 살피고 서로의 발견을 교차 검토해 `docs/cleanup/YYYY-MM-DD.md`에 보고서를 쓰고, 발견을 tasks로 만들지 묻는다. 동의하면 고른 발견을 `plan`에 넘긴다. 코드를 고치지 않는다. 사용자가 부른다 |

## tasks 끝의 PR

`run`은 tasks 끝에서 `docs/tasks/`를 비운 뒤 origin이 GitHub이면 `tasks/<이름>` 브랜치를 푸시해 기본 브랜치로 가는 PR을 열지 묻는다. PR 본문에는 tasks의 요청과 목표, 전체 보고(코드 평가와 하네스 eval의 등급)를 넣는다. plate 워크플로가 없으면 `docs/tasks/review.md`의 마지막 평가 절을 PR 댓글로 달고 사람이 머지한다. `run`은 PR을 머지하거나 닫지 않는다. origin이 없거나 GitHub의 것이 아니면 기본 브랜치로 합칠지 묻는다.

## CI 워크플로

`setup`이 승인받아 쓰는 `.github/workflows/plate-review.yml`은 PR이 열리거나 갱신될 때 돈다. `review` 잡이 읽기 권한만으로 이 공개 저장소에서 plate를 받아 `review`의 PR 모드로 평가하고, `verdict` 잡이 그 등급 묶음을 판정 스크립트(`plugins/plate/ci/verdict.py`)에 넘겨 평가서를 PR 댓글로 단 뒤 판정대로 한다.

PR이 바꾼 지시가 등급을 바꾸지 못하게, `review` 잡은 평가를 부르기 전에 `AGENTS.md`를 기준 브랜치의 것으로 되돌리고(기준 브랜치에 없으면 PR의 것을 지운다), `review`의 PR 모드는 지침 파일을 기준 브랜치에서 읽고 PR이 바꾼 파일의 글을 평가할 데이터로만 본다. 평가 단계가 실패하면 다음 단계가 실행 결과에서 오류 줄(`is_error`와 오류 글)만 로그에 낸다. Claude의 메시지 전부를 로그에 내는 입력은 켜지 않는다. `docs/ARCHITECTURE.md`에 `## 결과물인 마크다운` 절이 있으면 `review`는 거기 적힌 경로의 `.md`(이 레포에서는 스킬 본문)를 코드처럼 평가하되 그 줄을 커버리지와 중복에서 빼고, PR 모드는 이 절도 기준 브랜치에서 읽는다. 결과물인 마크다운의 줄을 뺀 새 줄이 20줄 미만인 PR은 커버리지를 재든 못 재든 "보지 않음"이다.

| 판정 | 조건 | 하는 일 |
|---|---|---|
| 자동 머지 | 빌드·린트·테스트가 모두 통과(없음도 든다), 새 줄 커버리지 80% 이상(보지 않음도 든다), 신뢰성·보안·유지보수성 A, 모름(측정 못함, 판단 못함) 없음, PR이 워크플로(`.github/workflows/`로 시작하는 경로)를 바꾸지 않음 | merge commit으로 합치고 머리 브랜치를 지운다 |
| 닫기 | 빌드·린트·테스트 가운데 실패가 있거나 보안이 C 이하 | PR을 닫는다 |
| 머지 요청 | 그 밖 | 사람이 머지하도록 둔다 |

워크플로를 바꿨는지는 `verdict` 잡이 PR의 바뀐 파일 목록(파일 목록 API `gh api --paginate repos/$GH_REPO/pulls/$PR/files`. 받지 못하면 워크플로를 바꾼 것으로 본다)을 판정 스크립트에 `--changed-files`로 넘겨 본다. 워크플로를 바꾼 PR은 다른 조건을 다 채워도 머지 요청이 되고 사람이 머지한다.

워크플로는 저장소 시크릿 `CLAUDE_CODE_OAUTH_TOKEN`이 있어야 돈다. `claude setup-token`으로 토큰을 만들어 `gh secret set CLAUDE_CODE_OAUTH_TOKEN`으로 넣는다.

### ruleset과 CODEOWNERS

같은 저장소의 PR은 PR 쪽의 워크플로 파일로 돌기 때문에, PR이 워크플로를 고치면 판정 스크립트의 검사도 건너뛸 수 있다. 이 길은 저장소 설정이 막는다. PR은 저장소 설정을 바꾸지 못한다. `.github/CODEOWNERS`에 워크플로와 CODEOWNERS 자신의 코드 소유자를 두고, 기본 브랜치에 코드 소유자 리뷰를 요구하는 ruleset을 건다.

- 막는 것: 코드 소유자가 아닌 계정(예: github-actions)이 연 워크플로 PR을 워크플로 토큰이 머지하는 것, 워크플로 토큰이 기본 브랜치에 직접 푸시하는 것.
- 막지 못하는 것: PR을 연 계정이 유일한 코드 소유자면 GitHub가 코드 소유자 리뷰를 채운 것으로 본다. 그래서 혼자 쓰는 저장소에서 내가 연 워크플로 PR은 그 PR 안의 워크플로가 스스로 머지할 수 있다. 이 길까지 닫으려면 코드 소유자를 PR을 여는 계정과 다른, 쓰기 권한이 있는 계정으로 둔다. 쓰기 권한이 없는 계정은 GitHub가 코드 소유자로 보지 않는다.
- ruleset을 걸기 전에는 판정 스크립트의 검사만 남는다. 비공개 저장소는 요금제에 따라 ruleset을 걸 수 없다. 걸고 나면 워크플로를 바꾼 PR은 코드 소유자가 승인하거나 관리자가 우회(`gh pr merge --admin`)해 머지한다.

ruleset은 `setup`이 보고에 적는 것과 같은 꼴로, 관리자 권한이 있는 계정이 저장소 폴더에서 건다. `{owner}`와 `{repo}`는 `gh`가 지금 저장소로 바꾼다.

```sh
gh api -X POST 'repos/{owner}/{repo}/rulesets' --input - <<'JSON'
{
  "name": "plate-workflow-guard",
  "target": "branch",
  "enforcement": "active",
  "conditions": {"ref_name": {"include": ["~DEFAULT_BRANCH"], "exclude": []}},
  "rules": [
    {"type": "pull_request", "parameters": {
      "required_approving_review_count": 0,
      "require_code_owner_review": true,
      "dismiss_stale_reviews_on_push": false,
      "require_last_push_approval": false,
      "required_review_thread_resolution": false}}
  ],
  "bypass_actors": [{"actor_id": 5, "actor_type": "RepositoryRole", "bypass_mode": "pull_request"}]
}
JSON
```

화면에서 걸려면 Settings → Rules → Rulesets에서 기본 브랜치를 대상으로 PR 필수, 승인 수 0, 코드 소유자 리뷰 필수를 켜고, 우회 목록에 Repository admin을 PR로만(pull request) 둔다.

### 이미 CI 워크플로를 둔 프로젝트

0.14.0 전에 `setup`으로 `plate-review.yml`을 둔 프로젝트는 `setup`이 워크플로 파일을 다시 쓰지 않으므로 세 가지를 손으로 한다.

1. CODEOWNERS 두 줄 넣기: `.github/CODEOWNERS`에 아래 두 줄을 넣는다. `<login>`은 코드 소유자로 둘 GitHub 계정이다.
   ```
   /.github/workflows/ @<login>
   /.github/CODEOWNERS @<login>
   ```
2. ruleset 걸기: 위 "ruleset과 CODEOWNERS"의 명령이나 화면으로 기본 브랜치에 건다.
3. verdict 단계에 `--changed-files` 넘기기: `.github/workflows/plate-review.yml`의 `verdict` 잡에서 판정 스크립트를 부르는 줄 앞에 바뀐 파일 목록을 받고, 그 파일을 `--changed-files`로 넘긴다.
   ```sh
   if ! gh api --paginate "repos/$GH_REPO/pulls/$PR/files" --jq '.[].filename' > changed-files.txt; then
     echo '.github/workflows/' > changed-files.txt
   fi
   verdict=$(printf '%s' "$BUNDLE" | python3 harness-plate/plugins/plate/ci/verdict.py --changed-files changed-files.txt)
   ```
   이 변경을 PR로 올리면 그 PR은 판정 검사가 없는 옛 줄이 아니라 PR 쪽의 새 워크플로로 돌아, 워크플로를 바꾼 PR이라 머지 요청이 된다.

## 훅

Claude Code에서는 훅 둘이 함께 돈다. 편집 훅(`edit_guard.py`)은 계획 없는 코드 편집과, 테스트 먼저인 phase에서 테스트보다 앞선 구현 편집을 막는다. `setup`이 아직 없는 `.github/workflows/plate-review.yml`과 `.github/CODEOWNERS`를 쓰는 것은 막지 않고, 이미 있는 두 파일의 편집은 다른 코드 파일처럼 막는다. 푸시 훅(`push_guard.py`)은 셋업된 프로젝트에서 에이전트가 Bash로 origin의 기본 브랜치에 푸시하는 것을 막는다. 다른 브랜치로의 푸시와 사람의 푸시는 막지 않는다. 다른 도구에서는 훅이 돌지 않고 `AGENTS.md`의 작업 규칙과 스킬의 규칙이 막는다.

## 설치

이 레포는 공개 저장소(`werwer748/harness-plate`)다. `<폴더>`는 이 레포를 받은 폴더의 경로다.

### Claude Code

공개 저장소에서 받는다.

```bash
claude plugin marketplace add werwer748/harness-plate
claude plugin install plate@harness-plate
```

받아 둔 폴더에서 설치하려면 첫 줄을 `claude plugin marketplace add <폴더>`로 바꾼다. 설치하지 않고 한 세션에서만 쓰려면 `claude --plugin-dir <폴더>/plugins/plate`로 시작한다. 스킬은 `/plate:setup`, `/plate:context`, `/plate:plan`, `/plate:run`, `/plate:phase`, `/plate:check`, `/plate:retro`, `/plate:review`, `/plate:eval`, `/plate:cleanup`으로 부른다.

### Codex

```bash
codex plugin marketplace add <폴더>
codex plugin add plate@harness-plate
```

스킬은 `$plate:setup`, `$plate:context`, `$plate:plan`, `$plate:run`, `$plate:phase`, `$plate:check`, `$plate:retro`, `$plate:review`, `$plate:eval`, `$plate:cleanup`으로 부른다. Codex는 설치할 때 플러그인을 복사해 두므로, 스킬이 바뀌면 `codex plugin add plate@harness-plate`를 다시 실행한다.

Codex에서의 확인은 2026-10-08에 멈춘 상태다. 그 뒤에 고친 스킬과 새로 더한 `plan`, `run`, `phase`, `check`, `retro`, `review`, `eval`, `cleanup` 스킬은 Codex에서 확인하지 않았고, 확인해 둔 것과 남은 것은 `docs/TOOLS.md`에 있다.
