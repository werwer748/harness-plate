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
- [x] 앞 phase의 산출물(run의 "BACKLOG를 고친다" 절의 세 절과 항목 꼴)에 대어 시험 저장소의 `docs/BACKLOG.md` 차림을 맞춘다 (시험 저장소)
- [x] 1번 "읽는다"에 `` `docs/BACKLOG.md`의 하네스 고칠 거리와 감수한 것 ``이 더해진다 (`plugins/plate/skills/eval/SKILL.md`)
- [x] 2번 예외 목록에 `` 코드 평가의 "하네스에서 걸린 것" 가운데 계획의 `돌리지 않음` 줄이 정한 동작 때문에 낮아진 등급만 적은 줄은 실패가 아니다 ``가 더해진다 (`plugins/plate/skills/eval/SKILL.md`)
- [x] 5번에 `처리는 규칙을 더하거나 고친다, 규칙을 지운다, 감수한다 가운데 하나다`, `잡힌 곳이 phase의 확인, task의 회고, tasks 끝인 실패나 멈춤이 근거에 있으면 문턱을 넘는다`, `` `docs/BACKLOG.md`의 하네스 고칠 거리에 같은 뜻의 항목이 있으면 문턱을 넘는다 ``, `` `docs/BACKLOG.md`의 감수한 것과 같은 뜻이면 고칠 거리로 적지 않는다 ``, `이슈 제목과 본문은 문턱을 넘었고 처리가 감수가 아닌 plate 자체의 것에만 적는다`가 들고, 옛 글 `plate 자체의 것에는 이슈로 올릴 제목과 본문을 적는다`가 지워진다. 기록의 양식의 하네스 고칠 거리 항목에 `   - 처리: {규칙을 더하거나 고친다 | 규칙을 지운다 | 감수한다}`(까닭과 함께)와 `   - 문턱: {넘음 | 넘지 않음}`(근거와 함께, plate 자체의 것에만) 줄이 더해진다 (`plugins/plate/skills/eval/SKILL.md`)
- [x] `EvalRulesTest`에 `test_threshold_and_disposition`(5번의 다섯 글과 양식의 두 줄)과 `test_74_untested_lines_not_failures`(2번의 글)가 더해진다 (`tests/test_skill_rules.py`)
- [x] 헤드리스 시험을 한다. task 머리의 결정대로 시험 저장소를 차린다: `AGENTS.md`(문서 지도와 `docs/tasks/` 행), tasks 머리, task 폴더 하나(task 머리, `done-phase-1.md`, `retro.md`), `FRICTION.md`, `RUNLOG.md`, `review.md`, 세 절의 `docs/BACKLOG.md`, 스킬의 꼴대로의 커밋. 기록에 다섯 실패를 둔다: (가) 확인 절의 실패로 잡힌 plate 자체의 것, (나) 그 자리에서만 적혔고 BACKLOG의 하네스 고칠 거리에 같은 뜻의 항목이 있는 것, (다) 그 자리에서만 적혔고 BACKLOG에 같은 것이 없는 것, (라) BACKLOG의 감수한 것과 같은 뜻인 것, (마) `review.md`의 "하네스에서 걸린 것"에 계획의 `돌리지 않음` 결정 때문에 테스트 적절성이 낮아졌다고만 적은 줄. `/plate:eval`을 돌려 더해진 `eval.md`를 읽는다. 차림, 출력, 돌릴 때의 `git hash-object plugins/plate/skills/eval/SKILL.md`를 기록의 "한 일"에 남긴다 (시험 저장소, 이 phase의 기록)

**통과 조건**
- 완료 조건 1과 2가 참이다.
  - 확인: `grep -cF -e '<글>' plugins/plate/skills/eval/SKILL.md`를 TODO의 새 글 여덟마다 돌리면 저마다 `1`이고, 옛 글은 `0`이다
  - 확인: 헤드리스 시험의 `eval.md`에서 (가)와 (나)의 고칠 거리는 `문턱: 넘음`이고 이슈 제목이 있고, (다)는 `문턱: 넘지 않음`이고 이슈 제목이 없고, (라)는 고칠 거리에 없고, (마)는 "실패"에 없다. 고칠 거리마다 `처리:` 줄이 있다. 기록에 적은 본문 해시가 지금 작업 트리에서 다시 낸 `git hash-object plugins/plate/skills/eval/SKILL.md`와 같다
