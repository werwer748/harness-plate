# Phase 13: 검증 1의 문제를 고친다

**목표**: 검증 1에서 나온 문제를 모두 고친다.

**테스트 먼저**: 아니오 — 고칠 문제가 모두 `.md`(`plugins/plate/skills/eval/SKILL.md`, `plugins/plate/skills/run/SKILL.md`, `docs/TOOLS.md`)만 고친다.

**읽을 것**
- `docs/tasks/010-tasks-cycle/verify.md`의 `## 검증 1` 절
- `plugins/plate/skills/eval/SKILL.md`
- `plugins/plate/skills/run/SKILL.md`
- `plugins/plate/skills/phase/SKILL.md`
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/ADR.md`
- `docs/TOOLS.md`
- `~/plate-rail-test/bin/` (네 장면을 다시 돌릴 실행 도구와 시험 폴더를 만드는 도구)

**TODO**
- [x] 하네스 eval의 낱말 "더한 phase"는 "메시지가 `plan:`으로 시작하는 커밋이 만들지 않은 phase"인데(`eval/SKILL.md` 36줄), 실행은 회고의 문제를 고칠 phase를 `plan: NNN-slug 수정`으로(`run/SKILL.md` 172줄), 고침 task의 phase를 `plan: NNN-fixes 더함`으로(345줄) 커밋한다. 글대로 따르면 실행이 더한 phase가 늘 0개라 eval 절 "대상"의 더한 phase 수와 효율의 되풀이 줄(`eval/SKILL.md` 117줄)이 틀린다 (`plugins/plate/skills/eval/SKILL.md`, `plugins/plate/skills/run/SKILL.md`)
- [x] 실행이 쓰는 고칠 phase와 고침 task의 꼴이 수행에게 읽지 않는다는 파일을 읽게 한다. 고칠 phase의 읽을 것에 "{문제에 적힌 파일의 경로}"(`run/SKILL.md` 185줄)를 옮기면 회고가 근거로 든 `done-phase-N.md`가 들어가고, 고침 task 머리의 마지막 완료 조건의 확인이 "`docs/tasks/plan.md`의 그 완료 조건에 적힌 확인을 모두 돌린다"(374~375줄)라 `phase-1.md`의 통과 조건(399~401줄)을 돌리려면 tasks 머리를 읽어야 한다. 수행 스킬 1번은 tasks 머리와 다른 phase의 파일을 읽지 않는다고 하고(`phase/SKILL.md` 34줄), 하네스 eval은 수행이나 확인이 읽기 범위 밖을 읽은 곳을 규칙 준수 C·D로 센다(`eval/SKILL.md` 152~153줄) (`plugins/plate/skills/run/SKILL.md`)
- [x] `docs/TOOLS.md` 21줄이 스킬을 `/plate:setup`, `/plate:context`, `/plate:plan`, `/plate:run`, `/plate:phase`, `/plate:retro`, `/plate:verify`로 부른다고 적는다. 이 tasks가 verify를 없애고 check, review, eval을 더했는데 그 줄이 그대로다 (`docs/TOOLS.md`)
- [x] 바뀐 본문으로 네 장면(setup·plan, run task 하나씩, run 일괄 끝까지와 다시 돌림, check 세 번 실패)을 다시 돌려 기록을 `~/plate-rail-test/logs/`에 남긴다. 다시 올린 이슈는 확인한 뒤 지운다

**통과 조건**
- 검증 1의 문제가 모두 고쳐졌다.
  - 확인: 문제마다 적힌 곳을 다시 읽거나 돌린다
- 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다

## 한 일
- 하네스 eval의 낱말 "더한 phase"가 실행의 커밋 꼴과 어긋난다: 낱말을 커밋 메시지가 아니라 제목(`# Phase M: 회고 K의 문제를 고친다` 꼴의 `done-phase-M.md`)으로 가르게 고치고, 실행이 이 phase도 `plan: NNN-slug 수정`으로 커밋한다는 까닭을 적었다. 0번의 "커밋으로 보는 근거"에서 "더한 phase"를 뺐다. 실행 쪽 커밋 꼴은 그대로 두었다(실행의 3번 표가 이미 같은 제목으로 고칠 phase를 가른다) (`plugins/plate/skills/eval/SKILL.md`)
- 고칠 phase와 고침 task의 꼴이 수행에게 읽지 않는다는 파일을 읽게 한다: 8번의 규칙에 "문제에 적힌 파일 가운데 `docs/tasks/` 아래의 tasks 머리, `phase-N.md`, `done-phase-N.md`는 읽을 것과 TODO에 옮기지 않는다"를 더했다(고침 task는 "읽을 것은 8번과 같은 규칙"으로 이 규칙을 따른다). 고침 task의 꼴에 마지막 완료 조건의 확인은 가리킨 tasks 완료 조건의 확인을 그대로 옮긴다는 규칙을 더하고, 양식의 확인 줄을 "`docs/tasks/plan.md`의 그 완료 조건에 적힌 확인을 모두 돌린다"에서 옮긴 확인의 자리로 바꿨다 (`plugins/plate/skills/run/SKILL.md`)
- `docs/TOOLS.md` 21줄의 옛 스킬 목록: `/plate:check`, `/plate:review`, `/plate:eval`을 넣고 `/plate:verify`를 빼고, 0.10.0에서 바뀐 것과 근거(2026-10-18 판정 기록의 init 줄)를 적었다 (`docs/TOOLS.md`)
- 바뀐 본문으로 네 장면을 다시 돌림: 앞 판정의 폴더를 `t-setup-try2`, `t-plan-try2`, `t-run-try2`, `t-all-try2`, `t-again-try2`, `t-stop-try2`로 옮기고 `bin/tasksmake.sh t-setup t-plan t-run t-all t-stop`(뒤에 `t-again`)으로 다시 만들어, `bin/tturn.sh`로 턴마다 돌렸다. 기록은 `~/plate-rail-test/logs/t3-*.jsonl`(`.state`, `.sid`, `.base` 함께)이고 claude 2.1.303, init 줄의 plate는 `/Users/gangjungi/Desktop/harness-plate/plugins/plate`(0.10.0)다. 새로 쓴 답 파일은 `answers/t3-plan-8.md`, `t3-all-3.md`, `t3-again-2.md`(물음의 번호가 앞 판정과 달라 새로 썼다)
  - setup·plan: `t3-setup-1`~`2`, `t3-plan-1`~`12`(물음 8번, tasks 머리·001·002 승인 뒤 `536e55f plan: list-delete`), `t3-plan-add`
  - run task 하나씩: `t3-run-1`~`3`(에이전트 5, 회고 뒤 다음 task로 가지 않음)
  - run 일괄 끝까지: `t3-all-1`~`4`(고칠 안을 소스 문제 1번만 고침 task로 고치고 plate 자체 1번만 이슈로 올리게 고쳐 승인). `gh issue create`가 `https://github.com/werwer748/harness-plate/issues/3`을 냈다. 다시 돌림은 `t3-again-1`~`3`(모두 BACKLOG로 미루고 이슈 1번만)이고 `gh issue comment 3 … --body-file -`(첫 줄 `다시 나옴`)이 `…/issues/3#issuecomment-6263627265`를 냈다
  - check 세 번 실패: `t3-stop-1`~`2`
  - 이슈 #3은 `gh issue view 3 … --json comments`로 댓글 첫 줄 `다시 나옴`을 본 뒤 `gh issue delete 3 --repo werwer748/harness-plate --yes`로 지웠다(종료 코드 0)
