# Phase 1: plan과 run의 본문, 맥락 문서, README, 테스트를 고친다

**목표**: plan 본문이 tasks 브랜치에 커밋하는 규칙을 적고, run 1번의 까닭 글과 맥락 문서, README가 그것과 맞고, 그것을 지키는 테스트가 있다.

**테스트 먼저**: 아니오 — 바뀌는 동작이 결과물인 마크다운(스킬 본문)의 것이다

**읽을 것**
- `plugins/plate/skills/plan/SKILL.md` (앞머리 description, 낱말의 "tasks 머리", 절대 규칙 4, "1. 진행 중인 tasks가 있는지 본다", "7. 쓰고 커밋한다", "8. 보고한다", 적는 규칙 "이름과 번호"의 tasks 머리 이름 줄, 양식의 `**이름**:` 줄)
- `plugins/plate/skills/run/SKILL.md` (앞머리 description, 낱말의 "기본 브랜치", "1. 시작 조건을 본다"의 3. tasks 브랜치. 이 절의 브랜치 물음은 plan이 따를 꼴이다)
- `tests/test_skill_rules.py` (`PlanRulesTest`, `RunRulesTest`의 1번 브랜치 테스트, `read`·`section`·`part` 도우미)
- `docs/ARCHITECTURE.md` (패턴과 규칙의 "run은 기본 브랜치(" 줄, 데이터 흐름의 `→ 계획(` 줄과 실행의 "tasks/<이름> 브랜치를 만들거나 바꾼 뒤" 줄, 디렉터리 구조의 `test_skill_rules.py` 줄)
- `README.md` (스킬 표의 `plan` 줄과 `run` 줄)
- `docs/PRD.md`, `docs/ADR.md`, `docs/TOOLS.md`, `docs/BACKLOG.md` (맥락 문서)

