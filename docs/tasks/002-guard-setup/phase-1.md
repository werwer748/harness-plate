# Phase 1: 판정 스크립트의 워크플로 검사

**목표**: 판정 스크립트가 `--changed-files`로 받은 목록에 워크플로 경로가 있으면 merge를 request로 내린다.

**테스트 먼저**: 예

**읽을 것**
- `plugins/plate/ci/verdict.py` (지금의 판정과 입력·출력 설명)
- `tests/test_verdict.py` (스크립트를 subprocess로 돌리는 시험의 꼴)
- `docs/ARCHITECTURE.md`의 17줄과 51줄 (판정 스크립트와 판정 규칙을 적은 줄)

**TODO**
- [ ] `tests/test_verdict.py`에 세 시험이 더해진다: 워크플로 경로가 든 목록이면 merge가 request가 된다, 그 목록이어도 close는 그대로다, 목록이 없거나 워크플로 경로가 없으면 지금과 같다. 구현 전에 돌려 실패를 본다 (`tests/test_verdict.py`)
- [ ] `verdict.py`가 선택 인자 `--changed-files <파일>`를 받고, 그 안에 `.github/workflows/`로 시작하는 줄이 있으면 merge를 request로 바꾸도록 바뀐다. 맨 위 설명의 입력·출력과 예에 인자가 더해진다 (`plugins/plate/ci/verdict.py`)
- [ ] `docs/ARCHITECTURE.md` 17줄의 판정 스크립트 설명과 51줄의 판정 규칙에 워크플로를 바꾼 PR은 자동 머지가 아니라 머지 요청이라는 것이 더해진다 (`docs/ARCHITECTURE.md`)

**통과 조건**
- (완료 조건 1) 판정 검사가 시험으로 닫힌다
  - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
  - 확인: `tests/test_verdict.py`를 읽어 세 경우(워크플로 목록이면 merge가 request가 된다, close는 그대로다, 목록이 없으면 지금과 같다)가 저마다 시험에 있다
  - 확인: 이 phase의 기록에 새 시험이 실패한 출력과 통과한 출력이 이 순서로 있다
- `docs/ARCHITECTURE.md`의 두 줄이 바뀐 판정과 맞는다
  - 확인: 17줄과 51줄을 하나씩 읽어 둘 다 워크플로를 바꾼 PR이 머지 요청이 된다는 것과 어긋나지 않는다
