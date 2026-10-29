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
- [ ] 편집 훅의 `main`이 예외를 잡아 `plate:`로 시작하는 까닭을 stderr에 내고 종료 2로 끝나게 바뀐다 (`plugins/plate/hooks/edit_guard.py`)
- [ ] 푸시 훅의 `main`이 예외를 잡아 까닭을 stderr에 내고, stdin의 글에 `push`가 있으면 종료 2, 없으면 종료 0으로 끝나게 바뀐다. stdin을 JSON으로 읽기 전의 글로 판단한다 (`plugins/plate/hooks/push_guard.py`)
- [ ] `count_block`이 세는 파일을 임시 파일에 쓰고 `os.replace`로 바꿔 넣고, 쓰기에 실패하면 STOP에 닿는 수를 돌려주게 바뀐다 (`plugins/plate/hooks/edit_guard.py`)
- [ ] 위 셋의 시험이 더해진다: 깨진 stdin, UTF-8이 아닌 phase 파일, `push`가 있고 없는 깨진 stdin, 세는 파일 자리가 폴더일 때 (`tests/test_edit_guard.py`, `tests/test_push_guard.py`)
- [ ] "막는 장치" 문단에 두 훅의 예외 처리가 더해진다 (`docs/ARCHITECTURE.md`)

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
