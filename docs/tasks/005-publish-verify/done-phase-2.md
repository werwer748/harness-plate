# Phase 2: setup과 CI 없는 PR 장면

**목표**: 시험 저장소를 origin으로 둔 시험 폴더에서 setup이 CI 워크플로를 둘지 묻고, plate 워크플로가 없는 시험 저장소로 run이 PR을 열어 평가서 댓글을 단다.

**테스트 먼저**: 아니오 — 시험 폴더에서 스킬을 돌려 보고, 이 저장소에서는 `docs/TOOLS.md`만 고친다

**읽을 것**
- `docs/TOOLS.md`의 Claude Code 절 (헤드리스 실행과 세션 잇기, 묻는 글을 기록에 남기는 법, "tasks 실행의 판정에서 본 것"의 시험 폴더와 실행 스크립트)
- `plugins/plate/skills/setup/SKILL.md` (CI 워크플로의 물음, 양식, 보고의 시크릿 안내)
- `plugins/plate/skills/run/SKILL.md` (tasks 끝의 PR 절, 평가서 댓글)
- `plugins/plate/hooks/hooks.json`과 거기에 걸린 푸시 훅 (셋업된 폴더에서 기본 브랜치로 하는 푸시를 막는다)

**TODO**
- [x] 시험 저장소의 `main`에 코드와 그 테스트가 있는 작은 시험 프로젝트가 생기고, plate 워크플로는 없다 (`werwer748/plate-ci-test`)
- [x] setup 장면: 시험 저장소를 origin으로 둔 시험 폴더에서 setup이 CI 에이전트를 둘지 묻고, 승인하면 그 폴더의 `.github/workflows/` 아래에 워크플로 파일이 생기고 보고에 `CLAUDE_CODE_OAUTH_TOKEN` 시크릿 등록 방법이 있다. 실행 기록은 setup 본문을 마지막으로 고친 뒤에 만든다
- [x] CI 없는 run 장면: 시험 저장소를 origin으로 두고 CI 에이전트를 거절해 셋업한 다른 시험 폴더에서 작은 tasks를 계획해 run을 끝까지 돌리면, tasks 끝에 PR을 열지 묻는다. 승인하면 `tasks/`로 시작하는 브랜치에서 `main`으로 가는 PR이 열리고 평가서 댓글이 달린다. 실행 기록은 run 본문을 마지막으로 고친 뒤에 만든다
- [x] 이 phase의 기록에 장면마다 시험 폴더와 실행 기록의 경로가, run 장면에는 PR 번호도 적힌다 (`docs/tasks/005-publish-verify/phase-2.md`)
- [x] 이 phase에서 확인한 도구의 사실이 시험 폴더와 실행 기록의 위치와 함께 적힌다 (`docs/TOOLS.md`)

**통과 조건**
- 완료 조건 3이 참이다.
  - 확인: 완료 조건 3의 확인을 모두 돌린다. `done-phase-2.md`는 이름이 바뀌기 전인 이 파일로 읽는다
- 시험 저장소의 `main`에 plate 워크플로가 없다.
  - 확인: `gh api repos/werwer748/plate-ci-test/contents/.github/workflows`가 404로 실패한다
- 이 phase에서 확인한 도구의 사실이 `docs/TOOLS.md`에 적혀 있다.
  - 확인: `docs/TOOLS.md`의 Claude Code 절을 읽어 이 phase의 장면에서 본 것이 시험 폴더와 실행 기록의 위치와 함께 있다

