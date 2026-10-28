# Phase 4: 맡기는 글과 고칠 꼴을 바로 넘기게 한다

**목표**: 작업 트리의 스킬 줄이 marketplace 매니페스트가 가리키는 한 곳만 고르고 옛 본문을 부르지 않게 하고, 고칠 phase와 고침 task가 걸리는 테스트와 조건 글을 넘기고, 양식을 읽는 법이 낱말에 한 번 있게 한다.

**테스트 먼저**: 아니오 — 스킬 본문(`.md`)과 그 글을 지키는 테스트, 맥락 문서만 바꾼다

**읽을 것**
- `plugins/plate/skills/run/SKILL.md` (`## 낱말`의 작업 트리의 스킬 줄과 표지 줄, 맡기는 글 다섯 자리: `## 4. 수행을 맡긴다`, `## 5. 확인을 맡긴다`, `## 7. task 회고를 맡긴다`, `### 코드 평가를 맡긴다`, `### 하네스 eval을 맡긴다`. 그리고 `## 8. 고칠 phase를 더한다`의 TODO·읽을 것 규칙과 꼴, `### 고침 task를 더한다`의 **고침 task의 꼴**과 두 파일의 꼴. 양식을 읽는 법 세 문장이 있는 다섯 자리: 8번, `### BACKLOG를 고친다`, `### 고침 task를 더한다`, `## PR을 연다`의 **PR 본문의 꼴**, `## `RUNLOG.md``)
- `.claude-plugin/marketplace.json` (이름 `plate`, `source` `./plugins/plate`)
- `docs/cleanup/2026-10-28.md` (보안-3, 성능-4, 기존 작업 정합성-3, 기존 작업 정합성-5, 유지보수성-12와 그 2라운드)
- `tests/test_skill_rules.py` (`RunRulesTest.test_51_marker_line_ends_every_hand_off_block`, `test_47_no_command_substitution_in_git_commands`, `CallerMarkerTest`)
- `plugins/plate/skills/phase/SKILL.md` (`## 6. 다섯 줄을 돌려준다`: 작업 트리의 스킬 줄로 run이 띄운 호출을 가르는 글)
- `docs/ARCHITECTURE.md` (`## 패턴과 규칙`의 스킬이 다른 스킬을 이름으로 부른다는 줄과 작업 트리의 스킬 줄 예외)

**TODO**
- [ ] 낱말의 작업 트리의 스킬 줄이 바뀐다. `.claude-plugin/marketplace.json`이 있고 이름이 `plate`인 플러그인의 `source`가 있으면 그 `source` 아래의 `skills/{스킬 이름}/SKILL.md`만 `{경로}`로 고르고, 없으면 지금 규칙대로 고른다. 명령 치환 없이 읽는 법이 함께 적힌다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] 작업 트리의 스킬 줄을 붙일 때 맡기는 글이 이름으로 옛 본문을 불러 싣게 하지 않게 바뀐다. 표지 줄은 블록 끝에 그대로 남고, 작업 트리의 스킬 줄은 `작업 트리의 {경로}를 읽어 그 절차를 따른다.`로 시작하며, git diff는 맡길 때마다 다시 낸다. 맡기는 글 다섯 자리의 붙이는 규칙 글도 이에 맞는다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] 8번에, 문제의 글(또는 고칠 줄의 핵심 낱말)을 테스트 폴더에서 찾아 걸리는 테스트를 읽을 것과 그 TODO의 파일 목록에 넣는다는 규칙이 더해지고, 고칠 phase의 꼴에 그 자리가 보인다. **고침 task의 꼴**의 "8번과 같은 규칙" 줄이 이 규칙도 덮는다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] **고침 task의 꼴**의 마지막 완료 조건 규칙과 task 머리의 꼴이, 가리킨 tasks 완료 조건마다 그 조건의 글과 확인을 함께 옮기게 바뀐다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] 양식을 읽는 법 세 문장("아래 코드 블록 안쪽이 …의 꼴이다. 블록을 여닫는 줄은 옮기지 않는다. `{…}`는 …")이 낱말에 한 낱말로 한 번 적힌다. 다섯 자리는 그 낱말을 가리키는 짧은 줄로 바뀐다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] `RunRulesTest`에 완료 조건 4의 단언(작업 트리의 스킬 줄의 두 갈래, 8번의 테스트 폴더 찾기, 고침 task의 조건 글 옮기기, 양식 읽는 법이 한 번이고 다섯 자리가 가리킴)이 더해진다. 바뀐 글에 걸리는 기존 테스트는 바뀐 뒤의 글로 고친다 (`tests/test_skill_rules.py`)
- [ ] ARCHITECTURE `## 패턴과 규칙`의 작업 트리의 스킬 줄 문장에, marketplace 매니페스트의 `source`로 좁힌다는 것과 그 줄을 붙이면 이름으로 옛 본문을 부르지 않는다는 것이 더해진다. `## 디렉터리 구조`의 `test_skill_rules.py` 줄에 새 테스트가 다루는 규칙이 더해진다 (`docs/ARCHITECTURE.md`)

**통과 조건**
- 맡기는 글과 고칠 꼴이 완료 조건 4대로다. (완료 조건 4)
  - 확인: `python3 -m unittest discover -s tests`가 `OK`로 끝난다. 완료 조건 4의 단언을 하는 테스트와 `test_51_marker_line_ends_every_hand_off_block`, `CallerMarkerTest`가 그 안에 있다
  - 확인: `mktemp -d`로 만든 `<임시>/m`에 `git init`을 하고 첫 커밋을 넣는다. `.claude-plugin/marketplace.json`(이름 `plate`, `source` `./plugins/plate`)을 두고, 두 사본을 만든다: `plugins/plate/.claude-plugin/plugin.json`(이름 `plate`)과 `plugins/plate/skills/phase/SKILL.md`, 그리고 `vendor/copy/.claude-plugin/plugin.json`(이름 `plate`)과 `vendor/copy/skills/phase/SKILL.md`. 이 둘을 둘째 커밋에 넣는다. 낱말에 적은 고르는 법대로 첫 커밋과 HEAD 사이에서 `phase`의 경로를 고른다. `plugins/plate/skills/phase/SKILL.md` 하나만 나온다. `marketplace.json`과 `vendor/copy`를 지운 커밋을 넣고 첫 커밋과 그 HEAD 사이에서 다시 고르면 `plugins/plate/skills/phase/SKILL.md`가 나온다
  - 확인: ARCHITECTURE `## 패턴과 규칙`의 작업 트리의 스킬 줄 문장을 읽는다. marketplace 매니페스트의 `source`로 좁힌다는 것과 이름으로 옛 본문을 부르지 않는다는 것이 둘 다 있다
- 앞 phase가 이룬 규칙이 그대로다. 이 phase가 "PR을 연다"의 꼴과 `RUNLOG.md` 절을 고치기 때문이다. (완료 조건 1, 2, 3)
  - 확인: `python3 -m unittest discover -s tests`가 `OK`로 끝난다. 완료 조건 1·2·3의 테스트가 그 안에 있다
- 앞 task가 이룬 tasks 완료 조건 1과 3이 그대로다. (완료 조건 5)
  - 확인: `git grep -n 'TOOLS.md' -- plugins/`가 아무것도 내지 않는다
  - 확인: `git grep -nE '사용량.*TOOLS\.md|TOOLS\.md.*사용량' -- docs/PRD.md docs/ARCHITECTURE.md docs/ADR.md README.md AGENTS.md`가 아무것도 내지 않는다