- `docs/TOOLS.md`의 Claude Code 버전 줄에 2.1.303(2026-10-19)을 더하고, "tasks 실행의 판정에서 본 것"에 다시 돌린 판정의 기록 위치(`t3-`), 옮긴 폴더(`-try2`), 이슈 #3, 실행 시간을 한 줄로 더했다 (`docs/TOOLS.md`)

## 확인 결과
- 검증 1의 문제가 모두 고쳐졌다.
  - 문제 1: `plugins/plate/skills/eval/SKILL.md` 36줄을 다시 읽음 → 더한 phase를 제목으로 가르고 커밋 메시지로는 가르지 않는다. 다시 돌린 `~/plate-rail-test/t-all`의 `dfee9c3:docs/tasks/eval.md` → 대상 "phase 3개(더한 phase 1개)", 효율 근거 "`수행 001-list-command phase 2` 되풀이 — 더한 phase"와 "`확인 001-list-command phase 2` 되풀이 — 더한 phase", 되풀이 몫 토큰 26.8%로 C. 통과
  - 문제 2: `run/SKILL.md` 8번 규칙과 고침 task의 꼴을 다시 읽음 → 위의 두 규칙과 양식의 확인 자리가 있다. 다시 돌린 `t-all`의 `16bc67e plan: 001-list-command 수정`이 만든 `phase-2.md`의 읽을 것 → `retro.md`의 `## 회고 1` 절, `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`이고 `done-phase-1.md`가 없다(TODO의 경로도 `docs/PRD.md`뿐). `90bba05 plan: 003-fixes 더함`의 `003-fixes/plan.md` 완료 조건 2 → "tasks 완료 조건 1, 2, 4, 5가 참이다" 아래에 확인 넷이 명령으로 옮겨져 있다. `44f58ed^:docs/tasks/003-fixes/done-phase-1.md`의 "하네스에서 걸린 것"과 확인 1의 "하네스에서 걸린 것"(없음)에 tasks 머리를 읽었다는 줄이 없다(`grep -n "tasks/plan.md\|tasks 머리"` → 0줄). 통과
  - 문제 3: `docs/TOOLS.md` 21줄을 다시 읽음 → `/plate:setup`, `/plate:context`, `/plate:plan`, `/plate:run`, `/plate:phase`, `/plate:check`, `/plate:retro`, `/plate:review`, `/plate:eval`. 통과
