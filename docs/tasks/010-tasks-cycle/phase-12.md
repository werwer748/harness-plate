# Phase 12: 맥락 문서, README, AGENTS.md, ADR, 매니페스트를 새 흐름에 맞춘다

**목표**: 맥락 문서, README, 이 레포의 `AGENTS.md`, 두 매니페스트가 새 흐름과 0.10.0을 말한다.

**테스트 먼저**: 아니오 — `.md`와 매니페스트의 버전·설명만 고친다.

**읽을 것**
- `docs/PRD.md` (목표 문단의 규칙 구간 설명, 핵심 기능 5, 7, 8)
- `docs/ARCHITECTURE.md` (디렉터리 구조, 패턴과 규칙의 run 브랜치 규칙과 막는 장치, 데이터 흐름)
- `docs/ADR.md` (항목의 꼴. 마지막은 ADR-019)
- `README.md` (스킬 표와 두 도구에서 부르는 이름)
- `AGENTS.md` (이 레포의 문서 지도와 규칙 구간)
- `plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json` (버전 0.9.1과 설명)
- `plugins/plate/skills/setup/SKILL.md` (phase 2가 바꾼 두 구간의 글)
- `plugins/plate/skills/run/SKILL.md` (새 흐름 전체)

**TODO**
- [ ] `docs/PRD.md`의 목표 문단과 핵심 기능 5, 7, 8이 새 흐름을 말한다: 5는 task 회고, 7은 두 실행 방식(이 단계에서 만들었다), 8은 tasks 끝의 코드 평가와 하네스 eval(이 단계에서 만들었다)과 011의 PR·CI
- [ ] `docs/ARCHITECTURE.md`의 디렉터리 구조가 아홉 스킬을, 패턴과 규칙이 `tasks/<이름>` 브랜치와 새 규칙 구간을, 데이터 흐름이 새 흐름을 말하고, 명령 절이 생긴다(테스트 `python3 -m unittest discover -s tests`, 빌드와 린트는 "없음"). "verify", "LESSONS", "worktree"가 남지 않는다
- [ ] `README.md`의 스킬 표와 두 도구에서 부르는 이름이 아홉 스킬이다
- [ ] 이 레포 `AGENTS.md`의 `docs/tasks/` 행과 규칙 구간이 setup 본문의 글과 같아진다
- [ ] `docs/ADR.md`에 ADR-020이 더해진다: GitHub 이슈(`werwer748/harness-plate`, `gh`)를 plate 자체의 고칠 거리를 모으는 외부 서비스로 쓴다. 결정, 이유, 트레이드오프를 적고 계획이나 task 폴더는 적지 않는다
- [ ] 두 매니페스트의 버전이 0.10.0이 되고 설명이 아홉 스킬을 말한다

**통과 조건**
- 완료 조건 2, 10, 11, 12가 참이다
  - 확인: 네 완료 조건의 확인을 모두 돌린다
- 완료 조건 15가 참이다
  - 확인: `python3 -m unittest discover -s tests` → 마지막 줄 `OK`
