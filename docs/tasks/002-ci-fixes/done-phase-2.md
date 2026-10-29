# Phase 2: 등급 묶음의 꼴 세 곳을 견주는 테스트

**목표**: 유지보수성-1이 고쳐져, 등급 묶음의 꼴이 세 곳에서 같은지 테스트가 본다.

**테스트 먼저**: 아니오 — 테스트만 더하고 코드의 동작을 바꾸지 않는다

**읽을 것**
- `docs/cleanup/2026-10-29.md` (유지보수성-1의 근거와 고치는 방향)
- `plugins/plate/skills/setup/SKILL.md`의 CI 워크플로 양식의 `--json-schema` 줄
- `plugins/plate/skills/review/SKILL.md`의 PR 모드 절의 등급 묶음 표
- `plugins/plate/ci/verdict.py` (`COMMANDS`, `GRADES`, docstring의 값)
- `tests/test_verdict.py`

**TODO**
- [x] `BundleShapeTest`가 더해진다: setup 양식에서 `--json-schema`의 JSON을 뽑아 키와 열거를 얻고, review 표의 키와 값, `verdict.py`의 `COMMANDS`·`GRADES`와 견준다. 셋 가운데 하나라도 다르면 실패한다 (`tests/test_verdict.py`)
- [x] `docs/ARCHITECTURE.md`의 디렉터리 구조의 `test_verdict.py` 줄에 등급 묶음의 꼴을 견준다는 것이 더해진다 (`docs/ARCHITECTURE.md`)

**통과 조건**
- 지금 세 곳이 같아 테스트가 통과한다(완료 조건 2).
  - 확인: `python3 -m unittest tests.test_verdict.BundleShapeTest -v` → `OK`
- 한 곳이 어긋나면 실패한다(완료 조건 2).
  - 확인: 작업 트리를 `cp -R`로 `mktemp -d` 사본에 옮기고, 사본의 `plugins/plate/skills/setup/SKILL.md`에서 `"maintainability":{"type":"string","enum":["A","B","C","D","E","unjudged"]}`를 `"maintainability":{"type":"string","enum":["A","B","C","D","E"]}`로 바꿔 사본에서 `python3 -m unittest tests.test_verdict.BundleShapeTest` → 실패(`FAILED`)
- 앞 phase의 동작이 그대로다(완료 조건 1).
  - 확인: `printf 'not json' | python3 plugins/plate/ci/verdict.py; echo "exit=$?"` → `request`, `exit=0`
- 테스트 묶음이 통과한다.
  - 확인: `python3 -m unittest discover -s tests` → 마지막 줄이 `OK`

## 한 일
- `BundleShapeTest`가 더해진다: `tests/test_verdict.py`에 도우미 셋(`setup_shape`, `review_shape`, `verdict_module`)과 `BundleShapeTest`의 테스트 셋을 더했다. `setup_shape`는 setup 본문에서 `--json-schema '…'`를 정규식으로 하나만 뽑아 JSON으로 읽고, `required`가 키 전부인지와 `additionalProperties`가 false인지 본 뒤 {키: 값의 집합}(수 값은 `number`)을 낸다. `review_shape`는 review 본문의 `## PR 모드` 절 아래 `| 키 | 값 | 뜻 |` 표를 읽어 같은 꼴을 낸다(`"A"`~`"E"`는 A부터 E로 펴고 "0~100의 수"는 `number`). `verdict_module`은 `importlib`로 `verdict.py`를 불러 `COMMANDS`·`GRADES`를 얻는다. 테스트는 setup과 review의 꼴이 같은지, 두 곳의 키가 `COMMANDS`∪`GRADES`∪{coverage} 일곱과 같은지, 두 곳의 값이 `COMMANDS` 키마다 {pass, fail, none, unmeasured}, `GRADES` 키마다 {A~E, unjudged}, coverage가 {number, skipped, unmeasured}인지 본다 (`tests/test_verdict.py`)
- `docs/ARCHITECTURE.md`의 디렉터리 구조의 `test_verdict.py` 줄에 등급 묶음의 꼴을 견준다는 것이 더해진다: 그 줄을 "판정 스크립트의 테스트와, 등급 묶음의 꼴(키 일곱 개와 값의 열거)이 setup 양식의 `--json-schema`, review의 PR 모드 절의 표, 판정 스크립트의 `COMMANDS`·`GRADES`에서 같은지 견주는 테스트"로 고쳤다 (`docs/ARCHITECTURE.md`)

