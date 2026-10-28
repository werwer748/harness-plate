# Phase 3: 맥락 문서, 테스트 설명, 버전을 맞춘다

**목표**: ADR, PRD, ARCHITECTURE, 문서 지도, 이 저장소의 BACKLOG, 테스트 모듈 설명이 바뀐 규칙과 맞고 버전이 0.22.0이 된다.

**테스트 먼저**: 아니오 — 문서와 매니페스트의 버전 줄만 바꾼다

**읽을 것**
- `docs/ADR.md` (ADR-020, ADR-024의 꼴)
- `docs/PRD.md` (핵심 기능 8)
- `docs/ARCHITECTURE.md` (디렉터리 구조의 `test_skill_rules.py` 줄, 데이터 흐름의 tasks 끝)
- `AGENTS.md` (문서 지도의 `docs/BACKLOG.md` 행)
- `docs/BACKLOG.md`
- `tests/test_skill_rules.py` (모듈 docstring)
- `plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`
- `docs/TOOLS.md`, `docs/cleanup/2026-10-28.md` (맥락 문서)

**TODO**
- [ ] `docs/ADR.md` 끝에 ADR-025가 더해진다. 내용은 task 머리의 결정 "ADR-025의 내용"(결정, 이유, 트레이드오프)이고, ADR-020의 결정에 `ADR-025로 바뀜`이 붙는다 (`docs/ADR.md`)
- [ ] PRD 핵심 기능 8의 `plate 자체의 고칠 거리는 GitHub 이슈로 올리고(ADR-020)`가 `문턱을 넘은 plate 자체의 고칠 거리만 GitHub 이슈로 올리고(ADR-025)`로 바뀌고, 넘지 않은 것과 감수한 것이 `docs/BACKLOG.md`로 간다는 것이 같은 문장에 든다 (`docs/PRD.md`)
- [ ] ARCHITECTURE 데이터 흐름의 `승인받은 대로 plate 자체의 고칠 거리는 GitHub 이슈로 올리고`가 `문턱을 넘은 plate 자체의 고칠 거리는 GitHub 이슈로 올리고`로 바뀌고, 미룬 하네스 고칠 거리와 감수한 것도 `docs/BACKLOG.md`에 적는다는 것이 든다. `test_skill_rules.py` 줄의 괄호 목록 끝에 `eval 고칠 거리의 처리와 문턱`과 `run 처음 안의 문턱과 BACKLOG 세 절`이 더해진다 (`docs/ARCHITECTURE.md`)
- [ ] 문서 지도의 BACKLOG 행이 task 머리의 결정의 행으로 바뀐다 (`AGENTS.md`)
- [ ] `docs/BACKLOG.md`가 `# BACKLOG` 아래에 세 절(`## 소스 문제`, `## 하네스 고칠 거리`, `## 감수한 것`)을 가진 빈 꼴이 된다 (`docs/BACKLOG.md`)
- [ ] 테스트 모듈 docstring의 eval 목록에 `#74`가 더해진다 (`tests/test_skill_rules.py`)
- [ ] 두 매니페스트의 `"version"`이 `0.22.0`이 된다 (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)

**통과 조건**
- 완료 조건 4, 5, 6이 참이다.
  - 확인: 완료 조건 4의 확인을 모두 돌린다
  - 확인: 완료 조건 5의 확인을 모두 돌린다(네 시험 모두)
  - 확인: 완료 조건 6의 확인을 모두 돌린다
- 완료 조건 1, 2, 3의 글이 그대로 있다.
  - 확인: 완료 조건 1, 2, 3의 `grep` 확인을 모두 돌린다(헤드리스 시험은 다시 돌리지 않는다)
