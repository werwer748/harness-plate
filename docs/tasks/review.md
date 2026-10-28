# 코드 평가

## 평가 1

**대상**
- 범위: `fc4358e`(main에서 갈라진 곳)부터 `9835d8f`까지
- 결과물인 마크다운 절: `plugins/plate/skills/*/SKILL.md`
- 바뀐 코드 파일 4개, 새 줄 12줄, 잴 새 줄 10줄
  - `plugins/plate/.claude-plugin/plugin.json` +1
  - `plugins/plate/.codex-plugin/plugin.json` +1
  - `tests/test_skill_rules.py` +8
  - `plugins/plate/skills/plan/SKILL.md` +2 (결과물인 마크다운)

**잰 것**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 193 tests`, 마지막 줄 `OK`. 통과
- 커버리지: 측정 못함 — 명령 절이 커버리지 도구를 두지 않는다고 적었고(ADR-024), `python3 -m coverage`는 `No module named coverage`
- 중복: 측정 못함 — 명령 절이 중복 도구를 두지 않는다고 적었고, `jscpd`가 이 환경에 없다
- 정적 분석: 측정 못함 — `ruff`, `pyflakes`, `mypy`, `pylint`가 이 환경에 없다
- 보안 검사: 측정 못함 — 명령 절이 보안 검사 도구를 두지 않는다고 적었고(의존성 목록도 없다), `semgrep`, `bandit`이 이 환경에 없다

**완료 조건**
- 1. plan 본문에 #65의 해결이 제자리에 있고 기존 규칙과 한 항목으로 이어진다
  - `grep -cF '<글>' plugins/plate/skills/plan/SKILL.md`를 세 글마다 → `1`, `1`, `1`. 통과
  - `grep -F '- 확인은 돌릴 명령과 기대 결과를 우선한다.' plugins/plate/skills/plan/SKILL.md` → `invalid option - 확인은 …`, 종료 코드 2. 패턴이 `-`로 시작해 옵션으로 읽혔다. 실패. 같은 뜻으로 `grep -F -e '…'`로 돌리면 한 줄이 나오고 두 글이 모두 든다(저마다 `grep -cF` → `1`). 결과물의 동작은 맞다
  - 돌리지 않음 줄: plan은 사람에게 묻고 초안마다 승인을 받는 스킬이라는 까닭이 적혀 있다
- 2. 고친 글이 빠지면 실패하는 테스트가 있고, 모든 테스트가 통과한다
  - `python3 -m unittest discover -s tests` → 마지막 줄 `OK`. 통과
  - `mktemp -d` 사본에 `plugins`, `tests`를 `cp -R`, 글 `값을 뽑아 견주는 확인은 뽑는 명령(또는 패턴)과 견주는 법을 적는다` 수 `1`, 빈 글로 바꾸고 테스트 → `FAIL: test_65_comparison_checks_name_extract_command (test_skill_rules.PlanRulesTest)`. 통과
  - 새 사본에서 글 `값을 뽑아 견주는 확인에 뽑는 명령과 견주는 법이 있는지 본다`를 빈 글로 → `FAIL: test_65_comparison_checks_name_extract_command (test_skill_rules.PlanRulesTest)`. 통과
- 3. 두 매니페스트의 버전이 0.20.0이고, 마켓플레이스가 유효하고, 테스트의 설명 글이 더한 규칙과 맞는다
  - `grep -h '"version"' …/.claude-plugin/plugin.json …/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "0.20.0",`. 통과
  - `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
  - `grep -c '값을 뽑아 견주는 확인' docs/ARCHITECTURE.md` → `1`, 그 줄은 39줄 `└── test_skill_rules.py` 줄. `sed -n '1,8p' tests/test_skill_rules.py`의 plan 목록에 `#65`가 있다(3줄). 통과

**범주**
- 신뢰성
  - 근거: `plugins/plate/skills/plan/SKILL.md:256`의 이어 적은 글과 `:109`의 6번 점검 줄을 그 절 전체에 대어 읽었다. 기존 항목과 뜻이 겹치거나 어긋나지 않고, 6번 줄의 "없으면 … 읽어서 견줄 자리를 적는다"가 256줄의 갈래와 같다. `tests/test_skill_rules.py:596-601`은 기존 헬퍼 `section`, `part`(79줄)를 기존 테스트와 같은 방식으로 쓰고, 테스트 193개가 통과한다. 문제 없음
  - 등급: A — 문제 0개