## 한 일
- 시험 저장소의 `main`에 코드와 그 테스트가 있는 작은 시험 프로젝트가 생기고, plate 워크플로는 없다: `~/plate-rail-test/ci-src`에 textkit(표준 라이브러리만 쓰는 `textkit/core.py`의 `word_count`, `char_count`와 `tests/test_core.py`의 unittest 테스트 넷, 채운 `docs/PRD.md`·`docs/ARCHITECTURE.md`(명령 절, 테스트 `python3 -m unittest`)·`docs/ADR.md`, `README.md`, `.gitignore`)를 만들어 커밋 `ae98f75`로 비어 있던 `werwer748/plate-ci-test`의 `main`에 푸시했다. `AGENTS.md`, `CLAUDE.md`, `.github/`는 없다 (시험 저장소, `~/plate-rail-test/ci-src`)
- setup 장면: `~/plate-rail-test/bin/cimake.sh`(새로 씀)로 시험 저장소를 복제한 `~/plate-rail-test/ci-setup`에서 `bin/tturn.sh`로 `/plate:setup`을 답 없이 불렀다. 기록 `~/plate-rail-test/logs/ci-setup-1.jsonl`(108초)에서 setup이 할 일 표에 CI 워크플로 쓰기를 승인 필요로 넣고 "**CI 에이전트를 둘까요?**"와 시크릿 `CLAUDE_CODE_OAUTH_TOKEN`이 있어야 돈다는 글을 쓰고 멈췄다. 같은 세션의 다음 턴에 "승인한다. CI 에이전트를 둔다."를 보낸 기록 `~/plate-rail-test/logs/ci-setup-2.jsonl`(178초)에서 `ci-setup/.github/workflows/plate-review.yml`을 setup 본문의 양식과 바이트까지 같게 쓰고, 보고의 "CI 시크릿 등록" 절에 `CLAUDE_CODE_OAUTH_TOKEN`, `claude setup-token`, `gh secret set CLAUDE_CODE_OAUTH_TOKEN`을 적었다. 그 폴더는 커밋하지 않고 푸시하지 않았다 (`~/plate-rail-test/ci-setup`)
- CI 없는 run 장면: 시험 저장소를 복제한 `~/plate-rail-test/ci-norun`에서 setup을 "CI 에이전트를 둘지: 두지 않는다"를 미리 주어 불렀다(기록 `logs/ci-norun-setup.jsonl`, 339초. 워크플로를 쓰지 않았다). `bin/cinorun-plan.sh`(새로 씀)가 그 결과를 `셋업`으로 커밋하고, tasks `line-count`(task `001-line-count`의 phase 하나, 테스트 먼저)의 계획 파일을 손으로 써서 `plan: line-count`로 커밋했다(둘 다 로컬 `main`, 푸시하지 않음). `RUN_ALLOW='Bash(git push:*)|Bash(git remote:*)'`로 세 턴을 돌렸다. `logs/ci-norun-1.jsonl`(1748초): "tasks 일괄로 한다."로 수행, 확인, 회고, 코드 평가, 하네스 eval을 차례로 맡기고 고칠 안을 물었다. `logs/ci-norun-2.jsonl`(130초): "아무것도 고치지 않고 이슈도 올리지 않는다."에 소스 문제 1을 `docs/BACKLOG.md`로 미루고 `docs/tasks/`를 비운 뒤 "**PR을 열까요?**"로 푸시할 브랜치 `tasks/line-count`, 가는 곳 `main`, 제목, 본문, plate 워크플로가 없어 `review.md`의 평가 절을 댓글로 단다는 것을 보이고 멈췄다. `logs/ci-norun-3.jsonl`(202초): "승인한다."에 `git push origin tasks/line-count`, `gh pr create`로 PR #1(https://github.com/werwer748/plate-ci-test/pull/1)을 열고 `review.md`의 `## 평가 1` 절을 댓글(https://github.com/werwer748/plate-ci-test/pull/1#issuecomment-6383196716)로 달았다. PR은 열린 채 둔다 (`~/plate-rail-test/ci-norun`, PR #1)
- 이 phase의 기록에 장면마다 시험 폴더와 실행 기록의 경로가, run 장면에는 PR 번호도 적힌다: 위의 두 항목과 아래 "확인 결과"에 적었다 (`docs/tasks/005-publish-verify/phase-2.md`)
- 이 phase에서 확인한 도구의 사실이 시험 폴더와 실행 기록의 위치와 함께 적힌다: Claude Code 절의 버전 줄에 이 tasks의 시험 버전(2.1.310)을 더하고, "setup의 CI 물음과 CI 없는 PR에서 본 것" 묶음을 더했다. setup의 CI 물음과 워크플로 쓰기, PR 단계에 필요한 허용 항목 `Bash(git push:*)`, 막힌 명령 치환과 지나간 꼴(`$(cat <<'EOF' … EOF)`), run이 단 댓글의 작성자가 `werwer748`인 것, 실행 시간이다 (`docs/TOOLS.md`)

