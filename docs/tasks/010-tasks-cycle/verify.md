# 검증

## 검증 1

**확인**
- 스킬은 아홉(setup, context, plan, run, phase, check, retro, review, eval)이고 verify는 없다.
  - `ls plugins/plate/skills` → `check`, `context`, `eval`, `phase`, `plan`, `retro`, `review`, `run`, `setup` 아홉만. 통과
- 스킬, 훅, README, 맥락 문서, 이 레포의 `AGENTS.md`가 tasks, task, phase를 결정의 뜻대로 쓴다.
  - `grep -n "작업" plugins/plate/skills/*/SKILL.md plugins/plate/hooks/edit_guard.py README.md docs/PRD.md docs/ARCHITECTURE.md AGENTS.md` → 10줄. 모두 읽었다: context:8 "다음 작업의 근거"(일반의 일), edit_guard.py:23 "작업 트리"(git의 working tree), AGENTS.md:16과 setup:132 "## 작업 규칙", setup:3과 setup:10 "작업 규칙"(규칙 구간의 이름), PRD:4 "작업하게 하는"과 "작업 규칙", PRD:7 "그 프로젝트의 모든 작업", PRD:24 "모든 작업이 파이프라인을 거친다"(일반의 일), ARCHITECTURE:36 "작업 디렉터리". tasks, task, phase를 가리키는 "작업"은 없다. 통과
  - 낱말 절이 있는 스킬(check, context, eval, phase, plan, retro, review, run)의 절을 `awk`로 뽑아 읽음 → tasks는 요청 하나를 계획한 묶음이고 `docs/tasks/`에 하나, task(task 폴더)는 `NNN-slug/` 폴더 하나, phase는 task 안의 `phase-N.md` 하나(통과하면 `done-phase-N.md`), tasks 머리는 제목·이름·여섯 절, task 머리는 제목·네 절로 결정과 같다. context의 낱말 절에는 그 정의가 없다. 통과
- setup은 설치만 하고 끝 물음 없이 끝나며, 넣는 문서 지도의 `docs/tasks/` 행과 규칙 구간이 새 구조와 새 스킬을 말한다.
  - `grep -n "plate:context\|이어서 채울지\|verify" plugins/plate/skills/setup/SKILL.md` → 0줄(종료 코드 1). 통과
  - `~/plate-rail-test/logs/t2-setup-1.jsonl`, `t2-setup-2.jsonl`의 마지막 답 → 1턴은 화면이 있는지 묻는 물음, 2턴은 만든 것·옮긴 것·건드리지 않은 것·직접 채우실 칸·`AGENTS.md` 크기의 보고로 끝나고 채울지 묻는 글이 없다. setup 본문의 문서 지도 구간에서 `docs/DESIGN.md` 행을 뺀 것 + 빈 줄 + 규칙 구간을 `~/plate-rail-test/t-setup/AGENTS.md`와 python으로 견줌 → `equal: True`. 통과
  - 완료 조건 13의 `find`에 `t2-setup-1.jsonl`, `t2-setup-2.jsonl`이 나온다. 통과
- plan은 tasks 머리를 먼저, 그다음 task마다 머리와 phase를 승인받아 모두 받은 뒤 한꺼번에 쓰고 한 커밋으로 넣는다. tasks가 진행 중이면 지금 tasks에 더할지 묻는다. ARCHITECTURE에 명령 절이 없으면 첫 task의 첫 phase TODO에 그 절을 쓰는 일을 넣는다.
  - `logs/t2-plan-1`~`12.jsonl`의 마지막 답에서 "승인하시나요"와 `쓸 위치:`를 셈(python) → `t2-plan-9`(`docs/tasks/plan.md`), `t2-plan-10`(`docs/tasks/001-book-list/`), `t2-plan-11`(`docs/tasks/002-book-delete/`)에 하나씩, 나머지 0. `AskUserQuestion` 0번. `t2-plan-1`~`11.state`의 `git status --short`와 `ls docs/tasks` → 모두 빈 출력. 통과
  - `~/plate-rail-test/t-plan`에서 `git log -1 --stat` → `9b33f72 plan: list-delete`에 `docs/tasks/plan.md`, `001-book-list/plan.md`, `001-book-list/phase-1.md`, `002-book-delete/plan.md`, `002-book-delete/phase-1.md` 다섯 파일. `docs/tasks/plan.md`의 완료 조건 절에 조건 셋과 확인이 있다. 통과
  - 그 폴더에서 `grep -n '^## ' docs/ARCHITECTURE.md` → 기술 스택, 디렉터리 구조, 패턴과 규칙, 데이터 흐름. `grep -c '^## 명령'` → `0`. `docs/tasks/001-book-list/phase-1.md`의 TODO 첫 항목이 `` `docs/ARCHITECTURE.md`에 `## 명령` 절이 생기고 … `` 다. 통과
  - `logs/t2-plan-add.jsonl`의 마지막 답 → 진행 중인 tasks `list-delete`를 알리고 "이번 요청(…)을 이 tasks에 새 task `003-…`로 더할지 정해 주세요". `t2-plan-add.state` → `git status --short` 빈 출력, `git log` 맨 위 `9b33f72`. 통과
  - 완료 조건 13의 `find`에 `t2-plan-1`~`12.jsonl`, `t2-plan-add.jsonl`이 나온다. 통과
