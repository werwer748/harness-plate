# Phase 2: phase가 부작용과 한계를 남은 것에 적는다

**목표**: phase의 기록 규칙이 수행이 아는 부작용과 한계를 "남은 것"에 적게 하고, ARCHITECTURE가 바뀐 두 스킬과 맞는다.

**테스트 먼저**: 아니오 — `.md`만 고친다

**읽을 것**
- `plugins/plate/skills/phase/SKILL.md`의 4번, 기록의 양식, 적는 규칙
- `git show c2a983c^:docs/tasks/003-push-guard/done-phase-2.md` (부작용을 "한 일"에만 적고 "남은 것"을 "없음"으로 둔 곳)
- `docs/ARCHITECTURE.md`

**TODO**
- [ ] 기록 양식의 "남은 것"을 `{끝내지 못한 TODO나 막힌 곳, 수행이 아는 부작용과 한계, 그 까닭}`으로 고친다 (`plugins/plate/skills/phase/SKILL.md`)
- [ ] 적는 규칙에 생긴다. 고친 것이 다른 꼴이나 다른 곳을 잘못 다룬다는 것처럼 수행이 아는 부작용과 한계는 "한 일"에 적었어도 "남은 것"에 적는다. 상태가 "끝남"이어도 그렇다 (`plugins/plate/skills/phase/SKILL.md`)
- [ ] `docs/ARCHITECTURE.md`에서 회고, phase 기록, `FRICTION.md`를 적은 줄이 바뀐 두 스킬과 어긋나면 맞춘다 (`docs/ARCHITECTURE.md`)

**통과 조건**
- 완료 조건 1의 둘째 확인이 참이다.
  - 확인: phase의 적는 규칙과 기록 양식의 "남은 것"을 읽어, 부작용과 한계를 "남은 것"에 적는 규칙이 둘 다에 있다
- 완료 조건 3이 참이다.
  - 확인: `grep -n '회고\|남은 것\|FRICTION' docs/ARCHITECTURE.md`가 낸 줄을 하나씩 읽어 어긋나는 줄이 없다
- phase 1이 이룬 완료 조건 1의 첫째 확인과 완료 조건 2가 그대로 참이다.
  - 확인: phase 1의 통과 조건 확인을 다시 돌린다
- 테스트가 모두 통과한다.
  - 확인: `python3 -m unittest discover -s tests`가 `OK`
