# 회고

## 회고 1

**확인**
- 1. 다시 수행하는 테스트 먼저 phase에서 그 phase 커밋의 테스트 변경을 센다(신뢰성-1)
  - `mktemp -d` 시험 레포(`AGENTS.md`에 docs-map 줄, 커밋된 `tests/test_x.py`·`tests/test_y.py`·`src.py`, `docs/tasks/001-a/plan.md`, `**테스트 먼저**: 예`인 `phase-1.md`)를 셋 만들어 `src.py` 편집 JSON을 `plugins/plate/hooks/edit_guard.py`에 넣음 → `tests/test_x.py`를 고친 `001-a: phase 1` 커밋과 `## 확인 1` 절: `exit=0`. 그 커밋이 `src.py`만 바꿈과 `## 확인 1` 절: `exit=2`. 테스트를 고친 커밋은 있고 `## 확인 1` 절이 없음(첫 수행): `exit=2`. 통과
- 2. 훅 안의 예외에서 편집 훅은 막고 푸시 훅은 `push`가 있을 때만 막는다(신뢰성-4)
  - `printf '{' | python3 plugins/plate/hooks/edit_guard.py; echo "exit=$?"` → stderr `plate: 편집 훅 안에서 예외가 나서 이 편집을 막는다: JSONDecodeError: …`, `exit=2`. 통과
  - 새 시험 레포의 `phase-1.md`에 `printf '\xff' >>` 뒤 `src.py` 편집 → stderr `plate: … UnicodeDecodeError: …`, `exit=2`. 통과
  - `printf '{"git push' | python3 plugins/plate/hooks/push_guard.py; echo "exit=$?"` → stderr `plate: 푸시 훅 안에서 예외가 났다: …`, `exit=2`. `printf '{"ls' | …` → `exit=0`. 통과
- 3. 세는 파일을 바꿔 넣고, 쓰기 실패면 STOP 글을 낸다(신뢰성-5)
  - 새 시험 레포에서 `mkdir .git/plate-test-first.json` 뒤 `src.py` 편집 → stderr `plate: 테스트 먼저 때문에 같은 파일을 세 번째 막았다: …`, `exit=2`. 통과
  - `grep -n 'os.replace' plugins/plate/hooks/edit_guard.py` → `237:        os.replace(tmp, store)`. 통과
- 4. 삭제뿐인 테스트 파일은 테스트 변경으로 세지 않는다(신뢰성-10)
  - 새 시험 레포에서 `git rm -q tests/test_x.py`만 한 뒤(`tests/test_y.py`는 남음) `src.py` 편집 → `exit=2`. 통과
- 5. `.md` 편집은 git 전에 통과하고, 커밋하지 않은 테스트 변경을 먼저 본다(성능-5·6)
  - `env PATH=/nonexistent $(command -v python3) plugins/plate/hooks/edit_guard.py`에 새 시험 레포의 `README.md` 편집 JSON → `exit=0`. `src.py` 편집 JSON → stderr `plate: … FileNotFoundError: … 'git'`, `exit=2`. 통과
  - `grep -n -e 'has_uncommitted_test_change(root)' -e 'has_tests(root)' plugins/plate/hooks/edit_guard.py` → `161:def has_tests`, `186:def has_uncommitted_test_change`, `285:    if has_uncommitted_test_change(root):`, `290:    if not has_tests(root):`. `check`는 248행에서 시작하고 그 안에서 285행이 290행보다 앞선다. 통과
- 6. `TEST_FIRST`의 테스트 파일 줄이 상수에서 만들어진다(유지보수성-5)
  - `grep -c -F '`test_*`, `*_test.*`' plugins/plate/hooks/edit_guard.py` → `0`. 통과
  - `python3 -c "… print(all(n in g.TEST_FIRST for n in g.TEST_NAMES) and all(d in g.TEST_FIRST for d in g.TEST_DIRS))"` → `True`. 통과
- 7. 맥락 문서가 바뀐 동작과 맞다
  - `grep -n -e '다시 수행' -e '예외' -e '결과물인 마크다운' docs/ARCHITECTURE.md` → 48, 53, 57, 85, 100행. 53행이 "막는 장치" 문단이고 `다시 수행` 1번, `예외` 2번, `결과물인 마크다운` 2번이 모두 그 줄에 있다. 통과
  - `grep -n '^### ADR-027' docs/ADR.md` → `63:### ADR-027: 편집 훅은 결과물인 마크다운도 막지 않는다` 한 줄. 통과
  - `docs/PRD.md`의 목표 절(4행)과 핵심 기능 6(16행)을 읽음 → 둘 다 훅이 막는 편집을 "코드 파일(`.md`가 아닌 파일)"의 편집으로 적고 `.md`는 막지 않는다(ADR-027)고 적는다. 통과