## 확인 결과
- 지금 세 곳이 같아 테스트가 통과한다(완료 조건 2).
  - `python3 -m unittest tests.test_verdict.BundleShapeTest -v` → 테스트 셋 모두 `ok`, `Ran 3 tests`, `OK`. 통과
- 한 곳이 어긋나면 실패한다(완료 조건 2).
  - `T=$(mktemp -d); cp -R /Users/hugo/Desktop/harness-plate/. "$T"/`, 사본의 `plugins/plate/skills/setup/SKILL.md`에서 그 글(한 번 나옴을 assert로 봄)을 `"maintainability":{"type":"string","enum":["A","B","C","D","E"]}`로 python으로 바꾸고 사본에서 `python3 -m unittest tests.test_verdict.BundleShapeTest` → `FAILED (failures=2)`. 통과
- 앞 phase의 동작이 그대로다(완료 조건 1).
  - `printf 'not json' | python3 plugins/plate/ci/verdict.py; echo "exit=$?"` → `request`, `exit=0`. 통과
- 테스트 묶음이 통과한다.
  - `python3 -m unittest discover -s tests` → `Ran 229 tests in 19.517s`, 마지막 줄 `OK`. 통과

## 계획과 달라진 점
- 없음

## 남은 것
- 값의 열거(pass/fail/none/unmeasured, A~E/unjudged, number/skipped/unmeasured)는 `verdict.py`에 상수로 없어 테스트 안의 상수(`COMMAND_VALUES`, `GRADE_VALUES`, `COVERAGE_VALUES`)와 견준다. setup과 review는 서로, 그리고 이 상수와 견주므로 한 곳만 바뀌면 실패하지만, `verdict.py`의 docstring의 값과 `verdict()` 안의 비교 글자(`"pass"`, `"C"` 같은 것)는 견주지 않는다.
- `review_shape`는 표의 값 칸을 백틱 속 큰따옴표 글자와 `"A"`~`"E"`, "0~100의 수"라는 글로 읽는다. 표의 적는 꼴이 바뀌면(예: 범위를 다른 글로 적음) 꼴이 같아도 테스트가 실패할 수 있다.

## 하네스에서 걸린 것
- 없음

## 확인 1

**통과 조건**
- 지금 세 곳이 같아 테스트가 통과한다(완료 조건 2).
  - `python3 -m unittest tests.test_verdict.BundleShapeTest -v` → 테스트 셋 모두 `ok`, `Ran 3 tests`, `OK`. 통과
- 한 곳이 어긋나면 실패한다(완료 조건 2).
  - `T=$(mktemp -d); cp -R . "$T"/`, 사본의 `plugins/plate/skills/setup/SKILL.md`에서 그 글(1번 나옴)을 `"maintainability":{"type":"string","enum":["A","B","C","D","E"]}`로 python으로 바꾸고 `(cd "$T" && python3 -m unittest tests.test_verdict.BundleShapeTest)` → `FAILED (failures=2)`. 통과
- 앞 phase의 동작이 그대로다(완료 조건 1).
  - `printf 'not json' | python3 plugins/plate/ci/verdict.py; echo "exit=$?"` → `request`, `exit=0`. 통과
- 테스트 묶음이 통과한다.
  - `python3 -m unittest discover -s tests` → `Ran 229 tests`, 마지막 줄 `OK`. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 229 tests`, `OK`. 통과

**남은 것**
- `verdict.py`의 docstring의 값과 `verdict()` 안의 비교 글자는 견주지 않는다 → 통과 조건(완료 조건 2)이 보는 것은 setup 양식, review 표, `COMMANDS`·`GRADES`(키만 담은 튜플)의 꼴이고, 셋은 견준다. docstring과 비교 글자는 통과 조건이 보는 동작에 걸리지 않는다. 하네스에서 걸린 것
- review 표의 적는 꼴이 바뀌면 꼴이 같아도 테스트가 실패할 수 있다 → 지금 꼴에서의 통과와 어긋남에서의 실패라는 통과 조건의 동작에 걸리지 않는다(틀린 통과가 아니라 지나친 실패의 위험). 하네스에서 걸린 것

**실패**
- 없음

**하네스에서 걸린 것**
- 남은 것: 값의 열거는 `verdict.py`에 상수로 없어 테스트 안의 상수와 견주고, `verdict.py`의 docstring의 값과 `verdict()` 안의 비교 글자는 견주지 않는다.
- 남은 것: `review_shape`는 표의 값 칸을 백틱 속 큰따옴표 글자와 `"A"`~`"E"`, "0~100의 수"라는 글로 읽어, 표의 적는 꼴이 바뀌면 꼴이 같아도 테스트가 실패할 수 있다.

**판정**: 통과
