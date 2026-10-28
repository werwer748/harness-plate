# Phase 1: tasks 끝의 문제를 고친다

**목표**: task 머리의 완료 조건에 적힌 것을 모두 고친다.

**테스트 먼저**: 아니오 — 고칠 것이 모두 `plugins/plate/skills/run/SKILL.md`(.md)의 글이다

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

**TODO**
- [x] 고침 task에서 뺀(또는 아무것도 고치지 않기로 한) 이 프로젝트만의 하네스 고칠 거리를 BACKLOG로 미룰 것으로 옮기는 길을 더한다. 그 동작을 적은 맥락 문서의 줄과 그 글을 지키는 테스트도 맞춘다 (`plugins/plate/skills/run/SKILL.md`, `docs/ARCHITECTURE.md`, `tests/test_skill_rules.py`)
- [x] 처음 안에서 문턱을 넘었고 처리가 감수인 plate 자체의 고칠 거리가 어느 쪽으로 가는지(감수가 먼저) 적는다. 그 글을 지키는 테스트도 맞춘다 (`plugins/plate/skills/run/SKILL.md`, `tests/test_skill_rules.py`)

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다

## 한 일
- 고침 task에서 뺀(또는 아무것도 고치지 않기로 한) 이 프로젝트만의 하네스 고칠 거리를 BACKLOG로 미룰 것으로 옮기는 길을 더한다: run "보고하고 묻는다"의 고칠 안 `BACKLOG로 미룰 것` 정의 끝에 `와, 고침 task에서 뺀 이 프로젝트만의 하네스 고칠 거리의 번호`를 더하고, 고칠 곳을 말할 때의 줄을 `고침 task에서 뺀 소스 문제와 이 프로젝트만의 하네스 고칠 거리는 BACKLOG로 미룰 것으로 옮긴다`로, 아무것도 고치지 않겠다는 답에 `고침 task에 두었던 이 프로젝트만의 하네스 고칠 거리도 BACKLOG로 미룰 것에 둔다`를 더했다. "BACKLOG를 고친다"의 `미룰 하네스 고칠 거리마다` 뒤에 `(갈래와 상관없이, 항목의 갈래 칸에 그 갈래를 적는다)`를 더했다. ARCHITECTURE의 `test_skill_rules.py` 줄에 이 규칙과 감수 먼저를 더했고, 테스트 `test_project_only_fixes_deferred_to_backlog`를 더하고 `test_first_proposal_uses_threshold`의 정의 줄 기대를 새 줄로 맞췄다 (`plugins/plate/skills/run/SKILL.md`, `docs/ARCHITECTURE.md`, `tests/test_skill_rules.py`)
- 처음 안에서 문턱을 넘었고 처리가 감수인 plate 자체의 고칠 거리가 어느 쪽으로 가는지(감수가 먼저) 적는다: 처음 안 문단에서 감수 갈래 글을 문턱 갈래 글 앞으로 옮기고 `감수가 문턱보다 먼저다: 처리가 감수인 plate 자체의 것은 문턱을 넘었어도 이슈로 올릴 것에 두지 않는다`를 더하고, 문턱 갈래 글 앞에 `처리가 감수가 아닌 것 가운데`를 붙였다. `test_first_proposal_uses_threshold`에 그 글과 두 글의 차례(감수 글이 앞)를 보는 단언을 더했다 (`plugins/plate/skills/run/SKILL.md`, `tests/test_skill_rules.py`)

## 확인 결과
- 완료 조건 1: 고침 task에서 뺀 이 프로젝트만의 하네스 고칠 거리가 BACKLOG로 미룰 것으로 가고 `갈래: 이 프로젝트만` 항목을 채울 길이 있다
  - `sed -n '351,360p'`와 "BACKLOG를 고친다"를 다시 읽음 → 정의 줄, 고칠 곳을 말할 때, 아무것도 고치지 않겠다는 답이 저마다 이 프로젝트만의 것을 BACKLOG로 미룰 것에 두고, "BACKLOG를 고친다"의 미룰 하네스 고칠 거리마다가 갈래와 상관없이 하네스 고칠 거리 절에 갈래 칸과 함께 더한다. 통과
