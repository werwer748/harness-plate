# 도구별로 확인해 둔 사실

레일을 돌리는 도구(Claude Code, Codex, Grok Build)마다 확인해 둔 사실과 확인을 멈춘 지점만 적는다. 사실마다 확인한 버전이나 날짜를 적었고, 그 뒤로 바뀌었을 수 있다. 시험 실행 기록(차림, 출력, 본문 해시, 임시 경로)은 적지 않는다. 그것은 그 시험을 돌린 phase의 기록에 있다.

## 지금 상태

| 도구 | 상태 |
|---|---|
| Claude Code | 완성 판정을 이 도구로 한다. 2.1.291(2026-10-06)부터 2.1.311(2026-10-28)까지 돌렸다 |
| Codex | 0.160.0에서 2026-10-08에 확인을 멈췄다. 남은 것은 아래 "Codex에서 확인을 멈춘 지점"에 있다 |
| Grok Build | 이 Mac에 설치돼 있지 않다. 판정을 돌린 적이 없다 |

Codex → Grok Build 순으로 넓히는 일은 v1.0 뒤에 한다(ADR-018).

## Claude Code

- `claude --plugin-dir <플러그인 폴더>`는 그 폴더의 플러그인을 그 세션에만 불러온다. init 줄에는 `plate@inline`으로 나온다.
- 스킬은 `/plate:<이름>`으로 부르고 헤드리스(`claude -p`)에서도 불린다. 스킬이 다른 스킬을 이름으로 불렀다가 돌아와 자기 절차를 잇는다(2.1.291~2.1.294).
- `CLAUDE.md`가 없을 때만 `AGENTS.md`를 읽는다. 그래서 `CLAUDE.md`에 `@AGENTS.md` 임포트를 둔다.
- 헤드리스에서 물음의 답을 미리 주면 묻지 않는다. 묻는 글을 봐야 하면 답을 빼고 부르고 `claude -p "<답>" --resume <session_id>`로 잇는다. 세션은 폴더에 묶인다(2.1.291~2.1.296).
- `--allowedTools`는 값을 여럿 받아 뒤에 둔 프롬프트를 삼킨다("Input must be provided either through stdin or as a prompt argument"). 프롬프트는 `-p` 바로 뒤에 둔다(2.1.311).
- `--permission-mode acceptEdits`만 주면 파일 쓰기는 되고 `git add`, `git commit`은 막힌다. 막힌 명령 하나마다 약 65초를 기다린다(2.1.296).
- 허용 목록에 든 명령도 꼴에 따라 막힌다. `git -C <경로> …`는 `Bash(git <하위 명령>:*)`에 맞지 않는다. `cd <폴더> && git …`, `sed -n`, `awk`, 프로젝트 밖으로 돌린 출력(`> /tmp/x`)도 승인을 요구한다(2.1.296~2.1.311).
- `&&`, `;`, 파이프, `for`, 명령 치환으로 이은 명령은 하나만 승인이 필요해도 전체가 막히고 허용 목록으로 풀리지 않는다. 한 명령씩 부르면 돈다. 명령 치환은 `$(cat <<'EOF' … EOF)` 꼴만 지나갔다(2.1.302~2.1.311).
- 에이전트는 프로젝트 폴더 밖의 파일을 읽거나 쓰지 못한다(플러그인의 `SKILL.md`를 경로로 여는 것도). 다른 스킬의 본문은 이름으로 불러야 받는다. WebFetch는 헤드리스에서 막힌다(2.1.296~2.1.300).
- stream-json의 init 줄(스킬 목록, `permissionMode`)은 훅 줄들 뒤에 나온다. acceptEdits의 헤드리스 세션은 스킬에게 지금 모드를 알려 주지 않는다(2.1.300~2.1.311).
- 세션 기록은 `${CLAUDE_CONFIG_DIR:-~/.claude}/projects/<작업 폴더 경로의 /와 .을 -로 바꾼 이름>/<세션 id>.jsonl`이다(2.1.311).
- 한글 본문을 `python3 -` heredoc으로 고치면 `SyntaxError: Non-UTF-8 code`로 깨질 수 있다. Edit 도구나 `python3 -c`, 파일로 쓴 스크립트를 쓴다. 늘 깨지지는 않아 같은 꼴이 돈 때도 있다(2.1.312).
- `git clone <원본>`은 원본의 지금 브랜치를 `origin/HEAD`로 둔다. 복제본에서 기본 브랜치를 보는 스킬을 돌리려면 `git remote set-head origin main`을 한다(2026-10-27).

