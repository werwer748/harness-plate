# Phase 2: run이 검증으로 잇는다

**목표**: run이 검증이 남은 작업을 알아보고 검증 에이전트에게 맡기며, 결과에 따라 LESSONS로 옮기거나 고칠 phase의 안을 승인받는다.

**읽을 것**
- `plugins/plate/skills/run/SKILL.md` (상태 표, 계획을 고친다, LESSONS 절)
- `plugins/plate/skills/verify/SKILL.md` (phase 1의 결과. 돌려주는 줄)
- `~/plate-rail-test/vf-fail/`, `~/plate-rail-test/run-rule/`, `~/plate-rail-test/run-nogit/` (시작 상태)
- `~/plate-rail-test/bin/runcheck.py`, `~/plate-rail-test/bin/run.sh`, `~/plate-rail-test/bin/rerun.sh`

**TODO**
- [ ] run이 "검증이 남은 작업"을 알아보고(0번의 대상 찾기, 2번의 상태 표), 남은 phase가 없으면 묻지 않고 새 에이전트에게 검증을 맡긴다. 그 에이전트는 수행·점검한 에이전트와 다르다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] 검증이 통과하면 run이 `verify.md`의 배운 것과 하네스의 문제점을 `docs/LESSONS.md`로 옮기고, git 레포가 아니면 `done-phase-N.md`를 지운다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] 검증이 "문제 있음"이면 run이 문제 목록을 TODO로 담은 새 `phase-M.md`의 안을 보여 주고 멈추며, 승인 뒤 계획 파일만 커밋하고 그 phase를 수행에 맡긴다. 전체 지시여도 멈춘다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] `runcheck.py`가 `run-verify`, `run-vfix`, `run-vrule`을 판정하고, `run-nogit`의 기대가 새 동작으로 바뀐다 (`~/plate-rail-test/bin/runcheck.py`)
- [ ] 네 경우를 헤드리스로 돌려 통과한다

**통과 조건**
- 완료 조건 5, 6, 7, 8이 참이다.
  - 확인: 완료 조건 5, 6, 7, 8의 확인을 돌린다
