# Phase 3: phase의 실패 출력 얻기와 review의 커버리지

**목표**: 신뢰성-2와 성능-4가 고쳐진다.

**테스트 먼저**: 아니오 — 스킬 본문(`.md`)만 고친다

**읽을 것**
- `docs/cleanup/2026-10-29.md` (신뢰성-2, 성능-4의 근거와 고치는 방향)
- `plugins/plate/skills/phase/SKILL.md`의 "2. TODO를 차례로 끝낸다" 절 (실패 출력 얻기 문단)
- `plugins/plate/skills/review/SKILL.md`의 "2. 잰다" 절
- `tests/test_skill_rules.py` (phase·review 본문을 지키는 시험)

**TODO**
- [ ] 실패 출력 얻기 문단에, phase 커밋의 부모 커밋에 없는 구현 파일(그 phase가 새로 만든 파일)은 잠깐 다른 자리로 옮겨 테스트를 돌리고 되살리는 갈래와 그 명령 예가 더해진다. 부모에 있는 파일의 `git checkout <커밋>^ -- <구현 파일>` 갈래는 그대로다 (`plugins/plate/skills/phase/SKILL.md`)
- [ ] "2. 잰다"의 커버리지 항목에, 커버리지 도구가 테스트 명령을 감쌀 수 있으면 1번의 테스트를 그 도구로 한 번만 돌려 테스트 결과와 커버리지에 함께 쓴다는 것이 더해진다 (`plugins/plate/skills/review/SKILL.md`)
- [ ] `tests/`에서 고친 두 문단의 옛 글을 찾아(`git grep -n -F 'checkout <커밋>^' -- tests/`, `git grep -n -F '커버리지 도구로 테스트를' -- tests/`) 걸리는 시험을 새 글을 지키게 고친다 (`tests/test_skill_rules.py`)

**통과 조건**
- phase 본문이 새 파일의 갈래를 적고 명령 예가 돈다(완료 조건 5).
  - 확인: `grep -n '부모 커밋에 없' plugins/plate/skills/phase/SKILL.md` → "2. TODO를 차례로 끝낸다" 절에 한 줄 이상
  - 확인: `mktemp -d` 시험 레포에 `tests/test_a.py`와, phase 커밋(`001-a: phase 1`)이 새로 만든 `new.py`와 고친 `old.py`를 둔다. 본문의 명령 예대로 `new.py`는 옮겼다 되살리고 `old.py`는 부모 것으로 되돌렸다 되살린 뒤, 그 사이에 테스트가 실패하고 끝에 `git status --porcelain`이 비어 있다
- review 본문이 한 번 돌림을 적는다(완료 조건 6).
  - 확인: `grep -n '한 번' plugins/plate/skills/review/SKILL.md` → "2. 잰다" 절의 커버리지 항목에 한 줄 이상
- 앞 phase의 동작이 그대로다(완료 조건 1~4).
  - 확인: `python3 -m unittest tests.test_skill_rules.RunRulesTest.test_no_result_relaunch_limit tests.test_skill_rules.RunRulesTest.test_stop_line_grep_runs_on_fake_runlog -v` → `OK`
- 테스트 묶음이 통과한다.
  - 확인: `python3 -m unittest discover -s tests` → 마지막 줄이 `OK`
