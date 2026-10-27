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
- [x] 8번 첫머리의 판정에, 고칠 파일이 task 머리나 tasks 머리의 완료 조건이 돌린 시각이나 본문 해시로 보는 파일이고 고친 뒤 그 확인을 다시 참으로 둘 길이 계획에 없으면 고칠 phase를 더하지 않고 "멈춘다"로 간다는 글이 더해진다. "멈춘다"의 자리 목록의 회고 항목도 이 경우를 담게 바뀐다 (`plugins/plate/skills/run/SKILL.md`)
- [x] 8번의 계획 커밋 찾기 명령과 낱말 "작업 트리의 스킬 줄"의 갈라진 곳 명령이, 명령 치환 없이 해시를 먼저 얻고 그 해시를 넣어 부르는 두 단계로 바뀐다 (`plugins/plate/skills/run/SKILL.md`)
- [x] "멈춘다" 4의 계획을 바꾸는 갈래에, 커밋 전에 이번 수정의 결정 줄이 task 머리(tasks 머리를 고쳤으면 tasks 머리에도)에 있는지 보고, 계획 수정마다 결정 줄 하나라는 글이 더해진다 (`plugins/plate/skills/run/SKILL.md`)
- [x] 맡기는 글 다섯(4번, 5번, 7번, "코드 평가를 맡긴다", "하네스 eval을 맡긴다"의 코드 블록)마다 마지막 줄로 `부른 쪽: plate:run`이 더해지고, 4번의 조건부 줄을 가리키는 글이 그 줄을 계속 가리키게 바뀐다 (`plugins/plate/skills/run/SKILL.md`)
- [x] 위 넷의 규칙 글이 제 절에 있는지 보는 테스트가 이슈마다 더해진다. run 본문의 git 명령에 `$(`가 없는지 보는 테스트와, 다섯 코드 블록마다 표지 줄이 있는지 보는 테스트가 든다. 모듈 docstring의 이슈 목록에 #46, #47, #48, #51이 더해진다 (`tests/test_skill_rules.py`)
- [x] `docs/PRD.md` 7과 `docs/ARCHITECTURE.md` "패턴과 규칙"의 run 문단에 해시·시각으로 보는 파일을 고칠 때의 멈춤과 계획 수정마다의 결정 줄이 더해진다. 같은 절의 맡기는 글 문단에 표지 줄 `부른 쪽: plate:run`이 더해진다. `README.md` `run` 행의 멈춤 괄호에 해시·시각으로 보는 파일의 멈춤이 더해진다. 디렉터리 구조의 `test_skill_rules.py` 줄에 이번 run 규칙이 더해진다 (`docs/PRD.md`, `docs/ARCHITECTURE.md`, `README.md`)

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

