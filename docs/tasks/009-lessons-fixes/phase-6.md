# Phase 6: 006의 실행 시험 여섯을 다시 돌린다

**목표**: 006의 실행 시험 여섯이 바뀐 본문으로 다시 돌아 `runcheck.py`에 실패한 항목이 없다.

**테스트 먼저**: 아니오 — 이 레포의 코드를 바꾸지 않고 시험 폴더에서 시험을 돌린다

**읽을 것**
- `~/plate-rail-test/bin/vfmake.sh`, `bin/rerun.sh`, `bin/run.sh`, `bin/runcheck.py` (시험 폴더를 만들고, 돌리고, 판정하는 도구)
- `~/plate-rail-test/answers/` (시험마다 미리 주는 답)
- `git show a0be6c4^:docs/tasks/006-verify/plan.md`의 완료 조건 7~11 (여섯 시험이 보는 것과 run-wt-gate를 만드는 꼴)
- `git show ec2f192:docs/LESSONS.md`의 미룬 문제 절 (006-verify, 검증 1)의 네 줄과, 프로젝트에서 배운 것 절의 (006-verify, 검증 1) 줄
- `docs/TOOLS.md`의 Claude Code 절 (헤드리스 실행의 꼴, 허용 목록, 실행 시간, 폴더가 다르면 한꺼번에 돌려도 된다)
- `plugins/plate/skills/run/SKILL.md` (phase 4가 바꾼 0번, "통과하면", "고칠 phase를 더한다", "`docs/LESSONS.md`" 절)

**TODO**
- [ ] run-vrule, run-nogit, run-small, run-all이 `bin/vfmake.sh`로 다시 만들어지고 바뀐 본문으로 돌아 `runcheck.py`에 실패한 항목이 없다. 옛 셋업을 바탕으로 한 폴더가 LESSONS의 위치를 물으면 `docs/LESSONS.md`로 답하는 턴을 잇는다 (`~/plate-rail-test/`)
- [ ] run-wt와 run-wt-gate가 다시 만들어지고 돌아 `runcheck.py`에 실패한 항목이 없다. run-wt는 worktree에서 검증이 닫힌 뒤 원래 자리에서 부르면 합칠지 묻고, run-wt-gate는 worktree에 닫힌 검증이 없어 그 worktree에서 run을 부르라고 안내한다 (`~/plate-rail-test/`)
- [ ] `runcheck.py`의 기대 가운데 이 작업의 결정이 바꾼 동작(`verify.md`의 `LESSONS로 옮겼다` 줄, 고칠 phase 양식, 0번의 worktree 갈래)에 걸리는 것만 고쳐지고, 고친 곳과 까닭이 phase 기록에 적힌다 (`~/plate-rail-test/bin/runcheck.py`)

**통과 조건**
- 완료 조건 9가 참이다.
  - 확인: 완료 조건 9의 확인을 모두 돌린다
