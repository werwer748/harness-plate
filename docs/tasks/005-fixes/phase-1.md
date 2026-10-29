# Phase 1: tasks 끝의 문제를 고친다

**목표**: task 머리의 완료 조건에 적힌 것을 모두 고친다.

**테스트 먼저**: 예

**읽을 것**
- `docs/tasks/review.md`의 `## 평가 1` 절
- `docs/tasks/eval.md`의 `## eval 1` 절
- `plugins/plate/hooks/edit_guard.py`
- `plugins/plate/skills/phase/SKILL.md`
- `tests/test_edit_guard.py`
- `tests/hook_helpers.py`
- `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `docs/BACKLOG.md`, `docs/cleanup/2026-10-29.md`

**TODO**
- [x] 다시 수행의 테스트 셈이 전체 역사에서 같은 제목의 커밋을 찾아, 지난 tasks의 같은 이름 phase 커밋이 테스트를 바꿨으면 이번 phase가 테스트를 바꾸지 않았어도 구현 편집을 통과시킨다. 갈라진 곳 뒤나 이 tasks의 계획 커밋 뒤의 커밋으로 좁힌다. 고친 뒤 ARCHITECTURE "막는 장치" 문단의 다시 수행 줄이 고친 동작과 맞게 한다 (`plugins/plate/hooks/edit_guard.py`, `docs/ARCHITECTURE.md`, `tests/test_edit_guard.py`)
- [x] phase 본문의 새 구현 파일 옮기기가 파일이 여럿일 때 임시 자리를 잃거나 같은 이름끼리 덮이지 않게 하고, `git status --porcelain`이 다를 때 되살리는 법을 적는다 (`plugins/plate/skills/phase/SKILL.md`)
- [x] `STOP`의 글이 "세 번째"를 손으로 적어 `STOP_COUNT`와 따로 노는 것을 상수에서 만들게 고친다. 그 글을 지키는 테스트(`tests/test_edit_guard.py:540`)도 고친 글을 지키게 한다 (`plugins/plate/hooks/edit_guard.py`, `tests/test_edit_guard.py`)
- [x] phase 커밋에서 테스트 파일을 지우기만 한 경우를 다시 수행의 셈에서 빼는지 보는 시험을 더한다 (`tests/test_edit_guard.py`)
- [x] 고친 코드에서 같은 뿌리의 꼴(같은 함수의 다른 입력, 앞서 막던 꼴)을 찾아 테스트로 남긴다 (`tests/test_edit_guard.py`)

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다

## 한 일
- 다시 수행의 테스트 셈을 이번 tasks의 계획 커밋 뒤로 좁히고 ARCHITECTURE를 맞춘다: `phase_commit_has_test_change`가 그 task 머리(`docs/tasks/NNN-slug/plan.md`)를 마지막으로 더한 커밋(`git log -1 --diff-filter=A -- <plan.md>`)을 찾아 `<그 커밋>..HEAD`에서만 같은 제목의 커밋을 본다. 그 커밋이 없으면 세지 않는다. ARCHITECTURE "막는 장치" 문단의 다시 수행 줄에 지우기만 한 것은 빼는 것과 이번 tasks의 계획 커밋 뒤에서만 찾는 것을 더했다 (`plugins/plate/hooks/edit_guard.py`, `docs/ARCHITECTURE.md`, `tests/test_edit_guard.py`)
- phase 본문의 새 구현 파일 옮기기: 임시 자리를 한 번만 잡고(`tmp=$(mktemp -d)`) 파일마다 저장소 안의 경로째 옮기고(`mkdir -p "$tmp/$(dirname <구현 파일>)" && mv <구현 파일> "$tmp/<구현 파일>"`) 되살린 뒤 `rm -rf "$tmp"`, `git status --porcelain`이 다르면 다른 파일마다 `git checkout HEAD -- <구현 파일>`로 되살리고 다시 견준다고 적었다 (`plugins/plate/skills/phase/SKILL.md`)
- `STOP`의 횟수 글을 상수에서 만든다: `ORDINALS`와 `ordinal(n)`(3 → `세 번째`, 열을 넘으면 숫자)을 두고 `STOP`을 `ordinal(STOP_COUNT)`로 만든다. `test_unwritable_count_file_says_stop`이 `ordinal(STOP_COUNT) + " 막았다"`를 보고, `test_stop_message_follows_stop_count`가 `STOP_COUNT = 4`로 바꾼 사본에서 세 번은 `TEST_FIRST`, 네 번째에 `네 번째 막았다`가 나는지 본다 (`plugins/plate/hooks/edit_guard.py`, `tests/test_edit_guard.py`)
- 지우기만 한 phase 커밋의 시험: `test_phase_commit_deleting_test_only_blocks`(phase 커밋이 `tests/test_app.py`를 `git rm`만 하고 `tests/test_other.py`는 남음 → 막음) (`tests/test_edit_guard.py`)
- 같은 뿌리의 꼴: `test_previous_tasks_phase_commit_does_not_count`(지난 tasks의 같은 제목 커밋만 테스트를 바꿈 → 막음), `test_current_tasks_phase_commit_counts_after_previous_tasks`(이번 tasks의 커밋도 테스트를 바꿈 → 통과), `test_previous_tasks_commit_does_not_count_before_phase_commit`(이번 tasks의 phase 커밋이 아직 없음 → 막음), `test_plan_md_change_after_phase_commit_keeps_it`(phase 커밋 뒤 task 머리를 고친 커밋이 있어도 통과 — 계획 커밋을 "고친 커밋"이 아니라 "더한 커밋"으로 잡는지 본다) (`tests/test_edit_guard.py`)
- 테스트 먼저
  - 실패: `python3 -m unittest tests.test_edit_guard` → `ImportError: cannot import name 'ordinal' from 'edit_guard'`, `FAILED (errors=1)`. `ordinal`만 끼워 넣고 돌린 것(`python3 -c "…edit_guard.ordinal=lambda n: …; unittest.main(module=None)" test_edit_guard`) → `FAIL: test_previous_tasks_commit_does_not_count_before_phase_commit`, `FAIL: test_previous_tasks_phase_commit_does_not_count`, `FAIL: test_stop_message_follows_stop_count`, `Ran 64 tests`, `FAILED (failures=3)`
  - 통과: `python3 -m unittest tests.test_edit_guard` → `Ran 64 tests in 11.467s`, `OK`

## 확인 결과
- 완료 조건 1: 지난 tasks의 같은 이름 phase 커밋 때문에 통과시키지 않는다
  - `mktemp -d` 시험 레포(지난 tasks의 `plan: old`, 테스트를 바꾼 `001-a: phase 1`, `docs/tasks` 비움, `plan: new`, 이번 tasks의 `001-a: phase 1`, `## 확인 1` 커밋)에 `src/app.py` 편집 JSON → 이번 커밋이 구현만 바꾸면 `impl exit=2`, 테스트도 바꾸면 `test exit=0`. 통과