**서브에이전트, 권한, worktree** (2.1.296~2.1.302)

- 서브에이전트가 플러그인 스킬을 이름으로 부른다. "probe의 work 스킬(`probe:work`)을 불러 그 절차를 따른다"와 번호만 넘겨도 따랐다.
- 서브에이전트에게 `CLAUDE.md`와 그 `@` 임포트, `--allowedTools`가 이어진다.
- 허용 목록 없이는 `test -f`, `grep -q`, `ls`와 그것들을 `&&`로 이은 것만 되고 `python3 -m unittest`, `python3 -c`는 막힌다.
- `"Bash(git worktree:*)" "Bash(git merge:*)" "Bash(git branch:*)" "Bash(git rm:*)"`를 더하면 worktree를 만들고 지우고 합친다. 원래 자리의 세션은 worktree 안의 `git status`를 돌리지 못한다. `.git/info/exclude`는 쓰지 못한다.
- 에이전트의 사용량은 결과와 함께 돌아온다. `tool_result` 끝에 `<usage>subagent_tokens: …\ntool_uses: …\nduration_ms: …</usage>`가 붙는다(2.1.302).

**훅** (2.1.302~2.1.310)

- `--plugin-dir`로 실은 플러그인의 `hooks/hooks.json`이 돈다. `${CLAUDE_PLUGIN_ROOT}`는 `--plugin-dir`에 준 폴더다. 서브에이전트의 호출에도 돈다.
- 종료 코드 2만 막고, 다른 0이 아닌 코드는 막지 않는 오류다(`"onFailure": "block"`이 없을 때). `python3`는 스크립트 파일이 없으면 2로 끝나므로 훅 명령은 스크립트가 없으면 0으로 끝낸다. 셸 꼴은 macOS·Linux에서 `sh -c`, Windows에서 Git Bash나 PowerShell로 돈다(code.claude.com/docs/en/hooks, 2026-10-17).
- 막힌 호출은 `tool_result`(`is_error: true`, `PreToolUse:<도구> hook error: …`)와 `result` 줄의 `permission_denials`에 남는다. 권한에 막힌 것과는 `tool_result_meta`의 `permission_decision.source`가 `hook`인지로 가른다. 통과시킨 호출은 기록에 훅 줄이 없다.
- 훅이 허용 목록보다 앞선다. `"Bash(git push:*)"`를 줘도 푸시 훅이 막았다(2.1.310).

**세션 도중의 스킬 본문 고침** (2.1.302, 2026-10-17)

