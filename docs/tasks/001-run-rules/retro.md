# 회고

## 회고 1

**확인**
- 1. tasks 완료 조건 1이 참이다
  - `plugins/plate/skills/run/SKILL.md`의 "8. 고칠 phase를 더한다", "멈춘다", 낱말 "작업 트리의 스킬 줄"(과 새 낱말 "표지 줄"), 맡기는 글 다섯의 코드 블록을 읽음 → #46: 8번 첫 문단이 "고칠 파일이 task 머리나 tasks 머리의 완료 조건이 돌린 시각이나 본문 해시로 보는 파일이면, 고친 뒤 그 확인을 다시 참으로 둘 길 … 이 계획에 있는지도 본다"와 "이 경우도 계획을 바꾸게 하는 문제다"로 "멈춘다"로 가고, "멈춘다" 자리 목록에도 같은 경우가 있다. #47: 8번은 `git log -1 --format=%h -- docs/tasks/NNN-slug/retro.md`로 해시를 얻고 `git log --format='%h %s' {해시}..HEAD -- docs/tasks/`를 따로 부르고, 낱말은 `git merge-base {기본 브랜치} HEAD`로 해시를 얻고 `git diff --name-only {해시} HEAD`를 따로 부르는 두 단계다. #48: "멈춘다" 4에 "계획 수정마다 결정 줄 하나다"와, 커밋 문장 앞에 "커밋하기 전에 이번 수정의 결정 줄이 task 머리(tasks 머리를 고쳤으면 tasks 머리에도)에 있는지 보고"가 있다. #51: 130, 146, 168, 296, 307행 — 다섯 코드 블록의 마지막 줄이 `부른 쪽: plate:run`이고, 4번의 조건부 줄 설명은 "`고칠 문제:` 줄은 …"으로 그 줄을 가리킨다. 통과
  - `grep -n 'git[^`]*\$(' plugins/plate/skills/run/SKILL.md` → 출력 없음(종료 코드 1). 본문 전체의 `$(`도 없다. 통과
  - 돌리지 않음: task 머리가 정한 대로 run의 고친 동작은 돌리지 않았다
- 2. 1의 규칙마다 글이 빠지면 실패하는 테스트가 있고, 모든 테스트가 통과한다
  - `python3 -m unittest discover -s tests` → `Ran 153 tests in 16.098s` / `OK`. 통과
  - `mktemp -d`에 `git archive HEAD`(4a9d713)를 풀어 "하네스 eval을 맡긴다" 코드 블록의 `부른 쪽: plate:run` 줄을 지우고 돌림 → `FAIL: test_51_marker_line_ends_every_hand_off_block (test_skill_rules.RunRulesTest) (heading='하네스 eval을 맡긴다')`, `FAILED (failures=1)`. 다시 풀어 8번의 계획 커밋 찾기를 `` `git log --format='%h %s' $(git log -1 --format=%h -- docs/tasks/NNN-slug/retro.md)..HEAD -- docs/tasks/` `` 한 줄로 되돌리고 돌림 → `FAIL: test_47_no_command_substitution_in_git_commands (test_skill_rules.RunRulesTest)`, `FAILED (failures=1)`. 통과
- 3. 맥락 문서와 README의 run 줄이 1이 바꾼 동작과 어긋나지 않는다
  - `docs/PRD.md` 17행(7) → 계획이 틀림의 괄호에 시각·본문 해시로 보는 파일을 고칠 때의 멈춤, "고칠 때마다 결정에 줄 하나를 더하고, 커밋 전에 그 줄이 있는지 본다"가 있다. `docs/ARCHITECTURE.md` 48행 맡기는 글 문단 → 두 단계 명령과 표지 줄 `부른 쪽: plate:run`(작업 트리의 스킬 줄은 그 뒤)이 있다. 54행 run 문단 → 시각·해시 멈춤(#46), 수정마다 결정 줄 하나와 커밋 전 점검(#48), 계획 커밋 찾기의 두 단계(#47)가 있다. 39행 `test_skill_rules.py` 줄 → 시각·해시 멈춤, 명령 치환 없음, 결정 줄, 표지 줄 넷이 있다. `README.md` `run` 행의 멈춤 괄호 → "고칠 파일이 완료 조건이 돌린 시각이나 본문 해시로 보는 파일인데 다시 참으로 둘 길이 계획에 없으면 멈추고 논의한다"가 있다. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 153 tests`, `OK`. 통과

**남은 것**
- phase 1: 고친 run의 동작(8번의 시각·해시 판정, "멈춘다" 4의 결정 줄 점검, 두 단계 명령의 헤드리스 통과)은 돌려 보지 않았다 → 문제 아님 (task 머리 완료 조건 1의 `돌리지 않음` 줄이 돌리지 않기로 정한 동작이고, 바뀐 본문을 직접 읽어 세 동작의 글이 저마다 제 자리에 있고 서로 어긋나지 않음을 봤다)
- phase 1: 테스트는 규칙 글이 제 절에 있는지만 본다. 글을 다른 말로 고치면 같은 뜻이어도 실패한다 → 문제 아님 (tasks 머리의 결정 "고친 동작은 규칙 글 테스트로 본다"가 고른 방식이고, 완료 조건 2는 글이 빠지면 실패하는지만 본다)
- phase 1: phase, check, retro가 표지 줄을 보고 보고 꼴을 가르는 쪽은 이 task 밖이라, 지금은 표지 줄이 있어도 받는 쪽이 쓰지 않는다 → 문제 아님 (tasks 머리 task 목록의 `003-agent-rules`의 일이고 이 task의 범위 밖이다. 기록은 "002"라 적었으나 task 목록상 003이다)

**문제**
- 없음

**판정**: 통과
