# Phase 11: run 일괄 끝까지와 check 세 번 실패를 시험한다

**목표**: 일괄 장면과 멈춤 장면을 돌려 완료 조건 6, 7, 8을 확인하고, 이 단계의 판정에서 확인한 도구 사실을 `docs/TOOLS.md`에 적는다. 멈춘 답과 eval 등급표를 고친 뒤 네 장면을 다시 돌려 완료 조건 3~8을 확인한다.

**테스트 먼저**: 아니오 — 이 레포에서는 `.md`(`docs/TOOLS.md`, run과 eval의 본문)만 고친다. 시험 폴더와 도구는 저장소 밖이다.

**읽을 것**
- `docs/TOOLS.md` (판정 묶음을 적는 꼴과 헤드리스 사실)
- `~/plate-rail-test/bin/` (phase 10이 바꾼 실행 도구와 시험 폴더를 만드는 도구)
- `plugins/plate/skills/run/SKILL.md`, `plugins/plate/skills/check/SKILL.md`, `plugins/plate/skills/retro/SKILL.md`, `plugins/plate/skills/review/SKILL.md`, `plugins/plate/skills/eval/SKILL.md` (기대하는 동작)

**TODO**
- [x] run 일괄 끝까지 장면이 돈다: 테스트가 있는 작은 프로젝트에 task 둘 이상의 계획을 두고, task 회고에서 문제가 나올 거리(task 머리의 완료 조건을 phase가 채우지 않는 곳)와 review가 소스 문제로 볼 거리를 미리 심는다. run을 부르고 방식은 "tasks 일괄"로 답해 끝의 보고와 물음까지 간 뒤, 소스 문제 하나는 고치고 하나는 미루고 plate 자체의 고칠 거리 하나는 이슈로 올린다고 답해 합칠지 묻는 데까지 간다
- [x] 비우기 전 상태를 되살린 폴더에서 같은 문제로 끝 단계를 다시 돌려 그 이슈에 "다시 나옴" 댓글이 달리는지 보고, 올린 이슈를 `gh issue delete`로 지운다
- [x] check 세 번 실패 장면이 돈다: 통과 조건을 채울 수 없는 phase가 든 계획에서 run을 부르고 방식은 "tasks 일괄"로 답한다
- [x] 장면의 기록이 `~/plate-rail-test/logs/`에 남는다
- [x] 완료 조건 6, 7, 8, 13의 확인을 모두 돌려 결과를 기록에 적는다
- [x] `docs/TOOLS.md`의 Claude Code 절에 이 단계의 판정 묶음이 더해진다: 에이전트 결과로 돌아오는 사용량, `gh`로 이슈 올리기·댓글·지우기, 시험 폴더와 기록 위치, 실행 시간을 날짜·버전과 함께 적는다
- [x] "멈춘다" 2번이 해결책을 하나만 내고, 다른 안이나 "멈춘다"를 고를 거리로 늘어놓지 않으며, 사용자가 다른 길을 말하면 3번에서 그때 논의한다 (`plugins/plate/skills/run/SKILL.md`)
- [x] 규칙 준수 등급표에 수행이나 확인이 자기 스킬의 읽기 범위를 어긴 것이 드는 칸이 생긴다: 하나면 C, 둘 이상이면 D (`plugins/plate/skills/eval/SKILL.md`)
- [x] 바뀐 본문으로 네 장면(phase 10의 setup·plan과 run task 하나씩, 이 phase의 run 일괄 끝까지와 다시 돌림, check 세 번 실패)을 다시 돌리고, 완료 조건 3~8과 13의 확인을 다시 돌려 결과를 기록에 적는다. 다시 올린 이슈는 확인한 뒤 지운다

**통과 조건**
- 완료 조건 3~8이 참이다
  - 확인: 여섯 완료 조건의 확인을 모두 돌린다
- 완료 조건 13이 참이다
  - 확인: 완료 조건 13의 확인을 돌린다
- 완료 조건 14가 참이다
  - 확인: 완료 조건 14의 확인을 돌린다

