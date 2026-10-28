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
- [x] 1번에, `docs/tasks/review.md`나 `docs/tasks/eval.md`가 있으면 tasks 끝의 평가가 이미 시작됐다고 알리고, 더할지 묻지 않고 아무것도 쓰지 않고 끝난다는 갈래가 더해진다 (`plugins/plate/skills/plan/SKILL.md`)
- [x] 1번 더하는 경우의 "이미 있는 task 폴더는 이름만 보고 내용은 읽지 않는다"가 바뀐다. 새 글은 이미 있는 task 폴더마다 task 머리를 읽고 phase 파일은 읽지 않으며, 앞 task가 바꿀 글은 그 task 머리에서 찾는다는 뜻이다 (`plugins/plate/skills/plan/SKILL.md`)
- [x] `PlanRulesTest`에 완료 조건 1의 두 단언이 더해진다 (`tests/test_skill_rules.py`)
- [x] ARCHITECTURE `## 데이터 흐름` 계획 단계 줄에 평가가 시작된 tasks면 더하지 않는다는 갈래가 더해진다. `## 디렉터리 구조`의 `test_skill_rules.py` 줄에 새 테스트가 다루는 규칙이 더해진다 (`docs/ARCHITECTURE.md`)

**통과 조건**
- 더하는 경우가 완료 조건 1대로다. (완료 조건 1)
  - 확인: `python3 -m unittest discover -s tests`가 `OK`로 끝나고, 완료 조건 1의 두 단언을 하는 테스트와 `test_57_quote_earlier_task_text_as_changed`가 그 안에 있다
  - 확인: ARCHITECTURE `## 데이터 흐름`의 계획 단계 줄을 읽는다. 더할지 묻는 갈래와 평가가 시작된 tasks면 더하지 않는 갈래가 둘 다 있다
- 앞 task가 이룬 tasks 완료 조건 3이 그대로다. (완료 조건 4)
  - 확인: `git grep -n 'TOOLS.md' -- plugins/`가 아무것도 내지 않는다

## 한 일
- 1번에 `review.md`·`eval.md`가 있으면 끝나는 갈래: `## 1. 진행 중인 tasks가 있는지 본다`에 "`docs/tasks/review.md`나 `docs/tasks/eval.md`가 있으면 그 tasks는 끝의 평가가 이미 시작된 것이다. … task로 더할지 묻지 않고 아무것도 쓰지 않고 끝난다." 문단과 그 까닭(실행이 이미 있는 평가를 보고 새 task의 평가를 건너뜀)을 더하고, 더할지 묻는 글은 "둘 다 없으면" 문단으로 옮겼다 (`plugins/plate/skills/plan/SKILL.md`)
- 더하는 경우에 앞 task 머리를 읽음: "이미 있는 task 폴더는 이름만 보고 내용은 읽지 않는다"를 "이미 있는 task 폴더마다 task 머리(`plan.md`)를 읽고, phase 파일(`phase-N.md`, `done-phase-N.md`)은 읽지 않는다. 앞 task가 바꿀 글(**결정**과 6번의 task 사이 맞물림 점검이 바뀐 뒤의 꼴로 인용하라는 글)은 그 task 머리에서 찾는다."로 바꿨다 (`plugins/plate/skills/plan/SKILL.md`)
- `PlanRulesTest`에 `test_no_adding_after_evaluation_started`(1번 절에 `review.md`·`eval.md` 갈래와 "task로 더할지 묻지 않고 아무것도 쓰지 않고 끝난다")와 `test_adding_reads_earlier_task_heads`(task 머리를 읽는 글, phase 파일을 읽지 않는 글, "내용은 읽지 않는다" 없음)를 더했다 (`tests/test_skill_rules.py`)
- ARCHITECTURE `## 데이터 흐름` 계획 단계에 "더하면 이미 있는 task 머리를 읽는다"와 "review.md나 eval.md가 있어 tasks 끝의 평가가 시작된 tasks면 더할지 묻지 않고 더하지 않는다고 알리고 끝난다" 갈래를, `## 디렉터리 구조`의 `test_skill_rules.py` 줄 끝에 새 테스트가 다루는 규칙을 더했다 (`docs/ARCHITECTURE.md`)

## 확인 결과
- 더하는 경우가 완료 조건 1대로다
  - `python3 -m unittest discover -s tests` → `Ran 183 tests in 16.802s` / `OK`. `python3 -m unittest -v tests.test_skill_rules`에 `test_57_quote_earlier_task_text_as_changed ... ok`, `test_adding_reads_earlier_task_heads ... ok`, `test_no_adding_after_evaluation_started ... ok`가 있다. 통과
  - `docs/ARCHITECTURE.md` `## 데이터 흐름`의 계획 단계를 읽음 → "tasks가 진행 중이면 새 요청을 지금 tasks에 task로 더할지 묻고, 더하면 이미 있는 task 머리를 읽는다"와 "docs/tasks/review.md나 eval.md가 있어 tasks 끝의 평가가 시작된 tasks면 더할지 묻지 않고 더하지 않는다고 알리고 끝난다" 두 갈래가 있다. 통과
- 앞 task가 이룬 tasks 완료 조건 3이 그대로다
  - `git grep -n 'TOOLS.md' -- plugins/` → 출력 없음(종료 코드 1). 통과

## 계획과 달라진 점
없음

## 남은 것
- `tests/test_skill_rules.py` 머리 docstring의 이슈 목록은 고치지 않았다. 새 테스트는 이슈 번호가 아니라 cleanup 발견에서 나와 주석으로 출처를 적었다

## 하네스에서 걸린 것
없음
