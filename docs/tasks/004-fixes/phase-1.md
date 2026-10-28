# Phase 1: tasks 끝의 문제를 고친다

**목표**: task 머리의 완료 조건에 적힌 것을 모두 고친다.

**테스트 먼저**: 아니오 — 고칠 것이 회귀 테스트를 더하는 것과 TOOLS.md 한 줄이고, 스킬 본문의 동작은 바꾸지 않아 먼저 실패할 테스트가 없다

**읽을 것**
- `docs/tasks/review.md`의 `## 평가 1` 절
- `docs/tasks/eval.md`의 `## eval 1` 절
- `plugins/plate/skills/run/SKILL.md`의 낱말 "글을 넘기는 법"과 3번 "상태를 읽는 법"
- `tests/test_skill_rules.py`
- `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `docs/BACKLOG.md`, `docs/cleanup/2026-10-28.md`

**TODO**
- [ ] run 3번 "상태를 읽는 법"의 `awk` 명령을 본문에서 뽑아 시험 파일(코드 블록 속 판정 줄, TODO 속 `## 확인 1`, 판정 줄 없는 마지막 절)에 돌리는 테스트와, 낱말 "글을 넘기는 법"대로 따옴표·백틱·`$(…)`가 든 제목을 가짜 `gh`에 넘겨 한 인자로 그대로 닿고 치환이 돌지 않음을 보는 테스트를 더한다. `docs/ARCHITECTURE.md`에 테스트 설명이 있으면 그 줄도 맞춘다 (`tests/test_skill_rules.py`, `docs/ARCHITECTURE.md`)
- [ ] `docs/TOOLS.md`의 `## Claude Code` 첫 목록에 "한글 본문을 `python3 -` heredoc으로 고치면 `SyntaxError: Non-UTF-8 code`로 깨질 수 있다. Edit 도구나 `python3 -c`, 파일로 쓴 스크립트를 쓴다"를 확인한 버전과 함께 한 줄로 더한다 (`docs/TOOLS.md`)

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다
