# 회고

## 회고 1

**확인**
- 완료 조건 1: 고침 task에서 뺀(또는 아무것도 고치지 않기로 한) 이 프로젝트만의 하네스 고칠 거리를 BACKLOG로 미룰 것으로 옮기는 길이 있고 양식의 `갈래: 이 프로젝트만` 항목을 채울 길이 있다
  - `plugins/plate/skills/run/SKILL.md` 351·358·359줄("보고하고 묻는다")과 384~390줄("BACKLOG를 고친다"), 412줄(양식)을 읽음 → 고칠 안의 BACKLOG로 미룰 것 정의에 `고침 task에서 뺀 이 프로젝트만의 하네스 고칠 거리의 번호`, 고칠 곳을 말할 때 `고침 task에서 뺀 소스 문제와 이 프로젝트만의 하네스 고칠 거리는 BACKLOG로 미룰 것으로 옮긴다`, 아무것도 고치지 않겠다는 답에 `고침 task에 두었던 이 프로젝트만의 하네스 고칠 거리도 BACKLOG로 미룰 것에 둔다`가 있고, `미룰 하네스 고칠 거리마다(갈래와 상관없이, 항목의 갈래 칸에 그 갈래를 적는다)`가 하네스 고칠 거리 절에 `갈래: {plate 자체 | 이 프로젝트만}` 항목을 더한다. 통과
- 완료 조건 2: 문턱을 넘었고 처리가 감수인 plate 자체의 고칠 거리가 갈 자리가 하나다
  - 같은 파일 354줄(처음 안 문단)을 읽음 → 감수 글이 앞에 있고 `감수가 문턱보다 먼저다: 처리가 감수인 plate 자체의 것은 문턱을 넘었어도 이슈로 올릴 것에 두지 않는다`가 있으며, 문턱 갈래 글은 `처리가 감수가 아닌 것 가운데`로 좁혀져 감수할 것 하나로 정해진다. 통과
- 완료 조건 3: tasks 완료 조건 3
  - 새 글 열셋마다 `grep -cF -e '<글>' plugins/plate/skills/run/SKILL.md` → 모두 `1`. 세 절 머리 `grep -cxF -e '<줄>'` → 저마다 `1`. 옛 글 셋 `grep -cF -e` → 모두 `0`. `grep -cE '^   - BACKLOG로 미룰 것: 소스 문제의 번호$' plugins/plate/skills/run/SKILL.md` → `0`. 통과
- 완료 조건 3: tasks 완료 조건 5
  - `python3 -m unittest discover -s tests` → `Ran 203 tests`, 마지막 줄 `OK`. 통과
  - 네 시험을 저마다 새 `mktemp -d` 사본(`cp -R plugins tests`)에서 돌림. 글은 저마다 `count= 1`이고, 빈 글로 바꾼 뒤 `python3 -m unittest discover -s tests` → `FAIL: test_threshold_and_disposition (test_skill_rules.EvalRulesTest)`, `FAIL: test_74_untested_lines_not_failures (test_skill_rules.EvalRulesTest)`, `FAIL: test_first_proposal_uses_threshold (test_skill_rules.RunRulesTest)`, `FAIL: test_backlog_three_sections (test_skill_rules.RunRulesTest)`가 저마다 나옴. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 203 tests`, `OK`. 통과

**남은 것**
- phase 1: 고침 task가 고치기로 한 이 프로젝트만의 하네스 고칠 거리와 같은 뜻의 BACKLOG 항목을 지우는 줄은 더하지 않았다 → 문제 (결함: 이 task가 이 프로젝트만의 항목이 BACKLOG에 드는 길을 열어, 그 항목이 다음 tasks에서 다시 나와 고침 task로 가면 "BACKLOG를 고친다"의 어느 줄에도 들지 않고 "그 밖의 항목"이 되어 다시 나왔는데도 다시 나오지 않은 tasks에 세어지고, 고친 뒤에도 미룬 것으로 남는다)
- phase 1: 바뀐 run 본문의 tasks 끝 동작은 헤드리스로 돌려 보지 않았다 → 문제 아님 (tasks 머리의 범위 밖 `run의 tasks 끝(고칠 안, BACKLOG 고치기)을 헤드리스로 돌려 보는 것. 돌리지 않음으로 둔다`와 결정 `헤드리스로 돌려 보는 것은 eval만 둔다`가 돌리지 않기로 정했다)

**문제**
- run "BACKLOG를 고친다"에 고침 task가 고치기로 한 이 프로젝트만의 하네스 고칠 거리와 같은 뜻의 하네스 고칠 거리 절 항목을 지우는 줄이 없다(소스 문제의 `고치기로 한 소스 문제와 같은 뜻의 항목은 지운다`에 맞먹는 것). 이 task가 그 항목이 BACKLOG에 드는 길을 열어, 그런 항목이 다시 나와 고침 task로 가면 "그 밖의 항목"으로 다시 나오지 않은 tasks에 세어지고 고친 뒤에도 셋이 될 때까지 미룬 것으로 남는다 (`plugins/plate/skills/run/SKILL.md`). 기준: 결함

**판정**: 문제 있음
