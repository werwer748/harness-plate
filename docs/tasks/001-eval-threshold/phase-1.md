# Phase 1: run의 처음 안과 BACKLOG가 문턱과 처리를 따른다

**목표**: run 본문의 tasks 끝(보고, 고칠 안, 처음 안, BACKLOG를 고친다)과 BACKLOG 양식이 task 머리의 결정대로 바뀌고 그 글을 지키는 테스트가 더해진다.

**테스트 먼저**: 아니오 — 동작을 바꾸는 것은 스킬 본문(`.md`)이고, 테스트는 그 글을 지킨다

**읽을 것**
- `plugins/plate/skills/run/SKILL.md` (낱말의 `docs/BACKLOG.md`와 "하네스 고칠 거리", "보고하고 묻는다", "BACKLOG를 고친다", "고침 task를 더한다"의 범위 밖 줄)
- `tests/test_skill_rules.py` (`RunRulesTest`, 특히 `test_template_reading_rule_in_one_place`가 세는 가리킴 다섯)
- `docs/ADR.md`의 ADR-020
- `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/TOOLS.md`, `docs/BACKLOG.md`, `docs/cleanup/2026-10-28.md` (맥락 문서)

**TODO**
- [ ] 낱말의 `docs/BACKLOG.md` 정의가 `미룬 소스 문제와 하네스 고칠 거리, 감수한 것을 tasks를 넘어 모으는 문서`를 담게 바뀌고, "하네스 고칠 거리" 낱말에 eval이 적는 처리와 문턱이 더해진다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] "보고하고 묻는다"의 4번에 `나눠 번호, 글, 처리와, plate 자체의 것은 문턱을 넘었는지`가 들고, 6번 고칠 안에 `- 감수할 것: 처리가 감수인 하네스 고칠 거리의 번호`가 더해지고, BACKLOG로 미룰 것 줄이 `- BACKLOG로 미룰 것: 소스 문제의 번호와, 문턱을 넘지 않은 plate 자체의 하네스 고칠 거리의 번호`로 바뀐다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] 처음 안 문단이 task 머리의 결정 "run의 처음 안"대로 바뀌어 `plate 자체의 하네스 고칠 거리는 문턱을 넘은 것만 이슈로 올릴 것에, 넘지 않은 것은 BACKLOG로 미룰 것에 둔다`와 `처리가 감수인 하네스 고칠 거리는 갈래와 상관없이 감수할 것에 둔다`가 들고, 옛 글 `plate 자체의 하네스 고칠 거리는 모두 이슈로 올릴 것에 두고`가 지워진다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] 고칠 곳을 말할 때의 줄에 `이슈로 올릴 것에서 뺀 하네스 고칠 거리는 BACKLOG로 미룰 것으로 옮긴다`가 더해지고, 아무것도 고치지 않겠다는 답의 줄이 `소스 문제와 plate 자체의 하네스 고칠 거리를 모두 BACKLOG로 미룰 것에 둔 안`으로 바뀌어 옛 글 `소스 문제를 모두 BACKLOG로 미룰 것에 둔 안`이 지워진다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] "BACKLOG를 고친다"에 `미룰 하네스 고칠 거리마다`(같은 뜻은 고칠 스킬과 문제가 같은 것), `이슈로 올린 하네스 고칠 거리와 같은 뜻의 항목은 지운다`, `감수할 것마다 감수한 것 절에 항목을 더한다`, `감수한 것 절의 항목은 다시 나오지 않은 tasks를 세지 않고 지우지 않는다`가 더해진다. 파일 양식이 세 절(`## 소스 문제`, `## 하네스 고칠 거리`, `## 감수한 것`)과 절마다의 항목 꼴로 바뀌고, 문서 지도에 더할 행이 task 머리의 결정의 행으로 바뀐다. 가리킴 `낱말의 "양식을 읽는 법"대로 옮긴다`는 본문에 다섯 번 그대로 남는다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] `RunRulesTest`에 `test_first_proposal_uses_threshold`(처음 안의 두 글과 고칠 안의 두 줄)와 `test_backlog_three_sections`("BACKLOG를 고친다"의 네 글, 세 절 머리, 새 문서 지도 행)가 더해진다 (`tests/test_skill_rules.py`)

**통과 조건**
- 완료 조건 3이 참이다.
  - 확인: 완료 조건 3의 확인을 모두 돌린다
- 모든 테스트가 통과하고, 고친 run 글이 빠지면 그 테스트가 실패한다.
  - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
  - 확인: 새 사본(`mktemp -d`로 만든 폴더에 작업 트리의 `plugins`와 `tests`를 `cp -R`로 복사한 것)마다, run 본문의 `plate 자체의 하네스 고칠 거리는 문턱을 넘은 것만 이슈로 올릴 것에, 넘지 않은 것은 BACKLOG로 미룰 것에 둔다`를 빈 글로 바꾸고 돌리면 `FAIL: test_first_proposal_uses_threshold (test_skill_rules.RunRulesTest`가 나온다. `감수할 것마다 감수한 것 절에 항목을 더한다`를 빈 글로 바꾸고 돌리면 `FAIL: test_backlog_three_sections (test_skill_rules.RunRulesTest`가 나온다. 두 글은 사본에 저마다 한 번 있다
