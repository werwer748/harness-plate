# Phase 1: 버전, README, 맥락 문서

**목표**: 버전이 0.15.0이 되고 README와 맥락 문서가 바뀐 동작과 맞는다.

**테스트 먼저**: 아니오 — 매니페스트의 버전과 `.md`만 고친다

**읽을 것**
- `plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json` (버전 줄)
- `README.md` (표의 `plan`, `run`, `check`, `retro`, `review`, `eval` 행과 그 아래 절)
- `docs/PRD.md` (핵심 기능 3~8)
- `docs/ARCHITECTURE.md` ("패턴과 규칙", "데이터 흐름")
- `docs/ADR.md` (ADR-024)
- `docs/TOOLS.md` ("Claude Code" 절)
- `plugins/plate/skills/plan/SKILL.md`, `plugins/plate/skills/check/SKILL.md`, `plugins/plate/skills/retro/SKILL.md`, `plugins/plate/skills/run/SKILL.md`, `plugins/plate/skills/review/SKILL.md`, `plugins/plate/skills/eval/SKILL.md` (앞 task들이 고친 본문. 읽기만 한다)

**TODO**
- [ ] 두 매니페스트의 `"version"`이 `0.15.0`으로 바뀐다 (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)
- [ ] README의 표에서 `plan`, `run`, `check`, `retro`, `review`, `eval` 행과 그 아래 절 가운데 바뀐 여섯 동작과 어긋나는 글이 맞게 바뀐다. 어긋나는 글이 없으면 그대로 둔다 (`README.md`)
- [ ] `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`에서 바뀐 여섯 동작과 어긋나는 줄이 맞게 바뀐다. 어긋나는 줄이 없으면 그대로 둔다 (`docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`)

**통과 조건**
- 완료 조건 1이 참이다.
  - 확인: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json`의 두 줄이 모두 `0.15.0`
  - 확인: `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
  - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
- 완료 조건 2가 참이다.
  - 확인: `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `README.md`를 문서마다 따로 읽어, 여섯 동작(plan의 줄 번호 규칙, plan의 돌려 보는 확인과 `돌리지 않음` 줄, check와 retro의 "남은 것" 판정, run의 로컬 기본 브랜치 물음과 로컬 merge-base, review의 결과물인 마크다운 테스트 적절성, eval의 정해 둔 물음) 가운데 어느 것과도 어긋나는 줄이 없다. 어긋나는 줄이 하나라도 있으면 실패