- 머리의 완료 조건이 모두 참이다.
  - 1: `ls plugins/plate/skills` → `check`, `context`, `eval`, `phase`, `plan`, `retro`, `review`, `run`, `setup` 아홉. 통과
  - 2: `grep -n "작업" plugins/plate/skills/*/SKILL.md plugins/plate/hooks/edit_guard.py README.md docs/PRD.md docs/ARCHITECTURE.md AGENTS.md` → 10줄(context:8, edit_guard.py:23, PRD:4·7·24, setup:3·10·132, AGENTS.md:16, ARCHITECTURE:36). 모두 일반의 일, git의 작업 트리, 규칙 구간의 이름, 작업 디렉터리이고 tasks, task, phase를 가리키지 않는다. 낱말 절이 있는 여덟 스킬의 절을 `awk`로 뽑아 읽음 → tasks, task(폴더), task 머리, tasks 머리, phase의 정의가 결정과 같다. 통과
  - 3: `grep -n "plate:context\|이어서 채울지\|verify" plugins/plate/skills/setup/SKILL.md` → 0줄(종료 코드 1). `logs/t3-setup-1.jsonl`의 마지막 답은 화면이 있는지 묻는 물음, `t3-setup-2.jsonl`은 만든 것·옮긴 것·건드리지 않은 것·채워야 할 칸·`AGENTS.md` 크기의 보고로 끝나고 채울지 묻는 글이 없다. setup 본문의 문서 지도 구간에서 `docs/DESIGN.md` 행을 뺀 것 + 빈 줄 + 규칙 구간을 `~/plate-rail-test/t-setup/AGENTS.md`와 python으로 견줌 → `equal: True`. 완료 조건 13의 `find`에 `t3-setup-1`, `t3-setup-2.jsonl`이 나온다. 통과
  - 4: `logs/t3-plan-1`~`12.jsonl`과 `t3-plan-add.jsonl`의 마지막 답에서 `쓸 위치:`를 셈(python) → `t3-plan-9`(`docs/tasks/plan.md`), `t3-plan-10`(`docs/tasks/001-list-command/`), `t3-plan-11`(`docs/tasks/002-delete-command/`)에 하나씩, 나머지 0. 셋 모두 승인을 묻는 글로 끝난다. `AskUserQuestion` 0번. `t3-plan-1`~`11.state`의 `git status --short`와 `ls docs/tasks` → 모두 빈 출력, `git log` 맨 위 `6712617 셋업 직후`. `t-plan`에서 `git log -1 --stat` → `536e55f plan: list-delete`에 `docs/tasks/plan.md`, `001-list-command/plan.md`, `001-list-command/phase-1.md`, `002-delete-command/plan.md`, `002-delete-command/phase-1.md` 다섯 파일. `docs/tasks/plan.md`의 완료 조건 절에 조건 넷과 확인이 있다. `grep -c '^## 명령' docs/ARCHITECTURE.md` → `0`, `001-list-command/phase-1.md`의 TODO 첫 항목이 `docs/ARCHITECTURE.md`에 `## 명령` 절을 쓰는 것이다. `t3-plan-add.jsonl`의 답 → 진행 중인 tasks `list-delete`를 알리고 "이 tasks에 세 번째 task(`003-...`)로 더할까요?", `.state`는 빈 `git status`, 맨 위 `536e55f`. 완료 조건 13의 `find`에 이 기록들이 나온다. 통과
  - 5: `t-run`에서 `git branch --show-current` → `tasks/list-delete`. `git log --oneline --reverse` → `d36da69 plan: list-delete` 뒤에 `722691a 001-list-command: phase 1`, `8c8375c … phase 1 확인`, `7306065 … phase 1 통과`, `8c5c4ac … phase 2`, `948b005 … phase 2 확인`, `603f33c … phase 2 통과`, `8edcb8a 001-list-command: 회고`가 이 차례. `ls -A docs/tasks/001-list-command` → `done-phase-1.md`, `done-phase-2.md`, `plan.md`, `retro.md`. `t3-run-1`의 답은 실행 방식(task 하나씩, tasks 일괄)을 묻고, `t3-run-2`는 회고 통과 보고 뒤 "다음 task인 `002-delete-command`(책 지우기 명령)로 갈까요?"로 끝난다. `docs/tasks/RUNLOG.md` → 에이전트 줄 5(줄마다 토큰, 도구 호출, 시간), 물음 줄 2(실행 방식, 다음 task). `python3 bin/tagents.py logs/t3-run-1.jsonl logs/t3-run-2.jsonl logs/t3-run-3.jsonl` → `= 모두: 에이전트 5`, 다섯 줄의 토큰·도구 호출·시간이 RUNLOG와 같다. 기록의 물음은 `t3-run-1`, `t3-run-2`의 둘. `docs/tasks/FRICTION.md`에 `` `001-list-command` 문제: `` 줄 둘. 완료 조건 13의 `find`에 `t3-run-1`~`3`이 나온다. 통과
  - 6: `t3-all-1`~`4`의 마지막 답 → 실행 방식(1), 고칠 안대로 할지(2), 고친 안대로 할지(3), `tasks/list-delete`를 `main`에 합칠지(4). `AskUserQuestion` 0번. `t-all`의 `git log --oneline --reverse` → `16bc67e plan: 001-list-command 수정`과 그 phase의 `1bf1244`, `995960a`, `aafa62a`, `2e0c6a6 list-delete: 코드 평가`, `dfee9c3 list-delete: 하네스 eval`, `90bba05 plan: 003-fixes 더함`과 `5b69deb`, `9851a0c`, `adbe284`, `908661e 003-fixes: 회고`, `44f58ed list-delete: 비움`이 이 차례. `git show 44f58ed^:docs/tasks/review.md` → 신뢰성 C, 보안 A, 유지보수성 A, 테스트 적절성 C, 기능 적합성 C, Sonar way 조건 넷과 "게이트: 실패", 판단 근거마다 파일:줄(`booklog/stats.py:12-13`, `booklog/cli.py:65`, `tests/test_delete.py:39-45` 등, 파일:줄 꼴 18곳). `git show 44f58ed^:docs/tasks/eval.md` → 결과 성공 D, 일관성 B, 효율 C, 규칙 준수 D, 사람 개입률 A, 실패 양상 E와 "스킬로 만들 후보" 절. `docs/BACKLOG.md` → 미룬 소스 문제 다섯, 항목마다 "나온 tasks: `list-delete`". `grep -n BACKLOG AGENTS.md` → 11줄의 문서 지도 행. `ls -A docs/tasks` → `.gitkeep`. 완료 조건 13의 `find`에 `t3-all-1`~`4`가 나온다. 통과
  - 7: `logs/t3-all-4.jsonl`의 `gh issue create --repo werwer748/harness-plate --title "plan: task 머리의 완료 조건 가운데 어느 phase도 맡지 않는 것이 생긴다" --body "$(cat <<'EOF' …)"` → `https://github.com/werwer748/harness-plate/issues/3`. `logs/t3-again-3.jsonl`의 `gh issue comment 3 --repo werwer748/harness-plate --body-file - <<'EOF'`(첫 줄 `다시 나옴`) → `https://github.com/werwer748/harness-plate/issues/3#issuecomment-6263627265`. 지운 뒤 `gh issue view 3 --repo werwer748/harness-plate` → `GraphQL: Could not resolve to an issue or pull request with the number of 3. (repository.issue)`, 종료 코드 1. `gh issue list --state all --json number` → `[]`. 완료 조건 13의 `find`에 `t3-all-4`, `t3-again-1`~`3`이 나온다. 통과
  - 8: `~/plate-rail-test/t-stop/docs/tasks/001-prd-scope/phase-1.md` → `## 확인 1`, `## 확인 2`, `## 확인 3`, 판정 셋 모두 `실패`. HEAD가 확인 3의 커밋 `b734b35`이고 그 뒤 수행 커밋이 없다. `logs/t3-stop-2.jsonl`의 마지막 답 → "## 원인"(확인 셋의 같은 실패와 커밋 수 표), "## 해결책" 하나(`--deselect`로 stamp 테스트를 빼고 바꿀 파일과 글), "이 해결책으로 갈까요?"로 끝나고 고를 선택지 목록이 없다. 완료 조건 13의 `find`에 `t3-stop-1`, `t3-stop-2`가 나온다. 통과
  - 9: `python3 -m unittest discover -s tests` → `Ran 39 tests`, 마지막 줄 `OK`. `grep -n 'task/\|\.worktrees' plugins/plate/hooks/edit_guard.py` → 0줄(종료 코드 1). `grep -c 'done-phase' tests/test_edit_guard.py` → `3`. 통과
  - 10: `grep -n "verify\|LESSONS\|worktree" docs/PRD.md docs/ARCHITECTURE.md README.md AGENTS.md` → 0줄(종료 코드 1). 규칙 구간 `diff` → 출력 없음(종료 코드 0). `grep -hF '| `docs/tasks/' AGENTS.md plugins/plate/skills/setup/SKILL.md | sort -u | wc -l` → `1`. `grep -c "^## 명령" docs/ARCHITECTURE.md` → `1`, 빌드 없음·린트 없음·테스트 `python3 -m unittest discover -s tests`. PRD 핵심 기능 5, 7, 8과 ARCHITECTURE의 디렉터리 구조, 패턴과 규칙, 데이터 흐름을 읽음 → 아홉 스킬과 새 흐름을 말한다(이 phase에서 두 문서를 고치지 않았다). 통과
  - 11: `grep -n "^### ADR-020" docs/ADR.md` → `28:### ADR-020: plate 자체의 고칠 거리는 GitHub 이슈로 모은다` 1줄. 항목에 결정, 이유, 트레이드오프가 있다. 통과
  - 12: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `  "version": "0.10.0",`. 두 `description`에 setup, context, plan, run, phase, check, retro, review, eval이 있고 verify가 없다. 통과
  - 13: `N=$(ls -t plugins/plate/skills/*/SKILL.md plugins/plate/hooks/*.py plugins/plate/hooks/*.json | head -1); find ~/plate-rail-test/logs -name '*.jsonl' -newer "$N"` → N은 `plugins/plate/skills/run/SKILL.md`(10월 19 16:28). 나온 기록은 `t3-setup-1`~`2`, `t3-plan-1`~`12`, `t3-plan-add`, `t3-run-1`~`3`, `t3-all-1`~`4`, `t3-again-1`~`3`, `t3-stop-1`~`2`로 네 장면이 모두 든다. 통과
  - 14: `docs/TOOLS.md`의 Claude Code 절을 읽음 → 버전 줄에 2.1.302(2026-10-18)와 2.1.303(2026-10-19), "tasks 실행의 판정에서 본 것"에 에이전트 결과의 사용량(`<usage>subagent_tokens …`, `totalTokens` 등), `gh issue create`·`comment`·`delete`와 그 출력, 시험 폴더(`tasksmake.sh`, `-try1`, `-try2`)와 기록 위치(`logs/<이름>-<턴>.jsonl`, `t2-`, `t3-`), 판정마다의 실행 시간. 통과
  - 15: `python3 -m unittest discover -s tests` → 마지막 줄 `OK`. 통과

