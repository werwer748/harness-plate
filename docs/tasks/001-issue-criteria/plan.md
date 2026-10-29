# eval과 run에 세 기준과 "eval에만"을 넣는다

## 목표
eval이 하네스 고칠 거리마다 세 기준을 먼저 대어 넘지 않은 것을 "eval에만"으로 적고, run이 그것을 고침 task, 이슈, BACKLOG, 감수 어디에도 두지 않게 한다. ADR-026과 맥락 문서가 그것을 적고, BACKLOG의 하네스 고칠 거리가 기준대로 비고, 작업 트리의 eval을 헤드리스로 돌려 그렇게 가르는 것을 본다.

## 범위 밖
- 코드 평가(review)의 소스 문제에 기준을 거는 것
- eval의 실패 세기와 여섯 기준의 등급표를 바꾸는 것. "eval에만"인 것도 실패와 등급에는 그대로 센다
- run의 "BACKLOG를 고친다"와 BACKLOG 양식을 바꾸는 것
- GitHub 이슈를 닫는 것

## 완료 조건
1. eval 스킬의 5절, 기록의 양식, 적는 규칙, description이 세 기준과 "eval에만"을 같은 뜻으로 적는다. 기준은 감수와 문턱보다 먼저 가르고, "eval에만"인 것에는 처리, 문턱, 이슈 줄을 두지 않는다(tasks 완료 조건 1).
   - 확인: `grep -n -e 'eval에만' plugins/plate/skills/eval/SKILL.md`가 description, 5절, 양식, 적는 규칙의 줄을 낸다
   - 확인: `(cd tests && python3 -m unittest test_skill_rules.EvalRulesTest.test_eval_only_criteria)`가 OK다
2. run 스킬의 낱말 "하네스 고칠 거리", "보고하고 묻는다"(4번, 6번 고칠 안, 처음 안, 답의 갈래), "고침 task의 꼴"이 "eval에만"인 것을 고침 task, 이슈, BACKLOG, 감수 어디에도 두지 않는다(tasks 완료 조건 2).
   - 확인: `grep -n -e 'eval에만' plugins/plate/skills/run/SKILL.md`가 낱말, 보고하고 묻는다, 고침 task의 꼴의 줄을 낸다
   - 확인: `(cd tests && python3 -m unittest test_skill_rules.RunRulesTest.test_eval_only_goes_nowhere)`가 OK다
   - 돌리지 않음: run의 "보고하고 묻는다"는 사용자에게 묻고 멈추는 자리라 헤드리스로 끝까지 돌려도 고칠 안의 승인 뒤 동작을 볼 수 없다
3. `docs/ADR.md`에 ADR-026이 있고, ADR-025의 결정에 ADR-026을 가리키는 말이 있으며, `docs/PRD.md` 핵심 기능 8번과 `docs/ARCHITECTURE.md` 데이터 흐름의 tasks 끝 줄이 세 기준과 "eval에만"을 적는다(tasks 완료 조건 3).
   - 확인: `grep -n -e '^### ADR-026' -e 'ADR-026' docs/ADR.md docs/PRD.md docs/ARCHITECTURE.md`가 ADR-026 머리, ADR-025 결정 줄, PRD 8번 줄, ARCHITECTURE의 tasks 끝 줄을 낸다
4. `docs/BACKLOG.md`의 하네스 고칠 거리 절에 항목이 없고, 세 절 머리는 남는다(tasks 완료 조건 4).
   - 확인: `awk '/^## 하네스 고칠 거리/{p=1;next} /^## /{p=0} p && /^- /' docs/BACKLOG.md | wc -l`가 `0`이고 `grep -c -e '^## ' docs/BACKLOG.md`가 `3`이다
5. 작업 트리의 eval 스킬을 헤드리스로 시험 저장소에서 돌리면, 등급만 낮춘 고칠 거리는 "eval에만"으로, 결과에 피해가 난 일반적인 고칠 거리는 기준을 넘은 것으로 적는다(tasks 완료 조건 5).
   - 확인: 시험을 돌린 phase의 기록에 돌릴 때의 `git hash-object plugins/plate/skills/eval/SKILL.md`와 시험 저장소 `eval.md`의 "하네스 고칠 거리" 절이 있고, 그 해시가 작업 트리에서 다시 낸 값과 같으며, 그 절에서 등급만 낮춘 것은 기준이 "eval에만"이고 처리·문턱·이슈 줄이 없으며, 피해가 난 것은 기준을 넘고 처리 줄이 있다
6. 테스트가 모두 통과한다(tasks 완료 조건 6).
   - 확인: `python3 -m unittest discover -s tests`가 OK다

## 결정
- 세 기준은 이렇다. 하나라도 넘지 않으면 그 고칠 거리의 기준은 "eval에만"이다. (1) 피해: 근거에 결과의 피해(결함이 확인을 지나갔다, 다시 수행·멈춤·사람 개입이 났다)가 있거나, 그 원인이 보안·성능·유지보수성의 치명적 결함으로 이어질 수 있다. 적힌 대로 다시 돌려 통과했거나 기록의 꼴이나 읽기 범위만 어겨 등급만 낮아진 것은 넘지 않는다. (2) 일반성: 다른 프로젝트의 평범한 tasks에서도 날 일이다. 이 프로젝트에서만 쓰는 장면(예: 스킬 본문을 헤드리스로 시험하는 차림)에서만 난 것은 넘지 않는다. (3) 고침의 꼴: 해결책을 여러 경우를 덮는 원리로 적을 수 있다. 한 사례만 막는 규칙이면 원리로 넓혀 적고, 넓힐 수 없으면 넘지 않는다. 이유: 사용자가 정한 기준
- 기준은 두 갈래(plate 자체, 이 프로젝트만) 모두에 대고, 일반성은 plate 자체의 것에만 댄다. 이유: 고침 task가 좁은 규칙을 쌓는 것도 같은 문제다
- 기준을 넘지 않은 것의 이름은 "eval에만"이다. `eval.md`에만 남고 고침 task, 이슈, BACKLOG, 감수 어디에도 두지 않으며, 다시 나서 기준을 넘으면 그때 고칠 거리가 된다. 이유: "기록만"은 eval 1번에서 이미 "기록만으로 평가한다"로 쓰여 뜻이 겹친다(추천안으로 정함)
- 기준은 감수와 문턱보다 먼저 가른다. 이유: 탈락한 것은 이슈에도 BACKLOG에도 넣지 않는다(사용자가 정한 기준)
- 고침 task에서 뺀 이 프로젝트만의 하네스 고칠 거리는 지금대로 BACKLOG로 미룬다. 이유: 기준을 넘은 것만 고침 task에 드니 뺀 것도 기준을 넘은 것이다
