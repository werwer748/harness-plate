# 회고

## 회고 1

**확인**
- 1. eval 스킬의 5절, 기록의 양식, 적는 규칙, description이 세 기준과 "eval에만"을 같은 뜻으로 적는다. 기준은 감수와 문턱보다 먼저 가르고, "eval에만"인 것에는 처리, 문턱, 이슈 줄을 두지 않는다
  - `grep -n -e 'eval에만' plugins/plate/skills/eval/SKILL.md` → 3(description), 179·183(5절), 256·262(기록의 양식), 280(적는 규칙). 179의 세 기준 항목이 처리(184)·문턱(185) 항목보다 앞서고, 280이 "eval에만"인 항목에서 처리·문턱·이슈 줄을 뺀다. 통과
  - `(cd tests && python3 -m unittest test_skill_rules.EvalRulesTest.test_eval_only_criteria)` → `Ran 1 test` `OK`. 통과
- 2. run 스킬의 낱말 "하네스 고칠 거리", "보고하고 묻는다"(4번, 6번 고칠 안, 처음 안, 답의 갈래), "고침 task의 꼴"이 "eval에만"인 것을 고침 task, 이슈, BACKLOG, 감수 어디에도 두지 않는다
  - `grep -n -e 'eval에만' plugins/plate/skills/run/SKILL.md` → 42(낱말), 346(4번), 353(6번 eval에만 줄), 355(처음 안), 360(아무것도 고치지 않는 갈래), 436(고침 task의 꼴). 통과
  - `(cd tests && python3 -m unittest test_skill_rules.RunRulesTest.test_eval_only_goes_nowhere)` → `Ran 1 test` `OK`. 통과
  - 돌리지 않음: run의 "보고하고 묻는다"는 사용자에게 묻고 멈추는 자리라 헤드리스로 볼 수 없다(task 머리에 정함). 355·360·436의 글을 직접 읽어 "eval에만"이 고침 task, 이슈, BACKLOG, 감수 어디에도 들지 않음을 봤다
- 3. `docs/ADR.md`에 ADR-026이 있고, ADR-025의 결정에 ADR-026을 가리키는 말이 있으며, PRD 핵심 기능 8번과 ARCHITECTURE 데이터 흐름의 tasks 끝 줄이 세 기준과 "eval에만"을 적는다
  - `grep -n -e '^### ADR-026' -e 'ADR-026' docs/ADR.md docs/PRD.md docs/ARCHITECTURE.md` → `docs/ADR.md:54`(ADR-025 결정 줄의 `(ADR-026으로 더함: …)`), `docs/ADR.md:58`(`### ADR-026` 머리), `docs/PRD.md:18`(8번 줄, 세 기준과 "eval에만"), `docs/ARCHITECTURE.md:76`(tasks 끝 줄, "eval에만"). 통과
- 4. `docs/BACKLOG.md`의 하네스 고칠 거리 절에 항목이 없고, 세 절 머리는 남는다
  - `awk '/^## 하네스 고칠 거리/{p=1;next} /^## /{p=0} p && /^- /' docs/BACKLOG.md | wc -l` → `0`, `grep -c -e '^## ' docs/BACKLOG.md` → `3`. 통과
- 5. 작업 트리의 eval 스킬을 헤드리스로 시험 저장소에서 돌리면, 등급만 낮춘 고칠 거리는 "eval에만"으로, 결과에 피해가 난 일반적인 고칠 거리는 기준을 넘은 것으로 적는다
  - `done-phase-4.md`의 "한 일"과 `git hash-object plugins/plate/skills/eval/SKILL.md` → 기록의 해시 `ac05dfe6b1a2ec0be73680e8e073566778c87c3e`와 작업 트리에서 다시 낸 값이 같다. 기록에 시험 저장소 `eval.md`의 "하네스 고칠 거리" 절이 붙어 있고, 시험 저장소(`/var/folders/0j/cj37rxmj1mj73vhflqpgsxm00000gn/T/tmp.NzuCKG53PT/docs/tasks/eval.md`)의 같은 절과 같다. A(고칠 거리 3)는 `- 기준: eval에만` 줄만 있고 처리·문턱·이슈 줄이 없다. B(고칠 거리 1)는 `- 기준: 넘음`과 `- 처리:` 줄이 있다. 통과
- 6. 테스트가 모두 통과한다
  - `python3 -m unittest discover -s tests` → `Ran 205 tests` `OK`. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 205 tests in 18.123s` `OK`. 통과

**남은 것**
- phase 1: 8절의 돌려주는 줄 "고칠 거리: plate 자체 N개, 이 프로젝트만 M개"는 "eval에만"인 항목을 세는지 빼는지 정하지 않았다 → 문제 아님 (완료 조건 1과 결정이 정한 곳은 description, 5절, 양식, 적는 규칙이고, run이 갈래를 정할 때 보는 것은 `eval.md`의 기준 줄이라 돌려주는 수가 "eval에만"을 어디에 두게 하지 않는다)
- phase 1: 낱말 절에 "eval에만"의 정의를 따로 두지 않았다. 뜻은 5절에만 있다 → 문제 아님 (어느 기준도 낱말 절에 두라고 정하지 않았다. 구조의 취향이다)
- phase 2: "아무것도 고치지 않겠다" 갈래의 "기준을 넘은 plate 자체의 하네스 고칠 거리를 모두 BACKLOG로"는 처리가 감수인 것도 글자로 품는다 → 문제 아님 (이 task 전부터 있던 겹침이고, 같은 줄(`plugins/plate/skills/run/SKILL.md:360`)의 "감수할 것에 둔 것은 그대로 감수할 것에 둔다"가 가른다. "eval에만"의 동작에는 걸리지 않는다)
- phase 2: run의 "보고하고 묻는다" 뒤의 동작은 헤드리스로 볼 수 없다 → 문제 아님 (task 머리 완료 조건 2의 돌리지 않음이 정한 것이고, 355·360·436의 글을 직접 읽어 "eval에만"이 어디에도 들지 않음을 봤다)
- phase 4: 시험은 한 번 돌렸다. 같은 기록에서 eval이 A와 B를 늘 같게 가르는지는 보지 않았다 → 문제 아님 (완료 조건 5는 돌린 한 번의 기록을 보고, 되풀이의 한결같음은 목표와 결정이 약속하지 않는다)
- phase 4: 시험 저장소는 시스템 임시 폴더에 남아 있다 → 문제 아님 (이 저장소 밖이고, 이 저장소의 `git status`는 깨끗하다)

**문제**
- 없음

**판정**: 통과
