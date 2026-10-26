# Phase 2: review가 결과물인 마크다운을 평가한다

**목표**: review의 바뀐 코드 파일이 `## 결과물인 마크다운` 절의 `.md`를 두 모드에서 넣고 게이트의 커버리지·중복에서는 그 줄을 빼며, 이 저장소의 `docs/ARCHITECTURE.md`에 그 절이 생기고, 맥락 문서의 review 줄이 그와 맞는다.

**테스트 먼저**: 아니오 — `.md`만 고친다

**읽을 것**
- `plugins/plate/skills/review/SKILL.md` (32~33줄 낱말 "바뀐 코드 파일"과 "새 줄", 49줄 git 레포가 아닐 때, 67~68줄 커버리지·중복, 126~127줄 게이트, 152~200줄 PR 모드와 `coverage` 행, 209~213줄 평가 절의 대상)
- `gh issue view 22 -R werwer748/harness-plate` (#22의 본문)
- `docs/ARCHITECTURE.md` (9~37줄 디렉터리 구조, 30줄 review 줄, 51줄 PR의 CI 문단, 65줄 tasks 끝, 73줄 review 잡)
- `docs/PRD.md` (18줄 핵심 기능 8)

**TODO**
- [ ] 낱말 "바뀐 코드 파일"이 `docs/ARCHITECTURE.md`의 `## 결과물인 마크다운` 절에 적힌 경로의 `.md`를 넣도록 바뀌고, 절이 없으면 지금처럼 `.md`를 뺀다. 0번의 git 레포가 아닐 때의 줄도 같이 바뀐다 (`plugins/plate/skills/review/SKILL.md`)
- [ ] PR 모드 절에 그 절을 기준 브랜치의 `docs/ARCHITECTURE.md`(`git show <기준 브랜치>:docs/ARCHITECTURE.md`)에서 읽는다는 줄이 더해진다 (`plugins/plate/skills/review/SKILL.md`)
- [ ] 결과물인 `.md`의 줄은 커버리지와 중복의 새 줄 수에서 빠지고 판단과 등급의 근거에는 든다는 것이 낱말 "새 줄", 2번, 6번, PR 모드 `coverage` 행에 맞게 더해진다 (`plugins/plate/skills/review/SKILL.md`)
- [ ] 평가 절 양식의 대상에 결과물인 `.md`로 넣은 파일을 구별해 적는 자리가 더해진다 (`plugins/plate/skills/review/SKILL.md`)
- [ ] `## 결과물인 마크다운` 절이 생기고 `plugins/plate/skills/*/SKILL.md`를 적는다 (`docs/ARCHITECTURE.md`)
- [ ] `docs/ARCHITECTURE.md` 30줄, 51줄, 65줄, 73줄과 `docs/PRD.md` 18줄 가운데 바뀐 review와 어긋나는 줄이 바뀐다. 어긋나는 줄이 없으면 고치지 않고 기록에 그렇다고 적는다 (`docs/ARCHITECTURE.md`, `docs/PRD.md`)

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
