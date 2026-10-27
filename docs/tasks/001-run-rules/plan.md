# run의 이슈 넷을 고친다

## 목표
run 본문에서 #46의 run 쪽(해시·시각으로 보는 파일을 고칠 때의 멈춤), #47(명령 치환 없는 두 단계 명령), #48(계획 수정마다의 결정 줄 점검), #51의 맡기는 글(표지 줄 `부른 쪽: plate:run`)을 고치고, 그 규칙 글이 빠지면 실패하는 테스트를 더하고, run의 바뀐 동작을 적은 맥락 문서와 README의 줄을 맞춘다.

## 범위 밖
- plan, phase, check, retro, review, eval 본문을 고치는 것(002, 003의 일)
- run의 description을 고치는 것
- 버전을 올리는 것(003의 일)
- run의 고친 동작을 헤드리스로 돌리는 것

## 완료 조건
1. tasks 완료 조건 1이 참이다
   - 확인: `plugins/plate/skills/run/SKILL.md`의 "8. 고칠 phase를 더한다", "멈춘다", 낱말의 "작업 트리의 스킬 줄", 맡기는 글 다섯(4번, 5번, 7번, "코드 평가를 맡긴다", "하네스 eval을 맡긴다"의 코드 블록)을 읽어 네 이슈의 해결이 저마다 적혀 있다. #46: 8번 첫머리의 판정이 고칠 파일과 완료 조건의 시각·해시 확인의 관계를 보고, 다시 참으로 둘 길이 계획에 없으면 "멈춘다"로 간다. #47: 두 명령이 해시를 먼저 얻고 그 해시를 넣어 부르는 두 단계다. #48: "멈춘다" 4가 커밋 전에 결정 줄을 보고, 계획 수정마다 결정 줄 하나다. #51: 다섯 코드 블록마다 `부른 쪽: plate:run` 줄이 있다. 하나라도 없으면 실패
   - 확인: `grep -n 'git[^`]*\$(' plugins/plate/skills/run/SKILL.md`가 아무것도 내지 않는다
   - 돌리지 않음: run은 사람에게 묻는 스킬이고, 8번과 "멈춘다"는 회고의 문제와 계획 수정까지 가는 tasks를 차려야 닿는다. 표지 줄은 003의 phase 장면이 run의 맡기는 글 그대로 돌린다
2. 1의 규칙마다 글이 빠지면 실패하는 테스트가 `tests/test_skill_rules.py`에 있고, 모든 테스트가 통과한다
   - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
   - 확인: `mktemp -d`에 `git archive HEAD`를 풀어 run 본문 "하네스 eval을 맡긴다"의 코드 블록에서 `부른 쪽: plate:run` 줄을 지우고 돌리면 실패한다. 다시 풀어 8번의 계획 커밋 찾기를 `$(git log -1 --format=%h -- docs/tasks/NNN-slug/retro.md)`를 넣은 한 줄로 되돌리고 돌리면 실패한다
3. tasks 완료 조건 5의 run 쪽이 참이다: 맥락 문서와 README의 run 줄이 1이 바꾼 동작과 어긋나지 않는다
   - 확인: `docs/PRD.md`의 7, `docs/ARCHITECTURE.md` "패턴과 규칙"의 맡기는 글 문단(작업 트리의 스킬 줄을 적은 문단)과 run 문단(시작 권한부터 RUNLOG 커밋까지 적은 문단), 디렉터리 구조의 `test_skill_rules.py` 줄, `README.md`의 `run` 행을 문서마다 따로 읽는다. 견줄 것: run 문단과 PRD 7이 해시·시각으로 보는 파일을 고칠 때의 멈춤과 계획 수정마다의 결정 줄을 적는다. 맡기는 글 문단이 표지 줄 `부른 쪽: plate:run`을 적는다. README `run` 행의 멈춤 괄호가 해시·시각으로 보는 파일의 멈춤을 담는다. `test_skill_rules.py` 줄이 이 task가 더한 run 규칙(#46, #47, #48, #51)을 담는다. 하나라도 어긋나면 실패

## 결정
- 표지 줄은 맡기는 글 코드 블록의 마지막 줄 `부른 쪽: plate:run`이다. 4번의 조건부 줄(고칠 문제)을 설명하는 글은 표지 줄을 더한 뒤에도 그 줄을 가리키게 고친다. 이유: tasks 머리의 결정. 003의 다섯 스킬이 이 글자 그대로를 본다
- #47의 두 단계는 먼저 해시를 얻는 명령(`git log -1 --format=%h -- docs/tasks/NNN-slug/retro.md`, `git merge-base {기본 브랜치} HEAD`)을 부르고, 그 출력을 넣어 다음 명령(`git log --format='%h %s' {해시}..HEAD -- docs/tasks/`, `git diff --name-only {해시} HEAD`)을 부른다. 이유: 헤드리스 권한 검사가 명령 치환을 승인 요구로 막고, 한 명령씩 부르면 돈다(`docs/TOOLS.md`의 "실행 스킬의 판정에서 본 것")
