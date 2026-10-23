# Phase 3: 회고 2의 문제를 고친다

**목표**: 회고 2에서 나온 문제를 모두 고친다.

**테스트 먼저**: 예

**읽을 것**
- `docs/tasks/003-push-guard/retro.md`의 `## 회고 2` 절
- `plugins/plate/hooks/push_guard.py`
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/ADR.md`
- `docs/TOOLS.md`

**TODO**
- [x] 줄 잇기(`\` 바로 뒤의 줄바꿈)를 명령의 경계로 읽는다. 셸은 `\`+줄바꿈을 지우고 한 명령으로 잇는데, `lexer`(39~44줄)는 그것을 줄바꿈 낱말 하나로 내고 `segments`(95줄)가 `SEPARATORS`에 든 낱말로 보아 명령을 나눈다. `segments('git push \\\n  origin main')`이 `[['git', 'push'], ['origin', 'main']]`을 냈다. 스크래치에 로컬 bare origin과 문서 지도 구간이 있는 레포를 만들고 `main`을 origin보다 한 커밋 앞서게 한 뒤, `tasks/x`에서 `git push \`(줄바꿈)`  origin main`을 훅에 넣으니 종료 코드 0이었고 같은 명령을 `git push --dry-run --porcelain`으로 bash에 돌리니 `refs/heads/main:refs/heads/main`이 나왔다. 거꾸로 `main`에서 `git push \`(줄바꿈)`  origin tasks/x`는 origin의 `main`을 바꾸지 않는데 종료 코드 2로 막았다 (`plugins/plate/hooks/push_guard.py`)
- [x] `#` 주석을 명령의 글로 읽는다. `lexer`가 `lex.commenters = ""`(43줄)로 주석을 두지 않고 `without_heredocs`(47~82줄)도 주석 안의 따옴표를 센다. 그래서 주석에 짝 없는 따옴표가 있으면 `lexer`가 `ValueError`를 내고 `segments`(89~90줄)가 빈 목록을 돌려 명령 전체를 통과시킨다. 같은 스크래치의 `tasks/x`에서 `# push it (it's ready)`(줄바꿈)`git push origin main`과 `echo "it's" # don't`(줄바꿈)`git push origin main`을 훅에 넣으니 둘 다 종료 코드 0이었고, bash의 `--dry-run --porcelain`은 둘 다 `refs/heads/main:refs/heads/main`을 냈다. 거꾸로 `echo hi # ; git push origin main`은 셸이 `#` 뒤를 주석으로 버려 푸시하지 않는데 종료 코드 2로 막았다 (`plugins/plate/hooks/push_guard.py`)

**통과 조건**
- 회고 2의 문제가 모두 고쳐졌다.
  - 확인: 문제마다 적힌 곳을 다시 읽거나 돌린다
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다

