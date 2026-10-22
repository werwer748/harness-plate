# Phase 2: review의 PR 모드

**목표**: review를 PR 모드로 부르면 tasks 머리 없이 PR에서 바뀐 코드를 평가해 평가서 파일과 등급 묶음을 낸다.

**테스트 먼저**: 아니오 — 스킬 본문(`.md`)만 고친다

**읽을 것**
- `plugins/plate/skills/review/SKILL.md` (tasks 끝 코드 평가의 절차, 등급표, 게이트, 기록의 양식)
- `docs/ARCHITECTURE.md` (명령 절, 패턴과 규칙)
- https://code.claude.com/docs/en/github-actions ("Run a skill"과 "Interactive and automation modes": 워크플로의 `prompt`로 플러그인 스킬을 부르는 꼴)
- https://raw.githubusercontent.com/anthropics/claude-code-action/main/action.yml (`claude_args`에 `--json-schema`를 주면 나오는 `structured_output`)

**TODO**
- [ ] review를 PR 모드로 부르는 길이 생긴다. 부를 때 받는 것(기준 브랜치 같은 것)과, tasks 머리 없이 기준 브랜치에서 갈라진 곳부터 바뀐 코드 파일만 보는 범위가 적힌다 (`plugins/plate/skills/review/SKILL.md`)
- [ ] PR 모드는 재기 전에 명령 절의 설치 명령을 돌린다. 명령 절, 커버리지, 중복, 정적 분석, 보안 검사와 네 범주(신뢰성, 보안, 유지보수성, 테스트 적절성), 게이트를 tasks 끝과 같은 등급표로 매기고, 기능 적합성은 매기지 않는다 (`plugins/plate/skills/review/SKILL.md`)
- [ ] PR 모드는 평가서를 파일로 쓰고, 커밋하지 않고, 묻지 않는다. 판정 스크립트가 읽을 등급 묶음(빌드·린트·테스트의 결과, 새 줄 커버리지, 신뢰성·보안·유지보수성의 등급, 모름을 가릴 수 있는 값)을 구조화 출력으로 돌려준다. 등급 묶음의 꼴(키와 값)은 PR 모드 절에 적힌다 (`plugins/plate/skills/review/SKILL.md`)
- [ ] tasks 끝 코드 평가의 절차와 결과는 바뀌지 않고, 스킬 설명(description)에 PR 모드가 든다 (`plugins/plate/skills/review/SKILL.md`)

**통과 조건**
- 완료 조건 2가 참이다.
  - 확인: 완료 조건 2의 확인을 모두 돌린다
- 완료 조건 1이 그대로 참이다. 이 phase도 `review/SKILL.md`를 고친다.
  - 확인: 완료 조건 1의 확인을 모두 돌린다
