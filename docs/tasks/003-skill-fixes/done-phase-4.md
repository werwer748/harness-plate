# Phase 4: cleanup의 맥락 문서 읽기와 결정의 범위

**목표**: 성능-2와 기존 작업 정합성-8이 고쳐진다.

**테스트 먼저**: 아니오 — 스킬 본문(`.md`)과 그 글을 지키는 테스트만 고친다

**읽을 것**
- `docs/cleanup/2026-10-29.md` (성능-2, 기존 작업 정합성-8의 근거와 고치는 방향, "하네스에서 걸린 것")
- `plugins/plate/skills/cleanup/SKILL.md`의 "2. 지난 보고서를 읽는다", "4. 2라운드", "2라운드에 맡기는 글" 절
- `tests/test_cleanup_skill.py` (맡기는 글과 2라운드 판정을 지키는 시험)

**TODO**
- [x] 2번에서 "맥락 문서를 모두 읽는다. 1라운드의 에이전트에게 넘길 자료다." 문단이 지워진다 (`plugins/plate/skills/cleanup/SKILL.md`)
- [x] 4번의 "반박이 있는 발견" 항목에, 반박의 근거가 든 맥락 문서를 그때 읽는다는 것과, "결정이 정한 것"은 맥락 문서(PRD의 범위 밖, ARCHITECTURE의 규칙, ADR, BACKLOG의 감수한 것)에 적힌 것과 지난 tasks 머리·task 머리의 결정 절(커밋으로 인용한 것)이고 닫힌 이슈의 글과 테스트만으로는 치지 않는다는 한 줄이 더해진다 (`plugins/plate/skills/cleanup/SKILL.md`)
- [x] "2라운드에 맡기는 글"의 규칙에, 맥락 문서나 지난 tasks의 결정 절이 이미 감수했으면 그 줄을 반박의 근거로 든다는 줄이 더해진다 (`plugins/plate/skills/cleanup/SKILL.md`)
- [x] 새 글을 지키는 시험이 더해지고, 지운 문단을 지키던 시험이 있으면 고쳐진다 (`tests/test_cleanup_skill.py`)

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

## 한 일
- 2번에서 "맥락 문서를 모두 읽는다. 1라운드의 에이전트에게 넘길 자료다." 문단이 지워진다: 그 문단을 지웠다 (`plugins/plate/skills/cleanup/SKILL.md`)
- 4번의 "반박이 있는 발견" 항목에 맥락 문서 읽기와 "결정이 정한 것"의 범위가 더해진다: 그 항목 아래에 "반박의 근거가 든 맥락 문서는 이 판정을 할 때 읽는다."와, 결정의 범위(맥락 문서의 PRD 범위 밖·ARCHITECTURE 규칙·ADR·BACKLOG 감수한 것, 지난 tasks 머리·task 머리의 결정 절(커밋으로 인용), 닫힌 이슈의 글과 테스트만으로는 치지 않음)를 하위 두 줄로 더했다 (`plugins/plate/skills/cleanup/SKILL.md`)
- "2라운드에 맡기는 글"의 규칙에 반박 근거 줄이 더해진다: "근거 없이 반박하지 않는다." 아래에, 맥락 문서나 지난 tasks 머리·task 머리의 결정 절이 이미 감수했으면 그 줄을 반박의 근거로 들고 닫힌 이슈의 글과 테스트만으로는 결정으로 들지 않는다는 줄을 더했다 (`plugins/plate/skills/cleanup/SKILL.md`)
- 새 글을 지키는 시험이 더해지고, 지운 문단을 지키던 시험이 있으면 고쳐진다: `CriteriaTest`에 `test_previous_reports_step_does_not_read_all_context_docs`, `test_rebuttal_reads_context_docs_and_scopes_decisions`를, `PromptTest`에 `test_round_two_prompt_cites_accepted_decisions_as_rebuttal`을 더했다. 지운 문단을 지키던 시험은 없었다 (`tests/test_cleanup_skill.py`)

