# 코드 평가

## 평가 1

**대상**
- 범위: `32e2fbb`(main에서 갈라진 곳)부터 `6292d12`까지
- 결과물인 마크다운 절: `plugins/plate/skills/*/SKILL.md`
- 바뀐 코드 파일 3개, 새 줄 267줄, 잴 새 줄 4줄
  - `plugins/plate/.claude-plugin/plugin.json` +2
  - `plugins/plate/.codex-plugin/plugin.json` +2
  - `plugins/plate/skills/cleanup/SKILL.md` +263 (결과물인 마크다운)

**잰 것**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 104 tests in 16.468s`, `OK`. 통과
- 커버리지: 측정 못함 — 프로젝트에 커버리지 도구가 없다(`docs/ARCHITECTURE.md` 명령 절, ADR-024). 잴 새 줄 4줄은 JSON 매니페스트라 실행되는 줄도 아니다
- 중복: 측정 못함 — 중복 검사 도구가 없다(ADR-024. `jscpd` 없음을 `which`로 확인)
- 정적 분석: `python3 -m json.tool` 두 매니페스트 → 둘 다 올바른 JSON. `claude plugin validate .` → `✔ Validation passed`. 바뀐 코드 파일에 걸린 결과 없음
- 보안 검사: 측정 못함 — 의존성 목록과 보안 검사 도구가 없다(ADR-024. `semgrep`, `bandit`, `pip-audit` 없음을 `which`로 확인)

**완료 조건**
- 1. `plugins/plate/skills/cleanup/SKILL.md`가 있고, 여섯 기준·2라운드 교차 검토·보고서 위치·문서 지도 행·tasks로 만들지 묻고 plan으로 넘기는 절차를 적는다.
  - `test -f plugins/plate/skills/cleanup/SKILL.md` → 0으로 끝남. 통과
  - `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
  - (본문을 읽음) 여섯 기준 `SKILL.md:24-30`, `75-82`, 1라운드 `69-88`, 2라운드 `90-100`, 보고서 위치 `61`, 지도 행 `106-110`, 묻기와 plan 넘김 `116-130`. 통과
- 2. 임시 복제본에서 두 장면으로 돌린 결과가 `docs/TOOLS.md`에 있고 SKILL.md의 마지막 커밋 뒤에 돌린 것이다.
  - `docs/TOOLS.md`의 "cleanup 스킬을 두 장면으로 돌려 본 것" 절을 읽음 → Claude Code 버전 2.1.311(절 머리, 두 장면 공통), 시각(첫 턴 15:39:37~15:56:47, 장면 2 15:57:12~15:57:42, 장면 1 15:58:00~15:58:32), 세션 id(장면 2 `ce76bda6-…`, 장면 1 `56d46cfa-…`), 장면 1의 커밋 파일 목록(`AGENTS.md`, `docs/cleanup/2026-10-27.md`)과 여섯 기준 절, 장면 2의 `plate:plan` 호출 줄이 모두 있다. 통과
  - `git log -1 --format=%cI -- plugins/plate/skills/cleanup/SKILL.md` → `2026-10-27T15:37:12+09:00`. 첫 턴 시작 15:39:37이 더 늦다. 통과
- 3. 두 매니페스트의 버전이 0.15.0이고 cleanup 스킬을 설명에 담는다. 테스트가 통과하고, 맥락 문서와 README가 cleanup 스킬과 어긋나지 않는다.
  - `grep -h '"version"' …` → 두 줄 모두 `"version": "0.15.0",`. 통과
  - `grep -c cleanup …` → 두 파일 모두 1. 통과
  - `python3 -m unittest discover -s tests` → 마지막 줄 `OK`. 통과
  - `docs/PRD.md`(9단계 `19`줄 "cleanup 스킬로 만들었다"), `docs/ARCHITECTURE.md`(구조 `32`줄, 규칙 문단 `49`줄 "여덟 스킬(… cleanup)", 데이터 흐름 `79-84`줄), `README.md`(스킬 수 "열" `3`줄, 표 `16`줄, `/plate:cleanup` `106`줄, `$plate:cleanup` `115`줄, Codex 미확인 목록 `117`줄)를 따로 읽음 → 어긋나는 줄 없음. 통과

**범주**
- 신뢰성
  - 근거: `plugins/plate/skills/cleanup/SKILL.md:16-17` 절대 규칙 1·2가 "`docs/tasks/`의 기록도 고치지 않는다", "쓰는 파일은 그 날의 보고서와 `AGENTS.md` 문서 지도의 행뿐이다. 커밋에도 이 둘만"이라 적는데, `130`줄은 같은 세션에서 `plate:plan`을 불러 plan이 `docs/tasks/`를 쓰고 커밋하게 한다. 절대 규칙 4(`19`줄)는 plan이 묻는 것만 plan의 규칙에 맡기고 쓰기와 커밋은 빼 주지 않아, 규칙을 문자 그대로 따르는 에이전트가 plan의 쓰기나 커밋을 멈출 수 있다. 시험 장면 2는 plan이 묻는 자리에서 끝나 이 길을 지나지 않았다 (기능, 낮음)
  - 그 밖에 읽은 것: 범위·보고서 번호(`56-61`), 지난 보고서(`63-67`), 측정 못함 처리(`84-86`, `100`), 버림·중복·충돌 판정(`94-99`), 묻는 자리의 세 답(`118-124`), 미룸 커밋(`128-129`). 매니페스트 두 파일은 버전과 설명 글만 바뀌었고 올바른 JSON이다
  - 등급: B — 가장 무거운 문제가 낮음
