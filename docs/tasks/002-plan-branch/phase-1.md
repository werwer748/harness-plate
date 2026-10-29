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
- [ ] plan 본문이 바뀐다. 절대 규칙 4의 "브랜치를 만들거나 바꾸지 않는다"가 브랜치 규칙(기본 브랜치이면 쓰기 전에 `tasks/<이름>`을 만들거나 바꾸고, `tasks/<이름>`이면 그대로, 그 밖이면 1번에서 물어 승인받은 때만 바꾸고, 푸시하지 않는다)으로 바뀐다. 낱말에 run과 같은 정의의 "기본 브랜치"가 더해진다. 1번에 git 레포에서 기본 브랜치도 `tasks/<이름>`도 아닌 브랜치이면 지금 브랜치를 보여 주고 `tasks/<이름>`(이름은 초안에서 정한다. 더하는 경우는 그 tasks의 이름)에 커밋할지 묻고, 거절하면 아무것도 쓰지 않고 끝나는 갈래가 더해진다. 7번에서 쓰기 전에 브랜치를 만들거나(`git switch -c`, 지금 HEAD에서) 바꾸고(`git switch`), 실패하면 쓰지 않고 실패한 명령과 오류를 보고하고 끝나는 글이 더해진다. 적는 규칙의 이름 줄에 로컬에 같은 이름의 `tasks/<이름>` 브랜치가 없는 이름을 고르는 글이 더해진다(더하는 경우는 그 브랜치가 있으면 바꾼다). 8번의 보고에 커밋한 브랜치가 더해진다. description에 tasks 브랜치에 커밋한다는 것이 더해지고 1024자 안이다. 본문의 명령은 명령 치환 없이 한 명령씩 적는다 (`plugins/plate/skills/plan/SKILL.md`)
- [ ] run의 description과 "1. 시작 조건을 본다" 3번에서 앞선 커밋을 묻는 까닭 글이 바뀐다. "plan은 브랜치를 바꾸지 않아서, 기본 브랜치에서 계획하면 계획의 커밋이 로컬 기본 브랜치에만 들어간다"와 description의 "계획의 커밋이 로컬 기본 브랜치에만 앞서 있고"가, 이번 고침 전의 plan으로 세운 계획이나 사람이 기본 브랜치에 넣은 커밋이면 로컬 기본 브랜치가 앞설 수 있다는 뜻으로 바뀐다. 물음, 되돌림, 명령 줄은 그대로다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] `PlanRulesTest`에 `test_commits_on_tasks_branch`가 더해진다. 절대 규칙, 1번, 7번, 적는 규칙의 이름 줄에 새 규칙의 글이 있는지와, 본문에 "브랜치를 만들거나 바꾸지 않는다"가 없는지를 본다. `RunRulesTest`에 `test_ahead_commits_reason`이 더해진다. 1번에 새 까닭 글이 있는지, "plan은 브랜치를 바꾸지 않아서"가 없는지, 되돌림 명령 `git branch -f {기본 브랜치} refs/remotes/origin/{기본 브랜치}`가 남았는지를 본다. ARCHITECTURE 디렉터리 구조의 `test_skill_rules.py` 줄의 괄호 목록에 두 테스트가 지키는 것이 더해진다 (`tests/test_skill_rules.py`, `docs/ARCHITECTURE.md`)
- [ ] `docs/ARCHITECTURE.md`가 바뀐다. 데이터 흐름의 `→ 계획(` 줄에 세 갈래(기본 브랜치이면 `tasks/<이름>`을 만들거나 바꾼다, `tasks/<이름>`이면 그대로, 그 밖이면 묻고 거절하면 쓰지 않는다)가 더해진다. 실행의 "tasks/<이름> 브랜치를 만들거나 바꾼 뒤, 계획의 커밋이 로컬 기본 브랜치에만 있고" 줄이 앞선 커밋 일반으로 바뀐다. 패턴과 규칙의 "run은 기본 브랜치(" 줄에 plan이 tasks 브랜치에 커밋한다는 것과 그 이유가 더해진다. 이 줄들은 고친 동작과 맞게 한다 (`docs/ARCHITECTURE.md`)
- [ ] `README.md` 스킬 표의 `plan` 줄에 세 갈래가 더해지고, `run` 줄의 "계획의 커밋이 로컬 기본 브랜치에만 있고"가 앞선 커밋 일반으로 바뀐다 (`README.md`)

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
