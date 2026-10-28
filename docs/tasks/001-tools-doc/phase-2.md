# Phase 2: TOOLS.md를 줄이고 시험 실행 기록 규칙을 바꾼다

**목표**: `docs/TOOLS.md`가 계속 쓰이는 도구 사실만 담아 15KB 이하가 되고, plan과 ARCHITECTURE가 시험 실행 기록을 맥락 문서에 적지 않게 한다.

**테스트 먼저**: 아니오 — 맥락 문서와 스킬 본문(`.md`), 그 글을 지키는 테스트만 바꾼다

**읽을 것**
- `docs/TOOLS.md` (전체. 남길 절: 머리글과 `## 지금 상태`, `## Claude Code`의 첫 목록, `서브에이전트, 권한, worktree`, `훅`, `세션 도중의 스킬 본문 고침`, `ruleset과 CODEOWNERS로 워크플로 PR의 자동 머지를 막는지 본 것`, `플러그인 폴더의 편집과 권한 모드`, `스킬을 헤드리스로 돌려 볼 때의 허용 목록`, `## Codex`부터 끝까지. 지울 절: "판정에서 본 것", "돌려 본 것"이 제목에 든 그 밖의 절들)
- `AGENTS.md` (작업 규칙의 마지막 줄이 `플러그인 폴더의 편집과 권한 모드`를 가리킨다)
- `docs/ADR.md` (ADR-018, ADR-023이 TOOLS.md와 그 절을 가리킨다)
- `docs/ARCHITECTURE.md` (`## 기술 스택`의 대상 도구 줄, `## 패턴과 규칙`의 `docs/TOOLS.md`에 적는다는 줄과 작업 트리의 스킬 줄 예외 줄, CI 줄의 "`docs/TOOLS.md`에서 시험한 JSON의 `gh api` 명령")
- `README.md` (Codex 확인을 멈춘 상태를 말하는 줄)
- `plugins/plate/skills/plan/SKILL.md` (`## 적는 규칙`의 **조건**)
- `tests/test_skill_rules.py` (`PlanRulesTest`)

**TODO**
- [x] 지울 절에 다음 계획이 알아야 할 도구 동작이 있으면 버전과 함께 한 줄로 남길 절에 옮기고, 지울 절을 모두 지운다. 남길 절도 임시 경로, 본문 해시, 커밋 id, 장면의 차림을 빼고 사실 위주로 줄인다. ruleset 절은 거는 `gh api` 명령과 JSON, PR을 연 계정이 유일한 코드 소유자면 막지 못한다는 사실을 남긴다. 머리글은 이 문서가 도구 사실과 확인을 멈춘 지점만 담고 시험 실행 기록은 담지 않는다고 바뀐다. 파일은 15360바이트 이하가 된다 (`docs/TOOLS.md`)
- [x] plan `적는 규칙`의 **조건**에, 돌려 본 확인의 결과(차림, 출력, 본문 해시)는 그 phase의 기록에만 남기고 맥락 문서에 옮겨 적는 TODO나 조건을 두지 않으며, 맥락 문서에는 다음 계획이 알아야 할 도구 동작만 한 줄로 더한다는 규칙이 더해진다 (`plugins/plate/skills/plan/SKILL.md`)
- [x] `PlanRulesTest`에 그 규칙의 글이 **조건**에 있는지 보는 테스트가 더해진다 (`tests/test_skill_rules.py`)
- [x] ARCHITECTURE `## 패턴과 규칙`의 "도구마다 다른 동작과 확인을 멈춘 지점은 `docs/TOOLS.md`에 적는다" 줄에 시험 실행 기록은 적지 않고 phase 기록에 둔다는 글이 더해지고, `test_skill_rules.py` 줄의 테스트 설명에 새 테스트가 다루는 규칙이 더해진다. 남긴 절을 가리키는 `AGENTS.md`, ADR-018·ADR-023, README, ARCHITECTURE의 줄은 절 이름이 그대로라 고치지 않는다 (`docs/ARCHITECTURE.md`)