## 확인 결과
- 2번이 맥락 문서를 모두 읽지 않는다(완료 조건 7).
  - `grep -n '맥락 문서를 모두 읽는다' plugins/plate/skills/cleanup/SKILL.md` → 출력 없음(종료 코드 1). 통과
- 결정의 범위가 4번과 2라운드 글에 있다(완료 조건 7).
  - `grep -n '결정 절' plugins/plate/skills/cleanup/SKILL.md` → 99행("4. 2라운드" 절, 90~103행)과 190행("2라운드에 맡기는 글" 절, 172~198행). 통과
  - `python3 -m unittest tests.test_cleanup_skill -v` → `Ran 28 tests`, `OK`. 통과
- 앞 phase의 동작이 그대로다(완료 조건 1~6).
  - `python3 -m unittest tests.test_skill_rules -v` → `Ran 80 tests`, `OK`. 통과
- 테스트 묶음이 통과한다.
  - `python3 -m unittest discover -s tests` → `Ran 236 tests`, 마지막 줄 `OK`. 통과

## 계획과 달라진 점
없음

## 남은 것
- 고친 본문대로 cleanup이 2번에서 맥락 문서를 읽지 않고 4번에서 필요한 것만 읽는지, 2라운드 에이전트가 새 줄대로 결정 절을 근거로 드는지는 돌려 보지 않았다. cleanup은 에이전트 열두 개를 띄우고 묻는 스킬이라 task 머리가 돌리지 않기로 정했다(완료 조건 7의 "돌리지 않음"). 시험은 본문의 글이 있는지만 본다

## 하네스에서 걸린 것
없음

## 확인 1

**통과 조건**
- 2번이 맥락 문서를 모두 읽지 않는다(완료 조건 7).
  - `grep -n '맥락 문서를 모두 읽는다' plugins/plate/skills/cleanup/SKILL.md` → 출력 없음(종료 코드 1). 통과
- 결정의 범위가 4번과 2라운드 글에 있다(완료 조건 7).
  - `grep -n '결정 절' plugins/plate/skills/cleanup/SKILL.md` → 99행("4. 2라운드" 절, 90~103행)과 190행("2라운드에 맡기는 글" 절, 172~198행). 통과
  - `python3 -m unittest tests.test_cleanup_skill -v` → `Ran 28 tests`, `OK`. 통과
- 앞 phase의 동작이 그대로다(완료 조건 1~6).
  - `python3 -m unittest tests.test_skill_rules -v` → `Ran 80 tests`, `OK`. 통과
- 테스트 묶음이 통과한다.
  - `python3 -m unittest discover -s tests` → `Ran 236 tests`, 마지막 줄 `OK`. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 236 tests`, `OK`. 통과

**남은 것**
- 고친 본문대로 cleanup이 2번에서 맥락 문서를 읽지 않고 4번에서 필요한 것만 읽는지, 2라운드 에이전트가 결정 절을 근거로 드는지 돌려 보지 않았다 → 통과 조건이 보는 동작(완료 조건 7)에 걸리지만, task 머리 완료 조건 7의 `- 돌리지 않음: cleanup은 에이전트 열두 개를 띄우고 묻는 스킬이라 헤드리스로 돌리지 않는다`가 돌리지 않기로 정한 동작의 돌려 보지 않은 위험이다. 하네스에서 걸린 것

**실패**
- 없음

**하네스에서 걸린 것**
- 남은 것: 고친 cleanup 본문의 동작(2번에서 맥락 문서를 읽지 않음, 4번에서 필요한 것만 읽음, 2라운드가 결정 절을 반박 근거로 듦)은 돌려 보지 않았다. 완료 조건 7의 `돌리지 않음` 줄이 정한 대로이며, 시험은 본문의 글이 있는지만 본다

**판정**: 통과
