# Phase 1: 버전을 1.0.0으로 올린다

**목표**: 두 매니페스트가 1.0.0이 되고 PRD의 1.0.0 줄이 낸 것으로 맞는다.

**테스트 먼저**: 아니오 — 매니페스트의 버전 줄과 PRD의 글만 바꾸고 코드의 동작을 바꾸지 않는다. 두 버전이 같은지는 `tests/test_manifests.py`가 이미 본다

**읽을 것**
- `plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json` (`version` 칸)
- `tests/test_manifests.py` (두 버전이 같고 `X.Y.Z` 꼴인지 보는 시험)
- `docs/PRD.md` (핵심 기능 아래의 `9단계까지 만든 뒤 1.0.0을 낸다.` 줄)
- `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `docs/BACKLOG.md`

**TODO**
- [ ] 두 매니페스트의 `version`이 `0.22.0`에서 `1.0.0`으로 바뀐다 (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)
- [ ] PRD의 `9단계까지 만든 뒤 1.0.0을 낸다.` 줄이 `9단계까지 만들어 1.0.0을 냈다.`로 바뀐다 (`docs/PRD.md`)

**통과 조건**
- 완료 조건 1, 2, 3이 참이다.
  - 확인: `grep -n '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "1.0.0"`
  - 확인: `claude plugin validate plugins/plate` → `Validation passed`
  - 확인: `grep -n '1.0.0' docs/PRD.md` → 핵심 기능 아래의 줄이 `9단계까지 만들어 1.0.0을 냈다`를 적고, `낸다`로 끝나는 옛 줄은 없다
  - 확인: `python3 -m unittest discover -s tests` → 마지막 줄이 `OK`