**TODO**
- [x] plan 본문이 바뀐다. 절대 규칙 4의 "브랜치를 만들거나 바꾸지 않는다"가 브랜치 규칙(기본 브랜치이면 쓰기 전에 `tasks/<이름>`을 만들거나 바꾸고, `tasks/<이름>`이면 그대로, 그 밖이면 1번에서 물어 승인받은 때만 바꾸고, 푸시하지 않는다)으로 바뀐다. 낱말에 run과 같은 정의의 "기본 브랜치"가 더해진다. 1번에 git 레포에서 기본 브랜치도 `tasks/<이름>`도 아닌 브랜치이면 지금 브랜치를 보여 주고 `tasks/<이름>`(이름은 초안에서 정한다. 더하는 경우는 그 tasks의 이름)에 커밋할지 묻고, 거절하면 아무것도 쓰지 않고 끝나는 갈래가 더해진다. 7번에서 쓰기 전에 브랜치를 만들거나(`git switch -c`, 지금 HEAD에서) 바꾸고(`git switch`), 실패하면 쓰지 않고 실패한 명령과 오류를 보고하고 끝나는 글이 더해진다. 적는 규칙의 이름 줄에 로컬에 같은 이름의 `tasks/<이름>` 브랜치가 없는 이름을 고르는 글이 더해진다(더하는 경우는 그 브랜치가 있으면 바꾼다). 8번의 보고에 커밋한 브랜치가 더해진다. description에 tasks 브랜치에 커밋한다는 것이 더해지고 1024자 안이다. 본문의 명령은 명령 치환 없이 한 명령씩 적는다 (`plugins/plate/skills/plan/SKILL.md`)
- [x] run의 description과 "1. 시작 조건을 본다" 3번에서 앞선 커밋을 묻는 까닭 글이 바뀐다. "plan은 브랜치를 바꾸지 않아서, 기본 브랜치에서 계획하면 계획의 커밋이 로컬 기본 브랜치에만 들어간다"와 description의 "계획의 커밋이 로컬 기본 브랜치에만 앞서 있고"가, 이번 고침 전의 plan으로 세운 계획이나 사람이 기본 브랜치에 넣은 커밋이면 로컬 기본 브랜치가 앞설 수 있다는 뜻으로 바뀐다. 물음, 되돌림, 명령 줄은 그대로다 (`plugins/plate/skills/run/SKILL.md`)
- [x] `PlanRulesTest`에 `test_commits_on_tasks_branch`가 더해진다. 절대 규칙, 1번, 7번, 적는 규칙의 이름 줄에 새 규칙의 글이 있는지와, 본문에 "브랜치를 만들거나 바꾸지 않는다"가 없는지를 본다. `RunRulesTest`에 `test_ahead_commits_reason`이 더해진다. 1번에 새 까닭 글이 있는지, "plan은 브랜치를 바꾸지 않아서"가 없는지, 되돌림 명령 `git branch -f {기본 브랜치} refs/remotes/origin/{기본 브랜치}`가 남았는지를 본다. ARCHITECTURE 디렉터리 구조의 `test_skill_rules.py` 줄의 괄호 목록에 두 테스트가 지키는 것이 더해진다 (`tests/test_skill_rules.py`, `docs/ARCHITECTURE.md`)
- [x] `docs/ARCHITECTURE.md`가 바뀐다. 데이터 흐름의 `→ 계획(` 줄에 세 갈래(기본 브랜치이면 `tasks/<이름>`을 만들거나 바꾼다, `tasks/<이름>`이면 그대로, 그 밖이면 묻고 거절하면 쓰지 않는다)가 더해진다. 실행의 "tasks/<이름> 브랜치를 만들거나 바꾼 뒤, 계획의 커밋이 로컬 기본 브랜치에만 있고" 줄이 앞선 커밋 일반으로 바뀐다. 패턴과 규칙의 "run은 기본 브랜치(" 줄에 plan이 tasks 브랜치에 커밋한다는 것과 그 이유가 더해진다. 이 줄들은 고친 동작과 맞게 한다 (`docs/ARCHITECTURE.md`)
- [x] `README.md` 스킬 표의 `plan` 줄에 세 갈래가 더해지고, `run` 줄의 "계획의 커밋이 로컬 기본 브랜치에만 있고"가 앞선 커밋 일반으로 바뀐다 (`README.md`)

**통과 조건**
- 완료 조건 1이 참이다.
  - 확인: `grep -n -e 'tasks/<이름>' plugins/plate/skills/plan/SKILL.md`가 description, 낱말, 절대 규칙 4, 1번, 7번, 적는 규칙의 이름 줄을 낸다
  - 확인: `grep -c -e '브랜치를 만들거나 바꾸지 않는다' plugins/plate/skills/plan/SKILL.md`가 `0`이다
  - 확인: `(cd tests && python3 -m unittest test_skill_rules.PlanRulesTest.test_commits_on_tasks_branch)`가 OK다
- 완료 조건 2가 참이다.
  - 확인: `grep -c -e 'plan은 브랜치를 바꾸지 않아서' -e '계획의 커밋이 로컬 기본 브랜치에만' plugins/plate/skills/run/SKILL.md`가 `0`이다
  - 확인: `(cd tests && python3 -m unittest test_skill_rules.RunRulesTest.test_ahead_commits_reason)`가 OK다
  - 확인: `git diff 97a5a3f -- plugins/plate/skills/run/SKILL.md`에서 `## 1. 시작 조건을 본다` 절 안의 바뀐 줄이 까닭 글을 담은 줄뿐이고, `git branch -f`와 `git log --oneline` 명령 줄은 바뀌지 않았다
- 완료 조건 3이 참이다.
  - 확인: `grep -c -e '계획의 커밋이 로컬 기본 브랜치에만' docs/ARCHITECTURE.md README.md`가 두 파일 모두 `0`이다
  - 확인: ARCHITECTURE 데이터 흐름의 `→ 계획(` 줄과 README의 `` | `plan` | `` 줄을 읽어, 저마다 세 갈래를 모두 적는지 본다
