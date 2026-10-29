# Phase 3: phase의 실패 출력 얻기와 review의 커버리지

**목표**: 신뢰성-2와 성능-4가 고쳐진다.

**테스트 먼저**: 아니오 — 스킬 본문(`.md`)만 고친다

**읽을 것**
- `docs/cleanup/2026-10-29.md` (신뢰성-2, 성능-4의 근거와 고치는 방향)
- `plugins/plate/skills/phase/SKILL.md`의 "2. TODO를 차례로 끝낸다" 절 (실패 출력 얻기 문단)
- `plugins/plate/skills/review/SKILL.md`의 "2. 잰다" 절
- `tests/test_skill_rules.py` (phase·review 본문을 지키는 시험)

**TODO**
- [x] 실패 출력 얻기 문단에, phase 커밋의 부모 커밋에 없는 구현 파일(그 phase가 새로 만든 파일)은 잠깐 다른 자리로 옮겨 테스트를 돌리고 되살리는 갈래와 그 명령 예가 더해진다. 부모에 있는 파일의 `git checkout <커밋>^ -- <구현 파일>` 갈래는 그대로다 (`plugins/plate/skills/phase/SKILL.md`)
- [x] "2. 잰다"의 커버리지 항목에, 커버리지 도구가 테스트 명령을 감쌀 수 있으면 1번의 테스트를 그 도구로 한 번만 돌려 테스트 결과와 커버리지에 함께 쓴다는 것이 더해진다 (`plugins/plate/skills/review/SKILL.md`)
- [x] `tests/`에서 고친 두 문단의 옛 글을 찾아(`git grep -n -F 'checkout <커밋>^' -- tests/`, `git grep -n -F '커버리지 도구로 테스트를' -- tests/`) 걸리는 시험을 새 글을 지키게 고친다 (`tests/test_skill_rules.py`)

**통과 조건**
- phase 본문이 새 파일의 갈래를 적고 명령 예가 돈다(완료 조건 5).
  - 확인: `grep -n '부모 커밋에 없' plugins/plate/skills/phase/SKILL.md` → "2. TODO를 차례로 끝낸다" 절에 한 줄 이상
  - 확인: `mktemp -d` 시험 레포에 `tests/test_a.py`와, phase 커밋(`001-a: phase 1`)이 새로 만든 `new.py`와 고친 `old.py`를 둔다. 본문의 명령 예대로 `new.py`는 옮겼다 되살리고 `old.py`는 부모 것으로 되돌렸다 되살린 뒤, 그 사이에 테스트가 실패하고 끝에 `git status --porcelain`이 비어 있다
- review 본문이 한 번 돌림을 적는다(완료 조건 6).
  - 확인: `grep -n '한 번' plugins/plate/skills/review/SKILL.md` → "2. 잰다" 절의 커버리지 항목에 한 줄 이상
- 앞 phase의 동작이 그대로다(완료 조건 1~4).
  - 확인: `python3 -m unittest tests.test_skill_rules.RunRulesTest.test_no_result_relaunch_limit tests.test_skill_rules.RunRulesTest.test_stop_line_grep_runs_on_fake_runlog -v` → `OK`
- 테스트 묶음이 통과한다.
  - 확인: `python3 -m unittest discover -s tests` → 마지막 줄이 `OK`

## 한 일
- 실패 출력 얻기 문단: 구현 파일마다 `git cat-file -e <커밋>^:<구현 파일>`로 부모 커밋에 있는지 보고 두 갈래로 나눴다. 부모에 있는 파일은 그대로 `git checkout <커밋>^ -- <구현 파일>`로 되돌리고 `git checkout HEAD -- <구현 파일>`로 되살린다. 부모 커밋에 없는 파일은 `tmp=$(mktemp -d) && mv <구현 파일> "$tmp"/`로 저장소 밖에 옮기고 `mv "$tmp"/<파일 이름> <구현 파일>`로 되살린다. 끝에 `git status --porcelain`이 시작과 같은지 본다는 줄을 더했다 (`plugins/plate/skills/phase/SKILL.md`)
- "2. 잰다"의 커버리지 항목: 커버리지 도구가 테스트 명령을 감쌀 수 있으면(`coverage run -m pytest`처럼) 1번의 테스트를 그 도구로 한 번만 돌려 테스트 결과와 커버리지에 함께 쓰고 같은 묶음을 다시 돌리지 않는다는 문장을 더했다 (`plugins/plate/skills/review/SKILL.md`)
- `tests/`의 옛 글 찾기: `git grep -n -F 'checkout <커밋>^' -- tests/`와 `git grep -n -F '커버리지 도구로 테스트를' -- tests/`가 둘 다 아무것도 내지 않아 고칠 시험이 없었다 (`tests/test_skill_rules.py`는 바꾸지 않음)

