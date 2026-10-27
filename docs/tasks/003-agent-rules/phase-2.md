# Phase 2: 고친 retro, eval, phase를 네 장면으로 돌린다

**목표**: 장면 R, E, P1, P2를 임시 복제본에서 돌린 결과가 `docs/TOOLS.md`의 새 절에 남고, 저마다 기대와 같다.

**테스트 먼저**: 아니오 — 이 phase는 스킬을 돌려 본 결과를 `docs/TOOLS.md`에 적기만 한다

**읽을 것**
- `plugins/plate/skills/retro/SKILL.md`, `plugins/plate/skills/eval/SKILL.md`, `plugins/plate/skills/phase/SKILL.md` (phase 1이 고친 본문. 장면의 대상이고, 돌릴 때 이 셋의 `git hash-object`를 적는다)
- `plugins/plate/skills/run/SKILL.md`의 4번, 7번, "하네스 eval을 맡긴다" 코드 블록 (장면의 프롬프트로 옮길 맡기는 글. 001이 마지막 줄 `부른 쪽: plate:run`을 더했다)
- `docs/TOOLS.md`의 "스킬을 헤드리스로 돌려 볼 때의 허용 목록"의 "차림에서 지킬 것"과 "description을 줄이고 `docs/TOOLS.md` 커밋 규칙을 한 곳에 모은 run을 장면 A~D로 다시 돌려 본 것" (차림의 사실과 장면 절의 꼴)
- `git show 44f2790^:docs/tasks/002-plan-phase-rules/done-phase-1.md`, `done-phase-2.md`, `done-phase-3.md` (장면 R의 자료. 확인 절의 `남은 것:` 줄 다섯), `git show 44f2790 -- docs/tasks/FRICTION.md` (지난 회고가 `문제`로 넣은 줄)
- `git show f080761:docs/tasks/eval.md` (장면 E의 자료로 돈 지난 eval이 "하네스에서 걸린 것"에 적은 두 줄)

**TODO**
- [ ] phase 1의 산출물에 대어 장면의 조건을 맞춘다: 고친 retro, eval, phase 본문과 run의 맡기는 글을 읽어, task 머리 결정의 장면 프롬프트와 기대가 그 글과 맞는지 본다. 맞지 않으면 장면을 돌리지 않고 "계획이 틀림"으로 돌아온다 (읽기만 한다)
- [ ] task 머리 결정의 공통 차림과 장면 R, E, P1, P2의 차림대로 장면 넷이 돌고, `docs/TOOLS.md`의 "Claude Code" 절 끝(Codex 절 앞)에 "고친 retro·eval·phase를 장면 R·E·P1·P2로 돌려 본 것" 절이 더해진다. 절 머리에 Claude Code 버전, 돌린 날, 공통 차림, 돌리기 전과 뒤의 원본 `git rev-parse HEAD`와 `git status --short`가 있다. 장면마다 명령, 돌린 시각과 `duration_ms`, 세션 id, 복제본과 기록 경로, 대상 본문 해시, 차림, 기대한 결과, 본 결과, 막힌 명령이 있다 (`docs/TOOLS.md`)

**통과 조건**
- 완료 조건 4가 참이다
  - 확인: `docs/TOOLS.md`의 새 장면 절을 읽어 장면 R, E, P1, P2마다 Claude Code 버전, 돌린 시각, 세션 id, 대상 본문 해시, 차림, 기대한 결과, 본 결과, 막힌 명령이 있고, 본 결과가 task 머리 결정의 기대와 같다. 하나라도 빠지거나 다르면 실패
  - 확인: 장면마다 적힌 본문 해시가 `git rev-parse HEAD:plugins/plate/skills/<retro|eval|phase>/SKILL.md`와 같다
  - 확인: 절 머리에 적힌, 돌리기 전과 뒤의 원본 `git rev-parse HEAD`가 같고 `git status --short`의 출력이 같다
- 완료 조건 3이 이 phase의 커밋 뒤에도 참이다
  - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
