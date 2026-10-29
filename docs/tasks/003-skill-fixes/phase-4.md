# Phase 4: cleanup의 맥락 문서 읽기와 결정의 범위

**목표**: 성능-2와 기존 작업 정합성-8이 고쳐진다.

**테스트 먼저**: 아니오 — 스킬 본문(`.md`)과 그 글을 지키는 테스트만 고친다

**읽을 것**
- `docs/cleanup/2026-10-29.md` (성능-2, 기존 작업 정합성-8의 근거와 고치는 방향, "하네스에서 걸린 것")
- `plugins/plate/skills/cleanup/SKILL.md`의 "2. 지난 보고서를 읽는다", "4. 2라운드", "2라운드에 맡기는 글" 절
- `tests/test_cleanup_skill.py` (맡기는 글과 2라운드 판정을 지키는 시험)

**TODO**
- [ ] 2번에서 "맥락 문서를 모두 읽는다. 1라운드의 에이전트에게 넘길 자료다." 문단이 지워진다 (`plugins/plate/skills/cleanup/SKILL.md`)
- [ ] 4번의 "반박이 있는 발견" 항목에, 반박의 근거가 든 맥락 문서를 그때 읽는다는 것과, "결정이 정한 것"은 맥락 문서(PRD의 범위 밖, ARCHITECTURE의 규칙, ADR, BACKLOG의 감수한 것)에 적힌 것과 지난 tasks 머리·task 머리의 결정 절(커밋으로 인용한 것)이고 닫힌 이슈의 글과 테스트만으로는 치지 않는다는 한 줄이 더해진다 (`plugins/plate/skills/cleanup/SKILL.md`)
- [ ] "2라운드에 맡기는 글"의 규칙에, 맥락 문서나 지난 tasks의 결정 절이 이미 감수했으면 그 줄을 반박의 근거로 든다는 줄이 더해진다 (`plugins/plate/skills/cleanup/SKILL.md`)
- [ ] 새 글을 지키는 시험이 더해지고, 지운 문단을 지키던 시험이 있으면 고쳐진다 (`tests/test_cleanup_skill.py`)

**통과 조건**
- 2번이 맥락 문서를 모두 읽지 않는다(완료 조건 7).
  - 확인: `grep -n '맥락 문서를 모두 읽는다' plugins/plate/skills/cleanup/SKILL.md` → 아무것도 나오지 않음
- 결정의 범위가 4번과 2라운드 글에 있다(완료 조건 7).
  - 확인: `grep -n '결정 절' plugins/plate/skills/cleanup/SKILL.md` → "4. 2라운드" 절과 "2라운드에 맡기는 글" 절에 저마다 한 줄 이상
  - 확인: `python3 -m unittest tests.test_cleanup_skill -v` → `OK`
- 앞 phase의 동작이 그대로다(완료 조건 1~6).
  - 확인: `python3 -m unittest tests.test_skill_rules -v` → `OK`
- 테스트 묶음이 통과한다.
  - 확인: `python3 -m unittest discover -s tests` → 마지막 줄이 `OK`
