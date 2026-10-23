# Phase 3: 판정 스크립트

**목표**: 판정 스크립트가 등급 묶음을 받아 세 규칙대로 자동 머지, 머지 요청, 닫기 가운데 하나를 낸다.

**테스트 먼저**: 예

**읽을 것**
- `plugins/plate/skills/review/SKILL.md`의 PR 모드 절 (phase 2가 적은 등급 묶음의 꼴)
- `tests/test_edit_guard.py` (이 저장소의 테스트 꼴)
- `plugins/plate/hooks/edit_guard.py` (표준 라이브러리만 쓰는 스크립트의 꼴)
- `docs/ADR.md`의 ADR-019 (Python 3 표준 라이브러리와 unittest)
- `docs/ARCHITECTURE.md` (디렉터리 구조)

**TODO**
- [x] 판정 스크립트의 테스트가 생긴다. 규칙마다의 경계(커버리지 79%와 80%, 신뢰성·보안·유지보수성의 A와 B, 보안의 B와 C, 모름, 빌드·린트·테스트의 실패)와, 커버리지가 "보지 않음"이고 다른 조건이 맞으면 자동 머지라는 경우를 본다 (`tests/`)
- [x] 판정 스크립트가 등급 묶음을 받아 자동 머지, 머지 요청, 닫기 가운데 하나를 낸다. 워크플로가 부를 수 있게 입력과 출력의 꼴이 스크립트에 적혀 있다 (`plugins/plate/` 아래)
- [x] 디렉터리 구조에 판정 스크립트와 그 테스트가 적힌다 (`docs/ARCHITECTURE.md`)

**통과 조건**
- 완료 조건 3이 참이다.
  - 확인: 완료 조건 3의 확인을 모두 돌린다
- 완료 조건 1이 그대로 참이다. 이 phase도 `docs/ARCHITECTURE.md`를 고친다.
  - 확인: 완료 조건 1의 확인을 모두 돌린다

## 한 일
- 판정 스크립트의 테스트가 생긴다: 등급 묶음 JSON을 stdin으로 주어 스크립트를 돌리고 stdout의 판정을 보는 테스트 14개를 썼다. 커버리지 79·79.9와 80·80.0, 신뢰성·보안·유지보수성의 A와 B, 보안의 B와 C·D·E, 모름(빌드·린트·테스트의 `"unmeasured"`, 세 등급의 `"unjudged"`, 커버리지의 `"unmeasured"`), 빌드·린트·테스트의 `"fail"`, 커버리지 `"skipped"`에서 자동 머지, `"none"`은 실패도 모름도 아님, 닫기가 모름보다 앞섬을 본다 (`tests/test_verdict.py`)
- 판정 스크립트가 등급 묶음을 받아 자동 머지, 머지 요청, 닫기 가운데 하나를 낸다: stdin의 등급 묶음 JSON을 읽어 stdout에 `close`, `merge`, `request` 가운데 한 줄을 내는 표준 라이브러리 스크립트를 썼다. 닫기(빌드·린트·테스트의 `"fail"`이나 보안 C 이하)를 먼저 보고, 자동 머지(빌드·린트·테스트가 `"pass"`나 `"none"`, 커버리지 80 이상이나 `"skipped"`, 세 등급이 모두 A)가 아니면 머지 요청이다. 입력과 출력의 꼴과 부르는 예를 docstring에 적었다 (`plugins/plate/ci/verdict.py`)
- 디렉터리 구조에 판정 스크립트와 그 테스트가 적힌다: `plugins/plate/` 아래에 `ci/verdict.py`를, `tests/` 아래에 `test_edit_guard.py`와 `test_verdict.py`를 적고, `tests/`의 설명을 "훅의 단위 테스트"에서 "단위 테스트"로 바꿨다 (`docs/ARCHITECTURE.md`)
- 테스트 먼저
  - 실패: `python3 -m unittest discover -s tests` → `FAIL: test_all_conditions_met_merges (test_verdict.MergeTest.test_all_conditions_met_merges)` 등 test_verdict의 27개가 `AssertionError: 종료 코드 2: ... can't open file '.../plugins/plate/ci/verdict.py': [Errno 2] No such file or directory`로 실패, `Ran 53 tests in 16.304s` / `FAILED (failures=27)`
  - 통과: `python3 -m unittest discover -s tests` → `Ran 53 tests in 15.921s` / `OK`

## 확인 결과
- 완료 조건 3이 참이다.
  - `python3 -m unittest discover -s tests` → `Ran 53 tests in 16.212s` / `OK`. 통과
  - `tests/test_verdict.py`를 읽음 → 커버리지 79·79.9(request)와 80·80.0(merge)은 `CoverageTest.test_boundary_79_and_80`, 세 등급의 A(merge)와 B(request)는 `GradeTest.test_a_merges_b_requests`, 보안 B(request)와 C·D·E(close)는 `GradeTest.test_security_b_requests_c_and_below_close`, 모름은 `UnknownTest` 두 테스트와 `CoverageTest.test_coverage_unmeasured_requests`, 빌드·린트·테스트의 실패는 `CloseTest.test_failed_command_closes`, 커버리지 "보지 않음"에서 자동 머지는 `MergeTest.test_coverage_skipped_does_not_block_merge`가 본다. 통과
  - `docs/ARCHITECTURE.md`의 디렉터리 구조를 읽음 → `plugins/plate/ci/verdict.py`(17줄)와 `tests/test_verdict.py`(33줄)가 있다. 통과
