# 회고

## 회고 1

**확인**
- 완료 조건 1: plan 본문이 브랜치 규칙을 같은 뜻으로 적는다
  - `grep -n -e 'tasks/<이름>' plugins/plate/skills/plan/SKILL.md` → 3(description), 10(첫 문단), 19(절대 규칙 4), 26(낱말 tasks 머리), 54(1번), 137(7번), 167(양식 이름 줄), 235(적는 규칙 이름 줄). 요구한 여섯 곳이 모두 나온다. 통과
  - `grep -c -e '브랜치를 만들거나 바꾸지 않는다' plugins/plate/skills/plan/SKILL.md` → `0`. 통과
  - `(cd tests && python3 -m unittest test_skill_rules.PlanRulesTest.test_commits_on_tasks_branch)` → `Ran 1 test` / `OK`. 통과
- 완료 조건 2: run의 description과 1번의 앞선 커밋 까닭 글이 바뀐다
  - `grep -c -e 'plan은 브랜치를 바꾸지 않아서' -e '계획의 커밋이 로컬 기본 브랜치에만' plugins/plate/skills/run/SKILL.md` → `0`. 통과
  - `(cd tests && python3 -m unittest test_skill_rules.RunRulesTest.test_ahead_commits_reason)` → `Ran 1 test` / `OK`. 통과
  - `git diff 97a5a3f -- plugins/plate/skills/run/SKILL.md` → `## 1. 시작 조건을 본다`(75~96줄) 안의 hunk는 `@@ -88,7 +88,7 @@` 하나, 바뀐 줄은 "브랜치를 만들거나 바꾼 뒤에는 …" 한 줄이다. 그 줄의 `` `git remote get-url origin` ``부터 끝까지(`git log --oneline` 명령 둘을 담은 부분)는 고치기 전과 뒤가 글자 그대로 같고 바뀐 것은 까닭 글 한 문장뿐이다. `git branch -f` 줄은 diff에 없다. 통과
- 완료 조건 3: ARCHITECTURE와 README가 plan의 브랜치 동작과 맞는다
  - `grep -c -e '계획의 커밋이 로컬 기본 브랜치에만' docs/ARCHITECTURE.md README.md` → `docs/ARCHITECTURE.md:0`, `README.md:0`. 통과
  - `docs/ARCHITECTURE.md` 63~64줄(`→ 계획(` 줄과 바로 아래 `→` 줄)과 `README.md` 9줄(`` | `plan` | ``)을 읽음 → 둘 다 기본 브랜치이면 `tasks/<이름>`을 만들거나 바꾼다, `tasks/<이름>`이면 그대로, 그 밖이면 묻는다(거절하면 쓰지 않는다)의 세 갈래를 적는다. 통과
- 완료 조건 4: 작업 트리의 plan을 헤드리스로 돌린 두 장면
  - `done-phase-2.md`의 해시 `85a5bb1528ac6afabf3cce1741093fb2e5436585`와 다시 낸 `git hash-object plugins/plate/skills/plan/SKILL.md` → 같다(그 뒤 이 파일을 바꾼 커밋은 `dfcd0e5`뿐이다). 통과
  - 기록의 (가) → 브랜치 `tasks/readme-intro`, 제목 `plan: readme-intro`, 돌리기 전과 뒤의 `main`이 모두 `fbf90696…`. 남은 첫째 시험 저장소에서 `git -C … branch --show-current`, `log -1 --format=%s tasks/readme-intro`, `rev-parse main`을 다시 내도 같다. 통과
  - 기록의 (나) 응답 글 전문 → `feature/x`가 기본 브랜치도 `tasks/<이름>`도 아니라고 들고 "계획을 `tasks/<이름>` 브랜치에 커밋해도 될까요?"라고 묻는다. 그 자리의 브랜치 `feature/x`, 마지막 커밋 `fbf9069 init`, `git status --porcelain` 출력 없음. 둘째 시험 저장소에서 다시 내도 같고 `tasks/` 브랜치가 없다. 통과
