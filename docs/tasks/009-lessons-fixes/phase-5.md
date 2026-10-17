# Phase 5: 맥락 문서와 버전

**목표**: `docs/TOOLS.md`와 `docs/ADR.md`가 바뀐 훅과 6단계를 반영하고, 두 매니페스트의 버전이 0.9.1이다.

**테스트 먼저**: 아니오 — 문서와 매니페스트의 버전만 고친다

**읽을 것**
- `docs/TOOLS.md` (머리글, "지금 상태" 표, Claude Code 절의 훅 묶음)
- `docs/ADR.md` (ADR-018의 이유, ADR-019의 트레이드오프)
- `plugins/plate/hooks/hooks.json` (phase 1이 바꾼 명령)
- `plugins/plate/skills/context/SKILL.md`의 답을 적는 규칙 (문장 중간에 있는 칸)
- code.claude.com/docs/en/hooks (종료 코드: 2만 막고 다른 0이 아닌 코드는 막지 않는다. 명령은 `sh -c`로 돈다)
- `plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`
- `git show ec2f192:docs/LESSONS.md`의 하네스의 문제점 절에서 (008-tdd, phase 4)의 첫째 줄, (008-tdd, phase 5)의 셋째 줄과, 프로젝트에서 배운 것 절의 (004-context-rules, 검증 1) 둘째 줄 (고칠 문제의 원문)

**TODO**
- [ ] TOOLS.md의 머리글과 "지금 상태" 표의 Claude Code 행이 6단계(TDD와 엣지케이스)까지 적는다 (`docs/TOOLS.md`)
- [ ] TOOLS.md의 훅 묶음에 종료 코드와 명령 실행의 사실이 출처 문서와 확인한 날짜와 함께 있다: 2만 막고 1이나 127 같은 다른 0이 아닌 코드는 막지 않는다, `python3`는 스크립트 파일을 열지 못하면 2로 끝난다, 명령은 `sh -c`로 돈다 (`docs/TOOLS.md`)
- [ ] ADR-019의 트레이드오프가 `python3`가 없거나 스크립트 파일이 없을 때 훅이 돌지 않고 규칙 구간만 남는다고 적는다 (`docs/ADR.md`)
- [ ] ADR-018의 이유 끝 "멈춘 이유는 없음"이 "멈춘 이유는 없다."다 (`docs/ADR.md`)
- [ ] 두 매니페스트의 버전이 0.9.1이다 (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)

**통과 조건**
- 완료 조건 8이 참이다.
  - 확인: 완료 조건 8의 확인을 모두 돌린다
- 완료 조건 14가 참이다.
  - 확인: 완료 조건 14의 확인을 돌린다
