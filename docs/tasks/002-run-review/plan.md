# run의 작업 트리 경로와 review의 결과물인 마크다운

## 목표
run이 tasks가 바꾼 스킬의 작업 트리 경로를 맡기는 글에 붙이고(#21), review가 `docs/ARCHITECTURE.md`의 `## 결과물인 마크다운` 절에 적힌 `.md`를 두 모드에서 바뀐 코드 파일로 평가하며(#22), 이 저장소의 `docs/ARCHITECTURE.md`에 그 절이 생긴다.

## 범위 밖
- setup의 `docs/ARCHITECTURE.md` 양식에 그 절을 넣는 것
- 판정 스크립트(`plugins/plate/ci/verdict.py`)의 세 규칙을 바꾸는 것
- plan 스킬을 고치는 것(`001-plan-rules`가 했다), 버전과 README(`003-release`가 한다)

## 완료 조건
1. (#21) run이 수행(4번), 확인(5번), 회고(7번), 코드 평가, 하네스 eval을 맡길 때, 기본 브랜치에서 갈라진 곳부터의 tasks 커밋이 그 스킬의 작업 트리 `SKILL.md`를 바꿨으면 넘기는 글에 작업 트리의 그 경로를 읽어 따르라는 줄을 붙이고, "다른 글을 더하지 않는다"는 규칙이 이 줄을 예외로 둔다.
   - 확인: `plugins/plate/skills/run/SKILL.md`의 4번, 5번, 7번, "코드 평가를 맡긴다", "하네스 eval을 맡긴다"를 하나씩 읽어 다섯 곳 모두에 그 줄을 붙이는 조건과 예외가 있다. 한 곳이라도 없으면 실패
2. (#22) review의 낱말 "바뀐 코드 파일"이 `docs/ARCHITECTURE.md`의 `## 결과물인 마크다운` 절에 적힌 경로의 `.md`를 넣고, 절이 없으면 지금처럼 `.md`를 뺀다. PR 모드는 그 절을 기준 브랜치의 `docs/ARCHITECTURE.md`에서 읽는다. git 레포가 아닐 때의 대상과 평가 절의 대상도 그에 맞는다.
   - 확인: `plugins/plate/skills/review/SKILL.md`의 낱말 절, 0번의 git 레포가 아닐 때의 줄, PR 모드 절, 평가 절 양식의 대상을 하나씩 읽어 네 곳이 저마다 위의 것과 맞는다
   - 확인: `grep -rn '바뀐 코드 파일' plugins/plate docs README.md`가 낸 줄 가운데 review 밖의 것을 하나씩 읽어, 바뀐 낱말과 어긋나는 줄이 없다
3. 결과물인 `.md`의 줄은 판단(4번)과 등급의 근거에는 들고, 게이트의 새 줄 커버리지와 새 줄 중복의 새 줄 수에서는 빠진다.
   - 확인: review의 낱말 "새 줄"과 2번의 커버리지·중복 줄, 6번의 두 게이트 줄, PR 모드 `coverage` 행을 하나씩 읽어 결과물인 `.md`의 줄을 커버리지와 중복에서 빼는 것이 네 곳에서 어긋나지 않는다
4. 이 저장소의 `docs/ARCHITECTURE.md`에 `## 결과물인 마크다운` 절이 있고 `plugins/plate/skills/*/SKILL.md`를 적는다.
   - 확인: `grep -n -A3 '^## 결과물인 마크다운' docs/ARCHITECTURE.md`가 그 절과 `plugins/plate/skills/*/SKILL.md` 경로를 낸다
5. 맥락 문서에서 run과 review의 동작을 적은 줄이 바뀐 동작과 맞는다.
   - 확인: `docs/ARCHITECTURE.md` 26줄(run 줄), 30줄(review 줄), 51줄(PR의 CI 문단), 59~66줄(데이터 흐름의 실행과 tasks 끝), 73줄(review 잡), `docs/PRD.md` 18줄(핵심 기능 8), `docs/TOOLS.md` 83줄(세션에 실린 스킬 본문)을 하나씩 읽어 어긋나는 줄이 없다
6. 테스트가 모두 통과한다.
   - 확인: `python3 -m unittest discover -s tests`가 `OK`

## 결정
- #21은 run이 tasks가 바꾼 스킬의 작업 트리 경로를 넘기는 것으로 고친다. 이유: 뒤 회고와 eval이 고친 규칙으로 돈다
- 결과물인 마크다운의 경로는 `docs/ARCHITECTURE.md`의 새 절 `## 결과물인 마크다운`에 적고, 절이 없으면 지금처럼 `.md`를 뺀다. setup의 양식은 바꾸지 않는다. 이유: 명령 절은 여러 스킬이 네 줄로 읽어 꼴을 바꾸면 넓게 번지고, 대부분의 프로젝트는 이 절이 필요 없다
- 이 규칙은 tasks 끝과 PR 모드에 함께 쓰고, PR 모드는 그 절을 기준 브랜치의 것으로 읽는다. 이유: 로컬과 CI가 같은 파일을 보고, PR이 그 절을 바꿔 평가 대상을 빼는 길을 막는다
- 결과물인 `.md`의 줄은 커버리지와 중복의 새 줄 수에서만 뺀다. 이유: 도구가 잴 수 없는 줄이 게이트를 측정 못함으로 만들지 않고, 판정 스크립트의 세 규칙은 바꾸지 않아도 된다
- 확인은 스킬 본문을 읽어 한다. 이유: 바뀌는 것이 스킬 본문의 규칙 글이다 (추천안으로 정함)
