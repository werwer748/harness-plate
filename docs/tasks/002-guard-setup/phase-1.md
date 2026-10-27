# Phase 1: 판정 스크립트의 워크플로 검사

**목표**: 판정 스크립트가 `--changed-files`로 받은 목록에 워크플로 경로가 있으면 merge를 request로 내린다.

**테스트 먼저**: 예

**읽을 것**
- `plugins/plate/ci/verdict.py` (지금의 판정과 입력·출력 설명)
- `tests/test_verdict.py` (스크립트를 subprocess로 돌리는 시험의 꼴)
- `docs/ARCHITECTURE.md`의 17줄과 51줄 (판정 스크립트와 판정 규칙을 적은 줄)

**TODO**
- [x] `tests/test_verdict.py`에 세 시험이 더해진다: 워크플로 경로가 든 목록이면 merge가 request가 된다, 그 목록이어도 close는 그대로다, 목록이 없거나 워크플로 경로가 없으면 지금과 같다. 구현 전에 돌려 실패를 본다 (`tests/test_verdict.py`)
- [x] `verdict.py`가 선택 인자 `--changed-files <파일>`를 받고, 그 안에 `.github/workflows/`로 시작하는 줄이 있으면 merge를 request로 바꾸도록 바뀐다. 맨 위 설명의 입력·출력과 예에 인자가 더해진다 (`plugins/plate/ci/verdict.py`)
- [x] `docs/ARCHITECTURE.md` 17줄의 판정 스크립트 설명과 51줄의 판정 규칙에 워크플로를 바꾼 PR은 자동 머지가 아니라 머지 요청이라는 것이 더해진다 (`docs/ARCHITECTURE.md`)

**통과 조건**
- (완료 조건 1) 판정 검사가 시험으로 닫힌다
  - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
  - 확인: `tests/test_verdict.py`를 읽어 세 경우(워크플로 목록이면 merge가 request가 된다, close는 그대로다, 목록이 없으면 지금과 같다)가 저마다 시험에 있다
  - 확인: 이 phase의 기록에 새 시험이 실패한 출력과 통과한 출력이 이 순서로 있다
- `docs/ARCHITECTURE.md`의 두 줄이 바뀐 판정과 맞는다
  - 확인: 17줄과 51줄을 하나씩 읽어 둘 다 워크플로를 바꾼 PR이 머지 요청이 된다는 것과 어긋나지 않는다

## 한 일
- `tests/test_verdict.py`에 세 시험이 더해진다: `ChangedFilesTest`를 더했다. 시험 도우미 `verdict()`가 `changed_files` 목록을 받으면 임시 파일에 한 줄에 하나씩 적어 `--changed-files`로 넘긴다. `test_workflow_path_turns_merge_into_request`(워크플로 경로가 든 목록이면 merge가 request), `test_workflow_path_keeps_close_and_request`(그 목록이어도 close와 request는 그대로), `test_no_list_or_no_workflow_path_is_unchanged`(목록 없음, 빈 목록, 워크플로 경로 없는 목록은 지금과 같음) (`tests/test_verdict.py`)
- `verdict.py`가 선택 인자 `--changed-files <파일>`를 받는다: argparse로 인자를 받고, 판정이 merge이고 목록 파일에 `.github/workflows/`로 시작하는 줄이 있으면 request로 바꾼다. 맨 위 설명에 선택 인자, merge·request 설명, 인자를 쓴 예를 더했다 (`plugins/plate/ci/verdict.py`)
- `docs/ARCHITECTURE.md` 17줄과 51줄: 17줄의 판정 스크립트 설명과 51줄의 판정 규칙 뒤에 워크플로 경로가 든 목록이면 자동 머지를 머지 요청으로 내린다는 것을 더했다 (`docs/ARCHITECTURE.md`)
- 테스트 먼저
  - 실패: `python3 -m unittest tests.test_verdict` → `FAIL: test_workflow_path_turns_merge_into_request (tests.test_verdict.ChangedFilesTest)` / `AssertionError: 'merge' != 'request'` / `Ran 17 tests` / `FAILED (failures=1)`
  - 통과: `python3 -m unittest tests.test_verdict` → `Ran 17 tests in 1.151s` / `OK`

## 확인 결과
- (완료 조건 1) 판정 검사가 시험으로 닫힌다
  - `python3 -m unittest discover -s tests` → `Ran 102 tests in 16.585s`, 마지막 줄 `OK`. 통과
  - `tests/test_verdict.py`를 읽음 → 세 경우가 `ChangedFilesTest`의 세 시험에 저마다 있다(워크플로 목록이면 request, close 그대로, 목록 없으면 merge 그대로). 통과
  - 이 기록의 "한 일" 테스트 먼저 항목 → 실패 출력 뒤에 통과 출력이 이 순서로 있다. 통과
- `docs/ARCHITECTURE.md`의 두 줄이 바뀐 판정과 맞는다
  - `sed -n '17p;51p' docs/ARCHITECTURE.md`로 읽음 → 17줄과 51줄 모두 워크플로 경로가 든 목록이면 자동 머지를 머지 요청으로 내린다고 적어 어긋나지 않는다. 통과

## 계획과 달라진 점
없음

## 남은 것
- 51줄은 판정 스크립트가 목록을 받을 때의 동작만 적는다. 양식 워크플로가 실제로 바뀐 파일 목록을 넘기는 것은 아직 아니며, task 머리의 완료 조건 3(setup 양식 절)과 다른 phase가 다룬다. 그때까지 깔린 워크플로는 인자 없이 지금처럼 판정한다
- 워크플로 경로 판단은 줄의 앞뒤 공백을 지운 뒤 `.github/workflows/`로 시작하는지만 본다. `./.github/workflows/`처럼 다른 꼴로 적은 경로나 대소문자가 다른 경로는 워크플로로 보지 않는다
- 판정이 merge가 아니면 목록 파일을 열지 않으므로, 없는 파일을 넘겨도 close·request에서는 오류가 나지 않는다. merge일 때 없는 파일이면 예외로 끝난다(종료 코드 0이 아님)

## 하네스에서 걸린 것
없음
