# 이슈·BACKLOG가 되는 기준을 세운다

**이름**: issue-criteria

## 요청
이슈·BACKLOG가 되는 기준을 세우고, 남은 이슈를 고친다.

1) 기준(사용자 승인됨): 하네스 고칠 거리가 GitHub 이슈나 docs/BACKLOG.md가 되려면 다음을 모두 넘어야 한다.
  - 피해: 등급이 아니라 결과에 피해가 있었다(결함이 통과함, 다시 하기·멈춤·사람 개입). 또는 치명적 결함(보안·성능·유지보수)의 원인일 수 있다. 적힌 대로 다시 돌려 통과했거나 기록의 꼴·읽기 범위 위반으로 등급만 깎인 것은 넘지 않는다.
  - 일반성: 다른 프로젝트의 평범한 tasks에서도 날 일이다. 이 저장소만의 장면(스킬 본문을 헤드리스로 시험하는 차림 등)에서만 난 것은 넘지 않는다.
  - 고침의 꼴: 해결책이 한 사례를 나열하는 규칙이 아니다. 그런 것은 원리로 넓히거나 버린다. 같은 뿌리는 하나로 묶는다.
  탈락한 것은 eval.md에 "기록만"으로 남기고 이슈에도 BACKLOG에도 넣지 않는다. 다시 나서 기준을 넘으면 그때 올린다.
  넣을 곳: docs/ADR.md에 ADR-026(ADR-025의 문턱에 더함), eval 스킬 5절과 양식, run 스킬 "보고하고 묻는다"의 고칠 안.
2) docs/BACKLOG.md의 하네스 고칠 거리 3개(모두 eval-threshold에서 나온 좁은 plan 규칙)를 이 기준으로 지운다.
3) 남길 이슈 고침:
  - #68 + #69 하나로 묶음: 확인 명령이 적힌 그대로 도는지를 원리로 다룬다(plan은 초안 때 확인 명령을 돌려 본다, phase/check/retro는 고쳐 돌렸으면 고친 명령과 까닭을 기록과 "하네스에서 걸린 것"에 남긴다). `-` 패턴 같은 사례 나열은 하지 않는다.
  - #77: 고침 task에서 뺀 이 프로젝트만의 하네스 고칠 거리는 버린다고 정하고, run의 BACKLOG 양식에서 `갈래: 이 프로젝트만`을 지운다(새 기준과 맞춤). 고른 쪽을 지키는 테스트를 둔다.
#76 #73 #72 #70은 이 기준으로 닫는다(사용자가 직접 닫음).

## 목표
eval이 하네스 고칠 거리마다 세 기준(피해, 일반성, 고침의 꼴)을 먼저 대어, 넘지 않은 것은 "eval에만"으로 `eval.md`에만 남기고 run이 그것을 고침 task, 이슈, BACKLOG, 감수 어디에도 두지 않게 한다. 그 결정을 ADR-026과 맥락 문서에 적고, 지금 BACKLOG의 하네스 고칠 거리를 기준대로 지운다.

## 범위 밖
- 코드 평가(review)의 소스 문제에 기준을 거는 것
- eval의 실패 세기와 여섯 기준의 등급표를 바꾸는 것. "eval에만"인 것도 실패와 등급에는 그대로 센다
- #68, #69, #77을 다시 고치는 것. 이미 고쳐져 있다
- GitHub 이슈를 닫는 것. 사용자가 한다

## 완료 조건
1. eval 스킬의 5절, 기록의 양식, 적는 규칙, description이 세 기준과 "eval에만"을 같은 뜻으로 적는다. 기준은 감수와 문턱보다 먼저 가르고, "eval에만"인 것에는 처리, 문턱, 이슈 줄을 두지 않는다.
   - 확인: `grep -n -e 'eval에만' plugins/plate/skills/eval/SKILL.md`가 description, 5절, 양식, 적는 규칙의 줄을 낸다
   - 확인: `(cd tests && python3 -m unittest test_skill_rules.EvalRulesTest.test_eval_only_criteria)`가 OK다