- 완료 조건 2: 문턱을 넘었고 처리가 감수인 plate 자체의 고칠 거리가 갈 자리가 하나다
  - 처음 안 문단을 다시 읽음 → 감수 글이 먼저 오고 "감수가 문턱보다 먼저다… 이슈로 올릴 것에 두지 않는다"와 문턱 갈래가 "처리가 감수가 아닌 것 가운데"로 좁혀져 감수할 것 하나로 정해진다. 통과
- 완료 조건 3: tasks 완료 조건 3
  - 새 글 열셋마다 `grep -cF -e '<글>' plugins/plate/skills/run/SKILL.md` → 모두 `1`. 세 절 머리 `grep -cxF -e` → 저마다 `1`. 옛 글 셋 `grep -cF -e` → 모두 `0`. `grep -cE '^   - BACKLOG로 미룰 것: 소스 문제의 번호$'` → `0`. 통과
- 완료 조건 3: tasks 완료 조건 5
  - `python3 -m unittest discover -s tests` → `Ran 203 tests`, 마지막 줄 `OK`. 통과
  - `mktemp -d` 사본 넷(`cp -R`로 `plugins`, `tests` 복사)에서 글이 저마다 `count=1`, 빈 글로 바꾸고 테스트를 돌림 → `FAIL: test_threshold_and_disposition (test_skill_rules.EvalRulesTest)`, `FAIL: test_74_untested_lines_not_failures (test_skill_rules.EvalRulesTest)`, `FAIL: test_first_proposal_uses_threshold (test_skill_rules.RunRulesTest)`, `FAIL: test_backlog_three_sections (test_skill_rules.RunRulesTest)`가 저마다 나옴. 통과

## 계획과 달라진 점
- 없음

## 남은 것
- 고침 task가 고치기로 한 이 프로젝트만의 하네스 고칠 거리와 같은 뜻의 BACKLOG 항목을 지우는 줄은 더하지 않았다(소스 문제의 "고치기로 한 소스 문제와 같은 뜻의 항목은 지운다"에 맞먹는 것). TODO 밖이라 두었고, 그런 항목은 "그 밖의 항목"으로 다시 나오지 않은 tasks가 세어지다 셋에서 지워진다
- 바뀐 run 본문의 tasks 끝 동작은 읽기 확인과 글 테스트로만 봤고 헤드리스로 돌려 보지 않았다(계획이 요구하지 않음)

## 하네스에서 걸린 것
- 사본 시험에서 글을 빈 글로 바꾸는 데 `python3`의 `str.replace`를 썼다. 계획은 바꾸는 도구를 정하지 않았다

