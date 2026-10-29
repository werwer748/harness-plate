# Phase 1: eval 본문에 세 기준을 넣는다

**목표**: eval이 하네스 고칠 거리마다 세 기준을 감수와 문턱보다 먼저 대어 "eval에만"을 가르고 그렇게 적는다.

**테스트 먼저**: 아니오 — 바뀌는 동작이 결과물인 마크다운(스킬 본문)의 것이다

**읽을 것**
- `plugins/plate/skills/eval/SKILL.md` (앞머리 description, "1. 읽는다", "5. 하네스 고칠 거리를 정한다", "기록의 양식"의 하네스 고칠 거리, "적는 규칙"의 이슈 제목과 이슈 본문 줄. "기록만으로 평가한다"는 다른 뜻으로 이미 쓰인다)
- `tests/test_skill_rules.py` (`EvalRulesTest.test_threshold_and_disposition`, `DescriptionTest.test_description_at_most_1024_chars`)
- `docs/ADR.md` (ADR-025)

**TODO**
- [x] 5절에 고칠 거리마다 task 머리 결정의 세 기준을 대어 보는 항목이 처리를 정하는 항목 앞에 더해진다. 하나라도 넘지 않으면 기준은 "eval에만"이고, 일반성은 plate 자체의 것에만 대며, "eval에만"인 것에는 처리, 문턱, 이슈 제목과 본문을 적지 않고, 다시 나서 기준을 넘으면 그때 고칠 거리가 된다는 것이 함께 적힌다 (`plugins/plate/skills/eval/SKILL.md`)
- [x] 5절의 처리, 문턱, 이슈 제목과 본문 항목이 기준을 넘은 것에만 걸리게 바뀐다 (`plugins/plate/skills/eval/SKILL.md`)
- [x] "기록의 양식"의 하네스 고칠 거리 두 갈래 항목에 처리 줄 앞에 `- 기준: {넘음 | eval에만} — {넘지 않은 기준과 까닭}` 꼴의 줄이 더해진다 (`plugins/plate/skills/eval/SKILL.md`)
- [x] "적는 규칙"에 "eval에만"인 항목은 기준 줄만 두고 처리, 문턱, 이슈 제목, 이슈 본문, 고칠 곳, 해결책 줄을 빼고 적는다는 규칙이 더해지고, 이슈 제목과 이슈 본문 줄의 규칙이 기준을 넘은 것에만 걸리게 바뀐다 (`plugins/plate/skills/eval/SKILL.md`)
- [x] description에 세 기준과 "eval에만"이 더해지고 1024자를 넘지 않는다 (`plugins/plate/skills/eval/SKILL.md`)
- [x] `EvalRulesTest`에 `test_eval_only_criteria`가 더해진다. 5절에 세 기준과 "eval에만"이 있고 그 항목이 처리 항목보다 앞서며, 양식에 기준 줄이, 적는 규칙에 "eval에만"의 규칙이, description에 "eval에만"이 있는지 본다. 바뀐 글에 맞춰 `test_threshold_and_disposition`도 고친다 (`tests/test_skill_rules.py`)

**통과 조건**
- eval 본문이 완료 조건 1을 이룬다.
  - 확인: `grep -n -e 'eval에만' plugins/plate/skills/eval/SKILL.md`가 description, 5절, 양식, 적는 규칙의 줄을 낸다
  - 확인: `grep -n -e '- 기준:' plugins/plate/skills/eval/SKILL.md`가 양식의 두 갈래 항목에서 한 줄씩 낸다
  - 확인: `(cd tests && python3 -m unittest test_skill_rules.EvalRulesTest.test_eval_only_criteria)`가 OK다
- 테스트가 모두 통과한다.
  - 확인: `python3 -m unittest discover -s tests`가 OK다

## 한 일
- 5절에 세 기준을 대어 보는 항목: "항목마다 plate 자체의 것인지 …" 다음, 처리 항목 앞에 세 기준(피해, 일반성, 고침의 꼴)을 하위 항목으로 둔 항목과 "eval에만"인 항목의 처리(`eval.md`에만 남고 처리·문턱·이슈를 정하지 않으며 고침 task, 이슈, BACKLOG, 감수 어디에도 두지 않고, 다시 나서 기준을 넘으면 그때 고칠 거리)를 더했다. 일반성은 plate 자체의 것에만 대고 이 프로젝트만의 것은 넘은 것으로 본다고 적었다 (`plugins/plate/skills/eval/SKILL.md`)
- 5절의 처리, 문턱, 이슈 제목과 본문 항목: "기준을 넘은 항목마다 처리를…", "기준을 넘은 plate 자체의 것은 문턱을…", "이슈 제목과 본문은 기준과 문턱을 넘었고…", "기준을 넘은 이 프로젝트만의 것에는 고칠 파일과…"로 바꿨다 (`plugins/plate/skills/eval/SKILL.md`)
- 양식의 두 갈래 항목: 처리 줄 앞에 `- 기준: {넘음 | eval에만} — {…}` 줄을 하나씩 더했다. 이 프로젝트만의 갈래는 넘은 근거를 "두 기준(피해, 고침의 꼴)"으로 적었다 (`plugins/plate/skills/eval/SKILL.md`)
- 적는 규칙: "기준이 "eval에만"인 항목은 기준 줄만 두고 처리, 문턱, 이슈 제목, 이슈 본문, 고칠 곳, 해결책 줄을 빼고 적는다"를 더하고, 이슈 줄의 규칙을 "기준과 문턱이 넘음이고"로 바꿨다 (`plugins/plate/skills/eval/SKILL.md`)
- description: 하네스 고칠 거리의 괄호에 세 기준과 "eval에만"을 더했다. 길이 618자 (`plugins/plate/skills/eval/SKILL.md`)
- `test_eval_only_criteria`를 더하고(5절의 세 기준·"eval에만"·처리 항목보다 앞섬, 양식의 기준 줄 두 개와 두 갈래 위치, 적는 규칙, description), `test_threshold_and_disposition`의 이슈 줄 글을 바뀐 글로 고치고 문턱 항목의 새 글을 더했다 (`tests/test_skill_rules.py`)

## 확인 결과
- eval 본문이 완료 조건 1을 이룬다.
  - `grep -n -e 'eval에만' plugins/plate/skills/eval/SKILL.md` → 3(description), 179·183(5절), 256·262(양식), 280(적는 규칙). 통과
  - `grep -n -e '- 기준:' plugins/plate/skills/eval/SKILL.md` → 256(plate 자체 갈래), 262(이 프로젝트만 갈래) 한 줄씩. 통과
  - `(cd tests && python3 -m unittest test_skill_rules.EvalRulesTest.test_eval_only_criteria)` → `Ran 1 test` `OK`. 통과
- 테스트가 모두 통과한다.
  - `python3 -m unittest discover -s tests` → `Ran 204 tests in 19.817s` `OK`. 통과

## 계획과 달라진 점
없음

## 남은 것
- 8절의 돌려주는 줄 "고칠 거리: plate 자체 N개, 이 프로젝트만 M개"는 "eval에만"인 항목을 세는지 빼는지 정하지 않았다. 이 phase의 TODO 밖이라 그대로 두었다
- 낱말 절에 "eval에만"의 정의를 따로 두지 않았다. 뜻은 5절에만 있다

## 하네스에서 걸린 것
없음
