# Phase 2: "조건"과 "TODO"의 적는 규칙과 양식

**목표**: plan의 적는 규칙 "조건"에 #20과 #23의 줄이, "TODO"에 #24의 바뀜의 종류와 자리가 더해지고, 양식의 TODO 줄과 맥락 문서가 그와 맞는다.

**테스트 먼저**: 아니오 — `.md`만 고친다

**읽을 것**
- `plugins/plate/skills/plan/SKILL.md` (188줄 양식의 TODO 줄, 220~232줄 "조건", 256~267줄 "TODO", phase 1이 고친 6번)
- `gh issue view 20 -R werwer748/harness-plate` (#20의 본문)
- `gh issue view 23 -R werwer748/harness-plate` (#23의 본문: 세 꼴의 실패 장면)
- `gh issue view 24 -R werwer748/harness-plate` (#24의 본문)
- `docs/PRD.md` (13줄 핵심 기능 3)
- `docs/ARCHITECTURE.md` (25줄 plan 스킬 줄, 57~58줄 데이터 흐름의 계획)

**TODO**
- [ ] "조건"에 다른 phase의 확인을 다시 돌릴 때 그 확인 글을 이 phase의 통과 조건에 옮겨 적고 "phase N의 확인" 같은 가리킴만 두지 않는다는 줄이 더해진다 (`plugins/plate/skills/plan/SKILL.md`)
- [ ] "조건"에 #23의 세 줄이 저마다 더해진다: 도구 출력을 보는 확인은 그 도구가 실제로 내는 필드나 줄로 적는다, 금지를 보는 `grep`은 대상 줄로 좁힌다, 뒤 task가 바꿀 수 있는 대상과 견주는 확인은 견줄 커밋이나 시점을 적는다 (`plugins/plate/skills/plan/SKILL.md`)
- [ ] "TODO"의 첫 줄이 결과 꼴을 두되 무엇이 어느 자리에 어떻게(더해진다, 바뀐다, 지워진다) 바뀌는지 적게 바뀌고, 그 줄의 예와 양식의 `phase-N.md` TODO 줄이 그에 맞게 바뀐다 (`plugins/plate/skills/plan/SKILL.md`)
- [ ] `docs/PRD.md` 13줄과 `docs/ARCHITECTURE.md` 25줄, 57~58줄 가운데 바뀐 plan과 어긋나는 줄이 바뀐다. 어긋나는 줄이 없으면 고치지 않고 기록에 그렇다고 적는다 (`docs/PRD.md`, `docs/ARCHITECTURE.md`)

**통과 조건**
- 완료 조건 2와 3이 참이다.
  - 확인: plan의 "조건" 절을 읽어 다른 phase의 확인을 옮겨 적는 줄과 #23의 세 줄이 하나씩 있다. 하나라도 없으면 실패
  - 확인: 6번을 읽어 통과 조건이 다른 phase를 가리키면 고친다는 줄이 있다
- 완료 조건 4가 참이다.
  - 확인: plan의 "TODO" 절, 양식의 `phase-N.md` TODO 줄, 6번을 하나씩 읽어 세 곳이 저마다 바뀜의 종류와 자리(또는 낱말 대어 보기)를 적는다
- phase 1이 이룬 완료 조건 1이 그대로 참이다.
  - 확인: `plugins/plate/skills/plan/SKILL.md`의 6번을 읽어 네 점검이 하나씩 따로 있다. 하나라도 없으면 실패
  - 확인: 같은 파일의 절대 규칙 3과 6번을 함께 읽어, 읽을 것의 명령은 돌려 보고 확인 명령은 돌려 보지 않는다는 것이 서로 어긋나지 않게 적혀 있다
- 완료 조건 5가 참이다.
  - 확인: `docs/PRD.md` 13줄, `docs/ARCHITECTURE.md` 25줄과 57~58줄을 하나씩 읽어 어긋나는 줄이 없다
- 테스트가 모두 통과한다.
  - 확인: `python3 -m unittest discover -s tests`가 `OK`
