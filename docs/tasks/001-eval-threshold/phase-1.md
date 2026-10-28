# Phase 1: run의 처음 안과 BACKLOG가 문턱과 처리를 따른다

**목표**: run 본문의 tasks 끝(보고, 고칠 안, 처음 안, BACKLOG를 고친다)과 BACKLOG 양식이 task 머리의 결정대로 바뀌고 그 글을 지키는 테스트가 더해진다.

**테스트 먼저**: 아니오 — 동작을 바꾸는 것은 스킬 본문(`.md`)이고, 테스트는 그 글을 지킨다

**읽을 것**
- `plugins/plate/skills/run/SKILL.md` (낱말의 `docs/BACKLOG.md`와 "하네스 고칠 거리", "보고하고 묻는다", "BACKLOG를 고친다", "고침 task를 더한다"의 범위 밖 줄)
- `tests/test_skill_rules.py` (`RunRulesTest`, 특히 `test_template_reading_rule_in_one_place`가 세는 가리킴 다섯)
- `docs/ADR.md`의 ADR-020
- `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/TOOLS.md`, `docs/BACKLOG.md`, `docs/cleanup/2026-10-28.md` (맥락 문서)

**TODO**
- [x] 낱말의 `docs/BACKLOG.md` 정의가 `미룬 소스 문제와 하네스 고칠 거리, 감수한 것을 tasks를 넘어 모으는 문서`를 담게 바뀌고, "하네스 고칠 거리" 낱말에 eval이 적는 처리와 문턱이 더해진다 (`plugins/plate/skills/run/SKILL.md`)
- [x] "보고하고 묻는다"의 4번에 `나눠 번호, 글, 처리와, plate 자체의 것은 문턱을 넘었는지`가 들고, 6번 고칠 안에 `- 감수할 것: 처리가 감수인 하네스 고칠 거리의 번호`가 더해지고, BACKLOG로 미룰 것 줄이 `- BACKLOG로 미룰 것: 소스 문제의 번호와, 문턱을 넘지 않은 plate 자체의 하네스 고칠 거리의 번호`로 바뀐다 (`plugins/plate/skills/run/SKILL.md`)
- [x] 처음 안 문단이 task 머리의 결정 "run의 처음 안"대로 바뀌어 `plate 자체의 하네스 고칠 거리는 문턱을 넘은 것만 이슈로 올릴 것에, 넘지 않은 것은 BACKLOG로 미룰 것에 둔다`와 `처리가 감수인 하네스 고칠 거리는 갈래와 상관없이 감수할 것에 둔다`가 들고, 옛 글 `plate 자체의 하네스 고칠 거리는 모두 이슈로 올릴 것에 두고`가 지워진다 (`plugins/plate/skills/run/SKILL.md`)
- [x] 고칠 곳을 말할 때의 줄에 `이슈로 올릴 것에서 뺀 하네스 고칠 거리는 BACKLOG로 미룰 것으로 옮긴다`가 더해지고, 아무것도 고치지 않겠다는 답의 줄이 `소스 문제와 plate 자체의 하네스 고칠 거리를 모두 BACKLOG로 미룰 것에 둔 안`으로 바뀌어 옛 글 `소스 문제를 모두 BACKLOG로 미룰 것에 둔 안`이 지워진다 (`plugins/plate/skills/run/SKILL.md`)
- [x] "BACKLOG를 고친다"에 `미룰 하네스 고칠 거리마다`(같은 뜻은 고칠 스킬과 문제가 같은 것), `이슈로 올린 하네스 고칠 거리와 같은 뜻의 항목은 지운다`, `감수할 것마다 감수한 것 절에 항목을 더한다`, `감수한 것 절의 항목은 다시 나오지 않은 tasks를 세지 않고 지우지 않는다`가 더해진다. 파일 양식이 세 절(`## 소스 문제`, `## 하네스 고칠 거리`, `## 감수한 것`)과 절마다의 항목 꼴로 바뀌고, 문서 지도에 더할 행이 task 머리의 결정의 행으로 바뀐다. 가리킴 `낱말의 "양식을 읽는 법"대로 옮긴다`는 본문에 다섯 번 그대로 남는다 (`plugins/plate/skills/run/SKILL.md`)
- [x] `RunRulesTest`에 `test_first_proposal_uses_threshold`(처음 안의 두 글과 고칠 안의 두 줄)와 `test_backlog_three_sections`("BACKLOG를 고친다"의 네 글, 세 절 머리, 새 문서 지도 행)가 더해진다 (`tests/test_skill_rules.py`)

