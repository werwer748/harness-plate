# 회고

## 회고 1

**확인**
- 1. run의 "보고하고 묻는다"가 "eval에만" 갈래를 끝까지 다룬다(고칠 안이 모두 비는 경우, eval에만인 것을 옮기자고 하는 경우)
  - `plugins/plate/skills/run/SKILL.md`의 "고칠 곳을 말하면" 줄(359줄)과 "소스 문제가 없고 …" 줄(363줄)을 읽음 → 359줄이 사용자가 eval에만인 것을 고치거나 올리자고 하면 이 프로젝트만의 것은 고침 task로, plate 자체의 것은 이슈로 올릴 것으로 옮긴다고 적고, 363줄이 소스 문제가 없고 하네스 고칠 거리가 없거나 모두 eval에만이거나 감수이면 고칠 것이 없다고 적고 묻지 않는다고 적는다. 통과
  - `(cd tests && python3 -m unittest test_skill_rules.RunRulesTest.test_eval_only_goes_nowhere)` → `Ran 1 test` `OK`. 통과
- 2. 작업 규칙에 헤드리스 시험 phase의 저장소 불변 확인 줄이 있다
  - `grep -n -e 'RUNLOG.md' AGENTS.md` → 14줄(문서 지도 행)과 25줄(작업 규칙 절, "헤드리스 시험을 두는 phase의 저장소 불변 확인 … `docs/tasks/RUNLOG.md`와 그 phase가 고치는 파일을 빼거나, phase 커밋 뒤에 돌린다고 통과 조건에 적는다"). 통과
- 3. "세션 도중의 스킬 본문 고침" 절에 해시를 새로 적는 줄이 있다
  - `docs/TOOLS.md`의 그 절을 읽음 → 절 끝(52줄)에 "헤드리스 시험의 완료 조건을 본문 해시로 볼 때, 그 본문을 뒤에서 고치는 phase(회고 뒤 더한 phase도)는 시험을 다시 돌려 새 해시를 기록에 남긴다. 계획은 이것을 그 완료 조건 곁에 적는다"가 있다. 통과
