# Phase 10: setup·plan과 run task 하나씩을 시험한다

**목표**: 바뀐 본문으로 setup·plan 장면과 run task 하나씩 장면을 헤드리스로 돌려 완료 조건 3, 4, 5를 확인한다.

**테스트 먼저**: 아니오 — 이 레포의 코드를 바꾸지 않는다. 시험 폴더와 도구는 저장소 밖(`~/plate-rail-test`)에 둔다.

**읽을 것**
- `docs/TOOLS.md` (헤드리스 실행의 꼴, 허용 목록, 막히는 명령의 꼴, 세션 잇기, 답을 미리 주면 묻지 않는다는 것, 실행 시간)
- `~/plate-rail-test/bin/run.sh` (지난 시험의 실행 도구와 허용 목록)
- `~/plate-rail-test/bin/vfmake.sh` (지난 시험 폴더를 만드는 법)
- `plugins/plate/skills/setup/SKILL.md`, `plugins/plate/skills/plan/SKILL.md`, `plugins/plate/skills/run/SKILL.md`, `plugins/plate/skills/check/SKILL.md`, `plugins/plate/skills/retro/SKILL.md` (기대하는 동작)

**TODO**
- [x] `~/plate-rail-test`의 실행 도구가 새 스킬(check, review, eval)과 `gh`를 허용 목록에 담고, 이 단계의 시험 폴더를 만드는 도구가 생긴다
- [x] setup·plan 장면이 돈다: 커밋이 없는 빈 git 레포에서 setup을 부르고, 셋업된 작은 프로젝트(`docs/ARCHITECTURE.md`에 명령 절이 없다)에서 task 둘 이상이 나올 요청으로 plan을 부른다. 답을 미리 주지 않고 턴마다 이어 승인하며, 승인 전 턴마다 `git status --short`와 `ls docs/tasks`를 남긴다. 쓴 뒤에는 tasks가 진행 중인 그 폴더에서 새 요청으로 plan을 다시 부른다
- [x] run task 하나씩 장면이 돈다: task 둘 이상이 계획된 테스트가 있는 작은 프로젝트에서 run을 부르고, 방식은 "task 하나씩"으로 답해 첫 task의 회고 뒤 물음까지 간다
- [x] 장면의 기록이 `~/plate-rail-test/logs/`에 남는다
- [x] 완료 조건 3, 4, 5의 확인을 모두 돌려 결과를 기록에 적는다

**통과 조건**
- 완료 조건 3이 참이다
  - 확인: 완료 조건 3의 확인을 모두 돌린다
- 완료 조건 4가 참이다
  - 확인: 완료 조건 4의 확인을 모두 돌린다
- 완료 조건 5가 참이다
  - 확인: 완료 조건 5의 확인을 모두 돌린다

