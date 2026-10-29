# 코드 평가

## 평가 1

**대상**
- 범위: `6258cf4`(main에서 갈라진 곳)부터 `432373f`까지
- 결과물인 마크다운 절: `plugins/plate/skills/*/SKILL.md`
- 바뀐 코드 파일 4개, 새 줄 128줄, 잴 새 줄 92줄
  - `tests/test_skill_rules.py` +92
  - `plugins/plate/skills/eval/SKILL.md` +14 (결과물인 마크다운)
  - `plugins/plate/skills/plan/SKILL.md` +14 (결과물인 마크다운)
  - `plugins/plate/skills/run/SKILL.md` +8 (결과물인 마크다운)

**잰 것**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 207 tests in 18.061s` `OK`. 통과
- 커버리지: 측정 못함 — `coverage` 모듈과 명령이 이 환경에 없고, 명령 절이 커버리지 도구를 두지 않는다고 적는다(ADR-024)
- 중복: 측정 못함 — `jscpd` 같은 중복 검사 도구가 없다(ADR-024)
- 정적 분석: 측정 못함 — `pyflakes`, `flake8`, `ruff`, `mypy`, `pylint`가 이 환경에 없다(`which`로 확인)
- 보안 검사: 측정 못함 — `bandit`, `semgrep`이 없고 의존성 목록도 없다(ADR-024)

**완료 조건**
- 1. eval 스킬의 5절, 기록의 양식, 적는 규칙, description이 세 기준과 "eval에만"을 같은 뜻으로 적는다
  - `grep -n -e 'eval에만' plugins/plate/skills/eval/SKILL.md` → 3(description), 179·183(5절), 256·262(양식), 280(적는 규칙). 통과
  - `(cd tests && python3 -m unittest test_skill_rules.EvalRulesTest.test_eval_only_criteria)` → `OK`. 통과
- 2. run 스킬의 낱말, "보고하고 묻는다", "고침 task의 꼴"이 "eval에만"인 것을 어디에도 두지 않는다
  - `grep -n -e 'eval에만' plugins/plate/skills/run/SKILL.md` → 42(낱말), 346·353·355·360(보고하고 묻는다), 436(고침 task의 꼴). 통과
  - `(cd tests && python3 -m unittest test_skill_rules.RunRulesTest.test_eval_only_goes_nowhere)` → `OK`. 통과
- 3. `docs/ADR.md`에 ADR-026이 있고 ADR-025 결정이 그것을 가리키며, PRD 8번과 ARCHITECTURE의 tasks 끝 줄이 세 기준과 "eval에만"을 적는다
  - `grep -n -e '^### ADR-026' -e 'ADR-026' docs/ADR.md docs/PRD.md docs/ARCHITECTURE.md` → `docs/ADR.md:58`(ADR-026 머리), `docs/ADR.md:54`(ADR-025 결정), `docs/PRD.md:18`(8번), `docs/ARCHITECTURE.md:78`(tasks 끝 줄). 두 줄 모두 "세 기준(피해, 일반성, 고침의 꼴)"과 "eval에만"을 적는다. 통과
- 4. `docs/BACKLOG.md`의 하네스 고칠 거리 절에 항목이 없고 세 절 머리는 남는다
  - `awk '/^## 하네스 고칠 거리/{p=1;next} /^## /{p=0} p && /^- /' docs/BACKLOG.md | wc -l` → `0`, `grep -c -e '^## ' docs/BACKLOG.md` → `3`. 통과
- 5. 작업 트리의 eval을 헤드리스로 돌리면 등급만 낮춘 것은 "eval에만", 피해가 난 일반적인 것은 기준을 넘은 것으로 적는다
  - `docs/tasks/001-issue-criteria/done-phase-4.md:28`의 해시 `ac05dfe6b1a2ec0be73680e8e073566778c87c3e`와 지금 `git hash-object plugins/plate/skills/eval/SKILL.md` → `ac05dfe6b1a2ec0be73680e8e073566778c87c3e`, 같다. 같은 기록 31~47줄의 "하네스 고칠 거리" 절에서 고칠 거리 3(다시 돌려 통과한 것)은 `- 기준: eval에만` 줄만 있고 처리·문턱·이슈 줄이 없으며, 고칠 거리 1(회고에서 잡혀 다시 수행한 것)은 `- 기준: 넘음`과 `- 처리:` 줄이 있다. 통과
- 6. 테스트가 모두 통과한다
  - `python3 -m unittest discover -s tests` → `Ran 207 tests` `OK`. 통과

**범주**
- 신뢰성
  - 근거: eval 5절(`plugins/plate/skills/eval/SKILL.md:179-188`)의 기준 → 처리 → 문턱 → 이슈 차례와 양식(256-264), 적는 규칙(280-281)이 서로 맞는다. run 낱말(`plugins/plate/skills/run/SKILL.md:42`), 고칠 안(346-360), 고침 task의 꼴(436)이 "eval에만"을 어디에도 두지 않는 것으로 같은 뜻이다. plan 1번(`plugins/plate/skills/plan/SKILL.md:54-57`), 7번(137), 이름 규칙(235)의 세 갈래(기본 브랜치, 같은 tasks의 `tasks/<이름>`, 그 밖)가 서로 맞고 실패하면 쓰지 않고 끝난다. 동작이 틀리는 곳을 찾지 못했다
  - 등급: A — 문제 0개
- 보안
  - 핫스팟: `plugins/plate/skills/plan/SKILL.md:137` 에이전트가 `git switch -c tasks/<이름>`, `git rev-parse --verify --quiet refs/heads/tasks/<이름>`을 셸로 부른다 → 안전. `<이름>`은 적는 규칙(235)이 영어 소문자 낱말과 하이픈으로 묶고, 명령 치환 없이 한 명령씩 부르라고 적는다
  - 근거: 비밀, 밖에서 들어온 입력을 셸에 넘기는 곳, 권한 건너뛰기를 새 줄에서 찾지 못했다. 푸시는 하지 않는다고 적는다(plan 절대 규칙 4)
  - 등급: A — 문제 0개
- 유지보수성
  - 근거: `plugins/plate/skills/run/SKILL.md:363` "소스 문제도 하네스 고칠 거리도 없으면 … 묻지 않는다"가 새 갈래를 다루지 않는다. 하네스 고칠 거리가 모두 "eval에만"(또는 감수)이고 소스 문제가 없으면 고칠 안이 모두 비어도 승인을 묻는다. 같은 절 358줄의 "고칠 곳을 말하면"도 사용자가 "eval에만"인 것을 올리자고 할 때 어디로 옮기는지 적지 않는다 (일관성, 15분)
  - 근거: 테스트 파일(`tests/test_skill_rules.py`)의 새 줄은 이 파일의 다른 테스트처럼 `section`/`subsection`/`part`로 절을 잘라 문구를 보는 꼴을 따른다. 문제 없음
  - 부채 비율: 15분 ÷ (128줄 × 30분) = 0.39%
  - 등급: A — 부채 비율 5% 이하
- 테스트 적절성
  - 근거: 결과물인 마크다운만 바뀐 경우의 표로 매김 — 바뀐 코드 파일이 결과물인 마크다운 3개(eval, plan, run의 SKILL.md)와 테스트 파일 1개(`tests/test_skill_rules.py`)뿐이다
  - 근거: eval의 세 기준 가르기는 tasks 완료 조건 5가 작업 트리의 본문을 헤드리스로 돌려 본다(`docs/tasks/plan.md` 완료 조건 5). 돌려 보는 확인
  - 근거: plan의 브랜치 동작은 `docs/tasks/002-plan-branch/plan.md` 완료 조건 4가 (가) 기본 브랜치, (나) 다른 브랜치를 헤드리스로 돌려 본다. 그대로 커밋, 있는 브랜치로 바꿈, 이름 겹침의 갈래는 `돌리지 않음` 줄(17줄)뿐이다(엣지케이스)
  - 근거: run의 "eval에만" 고칠 안 가르기는 주된 동작인데 `grep`과 문구를 보는 unittest(읽기만 하는 확인)와 `돌리지 않음` 줄(`docs/tasks/plan.md` 완료 조건 2, `docs/tasks/001-issue-criteria/plan.md:19`)뿐이다
  - 근거: run 1번의 까닭 글은 동작이 바뀌지 않았다(002 완료 조건 2의 diff 확인)
  - 등급: C — 주된 동작(run의 고칠 안 가르기) 가운데 돌려 보는 확인 없이 읽기만 하는 확인과 `돌리지 않음` 줄만 있는 것이 있다
- 기능 적합성
  - 근거: 완료 조건 1 통과: eval 본문의 네 자리와 테스트
  - 근거: 완료 조건 2 통과: run 본문의 세 자리와 테스트
  - 근거: 완료 조건 3 통과: ADR-026, ADR-025, PRD 8번, ARCHITECTURE 78줄
  - 근거: 완료 조건 4 통과: BACKLOG 하네스 고칠 거리 0개, 절 머리 3개
  - 근거: 완료 조건 5 통과: 기록의 해시가 지금 해시와 같고, 시험 eval.md가 A·B를 기대대로 가른다
  - 근거: 완료 조건 6 통과: 207개 OK
  - 등급: A — 완료 조건의 확인이 모두 통과한다

**Sonar way 게이트**
- 새 문제 0개: 1개. 실패
- 새 보안 핫스팟 모두 검토: 1/1. 통과
- 새 줄 커버리지 80% 이상: 측정 못함 — 커버리지 도구가 없다(잴 새 줄 92줄)
- 새 줄 중복 3% 이하: 측정 못함 — 중복 검사 도구가 없다(잴 새 줄 92줄)
- 게이트: 실패

**소스 문제**
1. run의 "보고하고 묻는다"가 "eval에만" 갈래를 끝까지 다루지 않는다: 고칠 안이 모두 비는 경우(하네스 고칠 거리가 모두 eval에만이나 감수이고 소스 문제가 없을 때)에도 승인을 묻고, 사용자가 eval에만인 것을 고치거나 올리자고 할 때 어디로 옮기는지 적지 않는다 (`plugins/plate/skills/run/SKILL.md:363`, `plugins/plate/skills/run/SKILL.md:358`). 범주: 유지보수성

**하네스에서 걸린 것**
- tasks 머리(`docs/tasks/plan.md`)의 목표와 완료 조건이 task `002-plan-branch`(plan이 `tasks/<이름>`에 커밋한다)를 담지 않는다. task 목록에만 있어 기능 적합성은 001의 조건 여섯으로만 매겼고, 002의 동작은 테스트 적절성의 근거로만 task 머리에서 봤다. plan이 진행 중인 tasks에 task를 더할 때 tasks 머리의 목표와 완료 조건을 고치지 않는다(plan "더하는 경우에는 tasks 머리의 task 목록 절 끝에 승인받은 줄만 더한다")
- 테스트 적절성 C의 까닭(run의 고칠 안 가르기에 돌려 보는 확인이 없음)은 tasks 머리 완료 조건 2의 `돌리지 않음` 줄이 정한 것이라 소스 문제로 넣지 않았다
- 완료 조건 5의 확인은 task 기록(`docs/tasks/001-issue-criteria/done-phase-4.md:28-47`)을 가리켜, 그 줄만 읽어 확인을 돌리는 데 썼다
