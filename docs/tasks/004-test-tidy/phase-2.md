# Phase 2: 스킬 description을 400자 이하로 줄인다

**목표**: 성능-7이 고쳐져, 스킬 description 열 개가 저마다 400자 이하이고 테스트가 그 상한을 지킨다.

**테스트 먼저**: 아니오 — 스킬 앞머리(`.md`)와 그 글을 지키는 테스트만 고친다

**읽을 것**
- `docs/cleanup/2026-10-29.md` (성능-7의 근거, 고치는 방향, 2라운드 판정)
- `plugins/plate/skills/*/SKILL.md`의 앞머리 열 개
- `tests/test_skill_rules.py`의 `DescriptionTest`와 eval 시험의 `front_matter("eval")` 줄
- `docs/ARCHITECTURE.md`의 디렉터리 구조 절의 `test_skill_rules.py` 줄

**TODO**
- [ ] 스킬 열 개의 description이 저마다 400자 이하로, 무엇을 내는지·언제 쓰는지(부르는 말)·쓰지 않을 때만 남기게 바뀐다. 끝은 `쓰지 않는다.`이고, run은 `"실행해줘"`, `"phase 진행하자"`, `"이어서 하자"`, `"끝까지 돌려줘"`, `계획이 없는 요청에는 쓰지 않는다`를, eval은 `"eval에만"`을 남긴다 (`plugins/plate/skills/*/SKILL.md`)
- [ ] `DescriptionTest`에 `test_description_at_most_400_chars`가 더해지고 클래스 docstring이 400자 상한을 적는다. 1024자 시험은 남긴다 (`tests/test_skill_rules.py`)
- [ ] 디렉터리 구조 절의 `test_skill_rules.py` 줄의 description 한도가 `description 400자`로 바뀐다 (`docs/ARCHITECTURE.md`)

**통과 조건**
- description이 400자 이하이고 지키는 글이 남는다(완료 조건 5).
  - 확인: `python3 -m unittest tests.test_skill_rules.DescriptionTest -v` → `test_description_at_most_400_chars`가 있고 `OK`
  - 확인: `python3 -m unittest tests.test_skill_rules.EvalRulesTest -v` → `OK`
  - 확인: `claude plugin validate plugins/plate` → `Validation passed`
- ARCHITECTURE가 맞다(완료 조건 6의 뒤 줄).
  - 확인: `grep -n 'description 400자' docs/ARCHITECTURE.md` → 디렉터리 구조 절에 한 줄
- 앞 phase와 앞 task들의 시험이 그대로다(완료 조건 1~4, 7).
  - 확인: `python3 -m unittest tests.test_cleanup_skill tests.test_manifests tests.test_verdict.BundleShapeTest -v` → `OK`
- 테스트 묶음이 통과한다.
  - 확인: `python3 -m unittest discover -s tests` → 마지막 줄이 `OK`