- 보안
  - 핫스팟: 없음. 새 줄에 셸 실행, 밖의 입력, 경로 사용이 없다(테스트의 새 줄은 문자열 포함 검사뿐, 매니페스트는 버전 값뿐)
  - 근거: 바뀐 코드 파일 네 개의 새 줄 12줄을 모두 읽었다. 문제 없음
  - 등급: A — 문제 0개
- 유지보수성
  - 근거: 새 테스트 이름 `test_65_…`과 꼴이 같은 클래스의 `#52`~`#57` 테스트와 같다(`tests/test_skill_rules.py:596`). 모듈 docstring의 plan 목록에 `#65`가 더해졌다(`tests/test_skill_rules.py:3`). plan 본문의 두 줄은 tasks 머리의 결정(기존 항목에 이어 적고 6번에 한 줄)대로다. 문제 없음
  - 부채 비율: 0분 ÷ (12줄 × 30분) = 0%
  - 등급: A — 부채 비율 5% 이하
- 테스트 적절성
  - 근거: 바뀐 코드 파일에 실행 코드인 `tests/test_skill_rules.py`가 있어 결과물인 마크다운만 바뀐 경우의 표가 아니라 기본 등급표를 썼다. 커버리지는 측정 못함이라 판단만으로 매긴다
  - 근거: 바뀐 동작(plan 본문의 #65 규칙 글 두 자리)은 `tests/test_skill_rules.py:596-601`이 본다. 사본에서 글 하나씩 지웠을 때 저마다 `FAIL: test_65_comparison_checks_name_extract_command`가 나와 깨지면 실패함을 확인했다. 테스트는 `assertIn` 세 줄로 단순하다
  - 근거: 고친 규칙대로 plan이 초안을 적는지는 돌리지 않았다(완료 조건 1의 `돌리지 않음` 줄). 테스트는 글이 제자리에 있는지만 본다
  - 등급: A — 바뀐 동작마다 깨지면 실패할 테스트가 있다(커버리지 측정 못함, 판단만으로 매김)
- 기능 적합성
  - 근거: 완료 조건 1 실패: 두 번째 확인 명령 `grep -F '- 확인은 …'`이 패턴을 옵션으로 읽어 돌지 않는다. `-e`로 돌리면 기대대로라 결과물의 동작은 맞다
  - 근거: 완료 조건 2 통과: 테스트 `OK`, 두 글을 지우면 저마다 `test_65_…`가 실패
  - 근거: 완료 조건 3 통과: 두 버전 `0.20.0`, `✔ Validation passed`, ARCHITECTURE와 docstring이 맞다
  - 등급: B — 실패한 확인이 있지만 결과물의 동작은 맞다(확인 명령이 틀렸다)

**Sonar way 게이트**
- 새 문제 0개: 0개. 통과
- 새 보안 핫스팟 모두 검토: 0/0. 통과
- 새 줄 커버리지 80% 이상: 측정 못함, 잴 새 줄 10줄로 20줄 미만. 보지 않음
- 새 줄 중복 3% 이하: 측정 못함, 잴 새 줄 10줄로 20줄 미만. 보지 않음
- 게이트: 통과

**소스 문제**
없음

**하네스에서 걸린 것**
- tasks 머리와 task 머리의 완료 조건 1 두 번째 확인 `grep -F '- 확인은 돌릴 명령과 기대 결과를 우선한다.' …`이 `-`로 시작하는 패턴을 `-e`나 `--` 없이 넘겨 옵션으로 읽힌다(이 환경의 `grep`은 ugrep이지만 GNU·BSD grep도 같다). 결과물이 아니라 계획의 확인 명령이 틀린 것이라 소스 문제에 넣지 않았다. plan의 6번 초안 점검에 "`-`로 시작하는 패턴은 `-e`로 넘기는지 본다" 같은 줄이 없어 초안 단계에서 잡히지 않았다
- review의 테스트 적절성 표 고르기: 결과물인 마크다운과 매니페스트 버전 말고는 그 글을 보는 테스트 파일만 바뀐 tasks도 테스트 파일이 실행 코드라 기본 등급표를 쓰게 된다. 실제 바뀐 제품 동작(스킬 본문)은 `돌리지 않음`인데 글 존재 테스트로 A가 나온다. 테스트 파일만 실행 코드인 경우를 어느 표로 매길지 본문에 없다