- 4. tasks 완료 조건 2, 6이 참이다
  - `grep -n -e 'eval에만' plugins/plate/skills/run/SKILL.md` → 42줄(낱말), 346·353·355·359·360·363줄(보고하고 묻는다), 436줄(고침 task의 꼴). 통과
  - `(cd tests && python3 -m unittest test_skill_rules.RunRulesTest.test_eval_only_goes_nowhere)` → `OK`. 통과
  - `python3 -m unittest discover -s tests` → `Ran 207 tests in 17.833s` `OK`. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 207 tests` `OK`. 통과

**남은 것**
- phase 1: ADR-026 결정과 `docs/PRD.md` 8번이 사용자 지시로 eval에만인 것을 옮기는 예외를 적지 않는다 → 문제 (맥락 문서: 같은 phase가 `docs/ARCHITECTURE.md` 78줄에는 "사용자가 고치거나 올리자고 하지 않는 한"과 고칠 것이 없을 때 묻지 않음을 더했으나, `docs/ADR.md`의 ADR-026 결정은 "run은 그것을 고침 task, 이슈, BACKLOG, 감수 어디에도 두지 않는다"로, PRD 8번은 "고침 task, 이슈, BACKLOG, 감수 어디에도 두지 않는다(ADR-026)"로 남아 run 본문과 ARCHITECTURE와 어긋난다)
- phase 1: 옮긴 eval에만인 것을 고침 task나 이슈로 올릴 것에서 다시 빼면 eval에만으로 돌아가지 않고 BACKLOG로 간다 → 문제 (결함: run 359줄의 "고침 task에서 뺀 … 이 프로젝트만의 하네스 고칠 거리는 BACKLOG로 미룰 것으로 옮긴다", "이슈로 올릴 것에서 뺀 하네스 고칠 거리는 BACKLOG로 미룰 것으로 옮긴다"와 360줄의 "고침 task에 두었던 이 프로젝트만의 하네스 고칠 거리도 BACKLOG로 미룰 것에 둔다"가 옮겨 온 eval에만인 것을 가리지 않아, 기준이 eval에만인 것이 BACKLOG에 들어간다. tasks 머리의 목표는 run이 eval에만인 것을 BACKLOG에 두지 않게 한다)
- phase 1: 고칠 안이 비는 경우에도 감수할 것은 묻지 않고 BACKLOG의 감수한 것 절에 적힌다 → 문제 아님 (task 머리 완료 조건 1이 "하네스 고칠 거리가 모두 eval에만이나 감수이고 소스 문제가 없을 때에도 승인을 묻는" 것을 고칠 것으로 정했다. 묻지 않음은 그 조건대로다)
- phase 1: run의 바뀐 동작을 헤드리스로 돌려 보지 않았다 → 문제 아님 (tasks 머리 완료 조건 2의 `- 돌리지 않음:` 줄이 run의 "보고하고 묻는다"는 묻고 멈추는 자리라 헤드리스로 승인 뒤 동작을 볼 수 없다고 정했고, 이번에 바뀐 글도 모두 그 절과 "고침 task의 꼴"이다)

**문제**
- ADR-026 결정과 PRD 8번이 run의 "보고하고 묻는다"와 `docs/ARCHITECTURE.md` 78줄에 더해진 두 동작(사용자가 고치거나 올리자고 하면 eval에만인 것을 갈래대로 옮긴다, 고칠 안이 모두 비면 묻지 않는다)을 적지 않아 "어디에도 두지 않는다"로 남는다 (`docs/ADR.md`, `docs/PRD.md`). 기준: 맥락 문서. 고칠 쪽: 문서 (task 머리 완료 조건 1이 run에 eval에만인 것을 옮길 곳을 적게 했고, 수행이 같은 뜻으로 ARCHITECTURE를 이미 맞췄다)
- 사용자가 고침 task나 이슈로 올릴 것으로 옮긴 eval에만인 하네스 고칠 거리를 다시 빼거나 "아무것도 고치지 않겠다"고 하면, run 359·360줄의 "뺀 것은 BACKLOG로 미룰 것으로 옮긴다"와 "고침 task에 두었던 이 프로젝트만의 하네스 고칠 거리도 BACKLOG로 미룰 것에 둔다"에 걸려 기준이 eval에만인 것이 BACKLOG로 간다 (`plugins/plate/skills/run/SKILL.md`). 기준: 결함. 고칠 쪽: 코드 (tasks 머리 목표: run이 eval에만인 것을 고침 task, 이슈, BACKLOG, 감수 어디에도 두지 않게 한다)

**판정**: 문제 있음

## 회고 2

**확인**
- 1. run의 "보고하고 묻는다"가 "eval에만" 갈래를 끝까지 다룬다(고칠 안이 모두 비는 경우, eval에만인 것을 옮기자고 하는 경우)
  - `plugins/plate/skills/run/SKILL.md`의 "고칠 곳을 말하면" 줄(359줄)과 "소스 문제가 없고 …" 줄(363줄)을 읽음 → 359줄이 사용자가 eval에만인 것을 고치거나 올리자고 하면 이 프로젝트만의 것은 고침 task로, plate 자체의 것은 이슈로 올릴 것으로 옮기고, 다시 빼면 BACKLOG가 아니라 eval에만으로 돌린다고 적고, 363줄이 소스 문제가 없고 하네스 고칠 거리가 없거나 모두 eval에만이거나 감수이면 고칠 것이 없다고 적고 묻지 않는다고 적는다. 통과
  - `(cd tests && python3 -m unittest test_skill_rules.RunRulesTest.test_eval_only_goes_nowhere)` → `Ran 1 test` `OK`. 통과
- 2. 작업 규칙에 헤드리스 시험 phase의 저장소 불변 확인 줄이 있다
  - `grep -n -e 'RUNLOG.md' AGENTS.md` → 14줄(문서 지도 행)과 25줄(작업 규칙 절, "헤드리스 시험을 두는 phase의 저장소 불변 확인 … `docs/tasks/RUNLOG.md`와 그 phase가 고치는 파일을 빼거나, phase 커밋 뒤에 돌린다고 통과 조건에 적는다"). 통과
- 3. "세션 도중의 스킬 본문 고침" 절에 해시를 새로 적는 줄이 있다
  - `docs/TOOLS.md`의 그 절을 읽음 → "헤드리스 시험의 완료 조건을 본문 해시로 볼 때, 그 본문을 뒤에서 고치는 phase(회고 뒤 더한 phase도)는 시험을 다시 돌려 새 해시를 기록에 남긴다. 계획은 이것을 그 완료 조건 곁에 적는다"가 있다. 통과
- 4. tasks 완료 조건 2, 6이 참이다
  - `grep -n -e 'eval에만' plugins/plate/skills/run/SKILL.md` → 42줄(낱말), 346·353·355·359·360·363줄(보고하고 묻는다), 436줄(고침 task의 꼴). 통과
  - `(cd tests && python3 -m unittest test_skill_rules.RunRulesTest.test_eval_only_goes_nowhere)` → `OK`. 통과
  - `python3 -m unittest discover -s tests` → `Ran 207 tests in 17.892s` `OK`. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 207 tests` `OK`. 통과

