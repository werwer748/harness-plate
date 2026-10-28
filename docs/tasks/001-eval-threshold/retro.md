# 회고

## 회고 1

**확인**
- 1. eval이 처리와 문턱을 적는다
  - 새 글 여덟마다 `grep -cF -e '<글>' plugins/plate/skills/eval/SKILL.md` → 모두 `1`. 옛 글 `plate 자체의 것에는 이슈로 올릴 제목과 본문을 적는다` → `0`. 통과
  - `done-phase-2.md` "한 일"의 헤드리스 시험 결과를 읽고, 남아 있는 시험 저장소 `…/scratchpad/evaltest.pKl7`(마지막 커밋 `22593d3 greet: 하네스 eval`)의 `docs/tasks/eval.md`를 직접 읽음 → 고칠 거리 1(나)·2(가)는 `문턱: 넘음`과 이슈 제목, 3(다)은 `문턱: 넘지 않음`이고 이슈 제목 없음, (라)는 고칠 거리에 없고 "하네스에서 걸린 것"에 감수한 것과 같은 뜻이라 적지 않았다고 적힘, (마)는 "실패" 1~4에 없음, 고칠 거리 넷 모두 `처리:` 줄 있음. 기록의 해시 `6d5fdd8ca384116079edbd4d261c0cc7829ad092`와 지금 `git hash-object plugins/plate/skills/eval/SKILL.md` → 같다. 통과
- 2. #74: eval 2번에 `돌리지 않음` 줄의 글이 있다
  - `grep -cF -e '코드 평가의 "하네스에서 걸린 것" 가운데 계획의 `돌리지 않음` 줄이 정한 동작 때문에 낮아진 등급만 적은 줄은 실패가 아니다' plugins/plate/skills/eval/SKILL.md` → `1`. 통과
  - 완료 조건 1의 헤드리스 시험 `eval.md`의 "실패" 1~4에 (마)가 없음(위와 같이 직접 읽음). 통과
- 3. run의 tasks 끝이 문턱과 처리를 따른다
  - 새 글 열셋마다 `grep -cF -e '<글>' plugins/plate/skills/run/SKILL.md` → 모두 `1`. 세 절 머리 `grep -cxF -e` → 저마다 `1`. 옛 글 셋 `grep -cF -e` → 모두 `0`. `grep -cE '^   - BACKLOG로 미룰 것: 소스 문제의 번호$' plugins/plate/skills/run/SKILL.md` → `0`. 통과
  - 돌리지 않음 줄(run의 tasks 끝은 헤드리스로 돌리지 않음)은 계획이 정한 것이라 돌리지 않았다
- 4. 맥락 문서가 바뀐 규칙과 맞는다
  - `grep -cF -e '### ADR-025' docs/ADR.md` → `1`, `grep -cF -e 'ADR-025로 바뀜' docs/ADR.md` → `1`. 통과
  - PRD 옛 글 → `0`, `문턱을 넘은 plate 자체의 고칠 거리만 GitHub 이슈로 올리고(ADR-025)` → `1`. 통과
  - ARCHITECTURE 옛 글 → `0`, `문턱을 넘은 plate 자체의 고칠 거리는 GitHub 이슈로 올리고` → `1`. 통과
  - `AGENTS.md`의 새 문서 지도 행 `grep -cF -e` → `1`, 옛 행 → `0`. 통과
  - `grep -cxF -e` `## 감수한 것`, `## 소스 문제`, `## 하네스 고칠 거리` (`docs/BACKLOG.md`) → 저마다 `1`. 통과
  - `docs/ARCHITECTURE.md`의 `test_skill_rules.py` 줄(1줄)에 `eval 고칠 거리의 처리와 문턱`과 `run 처음 안의 문턱과 BACKLOG 세 절`이 저마다 있음. `sed -n '1,8p' tests/test_skill_rules.py`에 `eval의 #36·#50·#51·#74`가 있음. 통과
- 5. 고친 글이 빠지면 실패하는 테스트가 있고, 모든 테스트가 통과한다
  - `python3 -m unittest discover -s tests` → `Ran 202 tests`, 마지막 줄 `OK`. 통과
  - 네 시험을 저마다 `mktemp -d`에 `cp -R plugins tests`한 새 사본에서 돌림 → 네 글 모두 사본에 `1`번, 빈 글로 바꾼 뒤 출력에 저마다 `FAIL: test_threshold_and_disposition (test_skill_rules.EvalRulesTest`, `FAIL: test_74_untested_lines_not_failures (test_skill_rules.EvalRulesTest`, `FAIL: test_first_proposal_uses_threshold (test_skill_rules.RunRulesTest`, `FAIL: test_backlog_three_sections (test_skill_rules.RunRulesTest`가 있고 마지막 줄 `FAILED (failures=1)`. 통과
- 6. 두 매니페스트의 버전이 0.22.0이고 마켓플레이스가 유효하다
  - `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "0.22.0",`. 통과
  - `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 202 tests`, `OK`. 통과

**남은 것**
- phase 1: `tests/test_skill_rules.py` 머리 docstring의 이슈 목록은 고치지 않았다 → 문제 아님 (phase 2가 `#74`를 더했고 완료 조건 4의 확인이 통과한다)
- phase 1: `docs/BACKLOG.md`, `AGENTS.md`의 문서 지도 행, 맥락 문서는 고치지 않았다 → 문제 아님 (phase 3의 TODO였고 완료 조건 4의 확인이 모두 통과한다)
- phase 1: 이슈를 올리지 못한(`gh` 실패) 하네스 고칠 거리가 BACKLOG에 남지 않고 10번의 보고에만 남는다 → 문제 아님 (run 본문 378줄과 ADR-020의 `gh` 실패 처리(보고에 보이고 잇는다)를 ADR-025가 "그대로다"로 두었다. 결정이 정한 경계 밖이라 `FRICTION.md`에 경계 밖으로 적었다)
- phase 1: 고친 run 본문의 동작은 헤드리스로 돌려 보지 않았다 → 문제 아님 (완료 조건 3의 `돌리지 않음` 줄이 정한 동작이다)
- phase 2: (라)의 같은 뜻 가르기는 BACKLOG와 거의 같은 글 한 꼴에서만 시험했다 → 문제 아님 (eval 5번이 같은 뜻을 "고칠 스킬과 문제가 같은 것"으로 정해 두었고, 완료 조건 1이 보는 차림에서 (라)는 걸러졌다)
- phase 2: 시험 저장소 `review.md`의 (마) 줄과 테스트 적절성 근거가 서로 맞지 않았다 → 문제 아님 (시험 차림의 흠이고, 시험 `eval.md`가 (마) 줄을 eval 2번의 규칙대로 실패로 세지 않았음을 직접 읽어 봤다)

**문제**
- 없음

**판정**: 통과
