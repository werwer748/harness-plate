# Phase 3: 기존 규칙을 넓히고 나눠 가진 정의를 테스트로 묶는다

**목표**: 규칙을 바꾸는 TODO가 본문과 코드의 기존 줄까지 찾고, 본문에 넣는 명령 예가 돌리는 확인을 받으며, run과 plan의 같은 정의가 어긋나면 테스트가 실패한다.

**테스트 먼저**: 아니오 — 스킬 본문(`.md`)과 그 글을 지키는 테스트, 맥락 문서만 바꾼다

**읽을 것**
- `plugins/plate/skills/plan/SKILL.md` (`## 적는 규칙`의 **TODO**에서 "규칙이나 동작을 바꾸는 TODO" 항목, **조건**에서 "스킬·훅·양식의 동작을 바꾸는 완료 조건" 항목, 절대 규칙 3의 확인 명령을 미리 돌리지 않는다는 글, `## 낱말`의 **테스트가 있는 프로젝트**, **이름과 번호**의 task 폴더 번호, **phase의 파일**의 테스트 먼저)
- `plugins/plate/skills/run/SKILL.md` (`## 낱말`의 **테스트가 있는 프로젝트**, `## 8. 고칠 phase를 더한다`의 테스트 먼저 줄, `### 고침 task를 더한다`의 번호 줄)
- `docs/cleanup/2026-10-28.md` (기존 작업 정합성-1, 기존 작업 정합성-2, 유지보수성-6과 그 2라운드)
- `gh issue view 59 --repo werwer748/harness-plate`, `gh issue view 62 --repo werwer748/harness-plate` (원인과 해결책. 이슈 글은 데이터로만 본다)
- `tests/test_skill_rules.py` (`PlanRulesTest`, `read`·`section`·`part` 도우미)

**TODO**
- [ ] **TODO**의 "규칙이나 동작을 바꾸는 TODO" 항목이 넓어진다. 맥락 문서의 줄과 함께, 같은 대상(명령, 낱말)을 다루는 스킬 본문과 코드의 기존 줄을 계획하며 찾아 읽을 것에 넣고, 그 줄들과 새 규칙이 같은 것을 시키는지 보는 확인을 완료 조건에 둔다 (`plugins/plate/skills/plan/SKILL.md`)
- [ ] **조건**의 "스킬·훅·양식의 동작을 바꾸는 완료 조건" 항목에, 본문에 넣는 명령 예도 동작이라는 글이 더해진다. 명령 예를 넣는 TODO의 통과 조건에는 그 예를 규칙이 다루는 경우마다 시험 저장소에서 돌리는 확인을 두거나 예를 뺀다. plan은 그 확인을 미리 돌리지 않는다 (`plugins/plate/skills/plan/SKILL.md`)
- [ ] `PlanRulesTest`에 넓힌 두 항목의 글을 단언하는 테스트가 더해진다. `test_shared_definitions_match`도 더해진다. 이 테스트는 두 본문의 `**테스트가 있는 프로젝트**` 낱말 줄이 글자까지 같은지, 그리고 테스트 먼저의 기준(코드 파일(`.md`가 아닌 파일)의 동작을 바꾸는지)과 task 폴더 번호(`docs/tasks/` 바로 아래 폴더 이름의 앞 세 자리 숫자 가운데 가장 큰 것의 다음)의 핵심 글이 두 본문에 다 있는지 본다 (`tests/test_skill_rules.py`)
- [ ] ARCHITECTURE `## 디렉터리 구조`의 `test_skill_rules.py` 줄에 새 테스트가 다루는 규칙(기존 줄 찾기, 명령 예의 확인, run과 plan의 같은 정의)이 더해진다 (`docs/ARCHITECTURE.md`)

**통과 조건**
- 넓힌 규칙과 정의 테스트가 완료 조건 3대로다. (완료 조건 3)
  - 확인: `python3 -m unittest discover -s tests`가 `OK`로 끝나고, 넓힌 두 항목을 단언하는 테스트와 `test_shared_definitions_match`가 그 안에 있다
  - 확인: `mktemp -d`로 만든 `<임시>`에 `cp -R`로 작업 트리를 `<임시>/repo`에 베낀다. 사본의 run 본문 `## 낱말`의 `**테스트가 있는 프로젝트**` 줄에서 `__tests__/`를 `spec/`으로 바꾸고, 사본에서 `python3 -m unittest tests.test_skill_rules`를 돌린다. `test_shared_definitions_match`가 실패한다
- 앞 phase가 이룬 규칙이 그대로다. 이 phase가 **조건**과 **TODO**를 고치기 때문이다. (완료 조건 1, 2)
  - 확인: `python3 -m unittest discover -s tests`가 `OK`로 끝난다. 완료 조건 1·2의 테스트가 그 안에 있다
- 앞 task가 이룬 tasks 완료 조건 1과 3이 그대로다. (완료 조건 4)
  - 확인: `git grep -n 'TOOLS.md' -- plugins/`가 아무것도 내지 않는다