- 완료 조건 2: 새 구현 파일 여럿 옮기기
  - 시험 레포에서 `pkg/a/__init__.py`, `pkg/b/__init__.py`를 새로 만든 `001-a: phase 1` 커밋 → `git cat-file -e` 둘 다 128, 본문 명령대로 옮김(` D pkg/a/__init__.py  D pkg/b/__init__.py`) → 되살림 뒤 `git status --porcelain`이 시작과 같음(빈 출력), 내용 `A`·`B` 그대로. 한 파일을 지운 상태에서 `git checkout HEAD -- pkg/a/__init__.py` → 시작과 같음. 본문에 그 명령 줄 `grep -c` → `1`. 통과
- 완료 조건 3: `STOP_COUNT`를 바꾼 사본
  - `sed 's/^STOP_COUNT = 3 /STOP_COUNT = 5 /'` 사본으로 같은 파일을 다섯 번 편집 → 네 번 `TEST_FIRST`, 다섯 번째 `같은 파일을 다섯 번째 막았다`. 통과
- 완료 조건 4: 지우기만 한 경우의 시험
  - `tests/test_edit_guard.py`에 `test_phase_commit_deleting_test_only_blocks`가 있다. `--diff-filter=d`를 뺀 사본(`grep -c` → `0`)에서 `python3 -m unittest tests.test_edit_guard.RerunTest` → `FAIL: test_phase_commit_deleting_test_only_blocks`, `FAILED (failures=1)`. 통과
