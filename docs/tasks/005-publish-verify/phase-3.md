# Phase 3: CI의 세 판정

**목표**: 시험 저장소의 `main`에 plate 복사본과 CI 워크플로가 있고, 세 판정의 PR과 run이 연 PR에서 CI가 평가서를 달고 판정대로 한다.

**테스트 먼저**: 아니오 — 시험 저장소에서 워크플로를 돌려 보고, 이 저장소에서는 `docs/TOOLS.md`만 고친다

**읽을 것**
- `docs/TOOLS.md`의 Claude Code 절 (헤드리스 실행과 세션 잇기, "tasks 실행의 판정에서 본 것"의 시험 폴더와 실행 스크립트)
- `plugins/plate/skills/setup/SKILL.md`의 양식 절 (CI 워크플로)
- `plugins/plate/skills/review/SKILL.md`의 PR 모드 절 (등급 묶음의 꼴)
- 판정 스크립트와 그 테스트 (`docs/ARCHITECTURE.md`의 디렉터리 구조에 경로가 있다. 세 규칙의 경계)
- `plugins/plate/skills/run/SKILL.md` (tasks 끝의 PR 절)
- `plugins/plate/hooks/hooks.json`과 거기에 걸린 푸시 훅 (셋업된 폴더에서 기본 브랜치로 하는 푸시를 막는다)
- https://code.claude.com/docs/en/github-actions (설정, 시크릿, `claude_args`)
- https://raw.githubusercontent.com/anthropics/claude-code-action/main/action.yml (입력과 `structured_output`)

**TODO**
- [x] 시험 저장소의 `main`에 `plugins/plate`의 복사본과 CI 워크플로가 생긴다. 워크플로는 setup 양식에서 plate를 받는 곳만 그 복사본을 쓰도록 바꾼 것이다. `main`을 새로 받아 복사본을 `diff -r <복사본> plugins/plate`로 견주면 아무것도 나오지 않는다 (`werwer748/plate-ci-test`)
- [x] 세 판정의 장면: 판정마다 그 판정이 나오게 바꾼 PR을 시험 저장소에 연다. CI가 PR마다 평가서를 댓글로 달고, 자동 머지 장면의 PR은 `MERGED`, 머지 요청 장면은 `OPEN`, 닫기 장면은 `CLOSED`가 된다. 세 PR의 CI는 `main`의 복사본을 마지막으로 바꾼 뒤에 돈다
- [x] CI 있는 run 장면: 시험 저장소를 origin으로 둔 셋업된 시험 폴더에서 작은 tasks를 계획해 run을 끝까지 돌리면, tasks 끝에 PR을 열지 묻는다. 승인하면 `tasks/`로 시작하는 브랜치에서 `main`으로 가는 PR이 열리고, run은 평가서 댓글을 달지 않으며 CI가 단다. 실행 기록은 run 본문을 마지막으로 고친 뒤에 만든다
- [x] 이 phase의 기록에 장면마다 PR 번호가, run 장면에는 시험 폴더와 실행 기록의 경로도 적힌다 (`docs/tasks/005-publish-verify/phase-3.md`)
- [x] 이 phase에서 확인한 도구의 사실(claude-code-action의 동작, 워크플로가 댓글을 달고 머지하고 닫는 꼴)이 시험 저장소와 실행 기록의 위치와 함께 적힌다 (`docs/TOOLS.md`)

**통과 조건**
- 완료 조건 4가 참이다.
  - 확인: 완료 조건 4의 확인을 모두 돌린다. `done-phase-3.md`는 이름이 바뀌기 전인 이 파일로 읽는다
- 이 phase에서 확인한 도구의 사실이 `docs/TOOLS.md`에 적혀 있다.
  - 확인: `docs/TOOLS.md`의 Claude Code 절을 읽어 이 phase의 장면에서 본 것이 시험 저장소와 실행 기록의 위치와 함께 있다

