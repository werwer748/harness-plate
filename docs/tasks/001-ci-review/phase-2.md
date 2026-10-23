# Phase 2: review의 PR 모드

**목표**: review를 PR 모드로 부르면 tasks 머리 없이 PR에서 바뀐 코드를 평가해 평가서 파일과 등급 묶음을 낸다.

**테스트 먼저**: 아니오 — 스킬 본문(`.md`)만 고친다

**읽을 것**
- `plugins/plate/skills/review/SKILL.md` (tasks 끝 코드 평가의 절차, 등급표, 게이트, 기록의 양식)
- `docs/ARCHITECTURE.md` (명령 절, 패턴과 규칙)
- https://code.claude.com/docs/en/github-actions ("Run a skill"과 "Interactive and automation modes": 워크플로의 `prompt`로 플러그인 스킬을 부르는 꼴)
- https://raw.githubusercontent.com/anthropics/claude-code-action/main/action.yml (`claude_args`에 `--json-schema`를 주면 나오는 `structured_output`)

**TODO**
- [x] review를 PR 모드로 부르는 길이 생긴다. 부를 때 받는 것(기준 브랜치 같은 것)과, tasks 머리 없이 기준 브랜치에서 갈라진 곳부터 바뀐 코드 파일만 보는 범위가 적힌다 (`plugins/plate/skills/review/SKILL.md`)
- [x] PR 모드는 재기 전에 명령 절의 설치 명령을 돌린다. 명령 절, 커버리지, 중복, 정적 분석, 보안 검사와 네 범주(신뢰성, 보안, 유지보수성, 테스트 적절성), 게이트를 tasks 끝과 같은 등급표로 매기고, 기능 적합성은 매기지 않는다 (`plugins/plate/skills/review/SKILL.md`)
- [x] PR 모드는 평가서를 파일로 쓰고, 커밋하지 않고, 묻지 않는다. 판정 스크립트가 읽을 등급 묶음(빌드·린트·테스트의 결과, 새 줄 커버리지, 신뢰성·보안·유지보수성의 등급, 모름을 가릴 수 있는 값)을 구조화 출력으로 돌려준다. 등급 묶음의 꼴(키와 값)은 PR 모드 절에 적힌다 (`plugins/plate/skills/review/SKILL.md`)
- [x] tasks 끝 코드 평가의 절차와 결과는 바뀌지 않고, 스킬 설명(description)에 PR 모드가 든다 (`plugins/plate/skills/review/SKILL.md`)

**통과 조건**
- 완료 조건 2가 참이다.
  - 확인: 완료 조건 2의 확인을 모두 돌린다
- 완료 조건 1이 그대로 참이다. 이 phase도 `review/SKILL.md`를 고친다.
  - 확인: 완료 조건 1의 확인을 모두 돌린다

## 한 일
- review를 PR 모드로 부르는 길이 생긴다: 머리말에 PR 모드로 불리면 0~9번 대신 "PR 모드" 절을 따른다는 줄을 넣고, 9번 뒤에 "PR 모드" 절을 더했다. 받는 것은 `PR 모드`라는 말과 기준 브랜치(ref), 평가서 파일 경로이고, 갈라진 곳은 `git merge-base <기준 브랜치> HEAD`, 바뀐 코드 파일과 새 줄은 거기서부터 센다. 0번의 조건(tasks 머리, 남은 phase, 지금 브랜치)은 보지 않고, 1번에서 tasks 머리와 task 머리를 빼고 읽는다 (`plugins/plate/skills/review/SKILL.md`)
- PR 모드는 재기 전에 설치 명령을 돌린다: 절차에 설치(없음이면 돌리지 않고, 실패해도 이어 간다), 2번대로 재기, 4번대로 판단(3번의 완료 조건 확인은 하지 않음), 5번 등급표로 네 범주 매기기(기능 적합성 뺌), 6번대로 게이트를 적었다 (`plugins/plate/skills/review/SKILL.md`)
- PR 모드는 평가서를 파일로 쓰고 커밋하지 않고 묻지 않는다, 등급 묶음: 받은 경로에 `# 코드 평가`와 평가 절 하나를 새로 쓰고(범위에 기준 브랜치, "잰 것"에 설치 줄, 완료 조건과 기능 적합성 뺌), 커밋하지 않는다. 등급 묶음은 키 `build`, `lint`, `test`(`pass`/`fail`/`none`/`unmeasured`), `coverage`(0~100의 수/`skipped`/`unmeasured`), `reliability`, `security`, `maintainability`(`A`~`E`/`unjudged`)의 JSON을 구조화 출력으로 돌려주고, 모름은 `unmeasured`와 `unjudged`로 가린다. 절대 규칙 1과 5에 PR 모드의 쓰는 파일과 커밋하지 않음을 더했다 (`plugins/plate/skills/review/SKILL.md`)
- tasks 끝 코드 평가의 절차는 바뀌지 않고 description에 PR 모드가 든다: description에 PR 모드 한 문장을 더했다(620자). 0~9번 절은 건드리지 않았다 (`plugins/plate/skills/review/SKILL.md`)

