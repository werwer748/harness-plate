# Phase 2: 열린 입력의 경계를 묻는다

**목표**: plan이 입력의 꼴이 열린 기능을 계획할 때 약속하는 꼴의 경계를 결정으로 묻는다.

**테스트 먼저**: 아니오 — `.md`만 고친다

**읽을 것**
- `plugins/plate/skills/plan/SKILL.md`의 5번(질문한다)과 적는 규칙의 "결정"
- `git show c2a983c^:docs/tasks/003-push-guard/plan.md` (task 머리 결정이 약속을 시험이 다루는 꼴로 닫은 곳)
- `git show c2a983c^:docs/tasks/RUNLOG.md` (34~50줄, 회고가 되풀이해 실패한 줄)
- `docs/ARCHITECTURE.md`의 푸시 훅 문단 ("약속하는 꼴은 시험이 다루는 꼴뿐"이라고 닫은 예)
- `docs/PRD.md`의 핵심 기능 3

**TODO**
- [ ] 5번에 생긴다. 요청한 기능이 입력의 꼴이 열린 것(셸 명령 글, 사용자가 쓴 글, 밖에서 오는 형식을 읽는 것)이면, 약속하는 꼴의 경계(무엇을 다루고 무엇을 다루지 않는지, 시험이 다루는 꼴로 닫을지)를 물어 결정으로 정한다. 추천안의 이유에는 경계가 없을 때 회고가 끝나지 않는다는 것을 든다 (`plugins/plate/skills/plan/SKILL.md`)
- [ ] `docs/ARCHITECTURE.md`와 `docs/PRD.md`에서 plan을 적은 줄이 바뀐 plan과 어긋나면 맞춘다 (`docs/ARCHITECTURE.md`, `docs/PRD.md`)

**통과 조건**
- 완료 조건 1의 첫째가 참이다.
  - 확인: 5번을 읽어 입력의 꼴이 열린 기능에서 경계를 결정으로 묻는 규칙이 있다
- 완료 조건 2가 참이다.
  - 확인: `grep -n '계획' docs/ARCHITECTURE.md docs/PRD.md`가 낸 줄을 하나씩 읽어 바뀐 plan과 어긋나는 줄이 없다
- phase 1이 이룬 완료 조건 1의 둘째, 셋째가 그대로 참이다.
  - 확인: phase 1의 통과 조건 확인을 다시 돌린다
- 테스트가 모두 통과한다.
  - 확인: `python3 -m unittest discover -s tests`가 `OK`