## 한 일
- 시험 저장소의 `main`에 `plugins/plate`의 복사본과 CI 워크플로가 생긴다: `~/plate-rail-test/bin/cimain.sh`가 `ci-src`(시험 저장소의 `main`을 만든 폴더)에 harness-plate에서 추적되는 `plugins/plate`의 파일 15개를 `.plate/`로 옮기고, setup 본문의 양식에서 뽑은 워크플로를 `.github/workflows/plate-review.yml`로 써서 `plate 복사본과 CI 워크플로`(`e67df4b`, 2026-10-24T19:51:08+09:00)로 커밋했다. `git -C ~/plate-rail-test/ci-src push origin main`으로 올렸다(`ae98f75..e67df4b`). 워크플로가 양식과 다른 곳은 넷이다: 맨 위에 `plate@harness-plate`가 든 주석 한 줄, review 잡에서 `plugin_marketplaces`·`plugins` 두 줄을 빼고 `claude_args`에 `--plugin-dir ${{ github.workspace }}/.plate`, verdict 잡의 checkout에서 `repository: werwer748/harness-plate` 대신 `ref: ${{ github.base_ref }}`, 판정 스크립트 경로 `harness-plate/.plate/ci/verdict.py`. 새로 받은 `main`의 `.plate`를 `diff -r`로 `plugins/plate`에 견주면 아무것도 나오지 않는다 (`werwer748/plate-ci-test`, `~/plate-rail-test/ci-src`, `~/plate-rail-test/bin/cimain.sh`)
- 세 판정의 장면: `~/plate-rail-test/bin/civerdict.sh merge request close`가 `ci-verdict-merge`, `ci-verdict-request`, `ci-verdict-close`에 시험 저장소를 복제해 브랜치를 푸시하고 PR을 열었다. 자동 머지 장면은 #2(`is-blank`: 결함 없는 `is_blank`와 그 테스트), 머지 요청 장면은 #3(`avg-word-length`: 테스트는 통과하지만 빈 글에서 `ZeroDivisionError`가 나는 `average_word_length`), 닫기 장면은 #4(`sentence-count`: 새 테스트가 실패하는 `sentence_count`)다. 처음 CI(실행 `40087608281`, `40087613376`, `40087621740`, 생성 10:52:06Z~10:52:18Z)는 시크릿의 OAuth 토큰이 폐기돼 모두 실패했다(까닭은 `show_full_output: true`를 켠 진단 PR #5로 찾았고 #5는 닫았다). 사용자가 새 토큰을 시크릿으로 넣은 뒤(2026-10-24T11:05:45Z) `gh run rerun <실행> -R werwer748/plate-ci-test`로 세 실행을 다시 돌렸다. 등급 묶음과 결과는 #2 `{"build":"none","lint":"none","test":"pass","coverage":"skipped","reliability":"A","security":"A","maintainability":"A"}` → 자동 머지, `MERGED`(머지 커밋 `2e308d4`, 머리 브랜치 지워짐), #3 `{…,"test":"pass","coverage":"unmeasured","reliability":"C",…}` → 머지 요청, `OPEN`, #4 `{…,"test":"fail","coverage":"skipped","reliability":"D",…}` → 닫기, `CLOSED`다. 셋 모두 `github-actions`가 `판정: <라벨>`으로 시작하는 평가서 댓글을 달았다. CI 로그는 `~/plate-rail-test/logs/ci-runs/<실행 id>.log`에 받았다
- CI 있는 run 장면: `cimake.sh ci-run`으로 #2가 머지된 `main`(`2e308d4`)을 `~/plate-rail-test/ci-run`에 복제하고, `tturn.sh ci-run setup ci-run-setup`으로 setup을 돌렸다(plate 워크플로가 있어 CI를 묻지 않았다). 새로 쓴 `~/plate-rail-test/bin/cirun-plan.sh`가 setup의 변경을 `셋업`으로 커밋하고 tasks `unique-words`(task `001-unique-words`, phase 하나, 테스트 먼저. `unique_word_count`와 PRD의 `4. 서로 다른 낱말 세기`)의 계획 파일을 `plan: unique-words`로 커밋했다. `RUN_ALLOW='Bash(git push:*)|Bash(git remote:*)'`로 run을 세 턴 돌렸다: tasks 일괄(1671초, 에이전트 5, 고칠지 물음에서 멈춤), "아무것도 고치지 않고 이슈도 올리지 않는다"(137초, BACKLOG·RUNLOG·비움 커밋 뒤 PR 물음에서 멈춤), "승인한다"(47초). 둘째 턴의 물음에 "PR을 열까요?"와 "`.github/workflows/plate-review.yml`이 있어서 그 워크플로가 PR을 평가하고 평가서를 댓글로 답니다"가 있다. 셋째 턴에서 run은 `git push origin tasks/unique-words`와 `gh pr create`만 하고 `gh pr comment`는 하지 않았다. 열린 PR은 #6(`tasks/unique-words` → `main`)이고, CI(실행 `40091269096`)가 자동 머지로 판정해 평가서 댓글을 달고 머지했다
- 이 phase의 기록에 장면마다 PR 번호를 적는다: 자동 머지 #2, 머지 요청 #3, 닫기 #4, CI 있는 run #6. run 장면의 시험 폴더는 `~/plate-rail-test/ci-run`, 실행 기록은 `~/plate-rail-test/logs/ci-run-setup.jsonl`, `~/plate-rail-test/logs/ci-run-1.jsonl`, `~/plate-rail-test/logs/ci-run-2.jsonl`(PR 물음), `~/plate-rail-test/logs/ci-run-3.jsonl`(PR을 연 턴)이다 (`docs/tasks/005-publish-verify/phase-3.md`)
- `docs/TOOLS.md`: Claude Code 절의 "setup의 CI 물음과 CI 없는 PR에서 본 것" 뒤에 "CI의 세 판정과 CI 있는 PR에서 본 것"을 더했다. 시험 저장소, 스크립트, 시험 폴더, 기록과 CI 로그의 위치와 함께 시험 워크플로가 양식과 다른 곳, `--plugin-dir`가 CLI로 넘어가는 것, 액션이 설정 경로(`CLAUDE.md` 등)를 기준 브랜치의 것으로 되돌리는 것, `show_full_output` 없이는 인증 실패가 보이지 않는 것, `gh run rerun`이 `createdAt`를 바꾸지 않는 것, 잡의 시간과 비용, 세 판정의 댓글·머지·닫기의 꼴, 커버리지 게이트가 갈린 것, CI 있는 run이 댓글을 달지 않은 것, `__pycache__`가 생기는 까닭, 실행 시간을 적었다 (`docs/TOOLS.md`)

