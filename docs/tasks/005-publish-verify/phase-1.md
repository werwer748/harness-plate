# Phase 1: 공개와 0.11.0

**목표**: harness-plate가 공개 저장소가 되고, 두 매니페스트가 0.11.0이 되며, 맥락 문서와 README가 바뀐 동작과 공개 저장소를 적는다.

**테스트 먼저**: 아니오 — 문서(`.md`)와 매니페스트의 버전 줄만 고치고 동작은 바꾸지 않는다

**읽을 것**
- `README.md` (스킬 표, 설치)
- `docs/PRD.md` (목표, 핵심 기능 8), `docs/ARCHITECTURE.md` (기술 스택의 배포 줄, 디렉터리 구조, 패턴과 규칙, 데이터 흐름, 명령 절), `docs/ADR.md` (항목의 꼴, ADR-005)
- `plugins/plate/skills/run/SKILL.md`, `plugins/plate/skills/review/SKILL.md`, `plugins/plate/skills/setup/SKILL.md`, `plugins/plate/hooks/hooks.json` (이 tasks에서 바뀐 동작: tasks 끝의 PR, review의 PR 모드, setup의 CI 워크플로, 푸시 훅)
- `plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json` (버전)
- `.claude-plugin/marketplace.json` (마켓플레이스 목록)
- https://code.claude.com/docs/en/plugin-marketplaces (GitHub 저장소를 마켓플레이스로 더하는 꼴)

**TODO**
- [ ] harness-plate 저장소가 공개가 된다 (GitHub의 `werwer748/harness-plate` 설정)
- [ ] 두 매니페스트의 버전이 0.11.0이 된다 (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)
- [ ] README가 tasks 끝의 PR, CI 워크플로와 그 판정, 푸시 훅을 적고, Claude Code 설치에 공개 저장소에서 받는 길이 생긴다 (`README.md`)
- [ ] ARCHITECTURE의 배포 줄이 공개 저장소를 적고, PRD와 ARCHITECTURE에 옛 동작(GitHub 원격이 있어도 로컬로 합친다, 비공개 저장소)이 남지 않는다 (`docs/PRD.md`, `docs/ARCHITECTURE.md`)
- [ ] ADR-022가 더해진다 (`docs/ADR.md`)

**통과 조건**
- 완료 조건 1, 2가 참이다.
  - 확인: 완료 조건 1, 2의 확인을 모두 돌린다
- 바꾼 뒤에도 기존 테스트가 모두 통과한다.
  - 확인: `python3 -m unittest discover -s tests`가 통과한다
