# eval의 문턱과 처리 갈래, run의 처음 안과 BACKLOG를 고친다

## 목표
eval은 하네스 고칠 거리마다 처리를 제안하고, plate 자체의 것은 문턱을 넘었는지 가른 뒤 넘은 것에만 이슈 제목과 본문을 적는다. 계획의 `돌리지 않음` 결정 때문에 낮아진 등급만 적은 코드 평가의 줄은 실패로 세지 않는다(#74). run의 처음 안과 `docs/BACKLOG.md`는 문턱과 처리를 따른다. eval은 헤드리스로 돌려 보고, 고친 글마다 테스트를 더하고, 맥락 문서와 버전(0.22.0)을 맞춘다.

## 범위 밖
- 이 프로젝트만의 하네스 고칠 거리에 문턱을 두는 것(처리 갈래는 둔다)
- run의 tasks 끝을 헤드리스로 돌려 보는 것
- 이미 열린 이슈를 다시 가르거나 닫는 것

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
- 문턱: plate 자체의 고칠 거리는 (1) 근거의 실패 가운데 잡힌 곳이 phase의 확인, task의 회고, tasks 끝인 것이나 멈춤이 있거나, (2) `docs/BACKLOG.md`의 하네스 고칠 거리 절에 같은 뜻의 항목이 있으면 문턱을 넘는다. 둘 다 아니면 넘지 않는다. 다시 나왔는지는 BACKLOG로만 보고 GitHub은 보지 않는다. 이 프로젝트만의 것에는 문턱을 두지 않는다. 이유: eval이 이미 적는 칸이라 기계적으로 가르고, eval은 기록과 커밋만 근거로 삼는다
- 처리: eval이 고칠 거리마다(두 갈래 모두) 규칙을 더하거나 고친다, 규칙을 지운다, 감수한다 가운데 하나와 까닭을 적고, run의 고칠 안에서 사용자가 승인한다. 감수한 것은 이슈로도 고침 task로도 가지 않고 BACKLOG의 감수한 것 절에 남는다. eval은 감수한 것과 같은 뜻의 것을 고칠 거리로 적지 않는다. 이유: 말하지 않음
- run의 처음 안: 소스 문제와, 처리가 감수가 아닌 이 프로젝트만의 고칠 거리는 고침 task에 둔다. plate 자체의 것은 문턱을 넘고 처리가 감수가 아닌 것만 이슈로 올릴 것에, 넘지 않은 것은 BACKLOG로 미룰 것에 둔다. 처리가 감수인 것은 갈래와 상관없이 감수할 것에 둔다 (추천안으로 정함)
- `docs/BACKLOG.md`는 세 절(`## 소스 문제`, `## 하네스 고칠 거리`, `## 감수한 것`)로 나눈다. 하네스 고칠 거리의 같은 뜻은 고칠 스킬과 문제가 같은 것이다. 하네스 고칠 거리 절의 항목은 소스 문제와 같이 나온 tasks와 다시 나오지 않은 tasks를 세고 셋에서 지운다. 감수한 것은 세지 않고 지우지 않는다. 문서 지도 행은 `` | `docs/BACKLOG.md` | 미룬 소스 문제와 하네스 고칠 거리, 감수한 것과 그것이 나온 tasks | tasks를 계획하거나 tasks 끝에서 고칠지 정할 때 | ``다 (추천안으로 정함)
- ADR-025의 내용: tasks 끝의 하네스 eval에서 나온 plate 자체의 고칠 거리는 문턱(위의 둘)을 넘고 처리가 감수가 아닌 것만 GitHub 이슈로 올리고, 넘지 않은 것은 `docs/BACKLOG.md`의 하네스 고칠 거리에, 감수한 것은 감수한 것 절에 둔다. ADR-020의 이슈로 올리는 길(같은 이슈면 "다시 나옴" 댓글, `gh` 실패 처리)은 그대로다. 이유: 실패는 51개에서 2~4개로 줄었는데 tasks마다 이슈는 3개 밑으로 내려간 적이 없고, 모든 고칠 거리를 이슈로 올리는 것이 그 바닥값을 만들었다(2026-10-29 조사). 트레이드오프: 한 번만 그 자리에서 걸린 plate의 결함은 다시 나올 때까지 이슈가 되지 않고, BACKLOG가 이 저장소의 것이라 다른 프로젝트에서 한 번씩 난 같은 결함은 합쳐 세지 않는다. 이유: 이슈 바닥값의 원인이 "모두 이슈로"라는 결정 자체였다
- 헤드리스 시험은 `mktemp -d`의 시험 저장소에서 `claude -p`에 작업 트리의 `plugins/plate`를 `--plugin-dir`로, `--permission-mode bypassPermissions`로 돌린다. 기록에는 차림, 출력, 그때의 본문 해시(`git hash-object`)를 남긴다. 이유: `docs/TOOLS.md`의 "스킬을 헤드리스로 돌려 볼 때의 허용 목록" (추천안으로 정함)
- 고친 글과 테스트 이름은 완료 조건에 적은 그대로 한다 (추천안으로 정함)
- 버전은 0.22.0이다. 이유: eval과 run의 동작이 바뀐다