- 완료 조건 5: tasks 완료 조건 1, 2, 4, 6
  - 1: `python3 -m unittest discover -s tests` → `OK`. 통과
  - 2: `docs/tasks/001-hook-fixes/plan.md`의 완료 조건 확인을 작업 트리에서 다시 돌림 → 1: 테스트를 바꾼 커밋+확인 절 `exit=0`, `src.py`만 `exit=2`, 확인 절 없음 `exit=2`. 2: `printf '{'` → `plate:` 줄과 `exit=2`, `\xff` → `plate:`(`UnicodeDecodeError`) 줄과 `exit=2`, 푸시 훅 `{"git push` → `exit=2`, `{"ls` → `exit=0`. 3: 세는 파일 자리에 폴더 → `세 번째 막았다` 줄과 `exit=2`, `os.replace` 253행. 4: `git rm tests/test_x.py`만 → `exit=2`. 5: `env PATH=/nonexistent python3`에서 `README.md` → `exit=0`, `src.py` → `FileNotFoundError: … 'git'` 줄과 `exit=2`, `has_uncommitted_test_change(root)` 301행 < `has_tests(root)` 306행. 6: `grep -c` → `0`, 상수 확인 → `True`. 7: ARCHITECTURE 54행에 `다시 수행`·`예외`·`결과물인 마크다운`, `### ADR-027` 63행 한 줄, PRD 4·16행이 코드 파일(`.md`가 아닌 파일)로 좁힘. 8: 1과 같음. 모두 기대대로. 통과
  - 4: `docs/tasks/003-skill-fixes/plan.md`의 완료 조건 확인을 다시 돌림 → 1: `다시 띄움: 결과 없음` 293행("멈춘다" 자리 목록)·570행, 시험 `OK`. 2: `tasks 브랜치` 89행 < `계획의 커밋` 96행. 3: `gh api user` 376·519행, `gh api user --jq .login` → `werwer748`, `gh issue view 68 … --jq '.author.login'` → `werwer748`. 4: 시험 `OK`. 5: `부모 커밋에 없` 59행("## 2. TODO를 차례로 끝낸다" 42행 아래), 시험 레포에서 바꾼 파일은 `git checkout <커밋>^ --`/`git checkout HEAD --`, 새 파일은 고친 본문의 명령대로 옮겼다 되살린 뒤 `git status --porcelain` 빈 출력. 6: review 72행 커버리지 항목에 `한 번`. 7: `맥락 문서를 모두 읽는다` 없음(종료 1), `결정 절` 99행("## 4. 2라운드" 90행 아래)·190행("## 2라운드에 맡기는 글" 172행 아래). 8: `결과 없` PRD 1줄·ARCHITECTURE 2줄, `gh api user` ARCHITECTURE 57행 run 문단. 9: 1과 같음. 모두 기대대로. 통과
  - 6: `python3 -m unittest tests.test_skill_rules tests.test_manifests tests.test_cleanup_skill tests.test_edit_guard tests.test_push_guard` → `OK`. `grep -n '^def section' tests/test_cleanup_skill.py` → 아무것도 나오지 않음(종료 1). 통과
  - "마지막 커밋에서"는 이 phase의 커밋 전 작업 트리에서 돌렸다(커밋에 들어갈 내용과 같다)

## 계획과 달라진 점
- 없음

## 남은 것
- 다시 수행의 셈은 그 task 머리(`plan.md`)를 더한 커밋이 git 역사에 없으면(계획을 커밋하지 않은 채 다시 수행) phase 커밋을 세지 않아 구현 편집을 막는다. plan 스킬이 계획을 늘 커밋하므로 그런 상태는 plate의 흐름에서 생기지 않는다고 봤다. 001의 완료 조건 확인 1도 시험 레포의 `plan.md`를 첫 커밋에 넣어 돌렸다
- 계획 커밋을 "그 경로를 더한 마지막 커밋"으로 잡으므로, 이번 tasks 안에서 그 task 폴더를 지웠다 다시 더하면 그 앞의 같은 제목 커밋은 세지 않는다

## 하네스에서 걸린 것
- 완료 조건 5의 "이 tasks의 마지막 커밋에서 다시 돌려"는 phase 커밋 전에 돌릴 수밖에 없어 커밋할 작업 트리에서 돌렸다
- 001 완료 조건 1의 시험 레포 설명이 `docs/tasks/001-a/plan.md`를 "있다"고만 하고 커밋했는지 적지 않는다. 고친 훅은 그 파일을 더한 커밋을 찾으므로 커밋한 레포로 돌렸다