- 완료 조건 1이 그대로 참이다.
  - `grep -n "설치" plugins/plate/skills/plan/SKILL.md plugins/plate/skills/check/SKILL.md plugins/plate/skills/retro/SKILL.md plugins/plate/skills/review/SKILL.md` → 네 파일 모두 명령 절 정의의 설치 줄을 낸다(plan 29줄, check 29줄, retro 29줄, review 34줄). 통과
  - `grep -c "^- 설치: 없음$" docs/ARCHITECTURE.md` → `1`. 통과
  - plan의 3번(62줄: 설치, 빌드, 린트, 테스트 가운데 적히지 않은 것을 찾고 못 찾으면 5번에서 묻는다)과 5번(76줄: 3번에서 찾지 못한 명령(설치, 빌드, 린트, 테스트)도 묻는다)을 읽음. check 3번(48줄)과 retro 3번(60줄)은 "설치는 돌리지 않는다", review 2번(64줄)은 빌드·린트·테스트만 돌리고 낱말(34줄)에 "tasks 끝의 코드 평가는 설치를 돌리지 않는다"가 있다. 통과

## 계획과 달라진 점
- 없음

## 남은 것
- 없음

## 하네스에서 걸린 것
- 없음

## 확인 1

**통과 조건**
- 완료 조건 3이 참이다.
  - `python3 -m unittest discover -s tests` → `Ran 53 tests in 15.481s` / `OK`. 통과
  - `tests/test_verdict.py`를 읽음 → 커버리지 79·79.9는 request, 80·80.0은 merge(`CoverageTest.test_boundary_79_and_80`). 신뢰성·보안·유지보수성의 A는 merge, B는 request(`GradeTest.test_a_merges_b_requests`). 보안 B는 request, C·D·E는 close(`GradeTest.test_security_b_requests_c_and_below_close`). 모름은 빌드·린트·테스트의 `"unmeasured"`, 세 등급의 `"unjudged"`가 request(`UnknownTest` 두 테스트), 커버리지 `"unmeasured"`가 request(`CoverageTest.test_coverage_unmeasured_requests`). 빌드·린트·테스트의 `"fail"`은 close(`CloseTest.test_failed_command_closes`). 커버리지 `"skipped"`에서 다른 조건이 맞으면 merge(`MergeTest.test_coverage_skipped_does_not_block_merge`). 통과
  - `docs/ARCHITECTURE.md`의 디렉터리 구조를 읽음 → `plugins/plate/` 아래 `ci/verdict.py`(판정 스크립트)와 `tests/` 아래 `test_verdict.py`(판정 스크립트의 테스트)가 있다. 통과
- 완료 조건 1이 그대로 참이다.
  - `grep -n "설치" plugins/plate/skills/plan/SKILL.md plugins/plate/skills/check/SKILL.md plugins/plate/skills/retro/SKILL.md plugins/plate/skills/review/SKILL.md` → 네 파일 모두 명령 절 정의의 설치 줄을 낸다(plan 29줄, check 29줄, retro 29줄, review 34줄). 통과
  - `grep -c "^- 설치: 없음$" docs/ARCHITECTURE.md` → `1`. 통과
  - `plugins/plate/skills/plan/SKILL.md` 3번(62줄)과 5번(76줄)을 읽음 → 3번은 설치, 빌드, 린트, 테스트 가운데 적히지 않은 것을 찾고 못 찾으면 5번에서 묻는다, 5번은 찾지 못한 명령(설치, 빌드, 린트, 테스트)도 묻는다. check 3번(48줄)과 retro 3번(60줄)은 "설치는 돌리지 않는다". review 2번(64줄)은 빌드·린트·테스트만 돌리고 낱말(34줄)에 "tasks 끝의 코드 평가는 설치를 돌리지 않는다", 설치는 PR 모드 절차(168줄)에만 있다. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 53 tests in 15.481s` / `OK`. 통과

**테스트 먼저 기록**
- `phase-3.md`의 "한 일"의 테스트 먼저 → 실패 출력(`verdict.py`가 없어 test_verdict 27개 실패, `FAILED (failures=27)`)이 먼저, 통과 출력(`Ran 53 tests` / `OK`)이 뒤에 있다. 통과

**실패**
- 없음

**하네스에서 걸린 것**
- 이 확인 에이전트에 실린 check 스킬 본문은 명령 절을 빌드·린트·테스트 세 줄로 정의하고 "설치는 돌리지 않는다"가 없는 옛 본문이었고, 저장소의 `plugins/plate/skills/check/SKILL.md`는 phase 1이 고친 네 줄 정의다. 세션이 띄워질 때 실린 플러그인 본문이 이 tasks의 변경을 따라오지 않는다. 이 저장소의 설치가 "없음"이라 판정에는 걸리지 않았다

**판정**: 통과
