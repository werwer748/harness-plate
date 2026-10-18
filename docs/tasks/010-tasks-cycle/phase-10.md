# Phase 10: setup·plan과 run task 하나씩을 시험한다

**목표**: 바뀐 본문으로 setup·plan 장면과 run task 하나씩 장면을 헤드리스로 돌려 완료 조건 3, 4, 5를 확인한다.

**테스트 먼저**: 아니오 — 이 레포의 코드를 바꾸지 않는다. 시험 폴더와 도구는 저장소 밖(`~/plate-rail-test`)에 둔다.

**읽을 것**
- `docs/TOOLS.md` (헤드리스 실행의 꼴, 허용 목록, 막히는 명령의 꼴, 세션 잇기, 답을 미리 주면 묻지 않는다는 것, 실행 시간)
- `~/plate-rail-test/bin/run.sh` (지난 시험의 실행 도구와 허용 목록)
- `~/plate-rail-test/bin/vfmake.sh` (지난 시험 폴더를 만드는 법)
- `plugins/plate/skills/setup/SKILL.md`, `plugins/plate/skills/plan/SKILL.md`, `plugins/plate/skills/run/SKILL.md`, `plugins/plate/skills/check/SKILL.md`, `plugins/plate/skills/retro/SKILL.md` (기대하는 동작)

**TODO**
- [ ] `~/plate-rail-test`의 실행 도구가 새 스킬(check, review, eval)과 `gh`를 허용 목록에 담고, 이 단계의 시험 폴더를 만드는 도구가 생긴다
- [ ] setup·plan 장면이 돈다: 커밋이 없는 빈 git 레포에서 setup을 부르고, 셋업된 작은 프로젝트(`docs/ARCHITECTURE.md`에 명령 절이 없다)에서 task 둘 이상이 나올 요청으로 plan을 부른다. 답을 미리 주지 않고 턴마다 이어 승인하며, 승인 전 턴마다 `git status --short`와 `ls docs/tasks`를 남긴다. 쓴 뒤에는 tasks가 진행 중인 그 폴더에서 새 요청으로 plan을 다시 부른다
- [ ] run task 하나씩 장면이 돈다: task 둘 이상이 계획된 테스트가 있는 작은 프로젝트에서 run을 부르고, 방식은 "task 하나씩"으로 답해 첫 task의 회고 뒤 물음까지 간다
- [ ] 장면의 기록이 `~/plate-rail-test/logs/`에 남는다
- [ ] 완료 조건 3, 4, 5의 확인을 모두 돌려 결과를 기록에 적는다

**통과 조건**
- 완료 조건 3이 참이다
  - 확인: 완료 조건 3의 확인을 모두 돌린다
- 완료 조건 4가 참이다
  - 확인: 완료 조건 4의 확인을 모두 돌린다
- 완료 조건 5가 참이다
  - 확인: 완료 조건 5의 확인을 모두 돌린다