**통과 조건**
- 완료 조건 3이 참이다.
  - 확인: 완료 조건 3의 확인을 모두 돌린다
- 모든 테스트가 통과하고, 고친 run 글이 빠지면 그 테스트가 실패한다.
  - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
  - 확인: 새 사본(`mktemp -d`로 만든 폴더에 작업 트리의 `plugins`와 `tests`를 `cp -R`로 복사한 것)마다, run 본문의 `plate 자체의 하네스 고칠 거리는 문턱을 넘은 것만 이슈로 올릴 것에, 넘지 않은 것은 BACKLOG로 미룰 것에 둔다`를 빈 글로 바꾸고 돌리면 `FAIL: test_first_proposal_uses_threshold (test_skill_rules.RunRulesTest`가 나온다. `감수할 것마다 감수한 것 절에 항목을 더한다`를 빈 글로 바꾸고 돌리면 `FAIL: test_backlog_three_sections (test_skill_rules.RunRulesTest`가 나온다. 두 글은 사본에 저마다 한 번 있다

## 한 일
- 낱말의 `docs/BACKLOG.md` 정의와 "하네스 고칠 거리" 낱말: BACKLOG 정의를 `미룬 소스 문제와 하네스 고칠 거리, 감수한 것을 tasks를 넘어 모으는 문서`로 바꾸고, 하네스 고칠 거리 낱말에 eval이 적는 처리(세 가지)와 까닭, plate 자체의 것의 문턱(넘음, 넘지 않음), 이슈 제목과 본문이 있는 고칠 거리를 더했다 (`plugins/plate/skills/run/SKILL.md`)
- "보고하고 묻는다"의 4번과 6번: 4번을 `나눠 번호, 글, 처리와, plate 자체의 것은 문턱을 넘었는지`로, BACKLOG로 미룰 것 줄을 새 글로 바꾸고 `- 감수할 것: 처리가 감수인 하네스 고칠 거리의 번호`를 더했다 (`plugins/plate/skills/run/SKILL.md`)
- 처음 안 문단: task 머리의 결정대로 고쳐 옛 글을 지우고 두 새 글을 넣었다. 소스 문제는 BACKLOG로 미룰 것에 두지 않는다는 문장을 남겼다(옛 "BACKLOG로 미룰 것은 없다"의 소스 문제 몫) (`plugins/plate/skills/run/SKILL.md`)
- 고칠 곳을 말할 때와 아무것도 고치지 않겠다는 답: `이슈로 올릴 것에서 뺀 하네스 고칠 거리는 BACKLOG로 미룰 것으로 옮긴다`를 더하고, 아무것도 고치지 않는 답의 안을 `소스 문제와 plate 자체의 하네스 고칠 거리를 모두 BACKLOG로 미룰 것에 둔 안`으로 바꾸고, 감수할 것은 그대로 둔다는 문장을 더했다 (`plugins/plate/skills/run/SKILL.md`)
- "BACKLOG를 고친다": 같은 뜻의 정의를 절마다로 나누고(하네스 고칠 거리와 감수한 것은 고칠 스킬과 문제가 같은 것), 절 머리가 없는 옛 파일을 세 절로 옮기는 줄, `미룰 하네스 고칠 거리마다`, `이슈로 올린 하네스 고칠 거리와 같은 뜻의 항목은 지운다`, `감수할 것마다 감수한 것 절에 항목을 더한다`, `감수한 것 절의 항목은 다시 나오지 않은 tasks를 세지 않고 지우지 않는다`를 더했다. 양식을 세 절과 절마다의 항목 꼴로, 문서 지도 행을 새 행으로 바꾸고, 문서 지도의 행이 새 행과 다르면 바꾼다는 줄을 더했다. 가리킴 `낱말의 "양식을 읽는 법"대로 옮긴다`는 다섯 번 그대로다 (`plugins/plate/skills/run/SKILL.md`)
- `RunRulesTest`에 `test_first_proposal_uses_threshold`와 `test_backlog_three_sections`를 더했다 (`tests/test_skill_rules.py`)

