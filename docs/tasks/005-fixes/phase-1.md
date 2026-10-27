# Phase 1: tasks 끝의 문제를 고친다

**목표**: task 머리의 완료 조건에 적힌 것을 모두 고친다.

**테스트 먼저**: 예 — 완료 조건 4의 description 길이 테스트를 먼저 써서 run의 1142자에서 실패하는 것을 본 뒤 1을 고친다

**읽을 것**
- `docs/tasks/review.md`의 `## 평가 1` 절
- `docs/tasks/eval.md`의 `## eval 1` 절
- `plugins/plate/skills/run/SKILL.md`
- `tests/test_skill_rules.py`
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/ADR.md`
- `docs/TOOLS.md`
- `docs/BACKLOG.md`
- `README.md`

**TODO**
- [ ] 스킬 description 길이를 보는 테스트가 없다. 모든 `plugins/plate/skills/*/SKILL.md`의 description이 1024자 이하인지 보는 테스트를 더한다 (`tests/test_skill_rules.py`)
- [ ] run의 description이 1142자로 1024자 한도를 넘어 Codex가 끝의 부르는 말과 "계획이 없는 요청에는 쓰지 않는다"를 자른다. 1024자 이하로 줄이되 그 둘은 남긴다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] `docs/TOOLS.md`를 `RUNLOG.md`와 함께 커밋한다는 괄호 글이 일곱 커밋 자리에 되풀이된다. 규칙을 "`RUNLOG.md`" 절 한 곳에 두고 커밋 자리는 그 절을 따르게 한다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] 헤드리스 장면의 차림 사실을 더한다: 허용 목록의 아홉 명령, 프롬프트는 `-p` 바로 뒤, 복제한 뒤 `git remote set-head origin main`, 세션 기록은 `${CLAUDE_CONFIG_DIR:-~/.claude}/projects/` 아래 (`docs/TOOLS.md`)
- [ ] 고친 run 본문으로 장면 A~D를 다시 돌려, 장면마다 버전, 시각, 세션 id, 돌릴 때의 run 본문 해시, 기대, 본 결과를 run 장면 절에 더한다 (`docs/TOOLS.md`)
- [ ] 고친 코드에서 같은 뿌리의 꼴(같은 함수의 다른 입력, 앞서 막던 꼴)을 찾아 테스트로 남긴다 (`tests/test_skill_rules.py`)

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다
