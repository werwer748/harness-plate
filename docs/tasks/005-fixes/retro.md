# 회고

## 회고 1

**확인**
- 1. 다시 수행의 테스트 셈이 지난 tasks의 같은 이름 phase 커밋 때문에 구현 편집을 통과시키지 않는다
  - `mktemp -d` 시험 레포(`AGENTS.md`의 docs-map 줄, 커밋된 `tests/test_x.py`·`src.py`, 지난 tasks의 `plan: old`와 테스트를 바꾼 `001-a: phase 1`, `docs/tasks` 비움, 이번 tasks의 `001-a: phase 1`, `**테스트 먼저**: 예`와 `## 확인 1` 절이 있는 `phase-1.md`)에 `src.py` 편집 JSON을 훅에 넣음. 이번 tasks의 task 머리를 커밋한 꼴(`plan: new`)과 커밋하지 않은 꼴 모두 → 이번 커밋이 구현만 바꾸면 종료 2, 테스트도 바꾸면 종료 0. 통과
- 2. phase 본문의 새 구현 파일 옮기기가 여럿·같은 이름에서 돌고, 다를 때 되살리는 법이 있다
  - 시험 레포에서 `pkg/a/__init__.py`, `pkg/b/__init__.py`를 새로 만든 `001-a: phase 1` 커밋 → `git cat-file -e <커밋>^:…` 둘 다 128. 본문 59행의 명령(`tmp=$(mktemp -d)`, 파일마다 `mkdir -p "$tmp/$(dirname f)" && mv f "$tmp/f"`, `mv "$tmp/f" f`, `rm -rf "$tmp"`)대로 옮김(` D pkg/a/__init__.py`, ` D pkg/b/__init__.py`) → 되살린 뒤 `git status --porcelain`이 시작과 같음, 내용 `A`·`B`. 본문 61행에 `git checkout HEAD -- <구현 파일>`로 되살리는 줄이 있고(`grep -c` → `1`), 한 파일을 지운 뒤 그 명령 → 시작과 같음. 통과
- 3. `STOP`의 글이 `STOP_COUNT`를 따른다
  - `plugins`·`tests`를 임시 폴더에 복사해 `sed 's/^STOP_COUNT = 3 /STOP_COUNT = 5 /'`로 바꾼 사본으로 시험 레포의 `src.py`를 다섯 번 편집 → 네 번 `TEST_FIRST` 글, 다섯 번째 `plate: 테스트 먼저 때문에 같은 파일을 다섯 번째 막았다`. 통과
- 4. 지우기만 한 phase 커밋의 시험이 있고 `--diff-filter=d`를 빼면 실패한다
  - `tests/test_edit_guard.py:491`에 `test_phase_commit_deleting_test_only_blocks`. 복사본에서 `"--diff-filter=d", sha`를 `sha`로 바꾼 사본(`grep -c 'diff-filter=d'` → `0`)에서 `python3 -B -m unittest tests.test_edit_guard` → `FAIL: test_phase_commit_deleting_test_only_blocks (tests.test_edit_guard.RerunTest)`, `Ran 69 tests`, `FAILED (failures=1)`. 통과
