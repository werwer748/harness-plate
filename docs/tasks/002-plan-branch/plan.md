# plan이 계획을 tasks 브랜치에 커밋한다

## 목표
plan이 계획 파일을 쓰기 전에 `tasks/<이름>` 브랜치를 만들거나 바꿔 그 브랜치에 커밋한다. 기본 브랜치에서는 묻지 않고, 기본 브랜치도 `tasks/<이름>`도 아닌 브랜치에서는 묻는다. 새 tasks의 이름은 이미 있는 브랜치와 겹치지 않게 고른다. run 1번의 까닭 글과 맥락 문서, README가 그것과 맞고, 작업 트리의 plan을 헤드리스로 돌려 두 장면을 본다.

## 범위 밖
- run 1번의 "로컬 기본 브랜치를 되돌릴지 묻는다" 규칙을 지우거나 그 동작을 바꾸는 것. 까닭 글만 고친다
- plan이 푸시하는 것
- phase, check, retro, review, eval, cleanup의 "브랜치를 만들거나 바꾸지 않는다" 규칙
- `tasks/<이름>`에서 그대로 커밋하는 갈래, 더하는 경우 있는 브랜치로 바꾸는 갈래, 이름이 겹치는 갈래를 시험 저장소에서 돌리는 것

## 완료 조건
1. plan 본문(description, 낱말, 절대 규칙 4, 1번, 7번, 적는 규칙의 이름 줄)이 브랜치 규칙을 같은 뜻으로 적는다. git 레포이면 다음과 같다. 지금 브랜치가 기본 브랜치이면 묻지 않고, 쓰기 전에 `tasks/<이름>`을 만들거나(없으면 지금 HEAD에서) 바꾼다. `tasks/<이름>`이면 그대로 둔다. 그 밖이면 1번에서 지금 브랜치를 보여 주고 `tasks/<이름>`에 커밋할지 묻고, 거절하면 아무것도 쓰지 않고 끝난다. 새 tasks의 이름은 로컬에 같은 이름의 `tasks/<이름>` 브랜치가 없는 것으로 고르고, 더하는 경우에는 그 브랜치가 있으면 바꾼다. 브랜치를 만들거나 바꾸지 못하면 쓰지 않고 실패한 명령과 오류를 보고한다. "브랜치를 만들거나 바꾸지 않는다"는 plan 본문에 없다.
   - 확인: `grep -n -e 'tasks/<이름>' plugins/plate/skills/plan/SKILL.md`가 description, 낱말, 절대 규칙 4, 1번, 7번, 적는 규칙의 이름 줄을 낸다
   - 확인: `grep -c -e '브랜치를 만들거나 바꾸지 않는다' plugins/plate/skills/plan/SKILL.md`가 `0`이다
   - 확인: `(cd tests && python3 -m unittest test_skill_rules.PlanRulesTest.test_commits_on_tasks_branch)`가 OK다
   - 돌리지 않음: `tasks/<이름>`에서 그대로 커밋하는 갈래, 더하는 경우 있는 브랜치로 바꾸는 갈래, 이름이 겹치는 갈래는 헤드리스로 돌리지 않는다. 여러 턴의 헤드리스 세션이 갈래마다 들어 두 장면만 돌리기로 정했다
2. run의 description과 1번에서 앞선 커밋을 묻는 글이 바뀐다. "plan은 브랜치를 바꾸지 않아서"와 "계획의 커밋이 로컬 기본 브랜치에만" 대신, 이번 고침 전의 plan으로 세운 계획이나 사람이 기본 브랜치에 넣은 커밋이면 로컬 기본 브랜치가 앞설 수 있다는 뜻으로 적는다. 물음과 되돌림의 동작은 그대로다.
   - 확인: `grep -c -e 'plan은 브랜치를 바꾸지 않아서' -e '계획의 커밋이 로컬 기본 브랜치에만' plugins/plate/skills/run/SKILL.md`가 `0`이다
   - 확인: `(cd tests && python3 -m unittest test_skill_rules.RunRulesTest.test_ahead_commits_reason)`가 OK다
   - 확인: `git diff 97a5a3f -- plugins/plate/skills/run/SKILL.md`에서 `## 1. 시작 조건을 본다` 절 안의 바뀐 줄이 까닭 글을 담은 줄뿐이고, `git branch -f`와 `git log --oneline` 명령 줄은 바뀌지 않았다
3. `docs/ARCHITECTURE.md`와 `README.md`가 plan의 브랜치 동작과 맞는다. ARCHITECTURE 데이터 흐름의 계획 줄과 README 스킬 표의 plan 줄은 저마다 세 갈래(기본 브랜치이면 `tasks/<이름>`을 만들거나 바꾼다, `tasks/<이름>`이면 그대로, 그 밖이면 묻는다)를 적는다. ARCHITECTURE 패턴과 규칙의 "run은 기본 브랜치(" 줄, 데이터 흐름 실행의 앞선 커밋 줄, README의 run 줄은 앞선 커밋을 "계획의 커밋이 로컬 기본 브랜치에만"으로 적지 않는다.
   - 확인: `grep -c -e '계획의 커밋이 로컬 기본 브랜치에만' docs/ARCHITECTURE.md README.md`가 두 파일 모두 `0`이다
   - 확인: ARCHITECTURE 데이터 흐름의 `→ 계획(` 줄과 README의 `` | `plan` | `` 줄을 읽어, 저마다 세 갈래를 모두 적는지 본다