## 확인 결과
- 완료 조건 3이 참이다.
  - `grep -cF -e '<글>' plugins/plate/skills/run/SKILL.md`를 새 글 열셋(고칠 안의 두 줄, 처음 안의 두 글, 고칠 곳의 두 글, 보고의 글, "BACKLOG를 고친다"의 네 글, 낱말의 글, 문서 지도 행)마다 → 모두 `1`. 통과
  - `grep -cxF -e '## 소스 문제'`, `'## 하네스 고칠 거리'`, `'## 감수한 것'` → 저마다 `1`. 통과
  - 옛 글 셋 `grep -cF -e` → 모두 `0`, `grep -cE '^   - BACKLOG로 미룰 것: 소스 문제의 번호$'` → `0`. 통과
- 모든 테스트가 통과하고, 고친 run 글이 빠지면 그 테스트가 실패한다.
  - `python3 -m unittest discover -s tests` → `Ran 200 tests in 17.145s` / `OK`. 통과
  - 새 사본(`mktemp -d`에 `plugins`, `tests`를 `cp -R`)에서 `plate 자체의 하네스 고칠 거리는 문턱을 넘은 것만 이슈로 올릴 것에, 넘지 않은 것은 BACKLOG로 미룰 것에 둔다`(사본에 `1`번)를 빈 글로 바꾸고 돌림 → `FAIL: test_first_proposal_uses_threshold (test_skill_rules.RunRulesTest)`, `FAILED (failures=1)`. 통과
  - 다른 새 사본에서 `감수할 것마다 감수한 것 절에 항목을 더한다`(사본에 `1`번)를 빈 글로 바꾸고 돌림 → `FAIL: test_backlog_three_sections (test_skill_rules.RunRulesTest) (text='감수할 것마다 감수한 것 절에 항목을 더한다')`, `FAILED (failures=1)`. 통과

## 계획과 달라진 점
- TODO에 적히지 않은 run 본문 두 줄을 결정에 맞췄다: 고침 task의 꼴의 "고칠 것은 … 이 프로젝트만의 하네스 고칠 거리다"에 `처리가 감수가 아닌`을 더하고, 고침 task 머리 양식의 범위 밖 줄 "이슈로 올리고 plate 저장소에서 고친다"를 "이슈로 올리거나 BACKLOG로 미루고 plate 저장소에서 고친다"로 바꿨다. 읽을 것이 "고침 task를 더한다"의 범위 밖 줄을 가리켰고, 그대로 두면 문턱을 넘지 않아 BACKLOG로 가는 plate 자체의 것과 어긋난다
- "BACKLOG를 고친다"에 TODO에 없는 운영 줄 셋을 더했다: 절 머리가 없는 옛 파일의 항목을 `## 소스 문제` 절로 옮긴다, 감수할 것과 같은 뜻의 하네스 고칠 거리 절 항목은 지운다, 파일이 이미 있어도 문서 지도의 행이 새 행과 다르면 바꾼다. 이 저장소의 `docs/BACKLOG.md`와 `AGENTS.md`가 옛 꼴이라 새 규칙만으로는 옮길 길이 없다