**통과 조건**
- TOOLS.md가 줄고 가리키는 절과 ruleset 명령이 남고 시험 실행 기록이 없다. (완료 조건 2)
  - 확인: `wc -c < docs/TOOLS.md`가 15360 이하다
  - 확인: `플러그인 폴더의 편집과 권한 모드`, `세션 도중의 스킬 본문 고침`, `ruleset과 CODEOWNERS로 워크플로 PR의 자동 머지를 막는지 본 것`, `도구를 넓힐 때 할 것`마다 `grep -c '<절 이름>' docs/TOOLS.md`가 1 이상이다
  - 확인: `grep -c 'rulesets --input -' docs/TOOLS.md`와 `grep -c '"enforcement"' docs/TOOLS.md`가 저마다 1 이상이다
  - 확인: `grep -cE '/var/folders/|tmp\.[A-Za-z0-9]{6,}|장면 [A-Z]' docs/TOOLS.md`가 0이다
- plan과 ARCHITECTURE가 시험 실행 기록을 맥락 문서에 적지 않게 한다. (완료 조건 3)
  - 확인: `python3 -m unittest discover -s tests`가 `OK`로 끝나고, 새 테스트가 plan `적는 규칙`의 **조건** 부분에서 그 규칙의 글을 단언한다
  - 확인: ARCHITECTURE `## 패턴과 규칙`의 TOOLS.md 줄을 읽어 "도구마다 다른 동작과 확인을 멈춘 지점"과 "시험 실행 기록은 적지 않는다"가 둘 다 있다
- 앞 phase가 고친 규칙이 그대로다. (완료 조건 1, 4)
  - 확인: `git grep -n 'TOOLS.md' -- plugins/`가 아무것도 내지 않는다
  - 확인: `git grep -nE '사용량.*TOOLS\.md|TOOLS\.md.*사용량' -- docs/PRD.md docs/ARCHITECTURE.md docs/ADR.md README.md AGENTS.md`가 아무것도 내지 않는다

## 한 일
- 지울 절의 도구 동작을 남길 절로 옮기고 지울 절을 모두 지우고 남길 절을 줄인다: "판정에서 본 것", "돌려 본 것"이 제목에 든 절(실행 스킬·5단계·tasks 실행의 판정, setup의 CI 물음, CI의 세 판정, AGENTS.md 되돌림, verdict 단계, 원격 없는 합치기, cleanup·run·plan·phase·eval·review·retro를 돌려 본 절들)을 지웠다. 그 절들에서 다음 계획이 알아야 할 도구 동작을 버전과 함께 한 줄로 옮겼다: 이은 명령과 명령 치환의 막힘, `git -C`·`cd && git`·`sed -n`·프로젝트 밖 출력의 승인 요구, 프로젝트 밖 파일과 WebFetch의 막힘, `--allowedTools`가 프롬프트를 삼킴, init 줄의 자리와 `permissionMode`, 세션 기록 위치, `git clone`의 `origin/HEAD`(`## Claude Code` 첫 목록), 사용량이 `tool_result`의 `<usage>`로 돌아옴(서브에이전트 절), Bash 훅의 기록 꼴과 `permission_denials`, 훅이 허용 목록보다 앞섬(훅 절), `gh issue list --search`, 이슈 번호, `workflow` 범위, claude-code-action의 되돌리는 경로·`execution_file`·github-actions PR의 실패(새 소절 "GitHub와 claude-code-action"). 허용 목록 절은 22항목 목록 하나와 `gh issue view`로 줄였다. ruleset 절은 `gh api -X POST repos/<owner>/<repo>/rulesets --input -`와 JSON, 막은 것, PR을 연 계정이 유일한 코드 소유자면 막지 못한다는 사실, 다른 설정이 막지 못한 것만 남겼다. 남길 절에서 임시 경로, 본문 해시, 커밋 id, 실행 id, 세션 id, 시험 스크립트·로그 경로, 실행 시간을 뺐다. Codex 이하도 사실 위주로 줄였다. 머리글은 도구 사실과 확인을 멈춘 지점만 담고 시험 실행 기록은 phase 기록에 있다고 바꿨다. 140201바이트 → 14287바이트 (`docs/TOOLS.md`)
- plan `적는 규칙`의 **조건**에 규칙을 더한다: "돌려 본 확인의 결과(차림, 출력, 본문 해시)는 그 phase의 기록에만 남긴다. 그 결과를 맥락 문서에 옮겨 적는 TODO나 조건을 두지 않는다. 맥락 문서에는 다음 계획이 알아야 할 도구 동작(…)만 한 줄로 더한다."를 `- 돌리지 않음` 규칙 줄 바로 뒤에 더했다. TOOLS.md라는 이름은 쓰지 않았다(task 머리 결정) (`plugins/plate/skills/plan/SKILL.md`)
- `PlanRulesTest`에 테스트를 더한다: `test_run_results_stay_in_phase_record`가 **조건** 부분에서 그 규칙의 글 네 조각을 단언한다 (`tests/test_skill_rules.py`)
- ARCHITECTURE를 고친다: `## 패턴과 규칙`의 TOOLS.md 줄에 "시험 실행 기록은 적지 않는다. 돌려 본 확인의 차림, 출력, 본문 해시는 그 phase의 기록에 두고, `docs/TOOLS.md`에는 다음 계획이 알아야 할 도구 동작만 버전과 함께 한 줄로 더한다."를 더했고, `test_skill_rules.py` 줄의 설명에 "돌려 본 확인의 결과는 phase 기록에만 두고 맥락 문서에는 도구 동작만 한 줄로 더함"을 더했다. AGENTS.md, ADR, README는 가리키는 절 이름이 그대로라 고치지 않았다 (`docs/ARCHITECTURE.md`)

