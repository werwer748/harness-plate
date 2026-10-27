# Phase 1: tasks 끝의 문제를 고친다

**목표**: task 머리의 완료 조건에 적힌 것을 모두 고친다.

**테스트 먼저**: 아니오 — 고칠 문제가 `plugins/plate/skills/check/SKILL.md`, `plugins/plate/skills/review/SKILL.md`(`.md`)의 글뿐이라 코드 파일의 동작을 바꾸지 않는다

**읽을 것**
- `docs/tasks/review.md`의 `## 평가 1` 절
- `docs/tasks/eval.md`의 `## eval 1` 절
- `plugins/plate/skills/check/SKILL.md`
- `plugins/plate/skills/review/SKILL.md`
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/ADR.md`
- `docs/TOOLS.md`

**TODO**
- [ ] check 5번이 계획의 `- 돌리지 않음: {까닭}` 줄로 돌리지 않기로 정한 동작에 대한 "돌려 보지 않은 위험" 줄까지 실패로 해, 수행이 고칠 길 없는 실패와 세 번 실패의 멈춤으로 이어질 수 있다 (`plugins/plate/skills/check/SKILL.md`)
- [ ] 결과물인 마크다운만 바뀐 경우의 테스트 적절성 표가 실행 경로 없는 파일(매니페스트 버전 줄)이 함께 바뀌면 쓰이지 않는다 (`plugins/plate/skills/review/SKILL.md`)
- [ ] "기능 적합성은 돌린 확인으로 매긴다" 줄이 새 표 뒤에 붙어 일반 등급표의 줄인지 새 표의 줄인지 흐려진다 (`plugins/plate/skills/review/SKILL.md`)

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다
