# Phase 1: tasks 끝의 문제를 고친다

**목표**: task 머리의 완료 조건에 적힌 것을 모두 고친다.

**테스트 먼저**: 아니오 — 고칠 것은 결과물인 마크다운(plan·run 본문)의 동작을 헤드리스로 돌려 보는 확인이고, 코드 파일의 동작을 바꾸지 않는다

**읽을 것**
- `docs/tasks/review.md`의 `## 평가 1` 절
- `docs/tasks/eval.md`의 `## eval 1` 절
- `plugins/plate/skills/plan/SKILL.md`
- `plugins/plate/skills/run/SKILL.md`
- `tests/test_skill_rules.py`
- `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `docs/BACKLOG.md`, `docs/cleanup/`

**TODO**
- [x] plan 6번·**조건**의 세 경우 규칙과 run 8번의 고칠 쪽 계획에서의 멈춤에 돌려 보는 확인이 없고, grep·단위 시험과 `돌리지 않음` 줄만 있다. 헤드리스 시험으로 두 규칙을 돌려 결과를 기록에 남기고, 고칠 동작을 적은 맥락 문서의 줄과 그 글을 지키는 테스트도 맞춘다 (`plugins/plate/skills/plan/SKILL.md`, `plugins/plate/skills/run/SKILL.md`, `docs/TOOLS.md`, `tests/test_skill_rules.py`)

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다

## 한 일
- plan 6번·**조건**의 세 경우 규칙과 run 8번의 고칠 쪽 계획에서의 멈춤에 돌려 보는 확인이 없고, grep·단위 시험과 `돌리지 않음` 줄만 있다. 헤드리스 시험으로 두 규칙을 돌려 결과를 기록에 남기고, 고칠 동작을 적은 맥락 문서의 줄과 그 글을 지키는 테스트도 맞춘다: 두 규칙을 헤드리스(작업 트리의 `--plugin-dir /Users/hugo/Desktop/harness-plate/plugins/plate --permission-mode bypassPermissions`)로 돌려 아래 "확인 결과"에 남겼다. 묻는 스킬과 에이전트를 띄우는 스킬도 헤드리스로 첫 물음이나 멈추는 자리까지 돈다는 도구 사실을 `docs/TOOLS.md`의 Claude Code 절에 한 줄 더했다 (`docs/TOOLS.md`). plan·run 본문과 `tests/test_skill_rules.py`는 고치지 않았다(아래 "계획과 달라진 점")

## 확인 결과
- 완료 조건 1: plan 6번·**조건**의 세 경우 규칙과 run 8번의 멈춤을 헤드리스 시험으로 돌린다
  - run: 시험 레포(scratchpad `p1/runA.wC26/repo`. `main`에서 갈라진 `tasks/x`에 tasks 머리(이름 x, 목표 "새 보고서 이름이 다른 브랜치의 보고서와 겹치지 않는다", 결정 "작업 트리의 `reports/`만 본다"), `001-report/done-phase-1.md`(확인 1 통과), `retro.md` 회고 1(문제 한 줄 `기준: 계획. 고칠 쪽: 계획`, `판정: 문제 있음`), `RUNLOG.md`의 `물음 | 실행 방식 | … | 답: tasks 일괄`. 합쳐지지 않은 `report/a`에 `reports/1.md`. 모두 커밋)에서 `claude -p '/plate:run' --plugin-dir … --permission-mode bypassPermissions --output-format json` → 결과 첫 줄 "실행이 멈췄습니다. … 실행 방식은 tasks 일괄이지만, 계획이 틀린 경우에는 고칠 phase를 더하지 않고 멈추게 되어 있습니다. 파일은 아무것도 고치지 않았고, 이번 세션에서 에이전트도 띄우지 않았습니다", 원인과 계획을 고칠 안을 보이고 승인을 물었다. 뒤에 `ls docs/tasks/001-report` → `done-phase-1.md plan.md retro.md`(`phase-2.md` 없음), `git status --porcelain` → 빈 출력, HEAD는 `001-report: RUNLOG` 그대로. 통과
  - plan: 시험 레포(scratchpad `p1/planA.HrSd/repo`. `main`에 작업 트리의 `reports/`만 보고 번호를 고르는 `scripts/new_report.sh`, 합쳐지지 않은 로컬 `report/a`에 `reports/1.md`, `git clone --bare`로 만든 origin에만 있는 `report/b`에 `reports/2.md`, `git remote set-head origin main`)에서 `claude -p '/plate:plan `scripts/new_report.sh`에 `-n <개수>` 옵션을 더해, 새 보고서를 한 번에 그 개수만큼 만들게 해 줘.' --plugin-dir … --permission-mode bypassPermissions --output-format json` → 첫 물음 "질문 1. 번호를 고를 때 합쳐지지 않은 다른 브랜치의 보고서도 피할까요?"가 "`report/a`(로컬과 origin)에 `reports/1.md`, `origin/report/b`에 `reports/2.md`가 있고 … `-n 3`을 돌리면 `1.md`, `2.md`, `3.md`가 만들어져 두 브랜치와 번호가 겹칩니다"를 들었다. 파일은 쓰지 않았다(`git status --porcelain` 빈 출력, 브랜치 `main`, `report/a`뿐). 통과
  - 시험한 본문 해시: `git hash-object` → run `a1745943192388f6a07aea6b666315c4271d3996`, plan `eb1eaa78021d47857aa64fdfb340d3e89a211c0a`(이 phase는 두 본문을 고치지 않았다)
- 완료 조건 2 / tasks 완료 조건 1: `python3 -m unittest discover -s tests` → `Ran 275 tests in 23.892s`, 마지막 줄 `OK`. 통과
- tasks 완료 조건 2
  - `grep -n '합쳐지지 않은 다른 브랜치' plugins/plate/skills/plan/SKILL.md plugins/plate/skills/retro/SKILL.md` → plan 115(6번), plan 266(**조건**), retro 79(4번). 통과
  - `cp -R` 사본에서 `sed -i '' '/합쳐지지 않은 다른 브랜치/d' plugins/plate/skills/plan/SKILL.md plugins/plate/skills/retro/SKILL.md` 뒤 `python3 -m unittest tests.test_skill_rules.PlanRulesTest.test_80_names_left_anywhere_covered tests.test_skill_rules.RetroRulesTest.test_80_retro_names_left_anywhere` → `FAILED (failures=3)`. 통과
- tasks 완료 조건 3: 시험 레포 A(scratchpad `p1/retroA.BpvT/repo`. `plan: 옛 tasks` → `001-x: phase 1`(old.txt) → `x: 비움` → `plan: 새 tasks` → `001-x: phase 1`(new.txt) → `001-x: phase 1 통과`(`done-phase-1.md`))에서 `claude -p '/plate:retro docs/tasks/001-x' --plugin-dir … --permission-mode bypassPermissions --output-format json` → `판정: 통과`, 커밋 `001-x: 회고`. 그 `retro.md`에서 `grep -c 'old.txt'` → 0, `grep -c 'new.txt'` → 2. 통과
- tasks 완료 조건 4
  - 시험 레포 B(scratchpad `p1/retroB.kVM9/repo`. 위 run 시험 레포에서 회고·RUNLOG 커밋을 뺀 꼴)에서 `claude -p '/plate:retro docs/tasks/001-report' …` → 첫 줄 `판정: 문제 있음`. `retro.md`의 "**문제**" 줄에 `기준: 계획. 고칠 쪽: 계획`. 통과
  - `grep -n '고칠 쪽' plugins/plate/skills/run/SKILL.md` → 108(2번), 209(8번 "고칠 phase를 더한다"), 298("멈춘다"), 593. 통과
  - `cp -R` 사본에서 `sed -i '' '/고칠 쪽/d' plugins/plate/skills/run/SKILL.md` 뒤 `python3 -m unittest tests.test_skill_rules.RunRulesTest.test_80_plan_side_problem_stops` → `FAILED (failures=1)`. 통과
  - retro 본문 해시 `git hash-object plugins/plate/skills/retro/SKILL.md` → `684f526efee0df1a7a919100a95275fc794d0592`
- tasks 완료 조건 5: `grep -n '고칠 쪽' docs/PRD.md docs/ARCHITECTURE.md` → PRD 17(핵심 기능 7), ARCHITECTURE 55(run 문단), 75(데이터 흐름의 실행), 101(멈춤 문단), 40(디렉터리 구조). 통과
- tasks 완료 조건 6
  - `grep -n '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "1.0.0"`. 통과
  - `grep -n '1.0.0' docs/PRD.md` → 21줄 `9단계까지 만들어 1.0.0을 냈다.`. 통과