## 확인 결과
- 완료 조건 4가 참이다.
  - `gh pr view <번호> -R werwer748/plate-ci-test --json state,comments` → #2 `MERGED`, #3 `OPEN`, #4 `CLOSED`. 셋 모두 댓글 하나이고 작성자 `github-actions`, 첫 줄이 차례로 `판정: 자동 머지`, `판정: 머지 요청`, `판정: 닫기`, 셋째 줄이 `# 코드 평가`인 평가서다. 통과
  - 시험 저장소를 scratchpad에 새로 복제(`91b8060`)해 `diff -r <받은 폴더>/.plate plugins/plate` → 출력 없음, 종료 코드 0(그 앞에 git이 무시하는 `plugins/plate/hooks/__pycache__`와 `plugins/plate/ci/__pycache__`를 지웠다). `git log -1 --format=%cI -- .plate` → `2026-10-24T19:51:08+09:00`(10:51:08Z). `gh run list -R werwer748/plate-ci-test --json headBranch,createdAt` → `is-blank` 10:52:06Z, `avg-word-length` 10:52:11Z, `sentence-count` 10:52:18Z로 모두 그 뒤다. 통과
  - run 장면의 실행 기록 `~/plate-rail-test/logs/ci-run-2.jsonl`의 결과 글에 "PR을 열까요?"와 "이대로 푸시하고 PR을 열까요?"가 있다. `test ~/plate-rail-test/logs/ci-run-2.jsonl -nt plugins/plate/skills/run/SKILL.md` → 참(`ci-run-1.jsonl`, `ci-run-3.jsonl`도 참. run 본문은 18:24, 기록은 20:43~20:47). 통과
  - `gh pr view 6 -R werwer748/plate-ci-test --json headRefName,baseRefName,comments` → 머리 브랜치 `tasks/unique-words`, 기준 브랜치 `main`, 댓글 작성자는 `github-actions` 하나뿐이고 `werwer748`의 댓글은 0개, 그 댓글의 첫 줄은 `판정: 자동 머지`이고 평가서가 이어진다. 통과
