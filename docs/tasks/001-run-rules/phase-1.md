# Phase 1: run 본문과 테스트와 문서를 고친다

**목표**: run 본문의 네 이슈가 고쳐지고, 그 규칙 글의 테스트가 더해지고, run 줄의 맥락 문서와 README가 맞춰진다.

**테스트 먼저**: 아니오 — 고치는 것은 스킬 본문(`.md`)이고, 더하는 테스트는 그 글이 있는지를 볼 뿐 코드의 동작을 바꾸지 않는다

**읽을 것**
- `plugins/plate/skills/run/SKILL.md`의 낱말 "작업 트리의 스킬 줄", "4. 수행을 맡긴다", "5. 확인을 맡긴다", "7. task 회고를 맡긴다", "8. 고칠 phase를 더한다", "멈춘다", "tasks 끝"의 "코드 평가를 맡긴다"와 "하네스 eval을 맡긴다" (고칠 자리)
- `gh issue view 46`, `gh issue view 47`, `gh issue view 48`, `gh issue view 51` (이슈마다의 원인과 해결책. #46은 run 8번 쪽만, #51은 run이 맡기는 글 쪽만 이 task의 일이다)
- `tests/test_skill_rules.py` (`section`, `subsection` 도우미와 이슈마다의 테스트 꼴)
- `docs/TOOLS.md`의 "실행 스킬의 판정에서 본 것"(명령 치환이 승인을 요구한다)과 "세션 도중의 스킬 본문 고침"(작업 트리의 스킬 줄의 까닭)
- `docs/PRD.md`의 7, `docs/ARCHITECTURE.md`의 "패턴과 규칙"과 디렉터리 구조, `README.md`의 스킬 표 (맞출 줄)

**TODO**
- [ ] 8번 첫머리의 판정에, 고칠 파일이 task 머리나 tasks 머리의 완료 조건이 돌린 시각이나 본문 해시로 보는 파일이고 고친 뒤 그 확인을 다시 참으로 둘 길이 계획에 없으면 고칠 phase를 더하지 않고 "멈춘다"로 간다는 글이 더해진다. "멈춘다"의 자리 목록의 회고 항목도 이 경우를 담게 바뀐다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] 8번의 계획 커밋 찾기 명령과 낱말 "작업 트리의 스킬 줄"의 갈라진 곳 명령이, 명령 치환 없이 해시를 먼저 얻고 그 해시를 넣어 부르는 두 단계로 바뀐다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] "멈춘다" 4의 계획을 바꾸는 갈래에, 커밋 전에 이번 수정의 결정 줄이 task 머리(tasks 머리를 고쳤으면 tasks 머리에도)에 있는지 보고, 계획 수정마다 결정 줄 하나라는 글이 더해진다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] 맡기는 글 다섯(4번, 5번, 7번, "코드 평가를 맡긴다", "하네스 eval을 맡긴다"의 코드 블록)마다 마지막 줄로 `부른 쪽: plate:run`이 더해지고, 4번의 조건부 줄을 가리키는 글이 그 줄을 계속 가리키게 바뀐다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] 위 넷의 규칙 글이 제 절에 있는지 보는 테스트가 이슈마다 더해진다. run 본문의 git 명령에 `$(`가 없는지 보는 테스트와, 다섯 코드 블록마다 표지 줄이 있는지 보는 테스트가 든다. 모듈 docstring의 이슈 목록에 #46, #47, #48, #51이 더해진다 (`tests/test_skill_rules.py`)
- [ ] `docs/PRD.md` 7과 `docs/ARCHITECTURE.md` "패턴과 규칙"의 run 문단에 해시·시각으로 보는 파일을 고칠 때의 멈춤과 계획 수정마다의 결정 줄이 더해진다. 같은 절의 맡기는 글 문단에 표지 줄 `부른 쪽: plate:run`이 더해진다. `README.md` `run` 행의 멈춤 괄호에 해시·시각으로 보는 파일의 멈춤이 더해진다. 디렉터리 구조의 `test_skill_rules.py` 줄에 이번 run 규칙이 더해진다 (`docs/PRD.md`, `docs/ARCHITECTURE.md`, `README.md`)

**통과 조건**
- 완료 조건 1이 참이다
  - 확인: `plugins/plate/skills/run/SKILL.md`의 "8. 고칠 phase를 더한다", "멈춘다", 낱말의 "작업 트리의 스킬 줄", 맡기는 글 다섯의 코드 블록을 읽어 #46, #47, #48, #51의 해결이 task 머리 완료 조건 1의 글대로 저마다 적혀 있다. 하나라도 없으면 실패
  - 확인: `grep -n 'git[^`]*\$(' plugins/plate/skills/run/SKILL.md`가 아무것도 내지 않는다
- 완료 조건 2가 참이다
  - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
  - 확인: `mktemp -d`에 `git archive HEAD`를 풀어 run 본문 "하네스 eval을 맡긴다"의 코드 블록에서 `부른 쪽: plate:run` 줄을 지우고 돌리면 실패한다. 다시 풀어 8번의 계획 커밋 찾기를 `$(git log -1 --format=%h -- docs/tasks/NNN-slug/retro.md)`를 넣은 한 줄로 되돌리고 돌리면 실패한다
- 완료 조건 3이 참이다
  - 확인: `docs/PRD.md`의 7, `docs/ARCHITECTURE.md` "패턴과 규칙"의 맡기는 글 문단과 run 문단, 디렉터리 구조의 `test_skill_rules.py` 줄, `README.md`의 `run` 행을 문서마다 따로 읽어, task 머리 완료 조건 3의 견줄 것을 저마다 담는다. 하나라도 어긋나면 실패
- 모든 스킬의 description이 1024자 이하다
  - 확인: `python3 -m unittest discover -s tests`의 `test_description_at_most_1024_chars`가 통과한다(위 `OK`에 든다)