**남은 것**
- phase 1: ADR-026 결정과 `docs/PRD.md` 8번이 사용자 지시로 eval에만인 것을 옮기는 예외를 적지 않는다 → 문제 아님 (phase 2가 고쳤다: ADR-026 결정(59줄)과 PRD 8번(18줄)이 옮김, eval에만으로 되돌림, 고칠 안이 비면 묻지 않음을 적어 run 본문, ARCHITECTURE 78줄과 맞는다)
- phase 1: 옮긴 eval에만인 것을 고침 task나 이슈로 올릴 것에서 다시 빼면 eval에만으로 돌아가지 않고 BACKLOG로 간다 → 문제 아님 (phase 2가 고쳤다: run 359줄의 BACKLOG로 옮기는 두 글이 "기준을 넘은" 것으로 좁혀지고 "다시 빼면 BACKLOG로 미룰 것이 아니라 eval에만으로 돌린다"가, 360줄에 "eval에만에서 … 옮긴 것은 eval에만으로 돌린다"가 더해졌다)
- phase 1: 고칠 안이 비는 경우에도 감수할 것은 묻지 않고 BACKLOG의 감수한 것 절에 적힌다 → 문제 아님 (task 머리 완료 조건 1이 그 경우에 묻지 않게 고칠 것으로 정했다)
- phase 1: run의 바뀐 동작을 헤드리스로 돌려 보지 않았다 → 문제 아님 (tasks 머리 완료 조건 2의 `- 돌리지 않음:` 줄이 정한 동작이다)
- phase 2: run 351줄 "BACKLOG로 미룰 것"의 "고침 task에서 뺀 이 프로젝트만의 하네스 고칠 거리의 번호"를 "기준을 넘은"으로 좁히지 않아 넓게 읽힐 수 있다 → 문제 아님 (351줄은 처음 안의 목록 꼴이고, 처음 안에서는 355줄대로 eval에만인 것이 고침 task에 들지 않으며, 옮긴 것을 다시 빼는 경우는 359·360줄이 eval에만으로 돌린다고 밝혀 동작이 틀리지 않는다. 글의 넓은 읽힘은 취향에 든다)
- phase 2: run의 바뀐 동작은 묻고 멈추는 자리라 헤드리스로 돌려 보지 않았다 → 문제 아님 (tasks 머리 완료 조건 2의 `- 돌리지 않음:` 줄이 정한 동작이고, phase 2가 바꾼 run의 글도 "보고하고 묻는다"뿐이다)

**문제**
- 없음

**판정**: 통과