- 완료 조건 5: 테스트가 모두 통과한다
  - `python3 -m unittest discover -s tests` → `Ran 207 tests` / `OK`. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 207 tests in 18.711s` / `OK`. 통과

**남은 것**
- phase 1: run 1번 3의 "계획의 커밋도 tasks의 커밋으로 세어진다"(되돌림 승인 갈래)를 명령 줄을 바꾸지 않는다는 통과 조건 때문에 그대로 두었다 → 문제 아님 (그 갈래는 고치기 전의 plan으로 세운 계획이 기본 브랜치에 있을 때 그대로 맞고, task 머리 완료 조건 2가 물음과 되돌림의 동작을 그대로 두기로 했다)
- phase 1: plan 본문의 새 브랜치 동작을 이 phase에서 돌려 보지 않았다 → 문제 아님 (phase 2의 헤드리스 시험이 (가)·(나) 두 장면을 돌렸고 이번 회고에서 시험 저장소를 다시 봤다)
- phase 2: (나)의 승인 뒤 `feature/x`에서 `tasks/<이름>`을 만드는 갈래와 거절해 끝나는 갈래는 돌리지 않았다 → 문제 아님 (task 머리 결정 "두 장면만 돌린다"가 정했고, 본문 1번의 "승인하면 2번으로 간다", "거절하면 아무것도 쓰지 않고 끝난다"와 7번의 "1번에서 승인받았으면 … `git switch -c tasks/<이름>`으로 지금 HEAD에서"를 직접 읽어 두 갈래가 적혀 있음을 봤다)
- phase 2: 두 시험 저장소가 `mktemp -d` 아래에 그대로 남아 있다 → 문제 아님 (이 저장소 밖이고, 완료 조건과 결정이 지우라고 하지 않는다)

**문제**
- 새 tasks를 다른 tasks의 브랜치(예: 앞 tasks가 끝난 뒤 남은 `tasks/old`)에서 계획하는 장면이 plan 본문에서 정해지지 않는다. 1번은 "기본 브랜치이거나 `tasks/<이름>`(더하는 경우는 그 tasks 머리의 이름)이면 묻지 않고" 가는데, 새 tasks의 `<이름>`은 6번에서야 정해져 1번에서 `tasks/old`가 `tasks/<이름>`인지 가를 수 없다. 묻지 않고 넘어가면 7번에서 지금 브랜치는 새 이름의 `tasks/<이름>`이 아니고(적는 규칙이 로컬에 있는 브랜치와 겹치지 않는 이름을 고르게 한다) 기본 브랜치도 1번의 승인도 아니어서 세 갈래 어디에도 들지 않아, 브랜치를 맞추지 않고 `tasks/old`에 커밋할 수 있다. task 머리 목표와 결정은 "기본 브랜치도 `tasks/<이름>`도 아닌 브랜치에서는 묻는다"로 이 장면을 묻는 쪽에 둔다 (`plugins/plate/skills/plan/SKILL.md` 54줄, 137줄). 기준: 결함

**판정**: 문제 있음

## 회고 2

**확인**
- 완료 조건 1: plan 본문이 브랜치 규칙을 같은 뜻으로 적는다
  - `grep -n -e 'tasks/<이름>' plugins/plate/skills/plan/SKILL.md` → 3(description), 10(첫 문단), 19(절대 규칙 4), 26(낱말 tasks 머리), 54(1번), 137(7번), 167(양식 이름 줄), 235(적는 규칙 이름 줄). 요구한 여섯 곳이 모두 나온다. 54줄은 기본 브랜치에서만(더하는 경우는 그 tasks의 `tasks/<이름>`에서도) 묻지 않고 새 tasks는 `tasks/old` 같은 다른 tasks의 브랜치에서도 묻는다고, 137줄은 그대로 두는 갈래를 더하는 경우로 좁히고 승인받았으면 `git switch -c`/`git switch`로 맞춘다고 적는다. 통과
  - `grep -c -e '브랜치를 만들거나 바꾸지 않는다' plugins/plate/skills/plan/SKILL.md` → `0`. 통과
  - `(cd tests && python3 -m unittest test_skill_rules.PlanRulesTest.test_commits_on_tasks_branch)` → `Ran 1 test` / `OK`. 통과
- 완료 조건 2: run의 description과 1번의 앞선 커밋 까닭 글이 바뀐다
  - `grep -c -e 'plan은 브랜치를 바꾸지 않아서' -e '계획의 커밋이 로컬 기본 브랜치에만' plugins/plate/skills/run/SKILL.md` → `0`. 통과
  - `(cd tests && python3 -m unittest test_skill_rules.RunRulesTest.test_ahead_commits_reason)` → `Ran 1 test` / `OK`. 통과
  - `git diff 97a5a3f -- plugins/plate/skills/run/SKILL.md` → `## 1. 시작 조건을 본다` 안의 hunk는 `@@ -88,7 +88,7 @@` 하나이고 바뀐 줄은 까닭 글을 담은 "브랜치를 만들거나 바꾼 뒤에는 …" 한 줄이다. 그 줄의 `git remote get-url origin`부터의 명령 부분과 `git branch -f` 줄(맥락 줄)은 그대로다. 나머지 hunk(낱말, 보고하고 묻는다, 고침 task의 꼴)는 `001-issue-criteria`의 변경이다. 통과