## 한 일
- `~/plate-rail-test`의 실행 도구가 새 스킬(check, review, eval)과 `gh`를 허용 목록에 담고, 이 단계의 시험 폴더를 만드는 도구가 생긴다: `bin/run.sh`의 허용 목록 갈래가 `run|phase|check|retro|review|eval|verify`가 되고 그 목록 끝에 `"Bash(gh:*)"`가 더해졌다(사용법 줄의 스킬 목록도 고침). `bin/tasksmake.sh`가 생겼다. `t-setup`(커밋이 없는 빈 git 레포), `t-plan`(바탕 `t-base`: test-base의 booklog를 새 git 이력 하나로 옮기고 옛 `docs/tasks/001-core-commands`와 `docs/LESSONS.md`를 빼고, `AGENTS.md`를 지금 setup 본문의 두 구간으로 쓴 것. 명령 절이 없다), `t-run`(`t-base`에 명령 절을 더하고 tasks `list-delete`의 계획 파일을 손으로 써서 `plan: list-delete`로 커밋. task `001-list-command`는 phase 둘, `002-delete-command`는 phase 하나)을 만든다. 턴 하나를 돌리고 끝난 뒤의 `git status --short`, `ls docs/tasks`, `git log --oneline -3`, 브랜치를 `logs/<이름>.state`에, 세션 id를 `logs/<이름>.sid`에 남기는 `bin/tturn.sh`와, run 기록에서 메인이 띄운 에이전트와 돌아온 사용량을 세는 `bin/tagents.py`도 생겼다 (`~/plate-rail-test/bin/run.sh`, `~/plate-rail-test/bin/tasksmake.sh`, `~/plate-rail-test/bin/tturn.sh`, `~/plate-rail-test/bin/tagents.py`)
- setup·plan 장면이 돈다: `t-setup`에서 `/plate:setup`(답 없이, 24초) → 화면이 있는지 묻고 멈춤 → "아니요. 화면이 없는 프로젝트다"(310초) → 셋업하고 보고로 끝남. `t-plan`에서 요청 "booklog에 책 목록 보기(`booklog list`)와 책 지우기(`booklog delete <번호>`)를 더한다. 목록 보기를 먼저 하고, 지우기는 그다음 task로 나눈다."로 `/plate:plan`을 부르고 답을 미리 주지 않고 아홉 턴을 이었다(155, 9, 8, 7, 71, 41, 50, 47, 75초). 1~5턴은 물음 하나씩(빌드·린트 명령, 지운 책의 메모, 지우기 전 확인, 빈 목록의 출력, 엣지케이스 논의)이고 추천안(엣지케이스만 "논의하지 않는다"와 이유)으로 답했다. 6턴이 tasks 머리 초안, 7턴이 `001-book-list` 초안, 8턴이 `002-book-delete` 초안이고 셋 모두 "승인한다."로 답했다. 9턴에 다섯 파일을 쓰고 `f29d6a4 plan: book-list-delete`로 커밋했다. 턴마다 `logs/t-plan-N.state`에 상태를 남겼다. 그 뒤 같은 폴더에서 새 세션으로 "booklog에 책 제목 고치기(`booklog rename <번호> <새 제목>`)를 더한다."로 plan을 다시 불렀고(23초) 지금 tasks에 더할지 묻고 멈췄다. 답하지 않아 아무것도 쓰지 않았다. plan의 답글은 1~8턴이 영어, 9턴과 다시 부른 턴이 한국어였다 (`~/plate-rail-test/t-setup`, `~/plate-rail-test/t-plan`, `~/plate-rail-test/answers/t-setup-2.md`, `~/plate-rail-test/answers/t-plan-1.md`~`t-plan-6.md`, `~/plate-rail-test/answers/t-approve.md`, `~/plate-rail-test/answers/t-plan-add.md`)
- run task 하나씩 장면이 돈다: `t-run`에서 `/plate:run`(32초) → `tasks/list-delete` 브랜치를 만들고 실행 방식을 묻고 멈춤 → "task 하나씩으로 한다."(620초) → 에이전트 다섯(phase 1 수행 65초, 확인 33초, phase 2 수행 106초, 확인 24초, 회고 250초)을 띄우고, 회고 1이 통과한 뒤 다음 task로 갈지 묻고 멈춤 → "아니요. 다음 task로 가지 않고 여기서 멈춘다."(27초) → 보고로 끝남 (`~/plate-rail-test/t-run`, `~/plate-rail-test/answers/t-run-2.md`, `~/plate-rail-test/answers/t-run-3.md`)
- 장면의 기록이 `~/plate-rail-test/logs/`에 남는다: `t-setup-1`, `t-setup-2`, `t-plan-1`~`t-plan-9`, `t-plan-add`, `t-run-1`~`t-run-3`의 `.jsonl`, `.err`, `.base`, `.state`, `.sid`가 남았다 (`~/plate-rail-test/logs/`)
- 완료 조건 3, 4, 5의 확인을 모두 돌려 결과를 기록에 적는다: 아래 "확인 결과"에 적었다 (`docs/tasks/010-tasks-cycle/phase-10.md`)

