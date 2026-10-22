# Phase 2: setup과 CI 없는 PR 장면

**목표**: 시험 저장소를 origin으로 둔 시험 폴더에서 setup이 CI 워크플로를 둘지 묻고, plate 워크플로가 없는 시험 저장소로 run이 PR을 열어 평가서 댓글을 단다.

**테스트 먼저**: 아니오 — 시험 폴더에서 스킬을 돌려 보고, 이 저장소에서는 `docs/TOOLS.md`만 고친다

**읽을 것**
- `docs/TOOLS.md`의 Claude Code 절 (헤드리스 실행과 세션 잇기, 묻는 글을 기록에 남기는 법, "tasks 실행의 판정에서 본 것"의 시험 폴더와 실행 스크립트)
- `plugins/plate/skills/setup/SKILL.md` (CI 워크플로의 물음, 양식, 보고의 시크릿 안내)
- `plugins/plate/skills/run/SKILL.md` (tasks 끝의 PR 절, 평가서 댓글)
- `plugins/plate/hooks/hooks.json`과 거기에 걸린 푸시 훅 (셋업된 폴더에서 기본 브랜치로 하는 푸시를 막는다)

**TODO**
- [ ] 시험 저장소의 `main`에 코드와 그 테스트가 있는 작은 시험 프로젝트가 생기고, plate 워크플로는 없다 (`werwer748/plate-ci-test`)
- [ ] setup 장면: 시험 저장소를 origin으로 둔 시험 폴더에서 setup이 CI 에이전트를 둘지 묻고, 승인하면 그 폴더의 `.github/workflows/` 아래에 워크플로 파일이 생기고 보고에 `CLAUDE_CODE_OAUTH_TOKEN` 시크릿 등록 방법이 있다. 실행 기록은 setup 본문을 마지막으로 고친 뒤에 만든다
- [ ] CI 없는 run 장면: 시험 저장소를 origin으로 두고 CI 에이전트를 거절해 셋업한 다른 시험 폴더에서 작은 tasks를 계획해 run을 끝까지 돌리면, tasks 끝에 PR을 열지 묻는다. 승인하면 `tasks/`로 시작하는 브랜치에서 `main`으로 가는 PR이 열리고 평가서 댓글이 달린다. 실행 기록은 run 본문을 마지막으로 고친 뒤에 만든다
- [ ] 이 phase의 기록에 장면마다 시험 폴더와 실행 기록의 경로가, run 장면에는 PR 번호도 적힌다 (`docs/tasks/005-publish-verify/phase-2.md`)
- [ ] 이 phase에서 확인한 도구의 사실이 시험 폴더와 실행 기록의 위치와 함께 적힌다 (`docs/TOOLS.md`)

**통과 조건**
- 완료 조건 3이 참이다.
  - 확인: 완료 조건 3의 확인을 모두 돌린다. `done-phase-2.md`는 이름이 바뀌기 전인 이 파일로 읽는다
- 시험 저장소의 `main`에 plate 워크플로가 없다.
  - 확인: `gh api repos/werwer748/plate-ci-test/contents/.github/workflows`가 404로 실패한다
- 이 phase에서 확인한 도구의 사실이 `docs/TOOLS.md`에 적혀 있다.
  - 확인: `docs/TOOLS.md`의 Claude Code 절을 읽어 이 phase의 장면에서 본 것이 시험 폴더와 실행 기록의 위치와 함께 있다