- 이 phase에서 확인한 도구의 사실이 `docs/TOOLS.md`에 적혀 있다.
  - `docs/TOOLS.md`의 Claude Code 절을 읽음 → "CI의 세 판정과 CI 있는 PR에서 본 것"에 이 phase의 장면(세 판정, 진단 PR, 다시 돌린 실행, CI 있는 run)에서 본 것이 시험 저장소 `werwer748/plate-ci-test`, 스크립트(`bin/cimain.sh`, `bin/civerdict.sh`, `bin/cimake.sh`, `bin/cirun-plan.sh`), 기록(`logs/ci-run-setup.jsonl`, `logs/ci-run-1.jsonl`~`logs/ci-run-3.jsonl`, `logs/ci-runs/<실행 id>.log`)의 위치와 함께 있다. 통과

## 계획과 달라진 점
- TODO 1은 워크플로를 "plate를 받는 곳만" 바꾼다고 적는다. 그 밖에 맨 위에 `plate@harness-plate`가 든 주석 한 줄을 더했다. run과 setup은 `.github/workflows/` 아래에 `plate@harness-plate`가 적힌 파일을 plate 워크플로로 보는데(run의 낱말 "plate 워크플로", setup의 1번), 받는 곳의 `plugins: "plate@harness-plate"` 줄을 빼면 그 글이 없어져 CI 있는 run 장면에서 run이 워크플로가 없다고 보고 평가서 댓글을 단다
- verdict 잡은 복사본을 PR의 머지 커밋이 아니라 기준 브랜치(`ref: ${{ github.base_ref }}`)에서 받는다. 양식이 PR 밖(harness-plate 저장소)의 판정 스크립트를 쓰는 것처럼 PR이 바꾼 판정 스크립트가 판정에 쓰이지 않게 했다. 복사본의 자리는 계획에 없어서 `.plate/`로 정했다
- 계획에 없는 진단 PR #5를 열고 닫았다. 세 PR의 CI가 까닭 없이 실패해 결과 글을 보려면 `show_full_output`을 켠 워크플로로 돌려야 했다
- 세 판정의 CI는 새 PR이 아니라 `gh run rerun`으로 다시 돌렸다. 다시 돌린 실행의 `createdAt`는 처음 그대로라 "복사본을 마지막으로 바꾼 뒤에 돈다"가 그대로 맞는다
- CI 있는 run 장면의 "작은 tasks를 계획해"는 plan 스킬을 부르지 않고 `cirun-plan.sh`가 계획 파일을 손으로 써서 했다. phase 2의 CI 없는 run 장면(`cinorun-plan.sh`)과 같은 방식이다. tasks 이름은 phase 2의 PR #1이 `tasks/line-count`를 쓰고 있어 `unique-words`로 했다
- `plugins/plate/hooks/__pycache__`와 `plugins/plate/ci/__pycache__`(git이 무시하는 파일)를 두 번 지웠다. 있으면 `diff -r <복사본> plugins/plate`가 `Only in plugins/plate/…: __pycache__`를 낸다

## 남은 것
- 없음