- run은 시작할 때 실행 방식을 묻고, `tasks/<이름>` 브랜치에서 phase마다 수행과 check를 새 에이전트에게 맡기고, 통과한 phase를 `done-phase-N.md`로 바꾸고, task의 phase가 모두 통과하면 task 회고를 맡긴다. task 하나씩이면 회고 뒤에 묻는다. `RUNLOG.md`에는 에이전트마다, 물은 자리마다 한 줄이 쌓이고 `FRICTION.md`에는 회고가 적은 줄이 있다.
  - `~/plate-rail-test/t-run`에서 `git branch --show-current` → `tasks/list-delete`. `git log --oneline --reverse` → `7235214 plan: list-delete` 뒤에 `50d2478 001-list-command: phase 1`, `5413ec7 … phase 1 확인`, `9aab8f4 … phase 1 통과`, `7bcb52b … phase 2`, `6e2cb4a … phase 2 확인`, `d0bd125 … phase 2 통과`, `df023bc 001-list-command: 회고`가 이 차례. 통과
  - `ls -A docs/tasks/001-list-command` → `done-phase-1.md`, `done-phase-2.md`, `plan.md`, `retro.md`. `phase-N.md`가 없다. 통과
  - `logs/t2-run-1.jsonl`의 답 → "어느 방식으로 실행할까요?"와 task 하나씩, tasks 일괄. `t2-run-2.jsonl`의 답 → 회고 통과 보고 뒤 "다음 task는 `002-delete-command`: 책 지우기 명령입니다(phase 1개). 이 task로 갈까요?". 통과
  - `docs/tasks/RUNLOG.md` → 에이전트 줄 5(줄마다 토큰, 도구 호출, 시간), 물음 줄 2(실행 방식, 다음 task). `python3 bin/tagents.py logs/t2-run-1.jsonl logs/t2-run-2.jsonl logs/t2-run-3.jsonl` → `= 모두: 에이전트 5`, 줄마다의 토큰·도구 호출·시간이 RUNLOG의 다섯 줄과 같다. 기록의 물음은 `t2-run-1`, `t2-run-2`의 둘이고 `t2-run-3`에는 없다. `docs/tasks/FRICTION.md` → `` - `001-list-command` 없음 ``. 통과
  - 완료 조건 13의 `find`에 `t2-run-1`~`3.jsonl`이 나온다. 통과
- tasks 일괄은 묻지 않고 모든 task를 처리하고, 회고에서 나온 문제는 고칠 phase를 더해 고친다. 모든 task가 끝나면 review와 eval을 맡겨 전체 보고를 하고 고칠지 한 번에 묻는다. 고치면 고침 task를 더해 같은 레일로 돌리고, 미룬 소스 문제를 `docs/BACKLOG.md`에 적고, `docs/tasks/`를 비운 뒤 합칠지 묻는다.
  - `logs/t2-all-1`~`4.jsonl`의 마지막 답 → 실행 방식(1), 고칠 안대로 할지(2), 고친 안대로 할지(3), `tasks/list-delete`를 `main`에 합칠지(4). 네 기록 모두 `AskUserQuestion` 0번. 물은 자리는 실행 방식, 고칠지, 합칠지 셋뿐이다. 통과
  - `~/plate-rail-test/t-all`의 `git log --oneline --reverse` → `7423698 plan: 001-list-command 수정`(회고 문제로 더한 phase)과 그 phase의 `d821abb`, `2a03c8e`, `6418c59`, `2dbe37d list-delete: 코드 평가`, `f09e5eb list-delete: 하네스 eval`, `a1c4f21 plan: 003-fixes 더함`과 `003-fixes`의 수행·확인·통과·회고 커밋, `fe56a34 list-delete: 비움`이 이 차례. 통과
  - `git show fe56a34^:docs/tasks/review.md` → 신뢰성 C, 보안 A, 유지보수성 A, 테스트 적절성 C, 기능 적합성 A, Sonar way 게이트 조건 넷의 결과와 "게이트: 실패", 판단 항목의 근거마다 파일:줄(`booklog/stats.py:12`, `booklog/store.py:50`, `tests/test_delete.py:38-44` 등). `git show fe56a34^:docs/tasks/eval.md` → 결과 성공 A, 일관성 B, 효율 C, 규칙 준수 D, 사람 개입률 A, 실패 양상 E와 "스킬로 만들 후보" 절(후보 둘). 통과
  - `t-all/docs/BACKLOG.md` → 미룬 소스 문제 다섯, 항목마다 "나온 tasks: `list-delete`". `grep -n BACKLOG AGENTS.md` → 11줄, 문서 지도의 `docs/BACKLOG.md` 행. `ls -A docs/tasks` → `.gitkeep`. 통과
  - 완료 조건 13의 `find`에 `t2-all-1`~`4.jsonl`이 나온다. 통과
- plate 자체의 고칠 거리는 묻고 GitHub 이슈로 올리며, 같은 이슈가 있으면 "다시 나옴" 댓글을 단다. 시험에서 올린 이슈는 확인한 뒤 지운다.
  - `logs/t2-all-4.jsonl`의 `gh issue create --repo werwer748/harness-plate --title "plan: task 머리의 완료 조건을 맡는 phase가 없어도 계획이 그대로 쓰인다" --body "…"` → `https://github.com/werwer748/harness-plate/issues/2`. `logs/t2-again-3.jsonl`의 `gh issue comment 2 --repo werwer748/harness-plate --body-file - <<'EOF'`(첫 줄 `다시 나옴`) → `https://github.com/werwer748/harness-plate/issues/2#issuecomment-6250671472`. 통과
  - `gh issue view 2 --repo werwer748/harness-plate` → `GraphQL: Could not resolve to an issue or pull request with the number of 2. (repository.issue)`, 종료 코드 1. 처음 판정의 #1도 같은 오류, 종료 코드 1. `gh issue list --state all` → `[]`. 통과
  - 완료 조건 13의 `find`에 `t2-all-4.jsonl`, `t2-again-1`~`3.jsonl`이 나온다. 통과
