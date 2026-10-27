# Phase 2: 장면 A와 B를 돌린다

**목표**: 시작할 때의 권한 물음(#40)과 `RUNLOG.md`의 커밋 자리(#44)를 임시 복제본에서 돌려 `docs/TOOLS.md`에 남긴다.

**테스트 먼저**: 아니오 — 스킬을 돌려 보고 `.md`에 적는다

**읽을 것**
- `plugins/plate/skills/run/SKILL.md`의 "1. 시작 조건을 본다", "7. task 회고를 맡긴다", "tasks 끝", "`RUNLOG.md`" 절 (phase 1이 고친 동작)
- `docs/TOOLS.md`의 "Claude Code" 절 (헤드리스 명령의 꼴, `--resume`, "스킬을 헤드리스로 돌려 볼 때의 허용 목록", "고친 cleanup 스킬을 두 장면으로 다시 돌려 본 것"의 장면 절 꼴)

**TODO**
- [ ] 장면 A: 복제본에 phase 하나가 남은 작은 tasks를 차리고 `--permission-mode plan`으로 run을 부른다. `RUNLOG.md`에 에이전트 줄이 없고 출력이 plan 모드를 알리며 바꿀지 묻고 멈춘 것을 본다 (임시 폴더)
- [ ] 장면 B: 새 복제본에 phase가 모두 통과하고(`done-phase-1.md`에 판정 통과인 확인 절) 회고가 없으며 `RUNLOG.md`에 실행 방식 `tasks 일괄` 줄이 있는 작은 tasks를 차리고 run을 부른다. "고칠지"를 묻고 멈춘 자리에서 `git log --format='%h %s' --name-only`로 회고 커밋 뒤와 하네스 eval 커밋 뒤에 `RUNLOG.md`만 바꾼 커밋이 저마다 있는지, `git status --short`가 비었는지 본다 (임시 폴더)
- [ ] 결과가 run 본문의 결함을 보이면 `plugins/plate/skills/run/SKILL.md`를 고치고 두 장면을 새 복제본에서 다시 돈다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] `docs/TOOLS.md`의 "Claude Code" 절 끝에 run 장면 A·B 절이 더해진다. task 머리의 결정에 적힌 필드를 장면마다 적는다 (`docs/TOOLS.md`)

**통과 조건**
- 장면 A와 B의 결과가 남았고 기대대로다(완료 조건 3의 A, B).
  - 확인: 더해진 절을 읽어 장면 A·B마다 Claude Code 버전, 돌린 시각, 세션 id, 기대한 결과와 본 결과가 있고 본 결과가 기대와 같다. 장면 A의 기대는 `RUNLOG.md`에 에이전트 줄이 없고 출력이 plan 모드를 알리며 묻고 멈춘 것, 장면 B의 기대는 회고 커밋 뒤와 하네스 eval 커밋 뒤에 `RUNLOG.md`만 바꾼 커밋이 저마다 있고 멈춘 자리의 `git status --short`가 빈 것이다
  - 확인: 그 절의 돌린 시각이 `git log -1 --format=%cI -- plugins/plate/skills/run/SKILL.md`보다 늦다
- 완료 조건 1이 여전히 참이다(이 phase가 run 본문을 고쳤을 때).
  - 확인: run 본문의 "1. 시작 조건을 본다", "7. task 회고를 맡긴다", "8. 고칠 phase를 더한다", "멈춘다", "코드 평가를 맡긴다", "하네스 eval을 맡긴다", "`RUNLOG.md`" 절을 읽어 다섯 해결이 저마다 적혀 있다
  - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`, `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