## 하네스에서 걸린 것
- 막힘: 시험 저장소의 시크릿의 OAuth 토큰이 폐기됐다(`Failed to authenticate: OAuth token revoked. Please log in again or contact your administrator.`, 401). 시크릿은 사용자만 만들 수 있어 수행 에이전트가 풀 수 없다. 원하는 해결책: 사용자가 `claude setup-token`으로 새 토큰을 만들어 시크릿으로 넣는다
- setup 양식의 워크플로는 claude-code-action의 `show_full_output`을 켜지 않아서, 대상 프로젝트에서도 토큰이 잘못되면 로그에는 `--json-schema was provided but Claude did not return structured_output`만 남고 까닭(인증 실패)이 보이지 않는다
- 막힘이면 커밋하지 않으므로 `docs/TOOLS.md`를 지금 고치지 않았다. 커밋하지 않은 `docs/TOOLS.md`는 run의 1번에서 "커밋하지 않은 변경"으로 물음이 되고, 진행하면 그 변경은 어느 커밋에도 들지 않는다. 그래서 확인한 사실은 이 기록에 두었다
- 완료 조건 4의 `diff -r <복사본> plugins/plate`는 `plugins/plate` 안에 git이 무시하는 `__pycache__`가 없을 때만 아무것도 내지 않는다. 테스트 명령(`python3 -m unittest discover -s tests`)을 돌리면 `push_guard.py`가 `edit_guard`를 불러오면서 `plugins/plate/hooks/__pycache__/edit_guard.cpython-313.pyc`가 생겨, 그 뒤의 `diff -r`는 `Only in plugins/plate/hooks: __pycache__`를 낸다(이 phase에서 테스트를 돌려 봤다). 확인할 때 그 폴더를 지우거나 테스트보다 먼저 견준다
- 이 세션은 `--plugin-dir plugins/plate`로 plate를 실어 푸시 훅이 돈다. 시험 저장소의 `main`으로 하는 푸시는 셋업되지 않은 `ci-src`에서 `git -C <폴더> push origin main`으로 했다. 같은 호출의 `cd` 뒤 push는 훅이 호출한 폴더(셋업된 harness-plate)에서 본다(`docs/ARCHITECTURE.md`)
- 이어 한 수행: 시험 폴더에서 `--plugin-dir`로 이 레포의 `plugins/plate`를 실은 헤드리스 세션(`ci-run`의 setup과 run)이 Bash를 부를 때도 푸시 훅이 `plugins/plate/hooks/__pycache__`를 만든다. 지운 뒤 시험을 돌리면 다시 생기므로, `diff -r`는 시험을 다 돌린 뒤 지우고 견준다
- review 스킬 6번의 커버리지 게이트는 "새 줄이 20줄 미만이면 보지 않음"과 "커버리지가 측정 못함이면 측정 못함"이 함께 맞을 때 어느 쪽인지 정하지 않는다. CI에서 11줄인 #3은 `"unmeasured"`, 11줄인 #4와 16줄인 #2는 `"skipped"`를 냈다. 판정 스크립트는 `"unmeasured"`를 머지 요청으로 보내므로, 세 등급이 A인 작은 PR도 이 갈림에 따라 자동 머지가 머지 요청이 될 수 있다
- claude-code-action은 PR의 `CLAUDE.md`, `.claude` 등을 기준 브랜치의 것으로 되돌린다. 셋업 커밋이 든 PR(#6)에서는 기준 브랜치에 `CLAUDE.md`가 없어 PR 모드 review가 `CLAUDE.md`가 지워진 작업 트리를 보고 "하네스에서 걸린 것"에 적었다. `AGENTS.md`는 남아 평가에는 영향이 없었다
- run이 연 PR #6의 본문 끝에 run의 "PR 본문의 꼴"에 없는 `🤖 Generated with [Claude Code](https://claude.com/claude-code)` 줄이 붙었다. 실행 환경의 기본 안내가 스킬의 꼴보다 앞섰다
- 시험 폴더의 셋업 커밋과 계획 커밋이 로컬 `main`에만 있어서 run의 PR에 그 두 커밋이 들어갔고, `ci-run`의 하네스 eval이 tasks 모드 review의 갈라진 곳(로컬 `main`과 `origin/main` 가운데 어느 쪽인지)을 plate 자체의 고칠 거리로 적었다(`ci-run`의 커밋 `bb5dada`의 `docs/tasks/eval.md`). 시험에서는 이슈로 올리지 않았다
