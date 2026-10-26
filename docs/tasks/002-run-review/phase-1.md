# Phase 1: run이 작업 트리의 스킬 경로를 넘긴다

**목표**: run이 맡기는 다섯 곳에서, tasks가 바꾼 스킬이면 작업 트리의 `SKILL.md` 경로를 읽어 따르라는 줄을 붙이고, 맥락 문서의 run 줄이 그와 맞는다.

**테스트 먼저**: 아니오 — `.md`만 고친다

**읽을 것**
- `plugins/plate/skills/run/SKILL.md` (16~20줄 절대 규칙, 106~156줄 4·5·7번, 262~280줄 "코드 평가를 맡긴다"와 "하네스 eval을 맡긴다")
- `gh issue view 21 -R werwer748/harness-plate` (#21의 본문)
- `docs/TOOLS.md` (83줄 세션에 실린 스킬 본문이 세션을 띄울 때의 것이라는 사실)
- `docs/ARCHITECTURE.md` (26줄 run 줄, 59~66줄 데이터 흐름의 실행과 tasks 끝)

**TODO**
- [x] 4번, 5번, 7번, "코드 평가를 맡긴다", "하네스 eval을 맡긴다"의 넘기는 글 아래에, 기본 브랜치에서 갈라진 곳부터의 tasks 커밋이 그 스킬의 작업 트리 `SKILL.md`를 바꿨을 때만 붙이는 줄(작업 트리의 그 경로를 읽어 그 절차를 따른다)과 그 조건이 더해진다 (`plugins/plate/skills/run/SKILL.md`)
- [x] 다섯 곳의 "다른 글을 더하지 않는다"가 그 줄을 예외로 두도록 바뀐다 (`plugins/plate/skills/run/SKILL.md`)
- [x] `docs/ARCHITECTURE.md` 26줄, 59~66줄과 `docs/TOOLS.md` 83줄 가운데 바뀐 run과 어긋나는 줄이 바뀐다. 어긋나는 줄이 없으면 고치지 않고 기록에 그렇다고 적는다 (`docs/ARCHITECTURE.md`, `docs/TOOLS.md`)

**통과 조건**
- 완료 조건 1이 참이다.
  - 확인: `plugins/plate/skills/run/SKILL.md`의 4번, 5번, 7번, "코드 평가를 맡긴다", "하네스 eval을 맡긴다"를 하나씩 읽어 다섯 곳 모두에 그 줄을 붙이는 조건과 예외가 있다. 한 곳이라도 없으면 실패
- 완료 조건 5 가운데 run의 몫이 참이다.
  - 확인: `docs/ARCHITECTURE.md` 26줄과 59~66줄, `docs/TOOLS.md` 83줄을 하나씩 읽어 바뀐 run과 어긋나는 줄이 없다
- 테스트가 모두 통과한다.
  - 확인: `python3 -m unittest discover -s tests`가 `OK`

## 한 일
- 4번, 5번, 7번, "코드 평가를 맡긴다", "하네스 eval을 맡긴다"의 넘기는 글 아래에 붙이는 줄과 조건: 낱말 절에 "작업 트리의 스킬 줄"을 더해 줄의 꼴(`작업 트리의 {경로}를 읽어 그 절차를 따른다.`), 조건(`git diff --name-only $(git merge-base {기본 브랜치} HEAD) HEAD`가 이름이 `plate`인 플러그인 폴더 아래 `skills/{스킬 이름}/SKILL.md`를 내면 그것이 경로, 없거나 git 레포가 아니면 붙이지 않음)과 까닭을 적고, 다섯 곳마다 "tasks 커밋이 `{phase|check|retro|review|eval}` 스킬의 `SKILL.md`를 바꿨으면 글의 끝에 작업 트리의 스킬 줄을 붙인다"를 더했다 (`plugins/plate/skills/run/SKILL.md`)
- 다섯 곳의 "다른 글을 더하지 않는다"의 예외: 다섯 곳마다 "이 줄은 다른 글을 더하지 않는다는 규칙의 예외다."를 더했다 (`plugins/plate/skills/run/SKILL.md`)
- `docs/ARCHITECTURE.md` 26줄, 59~66줄과 `docs/TOOLS.md` 83줄: 하나씩 읽었고 바뀐 run과 어긋나는 줄이 없어 고치지 않았다. 26줄은 run이 조율만 하고 다섯 스킬에 맡긴다는 것, 59~66줄은 새 에이전트가 수행·확인·회고·평가한다는 것, TOOLS.md 83줄은 세션에 실린 스킬 본문이 세션을 띄울 때의 것이라는 확인한 사실이라 바뀐 run과 부딪히지 않는다

## 확인 결과
- 완료 조건 1이 참이다.
  - `plugins/plate/skills/run/SKILL.md`의 4번(109줄), 5번(125줄), 7번(147줄), "코드 평가를 맡긴다"(265줄), "하네스 eval을 맡긴다"(275줄)를 하나씩 읽음 → 다섯 곳 모두 "tasks 커밋이 그 스킬의 `SKILL.md`를 바꿨으면 글의 끝에 작업 트리의 스킬 줄을 붙인다"는 조건과 "이 줄은 다른 글을 더하지 않는다는 규칙의 예외다"가 있고, 줄의 꼴과 기본 브랜치에서 갈라진 곳부터라는 조건은 낱말 "작업 트리의 스킬 줄"(47줄)에 있다. `git diff --name-only $(git merge-base main HEAD) HEAD | grep SKILL.md` → `plugins/plate/skills/plan/SKILL.md`로 조건 명령이 돈다. 통과
- 완료 조건 5 가운데 run의 몫이 참이다.
  - `docs/ARCHITECTURE.md` 26줄, 59~66줄, `docs/TOOLS.md` 83줄을 하나씩 읽음 → 어긋나는 줄이 없다. 통과
- 테스트가 모두 통과한다.
  - `python3 -m unittest discover -s tests` → `Ran 99 tests in 15.175s` `OK`. 통과

## 계획과 달라진 점
- 계획은 다섯 곳의 넘기는 글 아래에 줄과 조건을 더한다고 했다. 줄의 꼴과 조건을 고르는 명령은 낱말 절의 "작업 트리의 스킬 줄" 한 곳에 두고, 다섯 곳에는 어느 스킬의 `SKILL.md`가 바뀌었을 때 붙이는지와 예외를 적었다. 같은 정의를 다섯 번 되풀이하지 않으려는 것이다

## 남은 것
- `docs/TOOLS.md` 84줄("스킬의 절차를 바꾸는 tasks는 ... 새 세션에서 이어 간다")은 이 phase의 읽을 범위(83줄) 밖이라 고치지 않았다. run이 이제 작업 트리 경로를 넘기므로 이 줄이 낡았는지는 회고가 볼 일이다
- 작업 트리의 스킬 줄은 에이전트가 그 파일을 읽어 따르게 할 뿐, 스킬 도구가 싣는 고치기 전 본문도 함께 들어간다. 두 본문이 다르면 에이전트가 작업 트리 쪽을 따른다는 것은 줄의 글에 기댄다

## 하네스에서 걸린 것
- 없음

## 확인 1

**통과 조건**
- 완료 조건 1이 참이다.
  - `plugins/plate/skills/run/SKILL.md`의 4번(109줄), 5번(125줄), 7번(147줄), "코드 평가를 맡긴다"(265줄), "하네스 eval을 맡긴다"(275줄)를 하나씩 읽음 → 다섯 곳 모두 "tasks 커밋이 `{phase|check|retro|review|eval}` 스킬의 `SKILL.md`를 바꿨으면 글의 끝에 작업 트리의 스킬 줄을 붙인다"는 조건과 "이 줄은 다른 글을 더하지 않는다는 규칙의 예외다"가 있다. 줄의 꼴(작업 트리의 그 경로를 읽어 그 절차를 따른다)과 기본 브랜치에서 갈라진 곳부터의 커밋이라는 조건은 낱말 "작업 트리의 스킬 줄"(48줄)에 있다. 통과
- 완료 조건 5 가운데 run의 몫이 참이다.
  - `docs/ARCHITECTURE.md` 26줄(run이 조율만 하고 다섯 스킬에 맡김), 59~66줄(새 에이전트가 수행·확인·회고·평가), `docs/TOOLS.md` 83줄(세션에 실린 스킬 본문은 세션을 띄울 때의 것이라는 사실)을 읽음 → 바뀐 run과 어긋나는 줄이 없다. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 99 tests in 15.106s` `OK`. 통과

**실패**
- 없음

**하네스에서 걸린 것**
- 없음

**판정**: 통과