- 보안
  - 핫스팟: `plugins/plate/skills/cleanup/SKILL.md:82` 기존 작업 정합성 에이전트가 `gh issue list --state open`으로 밖에서 들어온 글(공개 저장소면 누구나 쓰는 이슈 제목)을 읽어 판단에 쓴다 → 취약점
  - 핫스팟: `plugins/plate/skills/cleanup/SKILL.md:82` `git log -- docs/tasks/` 실행 → 안전 (저장소 안의 기록만 읽는다)
  - 근거: `plugins/plate/skills/cleanup/SKILL.md:82`, `151-155` 1·2라운드에 맡기는 글이 이슈 글을 지시가 아니라 데이터로만 보라고 적지 않는다. review의 PR 모드는 같은 꼴의 밖에서 들어온 글에 그 규칙을 둔다. 에이전트는 파일을 고치지 않고(`152`) 메인이 tasks로 만들기 전에 사용자에게 묻으므로(`116-124`) 바로 악용할 길은 없다 (낮음)
  - 등급: B — 가장 무거운 문제가 낮음
- 유지보수성
  - 근거: 문제 없음. `SKILL.md` 263줄을 다른 스킬(review, retro)의 꼴(막는 실패, 절대 규칙, 낱말, 번호 절, 맡기는 글, 양식, 적는 규칙, 출처)과 견줘 읽었고, 결과물인 마크다운과 살필 파일의 뜻(`32-34`)은 review의 뜻과 같다고 출처(`262`)에 밝혀 둔다. 두 매니페스트의 설명 글이 같은 것은 갈라진 곳 전부터의 구조다
  - 부채 비율: 0분 ÷ (267줄 × 30분) = 0%
  - 등급: A — 부채 비율 5% 이하
- 테스트 적절성
  - 근거: `tests/`의 세 파일(`test_edit_guard.py`, `test_push_guard.py`, `test_verdict.py`)은 훅과 판정 스크립트만 시험하고, 매니페스트나 스킬 본문을 보는 테스트는 없다(`grep -n -i -E 'version|plugin.json|SKILL' tests/*.py` 결과 없음). 매니페스트는 `claude plugin validate .`이 깨지면 실패한다. cleanup 스킬의 주된 동작(여섯 기준 1라운드, 2라운드 판정, 보고서와 지도 행 커밋, 묻기, plan 넘김, 미룸)은 `docs/TOOLS.md`에 적힌 한 번의 손 시험뿐이고, 스킬이 깨지면 실패하는 되풀이 가능한 테스트가 없다. 이 프로젝트는 스킬을 실행 결과로 판정한다(`docs/ARCHITECTURE.md:46`)
  - 커버리지는 측정 못함이라 판단만으로 매김
  - 등급: D — 주된 동작의 절반 넘게 테스트가 없다
- 기능 적합성
  - 근거: 완료 조건 1 통과: 스킬 본문이 있고 검증을 지난다
  - 근거: 완료 조건 2 통과: 두 장면의 기록이 모두 있고 SKILL.md 마지막 커밋 뒤에 돌렸다
  - 근거: 완료 조건 3 통과: 버전 0.15.0, 설명에 cleanup, 테스트 OK, 세 문서에 어긋남 없음
  - 등급: A — 완료 조건의 확인이 모두 통과한다

**Sonar way 게이트**
- 새 문제 0개: 2개(신뢰성 1, 보안 1, 유지보수성 0). 실패
- 새 보안 핫스팟 모두 검토: 2/2. 통과
- 새 줄 커버리지 80% 이상: 잴 새 줄 4줄(20줄 미만). 보지 않음
- 새 줄 중복 3% 이하: 잴 새 줄 4줄(20줄 미만). 보지 않음
- 게이트: 실패

**소스 문제**
1. 절대 규칙 1·2가 쓰기와 커밋을 보고서와 지도 행으로만 묶어, 7번에서 부른 `plate:plan`이 `docs/tasks/`를 쓰고 커밋하는 것과 부딪힌다. 절대 규칙 4처럼 plan의 쓰기와 커밋도 plan의 규칙에 맡긴다고 적어야 한다 (`plugins/plate/skills/cleanup/SKILL.md:16-19`, `130`). 범주: 신뢰성
2. 기존 작업 정합성이 읽는 열린 이슈의 글을 지시가 아니라 데이터로만 보라는 규칙이 맡기는 글에 없다 (`plugins/plate/skills/cleanup/SKILL.md:82`, `151-155`). 범주: 보안
3. cleanup 스킬의 주된 동작에 되풀이 가능한 테스트가 없고 한 번의 손 시험만 있다 (`plugins/plate/skills/cleanup/SKILL.md`). 범주: 테스트 적절성

**하네스에서 걸린 것**
- 프로젝트의 규칙을 따름: `docs/ARCHITECTURE.md` 명령 절이 커버리지·중복·보안 검사 도구를 찾지 않고 측정 못함으로 적으라고 해(ADR-024) 그대로 적었다. `which`로 흔한 도구가 없는 것만 확인했다.
- tasks 완료 조건 2의 "두 장면이 저마다 Claude Code 버전"을 `docs/TOOLS.md`가 절 머리에 한 번(2.1.311)만 적어 두 장면에 함께 걸었다. 저마다 적은 것으로 읽어 통과로 봤다.
- 스킬 본문이 바뀐 코드의 거의 전부(267줄 가운데 263줄)인데 테스트 적절성 등급표는 실행 코드의 테스트를 가정해, 스킬은 실행 결과로 판정한다는 이 프로젝트의 방식(`docs/ARCHITECTURE.md:46`)과 맞지 않아 D가 나온다.
- 작업 트리에 이 평가 전부터 커밋하지 않은 `docs/tasks/RUNLOG.md` 변경이 있어 커밋에 넣지 않았다.
