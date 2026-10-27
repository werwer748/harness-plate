# Phase 1: plan 본문과 테스트와 문서를 고친다

**목표**: plan 본문의 세 이슈가 고쳐지고, 그 규칙 글의 테스트가 더해지고, `test_skill_rules.py` 줄이 맞춰진다.

**테스트 먼저**: 아니오 — 고치는 것은 스킬 본문(`.md`)이고, 더하는 테스트는 그 글이 있는지를 볼 뿐 코드의 동작을 바꾸지 않는다

**읽을 것**
- `plugins/plate/skills/plan/SKILL.md`의 "6. 초안을 보여 주고 승인받는다", 적는 규칙의 "조건"과 "phase의 파일" (고칠 자리)
- `gh issue view 46`, `gh issue view 52`, `gh issue view 53` (이슈마다의 원인과 해결책. #46은 plan의 "조건" 쪽만 이 task의 일이고, run 8번 쪽은 001이 고쳤다)
- `tests/test_skill_rules.py` (001이 더한 run 테스트(#46, #47, #48, #51)와 `section` 도우미의 꼴. 001은 이 파일의 모듈 docstring과 run 테스트들을 고쳤다)
- `docs/ARCHITECTURE.md` 디렉터리 구조의 `test_skill_rules.py` 줄 (001이 run 규칙을 더한 줄. 이 task가 plan 규칙을 더한다), `docs/PRD.md`의 3, `README.md`의 스킬 표의 `plan` 행

**TODO**
- [ ] 적는 규칙 "조건"의 남은 결과를 읽는 확인 항목에, 돌려 본 결과가 지금 본문의 것인지는 커밋 시각이 아니라 돌릴 때 적은 본문 해시(`git hash-object`)와 `git rev-parse HEAD:<경로>`로 견준다는 글이 더해진다 (`plugins/plate/skills/plan/SKILL.md`)
- [ ] 적는 규칙 "phase의 파일"의 읽을 것 항목에, 앞 task의 변경에 기대면 이슈 번호만으로 가리키지 않고 그 파일의 절 이름과 바뀐 글을 찾을 수 있게 적는다는 글이 더해진다 (`plugins/plate/skills/plan/SKILL.md`)
- [ ] 6번의 점검 목록에, 돌려 보는 확인마다 차림이 앞 단계를 지나 기대한 자리에 닿는지, 기대가 해결 방식이 아니라 관찰할 결과로 적혔는지, 결정과 TODO가 같은 멈출 자리를 말하는지 보고, 아니면 고친다는 항목이 더해진다 (`plugins/plate/skills/plan/SKILL.md`)
- [ ] 위 셋의 규칙 글이 제 절에 있는지 보는 테스트가 이슈마다 더해지고, 모듈 docstring의 이슈 목록에 plan의 #46, #52, #53이 더해진다 (`tests/test_skill_rules.py`)
- [ ] 디렉터리 구조의 `test_skill_rules.py` 줄에 이번 plan 규칙(돌려 본 결과의 해시 견줌, 앞 task 변경의 읽을 것, 장면 확인의 초안 점검)이 더해지고, 001이 더한 run 규칙은 그대로 남는다 (`docs/ARCHITECTURE.md`)

**통과 조건**
- 완료 조건 1이 참이다
  - 확인: `plugins/plate/skills/plan/SKILL.md`의 "조건", "phase의 파일", "6. 초안을 보여 주고 승인받는다"를 읽어 #46, #52, #53의 해결이 task 머리 완료 조건 1의 글대로 저마다 적혀 있다. 하나라도 없으면 실패
- 완료 조건 2가 참이다
  - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
  - 확인: `mktemp -d`에 `git archive HEAD`를 풀어 plan 본문 6번에서 #53의 점검 글을 지우고 돌리면 실패한다. 다시 풀어 "조건"에서 #46의 해시 글을 지우고 돌리면 실패한다
- 완료 조건 3이 참이다
  - 확인: `docs/ARCHITECTURE.md` 디렉터리 구조의 `test_skill_rules.py` 줄이 001의 run 규칙과 이 task의 plan 규칙을 모두 담고, `docs/PRD.md`의 3과 `README.md`의 `plan` 행에 1의 세 규칙과 어긋나는 줄이 없다. 하나라도 어긋나면 실패
