# 편집 훅과 푸시 훅의 발견을 고친다

## 목표
정리 점검 2026-10-29의 신뢰성-1·4·5·10, 성능-5·6, 유지보수성-5를 편집 훅(`plugins/plate/hooks/edit_guard.py`)과 푸시 훅(`plugins/plate/hooks/push_guard.py`)에서 고치고, 기능 적합성-2의 결정(결과물인 마크다운을 훅이 막지 않는다)을 맥락 문서에 적는다.

## 범위 밖
- 결과물인 마크다운을 편집 훅이 코드로 치는 것.
- 푸시 훅이 약속하는 셸 구문의 꼴을 넓히는 것(`docs/ARCHITECTURE.md`의 "막는 장치" 문단이 정한 대로 둔다).
- 훅을 끄는 스위치.

## 완료 조건
아래 "시험 레포"는 `mktemp -d`로 만든 git 레포다: `AGENTS.md`에 `<!-- plate:docs-map:start -->` 줄이 있고, `tests/test_x.py`와 `src.py`가 커밋돼 있고, `docs/tasks/001-a/plan.md`와 `**테스트 먼저**: 예` 줄을 둔 `docs/tasks/001-a/phase-1.md`가 있다. 편집 훅에는 `{"tool_input": {"file_path": "<파일>"}, "cwd": "<시험 레포>"}`를 stdin으로 넣고 종료 코드를 본다.

1. 다시 수행하는 테스트 먼저 phase(`phase-1.md`에 `## 확인 1` 절이 있다)에서, 커밋하지 않은 테스트 변경이 없어도 그 phase의 커밋(제목 `001-a: phase 1`)이 테스트 파일을 바꿨으면 구현 편집을 통과시키고, 그 커밋이 테스트 파일을 바꾸지 않았으면 막는다(신뢰성-1).
   - 확인: 시험 레포에서 `tests/test_x.py`를 고친 `001-a: phase 1` 커밋과 `## 확인 1` 절을 두고 `src.py` 편집 → 종료 0. 그 커밋이 `src.py`만 바꾼 레포 → 종료 2. `## 확인 1` 절이 없는 레포(첫 수행) → 종료 2
2. 훅 안에서 예외가 나면 두 훅 모두 까닭을 stderr에 낸다. 편집 훅은 종료 2로 막는다. 푸시 훅은 stdin의 글에 `push`가 있으면 종료 2로 막고, 없으면 종료 0으로 통과시킨다(신뢰성-4).
   - 확인: `printf '{' | python3 plugins/plate/hooks/edit_guard.py; echo "exit=$?"` → stderr에 `plate:`로 시작하는 줄, `exit=2`
   - 확인: 시험 레포의 `phase-1.md`에 UTF-8이 아닌 바이트(`printf '\xff' >>`)를 더하고 `src.py` 편집 → stderr에 `plate:` 줄, 종료 2
   - 확인: `printf '{"git push' | python3 plugins/plate/hooks/push_guard.py; echo "exit=$?"` → `exit=2`. `printf '{"ls' | python3 plugins/plate/hooks/push_guard.py; echo "exit=$?"` → `exit=0`
3. 막은 횟수를 세는 파일은 임시 파일에 쓴 뒤 바꿔 넣고, 쓰기에 실패하면 세 번째 막음의 글(STOP)을 낸다(신뢰성-5).
   - 확인: 시험 레포의 `.git/plate-test-first.json` 자리에 폴더를 만들고 `src.py` 편집 → stderr에 `세 번째`가 든 줄, 종료 2
   - 확인: `grep -n 'os.replace' plugins/plate/hooks/edit_guard.py` → 한 줄 이상
4. 상태가 삭제뿐인 테스트 파일은 테스트 변경으로 세지 않는다(신뢰성-10).
   - 확인: 시험 레포에서 `git rm tests/test_x.py`만 한 뒤(`tests/test_y.py`는 커밋돼 남아 있다) `src.py` 편집 → 종료 2
