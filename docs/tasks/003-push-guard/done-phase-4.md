# Phase 4: 회고 3의 문제를 고친다

**목표**: 회고 3에서 나온 문제를 모두 고친다.

**테스트 먼저**: 예

**읽을 것**
- `docs/tasks/003-push-guard/retro.md`의 `## 회고 3` 절
- `plugins/plate/hooks/push_guard.py`
- `tests/test_push_guard.py`
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/ADR.md`
- `docs/TOOLS.md`

**TODO**
- [x] 훅을 고치지 않고 한계로 적는다(task 머리의 결정). `docs/ARCHITECTURE.md`의 막는 장치에, 푸시 훅은 같은 호출에서 `cd`·`pushd` 뒤에 하는 push를 호출한 폴더에서 본다고 적는다. 문제: `cd <폴더> &&`(또는 `;`) 뒤의 push를 그 폴더가 아니라 호출의 `cwd`에서 본다. `check`(239~249줄)는 호출의 `cwd`를 모든 단순 명령에 넘기고, `push_call`(120~139줄)은 `git -C`에서만 폴더를 바꾼다. 스크래치에 로컬 bare origin과 문서 지도 구간이 있는 레포 `proj`(`main`이 origin보다 앞서고 지금 브랜치는 `tasks/x`), 셋업 안 된 레포 `other`(`main`이 그 origin보다 앞선다), git 레포가 아닌 폴더 `plain`을 만들고, 명령마다 훅의 종료 코드와 같은 명령의 `git push`를 `git push --dry-run --porcelain`으로 바꿔 bash에 돌린 결과를 견줬다. `cwd`가 `plain`일 때 `cd <proj> && git push origin main`, `cd <proj> && git push origin HEAD:main`, `cd <proj>; git push origin :main`은 셋 다 훅 0이고 bash는 `refs/heads/main`을 바꾸거나 지웠다(`refs/heads/main:refs/heads/main`, `HEAD:refs/heads/main`, `:refs/heads/main [deleted]`). 거꾸로 `cwd`가 `proj`일 때 `cd <other> && git push origin main`은 셋업 안 된 프로젝트의 푸시인데 훅이 2로 막았다 (`plugins/plate/hooks/push_guard.py`, `docs/ARCHITECTURE.md`)
- [x] 훅을 고치지 않고 한계로 적는다(task 머리의 결정). `docs/ARCHITECTURE.md`의 막는 장치에, 푸시 훅은 명령 치환이나 변수로 적은 대상과 `sh -c`·`eval`처럼 다른 명령이 감싼 push를 읽지 않는다고 적는다. 문제: 기본 브랜치에 있는 채 명령 치환으로 지금 브랜치를 적은 push를 막지 않는다. `target_refs`(201~211줄)는 `HEAD`, `@`만 지금 브랜치로 바꾸고, 따옴표 안의 `"$(git branch --show-current)"`는 그 글 그대로 `refs/heads/$(git branch --show-current)`로 본다. 따옴표가 없으면 `segments`가 `(`에서 명령을 나눠 대상이 `$`가 된다. 같은 스크래치의 `proj`를 `main`에 두고 `git push -u origin "$(git branch --show-current)"`와 `git push -u origin $(git rev-parse --abbrev-ref HEAD)`를 넣으니 둘 다 훅 0이었고 bash는 둘 다 `refs/heads/main:refs/heads/main`을 냈다. 같은 자리의 `git push origin HEAD`는 훅이 2로 막는다(`test_push_head_while_on_default_branch`도 같다) (`plugins/plate/hooks/push_guard.py`, `docs/ARCHITECTURE.md`)
- [x] 나누지 못한 명령을 막는다(task 머리의 결정). 따옴표가 어긋나 명령을 나누지 못하면, 호출한 폴더가 셋업된 프로젝트이고 명령의 글에 `push`가 있을 때 막고, push를 다른 명령과 잇지 말고 따로 하라고 알린다. `docs/ARCHITECTURE.md`의 막는 장치에도 적는다. 문제: `"$( … )"` 안의 큰따옴표를 바깥 큰따옴표의 끝으로 읽어, 그 뒤의 따옴표가 어긋나면 명령 전체를 통과시킨다. 셸은 큰따옴표 안의 `$(`부터 따옴표를 새로 세는데 `without_non_commands`(48~94줄)와 `lexer`(40~45줄)는 안쪽의 `"`에서 바깥 따옴표를 닫는다. 그래서 `git commit -m "$(cat <<'EOF'`(줄바꿈)`Keep "don't" wording`(줄바꿈)`EOF`(줄바꿈)`)" && git push origin main`은 `don't`의 `'`가 닫히지 않은 따옴표로 읽혀 `segments`(99~102줄)가 빈 목록을 돌려준다. phase 3이 더한 주석 빼기는 같은 어긋남 위에서 `Close "issue #12" properly`의 `#12" properly`를 주석으로 지워 바깥 따옴표를 닫히지 않게 만들고, 같은 빈 목록이 된다(`without_non_commands`의 출력에서 `#12" properly`가 빠진 것을 봤다). 같은 스크래치의 `tasks/x`에서 두 명령은 지금의 훅에서 0이고 bash는 둘 다 `refs/heads/main:refs/heads/main`을 냈다. phase 1(`f8f219b`)과 phase 2(`5cdb2a0`)의 `push_guard.py`에 같은 명령을 넣으니 `issue #12` 쪽은 2로 막았고 `don't` 쪽은 0이었다. 안쪽 따옴표가 없는 `Fix #12`, 짝이 맞고 `#`·`'`가 없는 `Rename "foo" to "bar"`는 지금도 2다 (`plugins/plate/hooks/push_guard.py`, `docs/ARCHITECTURE.md`)

**통과 조건**
- 회고 3의 문제가 모두 고쳐졌다. 첫째와 둘째 문제는 `docs/ARCHITECTURE.md`의 막는 장치에 한계로 적힌 것이 고친 것이다.
  - 확인: 문제마다 적힌 곳을 다시 읽거나 돌린다
- 나누지 못한 명령은 셋업된 프로젝트에서 글에 `push`가 있으면 막히고, 셋업 안 된 프로젝트에서는 막히지 않는다. task 머리의 결정에 적은 한계 안의 꼴(같은 호출의 `cd`·`pushd` 뒤의 push, 명령 치환이나 변수로 적은 대상, 다른 명령이 감싼 push)은 이 phase의 통과를 가르지 않는다.
  - 확인: `tests/test_push_guard.py`에 회고 3의 셋째 문제의 두 명령이 막히는 테스트와 셋업 안 된 프로젝트에서 나누지 못한 명령이 막히지 않는 테스트가 있고, `python3 -m unittest discover -s tests`가 통과한다
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다

## 한 일
- 훅을 고치지 않고 한계로 적는다(첫째, `cd`·`pushd` 뒤의 push): `docs/ARCHITECTURE.md`의 막는 장치(48줄)에 "푸시 훅은 셸 구문을 모두 읽지 않는다. 같은 호출에서 `cd`·`pushd` 뒤에 하는 push는 호출한 폴더에서 보고"를 더했다. 훅은 고치지 않았다 (`docs/ARCHITECTURE.md`)
- 훅을 고치지 않고 한계로 적는다(둘째, 명령 치환·변수·감싼 push): 같은 자리에 "명령 치환이나 변수로 적은 대상과 `sh -c`·`eval`처럼 다른 명령이 감싼 push는 읽지 않는다"를 더했다. 훅은 고치지 않았다 (`docs/ARCHITECTURE.md`)
- 나누지 못한 명령을 막는다: `segments`가 따옴표가 어긋나 나누지 못하면 빈 목록 대신 None을 돌려주고, `check`는 None이면 명령의 글에 `push`가 있고 호출한 폴더(`cwd`)가 셋업된 프로젝트일 때 새 글 `UNSPLIT`("push를 다른 명령과 잇지 말고 따로 부른다")으로 막는다. 셋업된 프로젝트인지는 `blocked_branch`에 있던 세 줄을 `setup_root`로 빼 둘이 함께 쓴다. 모듈 docstring에 한 줄을 더했다. `docs/ARCHITECTURE.md`의 막는 장치에 "따옴표가 어긋나 명령을 나누지 못하면(셸은 짝을 맞추는 `"$( … )"` 안의 큰따옴표도 든다) 호출한 폴더가 셋업된 프로젝트이고 명령의 글에 `push`가 있을 때 막고, push를 다른 명령과 잇지 말고 따로 하라고 알린다"를 더했다. 테스트는 회고 3의 셋째 문제의 두 명령(`UNSPLIT_PUSHES`)이 셋업된 프로젝트의 `tasks/x`에서 막히고 글에 "따로"가 있는 것(`test_unsplit_command_with_push`), 셋업 안 된 프로젝트에서 막히지 않는 것(`test_unsplit_command_in_project_not_set_up`), 셋업된 프로젝트에서도 글에 `push`가 없으면 막히지 않는 것(`test_unsplit_command_without_push`)을 더했다 (`plugins/plate/hooks/push_guard.py`, `tests/test_push_guard.py`, `docs/ARCHITECTURE.md`)
- 테스트 먼저
  - 실패: `python3 -m unittest discover -s tests` → `FAIL: test_unsplit_command_with_push (test_push_guard.BlockTest.test_unsplit_command_with_push) (command='git commit -m "$(cat <<\'EOF\'\nKeep "don\'t" wording\nEOF\n)" && git push origin main')`, `FAIL: test_unsplit_command_with_push (test_push_guard.BlockTest.test_unsplit_command_with_push) (command='git commit -m "$(cat <<\'EOF\'\nClose "issue #12" properly\nEOF\n)" && git push origin main')`, `Ran 87 tests in 32.380s` / `FAILED (failures=2)`. 더한 두 통과 시험은 지금의 동작을 지키는 시험이라 처음부터 통과했다
  - 통과: `python3 -m unittest discover -s tests` → `Ran 87 tests in 33.222s` / `OK`

## 확인 결과
- 회고 3의 문제가 모두 고쳐졌다. 첫째와 둘째 문제는 `docs/ARCHITECTURE.md`의 막는 장치에 한계로 적힌 것이 고친 것이다.
  - 첫째: `docs/ARCHITECTURE.md` 48줄을 읽음 → "같은 호출에서 `cd`·`pushd` 뒤에 하는 push는 호출한 폴더에서 보고"가 있다. 통과
  - 둘째: 같은 줄 → "명령 치환이나 변수로 적은 대상과 `sh -c`·`eval`처럼 다른 명령이 감싼 push는 읽지 않는다"가 있다. 통과
  - 셋째: 스크래치에 로컬 bare origin과 문서 지도 구간이 있는 레포 `proj`(`main`이 origin보다 앞서고 지금 브랜치는 `tasks/x`), 셋업 안 된 레포 `other`(같은 꼴)를 만들고 훅의 종료 코드와 `git push`를 `git push --dry-run --porcelain`으로 바꿔 bash에 돌린 결과를 견줌 → `proj`에서 `don't` 쪽과 `issue #12` 쪽(커밋에 `--allow-empty`를 붙인 꼴)은 훅 2와 stderr "plate: 따옴표의 짝을 맞추지 못해 명령을 나누지 못했고, …" / "push를 다른 명령과 잇지 말고 따로 부른다."이고, bash는 둘 다 `refs/heads/main:refs/heads/main	db634b0..37460eb`를 냈다. `Fix #12`와 `Rename "foo" to "bar"`는 그대로 훅 2(stderr "plate: 기본 브랜치(`main`)로 푸시하지 않는다"). `other`에서 두 명령은 훅 0, `proj`에서 push가 없는 `don't` 쪽 커밋 명령은 훅 0. 통과
- 나누지 못한 명령은 셋업된 프로젝트에서 글에 `push`가 있으면 막히고, 셋업 안 된 프로젝트에서는 막히지 않는다.
  - `tests/test_push_guard.py`를 읽음 → 두 명령(`UNSPLIT_PUSHES` 25줄)이 막히는 `test_unsplit_command_with_push`(201줄), 셋업 안 된 프로젝트에서 막히지 않는 `test_unsplit_command_in_project_not_set_up`(332줄)이 있다. `python3 -m unittest discover -s tests` → `Ran 87 tests in 32.780s` / `OK`. 통과
- task 머리의 완료 조건이 모두 참이다.
  - 완료 조건 1: `python3 -m unittest discover -s tests` → `Ran 87 tests in 32.780s` / `OK`. `tests/test_push_guard.py`를 읽음 → 대상 없이 하는 push(`test_push_without_target_on_default_branch` 80줄, `test_push_head_while_on_default_branch` 108줄), 기본 브랜치를 가리키는 push(`test_push_to_default_branch` 92줄), 지우는 push(`test_delete_default_branch` 113줄의 `--delete`, `-d`, `:main`, `:refs/heads/main`), 이어진 명령 안의 push(`test_push_inside_chained_command` 188줄), `git -C` 안의 push(`test_push_inside_git_c_uses_that_folder` 209줄, `test_git_c_folder_has_its_own_default_branch` 217줄), 다른 브랜치(`test_push_to_other_branch` 250줄), origin 밖 원격(`test_push_to_remote_other_than_origin` 281줄), 셋업 안 된 프로젝트(`test_project_not_set_up` 326줄)가 있다. `python3 -m unittest discover -s tests -p 'test_push_guard.py' -v` → `Ran 31 tests in 17.403s` / `OK`. 통과
  - 완료 조건 2: `python3 -c "import json; h=json.load(open('plugins/plate/hooks/hooks.json')); print([m['matcher'] for m in h['hooks']['PreToolUse']])"` → `['Edit|Write|MultiEdit|NotebookEdit', 'Bash']`. `plugins/plate/hooks/hooks.json` 9줄과 18줄을 읽음 → Bash 항목은 `f="${CLAUDE_PLUGIN_ROOT}/hooks/push_guard.py"; [ -f "$f" ] || exit 0; exec python3 "$f"`로 편집 훅과 스크립트 이름만 다르다. 그 명령을 `CLAUDE_PLUGIN_ROOT=/nonexistent sh -c`로 돌림 → 종료 코드 0. 통과
  - 완료 조건 3: `docs/PRD.md` 4줄(목표)에 "에이전트가 기본 브랜치에 하는 푸시", `docs/ARCHITECTURE.md`의 기술 스택(5줄)에 푸시 훅 `push_guard.py`, 디렉터리 구조(19, 21, 34줄)에 hooks.json의 Bash 항목과 `push_guard.py`, `test_push_guard.py`, 막는 장치(48줄)에 푸시 훅이 막는 것, 막지 않는 것, 한계, 나누지 못한 명령의 막음이 적혀 있다. 통과
  - 완료 조건 4: `python3 -m unittest discover -s tests` → `OK`(위와 같다). `git diff --stat f8f219b^ -- tests/test_verdict.py plugins/plate/ci/`(`f8f219b^`는 `5a7c002`) → 출력 없음. `python3 -m unittest discover -s tests -p 'test_verdict.py'` → `Ran 14 tests in 0.760s` / `OK`. 통과

## 계획과 달라진 점
- 없음

## 남은 것
- 없음

## 하네스에서 걸린 것
- 없음

## 확인 1

**통과 조건**
- 회고 3의 문제가 모두 고쳐졌다. 첫째와 둘째 문제는 `docs/ARCHITECTURE.md`의 막는 장치에 한계로 적힌 것이 고친 것이다.
  - 첫째(`cd`·`pushd` 뒤의 push): `docs/ARCHITECTURE.md` 48줄(막는 장치)을 읽음 → "푸시 훅은 셸 구문을 모두 읽지 않는다. 같은 호출에서 `cd`·`pushd` 뒤에 하는 push는 호출한 폴더에서 보고"가 있다. 통과
  - 둘째(명령 치환·변수·감싼 push): 같은 줄 → "명령 치환이나 변수로 적은 대상과 `sh -c`·`eval`처럼 다른 명령이 감싼 push는 읽지 않는다"가 있다. 통과
  - 셋째(나누지 못한 명령): 스크래치에 로컬 bare origin과 문서 지도 구간이 있는 레포 `proj`(`main`이 origin보다 하나 앞서고 지금 브랜치는 `tasks/x`), 셋업 안 된 레포 `other`(같은 꼴)를 만들고, 명령마다 훅의 종료 코드와 `git push`를 `git push --dry-run --porcelain`으로 바꿔 bash에 돌린 결과를 견줌(커밋에는 `--allow-empty`를 붙임) → `proj`에서 `don't` 쪽과 `issue #12` 쪽은 훅 2, stderr "plate: 따옴표의 짝을 맞추지 못해 명령을 나누지 못했고, …" / "push를 다른 명령과 잇지 말고 따로 부른다."이고, bash는 둘 다 `refs/heads/main:refs/heads/main`을 냈다. 같은 자리의 `Fix #12`(heredoc 안), `Rename "foo" to "bar"`(heredoc 안과 `-m "Rename \"foo\" to \"bar\""` 둘 다)는 훅 2(stderr "plate: 기본 브랜치(`main`)로 푸시하지 않는다: `git push origin main`"). `other`에서 두 명령은 훅 0, `proj`에서 push가 없는 `don't` 쪽 커밋 명령은 훅 0. `docs/ARCHITECTURE.md` 48줄에 "따옴표가 어긋나 명령을 나누지 못하면(…) 호출한 폴더가 셋업된 프로젝트이고 명령의 글에 `push`가 있을 때 막고, push를 다른 명령과 잇지 말고 따로 하라고 알린다"가 있다. 통과
- 나누지 못한 명령은 셋업된 프로젝트에서 글에 `push`가 있으면 막히고, 셋업 안 된 프로젝트에서는 막히지 않는다.
  - `tests/test_push_guard.py`를 읽음 → 회고 3의 셋째 문제의 두 명령(`UNSPLIT_PUSHES` 25~28줄)이 셋업된 프로젝트의 `tasks/x`에서 막히고 stderr에 "따로"가 있는 `test_unsplit_command_with_push`(201줄), 셋업 안 된 프로젝트에서 막히지 않는 `test_unsplit_command_in_project_not_set_up`(332줄)이 있다. `python3 -m unittest discover -s tests` → `Ran 87 tests in 32.210s` / `OK`. 통과
- task 머리의 완료 조건이 모두 참이다.
  - 완료 조건 1: `python3 -m unittest discover -s tests` → `Ran 87 tests in 32.210s` / `OK`. `tests/test_push_guard.py`를 읽음 → 기본 브랜치에 있는 채 대상 없이 하는 push(`test_push_without_target_on_default_branch` 80줄, `test_push_head_while_on_default_branch` 108줄), 기본 브랜치를 가리키는 push(`test_push_to_default_branch` 92줄), 지우는 push(`test_delete_default_branch` 113줄의 `--delete` 두 자리, `-d`, `:main`, `:refs/heads/main`), `&&`·`;`로 이어진 명령 안의 push(`test_push_inside_chained_command` 188줄), `git -C` 안의 push와 그 폴더의 기본 브랜치(`test_push_inside_git_c_uses_that_folder` 209줄, `test_git_c_folder_has_its_own_default_branch` 217줄), 다른 브랜치(`test_push_to_other_branch` 250줄), origin 밖 원격(`test_push_to_remote_other_than_origin` 281줄), 셋업 안 된 프로젝트(`test_project_not_set_up` 326줄)가 있다. `python3 -m unittest discover -s tests -p 'test_push_guard.py' -v` → `Ran 31 tests in 16.626s` / `OK`. 통과
  - 완료 조건 2: `python3 -c "import json; h=json.load(open('plugins/plate/hooks/hooks.json')); print([m['matcher'] for m in h['hooks']['PreToolUse']])"` → `['Edit|Write|MultiEdit|NotebookEdit', 'Bash']`. `plugins/plate/hooks/hooks.json` 9줄과 18줄을 읽음 → Bash 항목은 `f="${CLAUDE_PLUGIN_ROOT}/hooks/push_guard.py"; [ -f "$f" ] || exit 0; exec python3 "$f"`로 편집 훅의 명령과 스크립트 이름만 다르다. 그 명령을 `CLAUDE_PLUGIN_ROOT=/nonexistent`로 `sh -c`에 돌림 → 종료 코드 0. 통과
  - 완료 조건 3: `docs/PRD.md` 4줄(목표)과 `docs/ARCHITECTURE.md`의 기술 스택(5줄), 디렉터리 구조(19, 21, 34줄), 막는 장치(48줄)를 읽음 → PRD 목표에 "에이전트가 기본 브랜치에 하는 푸시", 기술 스택에 푸시 훅 `push_guard.py`, 디렉터리 구조에 hooks.json의 Bash 항목과 `push_guard.py`, `test_push_guard.py`, 막는 장치에 푸시 훅이 막는 것, 막지 않는 것, 한계, 나누지 못한 명령의 막음이 적혀 있다. 통과
  - 완료 조건 4: `python3 -m unittest discover -s tests` → `OK`(위와 같다). `git diff --stat f8f219b^ HEAD -- tests/test_verdict.py plugins/plate/ci/`(`f8f219b^`는 `5a7c002`) → 출력 없음. `python3 -m unittest discover -s tests -p 'test_verdict.py'` → `Ran 14 tests in 0.732s` / `OK`. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 87 tests in 32.210s` / `OK`. 통과

**테스트 먼저 기록**
- `phase-4.md`의 "한 일"의 테스트 먼저 → 실패 출력(`FAIL: test_unsplit_command_with_push …` 두 subTest, `Ran 87 tests in 32.380s` / `FAILED (failures=2)`)이 먼저, 통과 출력(`Ran 87 tests in 33.222s` / `OK`)이 뒤에 있다. 통과

**실패**
- 없음

**하네스에서 걸린 것**
- 없음

**판정**: 통과