## 한 일
- run 일괄 끝까지 장면이 돈다: `~/plate-rail-test/bin/tasksmake.sh`에 `t-all`을 더해 만들었다. booklog(테스트가 있다)에 tasks `list-delete`(task 001-list-command의 phase 하나, 002-delete-command의 phase 하나)를 두고, 001의 task 머리 완료 조건 3(PRD의 `4. 책 목록 보기`)을 채우는 phase를 빼 회고에서 문제가 나오게 했고, `tasks/list-delete` 브랜치의 계획 앞에 `booklog stats`(`booklog/stats.py`가 DB를 직접 열고 오류를 삼키며 테스트가 없다)를 커밋해 코드 평가가 볼 거리로 심었다. 처음 판정은 네 턴(`/plate:run` → "tasks 일괄로 한다." → 고칠 안의 답 → "승인한다.")에 이슈 #1, BACKLOG, 고침 task, 비움, 합칠지 물음까지 갔다. 그 폴더는 `~/plate-rail-test/t-all-try1/`로 옮겼다 (`~/plate-rail-test/bin/tasksmake.sh`, `~/plate-rail-test/answers/t-batch.md`, `answers/t-all-3.md`)
- 비우기 전 상태를 되살린 폴더에서 같은 문제로 끝 단계를 다시 돌려 그 이슈에 "다시 나옴" 댓글이 달리는지 보고, 올린 이슈를 `gh issue delete`로 지운다: `tasksmake.sh`의 `t-again`이 `t-all`을 복사해 `list-delete: 하네스 eval` 커밋으로 되돌리고 tasks 이름과 브랜치를 `book-commands`로 바꾼다. 처음 판정은 세 턴에 #1에 댓글을 달았고(`…/issues/1#issuecomment-6249218440`) `gh issue delete 1 --repo werwer748/harness-plate --yes`로 지웠다. 그 폴더는 `t-again-try1/`로 옮겼다 (`answers/t-again-2.md`)
- check 세 번 실패 장면이 돈다: `tasksmake.sh`의 `t-stop`. tasks `prd-scope`(task 하나, phase 하나: PRD의 범위 밖에 한 줄)의 통과 조건에 프로젝트 전체 테스트를 두고, `tests/test_stamp.py`(HEAD까지의 커밋 수가 짝수여야 통과)를 더했다. 수행은 커밋 전(짝수)에 돌려 통과하고 확인은 수행의 커밋 뒤(홀수)에 돌려 실패한다. 처음 판정은 두 턴에 확인 세 번 실패로 멈췄다(1424초, 에이전트 6). 그 폴더는 `t-stop-try1/`로 옮겼다
- 장면의 기록이 `~/plate-rail-test/logs/`에 남는다: 처음 판정은 `t-all-1`~`4`, `t-again-1`~`3`, `t-stop-1`~`2`와 앞의 두 시도 `t-stop-parity-1`~`2`, `t-stop-pth-1`~`2`, 다시 돌린 판정은 `t2-setup-1`~`2`, `t2-plan-1`~`12`, `t2-plan-add`, `t2-run-1`~`3`, `t2-all-1`~`4`, `t2-again-1`~`3`, `t2-stop-1`~`2`의 `.jsonl`, `.state`, `.sid`, `.base`, `.err`
- 완료 조건 6, 7, 8, 13의 확인을 모두 돌려 결과를 기록에 적는다: 처음 판정에서 6의 셋째와 8의 둘째가 실패했다. 고친 본문으로 다시 돌린 결과를 아래 "확인 결과"에 적었다
- `docs/TOOLS.md`의 Claude Code 절에 이 단계의 판정 묶음이 더해진다: 버전 줄에 010-tasks-cycle(0.10.0)의 판정을 더하고, "tasks 실행의 판정에서 본 것" 묶음(에이전트 결과의 사용량, `gh` 이슈 올리기·댓글·지우기와 검색, 프로젝트 밖으로 돌린 출력의 승인, 숨긴 까닭을 찾아내는 확인 에이전트, 시험 폴더와 기록 위치, 실행 시간)을 2.1.302, gh 2.89.0, 2026-10-18과 함께 적었다. 다시 돌린 뒤 기록 이름(`t2-`)과 옮긴 폴더(`-try1`), 지운 이슈의 번호를 다시 쓰지 않는 것(#2), 다시 돌린 판정의 실행 시간을 더했다 (`docs/TOOLS.md`)
- "멈춘다" 2번이 해결책을 하나만 내고, 다른 안이나 "멈춘다"를 고를 거리로 늘어놓지 않으며, 사용자가 다른 길을 말하면 3번에서 그때 논의한다: 2번을 "해결책을 하나 낸다"로 바꾸고 "원인에서 끌어낸 것 가운데 가장 나은 안 하나", "다른 안이나 멈추는 길을 고를 거리로 늘어놓지 않는다", "답글은 이 해결책으로 갈지 묻는 것으로 끝낸다"를 적었다. 3번에 "사용자가 다른 길(멈추는 것도 든다)을 말하면 그때 그 길을 논의한다"를 더했다 (`plugins/plate/skills/run/SKILL.md`)
- 규칙 준수 등급표에 수행이나 확인이 자기 스킬의 읽기 범위를 어긴 것이 드는 칸이 생긴다: C 칸에 "수행이나 확인이 자기 스킬의 읽기 범위 밖을 읽은 곳"을 더했다. 하나면 C, 둘 이상이면 D 칸의 "C의 위반이 둘 이상"에 든다 (`plugins/plate/skills/eval/SKILL.md`)
- 바뀐 본문으로 네 장면을 다시 돌리고, 완료 조건 3~8과 13의 확인을 다시 돌려 결과를 기록에 적는다. 다시 올린 이슈는 확인한 뒤 지운다: 처음 판정의 폴더를 `-try1`로 옮기고 `tasksmake.sh t-setup t-plan t-run t-all t-stop`으로 다시 만들어 `bin/tturn.sh`로 돌렸다. setup·plan은 setup 두 턴(`/plate:setup` → `answers/t-setup-2.md`), plan 열두 턴(`answers/t-plan-1.md` → 물음 여덟에 추천안 `answers/t2-plan-2.md`~`9.md` → `answers/t-approve.md` 셋)과 tasks가 진행 중일 때의 새 요청 한 턴(`answers/t-plan-add.md`). run task 하나씩은 세 턴(`/plate:run` → `answers/t-run-2.md` → `answers/t-run-3.md`, 917초). run 일괄은 네 턴(`/plate:run` → `answers/t-batch.md` 4166초 → `answers/t2-all-3.md` → `answers/t-approve.md` 1773초)에 이슈 #2를 올리고 합칠지 묻는 데까지 갔고, 그 뒤 `tasksmake.sh t-again`으로 되살린 폴더에서 세 턴(`/plate:run` → `answers/t2-again-2.md` → `answers/t-approve.md`)에 #2에 "다시 나옴" 댓글을 달았다. check 세 번 실패는 두 턴(`/plate:run` → `answers/t-batch.md`, 899초). 확인한 뒤 `gh issue delete 2 --repo werwer748/harness-plate --yes` → 종료 코드 0. 결과는 아래 "확인 결과"에 적었다 (`~/plate-rail-test/t-setup/`, `t-plan/`, `t-run/`, `t-all/`, `t-again/`, `t-stop/`)

## 확인 결과
- 완료 조건 3~8이 참이다
  - 3-1: `grep -n "plate:context\|이어서 채울지\|verify" plugins/plate/skills/setup/SKILL.md` → 0줄. 통과
  - 3-2: `logs/t2-setup-1`, `t2-setup-2`의 마지막 답 → UI 물음과 만든 것의 보고뿐이고 채울지 묻는 글이 없다(`grep '?\|까요\|할지\|채우'` → "## 직접 채우실 칸" 제목 한 줄뿐). `t-setup/AGENTS.md`는 setup 본문의 문서 지도 구간에서 `docs/DESIGN.md` 행을 뺀 것, 빈 줄, 규칙 구간을 이은 것과 같다(파이썬으로 견줌 → `True`). 통과
  - 4-1: `logs/t2-plan-1`~`12`의 마지막 답 → 승인 물음이 `t2-plan-9`(tasks 머리), `t2-plan-10`(`001-book-list`), `t2-plan-11`(`002-book-delete`)에 하나씩 있다. `t2-plan-1`~`11.state`의 `git status --short`와 `ls docs/tasks` → 모두 빈 출력. 통과
  - 4-2: `t-plan`의 `git log -1 --stat` → `9b33f72 plan: list-delete`에 `docs/tasks/plan.md`(완료 조건 셋), `001-book-list/plan.md`, `phase-1.md`, `002-book-delete/plan.md`, `phase-1.md` 다섯. 통과
  - 4-3: `t-plan/docs/ARCHITECTURE.md`의 절 → 기술 스택, 디렉터리 구조, 패턴과 규칙, 데이터 흐름(명령 절 없음). `001-book-list/phase-1.md` 17줄 → "`docs/ARCHITECTURE.md`에 `## 명령` 절이 생기고 …". 통과
  - 4-4: `logs/t2-plan-add.jsonl`의 답 → "이번 요청(…)을 이 tasks에 새 task `003-…`로 더할지 정해 주세요". 통과
  - 5-1: `t-run`의 `git branch --show-current` → `tasks/list-delete`. `git log --oneline` → `50d2478 001-list-command: phase 1`, `5413ec7 … phase 1 확인`, `9aab8f4 … phase 1 통과`, `7bcb52b … phase 2`, `6e2cb4a … phase 2 확인`, `d0bd125 … phase 2 통과`, `df023bc 001-list-command: 회고`가 이 차례. 통과
  - 5-2: `ls docs/tasks/001-list-command` → `done-phase-1.md`, `done-phase-2.md`, `plan.md`, `retro.md`(`phase-N.md` 없음). 통과
  - 5-3: `t2-run-1`의 답 → "어느 방식으로 실행할까요?"와 두 방식. `t2-run-2`의 답 → "다음 task는 `002-delete-command` … 이 task로 갈까요?". 통과
  - 5-4: `docs/tasks/RUNLOG.md` → 에이전트 줄 5(줄마다 토큰, 도구 호출, 시간), 물은 줄 2(실행 방식, 다음 task). `bin/tagents.py logs/t2-run-*.jsonl` → 에이전트 5. 기록의 물음은 실행 방식과 다음 task 둘. `FRICTION.md` → `` - `001-list-command` 없음 ``. 통과
  - 6-1: `logs/t2-all-1`~`4`의 마지막 답 → 실행 방식(1), 고칠지(2, 고친 안을 다시 보이고 3), 합칠지(4). 네 기록 모두 `AskUserQuestion` 0번. 비운 커밋의 부모 `RUNLOG.md`의 물은 줄도 실행 방식 하나, 고칠지 둘. 통과
  - 6-2: `t-all`의 `git log --oneline` → `7423698 plan: 001-list-command 수정`(회고 문제로 더한 phase), `2dbe37d list-delete: 코드 평가`, `f09e5eb list-delete: 하네스 eval`, `a1c4f21 plan: 003-fixes 더함`과 그 수행·확인·회고(고침 task의 회고 문제로 더한 `d005c00 plan: 003-fixes 수정`도 묻지 않고 돌았다), `fe56a34 list-delete: 비움`이 이 차례. 통과
  - 6-3: `git show fe56a34^:docs/tasks/review.md` → 신뢰성 C, 보안 A, 유지보수성 A, 테스트 적절성 C, 기능 적합성 A, Sonar way 게이트 조건 넷의 결과와 "게이트: 실패", 범주의 근거가 파일:줄(`booklog/stats.py:12`, `booklog/store.py:50`, `tests/test_delete.py:38-44` 등 18곳). `git show fe56a34^:docs/tasks/eval.md` → 결과 성공 A, 일관성 B, 효율 C, 규칙 준수 D("수행이나 확인이 자기 스킬의 읽기 범위 밖을 읽은 곳이 셋이다(C의 위반이 둘 이상)"), 사람 개입률 A, 실패 양상 E, "스킬로 만들 후보" 절 있음. 통과
  - 6-4: `t-all/docs/BACKLOG.md` → 미룬 소스 문제 다섯, 항목마다 "나온 tasks: `list-delete`". `grep -n BACKLOG AGENTS.md` → 11줄, 문서 지도의 `docs/BACKLOG.md` 행. `ls -A docs/tasks` → `.gitkeep`. 통과
  - 7-1: `logs/t2-all-4.jsonl`의 `gh issue create --repo werwer748/harness-plate --title "plan: task 머리의 완료 조건을 맡는 phase가 없어도 계획이 그대로 쓰인다" --body "…"` → `https://github.com/werwer748/harness-plate/issues/2`. `logs/t2-again-3.jsonl`의 `gh issue comment 2 --repo werwer748/harness-plate --body-file - <<'EOF'`(첫 줄 `다시 나옴`) → `https://github.com/werwer748/harness-plate/issues/2#issuecomment-6250671472`. 지우기 전 `gh issue view 2 --comments`에 그 댓글이 있었다. 통과
  - 7-2: `gh issue view 2 --repo werwer748/harness-plate` → `GraphQL: Could not resolve to an issue or pull request with the number of 2. (repository.issue)`, 종료 코드 1. `gh issue list --state all` → `[]`. 통과
  - 8-1: `t-stop/docs/tasks/001-prd-scope/phase-1.md` → `## 확인 1`, `## 확인 2`, `## 확인 3`, 판정 셋 모두 실패. 확인 3의 커밋 `d8bafef` 뒤 `git log --format=%s d8bafef..HEAD` → 0개. 통과
  - 8-2: `logs/t2-stop-2.jsonl`의 마지막 답 → "### 원인"(확인 셋의 실패, 수행 기록의 남은 것과 하네스에서 걸린 것), "### 해결책" 하나(`--deselect`로 stamp 테스트를 빼고 바꿀 파일과 글), "이 해결책으로 진행할까요?"로 끝난다. `grep '다른 안\|다른 길\|^- [A-C]\.\|멈추는\|선택\|고르'` → 0줄. `AskUserQuestion` 0번. 통과
  - 3-3, 4-5, 5-5, 6-5, 7-3, 8-3(완료 조건 13의 확인에 이 기록이 든다): 아래 13의 결과에 `t2-setup-*`, `t2-plan-*`, `t2-run-*`, `t2-all-*`, `t2-again-*`, `t2-stop-*`가 든다. 통과
- 완료 조건 13이 참이다
  - `N=$(ls -t plugins/plate/skills/*/SKILL.md plugins/plate/hooks/*.py plugins/plate/hooks/*.json | head -1); find ~/plate-rail-test/logs -name '*.jsonl' -newer "$N"` → N은 `plugins/plate/skills/eval/SKILL.md`(20:53), 나온 기록은 `t2-setup-1`~`2`, `t2-plan-1`~`12`, `t2-plan-add`(setup·plan), `t2-run-1`~`3`(run task 하나씩), `t2-all-1`~`4`와 `t2-again-1`~`3`(run 일괄 끝까지와 다시 돌림), `t2-stop-1`~`2`(check 세 번 실패). 통과
- 완료 조건 14가 참이다
  - `docs/TOOLS.md`의 Claude Code 절을 읽음 → 버전 줄에 "010-tasks-cycle(0.10.0)의 판정은 2.1.302(2026-10-18)", "tasks 실행의 판정에서 본 것"(2.1.302, gh 2.89.0, 2026-10-18)에 에이전트 결과의 사용량(`<usage>subagent_tokens …`, `totalTokens` 등), `gh issue create`·`comment`·`delete`와 그 출력, 시험 폴더(`tasksmake.sh`의 여섯 폴더, 옮긴 `-try1`)와 기록 위치(`logs/<이름>-<턴>.jsonl`, 다시 돌린 `t2-`), 처음과 다시 돌린 판정의 실행 시간이 있다. 통과

## 계획과 달라진 점
- check 세 번 실패 장면: TODO는 "통과 조건을 채울 수 없는 phase가 든 계획"이다. 통과 조건이 수행 때부터 채워지지 않으면 수행이 스스로 막힘으로 멈춰 확인까지 가지 않으므로, 수행 때는 통과하고 확인 때 실패하게 만들었다. 첫 시도(`t-stop-parity`, 홀짝 테스트만)는 확인이 까닭을 적고 고침 수행이 "계획이 틀림"으로, 둘째 시도(`t-stop-pth`, 같은 조건을 `.venv`의 `.pth`에 숨김)는 확인이 그 파일을 찾고 고침 수행이 "막힘"으로 돌아와 둘 다 확인 한 번에 멈췄다. 그래서 셋째(`t-stop`)는 홀짝 테스트를 그대로 두고 tasks 머리와 task 머리의 결정에 "수행은 그 테스트 때문에 막힘이나 계획이 틀림으로 멈추지 않는다"를 적었다
- 다시 돌림: "같은 문제로"를 비우기 전 상태 그대로가 아니라 하네스 eval 커밋으로 되돌린 폴더의 tasks 이름을 `book-commands`로 바꿔 돌렸다. run은 같은 이슈의 본문이나 댓글에 이 tasks 이름이 이미 있으면 댓글을 달지 않는다
- run 일괄의 고칠지 답: TODO는 "소스 문제 하나는 고치고 하나는 미루고"다. 코드 평가가 소스 문제를 여럿(처음 다섯, 다시 돌린 판정 여섯) 냈으므로 1번을 고치고 나머지를 미뤘다
- 코드 평가가 볼 거리는 계획 커밋 앞에 tasks 브랜치에 커밋해 심었다(`stats 명령을 더한다`). 회고는 task의 커밋만 봐서 이것을 보지 않는다
- 네 장면을 다시 돌릴 때 처음 판정의 기록을 덮어쓰지 않으려고 기록 이름을 `t2-`로 시작하게 하고, 처음 판정의 폴더는 `-try1`을 붙여 옮겼다. 처음 판정을 가리키는 아래 "하네스에서 걸린 것"의 기록 경로(`logs/t-stop-*` 등)는 그대로 있다
- plan 장면의 물음이 phase 10의 기록과 달랐다(물음 다섯에 번호 → 물음 여덟에 A·B·C). 그래서 phase 10의 답 파일(`answers/t-plan-2.md`~`6.md`)을 쓰지 않고, 물음마다 추천안을 고르는 답 파일(`answers/t2-plan-2.md`~`9.md`)을 새로 썼다. 엣지케이스 물음에는 phase 10처럼 정하지 않는다고 답했다
- TODO의 `docs/TOOLS.md` 항목은 처음 판정 뒤에 체크됐지만, 다시 돌린 뒤 그 묶음에 기록 이름, 옮긴 폴더, 이슈 번호, 실행 시간을 더했다. 처음 판정의 사실은 고치지 않았다

## 남은 것
- 없음

## 하네스에서 걸린 것
- 막힘: 완료 조건 8의 둘째 확인(멈춘 답이 고를 선택지 목록을 내지 않는다)이 실패하고, 고치려면 run 스킬 본문을 고쳐야 해서 이 phase에서 풀 수 없다. 완료 조건 6의 셋째 확인도 eval의 규칙 준수가 "판단 못함"이라 글 그대로는 실패다
- plate:run "멈춘다": "정해 둔 선택지를 내지 않는다"가 있어도 세 번의 멈춤 모두 다른 안을 늘어놓았다. "해결책을 낸다"와 "논의한다"만으로는 하나만 내라는 뜻이 서지 않는다
- plate:run "이슈를 올린다" 1: `gh issue list --search "{이슈 제목의 낱말}"`에 낱말을 여럿 주면 있는 이슈가 나오지 않았다(`--search "plan 완료 조건 phase 통과 조건"` → `[]`, `--search "완료 조건"` → #1). 다시 돌린 run은 열린 이슈를 모두 나열해 찾았다
- plate:eval 규칙 준수 등급표: 수행이 읽기 범위(tasks 머리를 읽지 않는다)를 어긴 것이 A~E 어느 칸에도 들지 않아 "판단 못함"이 됐다
- plate:review: 코드 평가 에이전트가 커버리지를 `/tmp/booklog-review-cov`에 만들고 지우지 못했다. 허용된 명령도 출력을 프로젝트 밖으로 돌리면 승인을 요구한다
- 이 phase의 TODO "통과 조건을 채울 수 없는 phase": 확인을 세 번 실패시키려면 수행 때는 통과해야 한다. 확인과 수행 에이전트가 까닭을 찾아내 멈추므로, 계획의 결정으로 수행에게 멈추지 말라고 적어야 했다
- 이 phase의 TODO "네 장면(phase 10의 setup·plan과 run task 하나씩 …)을 다시 돌리고": plate:phase 1번 "다른 phase의 파일은 읽지 않는다" 때문에 phase 10이 장면을 어떻게 돌렸는지 그 기록에서 읽을 수 없었다(phase 10의 파일은 지워졌다). `~/plate-rail-test/logs/t-setup-*`, `t-plan-*`, `t-run-*`의 `.state`와 마지막 답, `answers/`의 답 파일로 차례를 되짚었다
- plan을 헤드리스로 여러 턴 돌리는 장면은 물음의 수와 꼴이 실행마다 달라, 앞 판정의 답 파일을 다시 쓸 수 없다. 턴마다 답을 읽고 답 파일을 새로 써야 했다
- 다시 돌린 `t-all`에서 고침 task `003-fixes`의 회고 1이 `docs/BACKLOG.md`(문서 지도에 행이 생겨 맥락 문서가 됐다)의 항목이 고친 코드와 맞지 않는다고 문제로 적었고, run이 묻지 않고 더한 고칠 phase(`d005c00`)의 수행이 BACKLOG의 그 항목 글을 고쳤다(`99764ec`). plate:run 절대 규칙 5는 BACKLOG를 run이 고치는 파일로 두는데, 맥락 문서로 보는 회고와 수행도 고치게 된다
- 다시 돌린 하네스 eval이 plate 자체의 고칠 거리를 아홉 냈다(`t-all`의 `f09e5eb:docs/tasks/eval.md`). TODO대로 1번만 이슈로 올렸고 지웠다. 나머지 여덟(완료 조건을 맡는 phase가 없는 것을 수행과 확인이 기록만 하고 통과시킴, 확인을 참조로 적는 계획, 거짓이어도 통과하는 확인, 고칠 phase의 읽을 것에 든 phase 파일, 회고가 한 원인을 두 문제로 적음, 코드 평가의 임시 사본을 막는 편집 막이 훅, 계획 커밋 앞의 계획 없는 커밋, eval의 더한 phase 정의와 규칙 준수 표)은 그 기록에만 있다

## 회고 1: 확인만

**확인**
- 완료 조건 3~8이 참이다
  - 3-1: `grep -n "plate:context\|이어서 채울지\|verify" plugins/plate/skills/setup/SKILL.md` → 0줄(종료 코드 1). 통과
  - 3-2: `bin/summ.py logs/t2-setup-1.jsonl`, `t2-setup-2.jsonl`의 마지막 답 → UI 물음과 만든 것·옮긴 것·건드리지 않은 것·"직접 채우실 칸"의 보고뿐이고 채울지 묻는 글이 없다. setup 본문 111~123줄(문서 지도 구간)에서 `docs/DESIGN.md` 행을 뺀 것 + 빈 줄 + 131~137줄(규칙 구간)을 `~/plate-rail-test/t-setup/AGENTS.md`와 파이썬으로 견줌 → `True`. 통과
  - 4-1: `logs/t2-plan-1`~`12`의 마지막 답에서 "승인하시나요" → `t2-plan-9`(tasks 머리, `## task 목록`이 든 초안), `t2-plan-10`(`001-book-list`), `t2-plan-11`(`002-book-delete`)에 하나씩, 나머지 0. `t2-plan-1`~`11.state`의 `git status --short`와 `ls docs/tasks` → 모두 빈 출력. 통과
  - 4-2: `t-plan`의 `git log -1 --stat` → `9b33f72 plan: list-delete`에 `docs/tasks/plan.md`, `001-book-list/plan.md`, `001-book-list/phase-1.md`, `002-book-delete/plan.md`, `002-book-delete/phase-1.md` 다섯 파일. `docs/tasks/plan.md`의 완료 조건 절에 조건 셋. 통과
  - 4-3: `grep -n '^## ' t-plan/docs/ARCHITECTURE.md` → 기술 스택, 디렉터리 구조, 패턴과 규칙, 데이터 흐름(명령 절 없음). `001-book-list/phase-1.md`의 TODO 첫 항목 → "`docs/ARCHITECTURE.md`에 `## 명령` 절이 생기고 …". 통과
  - 4-4: `logs/t2-plan-add.jsonl`의 답 → 진행 중인 tasks `list-delete`를 말하고 "이번 요청(…)을 이 tasks에 새 task `003-…`로 더할지 정해 주세요". 그 턴의 `.state`에 새 파일 없음. 통과
  - 5-1: `t-run`에서 `git branch --show-current` → `tasks/list-delete`. `git log --oneline` → `50d2478 001-list-command: phase 1`, `5413ec7 … phase 1 확인`, `9aab8f4 … phase 1 통과`, `7bcb52b … phase 2`, `6e2cb4a … phase 2 확인`, `d0bd125 … phase 2 통과`, `df023bc 001-list-command: 회고`가 이 차례. 통과
  - 5-2: `ls docs/tasks/001-list-command` → `done-phase-1.md`, `done-phase-2.md`, `plan.md`, `retro.md`. 통과
  - 5-3: `t2-run-1`의 답 → "어느 방식으로 실행할까요?"와 두 방식. `t2-run-2`의 답 → 회고 통과 보고 뒤 "다음 task는 **`002-delete-command`** … 이 task로 갈까요?". 통과
  - 5-4: `t-run/docs/tasks/RUNLOG.md` → 에이전트 줄 5(줄마다 토큰, 도구 호출, 시간), 물음 줄 2(실행 방식, 다음 task). `bin/tagents.py logs/t2-run-*.jsonl` → 에이전트 5(phase·check 둘씩, retro 하나). 기록의 물음은 `t2-run-1`, `t2-run-2`의 둘. `FRICTION.md` → `` - `001-list-command` 없음 ``. 통과
  - 6-1: `logs/t2-all-1`~`4`의 마지막 답 → 실행 방식(1), 고칠 안대로 할지(2), 고친 안대로 할지(3), 합칠지(4). 네 기록 모두 `AskUserQuestion` 0번. `git show fe56a34^:docs/tasks/RUNLOG.md`의 물음 줄 → 실행 방식 하나, 고칠지 둘. 통과
  - 6-2: `t-all`의 `git log --oneline` → `7423698 plan: 001-list-command 수정`(`001-list-command/phase-2.md`를 더함)과 그 phase의 `d821abb`·`2a03c8e`·`6418c59`, `2dbe37d list-delete: 코드 평가`, `f09e5eb list-delete: 하네스 eval`, `a1c4f21 plan: 003-fixes 더함`과 `003-fixes`의 수행·확인·통과·회고 커밋, `fe56a34 list-delete: 비움`이 이 차례. 통과
  - 6-3: `git show fe56a34^:docs/tasks/review.md` → 신뢰성 C, 보안 A, 유지보수성 A, 테스트 적절성 C, 기능 적합성 A, Sonar way 게이트 조건 넷과 "게이트: 실패", 범주의 근거마다 파일:줄(`booklog/stats.py:12`, `booklog/store.py:50`, `tests/test_delete.py:38-44` 등). `git show fe56a34^:docs/tasks/eval.md` → 결과 성공 A, 일관성 B, 효율 C, 규칙 준수 D("수행이나 확인이 자기 스킬의 읽기 범위 밖을 읽은 곳이 셋이다(C의 위반이 둘 이상)"), 사람 개입률 A, 실패 양상 E, `**스킬로 만들 후보**` 절에 후보 둘. 통과
  - 6-4: `t-all/docs/BACKLOG.md` → 미룬 소스 문제 다섯, 항목마다 "나온 tasks: `list-delete`". `grep -n BACKLOG AGENTS.md` → 11줄, 문서 지도의 `docs/BACKLOG.md` 행. `ls -A docs/tasks` → `.gitkeep`. 통과
  - 7-1: `bin/calls.py logs/t2-all-4.jsonl` → `gh issue create --repo werwer748/harness-plate --title "plan: task 머리의 완료 조건을 맡는 phase가 없어도 계획이 그대로 쓰인다" --body "…"` → `https://github.com/werwer748/harness-plate/issues/2`. `bin/calls.py logs/t2-again-3.jsonl` → `gh issue comment 2 --repo werwer748/harness-plate --body-file - <<'EOF'`(첫 줄 `다시 나옴`) → `…/issues/2#issuecomment-6250671472`. 통과
  - 7-2: `gh issue view 2 --repo werwer748/harness-plate` → `GraphQL: Could not resolve to an issue or pull request with the number of 2. (repository.issue)`, 종료 코드 1. 처음 판정의 #1도 같은 오류, 종료 코드 1. `gh issue list --state all` → `[]`. 통과
  - 8-1: `t-stop/docs/tasks/001-prd-scope/phase-1.md` → `## 확인 1`, `## 확인 2`, `## 확인 3`, 판정 셋 모두 `실패`. `git log --format=%s d8bafef..HEAD` → 0줄(`d8bafef`는 확인 3의 커밋이고 HEAD). 통과
  - 8-2: `logs/t2-stop-2.jsonl`의 마지막 답 → "### 원인"(확인 셋의 같은 두 실패, 수행 기록의 남은 것과 하네스에서 걸린 것), "### 해결책" 하나(`--deselect`로 stamp 테스트를 빼고 바꿀 곳), "이 해결책으로 진행할까요?"로 끝난다. `grep -c '다른 안\|다른 길\|^- [A-C]\.\|멈추는\|선택\|고르'` → 0. `AskUserQuestion` 0번. 통과
  - 3-3, 4-5, 5-5, 6-5, 7-3, 8-3: 아래 완료 조건 13의 결과에 `t2-setup-*`, `t2-plan-*`, `t2-run-*`, `t2-all-*`, `t2-again-*`, `t2-stop-*`가 든다. 통과
- 완료 조건 13이 참이다
  - `N=$(ls -t plugins/plate/skills/*/SKILL.md plugins/plate/hooks/*.py plugins/plate/hooks/*.json | head -1); find ~/plate-rail-test/logs -name '*.jsonl' -newer "$N"` → N은 `plugins/plate/skills/eval/SKILL.md`(10월 18 20:53). 나온 기록은 `t2-setup-1`~`2`, `t2-plan-1`~`12`, `t2-plan-add`, `t2-run-1`~`3`, `t2-all-1`~`4`, `t2-again-1`~`3`, `t2-stop-1`~`2`로 네 장면이 모두 든다. 통과
- 완료 조건 14가 참이다
  - `docs/TOOLS.md`의 Claude Code 절(17줄, 86~92줄)을 읽음 → 버전 줄에 "010-tasks-cycle(0.10.0)의 판정은 2.1.302(2026-10-18)", "tasks 실행의 판정에서 본 것"(2.1.302, gh 2.89.0, 2026-10-18)에 에이전트 결과의 사용량(`<usage>subagent_tokens …`, `totalTokens` 등), `gh issue create`·`comment`·`delete`와 그 출력, 시험 폴더(`tasksmake.sh`의 여섯 폴더, `-try1`)와 기록 위치(`logs/<이름>-<턴>.jsonl`, `t2-`), 처음과 다시 돌린 판정의 실행 시간. 통과

**문제**
- 없음

**판정**: 통과
