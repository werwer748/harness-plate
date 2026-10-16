# Phase 4: 맥락 문서와 버전

**목표**: PRD, ARCHITECTURE, ADR이 훅과 6~9단계를 반영하고 두 매니페스트가 0.9.0이다.

**읽을 것**
- `docs/PRD.md` (목표, 핵심 기능, 범위 밖)
- `docs/ARCHITECTURE.md` (기술 스택, 디렉터리 구조, 패턴과 규칙의 "막는 장치" 줄)
- `docs/ADR.md` (항목의 꼴: 결정, 이유, 트레이드오프)
- `plugins/plate/hooks/`, `tests/` (phase 1의 결과)
- `plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`

**TODO**
- [ ] PRD의 목표, 범위 밖, 핵심 기능이 완료 조건 7대로 바뀐다 (`docs/PRD.md`)
- [ ] ARCHITECTURE의 기술 스택에 Python 3 훅이, 디렉터리 구조에 `plugins/plate/hooks/`와 `tests/`가 들어간다. 패턴과 규칙의 "훅은 두지 않는다"는 바뀐 규칙이 된다: 규칙 구간이 기본이고, 훅은 Claude Code의 구현이며, 세 번 막히면 멈춰 논의한다 (`docs/ARCHITECTURE.md`)
- [ ] ADR에 훅 스크립트의 런타임(Python 3 표준 라이브러리) 항목이 생긴다 (`docs/ADR.md`)
- [ ] 두 매니페스트의 버전이 0.9.0이 되고 설명에 훅이 들어간다 (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)

**통과 조건**
- 완료 조건 1, 7, 8, 13이 참이다.
  - 확인: 완료 조건 1, 7, 8, 13의 확인을 모두 돌린다
