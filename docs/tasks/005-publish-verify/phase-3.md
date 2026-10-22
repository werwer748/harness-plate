# Phase 3: CI의 세 판정

**목표**: 시험 저장소의 `main`에 plate 복사본과 CI 워크플로가 있고, 세 판정의 PR과 run이 연 PR에서 CI가 평가서를 달고 판정대로 한다.

**테스트 먼저**: 아니오 — 시험 저장소에서 워크플로를 돌려 보고, 이 저장소에서는 `docs/TOOLS.md`만 고친다

**읽을 것**
- `docs/TOOLS.md`의 Claude Code 절 (헤드리스 실행과 세션 잇기, "tasks 실행의 판정에서 본 것"의 시험 폴더와 실행 스크립트)
- `plugins/plate/skills/setup/SKILL.md`의 양식 절 (CI 워크플로)
- `plugins/plate/skills/review/SKILL.md`의 PR 모드 절 (등급 묶음의 꼴)
- 판정 스크립트와 그 테스트 (`docs/ARCHITECTURE.md`의 디렉터리 구조에 경로가 있다. 세 규칙의 경계)
- `plugins/plate/skills/run/SKILL.md` (tasks 끝의 PR 절)
- `plugins/plate/hooks/hooks.json`과 거기에 걸린 푸시 훅 (셋업된 폴더에서 기본 브랜치로 하는 푸시를 막는다)
- https://code.claude.com/docs/en/github-actions (설정, 시크릿, `claude_args`)
- https://raw.githubusercontent.com/anthropics/claude-code-action/main/action.yml (입력과 `structured_output`)

**TODO**
- [ ] 시험 저장소의 `main`에 `plugins/plate`의 복사본과 CI 워크플로가 생긴다. 워크플로는 setup 양식에서 plate를 받는 곳만 그 복사본을 쓰도록 바꾼 것이다. `main`을 새로 받아 복사본을 `diff -r <복사본> plugins/plate`로 견주면 아무것도 나오지 않는다 (`werwer748/plate-ci-test`)
- [ ] 세 판정의 장면: 판정마다 그 판정이 나오게 바꾼 PR을 시험 저장소에 연다. CI가 PR마다 평가서를 댓글로 달고, 자동 머지 장면의 PR은 `MERGED`, 머지 요청 장면은 `OPEN`, 닫기 장면은 `CLOSED`가 된다. 세 PR의 CI는 `main`의 복사본을 마지막으로 바꾼 뒤에 돈다
- [ ] CI 있는 run 장면: 시험 저장소를 origin으로 둔 셋업된 시험 폴더에서 작은 tasks를 계획해 run을 끝까지 돌리면, tasks 끝에 PR을 열지 묻는다. 승인하면 `tasks/`로 시작하는 브랜치에서 `main`으로 가는 PR이 열리고, run은 평가서 댓글을 달지 않으며 CI가 단다. 실행 기록은 run 본문을 마지막으로 고친 뒤에 만든다
- [ ] 이 phase의 기록에 장면마다 PR 번호가, run 장면에는 시험 폴더와 실행 기록의 경로도 적힌다 (`docs/tasks/005-publish-verify/phase-3.md`)
- [ ] 이 phase에서 확인한 도구의 사실(claude-code-action의 동작, 워크플로가 댓글을 달고 머지하고 닫는 꼴)이 시험 저장소와 실행 기록의 위치와 함께 적힌다 (`docs/TOOLS.md`)

**통과 조건**
- 완료 조건 4가 참이다.
  - 확인: 완료 조건 4의 확인을 모두 돌린다. `done-phase-3.md`는 이름이 바뀌기 전인 이 파일로 읽는다
- 이 phase에서 확인한 도구의 사실이 `docs/TOOLS.md`에 적혀 있다.
  - 확인: `docs/TOOLS.md`의 Claude Code 절을 읽어 이 phase의 장면에서 본 것이 시험 저장소와 실행 기록의 위치와 함께 있다