- 완료 조건 3이 그대로 참이다.
  - 확인: 완료 조건 3의 확인을 모두 돌린다
- 모든 테스트가 통과하고, 고친 eval 글이 빠지면 그 테스트가 실패한다.
  - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
  - 확인: 새 사본(`mktemp -d`로 만든 폴더에 작업 트리의 `plugins`와 `tests`를 `cp -R`로 복사한 것)마다, eval 본문의 `잡힌 곳이 phase의 확인, task의 회고, tasks 끝인 실패나 멈춤이 근거에 있으면 문턱을 넘는다`를 빈 글로 바꾸고 돌리면 `FAIL: test_threshold_and_disposition (test_skill_rules.EvalRulesTest`가 나온다. `` 코드 평가의 "하네스에서 걸린 것" 가운데 계획의 `돌리지 않음` 줄이 정한 동작 때문에 낮아진 등급만 적은 줄은 실패가 아니다 ``를 빈 글로 바꾸고 돌리면 `FAIL: test_74_untested_lines_not_failures (test_skill_rules.EvalRulesTest`가 나온다. 두 글은 사본에 저마다 한 번 있다

## 한 일
- 앞 phase의 산출물에 대어 시험 저장소의 `docs/BACKLOG.md` 차림을 맞춘다: run의 "BACKLOG를 고친다" 절의 양식대로 세 절(`## 소스 문제`, `## 하네스 고칠 거리`, `## 감수한 것`)과 항목 꼴(갈래, 처리, 나온 tasks, 다시 나오지 않은 tasks / 까닭)로 시험 저장소의 BACKLOG를 썼다 (시험 저장소)
- 1번 "읽는다"에 `` `docs/BACKLOG.md`의 하네스 고칠 거리와 감수한 것 ``을 더했다(없으면 없다고 적는다) (`plugins/plate/skills/eval/SKILL.md`)
- 2번 예외 목록에 #74의 글을 더했다. 뒤에 "계획이 돌리지 않기로 정한 것이라 하네스가 틀리거나 걸린 것이 아니다"를 붙였다 (`plugins/plate/skills/eval/SKILL.md`)
- 5번: 감수한 것과 같은 뜻이면 적지 않는다(같은 뜻의 정의, 적지 않은 것은 "하네스에서 걸린 것"에 적는다), 처리 셋과 감수를 고르는 때, 문턱 둘(잡힌 곳, BACKLOG)과 "둘 다 아니면 넘지 않는다", BACKLOG로만 보고 GitHub은 보지 않는다, 이 프로젝트만의 것에는 문턱이 없다, 이슈 제목과 본문은 문턱을 넘었고 처리가 감수가 아닌 plate 자체의 것에만 적는다를 넣고 옛 글을 지웠다. 기록의 양식의 plate 자체 항목에 `   - 처리: {규칙을 더하거나 고친다 | 규칙을 지운다 | 감수한다} — {까닭}`과 `   - 문턱: {넘음 | 넘지 않음} — {근거}`를, 이 프로젝트만 항목에 `   - 처리: {plate 자체의 것과 같은 셋 가운데 하나} — {까닭}`을 더했다. 적는 규칙에 이슈 두 줄은 문턱 넘음이고 감수가 아닌 것에만 둔다는 줄을 더했다. 앞머리 description의 "(plate 자체의 것에는 이슈 제목과 본문)"을 "(처리와, 문턱을 넘은 plate 자체의 것에는 이슈 제목과 본문)"으로 바꿨다(547자) (`plugins/plate/skills/eval/SKILL.md`)
- `EvalRulesTest`에 `test_threshold_and_disposition`(5번의 다섯 글, 옛 글 없음, 양식의 두 줄, 1번의 글)과 `test_74_untested_lines_not_failures`(2번의 글)를 더하고, 머리 docstring의 eval 이슈 목록에 `#74`를 더했다 (`tests/test_skill_rules.py`)
- 헤드리스 시험을 한다:
  - 차림: `mktemp -d`로 만든 `…/scratchpad/evaltest.pKl7`에 `git init`(main). `AGENTS.md`(문서 지도: ARCHITECTURE, BACKLOG, `docs/tasks/` 행), `docs/ARCHITECTURE.md`(명령 절), `greet.py`, 세 절의 `docs/BACKLOG.md`(하네스 고칠 거리: plan 스킬이 읽을 것에 `docs/TOOLS.md`를 넣게 하지 않음, 나온 tasks `hello` / 감수한 것: phase 스킬이 빈 절에도 "없음"을 적게 해 기록이 길어짐)를 `init`으로 커밋. 그 뒤 `plan: greet`(tasks 머리 `**이름**: greet`, 완료 조건 2에 `돌리지 않음` 줄, task 머리, `phase-1.md`), `tasks/greet` 브랜치에서 `001-greet: phase 1`, `001-greet: phase 1 확인`(확인 1 실패), `001-greet: phase 1 고침`, `001-greet: phase 1 확인`(확인 2 통과), `001-greet: phase 1 통과`(이름 바꾸기와 `RUNLOG.md`), `001-greet: 회고`(`retro.md`, `FRICTION.md`), `001-greet: RUNLOG`, `greet: 코드 평가`(`review.md`), `greet: RUNLOG`
  - 다섯 실패: (가) 확인 1의 "실패": phase 스킬의 기록 양식 때문에 통과 조건의 하위 확인을 빠뜨림. (나) 기록의 "하네스에서 걸린 것": plan 스킬이 읽을 것에 `docs/TOOLS.md`를 넣게 하지 않음(BACKLOG 하네스 고칠 거리와 같은 뜻). (다) 확인 2의 "하네스에서 걸린 것": check 스킬의 확인 절 번호 규칙이 적는 규칙 끝에 있음(BACKLOG에 없음). (라) 기록의 "하네스에서 걸린 것": phase 스킬이 빈 절에도 "없음"을 적게 해 기록이 길어짐(BACKLOG 감수한 것과 같은 뜻). (마) `review.md`의 "하네스에서 걸린 것": 완료 조건 2의 `돌리지 않음` 결정으로 테스트 적절성이 B로 낮아졌다는 줄
  - 명령: 시험 저장소에서 `claude -p "/plate:eval" --plugin-dir /Users/hugo/Desktop/harness-plate/plugins/plate --permission-mode bypassPermissions` (Claude Code 2.1.312). 첫 판(본문 해시 `5ae5a34…`)으로 한 번 돌린 뒤, 통과 조건의 grep 때문에 본문을 고쳐 `git reset --hard 57e6da2`로 되돌리고 고친 판으로 다시 돌렸다. 아래는 다시 돌린 것이다
  - 돌릴 때의 `git hash-object plugins/plate/skills/eval/SKILL.md`: `6d5fdd8ca384116079edbd4d261c0cc7829ad092`
  - 출력: `등급: 결과 성공 A, 일관성 D, 효율 C, 규칙 준수 A, 사람 개입률 A, 실패 양상 B` / `고칠 거리: plate 자체 3개, 이 프로젝트만 1개` / `기록: docs/tasks/eval.md`(커밋 `22593d3 greet: 하네스 eval`, `eval.md` 하나만)
  - `eval.md`의 실패: 1 plan/`docs/TOOLS.md`(그 자리), 2 phase의 "없음"(그 자리), 3 하위 확인 빠뜨림(phase의 확인), 4 check 번호 규칙(그 자리). (마)는 실패에 없다
  - `eval.md`의 하네스 고칠 거리: 1 plan/`docs/TOOLS.md` — `처리: 규칙을 더하거나 고친다`, `문턱: 넘음 — docs/BACKLOG.md 하네스 고칠 거리의 … 항목`, 이슈 제목 있음 (나). 2 phase 확인 결과 대조 — `처리: 규칙을 더하거나 고친다`, `문턱: 넘음 — 실패 3(잡힌 곳: phase의 확인)`, 이슈 제목 있음 (가). 3 check 번호 규칙 — `처리: 규칙을 더하거나 고친다`, `문턱: 넘지 않음 — 둘 다 없음`, 이슈 제목 없음 (다). 4 측정 도구 없음 — 갈래 이 프로젝트만, `처리: 감수한다`. (라)는 고칠 거리에 없고 "하네스에서 걸린 것"에 "BACKLOG 감수한 것의 … 항목과 같은 뜻이라 고칠 거리로 적지 않았다"로 적혔다. "하네스에서 걸린 것"에 (마)를 "eval 스킬 2번의 규칙대로 `돌리지 않음` 줄로 보고 실패로 세지 않았다"고 적었다

