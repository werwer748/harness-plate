# tasks 끝의 문제를 고친다

## 목표
tasks 끝의 코드 평가와 하네스 eval에서 고치기로 한 것을 모두 고친다.

## 범위 밖
- 코드 평가와 하네스 eval을 다시 하는 것
- plate 자체의 하네스 고칠 거리를 고치는 것. 이슈로 올리고 plate 저장소에서 고친다

## 완료 조건
1. tasks 끝에서 고침 task에서 뺀(또는 아무것도 고치지 않기로 한) 이 프로젝트만의 하네스 고칠 거리를 BACKLOG로 옮기는 길이 없어 사라지고, BACKLOG 양식의 하네스 고칠 거리 절이 허용하는 `갈래: 이 프로젝트만` 항목은 채워질 길이 없다 (`plugins/plate/skills/run/SKILL.md:358`)
   - 확인: `plugins/plate/skills/run/SKILL.md`의 "보고하고 묻는다"(고칠 곳을 말할 때, 아무것도 고치지 않겠다는 답, BACKLOG로 미룰 것의 정의)와 "BACKLOG를 고친다"를 다시 읽어, 고침 task에서 뺀 이 프로젝트만의 하네스 고칠 거리가 BACKLOG로 미룰 것으로 가고 양식의 `갈래: 이 프로젝트만` 항목을 채울 길이 있다
2. 처음 안의 문턱 갈래 글과 감수 갈래 글이 문턱을 넘은 감수인 plate 자체의 것에 겹쳐 두 자리를 가리키고 어느 쪽이 먼저인지 적지 않았다 (`plugins/plate/skills/run/SKILL.md:354`)
   - 확인: `plugins/plate/skills/run/SKILL.md`의 처음 안 문단을 다시 읽어, 문턱을 넘었고 처리가 감수인 plate 자체의 고칠 거리가 갈 자리가 하나로 정해져 있다
3. tasks 완료 조건 3, 5가 참이다.
   - tasks 완료 조건 3: run의 tasks 끝이 문턱과 처리를 따른다. run 본문에 고칠 안의 `- 감수할 것: 처리가 감수인 하네스 고칠 거리의 번호`와 `- BACKLOG로 미룰 것: 소스 문제의 번호와, 문턱을 넘지 않은 plate 자체의 하네스 고칠 거리의 번호`, 처음 안의 `plate 자체의 하네스 고칠 거리는 문턱을 넘은 것만 이슈로 올릴 것에, 넘지 않은 것은 BACKLOG로 미룰 것에 둔다`와 `처리가 감수인 하네스 고칠 거리는 갈래와 상관없이 감수할 것에 둔다`, 고칠 곳을 말할 때의 `이슈로 올릴 것에서 뺀 하네스 고칠 거리는 BACKLOG로 미룰 것으로 옮긴다`와 `소스 문제와 plate 자체의 하네스 고칠 거리를 모두 BACKLOG로 미룰 것에 둔 안`, 보고의 `나눠 번호, 글, 처리와, plate 자체의 것은 문턱을 넘었는지`, "BACKLOG를 고친다"의 `미룰 하네스 고칠 거리마다`, `이슈로 올린 하네스 고칠 거리와 같은 뜻의 항목은 지운다`, `감수할 것마다 감수한 것 절에 항목을 더한다`, `감수한 것 절의 항목은 다시 나오지 않은 tasks를 세지 않고 지우지 않는다`, 낱말의 `미룬 소스 문제와 하네스 고칠 거리, 감수한 것을 tasks를 넘어 모으는 문서`, 양식의 줄 `## 소스 문제`, `## 하네스 고칠 거리`, `## 감수한 것`과 문서 지도 행 `` | `docs/BACKLOG.md` | 미룬 소스 문제와 하네스 고칠 거리, 감수한 것과 그것이 나온 tasks | tasks를 계획하거나 tasks 끝에서 고칠지 정할 때 | ``가 저마다 한 번 있다. 옛 글 `plate 자체의 하네스 고칠 거리는 모두 이슈로 올릴 것에 두고`, `소스 문제를 모두 BACKLOG로 미룰 것에 둔 안`, `` | `docs/BACKLOG.md` | 미룬 소스 문제와 그것이 나온 tasks | ``는 없다
     - 확인: 위 새 글마다 `grep -cF -e '<글>' plugins/plate/skills/run/SKILL.md`가 `1`이다. 세 절 머리는 `grep -cxF -e '<줄>' plugins/plate/skills/run/SKILL.md`로 저마다 `1`이다. 옛 글 셋은 `grep -cF -e`로 `0`이고, `grep -cE '^   - BACKLOG로 미룰 것: 소스 문제의 번호$' plugins/plate/skills/run/SKILL.md`도 `0`이다. 하나라도 아니면 실패
   - tasks 완료 조건 5: 고친 글이 빠지면 실패하는 테스트가 있고, 모든 테스트가 통과한다
     - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
     - 확인: 아래 네 시험을 저마다 새 사본(`mktemp -d`로 만든 폴더에 작업 트리의 `plugins`와 `tests`를 `cp -R`로 복사한 것)에서 한다. 그 글이 사본의 파일에 한 번 있는지 보고(없으면 실패), 그 글을 빈 글로 바꾸고 사본에서 `python3 -m unittest discover -s tests`를 돌리면 출력에 그 테스트의 `FAIL:` 줄이 있다. eval 본문의 `잡힌 곳이 phase의 확인, task의 회고, tasks 끝인 실패나 멈춤이 근거에 있으면 문턱을 넘는다` → `FAIL: test_threshold_and_disposition (test_skill_rules.EvalRulesTest`, eval 본문의 `` 코드 평가의 "하네스에서 걸린 것" 가운데 계획의 `돌리지 않음` 줄이 정한 동작 때문에 낮아진 등급만 적은 줄은 실패가 아니다 `` → `FAIL: test_74_untested_lines_not_failures (test_skill_rules.EvalRulesTest`, run 본문의 `plate 자체의 하네스 고칠 거리는 문턱을 넘은 것만 이슈로 올릴 것에, 넘지 않은 것은 BACKLOG로 미룰 것에 둔다` → `FAIL: test_first_proposal_uses_threshold (test_skill_rules.RunRulesTest`, run 본문의 `감수할 것마다 감수한 것 절에 항목을 더한다` → `FAIL: test_backlog_three_sections (test_skill_rules.RunRulesTest`

## 결정
- 없음