## 확인 결과
- TOOLS.md가 줄고 가리키는 절과 ruleset 명령이 남고 시험 실행 기록이 없다. (완료 조건 2)
  - `wc -c < docs/TOOLS.md` → `14287`. 15360 이하. 통과
  - 네 절 이름마다 `grep -c '<절 이름>' docs/TOOLS.md` → `1`, `1`, `1`, `1`. 통과
  - `grep -c 'rulesets --input -' docs/TOOLS.md` → `1`, `grep -c '"enforcement"' docs/TOOLS.md` → `1`. 통과
  - `grep -cE '/var/folders/|tmp\.[A-Za-z0-9]{6,}|장면 [A-Z]' docs/TOOLS.md` → `0`. 통과
- plan과 ARCHITECTURE가 시험 실행 기록을 맥락 문서에 적지 않게 한다. (완료 조건 3)
  - `python3 -m unittest discover -s tests` → `Ran 165 tests`, `OK`. 새 테스트 `PlanRulesTest.test_run_results_stay_in_phase_record`가 `part(section(..., "적는 규칙"), "조건")`에서 규칙의 글을 단언하고, 따로 돌려 `OK`. 통과
  - ARCHITECTURE `## 패턴과 규칙`의 TOOLS.md 줄을 읽음 → "도구마다 다른 동작과 확인을 멈춘 지점"과 "시험 실행 기록은 적지 않는다"가 둘 다 있다. 통과
- 앞 phase가 고친 규칙이 그대로다. (완료 조건 1, 4)
  - `git grep -n 'TOOLS.md' -- plugins/` → 출력 없음(종료 코드 1). 통과
  - `git grep -nE '사용량.*TOOLS\.md|TOOLS\.md.*사용량' -- docs/PRD.md docs/ARCHITECTURE.md docs/ADR.md README.md AGENTS.md` → 출력 없음(종료 코드 1). 통과

## 계획과 달라진 점
- 읽을 것은 `## Codex`부터 끝까지를 남길 절로 적었으나, 15360바이트에 맞추려고 Codex의 세 소절을 한 목록으로, Grok Build를 한 문단으로, "두 도구에서 같은 결과를 확인한 것"을 한 문단으로, "Codex에서 확인을 멈춘 지점"의 표를 목록 두 줄로 줄였다. 절 제목(`## Codex`, `## Grok Build`, `## 두 도구에서 같은 결과를 확인한 것`, `## Codex에서 확인을 멈춘 지점`, `## 도구를 넓힐 때 할 것`)은 그대로다. TODO의 "남길 절도 사실 위주로 줄인다"에 든다고 봤다.
- 지울 절의 GitHub·claude-code-action 사실을 옮길 남길 절이 없어 `## Claude Code` 아래에 소절 "GitHub와 claude-code-action"을 새로 두었다.
- ruleset JSON의 `name`을 시험 때의 `workflow-guard-probe`에서 `workflow-guard`로 바꾸고 저장소 자리를 `<owner>/<repo>`로 두었다. 시험 차림이 아니라 거는 명령으로 남기려는 것이다.

## 남은 것
- 지운 절의 실행 시간, 판정마다의 관찰(스킬이 무엇을 출력했는지), 시험 폴더(`~/plate-rail-test`)와 스크립트 경로는 옮기지 않았다. 그것들은 git 기록(이 phase 앞의 `docs/TOOLS.md`)에만 남는다.
- "도구를 넓힐 때 할 것"에서 시험 폴더 `~/plate-rail-test`의 위치를 뺐다. 넓힐 때 판정 도구를 다시 차려야 할 수 있다.

## 하네스에서 걸린 것
- 없음