## 확인 결과
- 완료 조건 1과 2가 참이다.
  - `grep -cF -e '<글>' plugins/plate/skills/eval/SKILL.md`를 새 글 여덟과 2번의 글마다 → 모두 `1`. 옛 글 `plate 자체의 것에는 이슈로 올릴 제목과 본문을 적는다` → `0`. 통과
  - 헤드리스 시험의 `eval.md`(위 "한 일") → (가)·(나)는 `문턱: 넘음`과 이슈 제목, (다)는 `문턱: 넘지 않음`이고 이슈 제목 없음, (라)는 고칠 거리에 없음, (마)는 "실패"에 없음, 고칠 거리 넷 모두 `처리:` 줄 있음. 기록의 해시 `6d5fdd8ca384116079edbd4d261c0cc7829ad092`와 지금 `git hash-object plugins/plate/skills/eval/SKILL.md` → 같다. 통과
- 완료 조건 3이 그대로 참이다.
  - 완료 조건 3의 새 글 열셋 `grep -cF -e` → 모두 `1`. 세 절 머리 `grep -cxF -e` → 모두 `1`. 옛 글 셋 → 모두 `0`. `grep -cE '^   - BACKLOG로 미룰 것: 소스 문제의 번호$'` → `0`. 통과
- 모든 테스트가 통과하고, 고친 eval 글이 빠지면 그 테스트가 실패한다.
  - `python3 -m unittest discover -s tests` → 마지막 줄 `OK`(202 tests). 통과
  - 새 사본마다(`mktemp -d`에 `plugins`, `tests`를 `cp -R`) 글이 1번 있음을 보고 빈 글로 바꿔 돌림 → 문턱 글: `FAIL: test_threshold_and_disposition (test_skill_rules.EvalRulesTest) (phrase='잡힌 곳이 …')`. #74 글: `FAIL: test_74_untested_lines_not_failures (test_skill_rules.EvalRulesTest)`. 통과