## 확인 결과
- 완료 조건 3이 참이다.
  - 이 파일의 "한 일"에 적은 setup 장면의 실행 기록 → `grep -c 'CI 에이전트를 둘까요' ~/plate-rail-test/logs/ci-setup-1.jsonl` → `2`, `grep -c 'CLAUDE_CODE_OAUTH_TOKEN' ~/plate-rail-test/logs/ci-setup-2.jsonl` → `4`(보고의 시크릿 등록 절에 있다). 통과
  - `ls ~/plate-rail-test/ci-setup/.github/workflows/` → `plate-review.yml`. 통과
  - `test ~/plate-rail-test/logs/ci-setup-1.jsonl -nt plugins/plate/skills/setup/SKILL.md`, 같은 꼴로 `ci-setup-2.jsonl` → 둘 다 참. 통과
  - run 장면의 실행 기록 → `grep -c 'PR을 열까요' ~/plate-rail-test/logs/ci-norun-2.jsonl` → `2`. `test ~/plate-rail-test/logs/ci-norun-2.jsonl -nt plugins/plate/skills/run/SKILL.md`, 같은 꼴로 `ci-norun-3.jsonl` → 둘 다 참. 통과
  - `gh pr view 1 -R werwer748/plate-ci-test --json headRefName,baseRefName,comments` → `headRefName` `tasks/line-count`, `baseRefName` `main`, 댓글 하나(작성자 `werwer748`, 첫 줄 `## 평가 1`, 그 아래 `**대상**`과 범위·바뀐 코드 파일이 이어지는 평가서). 통과
- 시험 저장소의 `main`에 plate 워크플로가 없다.
  - `gh api repos/werwer748/plate-ci-test/contents/.github/workflows` → `{"message":"Not Found",…,"status":"404"}`, `gh: Not Found (HTTP 404)`, 종료 코드 1. 통과
- 이 phase에서 확인한 도구의 사실이 `docs/TOOLS.md`에 적혀 있다.
  - `docs/TOOLS.md`의 Claude Code 절을 다시 읽음 → "setup의 CI 물음과 CI 없는 PR에서 본 것" 묶음에 이 phase의 두 장면에서 본 것이 시험 저장소, 시험 폴더(`ci-src`, `ci-setup`, `ci-norun`), 스크립트(`bin/cimake.sh`, `bin/cinorun-plan.sh`, `bin/tturn.sh`), 실행 기록(`logs/ci-setup-*.jsonl`, `logs/ci-norun-*.jsonl`)의 위치와 함께 있다. 통과

## 계획과 달라진 점
- CI 없는 run 장면의 TODO는 "작은 tasks를 계획해"다. tasks는 plan 스킬을 부르지 않고 `bin/cinorun-plan.sh`로 계획 파일을 손으로 써서 커밋했다. 이 장면이 보는 것은 run의 tasks 끝이고, 앞선 run 판정(`bin/tasksmake.sh`의 `t-run`, `t-all`)도 같은 방법으로 계획을 뒀다
- 시험 저장소의 `main`에 채운 `docs/PRD.md`, `docs/ARCHITECTURE.md`(명령 절), `docs/ADR.md`를 함께 두었다. 그래서 두 장면의 setup은 문서 양식을 만들지 않고 `AGENTS.md`, `CLAUDE.md`, `docs/tasks/.gitkeep`(와 승인한 워크플로)만 만들었다. run의 확인과 평가가 명령 절을 읽고, 다음 phase의 CI도 같은 `main`을 쓰기 때문이다
- `ci-norun`의 셋업 커밋과 계획 커밋은 시험 저장소의 `main`에 올리지 않았다. 그래서 PR #1에는 그 두 커밋도 들어 있다. `main`에 plate의 기록을 두지 않고 다음 phase가 같은 `main`에서 시작하게 하려는 것이다

## 남은 것
- 없음

## 하네스에서 걸린 것
- `~/plate-rail-test/bin/run.sh`의 run 허용 목록에 `Bash(git push:*)`가 없다. PR 단계의 푸시가 막히지 않게 세 턴 모두 `RUN_ALLOW`로 더했다
- CI 없는 run 장면의 PR 댓글을 run이 `--body "$(git show … | tail -n +3)"`로 달려다 권한 검사("Quoted text in this command can't be checked before it runs")에 막혀 `--body-file -`로 바꿔 달았다. run 본문 "PR을 연다"의 4번은 댓글을 `--body "$(cat <<'EOF' … EOF)"`로 단다고 적는다. 이번에 run은 그 꼴을 쓰지 않았다
- 시험 장면의 하네스 eval(`ci-norun`의 커밋 `c65829e`의 `docs/tasks/eval.md`)이 plate 자체의 고칠 거리 넷(retro와 plan이 PRD의 다른 절과의 어긋남을 보지 않는다, review가 `/tmp`에 쓴 측정 파일을 지우지 못한다, eval이 코드 평가의 "걸린 것"을 실패로 세어 실패 양상을 E로 매긴다, eval의 규칙 준수 표에 `NNN-slug: phase N 통과` 커밋 꼴이 없다)을 냈다. 이 장면에서는 올리지 않는다고 답했고 이 phase에서 고치지 않았다

