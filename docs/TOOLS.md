# 도구별로 확인해 둔 사실

레일을 돌리는 도구(Claude Code, Codex, Grok Build)마다 확인해 둔 사실과 확인을 멈춘 지점을 적는다. 1단계부터 3단계까지를 만들면서 확인한 것을 단계 설계 문서에서 옮겼다(ADR-018). 사실마다 확인한 날짜나 버전을 적었고, 그 뒤로 바뀌었을 수 있다.

## 지금 상태

| 도구 | 상태 |
|---|---|
| Claude Code | 완성 판정을 이 도구로 한다. 1단계(셋업), 2단계(맥락 채우기), 3단계(계획)의 판정을 여기서 돌렸다 |
| Codex | 2026-10-08에 확인을 멈췄다. 1단계 전부와 2단계 판정의 일부만 확인했다. 남은 것은 아래 "Codex에서 확인을 멈춘 지점"에 있다 |
| Grok Build | 이 Mac에 설치돼 있지 않다. 판정을 돌린 적이 없다 |

Codex → Grok Build 순으로 넓히는 일은 v1.0 뒤에 한다(ADR-018).

## Claude Code

1단계는 2.1.291(2026-10-06), 2단계의 2026-10-08 판정은 2.1.293, 3단계의 판정은 2.1.294(2026-10-08)에서 돌렸다.

- `claude --plugin-dir <플러그인 폴더>`로 시작하면 그 폴더의 플러그인을 그 세션에만 불러온다. 설치 기록과 마켓플레이스 등록을 건드리지 않는다.
- 설치된 `plate@harness-plate`는 옛 0.3.0이고 꺼져 있다(2026-10-08). 시험은 `--plugin-dir`로 레포의 본문을 읽는다.
- 스킬은 `/plate:setup`, `/plate:context`, `/plate:plan`으로 부른다. 헤드리스(`claude -p`)에서도 불린다.
- `CLAUDE.md`가 없을 때만 `AGENTS.md`를 읽는다. 그래서 `CLAUDE.md`에 `@AGENTS.md` 임포트를 항상 둔다(ADR-007).
- 헤드리스에서 물음의 답을 프롬프트에 미리 주면 다시 묻지 않는다.
- 헤드리스에서도 한 스킬이 같은 플러그인의 다른 스킬을 이름으로 부른다(`plate:setup`, `plate:context`). 미리 준 답은 호출의 인자로 넘긴다(2026-10-06).
- 스킬이 다른 스킬을 불렀다가 돌아와 자기 절차를 잇는 것은 세 스킬에 걸쳐서도 된다(plan → setup → 돌아와 계획. 2026-10-08, 3단계의 판정 8과 10).
- 헤드리스에서 세션을 이어 여러 턴을 주고받을 수 있다(2026-10-06). `claude -p "<첫 턴>" --plugin-dir <플러그인 폴더> --permission-mode acceptEdits --output-format json`의 출력에서 `session_id`를 읽고, `claude -p --resume <session_id> "<다음 턴>"`에 같은 옵션을 붙여 잇는다. 세션 id는 턴이 바뀌어도 같다. 세션은 폴더에 묶이므로 모든 턴을 같은 폴더에서 실행한다.
- 헤드리스에서 `--permission-mode acceptEdits`만 주면 파일 쓰기는 되고 `git add`와 `git commit`은 승인을 요구하며 막힌다. `--allowedTools "Bash(git add:*)" "Bash(git commit:*)"`를 더하면 커밋까지 된다. `--allowedTools`는 뒤의 인자를 여럿 받으므로 요청 글을 옵션들 앞에 둔다(2026-10-08).
- 헤드리스에서 `git -C <경로> status`처럼 `-C`를 붙인 꼴은 읽기만 하는 명령이어도 승인을 요구했다. 폴더 안에서 `git status`로 돌린 것은 막히지 않았다(2026-10-08).
- 커밋 메시지의 본문에 `Co-Authored-By:` 줄을 붙였다. 제목 줄은 요청한 글 그대로였다(2026-10-08).
- 실행 시간. 2026-10-06에는 한 번에 2~9분이었고, 스킬이 시키지 않은 자체 검증 명령이 권한에 막혀 되풀이될 때 길어졌다(빈 폴더의 셋업 한 번이 12분). 2026-10-08에는 셋업이 257~459초, 맥락 채우기가 312~410초였다. 폴더가 다르면 여러 실행을 한꺼번에 돌려도 된다.

**서브에이전트, 권한, worktree** (2.1.296, 2026-10-13. 헤드리스에서 직접 돌려 확인했다. 시험용 플러그인은 `~/plate-rail-test/probe-plugin`, 실행 스크립트는 `bin/a2.sh`, 기록은 `logs/a2-*.jsonl`이다)

