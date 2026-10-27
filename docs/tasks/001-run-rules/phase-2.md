# Phase 2: 장면 A와 B를 돌린다

**목표**: 시작할 때의 권한 물음(#40)과 `RUNLOG.md`의 커밋 자리(#44)를 임시 복제본에서 돌려 `docs/TOOLS.md`에 남긴다.

**테스트 먼저**: 아니오 — 스킬을 돌려 보고 `.md`에 적는다

**읽을 것**
- `plugins/plate/skills/run/SKILL.md`의 "1. 시작 조건을 본다", "7. task 회고를 맡긴다", "tasks 끝", "`RUNLOG.md`" 절 (phase 1이 고친 동작)
- `docs/TOOLS.md`의 "Claude Code" 절 (헤드리스 명령의 꼴, `--resume`, "스킬을 헤드리스로 돌려 볼 때의 허용 목록", "고친 cleanup 스킬을 두 장면으로 다시 돌려 본 것"의 장면 절 꼴)

**TODO**
- [x] 장면 A: 복제본에 phase 하나가 남은 작은 tasks를 차리고 `--permission-mode plan`으로 run을 부른다. `RUNLOG.md`에 에이전트 줄이 없고 출력이 plan 모드를 알리며 바꿀지 묻고 멈춘 것을 본다 (임시 폴더)
- [x] 장면 B: 새 복제본에 phase가 모두 통과하고(`done-phase-1.md`에 판정 통과인 확인 절) 회고가 없으며 `RUNLOG.md`에 실행 방식 `tasks 일괄` 줄이 있는 작은 tasks를 차리고 run을 부른다. "고칠지"를 묻고 멈춘 자리에서 `git log --format='%h %s' --name-only`로 회고 커밋 뒤와 하네스 eval 커밋 뒤에 `RUNLOG.md`만 바꾼 커밋이 저마다 있는지, `git status --short`가 비었는지 본다 (임시 폴더)
- [x] 결과가 run 본문의 결함을 보이면 `plugins/plate/skills/run/SKILL.md`를 고치고 두 장면을 새 복제본에서 다시 돈다 (`plugins/plate/skills/run/SKILL.md`)
- [x] `docs/TOOLS.md`의 "Claude Code" 절 끝에 run 장면 A·B 절이 더해진다. task 머리의 결정에 적힌 필드를 장면마다 적는다 (`docs/TOOLS.md`)

**통과 조건**
- 장면 A와 B의 결과가 남았고 기대대로다(완료 조건 3의 A, B).
  - 확인: 더해진 절을 읽어 장면 A·B마다 Claude Code 버전, 돌린 시각, 세션 id, 기대한 결과와 본 결과가 있고 본 결과가 기대와 같다. 장면 A의 기대는 `RUNLOG.md`에 에이전트 줄이 없고 출력이 plan 모드를 알리며 묻고 멈춘 것, 장면 B의 기대는 회고 커밋 뒤와 하네스 eval 커밋 뒤에 `RUNLOG.md`만 바꾼 커밋이 저마다 있고 멈춘 자리의 `git status --short`가 빈 것이다
  - 확인: 그 절의 돌린 시각이 `git log -1 --format=%cI -- plugins/plate/skills/run/SKILL.md`보다 늦다
- 완료 조건 1이 여전히 참이다(이 phase가 run 본문을 고쳤을 때).
  - 확인: run 본문의 "1. 시작 조건을 본다", "7. task 회고를 맡긴다", "8. 고칠 phase를 더한다", "멈춘다", "코드 평가를 맡긴다", "하네스 eval을 맡긴다", "`RUNLOG.md`" 절을 읽어 다섯 해결이 저마다 적혀 있다
  - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`, `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`

## 한 일
- 장면 A: `mktemp -d`의 복제본(`/var/folders/0j/cj37rxmj1mj73vhflqpgsxm00000gn/T/tmp.xBtqx5E5M1/repo`, main `509b234`)의 `tasks/scene-a`에 `phase-1.md`가 남은 tasks를 차리고 `claude -p "/plate:run" --permission-mode plan`으로 불렀다. Agent 호출 0, `RUNLOG.md` 없음, 출력이 plan 모드와 막힐 쓰기를 알리고 "plan 모드를 끄고 이어 갈까요?"로 묻고 멈췄다 (임시 폴더)
- 장면 B: 새 복제본(`…/tmp.tAzMpMoMku/repo`)의 `tasks/scene-b`에 `done-phase-1.md`(판정 통과인 `## 확인 1`), 회고 없음, `RUNLOG.md`의 `tasks 일괄` 줄인 tasks를 차리고 `--permission-mode acceptEdits`로 run을 불렀다. "고칠지"를 묻고 멈춘 자리에서 `git log --format='%h %s' --name-only afc02b9..HEAD`에 `ed93268 001-hello: RUNLOG`(회고 커밋 `9e7967b` 뒤), `9145f2a scene-b: RUNLOG`(코드 평가 커밋 뒤), `823e8ea scene-b: RUNLOG`(하네스 eval 커밋 `5f2428e` 뒤)가 저마다 `docs/tasks/RUNLOG.md` 하나만 바꿨고 `git status --short`가 비었다 (임시 폴더)
- 결과가 run 본문의 결함을 보이면 고친다: 두 장면 모두 기대대로여서 run 본문을 고치지 않았다. 장면 B의 첫 차림이 회고에서 멈춘 것과 `origin/HEAD`가 `tasks/release-prep`을 가리킨 것은 장면을 차린 방법에서 온 것이다(아래 "계획과 달라진 점", "남은 것")
- `docs/TOOLS.md`의 "Claude Code" 절 끝에 "고친 run을 장면 A·B로 돌려 본 것" 절을 더했다. 장면마다 Claude Code 버전, 복제본의 main 커밋, 돌린 시각, 세션 id, 차린 tasks의 꼴, 기대한 결과, 본 결과, 걸린 시간, 막힌 명령, 임시 폴더의 기록 경로(지워질 수 있다고 밝힘)를 적었다 (`docs/TOOLS.md`)

## 확인 결과
- 장면 A와 B의 결과가 남았고 기대대로다(완료 조건 3의 A, B).
  - `docs/TOOLS.md`의 "고친 run을 장면 A·B로 돌려 본 것" 절을 읽음 → 장면 A: 2.1.311, 18:40:01~18:40:18, 세션 `75d5f20c-…`, 기대(에이전트 줄 없음, plan 모드를 알리며 묻고 멈춤)와 본 결과(Agent 0, `RUNLOG.md` 없음, plan 모드 알림과 물음)가 같다. 장면 B: 2.1.311, 18:44:23~19:26:47, 세션 `02367cb0-…`, 기대(회고 뒤와 하네스 eval 뒤의 `RUNLOG.md`만 바꾼 커밋, 빈 `git status --short`)와 본 결과(`ed93268`, `823e8ea`, 빈 상태)가 같다. 통과
  - `git log -1 --format=%cI -- plugins/plate/skills/run/SKILL.md` → `2026-10-27T18:38:03+09:00`. 절의 돌린 시각 18:40:01, 18:44:23(첫 차림 18:40:37)이 모두 늦다. 통과
- 완료 조건 1이 여전히 참이다(이 phase가 run 본문을 고쳤을 때).
  - 이 phase는 run 본문을 고치지 않았다(`git diff --stat`에 `plugins/plate/skills/run/SKILL.md` 없음). 다섯 해결은 phase 1의 글 그대로다. 통과
  - `python3 -m unittest discover -s tests` → `Ran 129 tests` / `OK`. `claude plugin validate .` → `✔ Validation passed`. 통과

## 계획과 달라진 점
- 장면 B를 처음 차린 tasks(`notes/hello.txt`만 만들고 범위 밖이 "다른 파일을 고치는 것")는 회고가 `docs/ARCHITECTURE.md`의 디렉터리 구조에 `notes/`가 없다는 문제를 찾아, run이 범위 밖과 부딪힌다며 "멈춘다"로 가 tasks 끝에 닿지 않았다. 완료 조건과 범위 밖에 `docs/ARCHITECTURE.md`의 `notes/` 줄을 넣어 새 복제본에 다시 차리고 돌렸다. 첫 차림도 회고 커밋 뒤의 `RUNLOG` 커밋과 빈 `git status --short`를 보였고, 그 기록을 절에 함께 적었다
- 허용 목록은 결정대로 "스킬을 헤드리스로 돌려 볼 때의 허용 목록"을 쓰되, 장면 B에는 run이 브랜치와 갈라진 곳을 보는 `"Bash(git merge-base:*)" "Bash(git symbolic-ref:*)" "Bash(git switch:*)" "Bash(git branch:*)"`를 더했다(`docs/TOOLS.md` 5단계의 판정에서 run에 필요하다고 적힌 것). 작은 tasks는 복제본의 `tasks/<이름>` 브랜치에 차려 run의 기본 브랜치 물음이 나지 않게 했다

## 남은 것
- 장면 B의 복제본은 `origin/HEAD`가 원본의 지금 브랜치 `tasks/release-prep`을 가리켜, run의 작업 트리의 스킬 줄 판정과 코드 평가의 `git merge-base tasks/release-prep HEAD`가 로컬 브랜치가 없어 실패했고 둘 다 원격 추적 ref로 돌아갔다. 하네스 eval이 이를 실패 하나와 "review: 로컬 기본 브랜치가 없을 때" 고칠 거리로 적었다. 장면을 차린 방법에서 온 것이라 run 본문은 고치지 않았다. phase 3의 장면은 복제본을 만든 뒤 `git remote set-head origin main`을 하면 피한다. review·run이 로컬 기본 브랜치가 없을 때의 길을 적지 않은 것은 이 task의 범위 밖이다
- 장면 B의 시작에서 run은 acceptEdits 모드를 확인할 수 없어 묻지 않고 이어 갔다(1번의 "확인할 수 없으면" 갈래). 헤드리스 acceptEdits 세션에서 쓰기가 막힐 모드를 알아보는 갈래는 돌려 보지 않았다
- 장면 B에서 `;`·`&&`·`for`·명령 치환으로 이은 Bash 6개가 승인을 요구하며 막혔다(허용 목록으로 풀리지 않는 꼴)

## 하네스에서 걸린 것
- 계획의 장면 B는 "phase가 모두 통과하고 회고가 없는 작은 tasks"만 정하고, 그 task가 맥락 문서와 맞아 회고가 통과해야 tasks 끝에 닿는다는 것을 적지 않았다. 처음 차린 tasks가 회고에서 멈춰 다시 차렸다
- 결정의 "이 저장소의 main을 복제"는 원본이 다른 브랜치에 있으면 복제본의 `origin/HEAD`가 그 브랜치를 가리키는 것을 다루지 않는다. run과 review가 기본 브랜치를 `tasks/release-prep`으로 봤다