- 일괄 방식에서도 같은 phase의 check가 세 번 실패하면 멈추고, 정해 둔 선택지 대신 원인과 해결책을 보이고 논의한다.
  - `~/plate-rail-test/t-stop/docs/tasks/001-prd-scope/phase-1.md` → `## 확인 1`, `## 확인 2`, `## 확인 3`, 판정 셋 모두 `실패`. 확인 3의 커밋 `d8bafef`가 HEAD이고 `git log d8bafef..HEAD` → 0개. 통과
  - `logs/t2-stop-2.jsonl`의 마지막 답 → "### 원인"(확인 셋의 같은 두 실패, 수행 기록의 남은 것과 하네스에서 걸린 것), "### 해결책" 하나(`--deselect`로 stamp 테스트를 빼고 바꿀 파일과 글), "이 해결책으로 진행할까요?"로 끝나고 고를 선택지 목록이 없다. 통과
  - 완료 조건 13의 `find`에 `t2-stop-1`, `t2-stop-2.jsonl`이 나온다. 통과
- 훅이 새 구조에서 돈다: `phase-N.md`가 있는 task가 없으면 코드 편집을 막고, `done-phase-N.md`만 있는 task는 끝난 task이고, 막는 글이 새 낱말을 쓰며, `task/NNN-slug` 브랜치와 `.worktrees/` 규칙이 없다.
  - `python3 -m unittest discover -s tests` → `Ran 39 tests`, 마지막 줄 `OK`. 통과
  - `grep -n 'task/\|\.worktrees' plugins/plate/hooks/edit_guard.py` → 0줄(종료 코드 1). 통과
  - `grep -c 'done-phase' tests/test_edit_guard.py` → `3`. 통과
- 맥락 문서, README, 이 레포의 `AGENTS.md`가 새 흐름을 말한다.
  - `grep -n "verify\|LESSONS\|worktree" docs/PRD.md docs/ARCHITECTURE.md README.md AGENTS.md` → 0줄(종료 코드 1). 통과
  - `diff <(sed -n '/<!-- plate:rules:start -->/,/<!-- plate:rules:end -->/p' AGENTS.md) <(sed -n '/<!-- plate:rules:start -->/,/<!-- plate:rules:end -->/p' plugins/plate/skills/setup/SKILL.md)` → 출력 없음(종료 코드 0). 통과
  - `grep -hF '| `docs/tasks/' AGENTS.md plugins/plate/skills/setup/SKILL.md | sort -u | wc -l` → `1`. 통과
  - `grep -c "^## 명령" docs/ARCHITECTURE.md` → `1`. 그 절 → `- 빌드: 없음`, `- 린트: 없음`, ``- 테스트: `python3 -m unittest discover -s tests` ``. 통과
  - `docs/PRD.md`와 `docs/ARCHITECTURE.md` 전체를 읽음 → PRD 핵심 기능 5(task 회고, `retro.md`, `FRICTION.md`), 7(두 실행 방식과 멈추는 자리), 8(다섯 범주와 여섯 기준의 A~E, Sonar way, 고칠지 묻기, 고침 task, ADR-020의 이슈, `docs/BACKLOG.md`, 011의 PR·CI), ARCHITECTURE의 디렉터리 구조(아홉 스킬), 패턴과 규칙(새 규칙 구간, `tasks/<이름>` 브랜치, 비운 뒤 합칠지 묻기), 데이터 흐름(셋업 → 맥락 → 계획 → 실행 → tasks 끝)이 아홉 스킬과 새 흐름을 말한다. 통과
- `docs/ADR.md`에 GitHub 이슈를 하네스 고칠 거리를 모으는 외부 서비스로 쓴다는 항목이 있다.
  - `grep -n "^### ADR-020" docs/ADR.md` → `28:### ADR-020: plate 자체의 고칠 거리는 GitHub 이슈로 모은다` 1줄. 항목을 읽음 → 결정(`gh`로 `werwer748/harness-plate`에 이슈, "다시 나옴" 댓글, `gh` 실패 때 보고하고 잇기), 이유, 트레이드오프가 있다. 통과