- 테스트가 모두 통과한다(완료 조건 5).
  - 확인: `python3 -m unittest discover -s tests`가 OK다

## 한 일
- plan 본문이 바뀐다: description에 git 레포이면 커밋이 `tasks/<이름>` 브랜치에 들어간다(기본 브랜치이면 묻지 않고 만들거나 바꾸고, 그 밖이면 묻는다)를 더했다(460자). 첫 문단에 커밋 브랜치를 더했다. 절대 규칙 4를 "계획 파일만 `tasks/<이름>` 브랜치에 커밋한다"와 세 갈래·푸시하지 않음으로 바꿨다. 낱말에 run과 같은 줄의 "기본 브랜치"를 더하고, "tasks 머리"의 이름 쓰임에 plan이 커밋하는 브랜치를 더했다. 1번 끝에 `git branch --show-current`로 지금 브랜치를 얻어, 기본 브랜치도 `tasks/<이름>`도 아니면 보여 주고 커밋할지 묻고(이름은 6번 초안에서 정한다, 더하는 경우는 그 tasks의 이름) 거절하면 아무것도 쓰지 않고 끝나는 갈래를 더했다. 7번 머리에 쓰기 전 브랜치를 맞추는 글(`git rev-parse --verify --quiet refs/heads/tasks/<이름>`로 있는지 보고, 없으면 `git switch -c tasks/<이름>`, 있으면 `git switch tasks/<이름>`, 실패하면 쓰지 않고 실패한 명령과 오류를 보고하고 끝남, 명령 치환 없이 한 명령씩)을 더했다. 적는 규칙 이름 줄에 로컬에 없는 이름을 고르는 글과 더하는 경우 바꾸는 글을, 8번에 커밋한 브랜치를 더했다 (`plugins/plate/skills/plan/SKILL.md`)
- run의 description과 1번 3의 까닭 글이 바뀐다: description의 "계획의 커밋이 로컬 기본 브랜치에만 앞서 있고 모두"를 "로컬 기본 브랜치가 origin보다 앞서 있고 그 커밋이 모두"로(994자), 1번 3의 "plan은 브랜치를 바꾸지 않아서, …들어간다."를 "plan은 계획을 `tasks/<이름>`에 커밋하지만, 그렇게 고치기 전의 plan으로 세운 계획이나 사람이 기본 브랜치에 넣은 커밋이 있으면 로컬 기본 브랜치가 원격보다 앞설 수 있다."로 바꿨다. 물음, 되돌림, 명령 줄은 그대로다 (`plugins/plate/skills/run/SKILL.md`)
- 테스트가 더해진다: `PlanRulesTest.test_commits_on_tasks_branch`(절대 규칙 4, 1번의 물음과 거절 갈래, 7번의 `git switch -c`·`git switch`와 실패 갈래가 쓰기 앞에 있음과 `$(` 없음, 이름 줄, 8번, 본문에 "브랜치를 만들거나 바꾸지 않는다" 없음, 기본 브랜치 정의 줄이 run과 같음)와 `RunRulesTest.test_ahead_commits_reason`(새 까닭 글, 옛 두 글이 없음, `git branch -f` 되돌림 명령이 남음)을 더했다. ARCHITECTURE 디렉터리 구조의 `test_skill_rules.py` 괄호 목록에 둘을 더했다 (`tests/test_skill_rules.py`, `docs/ARCHITECTURE.md`)
- `docs/ARCHITECTURE.md`가 바뀐다: 데이터 흐름의 `→ 계획(` 줄을 "한 커밋으로 tasks/<이름> 브랜치에 넣는다"로 바꾸고 그 아래에 세 갈래(기본 브랜치이면 만들거나 바꾼다, tasks/<이름>이면 그대로, 그 밖이면 묻고 거절하면 쓰지 않는다)의 줄을 더했다. 실행의 앞선 커밋 줄을 "로컬 기본 브랜치에 origin보다 앞선 커밋(고치기 전의 plan으로 세운 계획, 사람이 넣은 커밋)이 있고"로 바꿨다. 패턴과 규칙의 "run은 기본 브랜치(" 줄 앞에 plan의 브랜치 규칙과 이유의 줄을 더했다 (`docs/ARCHITECTURE.md`)
- `README.md`: `plan` 줄에 `tasks/<이름>` 브랜치 커밋과 세 갈래를, `run` 줄의 앞선 커밋 글을 앞선 커밋 일반으로 바꿨다 (`README.md`)