- 8. 테스트 묶음이 모두 통과한다
  - `python3 -m unittest discover -s tests` → `Ran 222 tests in 20.113s`, 마지막 줄 `OK`. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 222 tests`, `OK`. 통과
- 테스트 먼저 기록: phase 1
  - `done-phase-1.md` "한 일"의 "테스트 먼저" 줄 → 실패 출력(`FAILED (failures=3)`)이 먼저, 통과 출력(`Ran 47 tests`, `OK`)이 그 뒤에 있다. 통과
- 테스트 먼저 기록: phase 2
  - `done-phase-2.md` "한 일"의 "테스트 먼저" 줄 → 실패 출력(`FAILED (failures=1)`)이 먼저, 통과 출력(`Ran 6 tests`, `OK`)이 그 뒤에 있다. 통과
- 테스트 먼저 기록: phase 3
  - `done-phase-3.md` "한 일"의 "테스트 먼저" 줄 → 실패 출력(`FAILED (failures=6)`)이 먼저, 같은 명령의 통과 출력(`Ran 11 tests`, `OK`)이 그 뒤에 있다. 통과

**남은 것**
- phase 1: `.md` 갈래는 경로 글의 끝만 보아 `.md` 이름의 심볼릭 링크가 코드 파일을 가리키면 통과한다 → 문제 아님 (ADR-027과 "막는 장치" 문단이 `.md` 파일을 이름으로 코드에서 빼기로 정했고, 링크의 꼴은 그 결정의 경계 밖이다)
- phase 1: 삭제를 세지 않는 것은 `D `, ` D`뿐이고 `AD`, `MD`는 테스트 변경으로 센다 → 문제 아님 (완료 조건 4가 정한 것은 "상태가 삭제뿐인" 항목이고, 그 동작은 위 확인 4에서 막힘을 보았다)
- phase 1: `TEST_FIRST`의 폴더 차례가 `__tests__/`, `test/`, `tests/`로 바뀌었다 → 문제 아님 (글의 차례만 바뀌었고 완료 조건 6과 시험이 이름이 모두 드는지만 본다. 동작 차이 없음)
- phase 1: 시험이 `edit_guard`를 불러와 `plugins/plate/hooks/__pycache__/`가 생길 수 있다 → 문제 아님 (`.gitignore`에 `__pycache__/`가 있고 `git status --short`가 비어 있다)
- phase 2: 같은 제목의 커밋이 여럿이면 하나라도 테스트를 바꿨으면 세고, `NNN-slug: phase N 고침` 커밋은 세지 않는다 → 문제 아님 (task 머리의 결정이 "그 phase의 커밋은 제목이 `NNN-slug: phase N`인 커밋"이라 정한 대로다)
- phase 2: 다시 수행 갈래는 `git log` 전체를 훑어 이력이 긴 레포에서 느려진다 → 문제 아님 (확인 절이 있고 커밋하지 않은 테스트 변경이 없을 때만 돌고, 동작은 틀리지 않는다. 완료 조건은 판정만 본다)
- phase 3: 세는 파일의 쓰기에 실패하면 첫 막음부터 "세 번째 막았다" 글을 낸다 → 문제 아님 (완료 조건 3이 쓰기 실패에서 세 번째 막음의 글을 내라고 정했다)
- phase 3: 세는 파일이 깨진 JSON이면 셈을 비우고, 잠금이 없어 동시에 돌면 셈을 잃을 수 있다 → 문제 아님 (완료 조건 3은 바꿔 넣기와 쓰기 실패만 정했고, 바꿔 넣기로 반쯤 쓴 파일은 생기지 않는다. 남은 꼴은 FRICTION에 경계 밖으로 둔다)
- phase 3: 푸시 훅은 예외 때 stdin 글 어디에든 `push`가 있으면 막는다 → 문제 아님 (task 머리의 결정 "푸시 훅은 stdin의 글에 `push`가 있을 때만 막는다" 그대로다)

**문제**
- 없음

**판정**: 통과