- 세션에 실린 스킬 본문은 세션을 띄울 때의 것이다. 디스크에서 고친 뒤 같은 세션에서 띄운 에이전트는 고치기 전의 본문을 받았고, `/reload-plugins` 뒤에 띄운 에이전트는 고친 본문을 받았다. `-p` 세션에서도 `/reload-plugins`가 돈다(v2.1.260 이상). 이 레포의 run에서도 그랬다(2026-10-23~24).
- 그래서 run은 tasks 커밋이 맡길 스킬의 `SKILL.md`를 바꿨으면 맡기는 글 끝에 작업 트리의 스킬 줄(`작업 트리의 {경로}를 읽어 그 절차를 따른다. …`)을 붙인다. 경로가 저장소 안이라 밖을 읽지 못하는 제약에 걸리지 않는다. 그 줄이 닿지 않는 곳(run 자신, 사용자가 부르는 스킬)은 새 세션이나 `/reload-plugins`로 싣는다.
- 확인하지 않은 것: 그 세션에서 한 번도 부르지 않은 스킬도 고치기 전의 본문을 주는지.
- 그래서 한 phase 안에서도 수행과 확인이 다른 판의 본문으로 돌 수 있다. run은 맡길 때마다 tasks 커밋이 그 스킬의 `SKILL.md`를 바꿨는지 다시 보므로, phase가 phase·check 본문을 고치면 그 phase의 수행은 작업 트리의 스킬 줄 없이 이름으로 불린 세션의 옛 판으로, 뒤이은 확인은 작업 트리의 스킬 줄이 가리키는 고친 판으로 돈다(check-commands, 2026-10-28). 그래서 이 저장소의 작업 규칙은 수행과 확인이 run이 넘긴 판을 따르게 하고, 고친 본문의 동작은 그 판으로 돈 수행이나 확인이 아니라 헤드리스 시험(작업 트리의 `--plugin-dir`)으로 보게 한다.
- 헤드리스 시험의 완료 조건을 본문 해시로 볼 때, 그 본문을 뒤에서 고치는 phase(회고 뒤 더한 phase도)는 시험을 다시 돌려 새 해시를 기록에 남긴다. 계획은 이것을 그 완료 조건 곁에 적는다. 적지 않으면 회고의 고침이 해시를 바꿔 조건을 다시 참으로 둘 길이 없어 run이 멈춘다(issue-criteria, 2026-10-29).

**플러그인 폴더의 편집과 권한 모드** (2.1.296~2.1.310, 2026-10-13~26)

- `--plugin-dir`로 실은 폴더는 보호 경로다. 그 안의 쓰기는 `permissions.allow`로 미리 허락할 수 없고, 묻지 않고 지나가는 모드는 bypassPermissions뿐이다. 수동 모드와 acceptEdits에서는 묻는다(code.claude.com/docs/en/permission-modes의 "Protected paths").
- auto mode에서는 그 안의 편집이 "The server-side auto mode classifier gave no verdict (it skipped this action)"로 거부된다. 메인과 띄운 에이전트 모두 그렇고, `Edit(plugins/plate/skills/**)` 허용으로도 풀리지 않았다. 띄운 에이전트는 자기 모드를 바꾸지 못한다.
- 세션을 bypassPermissions(Shift+Tab)나 묻는 모드로 바꾼 뒤 띄운 에이전트의 편집은 지나갔다. 세션을 새로 열 필요는 없다. 세션을 연 `--permission-mode`는 지금 모드를 말해 주지 않는다.
- 그래서 이 저장소에서 스킬 본문(`plugins/plate/**`)을 고치는 tasks는 run 전에 bypassPermissions로 바꾸거나 묻는 모드로 두고 편집마다 승인한다.

**셸의 `=` 확장** (zsh, 2026-10-28)

- 이 Mac의 셸은 zsh라 Bash 도구의 명령도 zsh로 돈다. zsh는 `=`로 시작하는 낱말을 명령 경로로 확장해(`=ls`는 `/bin/ls`), `echo ====` 같은 구분 줄이 `zsh:1: === not found`로 그 명령을 깬다(check-commands의 phase 수행과 하네스 eval).
- 구분 줄은 `echo '----'`처럼 따옴표로 감싸거나 `=`로 시작하지 않게 쓴다.

**스킬을 헤드리스로 돌려 볼 때의 허용 목록** (2.1.311, 2026-10-27)

