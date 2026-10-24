# Phase 2: 회고 1의 문제를 고친다

**목표**: 회고 1에서 나온 문제를 모두 고친다.

**테스트 먼저**: 아니오 — `.md`만 고친다

**읽을 것**
- `docs/tasks/004-run-pr/retro.md`의 `## 회고 1` 절
- `plugins/plate/skills/run/SKILL.md`
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/ADR.md`
- `docs/TOOLS.md`

**TODO**
- [x] `docs/ARCHITECTURE.md` 48줄(패턴과 규칙의 막는 장치 문단)은 "에이전트의 푸시를 막는 기본은 스킬마다의 '푸시하지 않는다' 규칙이고, 푸시 훅은 흔한 꼴을 한 번 더 막는다"고 적는데, 이 task가 run의 절대 규칙 5(`plugins/plate/skills/run/SKILL.md` 20줄)의 "푸시하지 않는다"를 "푸시는 'PR을 연다'에서 승인받아 `tasks/<이름>`을 origin에 올릴 때만 한다"로 바꿔 run에는 그 규칙이 없다. 49줄의 run 규칙은 이 푸시를 적지만 48줄은 고치지 않아 같은 문서의 두 줄이 어긋난다. phase 1의 TODO와 완료 조건 3이 ARCHITECTURE에서 run 규칙과 데이터 흐름만 가리켰다(`docs/ARCHITECTURE.md`).

**통과 조건**
- 회고 1의 문제가 모두 고쳐졌다.
  - 확인: 문제마다 적힌 곳을 다시 읽거나 돌린다
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다

## 한 일
- `docs/ARCHITECTURE.md` 48줄(패턴과 규칙의 막는 장치 문단)의 "에이전트의 푸시를 막는 기본은 스킬마다의 '푸시하지 않는다' 규칙이고": 그 문장을 "에이전트의 푸시를 막는 기본은 스킬마다의 푸시 규칙(phase, check, retro, review, eval은 "푸시하지 않는다", run은 "PR을 연다"에서 승인받아 `tasks/<이름>`을 origin에 올릴 때만 푸시한다)이고, 푸시 훅은 흔한 꼴을 한 번 더 막는다."로 바꿨다. 괄호 안의 다섯 스킬은 `grep -ln '푸시하지 않는다' plugins/plate/skills/*/SKILL.md`가 낸 것이고, run의 글은 절대 규칙 5(20줄)를 옮겼다. 문단의 다른 글은 그대로다(`git diff --word-diff=porcelain`의 바뀐 낱말은 이 문장의 것뿐) (`docs/ARCHITECTURE.md`)

## 확인 결과
- 회고 1의 문제가 모두 고쳐졌다.
  - `grep -n -o '에이전트의 푸시를 막는 기본은[^.]*\.' docs/ARCHITECTURE.md` → 48줄 "에이전트의 푸시를 막는 기본은 스킬마다의 푸시 규칙(phase, check, retro, review, eval은 "푸시하지 않는다", run은 "PR을 연다"에서 승인받아 `tasks/<이름>`을 origin에 올릴 때만 푸시한다)이고, 푸시 훅은 흔한 꼴을 한 번 더 막는다." run 절대 규칙 5(`plugins/plate/skills/run/SKILL.md` 20줄)의 "푸시는 "PR을 연다"에서 승인받아 `tasks/<이름>`을 origin에 올릴 때만 한다."와 ARCHITECTURE 49줄의 "푸시는 이 PR을 열 때만 한다"와 맞는다. `grep -ln '푸시하지 않는다' plugins/plate/skills/*/SKILL.md` → check, phase, eval, retro, review로 괄호 안의 다섯과 같다. 통과
- task 머리의 완료 조건이 모두 참이다.
  - 완료 조건 1: `plugins/plate/skills/run/SKILL.md`의 "비운다"(408~416), "PR을 연다"(418~455), "합친다"(457~466)를 `grep`과 `sed -n`으로 읽었다 → 410줄 origin이 GitHub 원격이면 "PR을 연다"에 쓸 것을 지우기 전에 읽어 둔다, 416줄 GitHub 원격이면 "PR을 연다"로, 그 밖(origin 없음, GitHub 아님, git 레포 아님)이면 "합친다"로 간다, 422줄 브랜치·가는 곳·제목·본문을 보여 주고 묻고 plate 워크플로가 없으면 댓글을 단다는 것도 적고 거절하면 "푸시하지 않고 합치지도 않고 브랜치를 그대로 둔 채" 10번으로, 423~425줄 `git push origin tasks/<이름>`, `gh pr create --base {기본 브랜치} --head tasks/<이름>`, `gh pr comment {PR 주소}`, PR 본문의 꼴에 요청, 목표, 코드 평가(다섯 등급과 Sonar way 게이트), 하네스 eval(여섯 등급), 고친 것, 올린 이슈, 459줄 "'비운다'에서 origin이 GitHub 원격이 아닐 때 온다". 통과
  - 완료 조건 2: run 20줄, 218줄, 485줄과 `grep -n '정해 둔 물음' plugins/plate/skills/eval/SKILL.md` → 20줄 "푸시는 "PR을 연다"에서 승인받아 `tasks/<이름>`을 origin에 올릴 때만 한다. GitHub 이슈, PR, 댓글은 승인받은 것만 올린다.", 218줄 "PR을 열지 물었으면 연 PR의 주소와 단 댓글의 주소. 열지 않았으면 그 까닭(거절, 실패한 명령과 오류), 댓글을 달지 않았으면 그 까닭(plate 워크플로가 있다, 실패한 명령과 오류)", 485줄 비운 뒤에 물은 것(PR을 열지, 합칠지, 그 자리의 커밋하지 않은 변경)은 적지 않는다, eval 40줄 "tasks 끝의 고칠지, PR을 열지, 합칠지다". 통과
  - 완료 조건 3: `grep -n "합칠\|합친\|PR을 열" docs/ARCHITECTURE.md docs/PRD.md`와 ARCHITECTURE 49줄, 67~69줄, PRD 18줄 → ARCHITECTURE 49줄 "`docs/tasks/`를 비운 뒤 `origin`이 GitHub이면 … PR을 열지 묻고, `origin`이 없거나 GitHub의 것이 아니면 기본 브랜치로 합칠지 묻는다.", 67~69줄 비운다 → GitHub이면 PR을 열지 → 없거나 GitHub의 것이 아니면 합칠지, PRD 18줄 "origin이 GitHub이면 run이 tasks 브랜치를 푸시해 기본 브랜치로 가는 PR을 열지 묻고 … origin이 GitHub이 아니거나 없으면 기본 브랜치로 합칠지 묻는다". 조건 없이 합칠지 묻는 옛 글은 없다. 통과

## 계획과 달라진 점
- 없음

## 남은 것
- 없음

## 하네스에서 걸린 것
- 없음
