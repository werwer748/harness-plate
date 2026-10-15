# Phase 3: 브랜치와 합치기

**목표**: run이 기본 브랜치에서 시작하면 작업 브랜치에서 실행하고, 검증을 통과한 작업만 합칠지 묻는다.

**읽을 것**
- `plugins/plate/skills/run/SKILL.md` (시작 조건, 합친다)
- `~/plate-rail-test/plan-base/` (run-small, run-all의 시작 상태)
- `~/plate-rail-test/answers/run-wt-*.md`, `~/plate-rail-test/bin/runcheck.py`

**TODO**
- [ ] run이 기본 브랜치에서 시작하면 `task/NNN-slug`를 만들어 바꾸고 실행한다. 기본 브랜치가 아니면 만들지 않는다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] 검증이 통과하면 run이 합칠 브랜치와 합칠 곳을 보여 주고 합칠지 묻는다. 전체 지시여도 묻는다. worktree가 없어도 "합친다" 절차로 합치고 브랜치를 지운다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] worktree의 합치기는 판정이 통과인 `verify.md`가 있을 때만 묻고, 없으면 worktree에서 run을 부르라고 안내한다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] `runcheck.py`의 `run-small`, `run-all`, `run-wt` 기대가 새 동작으로 바뀌고 `run-wt-gate`를 판정한다 (`~/plate-rail-test/bin/runcheck.py`)
- [ ] 네 경우를 헤드리스로 돌려 통과한다

**통과 조건**
- 완료 조건 9, 10, 11이 참이다.
  - 확인: 완료 조건 9, 10, 11의 확인을 돌린다