## 한 일
- 8번 첫머리의 판정에 시각·해시로 보는 파일을 고칠 때의 멈춤: 8번 첫 문단에 "고칠 파일이 task 머리나 tasks 머리의 완료 조건이 돌린 시각이나 본문 해시로 보는 파일이면, 고친 뒤 그 확인을 다시 참으로 둘 길(고친 본문으로 다시 돌리는 TODO나 phase)이 계획에 있는지도 본다"와 그 까닭, "이 경우도 계획을 바꾸게 하는 문제다"를 더해 "멈춘다"로 가게 했다. "멈춘다"의 자리 목록의 회고 항목에 "고칠 파일이 완료 조건이 돌린 시각이나 본문 해시로 보는 파일인데 고친 뒤 그 확인을 다시 참으로 둘 길이 계획에 없을 때도 든다(8번)"를 더했다 (`plugins/plate/skills/run/SKILL.md`)
- 두 단계 명령: 8번의 계획 커밋 찾기를 "먼저 `git log -1 --format=%h -- docs/tasks/NNN-slug/retro.md`로 해시를 얻고, 그 해시를 넣어 `git log --format='%h %s' {해시}..HEAD -- docs/tasks/`를 따로 불러 찾는다"로, 낱말 "작업 트리의 스킬 줄"의 갈라진 곳을 "먼저 `git merge-base {기본 브랜치} HEAD`로 해시를 얻고, 그 해시를 넣어 `git diff --name-only {해시} HEAD`를 따로 부른다"로 바꾸고, 둘 다 명령 치환을 쓰지 않는 까닭(헤드리스의 권한 검사)을 적었다 (`plugins/plate/skills/run/SKILL.md`)
- "멈춘다" 4의 결정 줄 점검: "계획 수정마다 결정 줄 하나다: 같은 멈춤 안에서 계획을 두 번 고치면 결정 줄도 두 번 더한다"와 커밋 앞의 "커밋하기 전에 이번 수정의 결정 줄이 task 머리(tasks 머리를 고쳤으면 tasks 머리에도)에 있는지 보고, 없으면 더한 뒤에 커밋한다"를 더하고, "tasks 머리의 결정에"를 "tasks 머리의 결정에도"로 바꿨다 (`plugins/plate/skills/run/SKILL.md`)
- 표지 줄: 맡기는 글 다섯의 코드 블록 끝에 `부른 쪽: plate:run`을 더하고, 4번의 "넷째 줄은 …"을 "`고칠 문제:` 줄은 … 때만 붙이고, 붙이지 않으면 그 줄만 빼고 표지 줄은 남긴다"로 바꿨다. 낱말에 "표지 줄"을 더해 작업 트리의 스킬 줄이 표지 줄 뒤에 붙는다고 적었다 (`plugins/plate/skills/run/SKILL.md`)
- 테스트: `RunRulesTest`에 `test_46_fix_file_checked_by_time_or_hash_stops`, `test_47_no_command_substitution_in_git_commands`(본문 전체에 `git[^`\n]*\$\(`가 없음과 두 자리의 두 단계 글), `test_48_one_decision_line_per_plan_fix`(결정 줄 점검이 커밋 글보다 앞), `test_51_marker_line_ends_every_hand_off_block`(다섯 절마다 코드 블록 하나의 마지막 줄이 표지 줄)을 더하고 docstring 이슈 목록에 #46·#47·#48·#51을 더했다 (`tests/test_skill_rules.py`)
- 문서: PRD 7에 시각·해시로 보는 파일의 멈춤과 계획 수정마다의 결정 줄, ARCHITECTURE "패턴과 규칙"의 맡기는 글 문단에 두 단계 명령과 표지 줄 `부른 쪽: plate:run`, run 문단에 시각·해시 멈춤, 결정 줄 점검, 계획 커밋 찾기의 두 단계와 이유(#46, #47, #48), 디렉터리 구조의 `test_skill_rules.py` 줄에 네 규칙, README `run` 행의 멈춤 괄호에 시각·해시로 보는 파일의 멈춤을 더했다 (`docs/PRD.md`, `docs/ARCHITECTURE.md`, `README.md`)

## 확인 결과
- 완료 조건 1이 참이다
  - run 본문의 "8. 고칠 phase를 더한다", "멈춘다", 낱말 "작업 트리의 스킬 줄"과 "표지 줄", 맡기는 글 다섯의 코드 블록을 다시 읽음 → #46: 8번 첫 문단이 고칠 파일과 완료 조건의 시각·해시 확인의 관계를 보고 다시 참으로 둘 길이 없으면 "멈춘다"로 간다, "멈춘다" 목록에도 있다. #47: 두 명령 모두 해시를 먼저 얻고 넣어 부르는 두 단계다. #48: "멈춘다" 4가 커밋 전에 결정 줄을 보고 "계획 수정마다 결정 줄 하나다"가 있다. #51: 다섯 코드 블록의 마지막 줄이 `부른 쪽: plate:run`이다(`grep -c '부른 쪽: plate:run'` → 6, 블록 다섯과 낱말 하나). 통과
  - `grep -n 'git[^`]*\$(' plugins/plate/skills/run/SKILL.md` → 출력 없음. 통과
- 완료 조건 2가 참이다
  - `python3 -m unittest discover -s tests` → `Ran 153 tests in 16.077s` / `OK`. 통과
  - `mktemp -d`에 `git archive $(git write-tree)`(이 phase의 바뀐 것을 스테이지한 트리)를 풀어 "하네스 eval을 맡긴다"의 `부른 쪽: plate:run` 줄을 지우고 돌림 → `FAILED (failures=1)`, `FAIL: test_51_marker_line_ends_every_hand_off_block (test_skill_rules.RunRulesTest) (heading='하네스 eval을 맡긴다')`. 다시 풀어 8번의 계획 커밋 찾기를 `$(git log -1 --format=%h -- docs/tasks/NNN-slug/retro.md)`를 넣은 한 줄로 되돌리고 돌림 → `FAILED (failures=1)`, `FAIL: test_47_no_command_substitution_in_git_commands (test_skill_rules.RunRulesTest)`. 통과
- 완료 조건 3이 참이다
  - `docs/PRD.md` 7 → 시각·해시로 보는 파일을 고칠 때의 멈춤과 "고칠 때마다 결정에 줄 하나를 더하고, 커밋 전에 그 줄이 있는지 본다"가 있다. `docs/ARCHITECTURE.md` 맡기는 글 문단 → 표지 줄 `부른 쪽: plate:run`이 있다. run 문단 → 시각·해시 멈춤과 수정마다의 결정 줄이 있다. 디렉터리 구조의 `test_skill_rules.py` 줄 → 네 규칙이 있다. `README.md` `run` 행의 멈춤 괄호 → 시각·해시로 보는 파일의 멈춤이 있다. 통과
- 모든 스킬의 description이 1024자 이하다
  - 위 `python3 -m unittest discover -s tests`의 `OK`에 `test_description_at_most_1024_chars`가 든다(run의 description은 고치지 않았다). 통과

## 계획과 달라진 점
- 통과 조건은 `git archive HEAD`를 풀라고 했지만, 바뀐 것을 커밋하기 전에 돌려야 기록을 같은 커밋에 넣을 수 있어 바뀐 것을 스테이지한 트리(`git write-tree`)를 풀었다. 이 커밋의 HEAD와 같은 내용이다.
- 4번의 조건부 줄을 "넷째 줄"이 아니라 "`고칠 문제:` 줄"로 가리키게 바꿨다. 표지 줄을 더하면 조건부 줄이 없을 때 넷째 줄이 표지 줄이 되어 "넷째 줄"로는 가리킬 수 없다. 결정의 "그 줄을 가리키게 고친다"를 따른 것이다.
- 낱말에 "표지 줄"을 더했다. TODO에 적히지 않았지만 작업 트리의 스킬 줄과의 차례(표지 줄 뒤)를 한 곳에 적으려는 것이다.

## 남은 것
- 고친 run의 동작(8번의 시각·해시 판정, "멈춘다" 4의 결정 줄 점검, 두 단계 명령의 헤드리스 통과)은 돌려 보지 않았다. task 머리의 "돌리지 않음"이 정한 것이다.
- 테스트는 규칙 글이 제 절에 있는지만 본다. 글을 다른 말로 고치면 같은 뜻이어도 실패한다.
- phase, check, retro가 표지 줄을 보고 보고 꼴을 가르는 쪽은 이 task 밖(002)이라, 지금은 표지 줄이 있어도 받는 쪽이 쓰지 않는다.

## 하네스에서 걸린 것
- 통과 조건의 `git archive HEAD`는 phase 스킬 5번(끝에 한 커밋)과 차례가 맞지 않는다. 커밋 전에는 HEAD에 바뀐 것이 없다. 스테이지한 트리로 대신했다.

## 확인 1

**통과 조건**
- 완료 조건 1이 참이다
  - `plugins/plate/skills/run/SKILL.md`의 "8. 고칠 phase를 더한다", "멈춘다", 낱말 "작업 트리의 스킬 줄", 맡기는 글 다섯의 코드 블록을 읽음 → #46: 8번 첫 문단이 고칠 파일이 완료 조건의 시각·본문 해시로 보는 파일인지와 다시 참으로 둘 길이 계획에 있는지 보고, 없으면 "계획을 바꾸게 하는 문제"로 "멈춘다"로 간다. "멈춘다" 자리 목록에도 그 경우가 있다. #47: 8번은 `git log -1 --format=%h -- docs/tasks/NNN-slug/retro.md`로 해시를 얻고 `git log --format='%h %s' {해시}..HEAD -- docs/tasks/`를 따로 부르고, 낱말은 `git merge-base {기본 브랜치} HEAD`로 해시를 얻고 `git diff --name-only {해시} HEAD`를 따로 부르는 두 단계다. #48: "멈춘다" 4가 "계획 수정마다 결정 줄 하나다"를 적고, 커밋하기 전에 결정 줄이 task 머리(tasks 머리)에 있는지 본다. #51: 130, 146, 168, 296, 307행 — 다섯 코드 블록의 마지막 줄이 `부른 쪽: plate:run`이다. 통과
  - `grep -n 'git[^`]*\$(' plugins/plate/skills/run/SKILL.md` → 출력 없음(종료 코드 1). 통과
- 완료 조건 2가 참이다
  - `python3 -m unittest discover -s tests` → `Ran 153 tests in 16.054s` / `OK`. 통과
  - `mktemp -d`에 `git archive HEAD`(39804cf)를 풀어 "하네스 eval을 맡긴다" 코드 블록의 `부른 쪽: plate:run` 줄을 지우고 돌림 → `FAIL: test_51_marker_line_ends_every_hand_off_block (test_skill_rules.RunRulesTest) (heading='하네스 eval을 맡긴다')`, `FAILED (failures=1)`. 다시 풀어 8번의 계획 커밋 찾기를 `` `git log --format='%h %s' $(git log -1 --format=%h -- docs/tasks/NNN-slug/retro.md)..HEAD -- docs/tasks/` `` 한 줄로 되돌리고 돌림 → `FAIL: test_47_no_command_substitution_in_git_commands (test_skill_rules.RunRulesTest)`, `FAILED (failures=1)`. 통과
- 완료 조건 3이 참이다
  - `docs/PRD.md` 7 → 계획이 틀림의 괄호에 시각·본문 해시로 보는 파일을 고칠 때의 멈춤이 있고, "고칠 때마다 결정에 줄 하나를 더하고, 커밋 전에 그 줄이 있는지 본다"가 있다. `docs/ARCHITECTURE.md` 48행 맡기는 글 문단 → 표지 줄 `부른 쪽: plate:run`이 있다. 54행 run 문단 → 시각·해시 멈춤(#46)과 수정마다 결정 줄 하나·커밋 전 점검(#48)이 있다. 39행 `test_skill_rules.py` 줄 → 시각·해시 멈춤, 명령 치환 없음, 결정 줄, 표지 줄 넷이 있다. `README.md` `run` 행의 멈춤 괄호 → 시각·본문 해시로 보는 파일의 멈춤이 있다. 통과
- 모든 스킬의 description이 1024자 이하다
  - 위 `python3 -m unittest discover -s tests`의 `OK`에 `test_description_at_most_1024_chars`가 든다. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 153 tests`, `OK`. 통과

**남은 것**
- 고친 run의 동작(8번의 시각·해시 판정, "멈춘다" 4의 결정 줄 점검, 두 단계 명령의 헤드리스 통과)은 돌려 보지 않았다 → 돌려 보지 않은 위험이고, task 머리 완료 조건 1의 `- 돌리지 않음: run은 사람에게 묻는 스킬이고, 8번과 "멈춘다"는 회고의 문제와 계획 수정까지 가는 tasks를 차려야 닿는다…` 줄이 돌리지 않기로 정한 동작이다. 하네스에서 걸린 것
- 테스트는 규칙 글이 제 절에 있는지만 보아 같은 뜻의 다른 말로 고치면 실패한다 → 테스트의 취약함에 대한 위험이고, 통과 조건(완료 조건 2)은 글이 빠지면 실패하는지와 모든 테스트 통과를 볼 뿐 다른 말로 고쳤을 때의 동작을 보지 않는다. 걸리지 않는다. 하네스에서 걸린 것

**실패**
- 없음

**하네스에서 걸린 것**
- 남은 것: 고친 run의 동작(8번의 시각·해시 판정, "멈춘다" 4의 결정 줄 점검, 두 단계 명령의 헤드리스 통과)은 돌려 보지 않았다(task 머리 완료 조건 1의 `돌리지 않음` 줄).
- 남은 것: 테스트는 규칙 글이 제 절에 있는지만 본다. 글을 다른 말로 고치면 같은 뜻이어도 실패한다.
- 통과 조건의 `git archive HEAD`는 phase 스킬이 기록까지 한 커밋으로 넣는 차례와 맞지 않아 수행 쪽이 스테이지한 트리로 대신했다. 확인은 커밋 뒤라 `git archive HEAD` 그대로 돌렸다.

**판정**: 통과
