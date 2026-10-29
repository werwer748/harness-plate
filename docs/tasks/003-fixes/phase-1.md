# Phase 1: tasks 끝의 문제를 고친다

**목표**: task 머리의 완료 조건에 적힌 것을 모두 고친다.

**테스트 먼저**: 아니오 — 고칠 것이 모두 `.md`(스킬 본문, 지침 파일, 맥락 문서)다

**읽을 것**
- `docs/tasks/review.md`의 `## 평가 1` 절
- `docs/tasks/eval.md`의 `## eval 1` 절
- `plugins/plate/skills/run/SKILL.md` ("보고하고 묻는다")
- `AGENTS.md` (작업 규칙)
- `tests/test_skill_rules.py` (`RunRulesTest.test_eval_only_goes_nowhere`)
- `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `docs/BACKLOG.md` (맥락 문서)

**TODO**
- [x] run의 "보고하고 묻는다"가 "eval에만" 갈래를 끝까지 다룬다: 고칠 안이 모두 비는 경우(하네스 고칠 거리가 모두 eval에만이나 감수이고 소스 문제가 없을 때)와, 사용자가 eval에만인 것을 고치거나 올리자고 할 때 어디로 옮기는지를 적는다. 그 동작을 적은 ARCHITECTURE의 tasks 끝 줄과 그 글을 지키는 테스트도 맞춘다 (`plugins/plate/skills/run/SKILL.md`, `docs/ARCHITECTURE.md`, `tests/test_skill_rules.py`)
- [x] 작업 규칙의 스킬 본문 tasks 줄 곁에, 헤드리스 시험을 두는 phase의 저장소 불변 확인은 `docs/tasks/RUNLOG.md`와 그 phase가 고치는 파일을 빼거나 phase 커밋 뒤에 돌린다고 통과 조건에 적는다는 줄이 더해진다 (`AGENTS.md`)
- [x] "세션 도중의 스킬 본문 고침" 절에, 헤드리스 시험의 완료 조건을 본문 해시로 볼 때 그 본문을 뒤에서 고치는 phase(회고 뒤 더한 phase도)는 시험을 다시 돌려 새 해시를 기록에 남기고, 계획은 이것을 그 완료 조건 곁에 적는다는 줄이 더해진다 (`docs/TOOLS.md`)

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다

## 한 일
- run의 "보고하고 묻는다"가 "eval에만" 갈래를 끝까지 다룬다: (1) "소스 문제도 하네스 고칠 거리도 없으면" 줄을 "소스 문제가 없고 하네스 고칠 거리가 없거나 모두 기준이 eval에만이거나 처리가 감수이면, 고침 task, 이슈로 올릴 것, BACKLOG로 미룰 것이 모두 비므로 고칠 안 대신 고칠 것이 없다고 적고 묻지 않는다"로 바꾸고, 감수할 것과 eval에만의 번호는 그대로 적으며 감수할 것은 "BACKLOG를 고친다"가 적는다고 더했다. (2) "고칠 곳을 말하면" 줄에, 사용자가 eval에만인 것을 고치거나 올리자고 하면 이 프로젝트만의 것은 고침 task로, plate 자체의 것은 이슈로 올릴 것으로 옮기고, eval이 적지 않은 고칠 곳·해결책·이슈 제목·본문은 eval 절의 글과 근거로 써서 다시 보인다고 더했다. (3) 처음 안의 "어디에도 두지 않는다" 뒤에 "사용자가 고치거나 올리자고 할 때만 아래 \"고칠 곳을 말하면\"대로 옮긴다"를, "고침 task의 꼴"에 "사용자가 고치자고 해 옮긴 이 프로젝트만의 것만 넣는다"를 더했다. ARCHITECTURE의 tasks 끝 줄을 같은 뜻으로 맞추고, `test_eval_only_goes_nowhere`에 새 글 넷과 옛 줄이 없음을 보는 단언을 더하고 고침 task의 꼴 단언을 새 글로 바꿨다 (`plugins/plate/skills/run/SKILL.md`, `docs/ARCHITECTURE.md`, `tests/test_skill_rules.py`)
- 작업 규칙에 헤드리스 시험 phase의 저장소 불변 확인 줄: 스킬 본문 tasks 줄(24줄) 바로 뒤 25줄에 "`docs/tasks/RUNLOG.md`와 그 phase가 고치는 파일을 빼거나, phase 커밋 뒤에 돌린다고 통과 조건에 적는다"와 그 까닭을 더했다 (`AGENTS.md`)
- "세션 도중의 스킬 본문 고침" 절의 해시 줄: 절 끝에 "헤드리스 시험의 완료 조건을 본문 해시로 볼 때, 그 본문을 뒤에서 고치는 phase(회고 뒤 더한 phase도)는 시험을 다시 돌려 새 해시를 기록에 남긴다. 계획은 이것을 그 완료 조건 곁에 적는다"와 그 까닭을 더했다 (`docs/TOOLS.md`)

## 확인 결과
- task 머리의 완료 조건이 모두 참이다.
  - 완료 조건 1: run "보고하고 묻는다"의 359줄("고칠 곳을 말하면")과 363줄("소스 문제가 없고 …")을 다시 읽음 → 359줄이 eval에만인 것을 고치거나 올리자고 할 때 갈래마다 옮길 곳(고침 task, 이슈로 올릴 것)을, 363줄이 고칠 안이 모두 비는 경우(eval에만이나 감수뿐)에 묻지 않음을 다룬다. 통과
  - 완료 조건 1: `(cd tests && python3 -m unittest test_skill_rules.RunRulesTest.test_eval_only_goes_nowhere)` → `Ran 1 test` `OK`. 통과
  - 완료 조건 2: `grep -n -e 'RUNLOG.md' AGENTS.md` → 14줄(문서 지도 행)과 25줄(작업 규칙 절의 새 줄). 통과
  - 완료 조건 3: `docs/TOOLS.md`의 "세션 도중의 스킬 본문 고침" 절을 읽음 → 절 끝 줄에 해시 줄이 있다. 통과
  - 완료 조건 4(tasks 2): `grep -n -e 'eval에만' plugins/plate/skills/run/SKILL.md` → 42(낱말), 346·353·355·359·360·363(보고하고 묻는다), 436(고침 task의 꼴). 통과
  - 완료 조건 4(tasks 2): `(cd tests && python3 -m unittest test_skill_rules.RunRulesTest.test_eval_only_goes_nowhere)` → `OK`. 통과
  - 완료 조건 4(tasks 6): `python3 -m unittest discover -s tests` → `Ran 207 tests in 19.517s` `OK`. 통과

## 계획과 달라진 점
- 없음

## 남은 것
- 사용자가 eval에만인 것을 고치거나 올리자고 할 때 옮길 곳(이 프로젝트만은 고침 task, plate 자체는 이슈)은 계획이 정하지 않아 갈래마다의 기존 처음 안(기준을 넘은 것의 자리)을 따라 정했다. `docs/ADR.md`의 ADR-026 결정("run은 그것을 고침 task, 이슈, BACKLOG, 감수 어디에도 두지 않는다")과 `docs/PRD.md` 8번은 이 사용자 지시의 예외를 적지 않는다. 이 phase의 TODO 파일에 없어 고치지 않았다
- 옮긴 eval에만인 것을 사용자가 다시 고침 task나 이슈로 올릴 것에서 빼면, 같은 줄의 "뺀 것은 BACKLOG로 미룰 것으로 옮긴다"에 걸려 eval에만으로 돌아가지 않고 BACKLOG로 간다. 이 갈래는 적지 않았다
- 고칠 안이 비는 경우에도 감수할 것은 묻지 않고 BACKLOG의 감수한 것 절에 적힌다(전에는 승인 뒤에 적혔다)
- run의 바뀐 동작은 헤드리스로 돌려 보지 않았다. 확인은 글을 읽고 문구를 보는 unittest뿐이다

## 하네스에서 걸린 것
- 계획(완료 조건 1, TODO 1)이 eval에만인 것을 사용자가 옮기자고 할 때 어디로 옮길지 정하지 않아 수행이 정했다. 설계의 선택으로 볼 수도 있으나 기존 갈래의 자리를 따르는 것으로 보고 진행했다