## 확인 결과
- 완료 조건 3이 참이다
  - `grep -n "plate:context\|이어서 채울지\|verify" plugins/plate/skills/setup/SKILL.md | wc -l` → `0`. 통과
  - `logs/t-setup-2.jsonl`의 `result`(setup을 부른 기록의 마지막 답)를 읽음 → "만든 것", "옮긴 것과 건드리지 않은 것", "직접 채울 칸"(`{…}`가 남은 파일 셋), 32KiB 알림으로 끝나고 물음표가 든 줄이 없다. 채울지, 이어 갈지 묻는 글이 없다. 통과
  - `t-setup/AGENTS.md`의 두 구간을 setup 본문의 "문서 지도 구간", "규칙 구간" 블록과 줄 단위로 견줌(python) → 문서 지도 구간은 본문에만 있는 줄이 `| \`docs/DESIGN.md\` | 디자인 토큰과 UI 규칙 | 화면을 만들거나 고칠 때 |` 하나이고 파일에만 있는 줄은 없다. 규칙 구간은 같다. `python3 bin/setupcheck.py t-setup PRD,ARCHITECTURE,ADR` → `=> 셋업 대조: 모두 통과`. 통과
  - `N=$(ls -t plugins/plate/skills/*/SKILL.md plugins/plate/hooks/*.py plugins/plate/hooks/*.json | head -1); find ~/plate-rail-test/logs -name '*.jsonl' -newer "$N"` (N은 `plugins/plate/hooks/edit_guard.py`) → `t-setup-1.jsonl`, `t-setup-2.jsonl`이 나온다. 통과
- 완료 조건 4가 참이다
  - `logs/t-plan-1`~`t-plan-9.jsonl`의 `result`에서 `쓸 위치` 줄과 승인 물음을 찾음(python) → 6턴 `쓸 위치: \`docs/tasks/plan.md\`` + "Should I go ahead with this tasks header?", 7턴 `쓸 위치: \`docs/tasks/001-book-list/\`` + "Should I go ahead with this task's draft?", 8턴 `쓸 위치: \`docs/tasks/002-book-delete/\`` + 같은 물음. 1~5턴과 9턴에는 승인 물음이 없다. tasks 머리에 한 번, task마다 한 번이다. 통과
  - `logs/t-plan-1`~`t-plan-8.state`(마지막 승인 전 턴마다 남긴 것)의 `git status --short`와 `ls docs/tasks` → 여덟 턴 모두 둘 다 빈 출력. 통과
  - `t-plan`에서 `git log -1 --stat` → `f29d6a4 plan: book-list-delete`에 `docs/tasks/plan.md`, `docs/tasks/001-book-list/plan.md`, `docs/tasks/001-book-list/phase-1.md`, `docs/tasks/002-book-delete/plan.md`, `docs/tasks/002-book-delete/phase-1.md` 다섯 파일(139줄)이 든다. `docs/tasks/plan.md`의 완료 조건 절에는 조건 넷과 확인이 있다. 통과
  - `grep -c '^## 명령' docs/ARCHITECTURE.md`(t-plan) → `0`. `docs/tasks/001-book-list/phase-1.md` 17번 줄이 TODO `` `docs/ARCHITECTURE.md`에 `## 명령` 절이 생기고 `- 빌드: 없음`, `- 린트: 없음`, `- 테스트: .venv/bin/pytest` 세 줄이 든다 ``. 통과
  - `logs/t-plan-add.jsonl`의 `result`를 읽음 → "**이 요청(`booklog rename <번호> <새 제목>`)을 지금 tasks에 task로 더할까요?**"와 더한다/더하지 않는다 두 갈래. `logs/t-plan-add.state` → `git status --short` 빈 출력, `git log` 맨 위가 그대로 `f29d6a4`. 통과
  - 위의 `find` → `t-plan-1.jsonl`~`t-plan-9.jsonl`, `t-plan-add.jsonl`이 나온다. 통과
