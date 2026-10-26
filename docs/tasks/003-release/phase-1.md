# Phase 1: 버전과 문서

**목표**: 두 매니페스트가 0.13.0이 되고, 맥락 문서와 README의 어긋난 줄이 바뀐 동작에 맞게 고쳐진다.

**테스트 먼저**: 아니오 — 버전 값과 `.md`만 고친다. 테스트는 매니페스트를 읽지 않는다

**읽을 것**
- `plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json` (3줄 버전)
- `git diff main -- plugins/plate/skills/plan/SKILL.md plugins/plate/skills/run/SKILL.md plugins/plate/skills/review/SKILL.md` (이 tasks가 바꾼 스킬 본문)
- `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md` (맥락 문서)
- `README.md` (1~16줄 개요, 17줄 tasks 끝의 PR, 21줄 CI 워크플로)

**TODO**
- [ ] 두 매니페스트의 `"version"` 값이 `0.12.0`에서 `0.13.0`으로 바뀐다 (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)
- [ ] 맥락 문서 넷 가운데 바뀐 동작과 어긋나는 줄이 바뀐다. 문서마다 어긋난 줄이 없으면 고치지 않고 기록에 그렇다고 적는다 (`docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`)
- [ ] README의 개요, tasks 끝의 PR, CI 워크플로 절 가운데 바뀐 동작과 어긋나는 줄이 바뀐다. 어긋난 줄이 없으면 고치지 않고 기록에 그렇다고 적는다 (`README.md`)

**통과 조건**
- 완료 조건 1이 참이다.
  - 확인: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json`의 두 줄이 모두 `"version": "0.13.0",`
- 완료 조건 2가 참이다.
  - 확인: `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
- 완료 조건 3이 참이다.
  - 확인: `python3 -m unittest discover -s tests`가 `OK`
- 완료 조건 4가 참이다.
  - 확인: `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `README.md`를 문서마다 따로 읽어, 이 tasks가 바꾼 동작(plan의 초안 전 점검, run이 넘기는 작업 트리 경로, review의 결과물인 마크다운과 그 줄을 커버리지·중복에서 빼는 것)과 어긋나는 줄이 없다. 한 문서라도 어긋나는 줄이 있으면 실패
- 완료 조건 5가 참이다.
  - 확인: `grep -n -A3 '^## 결과물인 마크다운' docs/ARCHITECTURE.md`가 그 절과 `plugins/plate/skills/*/SKILL.md` 경로를 낸다
