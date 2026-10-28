# Phase 2: TOOLS.md를 줄이고 시험 실행 기록 규칙을 바꾼다

**목표**: `docs/TOOLS.md`가 계속 쓰이는 도구 사실만 담아 15KB 이하가 되고, plan과 ARCHITECTURE가 시험 실행 기록을 맥락 문서에 적지 않게 한다.

**테스트 먼저**: 아니오 — 맥락 문서와 스킬 본문(`.md`), 그 글을 지키는 테스트만 바꾼다

**읽을 것**
- `docs/TOOLS.md` (전체. 남길 절: 머리글과 `## 지금 상태`, `## Claude Code`의 첫 목록, `서브에이전트, 권한, worktree`, `훅`, `세션 도중의 스킬 본문 고침`, `ruleset과 CODEOWNERS로 워크플로 PR의 자동 머지를 막는지 본 것`, `플러그인 폴더의 편집과 권한 모드`, `스킬을 헤드리스로 돌려 볼 때의 허용 목록`, `## Codex`부터 끝까지. 지울 절: "판정에서 본 것", "돌려 본 것"이 제목에 든 그 밖의 절들)
- `AGENTS.md` (작업 규칙의 마지막 줄이 `플러그인 폴더의 편집과 권한 모드`를 가리킨다)
- `docs/ADR.md` (ADR-018, ADR-023이 TOOLS.md와 그 절을 가리킨다)
- `docs/ARCHITECTURE.md` (`## 기술 스택`의 대상 도구 줄, `## 패턴과 규칙`의 `docs/TOOLS.md`에 적는다는 줄과 작업 트리의 스킬 줄 예외 줄, CI 줄의 "`docs/TOOLS.md`에서 시험한 JSON의 `gh api` 명령")
- `README.md` (Codex 확인을 멈춘 상태를 말하는 줄)
- `plugins/plate/skills/plan/SKILL.md` (`## 적는 규칙`의 **조건**)
- `tests/test_skill_rules.py` (`PlanRulesTest`)

**TODO**
- [ ] 지울 절에 다음 계획이 알아야 할 도구 동작이 있으면 버전과 함께 한 줄로 남길 절에 옮기고, 지울 절을 모두 지운다. 남길 절도 임시 경로, 본문 해시, 커밋 id, 장면의 차림을 빼고 사실 위주로 줄인다. ruleset 절은 거는 `gh api` 명령과 JSON, PR을 연 계정이 유일한 코드 소유자면 막지 못한다는 사실을 남긴다. 머리글은 이 문서가 도구 사실과 확인을 멈춘 지점만 담고 시험 실행 기록은 담지 않는다고 바뀐다. 파일은 15360바이트 이하가 된다 (`docs/TOOLS.md`)
- [ ] plan `적는 규칙`의 **조건**에, 돌려 본 확인의 결과(차림, 출력, 본문 해시)는 그 phase의 기록에만 남기고 맥락 문서에 옮겨 적는 TODO나 조건을 두지 않으며, 맥락 문서에는 다음 계획이 알아야 할 도구 동작만 한 줄로 더한다는 규칙이 더해진다 (`plugins/plate/skills/plan/SKILL.md`)
- [ ] `PlanRulesTest`에 그 규칙의 글이 **조건**에 있는지 보는 테스트가 더해진다 (`tests/test_skill_rules.py`)
- [ ] ARCHITECTURE `## 패턴과 규칙`의 "도구마다 다른 동작과 확인을 멈춘 지점은 `docs/TOOLS.md`에 적는다" 줄에 시험 실행 기록은 적지 않고 phase 기록에 둔다는 글이 더해지고, `test_skill_rules.py` 줄의 테스트 설명에 새 테스트가 다루는 규칙이 더해진다. 남긴 절을 가리키는 `AGENTS.md`, ADR-018·ADR-023, README, ARCHITECTURE의 줄은 절 이름이 그대로라 고치지 않는다 (`docs/ARCHITECTURE.md`)

**통과 조건**
- TOOLS.md가 줄고 가리키는 절과 ruleset 명령이 남고 시험 실행 기록이 없다. (완료 조건 2)
  - 확인: `wc -c < docs/TOOLS.md`가 15360 이하다
  - 확인: `플러그인 폴더의 편집과 권한 모드`, `세션 도중의 스킬 본문 고침`, `ruleset과 CODEOWNERS로 워크플로 PR의 자동 머지를 막는지 본 것`, `도구를 넓힐 때 할 것`마다 `grep -c '<절 이름>' docs/TOOLS.md`가 1 이상이다
  - 확인: `grep -c 'rulesets --input -' docs/TOOLS.md`와 `grep -c '"enforcement"' docs/TOOLS.md`가 저마다 1 이상이다
  - 확인: `grep -cE '/var/folders/|tmp\.[A-Za-z0-9]{6,}|장면 [A-Z]' docs/TOOLS.md`가 0이다
- plan과 ARCHITECTURE가 시험 실행 기록을 맥락 문서에 적지 않게 한다. (완료 조건 3)
  - 확인: `python3 -m unittest discover -s tests`가 `OK`로 끝나고, 새 테스트가 plan `적는 규칙`의 **조건** 부분에서 그 규칙의 글을 단언한다
  - 확인: ARCHITECTURE `## 패턴과 규칙`의 TOOLS.md 줄을 읽어 "도구마다 다른 동작과 확인을 멈춘 지점"과 "시험 실행 기록은 적지 않는다"가 둘 다 있다
- 앞 phase가 고친 규칙이 그대로다. (완료 조건 1, 4)
  - 확인: `git grep -n 'TOOLS.md' -- plugins/`가 아무것도 내지 않는다
  - 확인: `git grep -nE '사용량.*TOOLS\.md|TOOLS\.md.*사용량' -- docs/PRD.md docs/ARCHITECTURE.md docs/ADR.md README.md AGENTS.md`가 아무것도 내지 않는다