- `"Bash(git add:*)" "Bash(git commit:*)" "Bash(git log:*)" "Bash(git diff:*)" "Bash(git show:*)" "Bash(git status:*)" "Bash(git ls-files:*)" "Bash(git rev-parse:*)" "Bash(git -C:*)" "Bash(git remote:*)" "Bash(git rm:*)" "Bash(git merge-base:*)" "Bash(git symbolic-ref:*)" "Bash(git switch:*)" "Bash(git branch:*)" "Bash(gh issue list:*)" "Bash(gh auth status:*)" "Bash(python3:*)" "Bash(wc:*)" "Bash(grep:*)" "Bash(cut:*)" "Bash(claude plugin validate:*)"`. 이슈 본문까지 읽게 하려면 `"Bash(gh issue view:*)"`를 더한다.
- 이은 Bash는 이 목록으로도 풀리지 않는다. 막힘 없이 돌리려면 `--permission-mode bypassPermissions`로 돌린다.

**GitHub와 claude-code-action** (gh 2.89.0~2.103.0, claude-code-action v1, 2026-10-18~27)

- `gh issue list --search`에 낱말을 여럿 주면 있는 이슈를 찾지 못했다. 지운 이슈의 번호는 다시 쓰이지 않는다. 워크플로를 바꾸는 푸시는 `gh auth` 토큰 범위에 `workflow`가 있어야 한다.
- 액션의 `claude_args`의 `--plugin-dir`는 CLI로 넘어간다. `pull_request`에서 액션은 `CLAUDE.md`, `.claude` 들을 기준 브랜치의 것으로 되돌리지만 `AGENTS.md`는 되돌리지 않는다.
- 액션은 `show_full_output` 없이는 결과 글을 로그에 내지 않는다. 실패 까닭은 `execution_file`의 JSON에서 `"type": "result"`인 메시지의 `is_error`, `api_error_status`, `result`로 읽는다. 인증 실패에서도 `subtype`은 `success`다.
- github-actions가 연 PR에서는 `pull_request` 워크플로가 잡 0개로 `failure`였다.

**ruleset과 CODEOWNERS로 워크플로 PR의 자동 머지를 막는지 본 것** (gh 2.103.0, 2026-10-27. 개인 계정 소유의 시험 저장소)

- ruleset은 `gh api -X POST repos/<owner>/<repo>/rulesets --input -`에 아래 JSON을 넣어 건다(기본 브랜치, PR 필수, 승인 수 0, 코드 소유자 리뷰 필수, 저장소 관리자는 PR로만 우회). CODEOWNERS는 `/.github/workflows/ @<login>`, `/.github/CODEOWNERS @<login>` 두 줄이다.

```json
{"name": "workflow-guard", "target": "branch", "enforcement": "active",
 "conditions": {"ref_name": {"include": ["~DEFAULT_BRANCH"], "exclude": []}},
 "rules": [{"type": "pull_request", "parameters": {
   "required_approving_review_count": 0, "require_code_owner_review": true,
   "dismiss_stale_reviews_on_push": false, "require_last_push_approval": false,
   "required_review_thread_resolution": false}}],
 "bypass_actors": [{"actor_id": 5, "actor_type": "RepositoryRole", "bypass_mode": "pull_request"}]}
```

- 막은 것: 코드 소유자가 아닌 github-actions가 연 워크플로 PR의 토큰 머지(`the base branch policy prohibits the merge.`)와 워크플로 토큰의 기본 브랜치 직접 푸시(`GH013 … Changes must be made through a pull request.`).
- 막지 못한 것: PR을 연 계정이 유일한 코드 소유자면 코드 소유자 리뷰 필수가 승인 없이 채워진 것으로 매겨져, 그 PR은 워크플로 토큰으로도, PR 안의 워크플로가 스스로도 머지한다. 관리자는 `gh pr merge --admin`으로 우회한다.
- 다른 설정: 승인 수 1은 저장소가 Actions의 PR 승인을 허용하면 막지 못한다. `file_path_restriction`은 push ruleset이면 개인 계정 저장소에 걸 수 없고(422 "Source only org-owned repos can have push rules"), branch ruleset에는 넣을 수 없다(422). 쓰기 권한 없는 코드 소유자는 `Unknown owner`로 무시된다.
- 확인하지 않은 것: `gh pr diff`가 실패할 만큼 큰 PR, 파일이 3000개를 넘어 PR 파일 목록 API가 잘리는 PR.