## 확인 결과
- 완료 조건 1이 참이다.
  - `grep -n -e 'tasks/<이름>' plugins/plate/skills/plan/SKILL.md` → 3(description), 10(첫 문단), 19(절대 규칙 4), 26(낱말 tasks 머리), 54(1번), 137(7번), 167(양식 이름 줄), 235(적는 규칙 이름 줄). 통과
  - `grep -c -e '브랜치를 만들거나 바꾸지 않는다' plugins/plate/skills/plan/SKILL.md` → `0`. 통과
  - `(cd tests && python3 -m unittest test_skill_rules.PlanRulesTest.test_commits_on_tasks_branch)` → `Ran 1 test … OK`. 통과
- 완료 조건 2가 참이다.
  - `grep -c -e 'plan은 브랜치를 바꾸지 않아서' -e '계획의 커밋이 로컬 기본 브랜치에만' plugins/plate/skills/run/SKILL.md` → `0`. 통과
  - `(cd tests && python3 -m unittest test_skill_rules.RunRulesTest.test_ahead_commits_reason)` → `Ran 1 test … OK`. 통과
  - `git diff 97a5a3f -- plugins/plate/skills/run/SKILL.md` → `## 1. 시작 조건을 본다` 절 안의 바뀐 줄은 까닭 글을 담은 "브랜치를 만들거나 바꾼 뒤에는 로컬 기본 브랜치에 원격보다 앞선 커밋이 있는지 본다." 줄 하나뿐이고, `git branch -f`와 `git log --oneline` 명령 줄은 바뀌지 않았다(그 밖의 바뀐 줄은 description과 001-issue-criteria가 고친 낱말·tasks 끝의 줄). 통과
- 완료 조건 3이 참이다.
  - `grep -c -e '계획의 커밋이 로컬 기본 브랜치에만' docs/ARCHITECTURE.md README.md` → `README.md:0`, `docs/ARCHITECTURE.md:0`. 통과
  - ARCHITECTURE 데이터 흐름의 `→ 계획(` 줄과 그 아래 줄, README의 `` | `plan` | `` 줄을 읽음 → 둘 다 기본 브랜치이면 `tasks/<이름>`을 만들거나 바꾼다, `tasks/<이름>`이면 그대로, 그 밖이면 묻는다(거절하면 쓰지 않는다)의 세 갈래를 적는다. 통과
- 테스트가 모두 통과한다(완료 조건 5).
  - `python3 -m unittest discover -s tests` → `Ran 207 tests in 17.951s` / `OK`. 통과

## 계획과 달라진 점
- ARCHITECTURE의 `→ 계획(` 줄은 세 갈래를 한 줄에 넣지 않고 바로 아래 `→` 줄로 더했다. 데이터 흐름의 다른 단계가 갈래를 아래 `→` 줄로 적는 꼴을 따랐다. 통과 조건의 확인은 그 줄과 아래 줄을 함께 읽었다
- TODO에 없던 plan 첫 문단(커밋이 `tasks/<이름>` 브랜치에 들어간다)과 낱말 "tasks 머리"의 이름 쓰임도 맞췄다. 바뀐 동작과 어긋난 채 남지 않게 했다

