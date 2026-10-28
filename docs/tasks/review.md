# 코드 평가

## 평가 1

**대상**
- 범위: `6f9ad57`(main에서 갈라진 곳)부터 `d35a11f`까지
- 결과물인 마크다운 절: `plugins/plate/skills/*/SKILL.md`
- 바뀐 코드 파일 5개, 새 줄 102줄, 잴 새 줄 60줄
  - `plugins/plate/.claude-plugin/plugin.json` +1
  - `plugins/plate/.codex-plugin/plugin.json` +1
  - `tests/test_skill_rules.py` +58
  - `plugins/plate/skills/eval/SKILL.md` +11 (결과물인 마크다운)
  - `plugins/plate/skills/run/SKILL.md` +31 (결과물인 마크다운)

**잰 것**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 202 tests in 16.872s`, `OK`. 통과
- 커버리지: 측정 못함 — 이 환경에 coverage 모듈이 없다(`python3 -m coverage` → `No module named coverage`). 명령 절도 커버리지 도구를 두지 않는다고 적는다(ADR-024)
- 중복: 측정 못함 — 중복 검사 도구(jscpd 같은 것)가 이 환경에 없고 명령 절도 두지 않는다
- 정적 분석: `python3 -m py_compile tests/test_skill_rules.py` → 오류 없음. pyflakes, flake8, ruff, mypy, pylint는 이 환경에 없어 돌리지 않았다
- 보안 검사: 측정 못함 — bandit, semgrep, pip-audit이 이 환경에 없고 의존성 목록도 없다

**완료 조건**
- 1. eval이 처리와 문턱을 적는다
  - `grep -cF -e '<글>' plugins/plate/skills/eval/SKILL.md`를 새 글 여덟마다 → 모두 `1`. 옛 글 `plate 자체의 것에는 이슈로 올릴 제목과 본문을 적는다` → `0`. 통과
  - `done-phase-2.md`의 헤드리스 시험 결과 줄(40~50, 75)과, 그 기록이 가리킨 시험 저장소 `…/scratchpad/evaltest.pKl7`의 `docs/tasks/eval.md`(커밋 `22593d3 greet: 하네스 eval`)를 직접 읽음 → 고칠 거리 1(나)·2(가)는 `문턱: 넘음`과 이슈 제목, 3(다)은 `문턱: 넘지 않음`이고 이슈 제목 없음, (라)는 고칠 거리에 없음, (마)는 "실패" 1~4에 없음, 고칠 거리 넷 모두 `처리:` 줄 있음. 기록의 해시 `6d5fdd8ca384116079edbd4d261c0cc7829ad092`와 지금 `git hash-object plugins/plate/skills/eval/SKILL.md` → 같다. 통과
- 2. #74: eval 2번에 `돌리지 않음` 줄 탓의 등급만 적은 줄은 실패가 아니라는 글이 있다
  - `grep -cF -e '<글>' plugins/plate/skills/eval/SKILL.md` → `1`. 통과
  - 완료 조건 1의 헤드리스 시험에서 (마)가 `eval.md`의 "실패"에 없음 → 위에서 확인. 통과
- 3. run의 tasks 끝이 문턱과 처리를 따른다
  - 새 글 열셋마다 `grep -cF -e` → 모두 `1`. 세 절 머리 `grep -cxF -e` → 저마다 `1`. 옛 글 셋 → 모두 `0`. `grep -cE '^   - BACKLOG로 미룰 것: 소스 문제의 번호$'` → `0`. 통과
  - 돌리지 않음: run의 tasks 끝은 사용자의 답과 `gh`가 있어야 돈다(계획의 결정)
- 4. 맥락 문서가 바뀐 규칙과 맞는다
  - `### ADR-025` → `1`, `ADR-025로 바뀜` → `1`. PRD의 옛 글 → `0`, 새 글 → `1`. ARCHITECTURE의 옛 글 → `0`, 새 글 → `1`. `AGENTS.md`의 새 문서 지도 행 → `1`, 옛 행 → `0`. `docs/BACKLOG.md`의 `## 감수한 것`, `## 소스 문제`, `## 하네스 고칠 거리` → 저마다 `1`. ARCHITECTURE의 `test_skill_rules.py` 줄에 두 글 → 저마다 든다. `sed -n '1,8p' tests/test_skill_rules.py`에 eval의 `#74` → 있다. 통과
- 5. 고친 글이 빠지면 실패하는 테스트가 있고, 모든 테스트가 통과한다
  - `python3 -m unittest discover -s tests` → 마지막 줄 `OK`. 통과
  - `mktemp -d` 사본 넷에서 글을 저마다 지우고(사본에 저마다 1번 있었다) 테스트를 돌림 → `FAIL: test_threshold_and_disposition (test_skill_rules.EvalRulesTest)`, `FAIL: test_74_untested_lines_not_failures (test_skill_rules.EvalRulesTest)`, `FAIL: test_first_proposal_uses_threshold (test_skill_rules.RunRulesTest)`, `FAIL: test_backlog_three_sections (test_skill_rules.RunRulesTest)`가 저마다 나옴. 통과