- 완료 조건 5가 참이다
  - `t-run`에서 `git branch --show-current` → `tasks/list-delete`. `git log --oneline --reverse 3714b11..HEAD` → `001-list-command: phase 1`, `phase 1 확인`, `phase 1 통과`, `phase 2`, `phase 2 확인`, `phase 2 통과`, `001-list-command: 회고`가 이 순서다. 통과
  - `ls docs/tasks/001-list-command` → `done-phase-1.md`, `done-phase-2.md`, `plan.md`, `retro.md`. `phase-N.md`가 없다. 통과
  - `logs/t-run-1.jsonl`의 `result` → "**실행 방식을 골라 주세요.**"와 task 하나씩, tasks 일괄. `logs/t-run-2.jsonl`의 `result` → "`001-list-command`의 회고가 통과했습니다(회고 1, 문제 0개)" 뒤에 "**다음 task `002-delete-command`(책 지우기 명령)로 갈까요?**". 통과
  - `grep -c '^- 에이전트 |' docs/tasks/RUNLOG.md` → `5`, `python3 bin/tagents.py logs/t-run-1.jsonl logs/t-run-2.jsonl logs/t-run-3.jsonl` → `= 모두: 에이전트 5`(줄마다의 토큰, 도구 호출, 시간이 RUNLOG의 줄과 같다). 에이전트 줄 가운데 `토큰 [0-9]+ | 도구 호출 [0-9]+ | 시간 [0-9]+초`로 끝나지 않는 줄 → `0`. `grep -c '^- 물음 |' docs/tasks/RUNLOG.md` → `2`(실행 방식, 다음 task)이고 기록의 물음도 둘(t-run-1의 실행 방식, t-run-2의 다음 task)이다. `grep -c '^- \`001-list-command\`' docs/tasks/FRICTION.md` → `2`(문제 줄 둘). 통과
  - 위의 `find` → `t-run-1.jsonl`, `t-run-2.jsonl`, `t-run-3.jsonl`이 나온다. 통과

## 계획과 달라진 점
- TODO는 run을 "첫 task의 회고 뒤 물음까지" 돌리라고 했다. 그 물음에 "가지 않고 멈춘다"로 한 턴을 더 답했다(t-run-3). 까닭: RUNLOG는 답을 받을 때 물음 줄을 적으므로, 답하지 않으면 완료 조건 5의 "물은 줄 수가 기록의 물음 수와 같다"를 견줄 수 없다. 이 턴은 커밋을 만들지 않았고 RUNLOG에 `다음 task` 물음 줄만 더했다(커밋하지 않은 채 남음)
- 장면 run task 하나씩의 계획은 plan을 돌린 결과가 아니라 `bin/tasksmake.sh`가 손으로 쓴 tasks `list-delete`이고, 그 폴더의 `docs/ARCHITECTURE.md`에는 명령 절(빌드·린트 없음, 테스트 `.venv/bin/python -m pytest`)을 미리 넣었다. 까닭: 장면 setup·plan과 함께 돌려 시간을 줄이고, check와 retro가 명령 절의 테스트를 돌리는지 보려고

## 남은 것
없음

## 하네스에서 걸린 것
- run 본문의 "`RUNLOG.md`"(돌아올 때마다 한 줄을 더하고 6번의 커밋에 함께 넣는다)를 메인이 한 번 어겼다. phase 1 확인 에이전트의 줄을 적기 전에 `001-list-command: phase 1 통과`(576e0ce)를 커밋해 그 커밋의 RUNLOG에는 그 줄이 없고, phase 2 수행 줄과 함께 적어 phase 2 통과 커밋에 넣었다. 파일의 줄과 차례는 맞다. 메인이 보고에 스스로 적었다(`logs/t-run-3.jsonl`)
- 허용 목록 밖의 꼴로 막힌 명령이 실행을 늘렸다(막힌 하나마다 약 65초, `docs/TOOLS.md`의 사실과 같다): setup의 명령 넷(`: > docs/tasks/.gitkeep`을 이은 것, `for` 변수를 쓴 것, `xxd`를 이은 것, `git -C <절대 경로> status`. t-setup-2가 310초), run 메인의 `git -C <절대 경로> status`와 `awk`, 회고 에이전트의 따옴표 든 이은 명령과 `/tmp` 쓰기(회고 250초)
- 회고 에이전트가 `FRICTION.md`에 하네스의 문제 줄 둘을 적었다: plan이 쓴 완료 조건의 확인이 `result.output`(표준 출력과 표준 오류를 합친 것)을 봐 "표준 출력으로"를 다 보지 못한다는 것, 완료 조건의 확인과 명령 절의 테스트가 같은 명령이라 check와 retro가 두 번 돌린다는 것(`~/plate-rail-test/t-run/docs/tasks/FRICTION.md`). 손으로 쓴 시험 계획에서 난 것이라 이 레포의 본문을 고칠 거리인지는 보지 않았다
- plan이 한국어 요청에 1~8턴을 영어로 답했다(setup과 run은 한국어). 시험 세션에 실리는 사용자 전역 지침의 영향으로 보이나 확인하지 않았다. 판정에는 걸리지 않았다
