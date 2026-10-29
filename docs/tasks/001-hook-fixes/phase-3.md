# Phase 3: 훅의 예외와 세는 파일 쓰기

**목표**: 신뢰성-4·5가 고쳐져, 두 훅이 예외를 정한 대로 다루고 세는 파일의 쓰기 실패가 STOP으로 간다.

**테스트 먼저**: 예

**읽을 것**
- `docs/cleanup/2026-10-29.md` (신뢰성-4·5의 근거와 고치는 방향)
- `plugins/plate/hooks/edit_guard.py` (`main`, `count_block`, `STOP`)
- `plugins/plate/hooks/push_guard.py` (`main`, `check`, `UNSPLIT`)
- `docs/ARCHITECTURE.md`의 "패턴과 규칙" 절의 "막는 장치" 문단
- `docs/TOOLS.md`의 "훅" 항목 (종료 코드 2만 막는다)
- `tests/test_edit_guard.py`, `tests/test_push_guard.py`

**TODO**
- [x] 편집 훅의 `main`이 예외를 잡아 `plate:`로 시작하는 까닭을 stderr에 내고 종료 2로 끝나게 바뀐다 (`plugins/plate/hooks/edit_guard.py`)
- [x] 푸시 훅의 `main`이 예외를 잡아 까닭을 stderr에 내고, stdin의 글에 `push`가 있으면 종료 2, 없으면 종료 0으로 끝나게 바뀐다. stdin을 JSON으로 읽기 전의 글로 판단한다 (`plugins/plate/hooks/push_guard.py`)
- [x] `count_block`이 세는 파일을 임시 파일에 쓰고 `os.replace`로 바꿔 넣고, 쓰기에 실패하면 STOP에 닿는 수를 돌려주게 바뀐다 (`plugins/plate/hooks/edit_guard.py`)
- [x] 위 셋의 시험이 더해진다: 깨진 stdin, UTF-8이 아닌 phase 파일, `push`가 있고 없는 깨진 stdin, 세는 파일 자리가 폴더일 때 (`tests/test_edit_guard.py`, `tests/test_push_guard.py`)
- [x] "막는 장치" 문단에 두 훅의 예외 처리가 더해진다 (`docs/ARCHITECTURE.md`)

**통과 조건**
- 예외에서 편집 훅은 막는다(완료 조건 2).
  - 확인: `printf '{' | python3 plugins/plate/hooks/edit_guard.py; echo "exit=$?"` → stderr에 `plate:`로 시작하는 줄, `exit=2`
  - 확인: 셋업된 시험 레포의 테스트 먼저 "예"인 `phase-1.md`에 `printf '\xff' >>`로 바이트를 더하고 `src.py` 편집 JSON → stderr에 `plate:` 줄, 종료 2
- 예외에서 푸시 훅은 `push`가 있을 때만 막는다(완료 조건 2).
  - 확인: `printf '{"git push' | python3 plugins/plate/hooks/push_guard.py; echo "exit=$?"` → `exit=2`
  - 확인: `printf '{"ls' | python3 plugins/plate/hooks/push_guard.py; echo "exit=$?"` → `exit=0`
- 세는 파일의 쓰기 실패는 STOP으로 간다(완료 조건 3).
  - 확인: 시험 레포의 `.git/plate-test-first.json` 자리에 폴더를 만들고 `src.py` 편집 JSON → stderr에 `세 번째`가 든 줄, 종료 2
  - 확인: `grep -n 'os.replace' plugins/plate/hooks/edit_guard.py` → 한 줄 이상
- ARCHITECTURE가 바뀐 동작을 적는다.
  - 확인: `grep -n '예외' docs/ARCHITECTURE.md` → "막는 장치" 문단에 두 훅의 처리가 있다
- 테스트 묶음이 통과한다.
  - 확인: `python3 -m unittest discover -s tests` → 마지막 줄이 `OK`