## 남은 것
- run 1번 3의 "계획의 커밋도 tasks의 커밋으로 세어진다"(되돌림 승인 갈래, `git branch -f` 명령 줄)는 명령 줄을 바꾸지 않는다는 통과 조건 때문에 그대로 두었다. 뜻은 앞선 커밋 일반에도 맞다
- plan 본문의 새 브랜치 동작은 이 phase에서 돌려 보지 않았다(완료 조건 4의 헤드리스 시험은 다음 phase의 일이다)

## 하네스에서 걸린 것
없음

## 확인 1

**통과 조건**
- 완료 조건 1이 참이다.
  - `grep -n -e 'tasks/<이름>' plugins/plate/skills/plan/SKILL.md` → 3(description), 10(첫 문단), 19(절대 규칙 4), 26(낱말 tasks 머리), 54(1번), 137(7번), 167(양식 이름 줄), 235(적는 규칙 이름 줄). 요구한 여섯 곳이 모두 나온다. 통과
  - `grep -c -e '브랜치를 만들거나 바꾸지 않는다' plugins/plate/skills/plan/SKILL.md` → `0`. 통과
  - `(cd tests && python3 -m unittest test_skill_rules.PlanRulesTest.test_commits_on_tasks_branch)` → `Ran 1 test` / `OK`. 통과
- 완료 조건 2가 참이다.
  - `grep -c -e 'plan은 브랜치를 바꾸지 않아서' -e '계획의 커밋이 로컬 기본 브랜치에만' plugins/plate/skills/run/SKILL.md` → `0`. 통과
  - `(cd tests && python3 -m unittest test_skill_rules.RunRulesTest.test_ahead_commits_reason)` → `Ran 1 test` / `OK`. 통과
  - `git diff 97a5a3f -- plugins/plate/skills/run/SKILL.md` → `## 1. 시작 조건을 본다`(75~96줄) 안의 바뀐 hunk는 `@@ -88,7 +88,7 @@` 하나이고, 바뀐 줄은 까닭 글을 담은 "브랜치를 만들거나 바꾼 뒤에는 로컬 기본 브랜치에 원격보다 앞선 커밋이 있는지 본다. …" 줄 하나뿐이다. `git branch -f`와 `git log --oneline` 명령 줄은 diff에 없다. 그 밖의 hunk는 description, 낱말(하네스 고칠 거리), tasks 끝 절의 것이다. 통과
- 완료 조건 3이 참이다.
  - `grep -c -e '계획의 커밋이 로컬 기본 브랜치에만' docs/ARCHITECTURE.md README.md` → `README.md:0`, `docs/ARCHITECTURE.md:0`. 통과
  - `docs/ARCHITECTURE.md` 63~64줄(`→ 계획(` 줄과 바로 아래 `→` 줄), `README.md` 9줄(`` | `plan` | ``)을 읽음 → 둘 다 기본 브랜치이면 `tasks/<이름>`을 만들거나 바꾼다, `tasks/<이름>`이면 그대로 둔다, 그 밖이면 묻는다(거절하면 쓰지 않는다)의 세 갈래를 적는다. 통과
- 테스트가 모두 통과한다(완료 조건 5).
  - `python3 -m unittest discover -s tests` → `Ran 207 tests in 17.916s` / `OK`. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 207 tests` / `OK`. 통과

**남은 것**
- plan 본문의 새 브랜치 동작은 이 phase에서 돌려 보지 않았다(완료 조건 4의 헤드리스 시험은 다음 phase의 일이다) → 이 phase의 통과 조건(완료 조건 1, 2, 3, 5)은 본문의 글과 테스트를 보고 plan의 실행 동작을 보지 않아 걸리지 않는다. 하네스에서 걸린 것

**실패**
없음

**하네스에서 걸린 것**
- 남은 것: plan 본문의 새 브랜치 동작은 이 phase에서 돌려 보지 않았다. 완료 조건 4의 헤드리스 시험이 다음 phase에서 본다

**판정**: 통과
