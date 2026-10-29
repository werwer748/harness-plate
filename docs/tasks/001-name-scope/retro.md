# 회고

## 회고 1

**확인**
- 1. plan 6번과 **조건**, retro 4번이 세 경우를 든다
  - `grep -n '합쳐지지 않은 다른 브랜치' plugins/plate/skills/plan/SKILL.md plugins/plate/skills/retro/SKILL.md` → plan 115(6번), plan 266(**조건**), retro 79(4번) 세 줄이고, 줄마다 `지난 tasks의 같은 이름`과 `이름마다`가 저마다 1번 든다. 통과
  - `cp -R` 사본에서 `sed -i '' '/합쳐지지 않은 다른 브랜치/d' plugins/plate/skills/plan/SKILL.md plugins/plate/skills/retro/SKILL.md` 뒤 `python3 -m unittest tests.test_skill_rules.PlanRulesTest.test_80_names_left_anywhere_covered tests.test_skill_rules.RetroRulesTest.test_80_retro_names_left_anywhere` → `FAILED (failures=3)`. 통과
  - 돌리지 않음(plan을 헤드리스로 끝까지 돌리지 않는다): 완료 조건에 적힌 대로 돌리지 않았다
- 2. retro의 "task의 커밋"이 task 머리를 마지막으로 더한 커밋 뒤의 것만 센다
  - `grep -n -F '**task의 커밋**' plugins/plate/skills/retro/SKILL.md` → 31줄 하나, 그 줄에 `마지막으로 더한 커밋`이 있다. 통과
  - scratchpad의 새 `mktemp -d`(`r/A.wnJZ`)에 시험 레포 A를 차리고(지난 tasks의 `001-x: phase 1`이 `old.txt`, 비움 뒤 이번 tasks의 `001-x: phase 1`이 `new.txt`) `claude -p "/plate:retro docs/tasks/001-x" --plugin-dir /Users/hugo/Desktop/harness-plate/plugins/plate --permission-mode bypassPermissions --output-format json` → `판정: 통과`, 회고 커밋 `3232bd6 001-x: 회고`. 그 `docs/tasks/001-x/retro.md`에서 `grep -c 'old.txt'` → `0`, `grep -c 'new.txt'` → `2`. 통과
- 3. retro가 결정이 정한 동작이 목표를 해치는 꼴을 문제(기준: 계획, 고칠 쪽: 계획)로 판정한다
  - 새 `mktemp -d`(`r/B.8TjY`)에 시험 레포 B를 차리고(합쳐지지 않은 `report/a`에 `reports/1.md`, 결정 "작업 트리의 `reports/`만 본다") 같은 명령 → 결과 첫 줄 `판정: 문제 있음`. `retro.md` 17줄("**문제**" 아래)에 `기준: 계획`과 `고칠 쪽: 계획`이 함께 있다. 그 레포의 `FRICTION.md`에 `경계 밖` 0줄. 통과
  - 두 헤드리스 시험 전후로 이 저장소의 `git status --porcelain` → 전후 모두 빈 출력(`diff` 같음), `git rev-parse HEAD` → 전후 모두 `d5cd686…`. 통과
  - `git hash-object plugins/plate/skills/retro/SKILL.md` → `684f526efee0df1a7a919100a95275fc794d0592`, phase 2 기록의 해시와 같다(이 회고의 두 시험도 이 본문으로 돌았다). 통과
- 4. run 8번과 "멈춘다"가 고칠 쪽이 계획인 문제에서 고칠 phase를 더하지 않고 멈춘다
  - `grep -n '고칠 쪽' plugins/plate/skills/run/SKILL.md` → 108(2번), 209(8번 첫 문단), 298("멈춘다"), 593(`RUNLOG.md` 절). 8번과 "멈춘다"에 저마다 한 줄. 통과
  - `tests/test_skill_rules.py` 214줄에 `RunRulesTest.test_80_plan_side_problem_stops`가 있고, `cp -R` 사본에서 `sed -i '' '/고칠 쪽/d' plugins/plate/skills/run/SKILL.md` 뒤 그 시험 → `FAILED (failures=1)`. 통과
  - 돌리지 않음(run을 헤드리스로 끝까지 돌리지 않는다): 완료 조건에 적힌 대로 돌리지 않았다
- 5. 맥락 문서가 바뀐 동작과 맞다
  - `grep -n '고칠 쪽' docs/PRD.md docs/ARCHITECTURE.md` → PRD 17(핵심 기능 7), ARCHITECTURE 55(run 문단), 75(데이터 흐름의 실행 "회고의 문제는 고칠 phase를 더해 고친다" 줄), 101(멈춤 문단), 40(디렉터리 구조). 통과
  - `grep -n -F 'test_skill_rules.py' docs/ARCHITECTURE.md` → 40줄 하나. 그 줄의 `합쳐지지 않은 다른 브랜치`, `task 머리를 마지막으로 더한 커밋`, `고칠 쪽이 계획` → 1, 1, 1. 통과
- 6. 테스트 묶음이 모두 통과한다
  - `python3 -m unittest discover -s tests` → `Ran 275 tests`, 마지막 줄 `OK`. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 275 tests`, `OK`. 통과

**남은 것**
- phase 1: retro 4번의 그 줄은 아직 `경계 밖`으로 모은다 → 문제 아님 (phase 2가 그 줄을 "`경계 밖`으로도 돌리지 않고 "문제"에 `기준: 계획`, `고칠 쪽: 계획`으로 적는다"로 바꿨고, 79줄에서 직접 보았다)
- phase 2: task 머리를 더한 커밋을 찾는 `git log -1 --diff-filter=A … -- <task 폴더>/plan.md`가 `git mv`로 들어온 task 머리를 더한 것으로 치지 않을 수 있다 → 문제 아님 (task 머리는 plan이 새 파일로 써서 한 커밋으로 넣고, 이 task의 목표·결정이 덮는 세 경우(지난 tasks, 다른 브랜치, 이름마다)에 이름 바꾸기는 들지 않는다. 이 저장소에서도 그 명령이 `plan: repeat-names`(416bd77)를 냈다)
- phase 2: 헤드리스 시험을 되풀이마다 같은 판정이 나는지 보지 않았다 → 문제 아님 (수행, 확인, 이 회고에서 새로 차린 레포로 세 번 돌려 A는 `통과`·`old.txt` 0, B는 `문제 있음`·`기준: 계획. 고칠 쪽: 계획`으로 같았다)

**문제**
없음

**판정**: 통과