- 두 매니페스트의 버전이 0.10.0이고 설명이 아홉 스킬을 말한다.
  - `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `  "version": "0.10.0",`. 통과
  - 두 매니페스트의 `description`을 읽음 → setup, context, plan, run, phase, check, retro, review, eval 아홉 스킬이 있고 verify가 없다. 통과
- 시험 장면 넷의 기록은 바뀐 본문으로 만든 것이다.
  - `N=$(ls -t plugins/plate/skills/*/SKILL.md plugins/plate/hooks/*.py plugins/plate/hooks/*.json | head -1); find ~/plate-rail-test/logs -name '*.jsonl' -newer "$N"` → N은 `plugins/plate/skills/eval/SKILL.md`(10월 18 20:53). 나온 기록은 `t2-setup-1`~`2`, `t2-plan-1`~`12`, `t2-plan-add`(setup·plan), `t2-run-1`~`3`(run task 하나씩), `t2-all-1`~`4`와 `t2-again-1`~`3`(run 일괄 끝까지와 그 다시 돌림), `t2-stop-1`~`2`(check 세 번 실패)로 네 장면이 모두 든다. 기록의 `init`에서 plate의 경로가 `/Users/gangjungi/Desktop/harness-plate/plugins/plate`다. 통과
- `docs/TOOLS.md`에 이 단계의 판정에서 확인한 사실이 있다.
  - `docs/TOOLS.md`의 Claude Code 절을 읽음 → 버전 줄에 "010-tasks-cycle(0.10.0)의 판정은 2.1.302(2026-10-18)", "tasks 실행의 판정에서 본 것"(2.1.302, gh 2.89.0, 2026-10-18)에 에이전트 결과의 사용량(`<usage>subagent_tokens …`, `totalTokens` 등), `gh issue create`·`comment`·`delete`와 그 출력, 시험 폴더(`tasksmake.sh`의 여섯 폴더, `-try1`)와 기록 위치(`logs/<이름>-<턴>.jsonl`, `t2-`), 처음과 다시 돌린 판정의 실행 시간이 있다. 통과
- 프로젝트 전체 테스트가 모두 통과한다.
  - `python3 -m unittest discover -s tests` → 마지막 줄 `OK`. 통과
- 테스트 먼저 기록: phase 9
  - `git show c93d110^:docs/tasks/010-tasks-cycle/phase-9.md`의 "한 일" 테스트 먼저 항목 → 실패 출력(`FAIL: test_branch_does_not_pick_task …`, `FAIL: test_plan_first_message_says_task …`, `FAIL: test_non_code_files_pass …`, `Ran 39 tests`, `FAILED (failures=3)`) 뒤에 통과 출력(`Ran 39 tests`, `OK`)이 이 순서로 있다. 통과

**문제**
- 하네스 eval의 낱말 "더한 phase"는 "메시지가 `plan:`으로 시작하는 커밋이 만들지 않은 phase"인데(`eval/SKILL.md` 36줄), 실행은 회고의 문제를 고칠 phase를 `plan: NNN-slug 수정`으로(`run/SKILL.md` 172줄), 고침 task의 phase를 `plan: NNN-fixes 더함`으로(345줄) 커밋한다. 글대로 따르면 실행이 더한 phase가 늘 0개라 eval 절 "대상"의 더한 phase 수와 효율의 되풀이 줄(`eval/SKILL.md` 117줄)이 틀린다. 시험 장면의 eval 1이 이 어긋남을 적고, 글대로면 되풀이 몫이 11.9%(B)라 낱말의 둘째 문장을 따라 C로 매겼다고 했다(`~/plate-rail-test/t-all`의 `f09e5eb:docs/tasks/eval.md` "하네스에서 걸린 것" 첫 줄) (`plugins/plate/skills/eval/SKILL.md`, `plugins/plate/skills/run/SKILL.md`). 기준: 결함
- 실행이 쓰는 고칠 phase와 고침 task의 꼴이 수행에게 읽지 않는다는 파일을 읽게 한다. 고칠 phase의 읽을 것에 "{문제에 적힌 파일의 경로}"(`run/SKILL.md` 185줄)를 옮기면 회고가 근거로 든 `done-phase-N.md`가 들어가고, 고침 task 머리의 마지막 완료 조건의 확인이 "`docs/tasks/plan.md`의 그 완료 조건에 적힌 확인을 모두 돌린다"(374~375줄)라 `phase-1.md`의 통과 조건(399~401줄)을 돌리려면 tasks 머리를 읽어야 한다. 수행 스킬 1번은 tasks 머리와 다른 phase의 파일을 읽지 않는다고 하고(`phase/SKILL.md` 34줄), 하네스 eval은 수행이나 확인이 읽기 범위 밖을 읽은 곳을 규칙 준수 C·D로 센다(`eval/SKILL.md` 152~153줄). 시험 장면 `t-all`에서 `7423698`이 만든 `001-list-command/phase-2.md`의 읽을 것에 `done-phase-1.md`가 들었고, `003-fixes`의 수행과 확인이 `docs/tasks/plan.md`를 읽었다고 적었다(`fe56a34^`의 `003-fixes/done-phase-1.md`, `done-phase-2.md` "하네스에서 걸린 것") (`plugins/plate/skills/run/SKILL.md`). 기준: 결함
- `docs/TOOLS.md` 21줄이 스킬을 `/plate:setup`, `/plate:context`, `/plate:plan`, `/plate:run`, `/plate:phase`, `/plate:retro`, `/plate:verify`로 부른다고 적는다. 이 tasks가 verify를 없애고 check, review, eval을 더했는데 그 줄이 그대로다 (`docs/TOOLS.md`). 기준: 맥락 문서

**배운 것**
- 시험 장면(`t-all`, `t-again`, `t-stop`, `t-run`)의 계획은 `~/plate-rail-test/bin/tasksmake.sh`가 손으로 쓴 것이다(예: 319~320줄, 353줄의 tasks 머리를 가리키는 확인). 그래서 `t-all`의 eval 1이 plan과 run 탓으로 적은 고칠 거리 1, 3, 4, 8(완료 조건을 맡는 phase가 없음, 확인을 참조로 적음, 거짓이어도 통과하는 확인, 계획 앞의 계획 없는 커밋)과 그것으로 올린 이슈 #1, #2는 심어 둔 것에서 나왔다. 본문의 규칙에서 나온 2, 5, 6, 7, 9는 이슈로 올리지 않아 `~/plate-rail-test/t-all`의 `f09e5eb:docs/tasks/eval.md`에만 있다.
- `plugins/plate/skills/context/SKILL.md` 32줄에 setup을 부를 때 "setup의 끝 물음(이어서 채울지)은 하지 않는다"가 남았다. 결정대로 context는 고치지 않았고 그 물음이 없어져 동작에는 걸리지 않는다.

**하네스의 문제점**
- 계획의 완료 조건 3~8은 시험 장면의 결과(물음, 커밋, 파일, 등급이 있는지)만 보고, 에이전트가 기록의 "하네스에서 걸린 것"에 적은 본문끼리의 어긋남은 보지 않는다. 문제 1, 2는 시험 기록에 적혀 있었고(완료 조건 6의 셋째 확인이 본 `eval.md`의 효율 C도 낱말을 글과 달리 세어 매긴 것이다) 확인을 지났다.
- 계획의 완료 조건 2와 10의 첫 확인이 grep하는 파일에 맥락 문서 `docs/TOOLS.md`가 없어, 문제 3의 옛 스킬 목록을 보지 못했다.
- phase 12가 이 레포 `AGENTS.md`의 문서 지도 `docs/tasks/` 행과 규칙 구간을 새 구조(retro, review, eval)로 바꿔, 결정대로 0.9.1의 plate:verify로 닫는 010에 맞는 행과 규칙이 없다. `verify.md`는 그 행의 내용에 없지만 위치 `docs/tasks/`가 표에 있어 묻지 않고 썼다. 이 검증 세션에 실린 지침은 바꾸기 전의 `AGENTS.md`(verify 규칙)였다.

**판정**: 문제 있음

## 검증 2

**확인**
- 스킬은 아홉(setup, context, plan, run, phase, check, retro, review, eval)이고 verify는 없다.
  - `ls plugins/plate/skills` → `check`, `context`, `eval`, `phase`, `plan`, `retro`, `review`, `run`, `setup` 아홉만. 통과
- 스킬, 훅, README, 맥락 문서, 이 레포의 `AGENTS.md`가 tasks, task, phase를 결정의 뜻대로 쓴다.
  - `grep -n "작업" plugins/plate/skills/*/SKILL.md plugins/plate/hooks/edit_guard.py README.md docs/PRD.md docs/ARCHITECTURE.md AGENTS.md` → 10줄. 모두 읽었다: context:8 "다음 작업의 근거", edit_guard.py:23 "작업 트리"(git의 working tree), AGENTS.md:16과 setup:132 "## 작업 규칙", setup:3과 setup:10 "작업 규칙", PRD:4 "작업하게 하는"과 "작업 규칙", PRD:7 "모든 작업", PRD:24 "모든 작업이", ARCHITECTURE:36 "작업 디렉터리". tasks, task, phase를 가리키는 "작업"은 없다. 통과
  - 낱말 절이 있는 스킬(check, context, eval, phase, plan, retro, review, run)의 절을 `awk`로 뽑아 읽음 → tasks는 요청 하나를 계획한 묶음으로 `docs/tasks/`에 하나, task는 `NNN-slug/` 폴더 하나, phase는 task 안의 `phase-N.md` 하나(통과하면 `done-phase-N.md`), tasks 머리는 제목·이름·여섯 절, task 머리는 제목·네 절로 결정과 같다. context의 낱말 절에는 그 정의가 없다. 통과
- setup은 설치만 하고 끝 물음 없이 끝나며, 넣는 문서 지도의 `docs/tasks/` 행과 규칙 구간이 새 구조와 새 스킬을 말한다.
  - `grep -n "plate:context\|이어서 채울지\|verify" plugins/plate/skills/setup/SKILL.md` → 0줄(종료 코드 1). 통과
  - `~/plate-rail-test/logs/t3-setup-1.jsonl`의 마지막 답은 화면이 있는지 묻는 물음, `t3-setup-2.jsonl`은 만든 것·옮긴 것·건드리지 않은 것·채워야 할 칸·`AGENTS.md` 크기의 보고로 끝나고 채울지 묻는 글이 없다. setup 본문의 문서 지도 구간에서 `docs/DESIGN.md` 행을 뺀 것 + 빈 줄 + 규칙 구간을 `~/plate-rail-test/t-setup/AGENTS.md`와 python으로 견줌 → `equal: True`. 통과
  - 완료 조건 13의 `find`에 `t3-setup-1`, `t3-setup-2.jsonl`이 나온다. 통과
- plan은 tasks 머리를 먼저, 그다음 task마다 머리와 phase를 승인받아 모두 받은 뒤 한꺼번에 쓰고 한 커밋으로 넣는다. tasks가 진행 중이면 지금 tasks에 더할지 묻는다. ARCHITECTURE에 명령 절이 없으면 첫 task의 첫 phase TODO에 그 절을 쓰는 일을 넣는다.
  - `logs/t3-plan-1`~`12.jsonl`의 마지막 답에서 승인 물음과 `쓸 위치:`를 셈(python) → `t3-plan-9`(`docs/tasks/plan.md`), `t3-plan-10`(`docs/tasks/001-list-command/`), `t3-plan-11`(`docs/tasks/002-delete-command/`)에 승인 물음이 하나씩, 1~8은 물음 1~8번, 12는 쓴 뒤의 보고. `AskUserQuestion` 0번. `t3-plan-1`~`11.state`의 `git status --short`와 `ls docs/tasks` → 모두 빈 출력, 맨 위 `6712617 셋업 직후`. 통과
  - `~/plate-rail-test/t-plan`에서 `git log -1 --stat` → `536e55f plan: list-delete`에 `docs/tasks/plan.md`, `001-list-command/plan.md`·`phase-1.md`, `002-delete-command/plan.md`·`phase-1.md` 다섯 파일. `docs/tasks/plan.md`의 완료 조건 절에 조건 넷과 확인이 있다. 통과
  - 그 폴더에서 `grep -n '^## ' docs/ARCHITECTURE.md` → 기술 스택, 디렉터리 구조, 패턴과 규칙, 데이터 흐름. `grep -c '^## 명령'` → `0`. `001-list-command/phase-1.md`의 TODO 첫 항목이 `` `docs/ARCHITECTURE.md`에 `## 명령` 절이 생기고 … `` 다. 통과
  - `logs/t3-plan-add.jsonl`의 마지막 답 → 진행 중인 tasks `list-delete`를 알리고 "`booklog rename <번호> <새 제목>` 요청을 이 tasks에 세 번째 task(`003-...`)로 더할까요?". `t3-plan-add.state` → `git status --short` 빈 출력, 맨 위 `536e55f`. 통과
  - 완료 조건 13의 `find`에 `t3-plan-1`~`12.jsonl`, `t3-plan-add.jsonl`이 나온다. 통과
- run은 시작할 때 실행 방식을 묻고, `tasks/<이름>` 브랜치에서 phase마다 수행과 check를 새 에이전트에게 맡기고, 통과한 phase를 `done-phase-N.md`로 바꾸고, task의 phase가 모두 통과하면 task 회고를 맡긴다. task 하나씩이면 회고 뒤에 묻는다. `RUNLOG.md`에는 에이전트마다, 물은 자리마다 한 줄이 쌓이고 `FRICTION.md`에는 회고가 적은 줄이 있다.
  - `~/plate-rail-test/t-run`에서 `git branch --show-current` → `tasks/list-delete`. `git log --oneline --reverse` → `d36da69 plan: list-delete` 뒤에 `722691a … phase 1`, `8c8375c … phase 1 확인`, `7306065 … phase 1 통과`, `8c5c4ac … phase 2`, `948b005 … phase 2 확인`, `603f33c … phase 2 통과`, `8edcb8a 001-list-command: 회고`가 이 차례. 통과
  - `ls -A docs/tasks/001-list-command` → `done-phase-1.md`, `done-phase-2.md`, `plan.md`, `retro.md`. `phase-N.md`가 없다. 통과
  - `logs/t3-run-1.jsonl`의 답 → task 하나씩과 tasks 일괄을 보이고 "어느 방식으로 할까요?". `t3-run-2.jsonl`의 답 → 회고 통과 보고 뒤 "다음 task인 `002-delete-command`(책 지우기 명령)로 갈까요?". 통과
  - 작업 트리의 `docs/tasks/RUNLOG.md` → 에이전트 줄 5(줄마다 토큰, 도구 호출, 시간), 물은 줄 2(실행 방식, 다음 task). 마지막 두 줄은 커밋되지 않았고 `t3-run-3`의 답이 실행 스킬의 규칙대로 뒤의 커밋에 넣는다고 적었다. `python3 -I bin/tagents.py logs/t3-run-1.jsonl logs/t3-run-2.jsonl logs/t3-run-3.jsonl` → `= 모두: 에이전트 5`, 다섯 줄의 토큰·도구 호출·시간이 RUNLOG의 다섯 줄과 같다. 기록의 물음은 `t3-run-1`, `t3-run-2`의 둘이다. `docs/tasks/FRICTION.md` → `` `001-list-command` 문제: `` 줄 둘. 통과
  - 완료 조건 13의 `find`에 `t3-run-1`~`3.jsonl`이 나온다. 통과
- tasks 일괄은 묻지 않고 모든 task를 처리하고, 회고에서 나온 문제는 고칠 phase를 더해 고친다. 모든 task가 끝나면 review와 eval을 맡겨 전체 보고를 하고 고칠지 한 번에 묻는다. 고치면 고침 task를 더해 같은 레일로 돌리고, 미룬 소스 문제를 `docs/BACKLOG.md`에 적고, `docs/tasks/`를 비운 뒤 합칠지 묻는다.
  - `logs/t3-all-1`~`4.jsonl`의 마지막 답 → 실행 방식(1), 고칠 안대로 할지(2), 고친 안대로 할지(3), `tasks/list-delete`를 `main`에 합칠지(4). 네 기록 모두 `AskUserQuestion` 0번. 물은 자리는 실행 방식, 고칠지, 합칠지 셋뿐이다. 통과
  - `~/plate-rail-test/t-all`의 `git log --oneline --reverse` → `16bc67e plan: 001-list-command 수정`(회고 문제로 더한 phase)과 그 phase의 `1bf1244`, `995960a`, `aafa62a`, `2e0c6a6 list-delete: 코드 평가`, `dfee9c3 list-delete: 하네스 eval`, `90bba05 plan: 003-fixes 더함`과 `5b69deb`, `9851a0c`, `adbe284`, `908661e`, `44f58ed list-delete: 비움`이 이 차례. 통과
  - `git show '44f58ed^:docs/tasks/review.md'` → 신뢰성 C, 보안 A, 유지보수성 A, 테스트 적절성 C, 기능 적합성 C, Sonar way 게이트 조건 넷의 결과와 "게이트: 실패", 판단 항목의 근거마다 파일:줄(`booklog/stats.py:12-13`, `booklog/stats.py:8-9`, `booklog/cli.py:62-65`, `tests/test_delete.py:39-45` 등). `git show '44f58ed^:docs/tasks/eval.md'` → 결과 성공 D, 일관성 B, 효율 C, 규칙 준수 D, 사람 개입률 A, 실패 양상 E와 "스킬로 만들 후보" 절. 통과
  - `t-all/docs/BACKLOG.md` → 미룬 소스 문제 다섯, 항목마다 "나온 tasks: `list-delete`". `grep -n BACKLOG AGENTS.md` → 11줄, 문서 지도의 `docs/BACKLOG.md` 행. `ls -A docs/tasks` → `.gitkeep`. 통과
  - 완료 조건 13의 `find`에 `t3-all-1`~`4.jsonl`이 나온다. 통과
- plate 자체의 고칠 거리는 묻고 GitHub 이슈로 올리며, 같은 이슈가 있으면 "다시 나옴" 댓글을 단다. 시험에서 올린 이슈는 확인한 뒤 지운다.
  - `logs/t3-all-4.jsonl`의 `gh issue create --repo werwer748/harness-plate --title "plan: task 머리의 완료 조건 가운데 어느 phase도 맡지 않는 것이 생긴다" --body "…"` → `https://github.com/werwer748/harness-plate/issues/3`. `logs/t3-again-3.jsonl`의 `gh issue comment 3 --repo werwer748/harness-plate --body-file - <<'EOF'`(첫 줄 `다시 나옴`) → `https://github.com/werwer748/harness-plate/issues/3#issuecomment-6263627265`. 통과
  - `gh issue view 3 --repo werwer748/harness-plate` → `GraphQL: Could not resolve to an issue or pull request with the number of 3. (repository.issue)`, 종료 코드 1. 앞 판정의 #2도 같은 오류, 종료 코드 1. `gh issue list --state all --json number` → `[]`. 통과
  - 완료 조건 13의 `find`에 `t3-all-4.jsonl`, `t3-again-1`~`3.jsonl`이 나온다. 통과
- 일괄 방식에서도 같은 phase의 check가 세 번 실패하면 멈추고, 정해 둔 선택지 대신 원인과 해결책을 보이고 논의한다.
  - `~/plate-rail-test/t-stop/docs/tasks/001-prd-scope/phase-1.md` → `## 확인 1`, `## 확인 2`, `## 확인 3`, 판정 셋 모두 `실패`. HEAD가 확인 3의 커밋 `b734b35`이고 그 뒤 커밋이 없다(작업 트리에 커밋하지 않은 `RUNLOG.md`만). `RUNLOG.md`의 실행 방식 답은 `tasks 일괄`. 통과
  - `logs/t3-stop-2.jsonl`의 마지막 답 → "## 원인"(확인 셋의 실패와 커밋 수 표), "## 해결책" 하나(`--deselect`로 stamp 테스트를 빼고 바꿀 파일과 글), "이 해결책으로 갈까요?"로 끝나고 고를 선택지 목록이 없다. 통과
  - 완료 조건 13의 `find`에 `t3-stop-1`, `t3-stop-2.jsonl`이 나온다. 통과
- 훅이 새 구조에서 돈다: `phase-N.md`가 있는 task가 없으면 코드 편집을 막고, `done-phase-N.md`만 있는 task는 끝난 task이고, 막는 글이 새 낱말을 쓰며, `task/NNN-slug` 브랜치와 `.worktrees/` 규칙이 없다.
  - `python3 -m unittest discover -s tests` → `Ran 39 tests`, 마지막 줄 `OK`. 통과
  - `grep -n 'task/\|\.worktrees' plugins/plate/hooks/edit_guard.py` → 0줄(종료 코드 1). 통과
  - `grep -c 'done-phase' tests/test_edit_guard.py` → `3`. 통과
- 맥락 문서, README, 이 레포의 `AGENTS.md`가 새 흐름을 말한다.
  - `grep -n "verify\|LESSONS\|worktree" docs/PRD.md docs/ARCHITECTURE.md README.md AGENTS.md` → 0줄(종료 코드 1). 통과
  - 규칙 구간의 `diff`(두 파일 모두 표시 줄이 있다) → 출력 없음(종료 코드 0). 통과
  - `grep -hF '| `docs/tasks/' AGENTS.md plugins/plate/skills/setup/SKILL.md | sort -u | wc -l` → `1`. 통과
  - `grep -c "^## 명령" docs/ARCHITECTURE.md` → `1`. 그 절 → `- 빌드: 없음`, `- 린트: 없음`, ``- 테스트: `python3 -m unittest discover -s tests` ``. 통과
  - `docs/PRD.md`와 `docs/ARCHITECTURE.md` 전체를 읽음 → PRD 핵심 기능 5(task 회고, `retro.md`, `FRICTION.md`), 7(두 실행 방식과 멈추는 자리), 8(다섯 범주와 여섯 기준의 A~E, Sonar way, 고칠지 묻기, 고침 task, ADR-020, `docs/BACKLOG.md`), ARCHITECTURE의 디렉터리 구조(아홉 스킬), 패턴과 규칙(규칙 구간, `tasks/<이름>` 브랜치, 비운 뒤 합칠지 묻기), 데이터 흐름(셋업 → 맥락 → 계획 → 실행 → tasks 끝)이 아홉 스킬과 새 흐름을 말한다. 통과
- `docs/ADR.md`에 GitHub 이슈를 하네스 고칠 거리를 모으는 외부 서비스로 쓴다는 항목이 있다.
  - `grep -n "^### ADR-020" docs/ADR.md` → `28:### ADR-020: plate 자체의 고칠 거리는 GitHub 이슈로 모은다` 1줄. 항목을 읽음 → 결정, 이유, 트레이드오프가 있다. 통과
- 두 매니페스트의 버전이 0.10.0이고 설명이 아홉 스킬을 말한다.
  - `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `  "version": "0.10.0",`. 통과
  - 두 매니페스트의 `description`을 읽음 → setup, context, plan, run, phase, check, retro, review, eval 아홉 스킬이 있고 verify가 없다. 통과
- 시험 장면 넷의 기록은 바뀐 본문으로 만든 것이다.
  - `N=$(ls -t plugins/plate/skills/*/SKILL.md plugins/plate/hooks/*.py plugins/plate/hooks/*.json | head -1); find ~/plate-rail-test/logs -name '*.jsonl' -newer "$N"` → N은 `plugins/plate/skills/run/SKILL.md`(10월 19 16:28, `git status` 깨끗). 나온 기록은 `t3-setup-1`~`2`, `t3-plan-1`~`12`, `t3-plan-add`(setup·plan), `t3-run-1`~`3`(run task 하나씩), `t3-all-1`~`4`와 `t3-again-1`~`3`(run 일괄 끝까지와 그 다시 돌림), `t3-stop-1`~`2`(check 세 번 실패)로 네 장면이 모두 든다. 기록의 init에서 plate는 `/Users/gangjungi/Desktop/harness-plate/plugins/plate`, 0.10.0이고 Claude Code는 2.1.303이다. 통과
- `docs/TOOLS.md`에 이 단계의 판정에서 확인한 사실이 있다.
  - `docs/TOOLS.md`의 Claude Code 절을 읽음 → 버전 줄에 2.1.302(2026-10-18)와 2.1.303(2026-10-19), "tasks 실행의 판정에서 본 것"(2.1.302, gh 2.89.0, 2026-10-18)에 에이전트 결과의 사용량(`<usage>subagent_tokens …`, `totalTokens` 등), `gh issue create`·`comment`·`delete`와 그 출력, 시험 폴더(`tasksmake.sh`의 여섯 폴더, `-try1`, `-try2`)와 기록 위치(`logs/<이름>-<턴>.jsonl`, `t2-`, `t3-`), 판정마다의 실행 시간이 있다. 통과
- 프로젝트 전체 테스트가 모두 통과한다.
  - `python3 -m unittest discover -s tests` → 마지막 줄 `OK`. 통과
- 테스트 먼저 기록: phase 9
  - `git show c93d110^:docs/tasks/010-tasks-cycle/phase-9.md`의 "한 일" 테스트 먼저 항목 → 실패 출력(`FAIL: test_branch_does_not_pick_task …`, `FAIL: test_plan_first_message_says_task …`, `FAIL: test_non_code_files_pass …`, `Ran 39 tests`, `FAILED (failures=3)`) 뒤에 통과 출력(`Ran 39 tests`, `OK`)이 이 순서로 있다. 통과

**문제**
- 실행이 쓰는 고침 task의 꼴은 소스 문제의 글을 그대로 완료 조건으로 옮겨서, 글대로면 결함이 남아 있어야 완료 조건이 참이 된다. "고침 task의 꼴"은 소스 문제의 글을 옮기고(`run/SKILL.md` 352줄) 완료 조건을 고칠 것 하나에 `{고칠 것의 글}` 하나로 적으며(353줄, 373줄), 그 확인은 "{그 문제가 적힌 곳을 다시 읽거나, 문제를 드러낸 명령을 다시 돌린다}"(374줄)라서 기대 결과를 정하지 않는다. 그런데 `phase-1.md`의 통과 조건은 "task 머리의 완료 조건이 모두 참이다"이다(401줄). 다시 돌린 `~/plate-rail-test/t-all`에서 `90bba05 plan: 003-fixes 더함`의 완료 조건 1이 "`stats`가 DB를 읽다 난 모든 오류를 삼켜, … `책 0권`과 종료 코드 0을 낸다"였다. 고친 뒤의 상태는 실행 에이전트가 확인에 덧붙인 "→ … 결과가 나오지 않는다"에만 있다. 그 tasks의 `003-fixes` 회고도 같은 것을 적었다(`44f58ed^:docs/tasks/FRICTION.md`의 `003-fixes` 둘째 줄) (`plugins/plate/skills/run/SKILL.md`). 기준: 결함
- `docs/TOOLS.md` 189줄("도구를 넓힐 때 할 것")이 "Codex에서 실행 스킬 셋(run, phase, retro)의 판정을 돌린다. … worktree와 `.git` 쓰기를 막는 샌드박스부터 확인한다"로 남아 있다. 이 tasks에서 실행이 맡기는 스킬은 phase, check, retro, review, eval이 됐고(`run/SKILL.md` 16줄), 머리의 결정은 worktree를 쓰지 않는다. 그런데 이 줄은 바뀌지 않았다. 검증 1의 문제 3은 같은 파일의 21줄만 가리켰고, phase 13도 그 줄만 고쳤다 (`docs/TOOLS.md`). 기준: 맥락 문서

**배운 것**
- 다시 돌린 `t-all`의 eval 1에는 하네스 고칠 거리가 아홉 있다. 그 가운데 이슈로 올린 것은 1번(심어 둔 계획에서 나온 것)뿐이고, 그 #3은 지웠다. 본문의 규칙에서 나온 2, 5, 6, 7번은 `~/plate-rail-test/t-all`의 `44f58ed^:docs/tasks/eval.md`에만 있다: phase·check가 맡은 phase가 없는 완료 조건을 보고도 멈추지 않는다, run이 계획의 커밋 앞에 든 계획 밖 커밋을 보지 않는다, review가 측정 파일을 저장소 밖에 쓴다, eval의 규칙 준수 커밋 표에 run의 커밋 꼴(`plan: NNN-slug 수정`, `NNN-slug: phase N 통과`)이 없다. 마지막 것은 eval 본문이 "표에 없는 꼴의 커밋은 보지 않는다"(`eval/SKILL.md` 124줄)고 정해 둔 동작이라, 이 검증에서는 문제로 적지 않았다.
- 실행은 회고 에이전트의 줄과 그 뒤 물음의 줄을 `RUNLOG.md`에 더한 채 커밋하지 않고 멈춘다(`t-run`의 작업 트리, `run/SKILL.md` 428줄). 그래서 RUNLOG의 줄 수를 세는 확인은 커밋이 아니라 작업 트리를 읽어야 맞는다.

**하네스의 문제점**
- 계획의 완료 조건 3~8은 여전히 시험 장면의 결과(물음, 커밋, 파일, 등급이 있는지)만 본다. 에이전트가 시험 기록의 `FRICTION.md`와 "하네스에서 걸린 것"에 적은 본문끼리의 어긋남은 보지 않는다. 문제 1은 `t-all`의 `003-fixes` 회고가 `FRICTION.md`에 적었는데도 완료 조건 6의 확인을 지나갔다.
- 계획 phase 13의 TODO는 검증 1 문제 3의 글(`docs/TOOLS.md` 21줄)을 그대로 옮겼고, 통과 조건도 "문제마다 적힌 곳을 다시 읽거나 돌린다"이다. 그래서 같은 꼴의 옛 스킬 목록(189줄)은 고칠 대상에도 확인에도 들지 않았다. 완료 조건 2와 10의 첫 확인이 grep하는 파일에도 `docs/TOOLS.md`는 아직 없다.
- 이 검증 세션에 실린 `AGENTS.md`는 새 구조의 문서 지도와 규칙 구간(retro, review, eval)이다. 결정대로 0.9.1의 plate:verify로 010을 닫는데, `verify.md`는 `docs/tasks/` 행의 내용에 없다. 파일이 이미 있어서 새로 만들지 않고 검증 절만 더했다.

**판정**: 문제 있음