- 완료 조건 3: ARCHITECTURE와 README가 plan의 브랜치 동작과 맞는다
  - `grep -c -e '계획의 커밋이 로컬 기본 브랜치에만' docs/ARCHITECTURE.md README.md` → `README.md:0`, `docs/ARCHITECTURE.md:0`. 통과
  - `docs/ARCHITECTURE.md` 63~64줄과 `README.md` 9줄을 읽음 → 둘 다 기본 브랜치이면 `tasks/<이름>`을 만들거나 바꾼다, 더하는 경우 그 tasks의 `tasks/<이름>`이면 그대로, 그 밖(새 tasks면 다른 `tasks/…`도 든다)이면 묻고 거절하면 쓰지 않는다의 세 갈래를 적는다. 통과
- 완료 조건 4: 작업 트리의 plan을 헤드리스로 돌린 두 장면
  - `done-phase-3.md`의 해시 `d0441987f160dc18ca1b35c48cf4cf89df0041f5`와 다시 낸 `git hash-object plugins/plate/skills/plan/SKILL.md` → 같다. 이 파일을 마지막으로 바꾼 커밋은 `58cdde2`(phase 3)다. 통과
  - 기록의 (가) → 브랜치 `tasks/readme-intro`, 제목 `plan: readme-intro`, 돌리기 전과 뒤의 `main`이 모두 `22cffcdbea889ec0b29f9df1eb7075765f1e831f`. 남은 시험 저장소 `tmp.UDBlrwqD9w`에서 다시 내도 브랜치 `tasks/readme-intro`, `81a55df plan: readme-intro`, `main` `22cffcd…`로 같다. 통과
  - 기록의 (나) 응답 글 전문 → `feature/x`가 기본 브랜치도 `tasks/<이름>`도 아니라고 들고 "계획을 `tasks/<이름>` 브랜치에 커밋할까요?"라고 묻는다. 그 자리의 브랜치 `feature/x`, 마지막 커밋 `22cffcd init`, `git status --porcelain` 출력 없음. `tmp.V9sLbzZm7J`에서 다시 내도 같고 커밋은 `22cffcd init` 하나뿐이다. 통과
- 완료 조건 5: 테스트가 모두 통과한다
  - `python3 -m unittest discover -s tests` → `Ran 207 tests in 19.165s` / `OK`. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 207 tests in 19.165s` / `OK`. 통과

**남은 것**
- phase 1: run 1번 3의 "계획의 커밋도 tasks의 커밋으로 세어진다"(되돌림 승인 갈래)를 명령 줄을 바꾸지 않는다는 통과 조건 때문에 그대로 두었다 → 문제 아님 (고치기 전의 plan으로 세운 계획이 기본 브랜치에 있을 때 그대로 맞고, 완료 조건 2가 물음과 되돌림의 동작을 그대로 두기로 했다)
- phase 1: plan 본문의 새 브랜치 동작을 이 phase에서 돌려 보지 않았다 → 문제 아님 (phase 3의 헤드리스 시험이 고친 본문으로 (가)·(나)·(다)를 돌렸고 이번 회고에서 시험 저장소를 다시 봤다)
- phase 2: (나)의 승인 뒤와 거절 뒤 갈래는 돌리지 않았다 → 문제 아님 (task 머리 결정 "두 장면만 돌린다"가 정했고, 본문 1번의 "승인하면 2번으로 간다", "거절하면 아무것도 쓰지 않고 끝난다"와 7번의 "1번에서 승인받았으면 … `git switch -c tasks/<이름>`으로 지금 HEAD에서"를 직접 읽어 두 갈래가 적혀 있음을 봤다)
- phase 2: 두 시험 저장소가 `mktemp -d` 아래에 남아 있다 → 문제 아님 (이 저장소 밖이고, 완료 조건과 결정이 지우라고 하지 않는다)
- phase 3: (나)·(다)는 첫 턴만 돌려 승인 뒤 `tasks/<이름>`을 만드는 갈래, 거절해 끝나는 갈래는 돌리지 않았다 → 문제 아님 (task 머리 결정과 phase 3 TODO가 첫 턴만 돌리기로 정했고, 위의 1번·7번 글에 두 갈래가 적혀 있다. 7번은 새 tasks가 다른 `tasks/…`에서 승인받았어도 그 브랜치에 커밋하지 않고 새 이름으로 `git switch -c`한다고 적는다)
- phase 3: 절대 규칙 4의 "`tasks/<이름>`일 때는 그대로 두고"를 그대로 두었다 → 문제 아님 (새 tasks의 이름은 235줄대로 로컬 브랜치와 겹치지 않게 골라 그 갈래에 들 수 없어 1번·7번과 뜻이 어긋나지 않는다. `docs/ARCHITECTURE.md` 55줄의 같은 꼴의 글도 같은 까닭으로 어긋나지 않는다)
- phase 3: 세 시험 저장소가 `mktemp -d` 아래에 남아 있다 → 문제 아님 (이 저장소 밖이고, 완료 조건과 결정이 지우라고 하지 않는다)

**문제**
- 없음

**판정**: 통과