## 남은 것
- `tests/test_skill_rules.py` 머리 docstring의 이슈 목록은 고치지 않았다. 완료 조건 4의 `#74` 목록 확인은 eval을 고치는 phase의 몫으로 봤다
- `docs/BACKLOG.md`, `AGENTS.md`의 문서 지도 행, 맥락 문서(ADR, PRD, ARCHITECTURE)는 이 phase의 TODO가 아니라 고치지 않았다
- 이슈를 올리지 못한(`gh` 실패) 하네스 고칠 거리가 BACKLOG에서 어떻게 되는지는 본문이 정하지 않는다. "이슈로 올린 … 항목은 지운다"만 있어, 올리지 못한 것은 BACKLOG에도 이슈에도 남지 않고 10번의 보고에만 남는다
- 고친 run 본문의 동작은 헤드리스로 돌려 보지 않았다(완료 조건 3의 `돌리지 않음`)

## 하네스에서 걸린 것
- 없음

## 확인 1

**통과 조건**
- 완료 조건 3이 참이다.
  - `grep -cF -e '<글>' plugins/plate/skills/run/SKILL.md`를 완료 조건 3의 새 글 열셋(고칠 안의 두 줄, 처음 안의 두 글, 고칠 곳의 두 글, 보고의 글, "BACKLOG를 고친다"의 네 글, 낱말의 글, 문서 지도 행)마다 → 모두 `1`. 통과
  - `grep -cxF -e '## 소스 문제'`, `-e '## 하네스 고칠 거리'`, `-e '## 감수한 것'` (`plugins/plate/skills/run/SKILL.md`) → 저마다 `1`. 통과
  - 옛 글 셋 `grep -cF -e` → 모두 `0`, `grep -cE '^   - BACKLOG로 미룰 것: 소스 문제의 번호$' plugins/plate/skills/run/SKILL.md` → `0`. 통과
- 모든 테스트가 통과하고, 고친 run 글이 빠지면 그 테스트가 실패한다.
  - `python3 -m unittest discover -s tests` → `Ran 200 tests` / `OK`. 통과
  - 새 사본(`mktemp -d`에 `plugins`, `tests`를 `cp -R`)에서 `plate 자체의 하네스 고칠 거리는 문턱을 넘은 것만 이슈로 올릴 것에, 넘지 않은 것은 BACKLOG로 미룰 것에 둔다`(사본에 `1`번)를 빈 글로 바꾸고 `python3 -m unittest discover -s tests` → `FAIL: test_first_proposal_uses_threshold (test_skill_rules.RunRulesTest)`, `FAILED (failures=1)`. 통과
  - 다른 새 사본에서 `감수할 것마다 감수한 것 절에 항목을 더한다`(사본에 `1`번)를 빈 글로 바꾸고 `python3 -m unittest discover -s tests` → `FAIL: test_backlog_three_sections (test_skill_rules.RunRulesTest) (text='감수할 것마다 감수한 것 절에 항목을 더한다')`, `FAILED (failures=1)`. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 200 tests` / `OK`. 통과

**남은 것**
- 이슈를 올리지 못한(`gh` 실패) 하네스 고칠 거리가 BACKLOG에서 어떻게 되는지 본문이 정하지 않는다 → 통과 조건(완료 조건 3의 글 확인과 테스트)은 `gh` 실패 때의 동작을 보지 않는다. 하네스에서 걸린 것
- 고친 run 본문의 동작은 헤드리스로 돌려 보지 않았다 → 완료 조건 3의 `- 돌리지 않음: run의 tasks 끝은 사용자의 답과 `gh`가 있어야 돌고 여러 턴을 이어야 닿는다. 사용자가 eval만 돌리기로 정했다`가 돌리지 않기로 정한 동작이다. 하네스에서 걸린 것

**실패**
- 없음

**하네스에서 걸린 것**
- 남은 것: 이슈를 올리지 못한(`gh` 실패) 하네스 고칠 거리가 BACKLOG에서 어떻게 되는지 run 본문이 정하지 않는다. "이슈로 올린 … 항목은 지운다"만 있어 올리지 못한 것은 10번의 보고에만 남는다 (`plugins/plate/skills/run/SKILL.md`)
- 남은 것: 고친 run 본문의 동작은 헤드리스로 돌려 보지 않았다(완료 조건 3의 `돌리지 않음`)

**판정**: 통과