- 헤드리스 시험의 저장소 불변(`docs/tasks/RUNLOG.md`와 이 phase가 고치는 파일을 빼고 본다): 시험 전 `git status --porcelain` → ` M docs/tasks/RUNLOG.md`, `git rev-parse HEAD` → `e5fba5f…`. 시험 뒤 → ` M docs/TOOLS.md`(이 phase의 편집), ` M docs/tasks/RUNLOG.md`, HEAD `e5fba5f…`. 통과

## 계획과 달라진 점
- TODO가 고칠 파일로 든 `plugins/plate/skills/plan/SKILL.md`, `plugins/plate/skills/run/SKILL.md`, `tests/test_skill_rules.py`는 고치지 않았다. 소스 문제는 두 규칙에 돌려 보는 확인이 없다는 것이고, 헤드리스 시험이 두 규칙 모두 기대대로 돌아 본문을 고칠 결함이 나오지 않았다. 본문의 글이 그대로라 그 글을 지키는 테스트도 고칠 것이 없다. plan **조건**의 "돌릴 수 없으면(사용자에게 묻는 스킬, …)"을 바꾸는 것은 plate 자체의 하네스 고침이라 task 머리의 범위 밖이다
- 완료 조건 2의 tasks 완료 조건 3·4 헤드리스 retro 시험은 지난 phase의 시험 레포가 남아 있지 않아 같은 꼴로 새로 차려 돌렸다

