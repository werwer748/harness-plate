# Phase 2: 스킬 description을 400자 이하로 줄인다

**목표**: 성능-7이 고쳐져, 스킬 description 열 개가 저마다 400자 이하이고 테스트가 그 상한을 지킨다.

**테스트 먼저**: 아니오 — 스킬 앞머리(`.md`)와 그 글을 지키는 테스트만 고친다

**읽을 것**
- `docs/cleanup/2026-10-29.md` (성능-7의 근거, 고치는 방향, 2라운드 판정)
- `plugins/plate/skills/*/SKILL.md`의 앞머리 열 개
- `tests/test_skill_rules.py`의 `DescriptionTest`와 eval 시험의 `front_matter("eval")` 줄
- `docs/ARCHITECTURE.md`의 디렉터리 구조 절의 `test_skill_rules.py` 줄

**TODO**
- [x] 스킬 열 개의 description이 저마다 400자 이하로, 무엇을 내는지·언제 쓰는지(부르는 말)·쓰지 않을 때만 남기게 바뀐다. 끝은 `쓰지 않는다.`이고, run은 `"실행해줘"`, `"phase 진행하자"`, `"이어서 하자"`, `"끝까지 돌려줘"`, `계획이 없는 요청에는 쓰지 않는다`를, eval은 `"eval에만"`을 남긴다 (`plugins/plate/skills/*/SKILL.md`)
- [x] `DescriptionTest`에 `test_description_at_most_400_chars`가 더해지고 클래스 docstring이 400자 상한을 적는다. 1024자 시험은 남긴다 (`tests/test_skill_rules.py`)
- [x] 디렉터리 구조 절의 `test_skill_rules.py` 줄의 description 한도가 `description 400자`로 바뀐다 (`docs/ARCHITECTURE.md`)

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

## 한 일
- 스킬 열 개의 description을 400자 이하로 줄임: 절차의 복사를 빼고 무엇을 내는지·언제 쓰는지(부르는 말)·쓰지 않을 때만 남겼다. 길이는 check 184, cleanup 321, context 216, eval 271, phase 207, plan 245, retro 280, review 308, run 306, setup 249자(전에는 합 약 5,400자, run 994자). 모두 `쓰지 않는다.`로 끝나고, run은 부르는 말 넷과 `계획이 없는 요청에는 쓰지 않는다`를, eval은 `"eval에만"`을 남겼다 (`plugins/plate/skills/*/SKILL.md`의 3번째 줄만)
- `DescriptionTest`에 `test_description_at_most_400_chars`를 더하고 클래스 docstring이 400자 상한과 그 까닭을 적게 바꿨다. 1024자 시험은 남겼다 (`tests/test_skill_rules.py`)
- 디렉터리 구조 절의 `test_skill_rules.py` 줄의 한도를 `Agent Skills 한도(description 1024자, name 64자)와 plate의 description 400자`로 바꿨다 (`docs/ARCHITECTURE.md`)

## 확인 결과
- description이 400자 이하이고 지키는 글이 남는다(완료 조건 5).
  - `python3 -m unittest tests.test_skill_rules.DescriptionTest -v` → `test_description_at_most_400_chars ... ok`를 포함해 6개, `OK`. 통과
  - `python3 -m unittest tests.test_skill_rules.EvalRulesTest -v` → `Ran 6 tests`, `OK`. 통과
  - `claude plugin validate plugins/plate` → `✔ Validation passed`. 통과
- ARCHITECTURE가 맞다(완료 조건 6의 뒤 줄).
  - `grep -n 'description 400자' docs/ARCHITECTURE.md` → 40번 줄 한 줄(디렉터리 구조 절은 9~43번 줄). 통과
- 앞 phase와 앞 task들의 시험이 그대로다(완료 조건 1~4, 7).
  - `python3 -m unittest tests.test_cleanup_skill tests.test_manifests tests.test_verdict.BundleShapeTest -v` → `Ran 34 tests`, `OK`. 통과
- 테스트 묶음이 통과한다.
  - `python3 -m unittest discover -s tests` → `Ran 239 tests`, 마지막 줄 `OK`. 통과

## 계획과 달라진 점
- TODO는 ARCHITECTURE 줄의 한도가 `description 400자`로 "바뀐다"고 적었으나, 1024자 시험이 남아 있으니 1024자를 지우지 않고 `와 plate의 description 400자`를 더했다. 줄이 테스트가 보는 것과 맞게 하려는 까닭이다

## 남은 것
- description이 짧아져 모델이 스킬을 고르는 판단이 바뀔 수 있다. task 머리의 `돌리지 않음` 줄대로 여러 요청 글로 골라지는지 보는 시험은 돌리지 않았다
- 줄인 description에서 빠진 세부(예: plan의 브랜치 물음 갈래, run의 기본 브랜치 되돌림 물음, review PR 모드의 네 범주)는 본문에만 있다. 본문 절차는 바꾸지 않았다

## 하네스에서 걸린 것
- 없음

## 확인 1

**통과 조건**
- description이 400자 이하이고 지키는 글이 남는다(완료 조건 5).
  - `python3 -m unittest tests.test_skill_rules.DescriptionTest -v` → `test_description_at_most_400_chars ... ok`를 포함해 `Ran 6 tests`, `OK`. 통과
  - `python3 -m unittest tests.test_skill_rules.EvalRulesTest -v` → `Ran 6 tests`, `OK`. 통과
  - `claude plugin validate plugins/plate` → `✔ Validation passed`. 통과
- ARCHITECTURE가 맞다(완료 조건 6의 뒤 줄).
  - `grep -n 'description 400자' docs/ARCHITECTURE.md` → 40번 줄 한 줄. `## 디렉터리 구조`(9번 줄)와 `## 패턴과 규칙`(44번 줄) 사이라 디렉터리 구조 절 안이다. 통과
- 앞 phase와 앞 task들의 시험이 그대로다(완료 조건 1~4, 7).
  - `python3 -m unittest tests.test_cleanup_skill tests.test_manifests tests.test_verdict.BundleShapeTest -v` → `Ran 34 tests`, `OK`. 통과
- 테스트 묶음이 통과한다.
  - `python3 -m unittest discover -s tests` → `Ran 239 tests`, 마지막 줄 `OK`. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 239 tests`, `OK`. 통과

**남은 것**
- description이 짧아져 모델이 스킬을 고르는 판단이 바뀔 수 있고, 골라지는지 보는 시험은 돌리지 않았다 → 돌려 보지 않은 위험이나, task 머리 완료 조건 5의 `- 돌리지 않음: description이 바뀌면 모델이 스킬을 고르는 판단이 바뀔 수 있는데, 여러 요청 글로 스킬이 골라지는지 보는 시험은 대화형 세션이 있어야 해 돌리지 않는다` 줄이 돌리지 않기로 정한 동작이다. 하네스에서 걸린 것

**실패**
- 없음

**하네스에서 걸린 것**
- 남은 것: description이 짧아져 모델이 스킬을 고르는 판단이 바뀔 수 있다. 완료 조건 5의 `돌리지 않음` 줄대로 골라지는지 보는 시험은 돌리지 않았다

**판정**: 통과
