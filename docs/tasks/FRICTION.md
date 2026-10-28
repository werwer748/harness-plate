# FRICTION

- `001-plan-rules` 문제: plan 본문 적는 규칙 "조건"의 기존 248줄(본문 해시를 `git rev-parse HEAD:<경로>`로 견준다)과 이번에 더한 249줄(`HEAD`를 보는 확인은 작업 트리로 적는다)·6번 102줄(확인에 `HEAD`가 있으면 작업 트리로 고친다)이 부딪힌다. 계획(tasks 머리·task 머리)이 #55의 새 규칙과 본문의 기존 `HEAD` 규칙이 맞물리는지를 점검할 곳으로 적지 않았고, 완료 조건은 새 글이 있는지만 봐 이 어긋남을 phase 확인이 잡지 못했다
- `001-plan-rules` 문제: `docs/tasks/RUNLOG.md`에 `001-plan-rules` phase 1의 수행 줄이 둘이고(첫 줄은 토큰·도구 호출·시간이 모두 "모름") 그 사이에 확인 줄이 없다. `done-phase-1.md`에는 수행 기록과 확인 절이 하나씩만 있어, 첫 수행 에이전트가 무엇을 했는지 기록에서 알 수 없다
- `001-plan-rules` 문제: 회고 1의 문제를 고치려고 더한 phase 2(`docs/tasks/001-plan-rules/done-phase-2.md`)의 읽을 것과 TODO가 고칠 글(plan 본문 적는 규칙 "조건" 248줄)만 적고, 그 글을 그대로 찾는 `tests/test_skill_rules.py`의 `test_46_rerun_results_compared_by_body_hash`를 적지 않았다. 수행이 "계획과 달라진 점"으로 그 테스트도 고쳤다. 본문 글을 고치는 고칠 phase에는 그 글을 지키는 테스트를 읽을 것과 TODO에 함께 적어야 수행이 계획 밖에서 고치지 않는다
- `001-plan-rules` 스킬 후보: 글을 지워 테스트 실패를 보는 확인(`mktemp -d` 사본에 `cp -R plugins tests`, 글의 수를 센 뒤 빈 글로 바꾸고 사본에서 `python3 -m unittest discover -s tests`, `FAIL:` 줄을 찾음)을 phase 1·2의 수행과 확인, 회고 1·2에서 글 셋마다 손으로 되풀이했다. 글과 기대 테스트 이름을 받아 돌리는 스크립트로 만들면 확인마다의 명령 묶음이 줄어든다(이번 tasks 머리는 범위 밖으로 둠)
