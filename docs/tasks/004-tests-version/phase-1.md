# Phase 1: 테스트를 더하고 버전과 문서를 맞춘다

**목표**: 두 테스트 파일이 더해지고 BACKLOG 항목이 지워지며, 버전이 0.17.0이 되고 맥락 문서와 README가 맞춰진다.

**테스트 먼저**: 아니오 — 새 테스트 파일을 더할 뿐 기존 코드 파일의 동작을 바꾸지 않는다. 새 테스트가 깨질 때 실패하는지는 통과 조건이 복사본에서 본다

**읽을 것**
- `tests/test_cleanup_skill.py` (스킬 본문의 글을 시험하는 선례)
- `plugins/plate/skills/run/SKILL.md`, `plugins/plate/skills/plan/SKILL.md`, `plugins/plate/skills/phase/SKILL.md`, `plugins/plate/skills/eval/SKILL.md` (앞 task들이 고친 규칙)
- `plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json` (두 매니페스트)
- `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `docs/BACKLOG.md`, `README.md` (맥락 문서와 README)

**TODO**
- [ ] `tests/test_manifests.py`가 더해진다. 두 매니페스트의 `"version"`이 서로 같은지 본다 (`tests/test_manifests.py`)
- [ ] `tests/test_skill_rules.py`가 더해진다. run의 #34·#35·#38·#40·#44, plan의 #37·#41, phase의 #42, eval의 #36이 고친 규칙의 글이 저마다 그 본문의 그 절에 있는지 본다 (`tests/test_skill_rules.py`)
- [ ] `docs/BACKLOG.md`의 항목이 지워지고 `# BACKLOG` 줄만 남는다 (`docs/BACKLOG.md`)
- [ ] 두 매니페스트의 버전이 0.17.0으로 바뀐다 (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)
- [ ] `docs/ARCHITECTURE.md`의 "디렉터리 구조"의 `tests/` 아래에 두 테스트 파일이 저마다 한 줄로 더해지고, 다섯 문서 가운데 이 tasks가 바꾼 동작과 어긋나는 줄이 그 동작을 담게 바뀐다 (`docs/ARCHITECTURE.md`, `docs/PRD.md`, `docs/ADR.md`, `docs/TOOLS.md`, `README.md`)

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건 1~4의 확인을 모두 돌린다
