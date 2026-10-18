# Phase 4: retro를 task 회고로 바꾸고 verify를 없앤다

**목표**: retro가 task 하나를 회고해 `retro.md`와 `FRICTION.md`에 적고, verify 스킬은 없다.

**테스트 먼저**: 아니오 — `.md`만 고치고 지운다.

**읽을 것**
- `plugins/plate/skills/retro/SKILL.md` (지금의 phase 회고)
- `plugins/plate/skills/verify/SKILL.md` (지금의 작업 검증: 완료 조건 확인, 작업 전체 점검의 넷, 테스트 먼저 기록 확인. 지우기 전에 읽는다)
- `plugins/plate/skills/check/SKILL.md` (phase 3이 만든 확인 절)
- `plugins/plate/skills/phase/SKILL.md` (기록 다섯 절과 "하네스에서 걸린 것")
- `plugins/plate/skills/plan/SKILL.md` (tasks 머리와 task 머리의 양식)

**TODO**
- [ ] retro가 task 폴더 하나를 받아 task 머리의 완료 조건 확인과 `docs/ARCHITECTURE.md` 명령 절의 빌드·린트·테스트를 직접 돌린다(없는 명령은 "없음") (`plugins/plate/skills/retro/SKILL.md`)
- [ ] task의 커밋이 바꾼 것 전부를 task 머리, tasks 머리, 맥락 문서에 대어 지금 verify의 넷(목표와 결정, 범위 밖, 맥락 문서, 결함)으로 점검하고, 테스트 먼저가 "예"인 `done-phase-N.md`마다 실패 출력과 통과 출력이 이 순서로 있는지 본다
- [ ] 회고 기록이 task 폴더의 `retro.md`에 회고 절(몇 번째인지, 확인, 문제, 판정 통과 또는 문제 있음)로 쌓이고, 판정과 문제 수와 기록 위치를 정해 둔 줄로 돌려준다
- [ ] retro가 `docs/tasks/FRICTION.md`에 그 task에서 tasks 끝에 볼 것(문제, 멈춤, 스킬로 만들 후보)을 task 이름과 함께 한 줄씩 더한다. phase 기록의 "하네스에서 걸린 것", `RUNLOG.md`의 물은 줄, 점검에서 본 것에서 모은다. 볼 것이 없으면 task 이름과 "없음"을 한 줄로 적는다. 파일이 없으면 만든다
- [ ] retro는 `retro.md`와 `FRICTION.md`만 `NNN-slug: 회고`로 커밋한다. 고치지 않고 묻지 않는다
- [ ] phase 하나의 회고, "확인만" 방식, 끝나지 않은 작업, "배운 것"이 본문에서 빠진다
- [ ] `plugins/plate/skills/verify/`가 지워진다
- [ ] description이 새 동작을 말한다

**통과 조건**
- retro 본문이 TODO대로다
  - 확인: `plugins/plate/skills/retro/SKILL.md`를 읽어 TODO 항목마다 그 동작이 적힌 곳을 찾는다
- verify가 없고 retro에 옛 방식이 남지 않았다
  - 확인: `ls plugins/plate/skills/verify` → `No such file or directory`
  - 확인: `grep -n "verify\|확인만\|배운 것" plugins/plate/skills/retro/SKILL.md` → 0줄
- 완료 조건 2 가운데 retro 본문의 몫이 참이다
  - 확인: `grep -n "작업" plugins/plate/skills/retro/SKILL.md`의 줄을 모두 읽어 tasks, task, phase를 가리키는 "작업"이 없다
