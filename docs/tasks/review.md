# 코드 평가

## 평가 1

**대상**
- 범위: `7991971`(main에서 갈라진 곳)부터 `6191642`까지
- 결과물인 마크다운 절: `plugins/plate/skills/*/SKILL.md`
- 바뀐 코드 파일 6개, 새 줄 74줄, 잴 새 줄 61줄
  - `plugins/plate/.claude-plugin/plugin.json` +1
  - `plugins/plate/.codex-plugin/plugin.json` +1
  - `tests/test_skill_rules.py` +59
  - `plugins/plate/skills/plan/SKILL.md` +2 (결과물인 마크다운)
  - `plugins/plate/skills/retro/SKILL.md` +7 (결과물인 마크다운)
  - `plugins/plate/skills/run/SKILL.md` +4 (결과물인 마크다운)

**잰 것**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 275 tests in 26.332s`, `OK`. 통과
- 커버리지: 측정 못함 — 명령 절이 커버리지 도구를 두지 않고(ADR-024) 이 환경에 `coverage` 모듈도 없다
- 중복: 측정 못함 — 명령 절이 중복 검사 도구를 두지 않고 이 환경에 `jscpd` 같은 도구가 없다
- 정적 분석: `python3 -m py_compile tests/test_skill_rules.py` → 오류 없음. `python3 -m json.tool`로 두 매니페스트 → 둘 다 올바른 JSON. `claude plugin validate plugins/plate` → `✔ Validation passed`. ruff·pyflakes·mypy 같은 도구는 이 환경에 없다
- 보안 검사: 측정 못함 — 의존성 목록이 없고 `semgrep`, `bandit`, `pip-audit`이 이 환경에 없다

**완료 조건**
- 1. 테스트 묶음이 모두 통과한다.
  - `python3 -m unittest discover -s tests` → 마지막 줄 `OK`. 통과
- 2. plan의 초안 점검과 **조건**, retro 4번이 세 경우를 확인 하나씩으로 덮게 한다. 테스트가 그 글을 지킨다.
  - `grep -n '합쳐지지 않은 다른 브랜치' plugins/plate/skills/plan/SKILL.md plugins/plate/skills/retro/SKILL.md` → plan 115(6번, 102~136줄 안), plan 266(적는 규칙의 **조건** 안), retro 79(4번, 64~84줄 안). 통과
  - `cp -R` 사본에서 `sed -i '' '/합쳐지지 않은 다른 브랜치/d'`로 두 본문의 그 줄을 지우고 `python3 -m unittest tests.test_skill_rules.PlanRulesTest.test_80_names_left_anywhere_covered tests.test_skill_rules.RetroRulesTest.test_80_retro_names_left_anywhere` → `FAILED (failures=3)`. 통과
  - 돌리지 않음 줄(plan은 묻는 스킬): 확인이 아니라 적어 둔다
- 3. retro의 "task의 커밋"이 task 머리를 마지막으로 더한 커밋 뒤의 커밋만 센다.
  - 헤드리스 시험: 시험 레포 A(셋업된 꼴, `plan: 옛 tasks` → `001-x: phase 1`(old.txt) → `tasks 비움` → `plan: 새 tasks` → `001-x: phase 1`(new.txt와 `done-phase-1.md`))에서 `claude -p '/plate:retro 001-x' --plugin-dir /Users/hugo/Desktop/harness-plate/plugins/plate --permission-mode bypassPermissions` → `판정: 통과`. 시험 레포의 `retro.md`에서 `grep -c 'old.txt'` → 0, `grep -c 'new.txt'` → 2. 통과
- 4. retro는 결정이 정한 동작이 세 경우에서 목표를 해치면 문제(기준: 계획, 고칠 쪽: 계획)로 판정하고, run 8번은 멈춘다.
  - 헤드리스 시험: 시험 레포 B(목표 "새 보고서 이름이 다른 브랜치의 보고서와 겹치지 않는다", 결정 "`new_report.sh`는 작업 트리의 `reports/`만 보고 없는 번호를 고른다", 합쳐지지 않은 로컬 브랜치 `report/a`에 `reports/1.md`)에서 같은 꼴로 `/plate:retro 001-report` → 첫 줄 `판정: 문제 있음`, `retro.md` 17줄에 `기준: 계획`과 `고칠 쪽: 계획`. 통과
  - `grep -n '고칠 쪽' plugins/plate/skills/run/SKILL.md` → 209(8번 "고칠 phase를 더한다"), 298("멈춘다"), 그 밖에 108, 593. 통과
  - `cp -R` 사본에서 `sed -i '' '/고칠 쪽/d' plugins/plate/skills/run/SKILL.md` 뒤 `RunRulesTest.test_80_plan_side_problem_stops` → `FAILED (failures=1)`. 그 글을 지키는 시험이 있다. 통과
  - 두 헤드리스 시험 전후로 이 저장소의 `git status --porcelain`과 `git rev-parse HEAD`가 같다. 시험에 쓴 retro 본문 해시 `684f526efee0df1a7a919100a95275fc794d0592`(작업 트리)
- 5. 맥락 문서가 바뀐 동작과 맞다.
  - `grep -n '고칠 쪽' docs/PRD.md docs/ARCHITECTURE.md` → PRD 17(핵심 기능 7), ARCHITECTURE 55(run 문단), 75(데이터 흐름의 실행), 101(멈춤 문단). `grep -n -F 'test_skill_rules.py' docs/ARCHITECTURE.md` → 40줄에 `합쳐지지 않은 다른 브랜치`, `task 머리를 마지막으로 더한 커밋`, `고칠 쪽이 계획`. 통과
- 6. 두 매니페스트의 버전이 1.0.0이고 PRD의 1.0.0 줄이 낸 것으로 맞다.
  - `grep -n '"version"' …` → 두 줄 모두 `"version": "1.0.0"`. `grep -n '1.0.0' docs/PRD.md` → 21줄 `9단계까지 만들어 1.0.0을 냈다.` 통과

**범주**
- 신뢰성
  - 근거: 문제 없음. retro 낱말의 "task의 커밋"(`plugins/plate/skills/retro/SKILL.md:31`)은 `git log -1 --diff-filter=A` 로 마지막 더함을 찾고 없을 때의 갈래(역사 전체)를 적어, 지난 tasks의 같은 이름 커밋을 빼는 것을 시험 레포 A에서 돌려 봤다. retro 4번(`retro/SKILL.md:77`, `:79`)과 5번(`:92`), 양식(`:152`), 적는 규칙(`:174`~`:175`)이 "고칠 쪽: 계획"을 서로 어긋남 없이 다루고, 시험 레포 B에서 그대로 판정이 났다. run 2번(`run/SKILL.md:108`), 8번(`:209`), 멈춘다(`:298`), RUNLOG 규칙(`:593`)이 같은 멈춤 자리를 말한다. plan 6번(`plan/SKILL.md:115`)과 **조건**(`:266`)은 같은 세 경우를 든다. 테스트 묶음 275개 통과
  - 등급: A — 문제 0개
- 보안
  - 핫스팟: `plugins/plate/skills/retro/SKILL.md:31` 회고가 돌리는 `git log -1 --diff-filter=A --format=%H -- <task 폴더>/plan.md` → 안전 (읽기만 하는 git 명령이고, 경로는 저장소 안의 task 폴더 이름이며 `--` 뒤에 놓여 옵션으로 읽히지 않는다)
  - 근거: 문제 없음. 그 밖의 새 줄은 매니페스트의 버전 값, 본문의 규칙 글, 본문 글을 읽어 견주는 단위 시험이라 입력을 실행하거나 비밀을 다루는 곳이 없다
  - 등급: A — 문제 0개
- 유지보수성
  - 근거: 문제 없음. 새 시험 다섯(`tests/test_skill_rules.py:214`, `:1082`, `:1165`, `:1176`, `:1199`의 `test_80_plan_side_problem_stops`, `test_80_names_left_anywhere_covered`, `test_80_task_commits_after_task_head`, `test_80_decided_gap_is_plan_problem`, `test_80_retro_names_left_anywhere`)은 파일의 기존 `section`·`part`·`subTest` 꼴을 따르고, 옛 시험(`test_80_decided_behavior_with_repeated_names_goes_out_of_bounds`)은 바뀐 규칙에 맞춰 이름과 기대를 함께 바꿨다. 본문의 고친 줄은 같은 세 경우를 plan·retro에 같은 낱말로 적어 서로 견줄 수 있다
  - 부채 비율: 0분 ÷ (74줄 × 30분) = 0%
  - 등급: A — 부채 비율 5% 이하
- 테스트 적절성
  - 근거: 결과물인 마크다운만 바뀐 경우의 표로 매김 — 바뀐 코드 파일이 결과물인 마크다운(plan·retro·run 본문), 실행 경로 없는 파일(두 매니페스트의 `"version"` 줄), 테스트 파일(`tests/test_skill_rules.py`)뿐이다
  - 근거: retro의 "task의 커밋"(tasks 완료 조건 3)과 retro의 계획 쪽 문제 판정(완료 조건 4의 첫 확인)은 헤드리스 시험으로 돌려 보는 확인이 있다. 버전은 `claude plugin validate`로 돌려 본다(002 완료 조건 1)
  - 근거: plan 6번·**조건**의 세 경우(`plugins/plate/skills/plan/SKILL.md:115`, `:266`, tasks 완료 조건 2)와 run 8번의 고칠 쪽 계획에서의 멈춤(`plugins/plate/skills/run/SKILL.md:209`, 완료 조건 4)은 grep과 그 글을 지키는 단위 시험(읽기만 하는 확인)과 `돌리지 않음` 줄뿐이다. 둘 다 요청의 주된 동작이다
  - 등급: C — 주된 동작 가운데 돌려 보는 확인 없이 읽기만 하는 확인이나 `돌리지 않음` 줄만 있는 것이 있다(다섯 동작 가운데 둘이라 절반을 넘지 않는다)
- 기능 적합성
  - 근거: 완료 조건 1 통과: 테스트 묶음 `OK`
  - 근거: 완료 조건 2 통과: 세 자리의 줄과 그 줄을 지우면 실패하는 시험
  - 근거: 완료 조건 3 통과: 시험 레포 A의 회고가 old.txt를 적지 않는다
  - 근거: 완료 조건 4 통과: 시험 레포 B의 `판정: 문제 있음`과 `기준: 계획`, run의 8번·멈춘다 줄과 지키는 시험
  - 근거: 완료 조건 5 통과: PRD·ARCHITECTURE의 다섯 자리
  - 근거: 완료 조건 6 통과: 두 매니페스트 1.0.0, PRD 21줄
  - 등급: A — 완료 조건의 확인이 모두 통과한다

**Sonar way 게이트**
- 새 문제 0개: 0개. 통과
- 새 보안 핫스팟 모두 검토: 1/1. 통과
- 새 줄 커버리지 80% 이상: 측정 못함 — 잴 새 줄 61줄, 커버리지 도구 없음
- 새 줄 중복 3% 이하: 측정 못함 — 잴 새 줄 61줄, 중복 검사 도구 없음
- 게이트: 통과

**소스 문제**
1. plan 6번·**조건**의 세 경우 규칙과 run 8번의 고칠 쪽 계획에서의 멈춤에 돌려 보는 확인이 없고, grep·단위 시험과 `돌리지 않음` 줄만 있다 (`plugins/plate/skills/plan/SKILL.md:115`, `plugins/plate/skills/run/SKILL.md:209`). 범주: 테스트 적절성

**하네스에서 걸린 것**
- 명령 절이 커버리지·중복·보안 검사를 두지 않아(ADR-024) 잴 새 줄이 61줄인데 게이트의 커버리지와 중복이 측정 못함이다.
- plan과 run은 묻거나 에이전트를 띄우는 스킬이라 헤드리스로 끝까지 돌리지 못해, 그 규칙을 바꾸는 tasks는 테스트 적절성이 C를 넘기 어렵다. 지난 tasks(cleanup-branch)의 평가에서도 같은 까닭으로 C였다.
