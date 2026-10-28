# Phase 2: eval이 처리와 문턱을 적고 #74의 줄을 실패로 세지 않는다

**목표**: eval 본문(1번, 2번, 5번, 기록의 양식)이 task 머리의 결정대로 바뀌고, 그 글을 지키는 테스트가 더해지고, 헤드리스 시험으로 다섯 갈래가 확인된다.

**테스트 먼저**: 아니오 — 동작을 바꾸는 것은 스킬 본문(`.md`)이고, 테스트는 그 글을 지킨다

**읽을 것**
- `plugins/plate/skills/eval/SKILL.md` (1번, 2번의 표와 예외 목록, 5번, 기록의 양식, 8번)
- `plugins/plate/skills/run/SKILL.md`의 "BACKLOG를 고친다" 절 (앞 phase가 바꾼 BACKLOG의 세 절과 항목 꼴)
- `tests/test_skill_rules.py` (`EvalRulesTest`)
- `docs/TOOLS.md`의 "스킬을 헤드리스로 돌려 볼 때의 허용 목록"과 "세션 도중의 스킬 본문 고침"
- `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/BACKLOG.md`, `docs/cleanup/2026-10-28.md` (맥락 문서)

**TODO**
- [ ] 앞 phase의 산출물(run의 "BACKLOG를 고친다" 절의 세 절과 항목 꼴)에 대어 시험 저장소의 `docs/BACKLOG.md` 차림을 맞춘다 (시험 저장소)
- [ ] 1번 "읽는다"에 `` `docs/BACKLOG.md`의 하네스 고칠 거리와 감수한 것 ``이 더해진다 (`plugins/plate/skills/eval/SKILL.md`)
- [ ] 2번 예외 목록에 `` 코드 평가의 "하네스에서 걸린 것" 가운데 계획의 `돌리지 않음` 줄이 정한 동작 때문에 낮아진 등급만 적은 줄은 실패가 아니다 ``가 더해진다 (`plugins/plate/skills/eval/SKILL.md`)
- [ ] 5번에 `처리는 규칙을 더하거나 고친다, 규칙을 지운다, 감수한다 가운데 하나다`, `잡힌 곳이 phase의 확인, task의 회고, tasks 끝인 실패나 멈춤이 근거에 있으면 문턱을 넘는다`, `` `docs/BACKLOG.md`의 하네스 고칠 거리에 같은 뜻의 항목이 있으면 문턱을 넘는다 ``, `` `docs/BACKLOG.md`의 감수한 것과 같은 뜻이면 고칠 거리로 적지 않는다 ``, `이슈 제목과 본문은 문턱을 넘었고 처리가 감수가 아닌 plate 자체의 것에만 적는다`가 들고, 옛 글 `plate 자체의 것에는 이슈로 올릴 제목과 본문을 적는다`가 지워진다. 기록의 양식의 하네스 고칠 거리 항목에 `   - 처리: {규칙을 더하거나 고친다 | 규칙을 지운다 | 감수한다}`(까닭과 함께)와 `   - 문턱: {넘음 | 넘지 않음}`(근거와 함께, plate 자체의 것에만) 줄이 더해진다 (`plugins/plate/skills/eval/SKILL.md`)
- [ ] `EvalRulesTest`에 `test_threshold_and_disposition`(5번의 다섯 글과 양식의 두 줄)과 `test_74_untested_lines_not_failures`(2번의 글)가 더해진다 (`tests/test_skill_rules.py`)
- [ ] 헤드리스 시험을 한다. task 머리의 결정대로 시험 저장소를 차린다: `AGENTS.md`(문서 지도와 `docs/tasks/` 행), tasks 머리, task 폴더 하나(task 머리, `done-phase-1.md`, `retro.md`), `FRICTION.md`, `RUNLOG.md`, `review.md`, 세 절의 `docs/BACKLOG.md`, 스킬의 꼴대로의 커밋. 기록에 다섯 실패를 둔다: (가) 확인 절의 실패로 잡힌 plate 자체의 것, (나) 그 자리에서만 적혔고 BACKLOG의 하네스 고칠 거리에 같은 뜻의 항목이 있는 것, (다) 그 자리에서만 적혔고 BACKLOG에 같은 것이 없는 것, (라) BACKLOG의 감수한 것과 같은 뜻인 것, (마) `review.md`의 "하네스에서 걸린 것"에 계획의 `돌리지 않음` 결정 때문에 테스트 적절성이 낮아졌다고만 적은 줄. `/plate:eval`을 돌려 더해진 `eval.md`를 읽는다. 차림, 출력, 돌릴 때의 `git hash-object plugins/plate/skills/eval/SKILL.md`를 기록의 "한 일"에 남긴다 (시험 저장소, 이 phase의 기록)

**통과 조건**
- 완료 조건 1과 2가 참이다.
  - 확인: `grep -cF -e '<글>' plugins/plate/skills/eval/SKILL.md`를 TODO의 새 글 여덟마다 돌리면 저마다 `1`이고, 옛 글은 `0`이다
  - 확인: 헤드리스 시험의 `eval.md`에서 (가)와 (나)의 고칠 거리는 `문턱: 넘음`이고 이슈 제목이 있고, (다)는 `문턱: 넘지 않음`이고 이슈 제목이 없고, (라)는 고칠 거리에 없고, (마)는 "실패"에 없다. 고칠 거리마다 `처리:` 줄이 있다. 기록에 적은 본문 해시가 지금 작업 트리에서 다시 낸 `git hash-object plugins/plate/skills/eval/SKILL.md`와 같다
- 완료 조건 3이 그대로 참이다.
  - 확인: 완료 조건 3의 확인을 모두 돌린다
- 모든 테스트가 통과하고, 고친 eval 글이 빠지면 그 테스트가 실패한다.
  - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
  - 확인: 새 사본(`mktemp -d`로 만든 폴더에 작업 트리의 `plugins`와 `tests`를 `cp -R`로 복사한 것)마다, eval 본문의 `잡힌 곳이 phase의 확인, task의 회고, tasks 끝인 실패나 멈춤이 근거에 있으면 문턱을 넘는다`를 빈 글로 바꾸고 돌리면 `FAIL: test_threshold_and_disposition (test_skill_rules.EvalRulesTest`가 나온다. `` 코드 평가의 "하네스에서 걸린 것" 가운데 계획의 `돌리지 않음` 줄이 정한 동작 때문에 낮아진 등급만 적은 줄은 실패가 아니다 ``를 빈 글로 바꾸고 돌리면 `FAIL: test_74_untested_lines_not_failures (test_skill_rules.EvalRulesTest`가 나온다. 두 글은 사본에 저마다 한 번 있다