- 명령의 꼴은 `claude -p "<요청>" --allowedTools "<항목>" "<항목>" --plugin-dir <플러그인 폴더> --permission-mode acceptEdits --forward-subagent-text --output-format stream-json --verbose`다. 이 꼴로 돌린 기록에는 서브에이전트가 받은 글, 쓴 글, 도구 호출이 `parent_tool_use_id`와 함께 남는다.
- 서브에이전트가 플러그인 스킬을 이름으로 부른다. 메인이 "probe의 work 스킬(`probe:work`)을 불러 그 절차를 따른다"와 번호만 넘겨도 서브에이전트가 스킬 본문을 받아 따랐다.
- 서브에이전트에게 `CLAUDE.md`와 그 `@` 임포트가 실린다(문서로 확인했다. 1단계의 판정에서도 서브에이전트에게 문서 지도가 실리는 것을 봤다).
- `--allowedTools`가 서브에이전트에게 이어진다. `"Bash(git add:*)" "Bash(git commit:*)"`만 주고 서브에이전트 셋이 모두 커밋했다.
- 한 번의 실행에서 메인이 에이전트 셋을 차례로 띄우고 돌아온 줄을 모아 보고했다. 80초가 걸렸다(에이전트 하나에 약 25초).
- 허용 목록 없이는 `test -f`, `grep -q`, `ls`와 그것들을 `&&`로 이은 명령만 되고, `python3 -m unittest`, `python3 -m venv`, `.venv/bin/pip install`, `.venv/bin/python -m pytest`, `python3 -c`는 승인을 요구하며 막힌다. `"Bash(python3:*)" "Bash(.venv/bin/pip:*)" "Bash(.venv/bin/python:*)"`를 더하면 서브에이전트가 모두 돌린다.
- 막힌 명령 하나마다 약 65초를 기다린다. 다섯이 막힌 실행이 363초였고 `--permission-prompts none`을 붙여도 367초였다. 허용 목록에서 빠진 명령은 실행 시간을 크게 늘린다.
- `"Bash(git rm:*)" "Bash(git worktree:*)" "Bash(git merge:*)" "Bash(git branch:*)"`를 더하면 `git worktree add <경로> -b <브랜치>`, `git rm`, `git merge <브랜치>`, `git worktree remove`, `git branch -d`가 된다. `git merge`는 편집기를 띄우지 않고 병합 커밋을 만든다.
- `.git/info/exclude`는 쓰지 못한다. 파일을 고치는 도구도 `echo … >> .git/info/exclude`도 민감한 파일이라며 막히고, `--allowedTools "Edit(.git/info/exclude)"`로도 풀리지 않는다. `.worktrees/.gitignore`에 `*` 한 줄을 쓰는 것은 막히지 않고, 그 뒤에 worktree를 만들고 지워도 `git status --short`가 비어 있다.
- worktree 폴더에서 연 헤드리스 세션도 플러그인 스킬을 부르고 그 브랜치에 커밋한다. 서브에이전트가 `git -C <절대 경로> add`를 먼저 써서 한 번 막힌 뒤 `git add`로 했다.

## Codex

0.160.0에서 확인했다(2026-10-06).

**설치와 매니페스트**

- `codex plugin marketplace add <폴더>`(로컬 경로 가능) 뒤 `codex plugin add plate@harness-plate`로 설치한다. 플러그인을 한 세션에만 불러오는 옵션은 없다. 로컬 마켓플레이스 등록과 설치는 그대로 뒀다(ADR-004).
- 설치할 때 플러그인을 `~/.codex/plugins/cache/harness-plate/plate/<버전>/`으로 복사해 그 사본을 읽는다. 스킬을 고친 뒤에는 `codex plugin add plate@harness-plate`를 다시 실행해야 설치본이 최신 스킬로 바뀐다.
- `plugins/plate/.codex-plugin/plugin.json`은 `name`, `version`, `description`, `author`, `repository`, `"skills": "./skills/"`만으로 설치된다. `interface`(표시 이름, 아이콘 등)는 없어도 된다.
- `.agents/plugins/marketplace.json`은 최상위에 `name`, `interface.displayName`, `plugins[]`를 두고, 항목마다 `name`, `source`(`"source": "local"`, `"path": "./plugins/plate"`), `policy.installation`, `policy.authentication`, `category`를 둔다.
- 공식 문서는 새 패키지에 플러그인 루트의 `plugin.json`(Agent Plugins 규격)을 권하고 `.codex-plugin/plugin.json`은 호환용이라고 적는다(지원은 계속된다). Codex가 Claude 형식 매니페스트와 `.claude-plugin/marketplace.json`도 읽는다고 적혀 있으나 직접 확인하지 않았다. 근거는 developers.openai.com/plugins/build/plugins.md와 `obra/superpowers`의 `.codex-plugin/plugin.json`, `.agents/plugins/marketplace.json`이다.

