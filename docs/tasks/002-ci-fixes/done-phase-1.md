# Phase 1: 판정 스크립트가 깨진 입력에서 머지 요청을 낸다

**목표**: 신뢰성-7이 고쳐져, 판정 스크립트가 읽지 못한 입력에서 `request`를 내고 0으로 끝난다.

**테스트 먼저**: 예

**읽을 것**
- `docs/cleanup/2026-10-29.md` (신뢰성-7의 근거와 고치는 방향)
- `plugins/plate/ci/verdict.py` (docstring, `verdict`, `main`)
- `plugins/plate/skills/setup/SKILL.md`의 CI 워크플로 양식의 `verdict` 잡 (판정 스크립트를 부르는 줄)
- `docs/ARCHITECTURE.md`의 "패턴과 규칙" 절의 PR의 CI 문단 (판정은 셋이라는 줄)
- `tests/test_verdict.py`

**TODO**
- [x] `main`이 stdin을 JSON으로 읽지 못하거나 객체가 아니면, 또는 `--changed-files`의 파일을 읽지 못하면 `request`를 내고 0으로 끝나게 바뀐다 (`plugins/plate/ci/verdict.py`)
- [x] docstring의 출력 설명에 읽지 못하면 `request`라는 것이 더해진다 (`plugins/plate/ci/verdict.py`)
- [x] 깨진 JSON, 객체가 아닌 JSON, 빈 입력, 읽지 못하는 목록 파일의 시험이 더해진다 (`tests/test_verdict.py`)
- [x] PR의 CI 문단의 판정 셋 줄에, 판정 스크립트가 입력을 읽지 못하면 머지 요청이라는 것이 더해진다 (`docs/ARCHITECTURE.md`)

**통과 조건**
- 읽지 못한 입력에서 `request`와 0이다(완료 조건 1).
  - 확인: `printf 'not json' | python3 plugins/plate/ci/verdict.py; echo "exit=$?"` → `request`, `exit=0`
  - 확인: `printf '[]' | python3 plugins/plate/ci/verdict.py; echo "exit=$?"` → `request`, `exit=0`
  - 확인: `printf '{"build":"pass","lint":"none","test":"pass","coverage":"skipped","reliability":"A","security":"A","maintainability":"A"}' | python3 plugins/plate/ci/verdict.py --changed-files /nonexistent; echo "exit=$?"` → `request`, `exit=0`
- 문서가 바뀐 동작을 적는다.
  - 확인: `grep -n '읽지 못하면' plugins/plate/ci/verdict.py docs/ARCHITECTURE.md` → 두 파일에 저마다 한 줄 이상
- 테스트 묶음이 통과한다.
  - 확인: `python3 -m unittest discover -s tests` → 마지막 줄이 `OK`

## 한 일
- `main`이 stdin을 JSON으로 읽지 못하거나 객체가 아니면, 또는 `--changed-files`의 파일을 읽지 못하면 `request`를 내고 0으로 끝나게 바뀐다: `main`이 새 함수 `decide`의 결과를 찍는다. `decide`는 `json.load`의 `ValueError`(깨진 JSON, 빈 입력, 디코딩 오류)와 객체가 아닌 값에서 `request`를 내고, `--changed-files`가 있으면 판정과 상관없이 파일을 먼저 읽어 `OSError`·`ValueError`에서 `request`를 낸다 (`plugins/plate/ci/verdict.py`)
- docstring의 출력 설명에 읽지 못하면 `request`라는 것이 더해진다: 출력 절 끝에 두 줄을 더했다 (`plugins/plate/ci/verdict.py`)
- 깨진 JSON, 객체가 아닌 JSON, 빈 입력, 읽지 못하는 목록 파일의 시험이 더해진다: `run_raw` 도우미와 `UnreadableInputTest`(네 시험, 객체가 아닌 JSON은 `[]`, `null`, `3`, `"merge"`의 subTest)를 더했다 (`tests/test_verdict.py`)
- PR의 CI 문단의 판정 셋 줄에, 판정 스크립트가 입력을 읽지 못하면 머지 요청이라는 것이 더해진다: "그 밖(모름이 있을 때도 든다)은 머지 요청이다." 뒤에 한 문장을 더했다 (`docs/ARCHITECTURE.md`)
- 테스트 먼저
  - 실패: `python3 -m unittest tests.test_verdict.UnreadableInputTest` → `FAIL: test_broken_json_requests`, `FAIL: test_empty_input_requests`, `FAIL: test_non_object_json_requests (stdin='[]')`(`null`, `3`, `"merge"`도), `FAIL: test_unreadable_changed_files_requests` (`AssertionError: Tuples differ: (1, '') != (0, 'request\n')`), `FAILED (failures=7)`
  - 통과: `python3 -m unittest tests.test_verdict -v` → `Ran 21 tests in 1.277s`, `OK`