- 5. tasks 완료 조건 1, 2, 4, 6이 참이다 (HEAD `4bed15b`, 작업 트리 깨끗함)
  - tasks 1: `python3 -m unittest discover -s tests` → `Ran 250 tests`, `OK`. 통과
  - tasks 2(`docs/tasks/001-hook-fixes/plan.md` 완료 조건 1~8): 1: 적힌 그대로(`plan.md`를 커밋하지 않은 시험 레포)와 커밋한 꼴 모두 테스트를 바꾼 `001-a: phase 1`+`## 확인 1` → 종료 0, `src.py`만 바꾼 커밋 → 종료 2, 확인 절 없음 → 종료 2. 2: `printf '{' | python3 plugins/plate/hooks/edit_guard.py` → `plate: 편집 훅 안에서 예외가 나서…JSONDecodeError` 줄, `exit=2`. `phase-1.md`에 `\xff` → `plate:`(`UnicodeDecodeError`) 줄, 종료 2. 푸시 훅 `{"git push` → `exit=2`, `{"ls` → `exit=0`. 3: `.git/plate-test-first.json` 자리에 폴더 → `…같은 파일을 세 번째 막았다` 줄, 종료 2. `os.replace` 253행. 4: `tests/test_y.py`를 커밋해 두고 `git rm tests/test_x.py`만 → 종료 2. 5: `env PATH=/nonexistent /usr/bin/python3`(`command -v python3`)에서 `README.md` → 종료 0, `src.py` → `FileNotFoundError: … 'git'` 줄, 종료 2. `has_uncommitted_test_change(root)` 301행 < `has_tests(root)` 306행(`check` 264행 안). 6: `grep -c` → `0`, 상수 확인 → `True`. 7: ARCHITECTURE 54행("막는 장치" 문단)에 `다시 수행`·`예외`·`결과물인 마크다운` 모두, `### ADR-027` 63행 한 줄, PRD 4행(목표)·16행(핵심 기능 6)이 "코드 파일(`.md`가 아닌 파일)"로 좁힘. 8: 위 tasks 1과 같음. 모두 기대대로. 통과
  - tasks 4(`docs/tasks/003-skill-fixes/plan.md` 완료 조건 1~9): 1: `다시 띄움: 결과 없음` 293행("멈춘다" 285행~)·570행(`RUNLOG.md` 절 555행~), `test_no_result_relaunch_limit` `OK`. 2: `tasks 브랜치` 89행 < `계획의 커밋` 96행. 3: `gh api user` 376행("이슈를 올린다" 369행~)·519행("PR 본문의 꼴" 516행~), `gh api user --jq .login` → `werwer748`, `gh issue view 68 … --jq '.author.login'` → `werwer748`. 4: `test_stop_line_grep_runs_on_fake_runlog` `OK`. 5: `부모 커밋에 없` 59행("2. TODO를 차례로 끝낸다" 42행~), 시험 레포에서 바꾼 파일 `mod.py`(`cat-file` 0)는 `git checkout <커밋>^ --`/`git checkout HEAD --`, 새 파일 `pkg/new.py`(`cat-file` 128)는 본문 명령대로 옮겼다 되살림 → `git status --porcelain` 빈 출력. 6: review 72행("2. 잰다" 67행~ 커버리지 항목)에 `한 번`. 7: `맥락 문서를 모두 읽는다` 없음(종료 1), `결정 절` 99행("4. 2라운드" 90행~)·190행("2라운드에 맡기는 글" 172행~). 8: `결과 없` PRD 17행·ARCHITECTURE 40·99행, `gh api user` ARCHITECTURE 57행(run 이슈·PR 문단). 9: 위 tasks 1과 같음. 모두 기대대로. 통과
  - tasks 6: `python3 -m unittest tests.test_skill_rules tests.test_manifests tests.test_cleanup_skill tests.test_edit_guard tests.test_push_guard` → `OK`. `grep -n '^def section' tests/test_cleanup_skill.py` → 출력 없음(종료 1). 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 250 tests`, `OK`. 통과
- 테스트 먼저 기록: phase 1
  - `done-phase-1.md`의 "한 일" "테스트 먼저" → 첫 수행의 실패 출력(`ImportError: cannot import name 'ordinal'`, `FAILED (errors=1)`, `ordinal`만 끼운 실행의 `FAILED (failures=3)`) 뒤에 통과 출력(`Ran 64 tests`, `OK`), 고침의 실패 출력(`RerunTest`의 `FAILED (failures=3)`) 뒤에 통과 출력(`Ran 69 tests`, `OK`)이 이 순서로 있다. 통과

**남은 것**
- phase 1: 셈의 경계를 "그 task 머리를 마지막으로 더하거나 지운 커밋"으로 잡으므로, 이번 tasks 안에서 그 task 폴더를 지웠다 다시 더하면 그 앞의 같은 제목 커밋은 세지 않는다 → 문제 아님 (ARCHITECTURE "막는 장치" 문단이 "그 task 머리 `plan.md`를 마지막으로 더하거나 지운 커밋 뒤에서만 찾고"라고 약속한 꼴 그대로이고, run은 tasks 안에서 task 머리를 지우지 않는다. 결정·맥락 문서와 어긋나지 않는다)
- phase 1: task 머리를 커밋하지 않았고 지난 tasks가 같은 task 머리를 지우지 않고 끝났으면 경계가 지난 tasks의 계획 커밋이 되어 지난 tasks의 같은 제목 커밋을 센다 → 문제 아님 (ARCHITECTURE가 task 머리를 커밋하지 않은 꼴의 경계를 "지난 tasks를 비운 커밋"으로 정했고, 그 꼴은 지난 tasks가 `docs/tasks/`를 비우지 않은 경우로 약속 밖이다. 완료 조건 1의 시험 레포(지난 tasks를 비운 꼴)에서는 기대대로 돈다)

**문제**
- 없음

**판정**: 통과
