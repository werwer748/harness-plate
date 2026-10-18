# Phase 11: run 일괄 끝까지와 check 세 번 실패를 시험한다

**목표**: 일괄 장면과 멈춤 장면을 돌려 완료 조건 6, 7, 8을 확인하고, 이 단계의 판정에서 확인한 도구 사실을 `docs/TOOLS.md`에 적는다.

**테스트 먼저**: 아니오 — 이 레포에서는 `docs/TOOLS.md`만 고친다. 시험 폴더와 도구는 저장소 밖이다.

**읽을 것**
- `docs/TOOLS.md` (판정 묶음을 적는 꼴과 헤드리스 사실)
- `~/plate-rail-test/bin/` (phase 10이 바꾼 실행 도구와 시험 폴더를 만드는 도구)
- `plugins/plate/skills/run/SKILL.md`, `plugins/plate/skills/check/SKILL.md`, `plugins/plate/skills/retro/SKILL.md`, `plugins/plate/skills/review/SKILL.md`, `plugins/plate/skills/eval/SKILL.md` (기대하는 동작)

**TODO**
- [ ] run 일괄 끝까지 장면이 돈다: 테스트가 있는 작은 프로젝트에 task 둘 이상의 계획을 두고, task 회고에서 문제가 나올 거리(task 머리의 완료 조건을 phase가 채우지 않는 곳)와 review가 소스 문제로 볼 거리를 미리 심는다. run을 부르고 방식은 "tasks 일괄"로 답해 끝의 보고와 물음까지 간 뒤, 소스 문제 하나는 고치고 하나는 미루고 plate 자체의 고칠 거리 하나는 이슈로 올린다고 답해 합칠지 묻는 데까지 간다
- [ ] 비우기 전 상태를 되살린 폴더에서 같은 문제로 끝 단계를 다시 돌려 그 이슈에 "다시 나옴" 댓글이 달리는지 보고, 올린 이슈를 `gh issue delete`로 지운다
- [ ] check 세 번 실패 장면이 돈다: 통과 조건을 채울 수 없는 phase가 든 계획에서 run을 부르고 방식은 "tasks 일괄"로 답한다
- [ ] 장면의 기록이 `~/plate-rail-test/logs/`에 남는다
- [ ] 완료 조건 6, 7, 8, 13의 확인을 모두 돌려 결과를 기록에 적는다
- [ ] `docs/TOOLS.md`의 Claude Code 절에 이 단계의 판정 묶음이 더해진다: 에이전트 결과로 돌아오는 사용량, `gh`로 이슈 올리기·댓글·지우기, 시험 폴더와 기록 위치, 실행 시간을 날짜·버전과 함께 적는다

**통과 조건**
- 완료 조건 6, 7, 8이 참이다
  - 확인: 세 완료 조건의 확인을 모두 돌린다
- 완료 조건 13이 참이다
  - 확인: 완료 조건 13의 확인을 돌린다
- 완료 조건 14가 참이다
  - 확인: 완료 조건 14의 확인을 돌린다