## 확인 1

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 완료 조건 1: `plugins/plate/skills/run/SKILL.md` 339~362줄("보고하고 묻는다")과 380~398줄("BACKLOG를 고친다"), 412줄(양식)을 읽음 → 고칠 안의 `BACKLOG로 미룰 것` 정의에 `고침 task에서 뺀 이 프로젝트만의 하네스 고칠 거리의 번호`가 있고, 고칠 곳을 말할 때 `고침 task에서 뺀 소스 문제와 이 프로젝트만의 하네스 고칠 거리는 BACKLOG로 미룰 것으로 옮긴다`, 아무것도 고치지 않겠다는 답에 `고침 task에 두었던 이 프로젝트만의 하네스 고칠 거리도 BACKLOG로 미룰 것에 둔다`가 있다. "BACKLOG를 고친다"의 `미룰 하네스 고칠 거리마다(갈래와 상관없이, 항목의 갈래 칸에 그 갈래를 적는다)`가 하네스 고칠 거리 절에 항목을 더하고, 양식 412줄의 `갈래: {plate 자체 | 이 프로젝트만}`을 채울 길이 있다. 통과
  - 완료 조건 2: 처음 안 문단(354줄)을 읽음 → `처리가 감수인 하네스 고칠 거리는 갈래와 상관없이 감수할 것에 둔다. 감수가 문턱보다 먼저다: 처리가 감수인 plate 자체의 것은 문턱을 넘었어도 이슈로 올릴 것에 두지 않는다`가 문턱 갈래 글보다 앞에 있고, 문턱 갈래 글은 `처리가 감수가 아닌 것 가운데`로 좁혀져 있다. 문턱을 넘은 감수인 plate 자체의 것은 감수할 것 하나로 간다. 통과
  - 완료 조건 3(tasks 완료 조건 3): 새 글 열셋마다 `grep -cF -e '<글>' plugins/plate/skills/run/SKILL.md` → 모두 `1`. 세 절 머리 `grep -cxF -e '<줄>' plugins/plate/skills/run/SKILL.md` → 저마다 `1`. 옛 글 셋 `grep -cF -e` → 모두 `0`. `grep -cE '^   - BACKLOG로 미룰 것: 소스 문제의 번호$' plugins/plate/skills/run/SKILL.md` → `0`. 통과
  - 완료 조건 3(tasks 완료 조건 5): `python3 -m unittest discover -s tests` → `Ran 203 tests`, 마지막 줄 `OK`. 통과
  - 완료 조건 3(tasks 완료 조건 5, 사본 시험): 저마다 새 `mktemp -d` 사본(`cp -R plugins tests`)에서 글을 한 번 있는지 세고(`count= 1` 넷) 빈 글로 바꾼 뒤 `python3 -m unittest discover -s tests` → `FAIL: test_threshold_and_disposition (test_skill_rules.EvalRulesTest)`, `FAIL: test_74_untested_lines_not_failures (test_skill_rules.EvalRulesTest)`, `FAIL: test_first_proposal_uses_threshold (test_skill_rules.RunRulesTest)`, `FAIL: test_backlog_three_sections (test_skill_rules.RunRulesTest)`가 저마다 나옴. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 203 tests`, `OK`. 통과

**남은 것**
- 고침 task가 고치기로 한 이 프로젝트만의 하네스 고칠 거리와 같은 뜻의 BACKLOG 항목을 지우는 줄을 더하지 않았다 → 완료 조건 1, 2와 tasks 완료 조건 3, 5는 BACKLOG로 미루는 길과 감수·문턱의 자리만 보고, 고치기로 한 하네스 고칠 거리의 BACKLOG 항목을 지우는 동작은 보지 않는다. 하네스에서 걸린 것
- 바뀐 run 본문의 tasks 끝 동작을 헤드리스로 돌려 보지 않았다 → 통과 조건(완료 조건 1, 2)이 보는 것은 본문의 글에 길과 자리가 정해져 있는지이고 그 확인은 다시 읽기와 글 테스트로 정해져 있어, 돌려 본 동작을 보지 않는다. 걸리지 않는다. 하네스에서 걸린 것

**실패**
- 없음

**하네스에서 걸린 것**
- 남은 것: 고침 task가 고치기로 한 이 프로젝트만의 하네스 고칠 거리와 같은 뜻의 BACKLOG 항목을 지우는 줄이 run 본문에 없다. 그런 항목은 "그 밖의 항목"으로 세어지다 다시 나오지 않은 tasks가 셋이 되어야 지워진다
- 남은 것: 바뀐 run 본문의 tasks 끝 동작은 헤드리스로 돌려 보지 않았다. task 머리에 `- 돌리지 않음` 줄이 없어 돌리지 않기로 정한 것도 아니다(AGENTS.md는 고친 본문의 동작을 헤드리스 시험으로 본다고 한다)
- 사본 시험에서 글을 빈 글로 바꾸는 도구를 계획이 정하지 않아 `python3`의 `str.replace`를 썼다

**판정**: 통과