## 계획과 달라진 점
- TODO에는 `docs/TOOLS.md` 21줄만 있었지만, 버전 줄에 2.1.303을 더하고 다시 돌린 판정의 기록 위치·옮긴 폴더·이슈 번호·실행 시간을 한 줄 더했다. 까닭: 완료 조건 14가 이 단계의 판정 사실(기록 위치, 실행 시간, 날짜·버전)을 보는데, 그대로 두면 `docs/TOOLS.md`가 `t2-` 판정까지만 말하고 이번 기록(`t3-`)을 가리키지 않는다.
- 다시 돌린 기록의 이름은 `t3-`로, 앞 판정의 폴더는 `-try2`를 붙여 옮겼다. 계획은 이름을 정하지 않았고, 검증 1의 근거(`t2-` 기록과 `t-all` 등)를 덮어쓰지 않으려고 앞 판정의 꼴(`t2-`, `-try1`)을 따랐다.

## 남은 것
- 없음

## 하네스에서 걸린 것
- 다시 돌린 `t-all`의 eval 1(`dfee9c3:docs/tasks/eval.md`)이 plate 자체의 고칠 거리 7로 "eval 3번 규칙 준수의 커밋 표에 실행이 만드는 `plan: NNN-slug 수정`과 `NNN-slug: phase N 통과` 꼴이 없어 그 커밋 넷을 보지 못했다"를 적었다. 이 phase의 TODO가 아니라 고치지 않았다. 표는 "표에 없는 꼴의 커밋은 보지 않는다"로 실행의 커밋을 일부러 뺀 것인지 정해 둔 곳이 없다.
- 같은 eval 1이 규칙 준수를 D로 매긴 근거("수행이나 확인이 읽기 범위 밖을 읽은 곳이 둘")는 `bin/tasksmake.sh`가 손으로 쓴 `002-delete-command`의 계획(319~320줄, 353줄의 "`docs/tasks/plan.md`의 … 확인을 모두 돌린다")에서 나왔다. 이 phase가 고친 실행의 고침 task 꼴과는 다른 곳이고, plan 스킬의 규칙(완료 조건이 "tasks 완료 조건 N"을 번호로 가리킨다, 227줄)도 확인을 옮겨 적으라고는 하지 않는다. eval 1은 이것을 plate 자체의 고칠 거리 4로 적었다.
- 다시 돌린 `t-run`의 회고 1(`8edcb8a`)은 문제 목록을 "없음", 판정을 통과로 적고, 같은 커밋에서 `FRICTION.md`에는 `` `001-list-command` 문제: `` 줄 둘(확인이 "표준 출력"을 다 보지 못함, 같은 테스트 명령을 두 번 돌림)을 더했다. retro 스킬의 회고 절 "문제"와 `FRICTION.md`의 문제 줄이 어긋났다.
- 다시 돌린 `t-stop`의 세 번째 확인 에이전트가 돌려준 첫 줄이 `判定: 실패`였다(check 스킬 7번의 양식은 `판정:`). 실행은 그대로 받아 멈췄다.
- `bin/tasksmake.sh t-again`이 `git reset --hard`와 `git clean`으로 `RUNLOG.md`의 커밋하지 않은 줄(002 회고, 코드 평가, 하네스 eval)을 지워, 다시 돌린 실행(`t3-again-1`)이 "RUNLOG.md에 에이전트 줄 세 개가 없다"고 보고했다. 실행이 RUNLOG의 줄을 "비운다"까지 커밋하지 않고 두는 규칙과 장면 도구가 겹친 것이다.

