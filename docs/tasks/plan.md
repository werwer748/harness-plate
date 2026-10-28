# eval에 하네스 고칠 거리의 문턱과 처리 갈래를 둔다

**이름**: eval-threshold

## 요청
권고 1: eval에 문턱을 둔다. 결과를 틀리게 했거나 두 tasks 이상에서 다시 나온 하네스 고칠 거리만 이슈로 올리고 나머지는 BACKLOG로 보낸다. "감수한다"와 "규칙을 지운다"를 고칠 거리와 같은 무게의 선택지로 둔다. run의 처음 안("모두 이슈로 올린다")도 이에 맞춘다. 관련 열린 이슈: #74.

## 목표
eval은 하네스 고칠 거리마다 처리(규칙을 더하거나 고친다, 규칙을 지운다, 감수한다)를 제안하고, plate 자체의 것은 잡힌 곳이나 BACKLOG의 재발로 문턱을 넘었는지 가르며, 문턱을 넘었고 처리가 감수가 아닌 것에만 이슈 제목과 본문을 적는다. 계획의 `돌리지 않음` 결정 때문에 낮아진 등급만 적은 코드 평가의 줄은 실패로 세지 않는다(#74). run의 처음 안은 문턱을 넘은 것만 이슈로, 넘지 않은 것은 BACKLOG로, 감수한 것은 BACKLOG의 감수한 것으로 보내고, `docs/BACKLOG.md`는 소스 문제, 하네스 고칠 거리, 감수한 것을 나눠 담는다. eval의 바뀐 동작은 헤드리스로 돌려 보고, 고친 글마다 빠지면 실패하는 테스트를 더한다. 맥락 문서(ADR, PRD, ARCHITECTURE, 문서 지도, 이 저장소의 BACKLOG)와 테스트 설명이 바뀐 규칙에 맞고, 버전은 0.22.0이 된다.

## 범위 밖
- 이 프로젝트만의 하네스 고칠 거리에 문턱을 두는 것. 지금처럼 고침 task로 간다(처리 갈래는 둔다)
- run의 tasks 끝(고칠 안, BACKLOG 고치기)을 헤드리스로 돌려 보는 것. `돌리지 않음`으로 둔다
- 이미 열린 이슈(#68~#70, #72, #73)를 문턱으로 다시 가르거나 닫는 것
- #74를 닫는 것. PR이 머지된 뒤 닫는다
- 확인 명령을 스크립트로 옮기는 것, 스킬 본문을 줄이는 것, 다른 프로젝트에서 돌려 보는 것(조사의 권고 2~4)

## 완료 조건
1. eval이 처리와 문턱을 적는다. eval 1번 "읽는다"에 `` `docs/BACKLOG.md`의 하네스 고칠 거리와 감수한 것 ``이 있다. 5번에 `처리는 규칙을 더하거나 고친다, 규칙을 지운다, 감수한다 가운데 하나다`, `잡힌 곳이 phase의 확인, task의 회고, tasks 끝인 실패나 멈춤이 근거에 있으면 문턱을 넘는다`, `` `docs/BACKLOG.md`의 하네스 고칠 거리에 같은 뜻의 항목이 있으면 문턱을 넘는다 ``, `` `docs/BACKLOG.md`의 감수한 것과 같은 뜻이면 고칠 거리로 적지 않는다 ``, `이슈 제목과 본문은 문턱을 넘었고 처리가 감수가 아닌 plate 자체의 것에만 적는다`가 있다. 기록의 양식에 `   - 처리: {규칙을 더하거나 고친다 | 규칙을 지운다 | 감수한다}`와 `   - 문턱: {넘음 | 넘지 않음}`이 있다. 옛 글 `plate 자체의 것에는 이슈로 올릴 제목과 본문을 적는다`는 없다
   - 확인: `grep -cF -e '<글>' plugins/plate/skills/eval/SKILL.md`를 위 새 글 여덟마다 돌리면 저마다 `1`이고, 옛 글은 `0`이다. 하나라도 아니면 실패
   - 확인: phase 2 기록의 eval 헤드리스 시험 결과를 읽는다. 시험 저장소의 기록에 다섯 실패를 둔다. (가) 확인 절의 실패로 잡힌 plate 자체의 것, (나) 그 자리에서만 적혔고 `docs/BACKLOG.md`의 하네스 고칠 거리에 같은 뜻의 항목이 있는 것, (다) 그 자리에서만 적혔고 BACKLOG에 같은 것이 없는 것, (라) `docs/BACKLOG.md`의 감수한 것과 같은 뜻인 것, (마) 코드 평가의 "하네스에서 걸린 것"에 계획의 `돌리지 않음` 결정 때문에 테스트 적절성이 낮아졌다고만 적은 줄. 더해진 `eval.md`에서 (가)와 (나)의 고칠 거리는 `문턱: 넘음`이고 이슈 제목이 있고, (다)는 `문턱: 넘지 않음`이고 이슈 제목이 없고, (라)는 고칠 거리에 없고, (마)는 "실패"에 없다. 고칠 거리마다 `처리:` 줄이 있다. 기록에 적힌 `git hash-object plugins/plate/skills/eval/SKILL.md`의 값이 지금 작업 트리에서 다시 낸 값과 같다. 하나라도 아니면 실패
2. #74: eval 2번에 `` 코드 평가의 "하네스에서 걸린 것" 가운데 계획의 `돌리지 않음` 줄이 정한 동작 때문에 낮아진 등급만 적은 줄은 실패가 아니다 ``가 있다
   - 확인: `grep -cF -e '<위 글>' plugins/plate/skills/eval/SKILL.md`가 `1`
   - 확인: 완료 조건 1의 헤드리스 시험에서 (마)가 `eval.md`의 "실패"에 없다
3. run의 tasks 끝이 문턱과 처리를 따른다. run 본문에 고칠 안의 `- 감수할 것: 처리가 감수인 하네스 고칠 거리의 번호`와 `- BACKLOG로 미룰 것: 소스 문제의 번호와, 문턱을 넘지 않은 plate 자체의 하네스 고칠 거리의 번호`, 처음 안의 `plate 자체의 하네스 고칠 거리는 문턱을 넘은 것만 이슈로 올릴 것에, 넘지 않은 것은 BACKLOG로 미룰 것에 둔다`와 `처리가 감수인 하네스 고칠 거리는 갈래와 상관없이 감수할 것에 둔다`, 고칠 곳을 말할 때의 `이슈로 올릴 것에서 뺀 하네스 고칠 거리는 BACKLOG로 미룰 것으로 옮긴다`와 `소스 문제와 plate 자체의 하네스 고칠 거리를 모두 BACKLOG로 미룰 것에 둔 안`, 보고의 `나눠 번호, 글, 처리와, plate 자체의 것은 문턱을 넘었는지`, "BACKLOG를 고친다"의 `미룰 하네스 고칠 거리마다`, `이슈로 올린 하네스 고칠 거리와 같은 뜻의 항목은 지운다`, `감수할 것마다 감수한 것 절에 항목을 더한다`, `감수한 것 절의 항목은 다시 나오지 않은 tasks를 세지 않고 지우지 않는다`, 낱말의 `미룬 소스 문제와 하네스 고칠 거리, 감수한 것을 tasks를 넘어 모으는 문서`, 양식의 줄 `## 소스 문제`, `## 하네스 고칠 거리`, `## 감수한 것`과 문서 지도 행 `` | `docs/BACKLOG.md` | 미룬 소스 문제와 하네스 고칠 거리, 감수한 것과 그것이 나온 tasks | tasks를 계획하거나 tasks 끝에서 고칠지 정할 때 | ``가 저마다 한 번 있다. 옛 글 `plate 자체의 하네스 고칠 거리는 모두 이슈로 올릴 것에 두고`, `소스 문제를 모두 BACKLOG로 미룰 것에 둔 안`, `` | `docs/BACKLOG.md` | 미룬 소스 문제와 그것이 나온 tasks | ``는 없다
   - 확인: 위 새 글마다 `grep -cF -e '<글>' plugins/plate/skills/run/SKILL.md`가 `1`이다. 세 절 머리는 `grep -cxF -e '<줄>' plugins/plate/skills/run/SKILL.md`로 저마다 `1`이다. 옛 글 셋은 `grep -cF -e`로 `0`이고, `grep -cE '^   - BACKLOG로 미룰 것: 소스 문제의 번호$' plugins/plate/skills/run/SKILL.md`도 `0`이다. 하나라도 아니면 실패
   - 돌리지 않음: run의 tasks 끝은 사용자의 답과 `gh`가 있어야 돌고 여러 턴을 이어야 닿는다. 사용자가 eval만 돌리기로 정했다
4. 맥락 문서가 바뀐 규칙과 맞는다
   - 확인: `grep -cF -e '### ADR-025' docs/ADR.md`가 `1`이고 `grep -cF -e 'ADR-025로 바뀜' docs/ADR.md`가 `1` 이상이다(ADR-020의 결정에 붙는다)
   - 확인: `grep -cF -e 'plate 자체의 고칠 거리는 GitHub 이슈로 올리고(ADR-020)' docs/PRD.md`가 `0`이고, `grep -cF -e '문턱을 넘은 plate 자체의 고칠 거리만 GitHub 이슈로 올리고(ADR-025)' docs/PRD.md`가 `1`이다
   - 확인: `grep -cF -e '승인받은 대로 plate 자체의 고칠 거리는 GitHub 이슈로 올리고' docs/ARCHITECTURE.md`가 `0`이고, `grep -cF -e '문턱을 넘은 plate 자체의 고칠 거리는 GitHub 이슈로 올리고' docs/ARCHITECTURE.md`가 `1`이다
   - 확인: 완료 조건 3의 새 문서 지도 행이 `AGENTS.md`에 `grep -cF -e`로 `1`이고, 옛 행은 `0`이다
   - 확인: `grep -cxF -e '## 감수한 것' docs/BACKLOG.md`가 `1`이고, `## 소스 문제`와 `## 하네스 고칠 거리`도 저마다 `1`이다
   - 확인: `docs/ARCHITECTURE.md`의 `test_skill_rules.py` 줄에 `eval 고칠 거리의 처리와 문턱`과 `run 처음 안의 문턱과 BACKLOG 세 절`이 저마다 든다. `sed -n '1,8p' tests/test_skill_rules.py`의 목록에 eval의 `#74`가 있다. 하나라도 없으면 실패
5. 고친 글이 빠지면 실패하는 테스트가 있고, 모든 테스트가 통과한다
   - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
   - 확인: 아래 네 시험을 저마다 새 사본(`mktemp -d`로 만든 폴더에 작업 트리의 `plugins`와 `tests`를 `cp -R`로 복사한 것)에서 한다. 그 글이 사본의 파일에 한 번 있는지 보고(없으면 실패), 그 글을 빈 글로 바꾸고 사본에서 `python3 -m unittest discover -s tests`를 돌리면 출력에 그 테스트의 `FAIL:` 줄이 있다. eval 본문의 `잡힌 곳이 phase의 확인, task의 회고, tasks 끝인 실패나 멈춤이 근거에 있으면 문턱을 넘는다` → `FAIL: test_threshold_and_disposition (test_skill_rules.EvalRulesTest`, eval 본문의 `` 코드 평가의 "하네스에서 걸린 것" 가운데 계획의 `돌리지 않음` 줄이 정한 동작 때문에 낮아진 등급만 적은 줄은 실패가 아니다 `` → `FAIL: test_74_untested_lines_not_failures (test_skill_rules.EvalRulesTest`, run 본문의 `plate 자체의 하네스 고칠 거리는 문턱을 넘은 것만 이슈로 올릴 것에, 넘지 않은 것은 BACKLOG로 미룰 것에 둔다` → `FAIL: test_first_proposal_uses_threshold (test_skill_rules.RunRulesTest`, run 본문의 `감수할 것마다 감수한 것 절에 항목을 더한다` → `FAIL: test_backlog_three_sections (test_skill_rules.RunRulesTest`
6. 두 매니페스트의 버전이 0.22.0이고 마켓플레이스가 유효하다
   - 확인: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json`의 두 줄이 모두 `0.22.0`
   - 확인: `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`

## 결정
- plate 자체의 고칠 거리의 문턱은 둘이다. 근거의 실패 가운데 잡힌 곳이 phase의 확인, task의 회고, tasks 끝인 것이나 멈춤이 있거나, `docs/BACKLOG.md`의 하네스 고칠 거리에 같은 뜻의 항목이 있다. 이유: eval이 이미 적는 칸이라 기계적으로 가르고, 틀린 결과가 나갔다가 뒤에서 잡힌 것과 그냥 걸린 것을 가른다
- 다시 나왔는지는 BACKLOG의 하네스 항목으로만 보고 GitHub 이슈는 보지 않는다. 이유: eval은 기록과 커밋만 근거로 삼고 GitHub을 보지 않는다(eval 절대 규칙 2)
- eval이 고칠 거리마다 처리(규칙을 더하거나 고친다, 규칙을 지운다, 감수한다)와 까닭을 제안하고, run의 고칠 안에서 사용자가 승인한다. 감수한 것은 BACKLOG의 감수한 것에 남기고, eval은 같은 뜻의 것을 다시 고칠 거리로 올리지 않는다. 이유: 말하지 않음
- 문턱은 plate 자체의 것에만 두고, 처리 갈래는 두 갈래 모두에 둔다. 이유: 요청은 이슈 흐름을 겨냥하고, 이 프로젝트만의 것은 보통 문서 한 줄이라 고치는 비용이 작다
- `docs/BACKLOG.md`는 세 절(소스 문제, 하네스 고칠 거리, 감수한 것)로 나눈다. 하네스 고칠 거리의 같은 뜻은 고칠 스킬과 문제가 같은 것이다. 감수한 것은 다시 나오지 않은 tasks를 세지 않고 지우지 않는다 (추천안으로 정함)
- #74를 함께 고친다. 이유: 같은 eval 2번과 5번을 고치는 일이고, 실패로 세지 않을 것을 거르는 같은 목적이다
- ADR-025를 새로 두어 ADR-020의 "plate 자체의 것은 이슈로 올린다"를 바꾸고, PRD 핵심 기능 8, ARCHITECTURE의 데이터 흐름, 문서 지도의 BACKLOG 행을 고친다. 이유: 이슈 바닥값의 원인이 "모두 이슈로"라는 이 결정 자체였다
- 헤드리스로 돌려 보는 것은 eval만 둔다. 이유: run의 고칠 안은 사용자의 답과 `gh`가 있어야 돈다
- 헤드리스 시험은 `mktemp -d`의 시험 저장소에서 `claude -p`에 작업 트리의 `plugins/plate`를 `--plugin-dir`로, `--permission-mode bypassPermissions`로 돌리고, 기록에는 차림, 출력, 그때의 본문 해시(`git hash-object`)를 남긴다. 이유: `docs/TOOLS.md`의 "스킬을 헤드리스로 돌려 볼 때의 허용 목록"(이은 Bash는 허용 목록으로 풀리지 않는다)과 plan의 남은 결과를 읽는 확인 규칙 (추천안으로 정함)
- 고친 글과 테스트 이름은 완료 조건에 적은 그대로 한다. 이유: 지울 글을 그대로 인용하고 실패할 테스트를 미리 적으려면 글과 이름이 계획에서 정해져야 한다 (추천안으로 정함)
- task 하나에 phase 셋으로 한다(run → eval과 헤드리스 시험 → 맥락 문서와 버전). 이유: eval의 시험 차림이 run이 정할 BACKLOG 양식에 기대고, 스킬마다 따로 확인할 수 있다 (추천안으로 정함)
- 버전은 0.22.0이다. 이유: eval과 run의 동작이 바뀐다
- run을 시작하기 전에 사용자가 plan 모드를 끄고 bypassPermissions로 둔다. 이유: `AGENTS.md`의 작업 규칙(`plugins/plate/skills/` 편집이 auto mode에서 막힌다)

## task 목록
- `001-eval-threshold`: eval이 처리와 문턱을 적고 #74의 줄을 실패로 세지 않으며, run의 처음 안과 BACKLOG가 이를 따르고, 맥락 문서·테스트·버전이 맞춰진다
- `002-fixes`: tasks 끝에서 고치기로 한 것이 고쳐진다