## 남은 것
- run 시험은 tasks 일괄 갈래만 돌렸다. task 하나씩 갈래와, 고칠 쪽이 계획이 아닌 문제에서 고칠 phase를 더하는 갈래는 돌리지 않았다(완료 조건이 정한 장면이 아니다)
- plan 시험은 첫 물음까지만 돌렸다. 답을 이어 초안 점검(6번)의 확인 목록까지는 보지 않았다(완료 조건은 "초안 점검이나 첫 물음"이다)
- 헤드리스 시험은 한 번씩만 돌려 되풀이마다 같은 결과가 나는지는 보지 않았다

## 하네스에서 걸린 것
- plan **조건**이 "사용자에게 묻는 스킬"을 돌릴 수 없는 예로 들어 `돌리지 않음` 줄을 부르지만, 이 phase에서 plan과 run 모두 헤드리스로 첫 물음과 멈추는 자리까지 돌았다. 그 예를 좁히는 것은 plate 자체의 하네스 고칠 거리라 이 task에서 고치지 않았다(`plugins/plate/skills/plan/SKILL.md`의 "적는 규칙" **조건**)

## 확인 1

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 완료 조건 1, run: phase 기록의 `mk_run.sh`로 새로 차린 시험 레포(scratchpad `chk1/run/repo`: `tasks/x`에 tasks 일괄 `RUNLOG.md`, 고칠 쪽이 계획인 문제가 든 `retro.md`, 합쳐지지 않은 `report/a`)에서 `claude -p '/plate:run' --plugin-dir /Users/hugo/Desktop/harness-plate/plugins/plate --permission-mode bypassPermissions --output-format json` → "회고가 계획 자체에 문제가 있다고 판정해서, 여기서 멈추고 결정을 여쭤봅니다", "tasks 일괄이어도 고칠 phase를 … 더하지 않고, 여기서 멈췄습니다"와 계획을 고칠 안. 뒤에 `ls docs/tasks/001-report` → `done-phase-1.md plan.md retro.md`(`phase-2.md` 없음), `git status --porcelain` 빈 출력, HEAD `001-report: RUNLOG` 그대로. 통과
  - 완료 조건 1, plan: `mk_plan.sh`로 새로 차린 시험 레포(`chk1/plan/repo`: 로컬 `report/a`에 `reports/1.md`, origin에만 `report/b`에 `reports/2.md`)에서 `claude -p '/plate:plan `scripts/new_report.sh`에 `-n <개수>` 옵션을 더해, 새 보고서를 한 번에 그 개수만큼 만들게 해 줘.' --plugin-dir … --permission-mode bypassPermissions --output-format json` → 첫 물음을 담은 글이 "다른 브랜치에 아직 합쳐지지 않은 보고서가 있습니다. `report/a`에 `reports/1.md`, `origin/report/b`에 `reports/2.md`가 있습니다"를 들었다(이번 첫 물음 자체는 `-n` 값의 범위를 묻고, 브랜치의 같은 이름은 그 물음 앞의 확인한 것에 든다). 파일을 쓰지 않았다(`git status --porcelain` 빈 출력, 브랜치 `main`·`report/a`). 통과
  - tasks 완료 조건 1: `python3 -m unittest discover -s tests` → `Ran 275 tests`, 마지막 줄 `OK`. 통과
  - tasks 완료 조건 2: `grep -n '합쳐지지 않은 다른 브랜치' plugins/plate/skills/plan/SKILL.md plugins/plate/skills/retro/SKILL.md` → plan 115(`## 6. 초안을 보여 주고 승인받는다` 아래), plan 266(`**조건**` 아래), retro 79(`## 4. task의 변경을 점검한다` 아래). 통과
  - tasks 완료 조건 2: `cp -R` 사본에서 `sed -i '' '/합쳐지지 않은 다른 브랜치/d'`로 두 본문의 그 줄을 지우고 `python3 -m unittest tests.test_skill_rules` → `FAILED (failures=7)`, 그 가운데 `PlanRulesTest.test_80_names_left_anywhere_covered`(part 6, 조건), `RetroRulesTest.test_80_retro_names_left_anywhere`. 통과
  - tasks 완료 조건 3: `mk_retroA.sh`로 새로 차린 시험 레포(`chk1/rA/repo`: 지난 tasks의 `001-x: phase 1`(old.txt)이 남음)에서 `claude -p '/plate:retro docs/tasks/001-x' --plugin-dir … --permission-mode bypassPermissions --output-format json` → `판정: 통과`, 커밋 `001-x: 회고`. `grep -c old.txt docs/tasks/001-x/retro.md` → 0, `grep -c new.txt` → 2. 통과
  - tasks 완료 조건 4: `mk_retroB.sh`로 새로 차린 시험 레포(`chk1/rB/repo`)에서 `claude -p '/plate:retro docs/tasks/001-report' …` → 첫 줄 `판정: 문제 있음`. `retro.md` 17줄의 문제 줄에 `기준: 계획`, 19줄 `**판정**: 문제 있음`. 통과
  - tasks 완료 조건 4: `grep -n '고칠 쪽' plugins/plate/skills/run/SKILL.md` → 108, 209(`## 8. 고칠 phase를 더한다` 아래), 298(`## 멈춘다` 아래), 593. `cp -R` 사본에서 `sed -i '' '/고칠 쪽/d'` 뒤 `python3 -m unittest tests.test_skill_rules` → `FAILED (failures=6)`, 그 가운데 `RunRulesTest.test_80_plan_side_problem_stops`. 통과
  - tasks 완료 조건 5: `grep -n '고칠 쪽' docs/PRD.md docs/ARCHITECTURE.md` → PRD 17(핵심 기능 7), ARCHITECTURE 40(디렉터리 구조), 55(run 문단), 75(데이터 흐름의 실행), 101(멈춤 문단). 통과
  - tasks 완료 조건 6: `grep -n '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "1.0.0"`. `grep -n '1.0.0' docs/PRD.md` → 21 `9단계까지 만들어 1.0.0을 냈다.`. 통과
  - 저장소 불변(phase 커밋 뒤, `docs/tasks/RUNLOG.md`를 빼고): 시험 전후 `git status --porcelain` → ` M docs/tasks/RUNLOG.md`만, `git rev-parse HEAD` → `04dee7b…` 그대로. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 275 tests`, `OK`. 통과

**남은 것**
- run 시험은 tasks 일괄 갈래만 돌렸다(task 하나씩, 고칠 쪽이 계획이 아닌 갈래는 돌리지 않음) → 완료 조건 1이 보는 장면은 tasks 일괄에서 고칠 쪽이 계획인 문제의 멈춤이라 걸리지 않는다. 하네스에서 걸린 것
- plan 시험은 첫 물음까지만 돌렸다 → 완료 조건 1은 "초안 점검이나 첫 물음"을 보므로 걸리지 않는다. 하네스에서 걸린 것
- 헤드리스 시험을 한 번씩만 돌려 되풀이마다 같은 결과인지 보지 않았다 → 완료 조건은 그 장면에서 한 번 기대대로 도는지를 보고, 되풀이를 보지 않는다. 이 확인에서 새로 차린 레포로 다시 돌려 같은 결과가 났다. 하네스에서 걸린 것

**실패**
- 없음

**하네스에서 걸린 것**
- 남은 것: run 시험은 tasks 일괄 갈래만 돌렸다. task 하나씩 갈래와 고칠 phase를 더하는 갈래는 돌리지 않았다
- 남은 것: plan 시험은 첫 물음까지만 돌렸고 초안 점검(6번)의 확인 목록은 보지 않았다
- 남은 것: 헤드리스 시험은 되풀이를 보지 않았다(이 확인의 다시 돌림이 두 번째다)
- 완료 조건 1의 plan 기대 "초안 점검이나 첫 물음이 그 브랜치의 같은 이름을 드는지"는 첫 물음을 담은 글 전체로 보았다. 이번 돌림에서 첫 물음 자체는 `-n` 값을 묻고 같은 이름은 그 앞의 확인한 것에 들어, 수행 기록(첫 물음이 같은 이름을 물음)과 꼴이 달랐다. 기대가 "물음"과 "글"을 가르지 않아 판정이 읽기에 기댄다 (`docs/tasks/003-fixes/plan.md`의 완료 조건 1)

**판정**: 통과
