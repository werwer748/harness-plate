# tasks 끝의 문제를 고친다

## 목표
tasks 끝의 코드 평가와 하네스 eval에서 고치기로 한 것을 모두 고친다.

## 범위 밖
- 코드 평가와 하네스 eval을 다시 하는 것
- plate 자체의 하네스 고칠 거리를 고치는 것. 이슈로 올리거나 BACKLOG로 미루고 plate 저장소에서 고친다

## 완료 조건
1. run의 "보고하고 묻는다"가 "eval에만" 갈래를 끝까지 다루지 않는다: 고칠 안이 모두 비는 경우(하네스 고칠 거리가 모두 eval에만이나 감수이고 소스 문제가 없을 때)에도 승인을 묻고, 사용자가 eval에만인 것을 고치거나 올리자고 할 때 어디로 옮기는지 적지 않는다 (`plugins/plate/skills/run/SKILL.md:363`, `plugins/plate/skills/run/SKILL.md:358`)
   - 확인: run의 "보고하고 묻는다"에서 "고칠 곳을 말하면" 줄과 "소스 문제도 하네스 고칠 거리도 없으면" 줄을 다시 읽어, 고칠 안이 모두 비는 경우와 eval에만인 것을 옮기자고 하는 경우를 저마다 다루는지 본다
   - 확인: `(cd tests && python3 -m unittest test_skill_rules.RunRulesTest.test_eval_only_goes_nowhere)`가 OK다
2. 헤드리스 시험을 두는 phase의 "시험이 이 저장소를 바꾸지 않았다" 확인이, 확인 전에 하네스(`docs/tasks/RUNLOG.md`)와 그 phase가 정당하게 쓰는 파일을 빼고 보거나 phase 커밋 뒤에 돌린다고 적게 한다. 해결책: 작업 규칙의 스킬 본문 tasks 줄 곁에 "헤드리스 시험을 두는 phase의 저장소 불변 확인은 `docs/tasks/RUNLOG.md`와 그 phase가 고치는 파일을 빼거나, phase 커밋 뒤에 돌린다고 통과 조건에 적는다"를 더한다 (`AGENTS.md`)
   - 확인: `grep -n -e 'RUNLOG.md' AGENTS.md`가 작업 규칙 절의 그 줄을 낸다
3. 스킬 본문의 해시로 보는 완료 조건을 둘 때, 회고 뒤 그 본문을 고치는 phase가 헤드리스 시험을 다시 돌려 해시를 새로 적는다는 것을 계획에 적게 한다. 해결책: "세션 도중의 스킬 본문 고침" 절에 "헤드리스 시험의 완료 조건을 본문 해시로 볼 때, 그 본문을 뒤에서 고치는 phase(회고 뒤 더한 phase도)는 시험을 다시 돌려 새 해시를 기록에 남긴다. 계획은 이것을 그 완료 조건 곁에 적는다"를 더한다 (`docs/TOOLS.md`)
   - 확인: `docs/TOOLS.md`의 "세션 도중의 스킬 본문 고침" 절을 읽어 그 줄이 있는지 본다
4. tasks 완료 조건 2, 6이 참이다.
   - tasks 완료 조건 2: run 스킬의 낱말 "하네스 고칠 거리", "보고하고 묻는다"(4번, 6번 고칠 안, 처음 안, 답의 갈래), "고침 task의 꼴"이 "eval에만"인 것을 고침 task, 이슈, BACKLOG, 감수 어디에도 두지 않는다.
     - 확인: `grep -n -e 'eval에만' plugins/plate/skills/run/SKILL.md`가 낱말, 보고하고 묻는다, 고침 task의 꼴의 줄을 낸다
     - 확인: `(cd tests && python3 -m unittest test_skill_rules.RunRulesTest.test_eval_only_goes_nowhere)`가 OK다
   - tasks 완료 조건 6: 테스트가 모두 통과한다.
     - 확인: `python3 -m unittest discover -s tests`가 OK다

## 결정
- 없음