## 확인 결과
- 완료 조건 2가 참이다.
  - `plugins/plate/skills/review/SKILL.md`의 "PR 모드" 절을 읽음 → tasks 머리 없이(0번 조건 안 봄, tasks 머리·task 머리 안 읽음) 기준 브랜치에서 갈라진 곳부터 바뀐 코드 파일만, 재기 전에 설치, 명령 절·커버리지·네 범주·게이트를 매기고 기능 적합성은 매기지 않음, 평가서를 파일로 씀, 등급 묶음을 구조화 출력으로 돌려줌, 커밋하지 않고 묻지 않음, 등급 묶음의 키와 값의 표가 있다. 통과
  - `git diff "$(git log --format=%h -1 --grep='^001-ci-review: phase 1$')^" -- plugins/plate/skills/review/SKILL.md` → 바뀐 곳은 description, 머리말 한 줄, 절대 규칙 1과 5, 낱말의 명령 절 정의(phase 1), 9번 뒤의 "PR 모드" 절뿐이고 `## 0.`~`## 9.` 절에는 변경이 없다. 통과
- 완료 조건 1이 그대로 참이다.
  - `grep -n "설치" plugins/plate/skills/plan/SKILL.md plugins/plate/skills/check/SKILL.md plugins/plate/skills/retro/SKILL.md plugins/plate/skills/review/SKILL.md` → plan:29, check:29, retro:29, review:34에 명령 절 정의의 `- 설치: {명령}`이 나온다. 통과
  - `grep -c "^- 설치: 없음$" docs/ARCHITECTURE.md` → `1`. 통과
  - plan의 3번(62줄: 설치도 매니페스트와 코드에서 찾고 못 찾으면 5번에서 묻는다)과 5번(76줄: 찾지 못한 설치도 묻는다)을 읽음. check 3번(48줄)과 retro 3번(60줄)은 "설치는 돌리지 않는다", review는 명령 절 정의(34줄)에 "tasks 끝의 코드 평가는 설치를 돌리지 않는다"이고 2번의 1(64줄)은 빌드·린트·테스트만 돌린다. 설치는 PR 모드에서만 돈다. 통과
- 덧붙여 `python3 -m unittest discover -s tests` → `Ran 39 tests`, `OK`

## 계획과 달라진 점
- 없음

## 남은 것
- 없음

## 하네스에서 걸린 것
- task 머리의 결정 3은 "PR 코드에 숨은 지시가 있어도 에이전트에게는 머지 권한이 없다"를 이유로 들지만, 등급 묶음이 자동 머지를 정하므로 PR이 바꾼 코드나 `AGENTS.md`의 지시가 등급을 올리게 할 길은 남는다(절대 규칙의 "프로젝트의 규칙을 따른다"도 PR이 바꾼 `AGENTS.md`를 읽는다). 이 phase의 TODO 밖이라 PR 모드에 막는 글은 넣지 않았다. 회고나 002에서 볼 거리다.
