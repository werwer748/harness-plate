# Phase 7: 이 레포에서 004를 실행한다 (자기 적용)

**목표**: `004-context-rules`가 run 스킬로 실행돼 두 phase가 통과하고 context 스킬에 규칙 둘이 들어 있다.

**읽을 것**
- `docs/tasks/004-context-rules/plan.md` (004의 완료 조건)
- `~/.claude/projects/-Users-gangjungi-Desktop-harness-plate/` (사용자가 연 세션의 기록 `<세션>.jsonl`)
- `~/plate-rail-test/bin/calls.py`, `~/plate-rail-test/bin/runcheck.py` (기록과 커밋을 보는 도구)

**TODO**
- [ ] 사용자가 새 세션에 붙여 넣을 글이 답글의 맨 끝에 코드 블록 하나로 주어진다. 004의 번호를 주어 부르는 글이다(005에도 `phase-N.md`가 남아 있어 번호 없이 부르면 run이 둘 가운데 묻는다)
- [ ] 사용자가 `claude --plugin-dir plugins/plate`로 연 새 세션에서 run을 직접 불러 004의 두 phase가 통과한다. 이 phase를 수행하는 세션은 run을 부르지 않는다
- [ ] 그 세션의 기록과 커밋을 읽은 결과가 사용자에게 보여진다: 커밋의 순서와 메시지, 메인이 직접 고친 파일, 에이전트에게 넘긴 글, 옮길 것이 있었으면 `docs/LESSONS.md`와 지도의 행
- [ ] 기대와 다른 것이 있었으면 스킬이 고쳐지고 걸리는 판정이 다시 통과한다. 본문의 규칙을 바꿔야 하면 고치기 전에 사용자에게 묻는다 (`plugins/plate/skills/`)

**통과 조건**
- 완료 조건 16이 참이다.
  - 확인: 완료 조건 16의 확인 넷을 돌리고 읽어 기대와 같은지 본다
