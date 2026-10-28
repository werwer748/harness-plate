# Phase 2: 회고 1의 문제를 고친다

**목표**: 회고 1에서 나온 문제를 모두 고친다.

**테스트 먼저**: 아니오 — 고칠 것이 `plugins/plate/skills/run/SKILL.md`(.md)의 글뿐이다

**읽을 것**
- `docs/tasks/002-fixes/retro.md`의 `## 회고 1`부터 `## 회고 1`까지의 절
- `plugins/plate/skills/run/SKILL.md`
- `tests/test_skill_rules.py`
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/ADR.md`
- `docs/TOOLS.md`
- `docs/BACKLOG.md`

**TODO**
- [x] run "BACKLOG를 고친다"에 고침 task가 고치기로 한 이 프로젝트만의 하네스 고칠 거리와 같은 뜻의 하네스 고칠 거리 절 항목을 지우는 줄이 없다(소스 문제의 `고치기로 한 소스 문제와 같은 뜻의 항목은 지운다`에 맞먹는 것). 이 task가 그 항목이 BACKLOG에 드는 길을 열어, 그런 항목이 다시 나와 고침 task로 가면 "그 밖의 항목"으로 다시 나오지 않은 tasks에 세어지고 고친 뒤에도 셋이 될 때까지 미룬 것으로 남는다. 그 줄을 더하고, 그 글을 지키는 테스트도 맞춘다 (`plugins/plate/skills/run/SKILL.md`, `tests/test_skill_rules.py`)

**통과 조건**
- 회고 1의 문제가 모두 고쳐졌다.
  - 확인: TODO에 넣은 문제마다 적힌 곳과 그 동작을 적은 맥락 문서와 README의 줄을 다시 읽거나 돌리고, 걸린 테스트를 돌린다
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다

## 한 일
- run "BACKLOG를 고친다"에 고침 task가 고치기로 한 이 프로젝트만의 하네스 고칠 거리와 같은 뜻의 항목을 지우는 줄이 없다: `- 이슈로 올린 하네스 고칠 거리와 같은 뜻의 항목은 지운다.` 줄 앞, `- 고치기로 한 소스 문제와 같은 뜻의 항목은 지운다. 고침 task가 고친다.` 줄 바로 아래에 `- 고침 task가 고치기로 한 이 프로젝트만의 하네스 고칠 거리와 같은 뜻의 항목은 지운다. 고침 task가 고친다.`를 더했다 (`plugins/plate/skills/run/SKILL.md`). 그 글을 `test_backlog_three_sections`의 지킬 글 목록에 더했다 (`tests/test_skill_rules.py`)

## 확인 결과
- 회고 1의 문제가 모두 고쳐졌다.
  - `plugins/plate/skills/run/SKILL.md`의 "BACKLOG를 고친다"를 다시 읽음 → 고침 task가 고치기로 한 이 프로젝트만의 하네스 고칠 거리와 같은 뜻의 항목을 지우는 줄이 있어, 그 항목은 "그 밖의 항목"으로 세어지지 않는다. `docs/PRD.md` 18줄, `docs/ARCHITECTURE.md` 76줄, `docs/ADR.md` 54줄을 다시 읽음 → 요약 수준의 글이라 새 줄과 어긋나지 않는다. 통과
  - `python3 -m unittest discover -s tests` → `Ran 203 tests`, `OK`. 새 사본(`mktemp -d`, `cp -R plugins tests`)에서 새 글을 빈 글로 바꾸면 `count= 1` 뒤 `FAIL: test_backlog_three_sections (test_skill_rules.RunRulesTest) (text='고침 task가 고치기로 한 이 프로젝트만의 하네스 고칠 거리와 같은 뜻의 항목은 지운다')`. 통과
- task 머리의 완료 조건이 모두 참이다.
  - 완료 조건 1: "보고하고 묻는다"와 "BACKLOG를 고친다"를 다시 읽음 → 고칠 안의 BACKLOG로 미룰 것에 `고침 task에서 뺀 이 프로젝트만의 하네스 고칠 거리의 번호`, 고칠 곳을 말할 때와 아무것도 고치지 않겠다는 답에 옮기는 줄, `미룰 하네스 고칠 거리마다(갈래와 상관없이, 항목의 갈래 칸에 그 갈래를 적는다)`가 있다. 통과
  - 완료 조건 2: 처음 안 문단을 다시 읽음 → `감수가 문턱보다 먼저다: 처리가 감수인 plate 자체의 것은 문턱을 넘었어도 이슈로 올릴 것에 두지 않는다`와 `처리가 감수가 아닌 것 가운데 plate 자체의 …`로 갈 자리가 감수할 것 하나다. 통과
  - 완료 조건 3(tasks 완료 조건 3): 새 글 열셋 `grep -cF -e` → 모두 `1`. 세 절 머리 `grep -cxF -e` → 저마다 `1`. 옛 글 셋 `grep -cF -e` → 모두 `0`. `grep -cE '^   - BACKLOG로 미룰 것: 소스 문제의 번호$'` → `0`. 통과
  - 완료 조건 3(tasks 완료 조건 5): `python3 -m unittest discover -s tests` → 마지막 줄 `OK`. 네 시험을 저마다 새 사본에서 돌림 → 글마다 `count= 1`, 빈 글로 바꾼 뒤 `FAIL: test_threshold_and_disposition (test_skill_rules.EvalRulesTest`, `FAIL: test_74_untested_lines_not_failures (test_skill_rules.EvalRulesTest`, `FAIL: test_first_proposal_uses_threshold (test_skill_rules.RunRulesTest`, `FAIL: test_backlog_three_sections (test_skill_rules.RunRulesTest`가 저마다 나옴. 통과

## 계획과 달라진 점
- 없음

## 남은 것
- 바뀐 run 본문의 BACKLOG 고치기 동작은 헤드리스로 돌려 보지 않았다. tasks 머리가 돌리지 않기로 정한 동작이다
- `docs/ARCHITECTURE.md` 39줄의 테스트 설명 목록에는 이 줄을 따로 더하지 않았다. TODO가 바꿀 파일로 스킬 본문과 테스트만 적었고, 기존 항목 "run 처음 안의 문턱과 BACKLOG 세 절"이 같은 테스트를 가리킨다

## 하네스에서 걸린 것
- 없음