## 한 일
- 줄 잇기(`\` 바로 뒤의 줄바꿈)를 명령의 경계로 읽는다: `without_heredocs`(이제 `without_non_commands`)가 따옴표 밖과 큰따옴표 안의 `\`+줄바꿈을 셸처럼 지워 앞뒤를 한 명령으로 잇는다. 작은따옴표 안의 `\`는 그대로 둔다. 시험: `test_push_across_line_continuation`(3꼴, `tasks/x`에서 막음), `test_line_continuation_is_one_command`(2꼴, `main`에서 다른 브랜치로 가는 push를 통과) (`plugins/plate/hooks/push_guard.py`, `tests/test_push_guard.py`)
- `#` 주석을 명령의 글로 읽는다: 같은 함수가 따옴표 밖에서 낱말의 첫 글자인 `#`(입력의 처음, 빈칸·탭·줄바꿈·`;&|()<>` 뒤, `<<` 뒤)부터 줄 끝까지를 뺀다. 줄바꿈은 남겨 다음 줄을 새 명령으로, `<<`가 있는 줄의 주석 뒤를 heredoc 본문의 시작으로 읽는다. 낱말 가운데의 `#`(`a#b`, `$#`)과 따옴표 안의 `#`은 주석으로 보지 않는다. 주석을 빼므로 주석 안의 짝 없는 따옴표가 `ValueError`를 내지 않는다. `lexer`의 `commenters`는 그대로 `""`다(shlex의 주석은 낱말 가운데의 `#`도 주석으로 보고 줄바꿈까지 먹는다). 함수가 heredoc 밖의 것도 빼게 되어 이름을 `without_non_commands`로 바꾸고, 모듈과 `segments`의 docstring에 주석과 줄 잇기를 적었다. 시험: `test_push_after_comment`(6꼴), `test_comment_is_not_a_command`(4꼴) (`plugins/plate/hooks/push_guard.py`, `tests/test_push_guard.py`)
- 테스트 먼저
  - 실패: `python3 -m unittest discover -s tests` → `FAIL: test_push_across_line_continuation (test_push_guard.BlockTest.test_push_across_line_continuation) (command='git push \\\n  origin main')`, `FAIL: test_push_across_line_continuation (test_push_guard.BlockTest.test_push_across_line_continuation) (command='git push origin \\\n  main')`, `FAIL: test_push_after_comment (test_push_guard.BlockTest.test_push_after_comment) (command="# push it (it's ready)\ngit push origin main")`, `FAIL: test_push_after_comment (test_push_guard.BlockTest.test_push_after_comment) (command='echo "it\'s" # don\'t\ngit push origin main')`, `FAIL: test_comment_is_not_a_command (test_push_guard.PassTest.test_comment_is_not_a_command) (command='echo hi # ; git push origin main')`, `FAIL: test_comment_is_not_a_command (test_push_guard.PassTest.test_comment_is_not_a_command) (command='git status # && git push origin main')`, `FAIL: test_line_continuation_is_one_command (test_push_guard.PassTest.test_line_continuation_is_one_command) (command='git push \\\n  origin tasks/x')`, `FAIL: test_line_continuation_is_one_command (test_push_guard.PassTest.test_line_continuation_is_one_command) (command='git push -u \\\n  origin HEAD:tasks/x')`, `Ran 84 tests in 33.904s` / `FAILED (failures=8)`
  - 통과: `python3 -m unittest discover -s tests` → `Ran 84 tests in 32.088s` / `OK`

## 확인 결과
- 회고 2의 문제가 모두 고쳐졌다.
  - 스크래치(`/private/tmp/claude-501/-Users-gangjungi-Desktop-harness-plate/3eef7c5c-5f6a-4ba3-b7e6-8c6c3309866e/scratchpad/p3`)에 로컬 bare origin과 문서 지도 구간이 있는 레포를 만들고 `main`을 origin보다 한 커밋 앞서게 한 뒤, 회고의 다섯 명령을 훅에 넣고 같은 명령을 `git push --dry-run --porcelain`으로 bash에 돌림 → `tasks/x`의 `git push \`(줄바꿈)`  origin main`: 훅 2, bash `refs/heads/main:refs/heads/main`. `main`의 `git push \`(줄바꿈)`  origin tasks/x`: 훅 0, bash `refs/heads/tasks/x:refs/heads/tasks/x`. `tasks/x`의 `# push it (it's ready)`(줄바꿈)`git push origin main`과 `echo "it's" # don't`(줄바꿈)`git push origin main`: 둘 다 훅 2, bash `refs/heads/main:refs/heads/main`. `tasks/x`의 `echo hi # ; git push origin main`: 훅 0, bash는 push하지 않음. 다섯 모두 훅의 판단이 bash의 실제 push와 맞다. 통과
- task 머리의 완료 조건이 모두 참이다.
  - 완료 조건 1: `python3 -m unittest discover -s tests` → `Ran 84 tests in 32.088s` / `OK`. `tests/test_push_guard.py`를 읽음 → 대상 없이 하는 push(74, 102줄), 기본 브랜치를 가리키는 push(86줄), 지우는 push(107줄의 `--delete`, `-d`, `:main`, `:refs/heads/main`), 이어진 명령 안의 push(182줄), `git -C` 안의 push와 그 폴더의 기본 브랜치(195, 203줄), 다른 브랜치(236줄), origin 밖 원격(267줄), 셋업 안 된 프로젝트(312줄)의 시험이 있다. 통과
  - 완료 조건 2: `python3 -c "import json; h=json.load(open('plugins/plate/hooks/hooks.json')); print([m['matcher'] for m in h['hooks']['PreToolUse']])"` → `['Edit|Write|MultiEdit|NotebookEdit', 'Bash']`. `plugins/plate/hooks/hooks.json` 18줄을 읽음 → `f="${CLAUDE_PLUGIN_ROOT}/hooks/push_guard.py"; [ -f "$f" ] || exit 0; exec python3 "$f"`로 9줄의 편집 훅과 스크립트 이름만 다르다. 그 명령을 `CLAUDE_PLUGIN_ROOT=/nonexistent`로 `sh -c`에 돌림 → 종료 코드 0. 통과
  - 완료 조건 3: `docs/PRD.md`의 목표(4줄), `docs/ARCHITECTURE.md`의 기술 스택(5줄), 디렉터리 구조(19, 21, 34줄), 막는 장치(48줄)를 읽음 → 모두 푸시 훅을 적고 있다. 이 phase는 두 문서를 바꾸지 않았고, 48줄의 "`&&`, `||`, `;`, `|`, 줄바꿈으로 나눠"는 줄 잇기와 주석을 고친 뒤에도 맞다. 통과
  - 완료 조건 4: `python3 -m unittest discover -s tests` → `OK`(위와 같다). `git diff --stat 5a7c002 -- tests/test_verdict.py plugins/plate/ci/` → 출력 없음. `python3 -m unittest discover -s tests -p 'test_verdict.py'` → `Ran 14 tests` / `OK`. 통과

## 계획과 달라진 점
- TODO는 `without_heredocs`(47~82줄)를 문제가 난 자리로만 적었다. 고치면서 그 함수가 주석과 줄 잇기도 빼게 되어 이름을 `without_non_commands`로 바꿨다. 이름이 하는 일과 맞지 않으면 다음에 읽는 쪽이 heredoc만 다루는 줄로 알기 때문이다. 이 함수를 부르는 곳은 `segments` 하나뿐이다.

## 남은 것
없음

## 하네스에서 걸린 것
없음
