# Phase 2: 회고 1의 문제를 고친다

**목표**: 회고 1에서 나온 문제를 모두 고친다.

**테스트 먼저**: 아니오 — 고칠 것이 모두 `.md`(스킬 본문, 맥락 문서)다

**읽을 것**
- `docs/tasks/003-fixes/retro.md`의 `## 회고 1` 절
- `docs/ADR.md` (ADR-026의 결정)
- `docs/PRD.md` (핵심 기능 8번)
- `plugins/plate/skills/run/SKILL.md` ("보고하고 묻는다"의 "고칠 곳을 말하면" 줄과 "아무것도 고치지 않고 올리지 않겠다고 하면" 줄)
- `tests/test_skill_rules.py` (`RunRulesTest`에서 "고침 task에서 뺀 소스 문제와 이 프로젝트만의 하네스 고칠 거리는 BACKLOG로 미룰 것으로 옮긴다"와 "고침 task에 두었던 이 프로젝트만의 하네스 고칠 거리도 BACKLOG로 미룰 것에 둔다"를 보는 테스트)
- `docs/ARCHITECTURE.md`, `docs/TOOLS.md`, `docs/BACKLOG.md` (맥락 문서)

**TODO**
- [x] ADR-026 결정과 PRD 8번이 run의 "보고하고 묻는다"와 `docs/ARCHITECTURE.md` 78줄에 더해진 두 동작(사용자가 고치거나 올리자고 하면 eval에만인 것을 갈래대로 옮긴다, 고칠 안이 모두 비면 묻지 않는다)을 적지 않아 "어디에도 두지 않는다"로 남는다. 두 문서의 그 줄이 고친 동작과 맞게 한다 (`docs/ADR.md`, `docs/PRD.md`)
- [x] 사용자가 고침 task나 이슈로 올릴 것으로 옮긴 eval에만인 하네스 고칠 거리를 다시 빼거나 "아무것도 고치지 않겠다"고 하면, run "보고하고 묻는다"의 "뺀 것은 BACKLOG로 미룰 것으로 옮긴다"와 "고침 task에 두었던 이 프로젝트만의 하네스 고칠 거리도 BACKLOG로 미룰 것에 둔다"에 걸려 기준이 eval에만인 것이 BACKLOG로 간다. 기준이 eval에만인 것은 빼면 eval에만으로 돌아가게 한다. 그 동작을 적은 `docs/ARCHITECTURE.md`의 tasks 끝 줄과, 위 두 글을 지키는 테스트가 고친 글을 지키게 한다 (`plugins/plate/skills/run/SKILL.md`, `docs/ARCHITECTURE.md`, `tests/test_skill_rules.py`)

**통과 조건**
- 회고 1의 문제가 모두 고쳐졌다.
  - 확인: TODO에 넣은 문제마다 적힌 곳(ADR-026 결정, PRD 8번, run "보고하고 묻는다"의 두 줄)과 그 동작을 적은 `docs/ARCHITECTURE.md`의 tasks 끝 줄을 다시 읽고, 걸린 테스트(`python3 -m unittest discover -s tests`)를 돌린다
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다