## 회고 1: 확인만

**확인**
- 검증 1의 문제가 모두 고쳐졌다.
  - 문제 1: `plugins/plate/skills/eval/SKILL.md` 36줄을 다시 읽음 → "더한 phase"를 제목 `# Phase M: 회고 K의 문제를 고친다` 꼴의 `done-phase-M.md`로 가르고 커밋 메시지로는 가르지 않는다고 적혀 있고, `run/SKILL.md` 8번 양식의 제목(`# Phase {M}: 회고 {K}의 문제를 고친다`)과 3번 표(98줄)가 같은 꼴이다. 53줄의 커밋으로 보는 근거에 "더한 phase"가 없다. `~/plate-rail-test/t-all`의 `git show '44f58ed^:docs/tasks/eval.md'` → 대상 "phase 3개(더한 phase 1개)", 효율 근거 "`수행 001-list-command phase 2` 되풀이 — 더한 phase"와 "`확인 001-list-command phase 2` 되풀이 — 더한 phase". 통과
  - 문제 2: `run/SKILL.md` 165줄 → 문제에 적힌 `docs/tasks/` 아래의 tasks 머리, `phase-N.md`, `done-phase-N.md`를 읽을 것과 TODO에 옮기지 않는다는 규칙이 있다. 353줄 → 고침 task 마지막 완료 조건의 확인에 tasks 머리의 확인을 그대로 옮긴다는 규칙, 376줄 양식의 확인 자리가 "{가리킨 tasks 완료 조건에 적힌 확인. 확인마다 한 줄로 그대로 옮긴다}"다. `phase/SKILL.md` 34줄과 `check/SKILL.md` 1번의 읽을 것에 tasks 머리가 없다. `t-all`의 `git show 16bc67e:docs/tasks/001-list-command/phase-2.md` → 읽을 것이 `retro.md`의 `## 회고 1` 절, `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`이고 `done-phase-1.md`가 없다. `git show 90bba05:docs/tasks/003-fixes/plan.md` → 완료 조건 2 "tasks 완료 조건 1, 2, 4, 5가 참이다" 아래에 명령 확인 넷. `git show '44f58ed^:docs/tasks/003-fixes/done-phase-1.md' | grep -n "tasks/plan.md\|tasks 머리"` → 0줄(종료 코드 1). 통과
  - 문제 3: `docs/TOOLS.md` 21줄을 다시 읽음 → `/plate:setup`, `/plate:context`, `/plate:plan`, `/plate:run`, `/plate:phase`, `/plate:check`, `/plate:retro`, `/plate:review`, `/plate:eval`이고 verify가 없다. 통과