## 확인 결과
- 읽지 못한 입력에서 `request`와 0이다(완료 조건 1).
  - `printf 'not json' | python3 plugins/plate/ci/verdict.py; echo "exit=$?"` → `request`, `exit=0`. 통과
  - `printf '[]' | python3 plugins/plate/ci/verdict.py; echo "exit=$?"` → `request`, `exit=0`. 통과
  - `printf '{"build":"pass",…,"maintainability":"A"}' | python3 plugins/plate/ci/verdict.py --changed-files /nonexistent; echo "exit=$?"`(통과 조건의 묶음 그대로) → `request`, `exit=0`. 통과
- 문서가 바뀐 동작을 적는다.
  - `grep -n '읽지 못하면' plugins/plate/ci/verdict.py docs/ARCHITECTURE.md` → `verdict.py:21`, `verdict.py:22`, `ARCHITECTURE.md:57`. 통과
- 테스트 묶음이 통과한다.
  - `python3 -m unittest discover -s tests` → `Ran 226 tests in 19.534s`, 마지막 줄 `OK`. 통과

## 계획과 달라진 점
없음

## 남은 것
- `--changed-files`의 파일을 읽지 못하면 묶음의 판정이 `close`여도 `request`를 낸다. TODO의 글("파일을 읽지 못하면 `request`")대로 했고, 이때도 머지는 일어나지 않는다(fail-closed). 닫아야 할 PR이 머지 요청으로 남을 수 있다.
- 묶음이 객체이면 키의 값 꼴(목록, 객체 같은 것)은 검사하지 않는다. 그런 값은 `verdict`가 예외 없이 `request` 쪽으로 보낸다.

## 하네스에서 걸린 것
없음

## 확인 1

**통과 조건**
- 읽지 못한 입력에서 `request`와 0이다(완료 조건 1).
  - `printf 'not json' | python3 plugins/plate/ci/verdict.py; echo "exit=$?"` → `request`, `exit=0`. 통과
  - `printf '[]' | python3 plugins/plate/ci/verdict.py; echo "exit=$?"` → `request`, `exit=0`. 통과
  - `printf '{"build":"pass","lint":"none","test":"pass","coverage":"skipped","reliability":"A","security":"A","maintainability":"A"}' | python3 plugins/plate/ci/verdict.py --changed-files /nonexistent; echo "exit=$?"` → `request`, `exit=0`. 통과
- 문서가 바뀐 동작을 적는다.
  - `grep -n '읽지 못하면' plugins/plate/ci/verdict.py docs/ARCHITECTURE.md` → `verdict.py:21`, `verdict.py:22`, `ARCHITECTURE.md:57`. 두 파일에 저마다 한 줄 이상. 통과
- 테스트 묶음이 통과한다.
  - `python3 -m unittest discover -s tests` → `Ran 226 tests in 19.754s`, 마지막 줄 `OK`. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 226 tests`, `OK`. 통과

**테스트 먼저 기록**
- 기록 "한 일"의 테스트 먼저 → 실패 출력(`FAILED (failures=7)`, `UnreadableInputTest`)이 먼저, 통과 출력(`Ran 21 tests`, `OK`)이 그 뒤에 있다. 통과

**남은 것**
- `--changed-files`의 파일을 읽지 못하면 묶음의 판정이 `close`여도 `request`를 낸다 → TODO와 완료 조건의 글대로의 동작이고, 통과 조건은 모두 A 묶음에서 `request`를 보므로 `close` 묶음의 동작에 걸리지 않는다. 하네스에서 걸린 것
- 묶음이 객체이면 키의 값 꼴은 검사하지 않는다 → 통과 조건은 읽지 못한 입력(깨진 JSON, 객체가 아닌 JSON, 읽지 못하는 목록 파일)만 보므로 걸리지 않는다. 하네스에서 걸린 것

**실패**
없음

**하네스에서 걸린 것**
- 남은 것: `--changed-files`의 파일을 읽지 못하면 묶음의 판정이 `close`여도 `request`를 내서, 닫아야 할 PR이 머지 요청으로 남을 수 있다.
- 남은 것: 묶음이 객체이면 키의 값 꼴(목록, 객체 같은 것)은 검사하지 않고 `verdict`가 `request` 쪽으로 보낸다.

**판정**: 통과
