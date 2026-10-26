# Phase 1: 6번의 초안 전 점검

**목표**: plan 6번의 초안 전 점검에 #19의 네 점검, #20의 다른 phase 가리킴 점검, #24의 낱말 대어 보기가 더해지고 절대 규칙 3과 맞는다.

**테스트 먼저**: 아니오 — `.md`만 고친다

**읽을 것**
- `plugins/plate/skills/plan/SKILL.md` (18줄 절대 규칙 3, 90~102줄 6번)
- `gh issue view 19 -R werwer748/harness-plate` (#19의 본문: 네 점검과 근거)
- `gh issue view 20 -R werwer748/harness-plate` (#20의 본문)
- `gh issue view 24 -R werwer748/harness-plate` (#24의 본문)

**TODO**
- [ ] 6번의 초안 전 점검 목록에 #19의 네 점검이 저마다 한 줄로 더해진다: 저장소 밖 경로가 있는지, 읽을 것의 명령이 기대한 것을 내는지, 가져올 값이 가리킨 기록에 있는지, 푸시·권한·인증이 훅이나 권한 범위에 막히는지(막히면 사용자의 단계로 결정에 적는다) (`plugins/plate/skills/plan/SKILL.md`)
- [ ] 절대 규칙 3의 "확인 명령은 미리 돌려 보지 않고 적는다"가 읽을 것의 읽기 명령을 돌려 보는 점검과 어긋나지 않게 바뀐다 (`plugins/plate/skills/plan/SKILL.md`)
- [ ] 6번의 점검에 통과 조건이 다른 phase의 확인을 가리키기만 하면 그 확인 글을 옮겨 적도록 고친다는 줄이 더해진다 (`plugins/plate/skills/plan/SKILL.md`)
- [ ] 6번의 점검에 조건과 TODO가 다른 스킬의 낱말을 쓰면 그 스킬의 낱말 절과 대어 본다는 줄이 더해진다 (`plugins/plate/skills/plan/SKILL.md`)

**통과 조건**
- 완료 조건 1이 참이다.
  - 확인: `plugins/plate/skills/plan/SKILL.md`의 6번을 읽어 네 점검이 하나씩 따로 있다. 하나라도 없으면 실패
  - 확인: 같은 파일의 절대 규칙 3과 6번을 함께 읽어, 읽을 것의 명령은 돌려 보고 확인 명령은 돌려 보지 않는다는 것이 서로 어긋나지 않게 적혀 있다
- 완료 조건 2와 4 가운데 6번의 몫이 참이다.
  - 확인: 6번을 읽어 다른 phase를 가리키는 통과 조건을 고치는 줄과, 다른 스킬의 낱말을 낱말 절과 대어 보는 줄이 저마다 있다
- 테스트가 모두 통과한다.
  - 확인: `python3 -m unittest discover -s tests`가 `OK`
