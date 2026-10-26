# Phase 2: review가 결과물인 마크다운을 평가한다

**목표**: review의 바뀐 코드 파일이 `## 결과물인 마크다운` 절의 `.md`를 두 모드에서 넣고 게이트의 커버리지·중복에서는 그 줄을 빼며, 이 저장소의 `docs/ARCHITECTURE.md`에 그 절이 생기고, 맥락 문서의 review 줄이 그와 맞는다.

**테스트 먼저**: 아니오 — `.md`만 고친다

**읽을 것**
- `plugins/plate/skills/review/SKILL.md` (32~33줄 낱말 "바뀐 코드 파일"과 "새 줄", 49줄 git 레포가 아닐 때, 67~68줄 커버리지·중복, 126~127줄 게이트, 152~200줄 PR 모드와 `coverage` 행, 209~213줄 평가 절의 대상)
- `gh issue view 22 -R werwer748/harness-plate` (#22의 본문)
- `docs/ARCHITECTURE.md` (9~37줄 디렉터리 구조, 30줄 review 줄, 51줄 PR의 CI 문단, 65줄 tasks 끝, 73줄 review 잡)
- `docs/PRD.md` (18줄 핵심 기능 8)

**TODO**
- [x] 낱말 "바뀐 코드 파일"이 `docs/ARCHITECTURE.md`의 `## 결과물인 마크다운` 절에 적힌 경로의 `.md`를 넣도록 바뀌고, 절이 없으면 지금처럼 `.md`를 뺀다. 0번의 git 레포가 아닐 때의 줄도 같이 바뀐다 (`plugins/plate/skills/review/SKILL.md`)
- [x] PR 모드 절에 그 절을 기준 브랜치의 `docs/ARCHITECTURE.md`(`git show <기준 브랜치>:docs/ARCHITECTURE.md`)에서 읽는다는 줄이 더해진다 (`plugins/plate/skills/review/SKILL.md`)
- [x] 결과물인 `.md`의 줄은 커버리지와 중복의 새 줄 수에서 빠지고 판단과 등급의 근거에는 든다는 것이 낱말 "새 줄", 2번, 6번, PR 모드 `coverage` 행에 맞게 더해진다 (`plugins/plate/skills/review/SKILL.md`)
- [x] 평가 절 양식의 대상에 결과물인 `.md`로 넣은 파일을 구별해 적는 자리가 더해진다 (`plugins/plate/skills/review/SKILL.md`)
- [x] `## 결과물인 마크다운` 절이 생기고 `plugins/plate/skills/*/SKILL.md`를 적는다 (`docs/ARCHITECTURE.md`)
- [x] `docs/ARCHITECTURE.md` 30줄, 51줄, 65줄, 73줄과 `docs/PRD.md` 18줄 가운데 바뀐 review와 어긋나는 줄이 바뀐다. 어긋나는 줄이 없으면 고치지 않고 기록에 그렇다고 적는다 (`docs/ARCHITECTURE.md`, `docs/PRD.md`)

**통과 조건**
- 완료 조건 2가 참이다.
  - 확인: `plugins/plate/skills/review/SKILL.md`의 낱말 절, 0번의 git 레포가 아닐 때의 줄, PR 모드 절, 평가 절 양식의 대상을 하나씩 읽어 네 곳이 저마다 위의 것과 맞는다
  - 확인: `grep -rn '바뀐 코드 파일' plugins/plate docs README.md`가 낸 줄 가운데 review 밖의 것을 하나씩 읽어, 바뀐 낱말과 어긋나는 줄이 없다
- 완료 조건 3이 참이다.
  - 확인: review의 낱말 "새 줄"과 2번의 커버리지·중복 줄, 6번의 두 게이트 줄, PR 모드 `coverage` 행을 하나씩 읽어 결과물인 `.md`의 줄을 커버리지와 중복에서 빼는 것이 네 곳에서 어긋나지 않는다
- 완료 조건 4가 참이다.
  - 확인: `grep -n -A3 '^## 결과물인 마크다운' docs/ARCHITECTURE.md`가 그 절과 `plugins/plate/skills/*/SKILL.md` 경로를 낸다
- 완료 조건 5 가운데 review의 몫이 참이다.
  - 확인: `docs/ARCHITECTURE.md` 30줄, 51줄, 65줄, 73줄과 `docs/PRD.md` 18줄을 하나씩 읽어 바뀐 review와 어긋나는 줄이 없다
- phase 1이 이룬 완료 조건 1과 그 문서 줄이 그대로 참이다. phase 1이 고친 `docs/ARCHITECTURE.md`를 이 phase도 고친다.
  - 확인: `plugins/plate/skills/run/SKILL.md`의 4번, 5번, 7번, "코드 평가를 맡긴다", "하네스 eval을 맡긴다"를 하나씩 읽어 다섯 곳 모두에 그 줄을 붙이는 조건과 예외가 있다. 한 곳이라도 없으면 실패
  - 확인: `docs/ARCHITECTURE.md` 26줄과 59~66줄, `docs/TOOLS.md` 83줄을 하나씩 읽어 바뀐 run과 어긋나는 줄이 없다
- 테스트가 모두 통과한다.
  - 확인: `python3 -m unittest discover -s tests`가 `OK`

## 한 일
- 낱말 "바뀐 코드 파일"과 0번의 git 레포가 아닐 때의 줄: 낱말 "결과물인 마크다운 절"(`docs/ARCHITECTURE.md`의 `## 결과물인 마크다운`, 목록 줄마다 경로, 글롭 허용)과 "결과물인 마크다운"을 더하고, 바뀐 코드 파일이 "`.md`가 아니거나 결과물인 마크다운"인 것을 넣으며 절이 없으면 `.md`를 모두 뺀다고 적었다. git 레포가 아닐 때의 뜻도 같게 바꾸고 절을 작업 트리에서 읽는다고 적었다 (`plugins/plate/skills/review/SKILL.md`)
- PR 모드에서 그 절을 기준 브랜치에서 읽는다: "지침 파일과 PR의 글"에 `git show <기준 브랜치>:docs/ARCHITECTURE.md`로 읽고, 기준 브랜치에 파일이나 절이 없으면 `.md`를 모두 뺀다는 줄을 더했다 (`plugins/plate/skills/review/SKILL.md`)
- 커버리지·중복에서 빼고 판단·등급에는 넣기: 낱말 "새 줄"에 결과물인 마크다운의 줄도 판단과 등급(부채 비율 포함)의 근거에 든다고 적고, 새 낱말 "잴 새 줄"(새 줄에서 결과물인 마크다운의 줄을 뺀 것)을 두어 2번의 커버리지·중복, 6번의 두 게이트 줄(20줄 기준 포함), PR 모드 `coverage` 행이 이것으로 센다고 바꿨다. 기록 양식의 커버리지·중복 줄도 "잴 새 줄"로 바꿨다 (`plugins/plate/skills/review/SKILL.md`)
- 평가 절 양식의 대상: "결과물인 마크다운 절: `{경로}` | 없음" 줄, 바뀐 코드 파일 줄에 "잴 새 줄 {수}줄", 파일 줄 `(결과물인 마크다운)` 꼴을 더하고, 적는 규칙에 구별해 적는 규칙을 더했다 (`plugins/plate/skills/review/SKILL.md`)
- `## 결과물인 마크다운` 절: `## 명령` 앞에 절을 만들고 `plugins/plate/skills/*/SKILL.md`를 적었다 (`docs/ARCHITECTURE.md`)
- 맥락 문서의 review 줄: 51줄(PR의 CI 문단)의 "PR 모드는 지침 파일을 기준 브랜치에서 읽고"에 결과물인 마크다운 절을 더하고, 자동 머지의 커버리지 "보지 않음" 괄호를 "결과물인 마크다운의 줄을 뺀 새 줄이 20줄 미만이면"으로 바꿨다. 73줄(review 잡)에도 결과물인 마크다운 절을 기준 브랜치에서 읽는다고 더했다. 30줄, 65줄, `docs/PRD.md` 18줄은 "바뀐 코드를 평가한다"는 수준이라 어긋나지 않아 고치지 않았다 (`docs/ARCHITECTURE.md`)

## 확인 결과
- 완료 조건 2가 참이다.
  - `plugins/plate/skills/review/SKILL.md`의 낱말 절(32~36줄), 0번의 git 레포가 아닐 때의 줄(53줄), PR 모드 "지침 파일과 PR의 글"의 결과물인 마크다운 절 줄, 기록 양식 "대상"과 적는 규칙을 읽음 → 낱말은 절의 `.md`를 넣고 절이 없으면 `.md`를 빼고, git 레포가 아닐 때도 같은 뜻이고, PR 모드는 `git show <기준 브랜치>:docs/ARCHITECTURE.md`에서 읽고, 대상에 절과 `(결과물인 마크다운)` 구별이 있다. 통과
  - `grep -rn '바뀐 코드 파일' plugins/plate docs README.md | grep -v skills/review/` → `docs/tasks/plan.md` 30·32·43줄, `docs/tasks/002-run-review/phase-2.md` 3·24줄, `docs/tasks/002-run-review/plan.md` 4·14·16줄뿐. 모두 바뀐 낱말을 적는 계획의 줄이라 어긋나지 않는다. 통과
- 완료 조건 3이 참이다.
  - 낱말 "새 줄"(판단·등급에 든다)과 "잴 새 줄", 2번의 커버리지·중복 줄(잴 새 줄), 6번의 두 게이트 줄(잴 새 줄, 20줄 기준도), PR 모드 `coverage` 행(잴 새 줄)을 읽음 → 네 곳 모두 결과물인 마크다운의 줄을 커버리지와 중복에서 빼고 어긋나지 않는다. 통과
- 완료 조건 4가 참이다.
  - `grep -n -A3 '^## 결과물인 마크다운' docs/ARCHITECTURE.md` → `81:## 결과물인 마크다운`, `83-- \`plugins/plate/skills/*/SKILL.md\``. 통과
- 완료 조건 5 가운데 review의 몫이 참이다.
  - `docs/ARCHITECTURE.md` 30줄, 51줄, 65줄, 73줄과 `docs/PRD.md` 18줄을 읽음 → 51·73줄은 이번에 고쳐 맞고, 30·65줄과 PRD 18줄은 바뀐 review와 어긋나지 않는다. 통과
- phase 1이 이룬 완료 조건 1과 그 문서 줄이 그대로 참이다.
  - `grep -n '작업 트리\|다른 글을 더하지' plugins/plate/skills/run/SKILL.md` → 47줄(작업 트리의 스킬 줄 낱말), 109줄(4. 수행), 125줄(5. 확인), 147줄(7. 회고), 265줄(코드 평가를 맡긴다), 275줄(하네스 eval을 맡긴다) 다섯 곳 모두에 붙이는 조건과 "다른 글을 더하지 않는다는 규칙의 예외"가 있다. 통과
  - `docs/ARCHITECTURE.md` 26줄과 59~66줄, `docs/TOOLS.md` 83줄을 읽음 → 이 phase는 그 줄을 바꾸지 않았고 바뀐 run과 어긋나지 않는다. 통과
- 테스트가 모두 통과한다.
  - `python3 -m unittest discover -s tests` → `Ran 99 tests in 15.262s` / `OK`. 통과

## 계획과 달라진 점
- TODO에 없던 낱말 "결과물인 마크다운 절", "결과물인 마크다운", "잴 새 줄"을 review의 낱말 절에 더했다. 네 곳(낱말, 2번, 6번, PR 모드 `coverage`)이 같은 빼기를 한 낱말로 가리켜 어긋나지 않게 하려는 것이다. 그래서 review 낱말 절의 줄 번호가 뒤로 밀렸다(git 레포가 아닐 때의 줄은 49줄→53줄).
- 기록 양식의 "잰 것" 커버리지·중복 줄도 "잴 새 줄"로 바꿨다. TODO는 대상만 적었지만 같은 수를 가리켜야 해서다.

## 남은 것
- 결과물인 마크다운 절의 꼴(목록 줄마다 경로 하나, 글롭 허용)은 review 본문과 이 저장소의 절에만 정했고, setup의 양식에는 없다(범위 밖).
- 부채 비율의 분모(새 줄 × 30분)에 마크다운 줄이 들어 스킬 본문을 많이 바꾼 tasks는 부채 비율이 낮게 나올 수 있다. 결정("커버리지와 중복의 새 줄 수에서만 뺀다")을 따른 것이다.

## 하네스에서 걸린 것
- 없음
