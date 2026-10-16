# Phase 1: 훅과 단위 테스트

**목표**: 플러그인의 Claude Code 훅이 코드 파일 편집을 완료 조건 1의 경우대로 막거나 통과시키고, `tests/`의 단위 테스트가 그것을 보인다.

**읽을 것**
- `plugins/plate/skills/plan/SKILL.md` (낱말 "테스트가 있는 프로젝트", 0번의 셋업 판단)
- `plugins/plate/skills/run/SKILL.md` (0번 대상 작업을 정하는 규칙, 낱말 "남은 첫 phase"·"끝나지 않은 작업")
- `plugins/plate/skills/phase/SKILL.md` (5번: phase가 끝날 때만 커밋한다)
- `plugins/plate/.claude-plugin/plugin.json`
- `docs/TOOLS.md` (Claude Code 절: `--plugin-dir`, 헤드리스 허용 목록의 `Bash(python3:*)`)

**TODO**
- [ ] 완료 조건 1의 경우마다 상황을 만들고 결과를 단언하는 단위 테스트가 `tests/`에 생기고, 훅이 없는 상태에서 돌린 실패 출력이 기록에 남는다 (`tests/`)
- [ ] 플러그인을 켜면 실리는 PreToolUse 훅이 파일 편집 도구의 호출을 보고 완료 조건 1의 경우대로 막거나 통과시킨다. 막을 때 에이전트가 받는 글에 까닭과 할 일(계획부터 / 실패하는 테스트부터 / 세 번째면 막힘으로 멈추고 까닭과 해결책을 적는다)이 있다 (`plugins/plate/hooks/`)
- [ ] 단위 테스트가 모두 통과한다

**통과 조건**
- 완료 조건 1과 13이 참이다.
  - 확인: 완료 조건 1, 13의 확인을 모두 돌린다