5. `.md` 편집은 git을 부르기 전에 통과시키고(`docs/tasks/` 아래도 그대로 통과), 테스트 먼저 검사는 커밋하지 않은 테스트 변경을 `git ls-files` 훑기보다 먼저 본다(성능-5·6).
   - 확인: `command -v python3`로 얻은 경로를 써서 `env PATH=/nonexistent <python3 경로> plugins/plate/hooks/edit_guard.py`에 시험 레포의 `README.md` 편집 JSON → 종료 0, `src.py` 편집 JSON → 종료 2(git이 없어 예외로 막는다)
   - 확인: `grep -n -e 'has_uncommitted_test_change(root)' -e 'has_tests(root)' plugins/plate/hooks/edit_guard.py` → `check` 함수 안에서 `has_uncommitted_test_change`의 줄이 `has_tests`의 줄보다 앞선다
6. 테스트 먼저로 막을 때의 글(`TEST_FIRST`)의 테스트 파일 줄이 `TEST_DIRS`와 `TEST_NAMES`에서 만들어진다(유지보수성-5).
   - 확인: `grep -c -F '`test_*`, `*_test.*`' plugins/plate/hooks/edit_guard.py` → `0`
   - 확인: `python3 -c "import sys; sys.path.insert(0, 'plugins/plate/hooks'); import edit_guard as g; print(all(n in g.TEST_FIRST for n in g.TEST_NAMES) and all(d in g.TEST_FIRST for d in g.TEST_DIRS))"` → `True`
7. 맥락 문서가 바뀐 동작과 맞다: `docs/ARCHITECTURE.md`의 "패턴과 규칙" 절의 "막는 장치" 문단이 다시 수행의 테스트 셈, 두 훅의 예외 처리, 결과물인 마크다운을 막지 않는다는 것을 적고, `docs/ADR.md`에 그 결정의 항목이 있고, `docs/PRD.md`의 목표 절과 핵심 기능 6이 "계획 없는 편집"을 코드 파일의 편집으로 좁힌다.
   - 확인: `grep -n -e '다시 수행' -e '예외' -e '결과물인 마크다운' docs/ARCHITECTURE.md` → "막는 장치" 문단에 셋 다 있다
   - 확인: `grep -n '^### ADR-027' docs/ADR.md` → 한 줄
   - 확인: `docs/PRD.md`의 목표 절과 핵심 기능 6을 읽어, 훅이 막는 편집이 코드 파일(`.md`가 아닌 파일)의 편집이라고 적혀 있다
8. 테스트 묶음이 모두 통과한다.
   - 확인: `python3 -m unittest discover -s tests` → 마지막 줄이 `OK`

## 결정
- 다시 수행은 `phase-N.md`에 `## 확인 N` 절이 있는 것으로 가르고, 그 phase의 커밋은 제목이 `NNN-slug: phase N`인 커밋이다. 이유: 첫 수행에서 지킨 테스트 먼저를 근거로 두고, 테스트 없이 커밋된 phase는 여전히 막는다.
- 훅 안의 예외에서 편집 훅은 막고, 푸시 훅은 stdin의 글에 `push`가 있을 때만 막는다. 둘 다 까닭을 stderr에 낸다. 이유: 막아야 할 때 조용히 통과시키지 않으면서, 푸시 훅 오류 하나로 모든 셸 명령이 막히는 것은 피한다.
- 결과물인 마크다운도 편집 훅은 막지 않고 규칙 구간이 막는다. 이유: 008-tdd의 결정(`git show 444fa84:docs/tasks/008-tdd/plan.md`의 "코드 파일은 `.md`가 아니고…")과 `tests/test_edit_guard.py`의 `.md` 시험을 뒤집지 않고, 훅이 대상 프로젝트마다 ARCHITECTURE를 읽을 필요가 없다.