**스킬**

- 스킬은 `$plate:setup`, `$plate:context`로 부른다. 이름은 Claude Code와 같다.
- 세션을 시작할 때 스킬마다 이름, 설명, 파일 경로를 모델에게 싣는다. 본문은 싣지 않는다. 사용자가 `$이름`으로 부르면 본문 전체를 넣고, 그 밖에는 모델이 필요하다고 판단할 때 스스로 파일을 연다(`codex debug prompt-input`과 공식 문서 `learn.chatgpt.com/docs/build-skills`로 확인).
- 스킬 목록은 컨텍스트의 2%까지만 쓴다. 스킬이 많으면 일부가 목록에서 빠질 수 있다.
- 스킬의 파일 경로에 버전이 들어 있다. 그래서 스킬 본문에서 다른 스킬은 경로가 아니라 이름으로 가리킨다(ADR-017).
- 본문에 "plate의 setup 스킬(`plate:setup`)을 불러 절차를 따른다"고만 적어도 모델이 그 스킬의 `SKILL.md`를 열어 절차를 따른다.
- `AGENTS.md`를 자동으로 읽는다.

**샌드박스와 헤드리스**

- `read-only`와 `workspace-write` 샌드박스 모두 플러그인 캐시 폴더를 읽을 수 있다.
- `read-only`에서는 `git rev-parse`가 실패한다(xcrun이 캐시 파일을 쓰지 못한다). 판정은 `workspace-write`로 돌린다.
- `workspace-write`는 `.git` 쓰기를 막는다. 빈 폴더에서 `git init`이 실패하고, Codex는 실패를 보고한 뒤 나머지를 끝낸다. 그래서 시험할 빈 폴더는 미리 `git init`을 해 둔다.
- 헤드리스 실행은 `codex exec --sandbox workspace-write "<요청>"`이다. 물음의 답을 미리 주면 다시 묻지 않는다.
- 헤드리스에서 세션을 이어 여러 턴을 주고받을 수 있다. `codex exec --sandbox workspace-write --json "<첫 턴>"`의 첫 줄(`thread.started`)에서 `thread_id`를 읽고, `codex exec resume <thread_id> --json "<다음 턴>"`으로 잇는다. `resume`에는 `--sandbox` 옵션이 없고, 첫 턴의 `workspace-write`가 이어져 둘째 턴도 파일을 썼다(`~/.codex/config.toml`에 샌드박스 설정이 없는 상태였다). 세션은 폴더에 묶인다.
- 실행 시간은 한 번에 1~2분이었다.
- 2026-10-06 22:55쯤 사용 한도에 걸렸다. 오류 글은 10월 7일 00:57에 다시 쓸 수 있다고 했다.

## Grok Build

1.0.46 기준이다. 이 Mac에 설치돼 있지 않다(2026-10-06). 아래 셋을 어떻게 확인했는지는 기록이 없다.

- Claude 형식 플러그인을 그대로 읽는다.
- `AGENTS.md`를 자동으로 읽는다.
- 종료 차단 훅이 없다.

## 두 도구에서 같은 결과를 확인한 것

Claude Code와 Codex에 같은 답을 주고 헤드리스로 돌렸다(2026-10-06).

**셋업**

- 빈 폴더와 excel-viewer 복제본(`CLAUDE.md` 내용 옮기기 승인)에서 두 도구의 결과 폴더가 바이트 단위로 같았다.
- 다시 돌려도 변화가 없었다.
- 셋업 스킬에 재실행 물음과 끝 물음을 더한 뒤에 다시 돌렸을 때도 같았다.

**맥락 채우기** (커밋 a131ed4의 스킬)

- 빈 폴더에서 답을 모두 주면 PRD·ARCHITECTURE·ADR이 채워지고 남은 칸이 0개다. 구조는 두 도구가 같았고, 글자가 다른 곳은 다듬은 표현 넷이었다.
- 일부 답을 미루면 그 칸이 `{확인 필요}`가 된다. 두 도구에서 같은 칸이었다.
- 남은 답을 주고 다시 부르면 남은 칸만 바뀐다.
- 남은 칸이 없을 때 다시 부르면 변화가 없다.
- 셋업하지 않은 폴더에서 맥락 채우기를 부르면 셋업을 할지 묻고, 승인하면 셋업 결과가 셋업을 따로 돌린 결과와 같고, 이어서 채운다.
- 셋업의 끝 물음에 채운다고 답하면 맥락 채우기로 이어진다.
- 채운 뒤 셋업을 다시 돌려도 화면이 있는 프로젝트인지 묻지 않고 변화가 없다.

