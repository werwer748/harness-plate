# Phase 1: 검증 스킬을 만든다

**목표**: `plate:verify`가 불리고, 검증이 남은 작업 하나를 완료 조건과 작업 전체의 변경에 대어 보고 `verify.md`를 남긴다.

**읽을 것**
- `plugins/plate/skills/retro/SKILL.md` (회고 절의 꼴과 규칙. `verify.md`가 같은 꼴이다)
- `plugins/plate/skills/run/SKILL.md` (낱말, 에이전트에게 넘기는 글의 꼴)
- `~/plate-rail-test/bin/runcheck.py`, `~/plate-rail-test/bin/run.sh` (판정 도구와 실행 스크립트)
- `~/plate-rail-test/run-small/` (완료 조건 1~3의 시작 상태)

**TODO**
- [ ] `plate:verify`가 생긴다. 대상 작업을 정하고, 완료 조건의 확인을 모두 직접 돌리고, 작업 전체의 변경을 점검하고, `verify.md`에 `## 검증 N` 절을 더해 그 파일만 커밋하고, 짧은 결과 줄을 돌려준다. 고치지 않고 묻지 않는다 (`plugins/plate/skills/verify/SKILL.md`)
- [ ] 시험 폴더 `vf-pass`, `vf-fail`, `vf-scope`가 `run-small`의 끝 상태에서 만들어진다 (`~/plate-rail-test/`)
- [ ] `runcheck.py`가 `vf-pass`, `vf-fail`, `vf-scope`를 판정한다 (`~/plate-rail-test/bin/runcheck.py`)
- [ ] 세 경우를 헤드리스로 돌려 통과한다

**통과 조건**
- 완료 조건 1, 2, 3, 4가 참이다.
  - 확인: 완료 조건 1, 2, 3, 4의 확인을 돌린다