## 한 일
- ADR-026 결정과 PRD 8번을 고친 동작과 맞춘다: ADR-026 결정의 "run은 그것을 고침 task, 이슈, BACKLOG, 감수 어디에도 두지 않는다." 뒤에 사용자가 고치거나 올리자고 하면 이 프로젝트만의 것은 고침 task로, plate 자체의 것은 이슈로 올릴 것으로 옮기고, 다시 빼거나 아무것도 고치지 않겠다고 하면 eval에만으로 돌리며, 고칠 안이 모두 비면 묻지 않는다는 글을 더했다. PRD 8번의 eval에만 문장도 "사용자가 고치거나 올리자고 하지 않는 한"과 옮김·되돌림·묻지 않음을 적게 고쳤다 (`docs/ADR.md`, `docs/PRD.md`)
- 옮긴 eval에만인 것을 다시 빼면 eval에만으로 돌아가게 한다: run "보고하고 묻는다"의 "고칠 곳을 말하면" 줄에서 BACKLOG로 옮기는 두 글을 "기준을 넘은" 하네스 고칠 거리로 좁히고 "그렇게 옮긴 것을 고침 task나 이슈로 올릴 것에서 다시 빼면 BACKLOG로 미룰 것이 아니라 eval에만으로 돌린다"를 더했다. "아무것도 고치지 않고" 줄은 "고침 task에 두었던 기준을 넘은 이 프로젝트만의 하네스 고칠 거리도 BACKLOG로 미룰 것에 둔다"로 좁히고 "eval에만에서 고침 task나 이슈로 올릴 것으로 옮긴 것은 eval에만으로 돌린다"를 더했다. `docs/ARCHITECTURE.md` 78줄에 "옮긴 것을 다시 빼거나 아무것도 고치지 않겠다고 하면 BACKLOG가 아니라 eval에만으로 돌아간다"를 더했다. `test_eval_only_goes_nowhere`와 `test_project_only_fixes_deferred_to_backlog`가 고친 글(되돌림 두 글, 좁힌 BACKLOG 세 글)을 보게 고쳤다 (`plugins/plate/skills/run/SKILL.md`, `docs/ARCHITECTURE.md`, `tests/test_skill_rules.py`)

## 확인 결과
- 회고 1의 문제가 모두 고쳐졌다.
  - `docs/ADR.md` ADR-026 결정, `docs/PRD.md` 8번, run SKILL.md 359·360줄, `docs/ARCHITECTURE.md` 78줄을 다시 읽음 → 네 곳 모두 사용자 지시로 옮기는 예외와 고칠 안이 비면 묻지 않음을 적고, run 359·360줄과 ARCHITECTURE 78줄은 옮긴 eval에만인 것을 다시 빼면 eval에만으로 돌린다고 적는다. BACKLOG로 옮기는 글은 "기준을 넘은" 것으로 좁혀졌다. 통과
  - `python3 -m unittest discover -s tests` → `Ran 207 tests in 18.928s` `OK`. 통과
- task 머리의 완료 조건이 모두 참이다.
  - 1: run "보고하고 묻는다"의 "고칠 곳을 말하면" 줄(359)과 "소스 문제가 없고 …" 줄(363)을 읽음 → 옮기는 경우와 고칠 안이 모두 비는 경우를 저마다 다룬다. `(cd tests && python3 -m unittest test_skill_rules.RunRulesTest.test_eval_only_goes_nowhere)` → `OK`. 통과
  - 2: `grep -n -e 'RUNLOG.md' AGENTS.md` → 14줄(문서 지도)과 25줄(작업 규칙 절의 헤드리스 시험 저장소 불변 확인 줄). 통과
  - 3: `docs/TOOLS.md` "세션 도중의 스킬 본문 고침" 절 52줄에 "헤드리스 시험의 완료 조건을 본문 해시로 볼 때, … 새 해시를 기록에 남긴다. 계획은 이것을 그 완료 조건 곁에 적는다"가 있다. 통과
  - 4: `grep -n -e 'eval에만' plugins/plate/skills/run/SKILL.md` → 42줄(낱말), 346·353·355·359·360·363줄(보고하고 묻는다), 436줄(고침 task의 꼴). `test_eval_only_goes_nowhere` → `OK`. `python3 -m unittest discover -s tests` → `Ran 207 tests` `OK`. 통과

## 계획과 달라진 점
- 없음

## 남은 것
- run "보고하고 묻는다"의 처음 안 목록 "BACKLOG로 미룰 것" 줄(351)의 "고침 task에서 뺀 이 프로젝트만의 하네스 고칠 거리의 번호"는 "기준을 넘은"으로 좁히지 않았다. 355줄의 eval에만 규칙과 359·360줄의 되돌림이 덮지만 글만 보면 넓게 읽힐 수 있다. 회고 1의 문제가 359·360줄을 가리켜 그 줄만 고쳤다
- run의 바뀐 동작은 묻고 멈추는 자리라 헤드리스로 돌려 보지 않았다

## 하네스에서 걸린 것
- 없음