## 계획과 달라진 점
- 이 프로젝트만 항목의 처리 줄: TODO는 양식의 하네스 고칠 거리 항목에 처리 줄을 더하라고 했고 결정은 두 갈래 모두 처리를 적게 했다. 두 항목에 같은 줄을 두면 통과 조건의 `grep -cF`가 `2`가 되어, 이 프로젝트만 항목은 `   - 처리: {plate 자체의 것과 같은 셋 가운데 하나} — {까닭}`으로 적었다
- TODO에 없던 것: 앞머리 description을 새 규칙에 맞췄고, 적는 규칙에 이슈 두 줄을 두는 때를 한 줄 더했고, 5번에 감수와 같은 뜻의 정의와 적지 않은 것을 "하네스에서 걸린 것"에 적는 줄을 더했고, 테스트 docstring에 `#74`를 더했다(완료 조건 4가 보는 줄). 바뀐 규칙과 본문이 어긋나지 않게 하려는 것이다
- 헤드리스 시험을 두 번 돌렸다. 첫 판 뒤 본문을 고쳐 해시가 바뀌었기 때문이다. 첫 판의 결과도 다섯 갈래가 같았다

## 남은 것
- (라)를 걸러 낸 것은 이 시험의 한 가지 꼴(BACKLOG의 글과 거의 같은 글)에서만 봤다. 글이 많이 다른 같은 뜻의 것을 가르는지는 보지 않았다
- 시험 저장소의 `review.md`에서 (마)의 줄과 테스트 적절성 근거(`greet.py:3` 인자 없는 갈래)가 서로 맞지 않았고, eval이 이를 "하네스에서 걸린 것"에 적었다. 시험 차림의 흠이고 (마)의 판정에는 영향이 없었다

## 하네스에서 걸린 것
- 시험 저장소의 확인 절과 RUNLOG 꼴을 맞추려고 `docs/tasks/001-eval-threshold/done-phase-1.md`의 머리 다섯 줄과 절 제목 줄(`grep -n`)을 봤다. phase 스킬 1번은 앞 phase의 기록을 읽지 않게 한다. 꼴은 check·retro·review·run 본문의 양식에서 다시 가져왔다
- phase-2의 통과 조건(처리 줄 `grep -cF`가 `1`)과 결정(두 갈래 모두 처리를 적는다)이 양식에서 두 항목에 같은 줄을 둘 수 없게 해, 이 프로젝트만 항목의 처리 줄 꼴을 바꿨다