2. run 스킬의 낱말 "하네스 고칠 거리", "보고하고 묻는다"(4번, 6번 고칠 안, 처음 안, 답의 갈래), "고침 task의 꼴"이 "eval에만"인 것을 고침 task, 이슈, BACKLOG, 감수 어디에도 두지 않는다.
   - 확인: `grep -n -e 'eval에만' plugins/plate/skills/run/SKILL.md`가 낱말, 보고하고 묻는다, 고침 task의 꼴의 줄을 낸다
   - 확인: `(cd tests && python3 -m unittest test_skill_rules.RunRulesTest.test_eval_only_goes_nowhere)`가 OK다
   - 돌리지 않음: run의 "보고하고 묻는다"는 사용자에게 묻고 멈추는 자리라 헤드리스로 끝까지 돌려도 고칠 안의 승인 뒤 동작을 볼 수 없다
3. `docs/ADR.md`에 ADR-026이 있고, ADR-025의 결정에 ADR-026을 가리키는 말이 있으며, `docs/PRD.md` 핵심 기능 8번과 `docs/ARCHITECTURE.md` 데이터 흐름의 tasks 끝 줄이 세 기준과 "eval에만"을 적는다.
   - 확인: `grep -n -e '^### ADR-026' -e 'ADR-026' docs/ADR.md docs/PRD.md docs/ARCHITECTURE.md`가 ADR-026 머리, ADR-025 결정 줄, PRD 8번 줄, ARCHITECTURE의 tasks 끝 줄을 낸다
4. `docs/BACKLOG.md`의 하네스 고칠 거리 절에 항목이 없고, 세 절 머리는 남는다.
   - 확인: `awk '/^## 하네스 고칠 거리/{p=1;next} /^## /{p=0} p && /^- /' docs/BACKLOG.md | wc -l`가 `0`이고 `grep -c -e '^## ' docs/BACKLOG.md`가 `3`이다
5. 작업 트리의 eval 스킬을 헤드리스로 시험 저장소에서 돌리면, 등급만 낮춘 고칠 거리는 "eval에만"으로, 결과에 피해가 난 일반적인 고칠 거리는 기준을 넘은 것으로 적는다.
   - 확인: 시험을 돌린 phase의 기록에 돌릴 때의 `git hash-object plugins/plate/skills/eval/SKILL.md`와 시험 저장소 `eval.md`의 "하네스 고칠 거리" 절이 있고, 그 해시가 작업 트리에서 다시 낸 값과 같으며, 그 절에서 등급만 낮춘 것은 기준이 "eval에만"이고 처리·문턱·이슈 줄이 없으며, 피해가 난 것은 기준을 넘고 처리 줄이 있다
6. 테스트가 모두 통과한다.
   - 확인: `python3 -m unittest discover -s tests`가 OK다

## 결정
- 기준은 두 갈래(plate 자체, 이 프로젝트만)의 하네스 고칠 거리 모두에 건다. 일반성은 plate 자체의 것에만 대어 본다. 이유: 고침 task가 좁은 규칙을 쌓는 것도 같은 문제다(추천안을 고름)
- 기준을 넘지 않은 것의 이름은 "eval에만"으로 한다. 이유: "기록만"은 eval 1번에서 이미 "기록만으로 평가한다"로 쓰여 뜻이 겹친다(추천안으로 정함)
- "eval에만"은 감수와 문턱보다 먼저 가른다. 이유: 탈락한 것은 이슈에도 BACKLOG에도 넣지 않는다(사용자가 정한 기준)
- 코드 평가의 소스 문제에는 기준을 걸지 않는다. 이유: review가 이미 파일:줄 근거와 범주로 거르고, 범위를 좁게 둔다(추천안을 고름)
- 고침 task에서 뺀 이 프로젝트만의 하네스 고칠 거리는 지금대로 BACKLOG로 미룬다(#77은 `002-fixes`에서 이 쪽으로 고쳐졌다). 이유: 기준을 넘은 것만 고침 task에 드니 뺀 것도 기준을 넘은 것이다(추천안을 고름)
- #68, #69(`check-commands`에서 고쳐짐), #77은 고쳐진 것으로, #70, #72, #73, #76은 기준으로 사용자가 닫는다. 이유: 사용자가 정함
- run을 시작하기 전에 사용자가 plan 모드를 끄고 bypassPermissions로 바꾼다. 이유: 스킬 본문을 쓰는 tasks는 auto mode에서 수행의 쓰기가 막힌다(`AGENTS.md` 작업 규칙, `docs/TOOLS.md`의 "플러그인 폴더의 편집과 권한 모드")

## task 목록
- `001-issue-criteria`: eval과 run이 세 기준과 "eval에만"을 따르고, ADR-026과 맥락 문서, BACKLOG가 그것과 맞는다