## 한 일
- 편집 훅의 `main`이 예외를 잡아 `plate:`로 시작하는 까닭을 stderr에 내고 종료 2로 끝나게 바뀐다: `main`이 `check(json.load(sys.stdin))`의 예외를 잡아 `ERROR` 글(`plate: 편집 훅 안에서 예외가 나서 이 편집을 막는다: {예외 이름}: {글}`)을 내고 2를 돌려준다 (`plugins/plate/hooks/edit_guard.py`)
- 푸시 훅의 `main`이 예외를 잡아 까닭을 stderr에 내고, stdin의 글에 `push`가 있으면 종료 2, 없으면 종료 0으로 끝나게 바뀐다: stdin을 바이트로 먼저 읽고 `json.loads`와 `check`의 예외를 잡아 `ERROR` 글을 내고, 읽은 바이트에 `push`가 있으면 2, 없으면 0을 돌려준다 (`plugins/plate/hooks/push_guard.py`)
- `count_block`이 세는 파일을 임시 파일에 쓰고 `os.replace`로 바꿔 넣고, 쓰기에 실패하면 STOP에 닿는 수를 돌려주게 바뀐다: 쓰기를 `write_counts`로 떼어 같은 폴더에 `tempfile.mkstemp`로 쓰고 `os.replace`로 바꿔 넣으며, `OSError`면 임시 파일을 지우고 False를 돌려준다. 그때 `count_block`은 `STOP_COUNT`(3, `check`의 비교도 이 상수로 바꿈)를 돌려준다 (`plugins/plate/hooks/edit_guard.py`)
- 위 셋의 시험이 더해진다: `test_edit_guard.ExceptionTest`(깨진 stdin, UTF-8이 아닌 phase 파일), `ThirdBlockTest.test_unwritable_count_file_says_stop`(세는 파일 자리가 폴더), `ThirdBlockTest.test_count_file_is_replaced_not_rewritten`(읽기 전용 세는 파일도 바꿔 넣어 셈이 이어지고 임시 파일이 남지 않는다), `test_push_guard.ExceptionTest`(`push`가 있고 없는 깨진 stdin) (`tests/test_edit_guard.py`, `tests/test_push_guard.py`)
- "막는 장치" 문단에 두 훅의 예외 처리가 더해진다: 세는 파일을 바꿔 넣고 쓰기 실패면 세 번째 막음의 글을 낸다는 문장과, 두 훅의 예외 처리(편집 훅은 막고, 푸시 훅은 `push`가 있을 때만 막는다)와 그 까닭을 더했다 (`docs/ARCHITECTURE.md`)
- 테스트 먼저
  - 실패: `cd tests && python3 -m unittest test_edit_guard.ThirdBlockTest test_edit_guard.ExceptionTest test_push_guard.ExceptionTest` → `FAIL: test_count_file_is_replaced_not_rewritten`, `FAIL: test_unwritable_count_file_says_stop` (`'더 시도하지 않는다' not found`), `FAIL: test_broken_stdin_blocks`, `FAIL: test_non_utf8_phase_file_blocks` (`1 != 2 : 막아야 하는데 통과시켰다 (종료 코드 1): Traceback`), `FAIL: test_broken_stdin_with_push_blocks` (`1 != 2`), `FAIL: test_broken_stdin_without_push_passes` (`1 != 0`), `FAILED (failures=6)`
  - 통과: 같은 명령 → `Ran 11 tests in 2.096s`, `OK`

## 확인 결과
- 예외에서 편집 훅은 막는다(완료 조건 2).
  - `printf '{' | python3 plugins/plate/hooks/edit_guard.py; echo "exit=$?"` → stderr `plate: 편집 훅 안에서 예외가 나서 이 편집을 막는다: JSONDecodeError: …`, `exit=2`. 통과
  - `mktemp -d` 시험 레포(`AGENTS.md`에 docs-map 줄, `tests/test_x.py`, `src.py`, `docs/tasks/001-a/plan.md`, `**테스트 먼저**: 예`인 `phase-1.md` 커밋)의 `phase-1.md`에 `printf '\xff' >>` 뒤 `src.py` 편집 JSON → stderr `plate: 편집 훅 안에서 예외가 나서 이 편집을 막는다: UnicodeDecodeError: …`, 종료 2. 통과
- 예외에서 푸시 훅은 `push`가 있을 때만 막는다(완료 조건 2).
  - `printf '{"git push' | python3 plugins/plate/hooks/push_guard.py; echo "exit=$?"` → stderr `plate: 푸시 훅 안에서 예외가 났다: …`, `exit=2`. 통과
  - `printf '{"ls' | python3 plugins/plate/hooks/push_guard.py; echo "exit=$?"` → stderr `plate: 푸시 훅 안에서 예외가 났다: …`, `exit=0`. 통과
- 세는 파일의 쓰기 실패는 STOP으로 간다(완료 조건 3).
  - 새 시험 레포에서 `mkdir .git/plate-test-first.json` 뒤 `src.py` 편집 JSON → stderr `plate: 테스트 먼저 때문에 같은 파일을 세 번째 막았다: \`src.py\` …`, 종료 2. 통과
  - `grep -n 'os.replace' plugins/plate/hooks/edit_guard.py` → `237:        os.replace(tmp, store)`. 통과
- ARCHITECTURE가 바뀐 동작을 적는다.
  - `grep -n '예외' docs/ARCHITECTURE.md` → 48행(다른 문단)과 53행. 53행이 "막는 장치" 문단이고 두 훅의 예외 처리가 있다. 통과
- 테스트 묶음이 통과한다.
  - `python3 -m unittest discover -s tests` → `Ran 222 tests in 20.492s`, 마지막 줄 `OK`. 통과

## 계획과 달라진 점
- 없음

## 남은 것
- 세는 파일의 쓰기에 실패하면 실제로 막은 횟수와 상관없이 첫 막음부터 STOP 글("세 번째 막았다")을 낸다. 글의 횟수는 그때 사실과 다르다.
- 세는 파일이 깨진 JSON이면 여전히 셈을 비우고 처음부터 센다(신뢰성-5의 "깨진 파일을 삼킨다"는 이 phase의 TODO가 다루지 않았다). 잠금도 두지 않았다. 바꿔 넣기로 반쯤 쓴 파일은 생기지 않지만, 두 훅이 같은 때 돌면 한쪽의 셈을 잃을 수 있다.
- 푸시 훅은 예외가 나면 stdin 글 어디에든 `push`가 있으면 막는다(`description`이나 다른 낱말 속의 `push`도 든다).

## 하네스에서 걸린 것
- 처음 시험 레포에서 기준 편집을 먼저 돌려 세는 파일이 생긴 뒤 `mkdir`이 실패해, 폴더 자리 확인은 새 시험 레포에서 다시 돌렸다. 통과 조건이 시험 레포를 확인마다 새로 만드는지 적지 않았다.
