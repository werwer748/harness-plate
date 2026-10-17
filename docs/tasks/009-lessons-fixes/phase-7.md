# Phase 7: 시험으로만 닫히는 셋과 LESSONS 정리

**목표**: 시험으로만 닫히는 셋이 확인되어 `docs/TOOLS.md`에 적히고, `docs/LESSONS.md`에서 이 작업이 닫은 41줄이 지워진다.

**테스트 먼저**: 아니오 — 이 레포의 코드를 바꾸지 않고 시험을 돌리고 문서를 고친다

**읽을 것**
- `~/plate-rail-test/bin/vfmake.sh`, `bin/run.sh`, `bin/rerun.sh`
- `~/plate-rail-test/probe-plugin`과 `bin/a2.sh` (헤드리스에서 서브에이전트가 스킬을 부르는 시험의 꼴. `docs/TOOLS.md`의 "서브에이전트, 권한, worktree")
- `plugins/plate/skills/run/SKILL.md`의 3번(세 번째 막음 갈래)과 "`docs/LESSONS.md`" 절의 문서 지도(다른 위치)
- `plugins/plate/skills/phase/SKILL.md`의 2번과 적는 규칙(세 번째 막음 줄)
- `plugins/plate/hooks/edit_guard.py` (테스트 파일의 기준과 막은 횟수를 두는 곳. phase 1이 바꿨다)
- `docs/TOOLS.md`의 Claude Code 절
- code.claude.com/docs/en/skills, code.claude.com/docs/en/plugins/cli-reference (스킬 본문은 부를 때 대화에 한 번 들어가고 다시 읽히지 않는다. `/reload-plugins`는 디스크에서 고친 플러그인을 세션에 다시 싣는다)
- `git show ec2f192:docs/LESSONS.md` (지울 41줄의 원문. 하네스의 문제점 절의 (007-harness-issues, 검증 2) 줄, (008-tdd, phase 3)의 넷째 줄, (008-tdd, phase 4)의 셋째 줄, (008-tdd, 검증 1)의 둘째 줄이 이 phase가 시험으로 닫는 것이다)

**TODO**
- [ ] `~/plate-rail-test/run-oldsetup`이 다시 만들어지고, `/plate:run 001`의 첫 턴이 LESSONS의 위치를 묻고 멈춘 뒤, `docs/notes/lessons.md`로 답한 둘째 턴에서 완료 조건 10대로 된다 (`~/plate-rail-test/run-oldsetup`)
- [ ] `~/plate-rail-test/tdd-stop`이 완료 조건 11의 꼴로 생기고, `/plate:run`을 헤드리스로 한 턴 돌린 기록 `logs/tdd-stop.jsonl`에서 완료 조건 11대로 된다 (`~/plate-rail-test/tdd-stop`)
- [ ] `probe-plugin`으로 세션 도중의 본문 고침과 `/reload-plugins`를 헤드리스로 시험한 기록이 `logs/reload-probe*.jsonl`에 있고, 그 결과(두 에이전트가 받은 본문, 돌린 명령의 꼴, 버전, 날짜)가 `docs/TOOLS.md`의 Claude Code 절에 적힌다 (`docs/TOOLS.md`)
- [ ] `docs/LESSONS.md`에서 완료 조건 13의 41줄이 지워진다. 이 작업의 phase가 통과할 때 run이 더한 줄과 다른 줄은 그대로다 (`docs/LESSONS.md`)

**통과 조건**
- 완료 조건 10이 참이다.
  - 확인: 완료 조건 10의 확인을 모두 돌린다
- 완료 조건 11이 참이다.
  - 확인: 완료 조건 11의 확인을 모두 돌린다
- 완료 조건 12가 참이다.
  - 확인: 완료 조건 12의 확인을 돌린다
- 완료 조건 13이 참이다.
  - 확인: 완료 조건 13의 확인을 모두 돌린다
- 완료 조건 8이 참이다. 이 phase가 `docs/TOOLS.md`를 고친다.
  - 확인: 완료 조건 8의 확인을 모두 돌린다
- 완료 조건 15가 참이다.
  - 확인: 완료 조건 15의 확인을 돌린다
