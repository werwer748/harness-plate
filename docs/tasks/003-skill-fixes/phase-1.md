# Phase 1: run이 결과 없이 돌아온 에이전트를 세 번째에 멈춘다

**목표**: 신뢰성-3이 고쳐져, run이 결과 없이 돌아온 에이전트를 같은 자리에서 연달아 세 번째에 멈추고, `review.md` 없이 하네스 eval로 가지 않는다.

**테스트 먼저**: 아니오 — 스킬 본문(`.md`)과 그 글을 지키는 테스트만 고친다

**읽을 것**
- `docs/cleanup/2026-10-29.md` (신뢰성-3의 근거와 고치는 방향)
- `plugins/plate/skills/run/SKILL.md`의 "3. 갈 곳을 정한다", "4. 수행을 맡긴다", "5. 확인을 맡긴다", "7. task 회고를 맡긴다", "코드 평가를 맡긴다", "하네스 eval을 맡긴다", "멈춘다", "`RUNLOG.md`" 절
- `docs/PRD.md`의 핵심 기능 7
- `docs/ARCHITECTURE.md`의 데이터 흐름 절 뒤 "어느 실행 방식이든" 문단과 디렉터리 구조의 `test_skill_rules.py` 줄
- `tests/test_skill_rules.py` (`RunRulesTest`, `section`, `subsection`)

**TODO**
- [ ] 4번, 5번, 7번, "코드 평가를 맡긴다", "하네스 eval을 맡긴다"의 돌아온 뒤에, 정한 결과(수행이면 `## 한 일` 기록 절, 확인이면 새 확인 절, 회고면 새 회고 절, 코드 평가면 `docs/tasks/review.md`, 하네스 eval이면 `docs/tasks/eval.md`)가 없으면 같은 자리를 다시 띄우고 에이전트 줄에 `| 다시 띄움: 결과 없음`을 덧붙이는 규칙이 더해진다. 같은 자리의 바로 앞 두 에이전트 줄이 모두 그 표시를 달았으면 다시 띄우지 않고 "멈춘다"로 간다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] "코드 평가를 맡긴다"의 돌아온 뒤가 `review.md`가 있을 때만 "하네스 eval을 맡긴다"로 가게 바뀐다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] "멈춘다"의 자리 목록에 결과 없이 돌아온 에이전트의 연달아 세 번째가 더해지고, "`RUNLOG.md`" 절의 `다시 띄움` 설명에 `결과 없음`이 더해진다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] 위 글을 지키는 `RunRulesTest.test_no_result_relaunch_limit`이 더해진다 (`tests/test_skill_rules.py`)
- [ ] PRD 핵심 기능 7의 멈추는 자리와 ARCHITECTURE의 "어느 실행 방식이든" 문단에 결과 없는 에이전트의 세 번째가 더해지고, ARCHITECTURE의 `test_skill_rules.py` 줄에 새 시험이 더해진다 (`docs/PRD.md`, `docs/ARCHITECTURE.md`)

**통과 조건**
- run 본문이 다시 띄움과 상한을 적는다(완료 조건 1).
  - 확인: `grep -n '다시 띄움: 결과 없음' plugins/plate/skills/run/SKILL.md` → "멈춘다" 절과 "`RUNLOG.md`" 절에 저마다 한 줄 이상
  - 확인: `python3 -m unittest tests.test_skill_rules.RunRulesTest.test_no_result_relaunch_limit -v` → `OK`
- 맥락 문서가 맞다(완료 조건 8의 앞 절).
  - 확인: `grep -n '결과 없' docs/PRD.md docs/ARCHITECTURE.md` → 두 파일에 저마다 한 줄 이상
- 테스트 묶음이 통과한다.
  - 확인: `python3 -m unittest discover -s tests` → 마지막 줄이 `OK`