## Codex

0.160.0에서 확인했다(2026-10-06).

- 설치는 `codex plugin marketplace add <폴더>` 뒤 `codex plugin add plate@harness-plate`다. 한 세션에만 불러오는 옵션은 없다. 설치본은 `~/.codex/plugins/cache/harness-plate/plate/<버전>/`의 사본이라 스킬을 고치면 다시 설치한다.
- `.codex-plugin/plugin.json`은 `name`, `version`, `description`, `author`, `repository`, `"skills": "./skills/"`만으로 설치된다. `.agents/plugins/marketplace.json`은 `name`, `interface.displayName`, `plugins[]`(항목마다 `name`, `source`, `policy`, `category`)를 둔다. 공식 문서는 루트의 `plugin.json`을 권하고 `.codex-plugin/`은 호환용이라고 적는다.
- 스킬은 `$plate:setup`처럼 부른다. `AGENTS.md`를 자동으로 읽는다. 세션 시작 때 스킬의 이름, 설명, 경로만 싣고(컨텍스트의 2%까지), 본문은 부르거나 모델이 필요할 때 연다. 경로에 버전이 들어 있어 본문에서 다른 스킬은 이름으로 가리킨다.
- `read-only`에서는 `git rev-parse`가 실패하고, `workspace-write`는 `.git` 쓰기를 막는다. 판정은 미리 `git init`한 폴더에서 `codex exec --sandbox workspace-write "<요청>"`로 돌린다. `--json` 첫 줄의 `thread_id`로 `codex exec resume <thread_id>`를 하면 잇는다.

## Grok Build

1.0.46 기준이고 이 Mac에 설치돼 있지 않다(2026-10-06). Claude 형식 플러그인을 그대로 읽고, `AGENTS.md`를 자동으로 읽고, 종료 차단 훅이 없다고 적혀 있으나 어떻게 확인했는지는 기록이 없다.

## 두 도구에서 같은 결과를 확인한 것

2026-10-06에 같은 답을 주고 헤드리스로 돌렸다. 셋업은 두 도구의 결과 폴더가 바이트 단위로 같았다. 맥락 채우기는 구조와 `{확인 필요}` 칸이 같았고, 다시 부르면 남은 칸만 바뀌었다.

## Codex에서 확인을 멈춘 지점

- 끊긴 판정 넷(Claude Code에서는 통과): 스캔한 사실의 출처 경로와 ADR 후보 범주, `docs/DESIGN.md`의 토큰이 CSS의 이름과 값 그대로인지, 이미 채운 문서는 두고 `docs/DESIGN.md`만 채우는지, 여러 턴에서 질문이 하나씩 나오고 승인 전에는 파일이 바뀌지 않는지.
- 2026-10-08에 고친 본문 셋: 맥락 채우기의 "기술 스택" 절(빌드 매니페스트에서만 적는다), DESIGN 앞머리 출처 주석, 셋업의 새 `AGENTS.md` 첫 줄(Codex만 빈 줄을 두던 곳).

## 도구를 넓힐 때 할 것

v1.0 뒤에 한다(ADR-018).

- Codex에서 끊긴 판정 넷과 고친 본문 셋을 확인한다.
- Codex에서 plan을 돌린다. plan은 커밋을 하는데 `workspace-write`는 `.git` 쓰기를 막으므로 샌드박스부터 확인한다.
- Codex에서 run과 그것이 맡기는 스킬, cleanup을 돌린다. 서브에이전트를 띄우는 방법과 서브에이전트가 스킬을 부르는 방법부터 확인한다.
- 두 도구의 결과를 견주는 기계 기준을 다시 쓴다. 지금은 바뀐 파일 목록, 절 제목과 순서, 남은 `{…}` 안내 글, `{확인 필요}` 칸, 목록 칸의 항목 수, 출처 경로의 집합이고, 해석 칸은 빠져 있다.
- Codex 다음에 Grok Build를 확인한다.