4. 작업 트리의 plan을 헤드리스로 시험 저장소에서 돌리면 두 장면이 이렇다. (가) 기본 브랜치 `main`에서 새 tasks를 계획하면 계획 커밋이 `tasks/<이름>`에 들어가고, 로컬 `main`은 돌리기 전 커밋 그대로다. (나) `feature/x`에서 부르면 `feature/x`와 `tasks/<이름>`을 들어 바꿀지 묻고, 그 자리에서 계획 파일도 새 커밋도 없다.
   - 확인: 시험을 돌린 phase의 기록에 돌릴 때의 `git hash-object plugins/plate/skills/plan/SKILL.md`가 있고, 작업 트리에서 다시 낸 값과 같다
   - 확인: 기록에 (가)의 `git branch --show-current`, `git log -1 --format=%s tasks/<이름>`, 돌리기 전과 뒤의 `git rev-parse main`이 있다. 브랜치가 `tasks/<이름>`이고, 제목이 `plan: <이름>`이고, 두 `main` 해시가 같다
   - 확인: 기록에 (나)의 마지막 응답 글 전문과 그 자리의 `git branch --show-current`, `git log --oneline -1`, `git status --porcelain`이 있다. 응답이 `feature/x`와 `tasks/<이름>`을 들어 바꿀지 묻고, 브랜치가 `feature/x`이고, 마지막 커밋이 돌리기 전 그대로이고, `git status --porcelain`이 아무것도 내지 않는다
5. 테스트가 모두 통과한다(tasks 완료 조건 6).
   - 확인: `python3 -m unittest discover -s tests`가 OK다

## 결정
- plan이 브랜치를 만들거나 바꾸기로 하고, plan 절대 규칙 4, `docs/ARCHITECTURE.md`, run 1번의 어긋난 글을 이 task에서 고친다. 이유: 요청이 바로 이 규칙을 바꾸는 것이고, 문서를 두면 바뀐 동작과 어긋난다
- 기본 브랜치도 `tasks/<이름>`도 아닌 브랜치에서는 지금 브랜치를 보여 주고 `tasks/<이름>`에 커밋할지 묻고, 거절하면 쓰지 않고 끝난다. 이유: run 1번이 같은 장면에서 그렇게 묻고, PR과 합침은 늘 `tasks/<이름>`을 다뤄 다른 브랜치의 계획 커밋은 PR에 들지 않는다
- 그 물음은 1번에서 낸다. 이름은 6번의 초안에서 정하므로 물음에는 `tasks/<이름>`의 이름을 초안에서 정한다고 적는다(더하는 경우는 그 tasks의 이름). 이유: 초안을 다 승인받은 뒤에 거절하면 초안이 버려진다(추천안으로 정함)
- 새 tasks의 이름은 6번 초안에서 로컬에 같은 이름의 `tasks/<이름>` 브랜치가 없는 것으로 고른다. 이유: 옛 브랜치로 바꾸면 그 브랜치의 지난 커밋이 새 tasks에 섞여 PR과 코드 평가 범위에 든다
- run 1번의 앞선 커밋 물음은 남기고 까닭 글만 고친다. 이유: 이번 고침 전에 세운 계획이나 손으로 넣은 커밋에서는 그 장면이 여전히 나고, 규칙과 테스트가 이미 있다
- plan의 기본 브랜치는 run 낱말의 "기본 브랜치"와 같은 정의다(`origin`의 HEAD, 없으면 `main`, 그다음 `master`). 이유: 두 스킬이 같은 브랜치를 기본으로 봐야 run 1번이 plan의 커밋을 앞선 커밋으로 잡지 않는다(추천안으로 정함)
- 헤드리스 시험은 (가) 기본 브랜치에서 새 tasks, (나) 다른 브랜치에서 부름의 두 장면만 돌린다. 이유: (가)가 요청의 핵심 장면이고 (나)는 멈추는 자리라 첫 턴만 보면 된다. 갈래마다 돌리면 여러 턴의 헤드리스 세션이 다섯 번 든다
- 회고 1의 문제(새 tasks를 다른 tasks의 브랜치에서 계획하는 장면)를 고치는 phase 3에, 고친 plan 본문으로 헤드리스 시험을 다시 돌리고 그 장면 (다)도 돌리는 TODO를 둔다. 이유: plan 본문을 고치면 완료 조건 4의 본문 해시 확인이 거짓이 되는데, 계획에 다시 참으로 둘 길이 없었다
