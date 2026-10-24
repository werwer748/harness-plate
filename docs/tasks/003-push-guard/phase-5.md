# Phase 5: 회고 4의 문제를 고친다

**목표**: 회고 4에서 나온 문제를 모두 고친다.

**테스트 먼저**: 예

**읽을 것**
- `docs/tasks/003-push-guard/retro.md`의 `## 회고 4` 절
- `plugins/plate/hooks/push_guard.py`
- `tests/test_push_guard.py`
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/ADR.md`
- `docs/TOOLS.md`

**TODO**
- [x] 명령 치환을 따로 읽는다(task 머리의 결정). 명령을 나눌 때 `$( … )`와 백틱 치환은 그 안에서 따옴표, 주석, heredoc을 새로 세고, 닫는 `)`나 백틱에서 바깥(바깥 큰따옴표 안이었으면 그 안)으로 돌아온다. 치환 안의 push는 읽지 않는다. `docs/ARCHITECTURE.md`의 막는 장치에도 적는다. 문제: `"$( … )"` 안의 큰따옴표 사이에 `#`이 있는 한 줄 명령 뒤에 `&&`나 `;`로 이은 push를 막지 않는다. `without_non_commands`(53~99줄)는 `"$( … )"` 안쪽의 `"`에서 바깥 따옴표가 닫힌다고 읽고, 그 뒤 낱말 첫머리의 `#`(69~72줄)를 주석으로 보아 줄 끝까지 지운다. 지운 글에 `"`가 짝수 개면 남은 글의 따옴표 짝이 맞아 `segments`(102~123줄)가 None이 아닌 목록을 돌려주므로 phase 4가 더한 나누지 못한 명령의 막음(`check` 259~260줄)에 걸리지 않고, 뒤의 push는 지워진 채 통과한다. `git commit -m "$(echo "fix #1")" && git push origin main`을 넣으니 `without_non_commands`는 `git commit -m "$(echo "fix `를, `segments`는 `[['git', 'commit', '-m', '$(echo fix']]`를 냈다. 스크래치에 로컬 bare origin과 문서 지도 구간이 있는 레포(`main`이 origin보다 한 커밋 앞서고 지금 브랜치는 `tasks/x`)를 만들고, 이 명령과 `echo "$(echo "fix #1")" && git push origin main`, `echo "$(git log -1 --format="%h #%s")"; git push origin main`을 훅에 넣고 같은 명령의 `git push`를 `git push --dry-run --porcelain`으로 바꿔 bash에 돌리니, 셋 다 지금의 훅에서 0이고 bash는 셋 다 `refs/heads/main:refs/heads/main`을 냈다. phase 1(`f8f219b`)과 phase 2(`5cdb2a0`)의 훅은 셋 다 2로 막았고 phase 3(`8c3673b`)의 훅부터 0이다. 회고 3의 셋째 문제와 같은 오독 위에서 주석 빼기가 따옴표 짝을 맞추는 꼴이다. push는 명령 치환이나 다른 명령 안이 아니라 `&&`·`;`로 이어진 명령이고 대상도 글로 적혀 있어, task 머리 결정의 한계에 들지 않는다. 안쪽 따옴표가 없는 `git commit --allow-empty -m "fix #1" && git push origin main`과 `echo "$(echo "a")" && git push origin main`은 지금도 2다 (`plugins/plate/hooks/push_guard.py`, `docs/ARCHITECTURE.md`)

**통과 조건**
- 회고 4의 문제가 모두 고쳐졌다.
  - 확인: 문제마다 적힌 곳을 다시 읽거나 돌린다
- 셋업된 프로젝트에서 기본 브랜치가 아닌 브랜치에 있을 때, 회고 4의 문제에 적힌 세 명령과 `git commit -m "$(cat <<'EOF'`(줄바꿈)`Keep "don't" wording`(줄바꿈)`EOF`(줄바꿈)`)" && git push origin main`, `git commit -m "$(cat <<'EOF'`(줄바꿈)`Close "issue #12" properly`(줄바꿈)`EOF`(줄바꿈)`)" && git push origin main`은 막히고, push가 없는 `git commit -m "$(cat <<'EOF'`(줄바꿈)`Keep "don't" push wording`(줄바꿈)`EOF`(줄바꿈)`)"`는 막히지 않는다. 막힌 명령의 까닭은 나누지 못한 명령의 글이 아니라 기본 브랜치로 가는 push의 글이다. task 머리의 결정에 적은 한계 안의 꼴은 이 phase의 통과를 가르지 않는다.
  - 확인: `tests/test_push_guard.py`에 이 명령마다 테스트가 있고, `python3 -m unittest discover -s tests`가 통과한다
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다

