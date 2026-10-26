# Phase 1: 버전을 올리고 문서를 맞춘다

**목표**: 버전이 0.12.0이고, 매니페스트 설명, README, ARCHITECTURE, ADR, TOOLS가 바뀐 동작과 맞으며, 검증과 테스트가 통과한다.

**테스트 먼저**: 아니오 — 버전 값과 `.md`만 고친다

**읽을 것**
- `docs/tasks/plan.md` (tasks 머리의 목표와 완료 조건)
- `docs/tasks/001-ci-trust/`~`docs/tasks/005-eval-rules/`의 task 머리 (바뀐 동작을 모으려고)
- `plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`
- `README.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`
- `git show e521e80 -- plugins/plate/.claude-plugin/plugin.json docs/TOOLS.md` (0.11.0을 낼 때 바꾼 꼴)

**TODO**
- [ ] 두 매니페스트의 `version`을 `0.12.0`으로 올린다 (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)
- [ ] 두 매니페스트의 `description`에서 완료 조건 2의 일곱과 어긋나는 글을 고친다. 어긋남이 없으면 그대로 둔다 (같은 두 파일)
- [ ] `README.md`에서 바뀐 동작과 어긋나는 줄을 고친다. 특히 "CI 워크플로" 절이 지침 파일 되돌리기와 실패 때 오류 줄을 다루는지 본다 (`README.md`)
- [ ] `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`를 하나씩 읽어 001~005가 맞추고 남긴 어긋남을 고친다 (같은 세 파일)
- [ ] `docs/TOOLS.md` 17줄 근처의 판정 버전 문단에 `tasks issue-fixes(0.12.0)`의 시험을 돌린 Claude Code 버전과 날짜를 더한다. 버전은 `claude --version`으로, 날짜는 001 phase 3의 기록에서 가져온다 (`docs/TOOLS.md`)

**통과 조건**
- 완료 조건 1이 참이다.
  - 확인: `grep -n '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json`이 두 줄 모두 `"0.12.0"`
  - 확인: `claude plugin validate .`가 오류 없이 끝난다
  - 확인: 네 문서를 하나씩 따로 읽어 문서마다 일곱과 어긋나는 줄이 없다. 문서마다 결과를 적는다
- 완료 조건 2가 참이다.
  - 확인: 두 `description`을 읽어 어긋나는 글이 없다
- 완료 조건 3이 참이다.
  - 확인: `grep -n 'issue-fixes(0.12.0)' docs/TOOLS.md`가 판정 버전 문단에서 한 줄을 낸다
- 테스트가 모두 통과한다.
  - 확인: `python3 -m unittest discover -s tests`가 `OK`