## 확인 1

**통과 조건**
- 완료 조건 3이 참이다.
  - setup 장면의 실행 기록 → `grep -c 'CI 에이전트를 둘까요' ~/plate-rail-test/logs/ci-setup-1.jsonl` → `2`. 그 기록의 `result`에 할 일 표의 "CI 워크플로 쓰기 | `.github/workflows/plate-review.yml` | **필요**"와 "**CI 에이전트를 둘까요?**", 시크릿 `CLAUDE_CODE_OAUTH_TOKEN`이 있어야 돈다는 글이 있다. 같은 세션(`3543fa8d-…`)의 `ci-setup-2.jsonl`의 `result`에 "## CI 시크릿 등록" 절(`CLAUDE_CODE_OAUTH_TOKEN`, `claude setup-token`, `gh secret set CLAUDE_CODE_OAUTH_TOKEN`)이 있다. 통과
  - `ls -la ~/plate-rail-test/ci-setup/.github/workflows/` → `plate-review.yml`(3136바이트). 통과
  - `test ~/plate-rail-test/logs/ci-setup-1.jsonl -nt plugins/plate/skills/setup/SKILL.md`, 같은 꼴로 `ci-setup-2.jsonl` → 둘 다 참(기록 10월 24일 18:59, 19:07, 본문 10월 23일 21:55). 통과
  - run 장면의 실행 기록 → `grep -c 'PR을 열까요' ~/plate-rail-test/logs/ci-norun-2.jsonl` → `2`. 그 기록의 `result`에 "## PR을 열까요?"와 푸시할 브랜치 `tasks/line-count`, 가는 곳 `main`, 제목, 본문, plate 워크플로가 없어 `review.md`의 `## 평가 1` 절을 댓글로 단다는 글이 있다. `test ~/plate-rail-test/logs/ci-norun-2.jsonl -nt plugins/plate/skills/run/SKILL.md`, 같은 꼴로 `ci-norun-1.jsonl`, `ci-norun-3.jsonl` → 모두 참(기록 19:33, 19:36, 19:39, 본문 18:24). 세 기록의 세션은 하나(`7d44dfe9-…`)다. 통과
  - `gh pr view 1 -R werwer748/plate-ci-test --json headRefName,baseRefName,state,comments` → `headRefName` `tasks/line-count`, `baseRefName` `main`, `state` `OPEN`, 댓글 하나(작성자 `werwer748`, 첫 줄 `## 평가 1`, 그 아래 `**대상**`, "범위: `05e57bc`(main에서 갈라진 곳)부터 `5bd539a`까지"). 통과
- 시험 저장소의 `main`에 plate 워크플로가 없다.
  - `gh api repos/werwer748/plate-ci-test/contents/.github/workflows` → `{"message":"Not Found",…,"status":"404"}`, `gh: Not Found (HTTP 404)`, 종료 코드 1. 통과
- 이 phase에서 확인한 도구의 사실이 `docs/TOOLS.md`에 적혀 있다.
  - `docs/TOOLS.md`의 Claude Code 절을 읽음 → 버전 줄에 "tasks pr-ci(0.11.0)의 시험은 2.1.310(2026-10-24)"이 있고, "**setup의 CI 물음과 CI 없는 PR에서 본 것**" 묶음(97줄~)에 setup의 CI 물음과 워크플로 쓰기, PR 단계의 `Bash(git push:*)` 허용, 막힌 명령 치환과 지나간 꼴, 댓글 작성자 `werwer748`, 막힌 명령, 실행 시간이 시험 저장소 `werwer748/plate-ci-test`, 시험 폴더 `ci-src`·`ci-setup`·`ci-norun`, 스크립트 `bin/cimake.sh`·`bin/cinorun-plan.sh`·`bin/tturn.sh`, 실행 기록 `logs/ci-setup-1.jsonl`·`logs/ci-setup-2.jsonl`·`logs/ci-norun-setup.jsonl`·`logs/ci-norun-1.jsonl`~`logs/ci-norun-3.jsonl`의 위치와 함께 있다. 적힌 폴더와 스크립트는 `~/plate-rail-test` 아래에 있다. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 89 tests in 34.278s`, `OK`. 통과

**실패**
- 없음

**하네스에서 걸린 것**
- 없음

**판정**: 통과
