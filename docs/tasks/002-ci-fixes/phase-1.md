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
- [ ] `main`이 stdin을 JSON으로 읽지 못하거나 객체가 아니면, 또는 `--changed-files`의 파일을 읽지 못하면 `request`를 내고 0으로 끝나게 바뀐다 (`plugins/plate/ci/verdict.py`)
- [ ] docstring의 출력 설명에 읽지 못하면 `request`라는 것이 더해진다 (`plugins/plate/ci/verdict.py`)
- [ ] 깨진 JSON, 객체가 아닌 JSON, 빈 입력, 읽지 못하는 목록 파일의 시험이 더해진다 (`tests/test_verdict.py`)
- [ ] PR의 CI 문단의 판정 셋 줄에, 판정 스크립트가 입력을 읽지 못하면 머지 요청이라는 것이 더해진다 (`docs/ARCHITECTURE.md`)

**통과 조건**
- 읽지 못한 입력에서 `request`와 0이다(완료 조건 1).
  - 확인: `printf 'not json' | python3 plugins/plate/ci/verdict.py; echo "exit=$?"` → `request`, `exit=0`
  - 확인: `printf '[]' | python3 plugins/plate/ci/verdict.py; echo "exit=$?"` → `request`, `exit=0`
  - 확인: `printf '{"build":"pass","lint":"none","test":"pass","coverage":"skipped","reliability":"A","security":"A","maintainability":"A"}' | python3 plugins/plate/ci/verdict.py --changed-files /nonexistent; echo "exit=$?"` → `request`, `exit=0`
- 문서가 바뀐 동작을 적는다.
  - 확인: `grep -n '읽지 못하면' plugins/plate/ci/verdict.py docs/ARCHITECTURE.md` → 두 파일에 저마다 한 줄 이상
- 테스트 묶음이 통과한다.
  - 확인: `python3 -m unittest discover -s tests` → 마지막 줄이 `OK`
