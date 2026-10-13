# Phase 6: 이 레포의 문서를 4단계 상태로 고친다

**목표**: README, 두 매니페스트, PRD, ARCHITECTURE, TOOLS가 스킬 여섯과 `phase-N.md`로 나뉜 계획을 말한다.

**읽을 것**
- `README.md`, `plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`
- `docs/PRD.md` (핵심 기능의 3~5번과 그 아래 문장)
- `docs/ARCHITECTURE.md` (디렉터리 구조, "패턴과 규칙"의 마지막 줄, 데이터 흐름과 그 아래 두 문장)
- `docs/TOOLS.md` (첫머리, "지금 상태")
- `plugins/plate/skills/run/SKILL.md`, `phase/SKILL.md`, `retro/SKILL.md`, `plan/SKILL.md`의 설명 (표에 옮길 한 줄)

**TODO**
- [ ] 스킬 표에 run, phase, retro가 있고 plan의 줄이 `plan.md`와 `phase-N.md`를 말하며, 부르는 법에 세 스킬이 있다 (`README.md`)
- [ ] 두 매니페스트의 설명에 세 스킬이 있다
- [ ] 핵심 기능의 계획 줄이 `plan.md`와 `phase-N.md`를 말하고 실행 줄이 4단계에서 만들었다고 말한다 (`docs/PRD.md`)
- [ ] 디렉터리 구조에 세 스킬이 있고, 프로젝트의 규칙 줄이 네 스킬의 본문에 넣었다고 말하고, 데이터 흐름과 그 아래 문장이 phase 파일을 지우는 것과 `docs/LESSONS.md`를 말한다 (`docs/ARCHITECTURE.md`)
- [ ] 첫머리와 "지금 상태"에 4단계가 있다 (`docs/TOOLS.md`)

**통과 조건**
- 완료 조건 19가 참이다.
  - 확인: 완료 조건 19의 확인 둘을 돌리고 읽어 기대와 같은지 본다
- 문서에 한 파일 시절의 글이 없다.
  - 확인: `grep -n 'phase 절' README.md docs/PRD.md docs/ARCHITECTURE.md` → 출력 없음