- 머리의 완료 조건이 모두 참이다.
  - 1: `ls plugins/plate/skills` → `check`, `context`, `eval`, `phase`, `plan`, `retro`, `review`, `run`, `setup` 아홉. 통과
  - 2: `grep -n "작업" plugins/plate/skills/*/SKILL.md plugins/plate/hooks/edit_guard.py README.md docs/PRD.md docs/ARCHITECTURE.md AGENTS.md` → 10줄(PRD:4·7·24, context:8, setup:3·10·132, edit_guard.py:23, ARCHITECTURE:36, AGENTS.md:16)을 모두 읽음 → 일반의 일, 규칙 구간의 이름, git 작업 트리, 작업 디렉터리이고 tasks, task, phase를 가리키는 것이 없다. 낱말 절이 있는 스킬(check, context, eval, phase, plan, retro, review, run)의 절을 `awk`로 뽑아 읽음 → tasks, task(폴더), phase, tasks 머리(제목·이름·여섯 절), task 머리(제목·네 절)가 결정과 같다. 통과
  - 3: `grep -n "plate:context\|이어서 채울지\|verify" plugins/plate/skills/setup/SKILL.md` → 0줄(종료 코드 1). `logs/t3-setup-1.jsonl`의 마지막 답은 화면이 있는지 묻는 물음, `t3-setup-2.jsonl`은 만든 것·옮긴 것·건드리지 않은 것·채워야 할 칸·`AGENTS.md` 크기의 보고로 끝나고 채울지 묻는 글이 없다(`AskUserQuestion` 0번). setup 본문의 문서 지도 구간에서 `docs/DESIGN.md` 행을 뺀 것 + 빈 줄 + 규칙 구간을 `~/plate-rail-test/t-setup/AGENTS.md`와 python으로 견줌 → `equal: True`. 13의 `find`에 두 기록이 나온다. 통과
  - 4: `logs/t3-plan-1`~`12.jsonl`, `t3-plan-add.jsonl`의 마지막 답에서 `쓸 위치:`를 셈(python) → `t3-plan-9`(`docs/tasks/plan.md`), `t3-plan-10`(`docs/tasks/001-list-command/`), `t3-plan-11`(`docs/tasks/002-delete-command/`)에 하나씩, 나머지 0. `AskUserQuestion` 모두 0번. `t3-plan-1`~`11.state` → `git status --short`와 `ls docs/tasks` 모두 빈 출력, 맨 위 `6712617 셋업 직후`. `t-plan`의 `git log -1 --stat` → `536e55f plan: list-delete`에 `docs/tasks/plan.md`, `001-list-command/plan.md`·`phase-1.md`, `002-delete-command/plan.md`·`phase-1.md` 다섯 파일, `docs/tasks/plan.md` 완료 조건 절에 조건 넷과 확인. `grep -c '^## 명령' docs/ARCHITECTURE.md` → `0`, `001-list-command/phase-1.md` TODO 첫 항목이 `## 명령` 절을 쓰는 것. `t3-plan-add`의 답 → 진행 중인 tasks `list-delete`를 알리고 "이 tasks에 세 번째 task(`003-...`)로 더할까요?". 13의 `find`에 이 기록들이 나온다. 통과
  - 5: `t-run`에서 `git branch --show-current` → `tasks/list-delete`. `git log --oneline --reverse` → `d36da69 plan: list-delete` 뒤에 `722691a … phase 1`, `8c8375c … phase 1 확인`, `7306065 … phase 1 통과`, `8c5c4ac … phase 2`, `948b005 … phase 2 확인`, `603f33c … phase 2 통과`, `8edcb8a 001-list-command: 회고` 차례. `ls -A docs/tasks/001-list-command` → `done-phase-1.md`, `done-phase-2.md`, `plan.md`, `retro.md`. `t3-run-1`의 답은 실행 방식을, `t3-run-2`는 회고 통과 뒤 "다음 task인 `002-delete-command`(책 지우기 명령)로 갈까요?"를 묻는다. `python3 -I bin/tagents.py logs/t3-run-1.jsonl logs/t3-run-2.jsonl logs/t3-run-3.jsonl` → `= 모두: 에이전트 5`, 다섯 줄의 토큰·도구 호출·시간이 `RUNLOG.md`의 에이전트 줄 다섯과 같다. 물은 줄 둘(실행 방식, 다음 task)과 기록의 물음 둘. `FRICTION.md`에 `` `001-list-command` 문제: `` 줄 둘. 13의 `find`에 `t3-run-1`~`3`이 나온다. 통과
  - 6: `t3-all-1`~`4`의 마지막 답 → 실행 방식, 고칠 안대로 할지, 고친 안대로 할지, `tasks/list-delete`를 `main`에 합칠지. `AskUserQuestion` 0번. `t-all`의 `git log --oneline --reverse` → `16bc67e plan: 001-list-command 수정`과 그 phase의 `1bf1244`·`995960a`·`aafa62a`, `2e0c6a6 list-delete: 코드 평가`, `dfee9c3 list-delete: 하네스 eval`, `90bba05 plan: 003-fixes 더함`과 `5b69deb`·`9851a0c`·`adbe284`·`908661e`, `44f58ed list-delete: 비움` 차례. `git show 44f58ed^:docs/tasks/review.md` → 신뢰성 C, 보안 A, 유지보수성 A, 테스트 적절성 C, 기능 적합성 C, Sonar way 조건 넷과 "게이트: 실패", 근거마다 파일:줄(`booklog/stats.py:12-13`, `booklog/cli.py:65`, `tests/test_delete.py:39-45` 등). `git show '44f58ed^:docs/tasks/eval.md'` → 결과 성공 D, 일관성 B, 효율 C, 규칙 준수 D, 사람 개입률 A, 실패 양상 E와 "스킬로 만들 후보" 절. `docs/BACKLOG.md` → 미룬 소스 문제 다섯, 항목마다 "나온 tasks: `list-delete`". `grep -n BACKLOG AGENTS.md` → 11줄의 문서 지도 행. `ls -A docs/tasks` → `.gitkeep`. 13의 `find`에 `t3-all-1`~`4`가 나온다. 통과
  - 7: `logs/t3-all-4.jsonl`의 `gh issue create --repo werwer748/harness-plate --title "plan: task 머리의 완료 조건 가운데 어느 phase도 맡지 않는 것이 생긴다" …` → `https://github.com/werwer748/harness-plate/issues/3`. `logs/t3-again-3.jsonl`의 `gh issue comment 3 --repo werwer748/harness-plate --body-file - <<'EOF'`(첫 줄 `다시 나옴`) → `…/issues/3#issuecomment-6263627265`. `gh issue view 3 --repo werwer748/harness-plate` → `GraphQL: Could not resolve to an issue or pull request with the number of 3. (repository.issue)`, 종료 코드 1. `gh issue list --state all --json number` → `[]`. 13의 `find`에 두 기록이 나온다. 통과
  - 8: `~/plate-rail-test/t-stop/docs/tasks/001-prd-scope/phase-1.md` → `## 확인 1`·`2`·`3`, 판정 셋 모두 `실패`. HEAD가 확인 3의 커밋 `b734b35`이고 그 뒤 커밋이 없다. `logs/t3-stop-2.jsonl`의 마지막 답 → "## 원인"(확인 셋의 실패와 커밋 수 표), "## 해결책" 하나(`--deselect`로 stamp 테스트를 빼고 바꿀 곳), "이 해결책으로 갈까요?"로 끝나고 고를 선택지 목록이 없다. 13의 `find`에 `t3-stop-1`, `t3-stop-2`가 나온다. 통과
  - 9: `python3 -m unittest discover -s tests` → `Ran 39 tests`, 마지막 줄 `OK`. `grep -n 'task/\|\.worktrees' plugins/plate/hooks/edit_guard.py` → 0줄(종료 코드 1). `grep -c 'done-phase' tests/test_edit_guard.py` → `3`. 통과
  - 10: `grep -n "verify\|LESSONS\|worktree" docs/PRD.md docs/ARCHITECTURE.md README.md AGENTS.md` → 0줄(종료 코드 1). 규칙 구간 `diff` → 출력 없음(종료 코드 0). `grep -hF '| `docs/tasks/' AGENTS.md plugins/plate/skills/setup/SKILL.md | sort -u | wc -l` → `1`. `grep -c "^## 명령" docs/ARCHITECTURE.md` → `1`, 빌드 없음·린트 없음·테스트 `python3 -m unittest discover -s tests`. PRD 핵심 기능 5, 7, 8과 ARCHITECTURE의 디렉터리 구조, 패턴과 규칙, 데이터 흐름을 읽음 → 아홉 스킬과 새 흐름을 말한다. 통과
  - 11: `grep -n "^### ADR-020" docs/ADR.md` → `28:### ADR-020: plate 자체의 고칠 거리는 GitHub 이슈로 모은다` 1줄. 결정, 이유, 트레이드오프가 있다. 통과
  - 12: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `  "version": "0.10.0",`. 두 `description`에 setup, context, plan, run, phase, check, retro, review, eval이 있고 verify가 없다. 통과
  - 13: `N=$(ls -t plugins/plate/skills/*/SKILL.md plugins/plate/hooks/*.py plugins/plate/hooks/*.json | head -1); find ~/plate-rail-test/logs -name '*.jsonl' -newer "$N"` → N은 `plugins/plate/skills/run/SKILL.md`(10월 19 16:28, 작업 트리 변경 없음). 나온 기록은 `t3-setup-1`~`2`, `t3-plan-1`~`12`, `t3-plan-add`, `t3-run-1`~`3`, `t3-all-1`~`4`, `t3-again-1`~`3`, `t3-stop-1`~`2`로 네 장면이 모두 든다. 기록의 init에서 plate는 `/Users/gangjungi/Desktop/harness-plate/plugins/plate`, 0.10.0이다. 통과
  - 14: `docs/TOOLS.md`의 Claude Code 절을 읽음 → 버전 줄에 2.1.302(2026-10-18)와 2.1.303(2026-10-19), "tasks 실행의 판정에서 본 것"(2.1.302, gh 2.89.0, 2026-10-18)에 에이전트 결과의 사용량(`<usage>subagent_tokens …`, `totalTokens` 등), `gh issue create`·`comment`·`delete`와 출력, 시험 폴더(`tasksmake.sh`의 여섯 폴더, `-try1`, `-try2`)와 기록 위치(`logs/<이름>-<턴>.jsonl`, `t2-`, `t3-`), 판정마다의 실행 시간. 통과
  - 15: `python3 -m unittest discover -s tests` → 마지막 줄 `OK`. 통과

**문제**
- 없음

**판정**: 통과