## Codex에서 확인을 멈춘 지점

**끊긴 판정 넷.** Claude Code에서는 모두 통과했다. Codex에서는 2026-10-06의 사용 한도 오류로 앞의 셋이 도중에 끊겼고 넷째는 시작하지 못했다.

| 시험 폴더 | 확인하는 것 |
|---|---|
| excel-viewer 복제본 | 스캔으로 적은 사실에 출처 경로가 붙는다. ADR 후보가 다섯 범주 안이다. `README.md`·`TODO.md`가 바뀌지 않는다 |
| badak-next-app 복제본(루트 `DESIGN.md`를 지운 변형) | `docs/DESIGN.md`의 토큰이 `src/app/global.css`의 이름과 값 그대로다 |
| finsight 복제본(커밋 `bdff8d9`) | 이미 채워진 PRD·ARCHITECTURE·ADR은 바뀌지 않고 `docs/DESIGN.md`만 채워진다 |
| 셋업한 빈 폴더, 여러 턴 | 답을 미리 주지 않으면 질문이 한 턴에 하나씩 나온다. 초안을 승인하기 전에는 파일이 바뀌지 않는다. 도중에 그만하면 답한 칸만 쓰인다 |

**2026-10-08에 고친 본문.** Codex에서 확인하지 않았다. Codex 설치본(`~/.codex/plugins/cache/harness-plate/plate/0.5.0`)의 스킬은 커밋 a131ed4의 것이고 이날 고친 본문은 들어 있지 않다.

- 맥락 채우기의 "기술 스택" 절. 2026-10-06의 실행에서 badak-next-app의 기술 스택이 도구마다 달랐다. Claude Code는 8줄에 빌드 매니페스트 밖에서 읽은 것(DB 없음, 배포처, 패키지 매니저)이 섞였고, Codex는 7줄에 모두 `package.json`에서 적었으나 묶는 방식이 달랐다. 규칙을 더한 뒤 Claude Code에서는 14줄(언어 1, `dependencies` 13)로 `package.json`과 맞았다.
- 맥락 채우기의 DESIGN 앞머리 출처 주석. 토큰 파일에서 옮긴 범주에만 붙인다.
- 셋업의 새 `AGENTS.md` 첫 줄. `CLAUDE.md`의 내용을 옮기는데 `AGENTS.md`가 없던 프로젝트(badak-next-app, finsight)에서 Codex는 새 `AGENTS.md`의 첫 줄을 빈 줄로 두고 Claude Code는 두지 않았다. 한 바이트가 달랐다. 본문이 `AGENTS.md`가 없을 때 빈 줄을 어떻게 하는지 말하지 않았기 때문이고, 빈 줄 없이 첫 줄부터 적는다고 고쳤다.

## 도구를 넓힐 때 할 것

v1.0 뒤에 한다(ADR-018). 시험 폴더, 판정 도구, 답 파일의 위치는 ADR-019에 있다.

- Codex에서 끊긴 판정 넷을 돌린다.
- 2026-10-08에 고친 본문 셋을 Codex에서 확인한다. 새 `AGENTS.md`의 첫 줄은 Codex에서만 빈 줄이 나오던 곳이다.
- Codex에서 계획 스킬의 판정 열 경우를 돌린다(ADR-031). 계획 스킬은 Codex에서 돌린 적이 없다. 계획 스킬은 커밋을 하는데 `workspace-write`는 `.git` 쓰기를 막으므로 돌릴 샌드박스부터 확인한다.
- Codex에서 실행 스킬 셋(run, phase, retro)의 판정을 돌린다. 서브에이전트를 띄우는 방법, 서브에이전트가 스킬을 부르는 방법, worktree와 `.git` 쓰기를 막는 샌드박스부터 확인한다.
- 두 도구의 결과를 서로 견주는 기계 기준을 다시 쓴다. 지금의 기준은 바뀐 파일 목록, 절 제목과 순서, 남은 `{…}` 안내 글이 없음, `{확인 필요}`가 있는 칸, 목록 칸의 항목 수, 출처 경로의 집합이고, 해석 칸(패턴과 규칙, 데이터 흐름, 폴더의 역할)은 빠져 있다(ADR-019).
- Codex 다음에 Grok Build를 확인한다.
