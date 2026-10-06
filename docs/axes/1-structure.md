# 1축. 구조 설계 — 폴더 / 도구 / 경계

> [HANDOFF.md](../../HANDOFF.md)에서 나눈 6축 문서다. 표시(기본값·결정·보류·남음)의 뜻과 기호(J, R, M1–M4)는 HANDOFF.md에 있다. 결정을 확정하거나 바꾸면 아래 표와 [결정 기록](../decisions.md)을 함께 고친다.

**다루는 질문**: 무엇을 어디에 두고, 누가 어떤 도구까지 쓸 수 있는가.

| | 레퍼런스와 내 자산 |
|---|---|
| 폴더 | **J**: `docs/`, `phases/{name}/`, `.claude/commands/`, `scripts/`<br>**R**: `.claude/agents/`(누가) ↔ `.claude/skills/`(어떻게), 중간 산출물은 `_workspace/`, `commands/`는 금지<br>**M1**: `plugins/<kit>/{hooks,skills,agents,scripts}`, `.claude/rules/` |
| 도구 | **R**: 읽기 전용 리뷰어는 Edit·Write를 뺀다<br>**M1**: `agent-guard.sh`가 `agent_type`별로 Bash 쓰기를 거부한다 |
| 경계 | **J**: 가드 훅이 사실상 동작하지 않는다(`$CLAUDE_TOOL_INPUT`, `exit 1`)<br>**M1**: 마커로 프로젝트를 식별해 옵트인하고, MCP 쓰기 도구·`touch`·`cat >` 우회까지 막는다 |

**결정과 처리**

| # | 결정 | 처리 |
|---|---|---|
| 1 | 배포 형태: 플러그인+마켓플레이스(업데이트 전파됨) / 복사형 템플릿 / 혼합(플러그인 + init 스캐폴드) | **결정**(2026-10-04): 플러그인+마켓플레이스다. 이 레포가 마켓플레이스 `harness-plate`이고 플러그인 `plate`는 `plugins/plate/`에 둔다(설계 문서는 설치본에 넣지 않는다). 설치 원본은 GitHub의 `main`이다. 설치는 쓸 프로젝트에서 프로젝트 범위로만 한다(5번): `claude plugin marketplace add werwer748/harness-plate --scope project` → `claude plugin install plate@harness-plate --scope project`. 두 명령 모두 기본 범위가 user라서 `--scope project`를 빼면 전역 설정에 적힌다. 내려받은 사본과 설치 기록은 Claude Code가 `~/.claude/plugins/`에 둔다. 업데이트: `claude plugin marketplace update harness-plate` → `claude plugin update plate@harness-plate`. 합치기 전에는 `claude --plugin-dir plugins/plate`로 불러와 확인한다 |
| 2 | 하네스 공통부(플러그인)와 프로젝트 고유부(`CLAUDE.md`, `docs/`, 검사 명령)의 경계선 | **결정**(2026-10-05, 문서): 양식과 절차는 플러그인(`plugins/plate/skills/init/SKILL.md`)에 두고, 채운 문서(`docs/`)와 `CLAUDE.md`는 프로젝트에 둔다. **보류**(그 밖): 검사 명령처럼 훅이 읽을 프로젝트 값은 그런 장치를 플러그인에 넣게 될 때 정한다 |
| 3 | 폴더 규약: `phases/`, `_workspace/`, `docs/`, `.claude/rules/` 중 무엇을 표준으로 삼을지 | **기본값**: 새 규약을 만들지 않는다. `docs/`는 `/plate:init`이 만드는 세 문서의 자리로 쓴다(2축 3번). `phases/`와 `_workspace/`는 step 분할과 팀 실행을 전제로 하므로 그 장치를 켤 때 함께 정한다 |
| 4 | 도구 경계를 어느 층에서 거는가: `settings` permissions / agent `tools:` / PreToolUse 훅 | **결정**: permissions(와 auto mode·샌드박스) → 에이전트 `tools:` → 훅 순서로 건다. 훅은 예외 없이 막아야 하는 것과, Bash가 필요한 읽기 전용 에이전트의 쓰기 차단에만 쓴다(`tools:`로는 `cat >`와 `touch`를 막지 못한다) |
| 5 | 프로젝트 옵트인 방식: 마커 파일(예: `.claude/plate.json`)을 둘 것인가 | **결정**(2026-10-04): 마커 파일을 두지 않는다. 플러그인을 프로젝트 범위로 설치하는 것이 옵트인이다. 그 프로젝트의 `.claude/settings.json`에 `extraKnownMarketplaces`와 `enabledPlugins`가 적히고, 설치하지 않은 프로젝트에서는 하네스가 돌지 않는다. 사용자 범위 설치와 전역 설정 배선은 하지 않는다 |

**이미 겪은 함정 (M2)**
- 플러그인 에이전트 matcher는 `(^|:)name$`로 써야 한다
- 플러그인 에이전트 frontmatter의 `hooks:`는 무시된다
- 워크트리에서는 본체 쪽 훅이 돈다
- 디렉터리 마켓플레이스도 캐시로 복사되므로 버전을 올려야 반영된다(sheetview-kit 캐시가 1.0.0에 머물러 있다)
