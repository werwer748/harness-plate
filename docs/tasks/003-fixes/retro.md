# 회고

## 회고 1

**확인**
- 1. plan 6번·**조건**의 세 경우 규칙과 run 8번의 고칠 쪽 계획에서의 멈춤을 헤드리스 시험(작업 트리의 `--plugin-dir`)으로 돌린다
  - run: phase 기록의 `mk_run.sh`로 새로 차린 시험 레포(scratchpad `retro1/run/repo`: `tasks/x`, tasks 일괄 `RUNLOG.md`, 고칠 쪽이 계획인 문제가 든 `retro.md`, 합쳐지지 않은 `report/a`)에서 `claude -p '/plate:run' --plugin-dir /Users/hugo/Desktop/harness-plate/plugins/plate --permission-mode bypassPermissions --output-format json` → "계획대로 실행하다가 멈췄습니다. `001-report`의 회고가 계획 자체를 문제로 짚었기 때문입니다", "고칠 phase만 더해서는 고칠 수 없습니다"와 결정·완료 조건을 고칠 안, "이 해결책으로 갈까요?". "이번 세션에서는 에이전트를 띄우지 않았고 커밋도 하지 않았습니다". 뒤에 `ls docs/tasks/001-report` → `done-phase-1.md plan.md retro.md`(`phase-2.md` 없음), `git status --porcelain` 빈 출력, HEAD `001-report: RUNLOG` 그대로. 통과
  - plan: `mk_plan.sh`로 새로 차린 시험 레포(`retro1/plan/repo`: 로컬 `report/a`에 `reports/1.md`, origin에만 있는 `report/b`에 `reports/2.md`)에서 `claude -p '/plate:plan `scripts/new_report.sh`에 `-n <개수>` 옵션을 더해, 새 보고서를 한 번에 그 개수만큼 만들게 해 줘.' --plugin-dir … --permission-mode bypassPermissions --output-format json` → 첫 물음 "질문 1. 번호를 고를 때 무엇을 볼까요?" 앞에 "`report/a`(로컬과 origin)에는 `reports/1.md`가, `origin/report/b`에는 `reports/2.md`가 있습니다 … 번호가 겹칩니다"를 들었고, 물음의 B안이 그 브랜치들의 번호를 피하는 것이다. `git status --porcelain` 빈 출력, 브랜치 `main`·`report/a`. 통과
  - 시험한 본문 해시 `git hash-object` → plan `eb1eaa78021d47857aa64fdfb340d3e89a211c0a`, run `a1745943192388f6a07aea6b666315c4271d3996`, retro `684f526efee0df1a7a919100a95275fc794d0592`(phase 기록과 같다)
- 2. tasks 완료 조건 1, 2, 3, 4, 5, 6이 참이다.
  - tasks 완료 조건 1: `python3 -m unittest discover -s tests` → `Ran 275 tests in 22.991s`, 마지막 줄 `OK`. 통과
  - tasks 완료 조건 2: `grep -n '합쳐지지 않은 다른 브랜치' plugins/plate/skills/plan/SKILL.md plugins/plate/skills/retro/SKILL.md` → plan 115(`## 6. 초안을 보여 주고 승인받는다` 102줄 아래), plan 266(**조건** 260줄 아래), retro 79(`## 4. task의 변경을 점검한다` 아래). 통과
  - tasks 완료 조건 2: `cp -R` 사본에서 `sed -i '' '/합쳐지지 않은 다른 브랜치/d' plugins/plate/skills/plan/SKILL.md plugins/plate/skills/retro/SKILL.md` 뒤 `python3 -m unittest tests.test_skill_rules.PlanRulesTest.test_80_names_left_anywhere_covered tests.test_skill_rules.RetroRulesTest.test_80_retro_names_left_anywhere` → `FAILED (failures=3)`. 통과
  - tasks 완료 조건 3: `mk_retroA.sh`로 새로 차린 시험 레포(`retro1/rA/repo`: 지난 tasks의 `001-x: phase 1`(old.txt)이 남음)에서 `claude -p '/plate:retro docs/tasks/001-x' --plugin-dir … --permission-mode bypassPermissions --output-format json` → `판정: 통과`, 커밋 `001-x: 회고`. `grep -c old.txt docs/tasks/001-x/retro.md` → 0, `grep -c new.txt` → 2. 통과
  - tasks 완료 조건 4: `mk_retroB.sh`로 새로 차린 시험 레포(`retro1/rB/repo`)에서 `claude -p '/plate:retro docs/tasks/001-report' …` → 첫 줄 `판정: 문제 있음`. `retro.md` 17·18줄의 문제 줄에 `기준: 계획. 고칠 쪽: 계획`, 20줄 `**판정**: 문제 있음`. 통과
  - tasks 완료 조건 4: `grep -n '고칠 쪽' plugins/plate/skills/run/SKILL.md` → 108, 209(`## 8. 고칠 phase를 더한다` 207줄 아래), 298(`## 멈춘다` 289줄 아래), 593. `cp -R` 사본에서 `sed -i '' '/고칠 쪽/d' plugins/plate/skills/run/SKILL.md` 뒤 `python3 -m unittest tests.test_skill_rules.RunRulesTest.test_80_plan_side_problem_stops` → `FAILED (failures=1)`. 통과
  - tasks 완료 조건 5: `grep -n '고칠 쪽' docs/PRD.md docs/ARCHITECTURE.md` → PRD 17(핵심 기능 7), ARCHITECTURE 40(디렉터리 구조의 `test_skill_rules.py`), 55(run 문단), 75(데이터 흐름의 실행), 101(멈춤 문단). 통과
  - tasks 완료 조건 6: `grep -n '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "1.0.0"`. 통과
  - tasks 완료 조건 6: `grep -n '1.0.0' docs/PRD.md` → 21 `9단계까지 만들어 1.0.0을 냈다.`. 통과
  - 저장소 불변: 네 헤드리스 시험 전후 `git status --porcelain` → 빈 출력, `git rev-parse HEAD` → `47028f6…` 그대로. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 275 tests`, `OK`. 통과

**남은 것**
- phase 1: run 시험은 tasks 일괄 갈래만 돌렸다. task 하나씩 갈래와, 고칠 쪽이 계획이 아닌 문제에서 고칠 phase를 더하는 갈래는 돌리지 않았다 → 문제 아님 (완료 조건 1과 소스 문제가 보는 동작은 run 8번의 고칠 쪽 계획에서의 멈춤이고, 이 회고의 다시 돌림에서도 tasks 일괄에서 `phase-2.md` 없이 멈췄다. 멈춤 규칙(`run/SKILL.md` 298줄)은 실행 방식을 가리지 않는다)
- phase 1: plan 시험은 첫 물음까지만 돌려 초안 점검(6번)의 확인 목록은 보지 않았다 → 문제 아님 (완료 조건 1의 기대가 "초안 점검이나 첫 물음"이고, 첫 물음 앞의 글과 물음의 갈래가 합쳐지지 않은 두 브랜치의 같은 이름을 들었다)
- phase 1: 헤드리스 시험은 한 번씩만 돌려 되풀이를 보지 않았다 → 문제 아님 (완료 조건은 되풀이를 요구하지 않고, 확인 1과 이 회고에서 새로 차린 레포로 두 번 더 돌려 같은 결과가 났다)

**문제**
- 없음

**판정**: 통과
