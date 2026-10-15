# Phase 1: 검증 스킬을 만든다

**목표**: `plate:verify`가 불리고, 검증이 남은 작업 하나를 완료 조건과 작업 전체의 변경에 대어 보고 `verify.md`를 남긴다.

**읽을 것**
- `plugins/plate/skills/retro/SKILL.md` (회고 절의 꼴과 규칙. `verify.md`가 같은 꼴이다)
- `plugins/plate/skills/run/SKILL.md` (낱말, 에이전트에게 넘기는 글의 꼴)
- `~/plate-rail-test/bin/runcheck.py`, `~/plate-rail-test/bin/run.sh` (판정 도구와 실행 스크립트)
- `~/plate-rail-test/run-small/` (완료 조건 1~3의 시작 상태)

**TODO**
- [x] `plate:verify`가 생긴다. 대상 작업을 정하고, 완료 조건의 확인을 모두 직접 돌리고, 작업 전체의 변경을 점검하고, `verify.md`에 `## 검증 N` 절을 더해 그 파일만 커밋하고, 짧은 결과 줄을 돌려준다. 고치지 않고 묻지 않는다 (`plugins/plate/skills/verify/SKILL.md`)
- [x] 시험 폴더 `vf-pass`, `vf-fail`, `vf-scope`가 `run-small`의 끝 상태에서 만들어진다 (`~/plate-rail-test/`)
- [x] `runcheck.py`가 `vf-pass`, `vf-fail`, `vf-scope`를 판정한다 (`~/plate-rail-test/bin/runcheck.py`)
- [x] 세 경우를 헤드리스로 돌려 통과한다

**통과 조건**
- 완료 조건 1, 2, 3, 4가 참이다.
  - 확인: 완료 조건 1, 2, 3, 4의 확인을 돌린다

## 한 일
- `plate:verify`가 생긴다: 검증 스킬의 본문을 retro와 같은 꼴(절대 규칙 다섯, 낱말, 0~7번, 검증 절의 양식, 적는 규칙)로 새로 썼다. 작업의 커밋은 작업 폴더의 파일을 바꾼 커밋과 메시지가 작업 폴더의 이름으로 시작하는 커밋이고, 다른 작업의 이름으로 시작하는 커밋은 뺀다(이 레포의 `005-run: phase 8`이 004의 `plan.md`를 고친 것 때문이다). `verify.md`는 `# 검증` 한 줄로 시작한다 (`plugins/plate/skills/verify/SKILL.md`)
- 시험 폴더 `vf-pass`, `vf-fail`, `vf-scope`: `run-small`의 지금 끝 상태(`de02297`)를 `vf-base`로 복제해 두고 `bin/vfmake.sh`가 그것에서 세 폴더를 다시 만든다. `vf-fail`은 `*.db` 줄을 지워, `vf-scope`는 `*.log`를 더해 커밋했고, 두 메시지는 작업의 커밋으로 보이게 `001-gitignore:`로 시작한다 (`~/plate-rail-test/vf-base/`, `~/plate-rail-test/bin/vfmake.sh`)
- `runcheck.py`가 세 경우를 판정한다: 경우 셋과 `check_verify`(커밋 하나와 그 메시지와 든 파일, git status, 작업 폴더에 남은 파일, `plan.md`가 그대로인지, 메인이 고친 파일, 묻는 도구), `check_verify_text`(첫 줄, 절 번호, 다섯 항목의 순서, 완료 조건마다의 항목과 확인마다의 결과 줄, 판정, 문제의 기준)를 더했다. 손으로 쓴 표본으로 통과와 실패를 가르는 것을 먼저 봤다. `run.sh`의 허용 목록 갈래에 `verify`를 더했다 (`~/plate-rail-test/bin/runcheck.py`, `~/plate-rail-test/bin/run.sh`)
- 세 경우를 헤드리스로 돌려 통과한다: 2.1.300에서 셋을 한꺼번에 돌렸다. `vf-pass` 44초, `vf-fail` 63초, `vf-scope` 179초 (`~/plate-rail-test/logs/vf-*.jsonl`)

## 확인 결과
- 완료 조건 1, 2, 3, 4가 참이다.
  - `runcheck.py vf-pass` → 모두 통과. 판정 "통과", 확인 셋 모두 통과, 커밋 `001-gitignore: 검증`에 `verify.md`만 들었다. 통과
  - `runcheck.py vf-fail` → 모두 통과. 실패한 확인 둘이 문제에 기준 "확인 실패"로 적혔고, `*.db` 줄을 지운 커밋이 기준 "계획"으로 더 적혔다. 판정 "문제 있음". 통과
  - `runcheck.py vf-scope` → 모두 통과. 확인 셋이 모두 통과하고 `*.log`를 더한 커밋이 기준 "범위"로 적혔다. 판정 "문제 있음". 통과
  - `claude -p ok --plugin-dir plugins/plate --output-format stream-json --verbose`의 init 줄 → `plate:setup`, `plate:context`, `plate:plan`, `plate:run`, `plate:phase`, `plate:retro`, `plate:verify`가 모두 있다. init 줄은 첫 줄이 아니라 훅 줄들 뒤에 있다. 통과

## 계획과 달라진 점
- TODO 둘째는 시험 폴더를 `run-small`의 끝 상태에서 만든다고 적었다. 그 상태를 `vf-base`로 복제해 두고 거기서 만든다. 까닭: phase 3이 `run-small`을 다시 돌려 끝 상태가 바뀌고, phase 2의 `run-verify`가 같은 시작 상태를 쓴다.
- TODO에 없던 `run.sh`를 고쳤다. 까닭: 스킬 이름에 따라 허용 목록을 붙이는데, `verify`가 없으면 `git add`와 `git commit`이 막힌다.

## 남은 것
없음

## 하네스에서 걸린 것
- verify 본문 4번의 "어느 스킬의 어느 규칙인지를 적는다"를 따르려고 `vf-scope`의 검증이 프로젝트 밖의 `plugins/plate/skills/plan/SKILL.md`를 두 번 읽으려다 막혀, 실행이 179초로 늘었다(다른 둘은 44초, 63초). retro의 점검 에이전트와 같은 일이다(`docs/TOOLS.md`의 "에이전트는 프로젝트 폴더 밖의 파일을 읽지 못한다").