## 한 일
- 명령 치환을 따로 읽는다: `without_non_commands`의 몸을 `scan(command, i, closer)`로 옮겨, 따옴표 밖이거나 큰따옴표 안의 `$(`와 백틱을 만나면 그 뒤를 새 `scan`(따옴표, 주석, heredoc을 새로 센다)으로 읽고 닫는 `)`(`$((1+2))`나 서브셸의 괄호는 짝을 센다)나 다음 백틱에서 돌아오게 했다. 치환은 `SUBSTITUTION`(`$_`)으로 바꿔 안의 push를 읽지 않고, 바깥의 따옴표 상태는 그대로 두어 바깥 큰따옴표 안이었으면 그 안으로 돌아온다. 모듈 설명과 `segments`의 ValueError 주석(이제 `"$( … )"`가 아니라 `$'…'` 안의 `\'` 같은 꼴)도 고쳤다. 따옴표 밖의 `echo $(git push origin main)`은 전에는 괄호에서 나뉘어 막혔는데, task 머리의 결정대로 이제 치환 안이라 읽지 않는다. 서브셸 `(git push origin main)`은 치환이 아니라 그대로 막는다 (`plugins/plate/hooks/push_guard.py`). 막는 장치에 치환을 따로 세고 치환 안의 push는 읽지 않는다는 것을 더하고, 나누지 못하는 꼴의 예를 `$'…'` 안의 `\'`로 바꿨다 (`docs/ARCHITECTURE.md` 48줄). 시험은 `SUBSTITUTION_PUSHES`(회고 4의 세 명령, 통과 조건의 heredoc 두 명령, 백틱 안 따옴표 한 명령)를 `test_push_after_substitution_with_quotes`가 "`main`"과 `git push origin main`이 든 까닭으로 막고 "나누지 못했"이 없는지 보게 더했고, 치환 안 따옴표가 든 push 없는 명령(통과 조건의 `Keep "don't" push wording` 포함)을 `test_substitution_with_quotes_without_push`로 더했다. 이제 나눠 읽히는 옛 `UNSPLIT_PUSHES`는 셸은 짝을 맞추는데 훅은 못 맞추는 `echo $'it\'s' && git push origin main`과 따옴표가 닫히지 않은 `git commit -m "don't && git push origin main`으로 바꾸고, `test_unsplit_command_without_push`의 명령도 `echo $'it\'s' && git status`로 바꿨다 (`tests/test_push_guard.py`)
- 테스트 먼저
  - 실패: `python3 -m unittest discover -s tests` → `FAIL: test_push_after_substitution_with_quotes (test_push_guard.BlockTest.test_push_after_substitution_with_quotes) (command='git commit -m "$(cat <<\'EOF\'\nKeep "don\'t" wording\nEOF\n)" && git push origin main')`, 같은 시험의 `Close "issue #12" properly`, `git commit -m "$(echo "fix #1")" && git push origin main`, `echo "$(echo "fix #1")" && git push origin main`, `echo "$(git log -1 --format="%h #%s")"; git push origin main`, ``echo "`echo "it's"`" && git push origin main`` subTest, `FAIL: test_substitution_with_quotes_without_push (test_push_guard.PassTest.test_substitution_with_quotes_without_push) (command='git commit -m "$(cat <<\'EOF\'\nKeep "don\'t" push wording\nEOF\n)"')`, 같은 시험의 ``echo "`echo "it's"`" && git push origin tasks/x`` subTest / `Ran 89 tests in 33.345s` / `FAILED (failures=8)`
  - 통과: `python3 -m unittest discover -s tests` → `Ran 89 tests in 33.743s` / `OK`

## 확인 결과
- 회고 4의 문제가 모두 고쳐졌다.
  - 스크래치에 로컬 bare origin과 문서 지도 구간이 있는 `AGENTS.md`를 둔 레포(`main`이 origin보다 한 커밋 앞서고 지금 브랜치는 `tasks/x`)를 만들어 회고 4의 세 명령을 넣음 → `without_non_commands`는 `git commit -m "$_" && git push origin main`, `echo "$_" && git push origin main`, `echo "$_"; git push origin main`을, `segments`는 셋 다 `[…, ['git', 'push', 'origin', 'main']]`을 내고, 훅은 셋 다 종료 코드 2와 `plate: 기본 브랜치(`main`)로 푸시하지 않는다: `git push origin main``을 냈다. 같은 명령의 `git push`를 `git push --dry-run --porcelain`으로 바꿔(`git commit`에는 `--allow-empty`를 더해) bash에 돌림 → 셋 다 `refs/heads/main:refs/heads/main`. 안쪽 따옴표가 없는 `git commit --allow-empty -m "fix #1" && git push origin main`과 `echo "$(echo "a")" && git push origin main`도 2. 통과
- 셋업된 프로젝트에서 기본 브랜치가 아닌 브랜치에 있을 때, 회고 4의 문제에 적힌 세 명령과 heredoc 두 명령은 막히고, push가 없는 `Keep "don't" push wording` 명령은 막히지 않는다. 막힌 명령의 까닭은 기본 브랜치로 가는 push의 글이다.
  - `tests/test_push_guard.py`를 읽음 → 다섯 명령은 `SUBSTITUTION_PUSHES`(25~32줄)에 있고 `test_push_after_substitution_with_quotes`(211줄)가 `tasks/x` 브랜치에서 `assertBlocked(…, "`main`", "git push origin main")`과 `assertNotIn("나누지 못했", err)`로 본다. `Keep "don't" push wording` 명령은 `test_substitution_with_quotes_without_push`(363줄)가 `assertPassed`로 본다. 위의 스크래치 레포에서도 heredoc 두 명령은 2와 같은 BLOCK 글, `Keep "don't" push wording` 명령은 0이었다. `python3 -m unittest discover -s tests` → `Ran 89 tests in 34.540s` / `OK`. 통과
- task 머리의 완료 조건이 모두 참이다.
  - 완료 조건 1: `python3 -m unittest discover -s tests` → `Ran 89 tests in 34.540s` / `OK`. `tests/test_push_guard.py`를 읽음 → 대상 없는 push(`test_push_without_target_on_default_branch` 90줄, `test_push_head_while_on_default_branch` 118줄), 기본 브랜치를 가리키는 push(`test_push_to_default_branch` 102줄), 지우는 push(`test_delete_default_branch` 123줄의 `--delete`, `-d`, `:main`, `:refs/heads/main`), 이어진 명령 안의 push(`test_push_inside_chained_command` 198줄), `git -C`(`test_push_inside_git_c_uses_that_folder` 228줄, `test_git_c_folder_has_its_own_default_branch` 236줄), 다른 브랜치(`test_push_to_other_branch` 269줄), origin 밖 원격(`test_push_to_remote_other_than_origin` 300줄), 셋업 안 된 프로젝트(`test_project_not_set_up` 345줄)가 있다. `python3 -m unittest discover -s tests -p 'test_push_guard.py' -v` → `Ran 33 tests in 18.668s` / `OK`. 통과
  - 완료 조건 2: `python3 -c "import json; h=json.load(open('plugins/plate/hooks/hooks.json')); print([m['matcher'] for m in h['hooks']['PreToolUse']])"` → `['Edit|Write|MultiEdit|NotebookEdit', 'Bash']`. `plugins/plate/hooks/hooks.json` 9줄과 18줄을 읽음 → 18줄은 `f="${CLAUDE_PLUGIN_ROOT}/hooks/push_guard.py"; [ -f "$f" ] || exit 0; exec python3 "$f"`로 9줄의 편집 훅과 스크립트 이름만 다르다. 그 명령을 `CLAUDE_PLUGIN_ROOT=/nonexistent sh -c`로 돌림 → 종료 코드 0. 통과
  - 완료 조건 3: `docs/PRD.md` 4줄(목표)과 `docs/ARCHITECTURE.md` 5줄(기술 스택), 19·21·34줄(디렉터리 구조), 48줄(막는 장치)을 읽음 → PRD 목표에 "에이전트가 기본 브랜치에 하는 푸시", 기술 스택에 `push_guard.py`, 디렉터리 구조에 hooks.json의 Bash 항목과 `push_guard.py`, `test_push_guard.py`, 막는 장치에 푸시 훅이 막는 것, 막지 않는 것, 명령 치환을 따로 세는 것, 셸 구문의 한계, 나누지 못한 명령의 막음이 있다. 통과
  - 완료 조건 4: `python3 -m unittest discover -s tests` → `OK`(위와 같다). `git diff --stat 5a7c002 HEAD -- tests/test_verdict.py plugins/plate/ci/`(`5a7c002`는 `002-ci-workflow: 회고`)와 `git diff --stat -- tests/test_verdict.py plugins/plate/ci/` → 둘 다 출력 없음. `python3 -m unittest discover -s tests -p 'test_verdict.py'` → `Ran 14 tests in 0.737s` / `OK`. 통과

## 계획과 달라진 점
- 없음

## 남은 것
- 없음

## 하네스에서 걸린 것
- 없음
