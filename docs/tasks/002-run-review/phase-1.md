# Phase 1: run이 작업 트리의 스킬 경로를 넘긴다

**목표**: run이 맡기는 다섯 곳에서, tasks가 바꾼 스킬이면 작업 트리의 `SKILL.md` 경로를 읽어 따르라는 줄을 붙이고, 맥락 문서의 run 줄이 그와 맞는다.

**테스트 먼저**: 아니오 — `.md`만 고친다

**읽을 것**
- `plugins/plate/skills/run/SKILL.md` (16~20줄 절대 규칙, 106~156줄 4·5·7번, 262~280줄 "코드 평가를 맡긴다"와 "하네스 eval을 맡긴다")
- `gh issue view 21 -R werwer748/harness-plate` (#21의 본문)
- `docs/TOOLS.md` (83줄 세션에 실린 스킬 본문이 세션을 띄울 때의 것이라는 사실)
- `docs/ARCHITECTURE.md` (26줄 run 줄, 59~66줄 데이터 흐름의 실행과 tasks 끝)

**TODO**
- [ ] 4번, 5번, 7번, "코드 평가를 맡긴다", "하네스 eval을 맡긴다"의 넘기는 글 아래에, 기본 브랜치에서 갈라진 곳부터의 tasks 커밋이 그 스킬의 작업 트리 `SKILL.md`를 바꿨을 때만 붙이는 줄(작업 트리의 그 경로를 읽어 그 절차를 따른다)과 그 조건이 더해진다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] 다섯 곳의 "다른 글을 더하지 않는다"가 그 줄을 예외로 두도록 바뀐다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] `docs/ARCHITECTURE.md` 26줄, 59~66줄과 `docs/TOOLS.md` 83줄 가운데 바뀐 run과 어긋나는 줄이 바뀐다. 어긋나는 줄이 없으면 고치지 않고 기록에 그렇다고 적는다 (`docs/ARCHITECTURE.md`, `docs/TOOLS.md`)

**통과 조건**
- 완료 조건 1이 참이다.
  - 확인: `plugins/plate/skills/run/SKILL.md`의 4번, 5번, 7번, "코드 평가를 맡긴다", "하네스 eval을 맡긴다"를 하나씩 읽어 다섯 곳 모두에 그 줄을 붙이는 조건과 예외가 있다. 한 곳이라도 없으면 실패
- 완료 조건 5 가운데 run의 몫이 참이다.
  - 확인: `docs/ARCHITECTURE.md` 26줄과 59~66줄, `docs/TOOLS.md` 83줄을 하나씩 읽어 바뀐 run과 어긋나는 줄이 없다
- 테스트가 모두 통과한다.
  - 확인: `python3 -m unittest discover -s tests`가 `OK`