## 확인 결과
- phase 본문이 새 파일의 갈래를 적고 명령 예가 돈다(완료 조건 5).
  - `grep -n '부모 커밋에 없' plugins/plate/skills/phase/SKILL.md` → `59:- 부모 커밋에 없는 파일(그 phase가 새로 만든 파일): ...`. 59줄은 "## 2. TODO를 차례로 끝낸다"(42줄)와 다음 절 사이다. 통과
  - `mktemp -d` 시험 레포: `base` 커밋에 `tests/test_a.py`(test_old는 `old.f()==1`, test_new는 `new.g()==2`를 본다)와 `old.py`(`return 0`), `001-a: phase 1` 커밋에서 `old.py`를 `return 1`로 고치고 `new.py`를 새로 만들었다. 시작 `git status --porcelain` → 빈 줄. `git cat-file -e` → `old.py in parent`, `new.py not in parent`. `git checkout "$c^" -- old.py`, `tmp=$(mktemp -d) && mv new.py "$tmp"/` 뒤 `python3 -m unittest discover -s tests` → `ERROR: test_new (test_a.T)`, `FAIL: test_old (test_a.T)`, `FAILED (failures=1, errors=1)`. `git checkout HEAD -- old.py`, `mv "$tmp"/new.py new.py` 뒤 → `OK`, 끝 `git status --porcelain` → 빈 줄. 옛 명령 `git checkout "$c^" -- new.py` → `error: pathspec 'new.py' did not match any file(s) known to git`(고친 까닭이 재현됨). 통과
- review 본문이 한 번 돌림을 적는다(완료 조건 6).
  - `grep -n '한 번' plugins/plate/skills/review/SKILL.md` → `72:2. **커버리지**: ... 1번의 테스트를 그 도구로 한 번만 돌려 ...`. "## 2. 잰다" 절의 커버리지 항목이다. 통과
- 앞 phase의 동작이 그대로다(완료 조건 1~4).
  - `python3 -m unittest tests.test_skill_rules.RunRulesTest.test_no_result_relaunch_limit tests.test_skill_rules.RunRulesTest.test_stop_line_grep_runs_on_fake_runlog -v` → `Ran 2 tests`, `OK`. 통과
- 테스트 묶음이 통과한다.
  - `python3 -m unittest discover -s tests` → `Ran 233 tests in 20.620s`, `OK`. 통과

## 계획과 달라진 점
- TODO 3은 `tests/test_skill_rules.py`를 고친다고 적었으나, 두 grep이 걸린 시험을 하나도 내지 않아 그 파일을 바꾸지 않았다.

## 남은 것
- 새 갈래와 한 번 돌림을 지키는 시험은 `tests/`에 없다. 본문 글이 바뀌어도 시험은 실패하지 않는다(이 phase의 TODO가 새 시험을 두라고 하지 않았다).
- 시험 레포의 첫 시도에서 `old.py`의 두 판이 크기가 같고 같은 초에 바뀌어, `sys.pycache_prefix`(`~/Library/Caches/com.apple.python`)의 낡은 바이트코드가 읽혀 test_old가 실패하지 않았다. 크기가 다른 판으로 다시 돌려 위 결과를 얻었다. 본문의 갈래대로 되돌려도 Python 프로젝트에서 이 캐시가 실패 출력을 가릴 수 있으나 본문에는 적지 않았다.
- 고칠 문제 갈래에서 구현 파일에 커밋되지 않은 변경이 있으면 `git checkout HEAD -- <구현 파일>`이 그 변경을 지운다. 이 문단은 phase 커밋이 끝난 뒤 실패 출력만 얻는 자리라 그대로 두었다.

## 하네스에서 걸린 것
- 프로젝트의 규칙을 따름: AGENTS.md의 스킬 본문 규칙대로, 이 phase는 세션에 실린 판의 `plate:phase`를 따라 수행했고 고친 phase 본문의 동작은 그 본문을 따라 도는 것이 아니라 시험 레포에서 명령 예를 돌려 봤다.
