# Phase 1: eval 본문에 세 기준을 넣는다

**목표**: eval이 하네스 고칠 거리마다 세 기준을 감수와 문턱보다 먼저 대어 "eval에만"을 가르고 그렇게 적는다.

**테스트 먼저**: 아니오 — 바뀌는 동작이 결과물인 마크다운(스킬 본문)의 것이다

**읽을 것**
- `plugins/plate/skills/eval/SKILL.md` (앞머리 description, "1. 읽는다", "5. 하네스 고칠 거리를 정한다", "기록의 양식"의 하네스 고칠 거리, "적는 규칙"의 이슈 제목과 이슈 본문 줄. "기록만으로 평가한다"는 다른 뜻으로 이미 쓰인다)
- `tests/test_skill_rules.py` (`EvalRulesTest.test_threshold_and_disposition`, `DescriptionTest.test_description_at_most_1024_chars`)
- `docs/ADR.md` (ADR-025)

**TODO**
- [ ] 5절에 고칠 거리마다 task 머리 결정의 세 기준을 대어 보는 항목이 처리를 정하는 항목 앞에 더해진다. 하나라도 넘지 않으면 기준은 "eval에만"이고, 일반성은 plate 자체의 것에만 대며, "eval에만"인 것에는 처리, 문턱, 이슈 제목과 본문을 적지 않고, 다시 나서 기준을 넘으면 그때 고칠 거리가 된다는 것이 함께 적힌다 (`plugins/plate/skills/eval/SKILL.md`)
- [ ] 5절의 처리, 문턱, 이슈 제목과 본문 항목이 기준을 넘은 것에만 걸리게 바뀐다 (`plugins/plate/skills/eval/SKILL.md`)
- [ ] "기록의 양식"의 하네스 고칠 거리 두 갈래 항목에 처리 줄 앞에 `- 기준: {넘음 | eval에만} — {넘지 않은 기준과 까닭}` 꼴의 줄이 더해진다 (`plugins/plate/skills/eval/SKILL.md`)
- [ ] "적는 규칙"에 "eval에만"인 항목은 기준 줄만 두고 처리, 문턱, 이슈 제목, 이슈 본문, 고칠 곳, 해결책 줄을 빼고 적는다는 규칙이 더해지고, 이슈 제목과 이슈 본문 줄의 규칙이 기준을 넘은 것에만 걸리게 바뀐다 (`plugins/plate/skills/eval/SKILL.md`)
- [ ] description에 세 기준과 "eval에만"이 더해지고 1024자를 넘지 않는다 (`plugins/plate/skills/eval/SKILL.md`)
- [ ] `EvalRulesTest`에 `test_eval_only_criteria`가 더해진다. 5절에 세 기준과 "eval에만"이 있고 그 항목이 처리 항목보다 앞서며, 양식에 기준 줄이, 적는 규칙에 "eval에만"의 규칙이, description에 "eval에만"이 있는지 본다. 바뀐 글에 맞춰 `test_threshold_and_disposition`도 고친다 (`tests/test_skill_rules.py`)

**통과 조건**
- eval 본문이 완료 조건 1을 이룬다.
  - 확인: `grep -n -e 'eval에만' plugins/plate/skills/eval/SKILL.md`가 description, 5절, 양식, 적는 규칙의 줄을 낸다
  - 확인: `grep -n -e '- 기준:' plugins/plate/skills/eval/SKILL.md`가 양식의 두 갈래 항목에서 한 줄씩 낸다
  - 확인: `(cd tests && python3 -m unittest test_skill_rules.EvalRulesTest.test_eval_only_criteria)`가 OK다
- 테스트가 모두 통과한다.
  - 확인: `python3 -m unittest discover -s tests`가 OK다
