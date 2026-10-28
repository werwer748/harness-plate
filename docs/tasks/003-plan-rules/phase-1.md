# Phase 1: 진행 중인 tasks에 더하는 경우를 바로잡는다

**목표**: 평가가 시작된 tasks에는 더하지 않고, 더하는 경우에는 앞 task 머리를 읽어 바뀐 뒤의 글을 인용할 수 있다.

**테스트 먼저**: 아니오 — 스킬 본문(`.md`)과 그 글을 지키는 테스트, 맥락 문서만 바꾼다

**읽을 것**
- `plugins/plate/skills/plan/SKILL.md` (`## 1. 진행 중인 tasks가 있는지 본다`, `## 6. 초안을 보여 주고 승인받는다`의 task 사이 맞물림 점검, `## 적는 규칙`의 **결정**)
- `plugins/plate/skills/run/SKILL.md` (`## tasks 끝`의 표: `review.md`·`eval.md`가 있으면 평가를 건너뛴다)
- `docs/cleanup/2026-10-28.md` (신뢰성-4, 신뢰성-5와 그 2라운드)
- `tests/test_skill_rules.py` (`PlanRulesTest`)
- `docs/ARCHITECTURE.md` (`## 데이터 흐름`의 계획 단계 줄)

**TODO**
- [ ] 1번에, `docs/tasks/review.md`나 `docs/tasks/eval.md`가 있으면 tasks 끝의 평가가 이미 시작됐다고 알리고, 더할지 묻지 않고 아무것도 쓰지 않고 끝난다는 갈래가 더해진다 (`plugins/plate/skills/plan/SKILL.md`)
- [ ] 1번 더하는 경우의 "이미 있는 task 폴더는 이름만 보고 내용은 읽지 않는다"가 바뀐다. 새 글은 이미 있는 task 폴더마다 task 머리를 읽고 phase 파일은 읽지 않으며, 앞 task가 바꿀 글은 그 task 머리에서 찾는다는 뜻이다 (`plugins/plate/skills/plan/SKILL.md`)
- [ ] `PlanRulesTest`에 완료 조건 1의 두 단언이 더해진다 (`tests/test_skill_rules.py`)
- [ ] ARCHITECTURE `## 데이터 흐름` 계획 단계 줄에 평가가 시작된 tasks면 더하지 않는다는 갈래가 더해진다. `## 디렉터리 구조`의 `test_skill_rules.py` 줄에 새 테스트가 다루는 규칙이 더해진다 (`docs/ARCHITECTURE.md`)

**통과 조건**
- 더하는 경우가 완료 조건 1대로다. (완료 조건 1)
  - 확인: `python3 -m unittest discover -s tests`가 `OK`로 끝나고, 완료 조건 1의 두 단언을 하는 테스트와 `test_57_quote_earlier_task_text_as_changed`가 그 안에 있다
  - 확인: ARCHITECTURE `## 데이터 흐름`의 계획 단계 줄을 읽는다. 더할지 묻는 갈래와 평가가 시작된 tasks면 더하지 않는 갈래가 둘 다 있다
- 앞 task가 이룬 tasks 완료 조건 3이 그대로다. (완료 조건 4)
  - 확인: `git grep -n 'TOOLS.md' -- plugins/`가 아무것도 내지 않는다