- 6. 두 매니페스트의 버전이 0.22.0이고 마켓플레이스가 유효하다
  - `grep -h '"version"' …` → 두 줄 모두 `"version": "0.22.0"`. 통과
  - `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과

**범주**
- 신뢰성
  - 근거: `plugins/plate/skills/run/SKILL.md:358-359` 고칠 곳을 말하거나 아무것도 고치지 않겠다고 할 때 BACKLOG로 옮기는 길이 소스 문제와 plate 자체의 하네스 고칠 거리에만 있다. 고침 task에서 뺀 이 프로젝트만의 하네스 고칠 거리는 어디에도 남지 않는데, 같은 본문의 BACKLOG 양식(`:412`)과 같은 뜻의 정의(`:382`)는 하네스 고칠 거리 절에 `갈래: 이 프로젝트만` 항목을 두게 해 그 항목을 채울 길이 없다 (기능, 낮음)
  - 등급: B — 가장 무거운 문제가 낮음
- 보안
  - 핫스팟: 없음. 바뀐 줄에 셸 명령 실행, 밖의 입력 사용, 인증·권한 코드가 없다(테스트는 저장소의 스킬 본문만 읽고, 스킬 본문의 새 줄은 BACKLOG와 eval 기록의 규칙뿐이다)
  - 근거: 바뀐 다섯 파일의 새 줄 102줄을 모두 읽었고 취약점이 없다
  - 등급: A — 문제 0개
- 유지보수성
  - 근거: `plugins/plate/skills/run/SKILL.md:354` 처음 안의 "plate 자체의 하네스 고칠 거리는 문턱을 넘은 것만 이슈로 올릴 것에"와 바로 뒤의 "처리가 감수인 하네스 고칠 거리는 갈래와 상관없이 감수할 것에"가 문턱을 넘은 감수인 것에 겹쳐 두 자리를 가리킨다. 어느 쪽이 먼저인지 적지 않아 읽는 쪽이 맞춰 봐야 한다 (설계·일관성, 10분)
  - 부채 비율: 10분 ÷ (102줄 × 30분) = 0.3%
  - 등급: A — 부채 비율 5% 이하
- 테스트 적절성
  - 근거: 결과물인 마크다운만 바뀐 경우의 표로 매김 — 바뀐 코드 파일이 결과물인 마크다운(eval, run의 `SKILL.md`), 실행 경로 없는 파일(두 매니페스트의 `"version"` 줄), 테스트 파일(`tests/test_skill_rules.py`)뿐이다
  - 근거: eval의 처리·문턱(5번)과 #74(2번)는 완료 조건 1·2의 헤드리스 시험이 돌려 본다(다섯 실패 차림으로 eval을 돌려 `eval.md`를 봄)
  - 근거: run의 tasks 끝(처음 안의 문턱 갈래, 감수할 것, BACKLOG 세 절)은 완료 조건 3의 읽기만 하는 확인(`grep -cF`)과 `돌리지 않음` 줄뿐이다. 이 tasks의 주된 동작 가운데 하나다
  - 근거: (라)의 같은 뜻 가르기는 BACKLOG 항목과 거의 같은 글 한 꼴로만 돌려 봤다(엣지케이스)
  - 등급: C — 주된 동작 가운데 돌려 보는 확인 없이 읽기만 하는 확인과 `돌리지 않음` 줄만 있는 것(run의 tasks 끝)이 있다
- 기능 적합성
  - 근거: 완료 조건 1 통과: grep 아홉과 헤드리스 시험의 `eval.md`, 본문 해시
  - 근거: 완료 조건 2 통과: grep과 (마)가 "실패"에 없음
  - 근거: 완료 조건 3 통과: grep 스물과 `돌리지 않음`(계획의 결정)
  - 근거: 완료 조건 4 통과: ADR, PRD, ARCHITECTURE, AGENTS, BACKLOG, 테스트 머리
  - 근거: 완료 조건 5 통과: 테스트 `OK`와 지운 글마다의 `FAIL:` 넷
  - 근거: 완료 조건 6 통과: 버전 0.22.0 둘과 `✔ Validation passed`
  - 등급: A — 완료 조건의 확인이 모두 통과한다

**Sonar way 게이트**
- 새 문제 0개: 2개(신뢰성 1, 유지보수성 1). 실패
- 새 보안 핫스팟 모두 검토: 0/0. 통과
- 새 줄 커버리지 80% 이상: 측정 못함 — 잴 새 줄 60줄, 커버리지 도구 없음
- 새 줄 중복 3% 이하: 측정 못함 — 잴 새 줄 60줄, 중복 검사 도구 없음
- 게이트: 실패

**소스 문제**
1. tasks 끝에서 고침 task에서 뺀(또는 아무것도 고치지 않기로 한) 이 프로젝트만의 하네스 고칠 거리를 BACKLOG로 옮기는 길이 없어 사라지고, BACKLOG 양식의 하네스 고칠 거리 절이 허용하는 `갈래: 이 프로젝트만` 항목은 채워질 길이 없다 (`plugins/plate/skills/run/SKILL.md:358`). 범주: 신뢰성
2. 처음 안의 문턱 갈래 글과 감수 갈래 글이 문턱을 넘은 감수인 plate 자체의 것에 겹쳐 두 자리를 가리키고 어느 쪽이 먼저인지 적지 않았다 (`plugins/plate/skills/run/SKILL.md:354`). 범주: 유지보수성

**하네스에서 걸린 것**
- 완료 조건 1의 둘째 확인이 phase 2 기록을 가리켜, 그 확인에 필요한 줄(`done-phase-2.md`의 시험 결과와 해시 줄)만 읽었다(review 1번의 예외). 기록이 가리킨 시험 저장소의 `eval.md`도 직접 읽어 맞춰 봤다. 등급의 근거로는 쓰지 않았다
- 명령 절에 빌드·린트가 "없음"이고 커버리지·중복·보안 검사 도구를 두지 않아(ADR-024) 게이트의 커버리지와 중복이 측정 못함이다
- 테스트 적절성 C는 완료 조건 3의 `돌리지 않음` 줄(계획의 결정: run의 tasks 끝은 사용자의 답과 `gh`가 있어야 돈다) 때문이다. 계획의 결정이 정한 것이라 소스 문제로 적지 않았다
