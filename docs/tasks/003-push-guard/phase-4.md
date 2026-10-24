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
- [ ] 훅을 고치지 않고 한계로 적는다(task 머리의 결정). `docs/ARCHITECTURE.md`의 막는 장치에, 푸시 훅은 같은 호출에서 `cd`·`pushd` 뒤에 하는 push를 호출한 폴더에서 본다고 적는다. 문제: `cd <폴더> &&`(또는 `;`) 뒤의 push를 그 폴더가 아니라 호출의 `cwd`에서 본다. `check`(239~249줄)는 호출의 `cwd`를 모든 단순 명령에 넘기고, `push_call`(120~139줄)은 `git -C`에서만 폴더를 바꾼다. 스크래치에 로컬 bare origin과 문서 지도 구간이 있는 레포 `proj`(`main`이 origin보다 앞서고 지금 브랜치는 `tasks/x`), 셋업 안 된 레포 `other`(`main`이 그 origin보다 앞선다), git 레포가 아닌 폴더 `plain`을 만들고, 명령마다 훅의 종료 코드와 같은 명령의 `git push`를 `git push --dry-run --porcelain`으로 바꿔 bash에 돌린 결과를 견줬다. `cwd`가 `plain`일 때 `cd <proj> && git push origin main`, `cd <proj> && git push origin HEAD:main`, `cd <proj>; git push origin :main`은 셋 다 훅 0이고 bash는 `refs/heads/main`을 바꾸거나 지웠다(`refs/heads/main:refs/heads/main`, `HEAD:refs/heads/main`, `:refs/heads/main [deleted]`). 거꾸로 `cwd`가 `proj`일 때 `cd <other> && git push origin main`은 셋업 안 된 프로젝트의 푸시인데 훅이 2로 막았다 (`plugins/plate/hooks/push_guard.py`, `docs/ARCHITECTURE.md`)
- [ ] 훅을 고치지 않고 한계로 적는다(task 머리의 결정). `docs/ARCHITECTURE.md`의 막는 장치에, 푸시 훅은 명령 치환이나 변수로 적은 대상과 `sh -c`·`eval`처럼 다른 명령이 감싼 push를 읽지 않는다고 적는다. 문제: 기본 브랜치에 있는 채 명령 치환으로 지금 브랜치를 적은 push를 막지 않는다. `target_refs`(201~211줄)는 `HEAD`, `@`만 지금 브랜치로 바꾸고, 따옴표 안의 `"$(git branch --show-current)"`는 그 글 그대로 `refs/heads/$(git branch --show-current)`로 본다. 따옴표가 없으면 `segments`가 `(`에서 명령을 나눠 대상이 `$`가 된다. 같은 스크래치의 `proj`를 `main`에 두고 `git push -u origin "$(git branch --show-current)"`와 `git push -u origin $(git rev-parse --abbrev-ref HEAD)`를 넣으니 둘 다 훅 0이었고 bash는 둘 다 `refs/heads/main:refs/heads/main`을 냈다. 같은 자리의 `git push origin HEAD`는 훅이 2로 막는다(`test_push_head_while_on_default_branch`도 같다) (`plugins/plate/hooks/push_guard.py`, `docs/ARCHITECTURE.md`)
- [ ] 나누지 못한 명령을 막는다(task 머리의 결정). 따옴표가 어긋나 명령을 나누지 못하면, 호출한 폴더가 셋업된 프로젝트이고 명령의 글에 `push`가 있을 때 막고, push를 다른 명령과 잇지 말고 따로 하라고 알린다. `docs/ARCHITECTURE.md`의 막는 장치에도 적는다. 문제: `"$( … )"` 안의 큰따옴표를 바깥 큰따옴표의 끝으로 읽어, 그 뒤의 따옴표가 어긋나면 명령 전체를 통과시킨다. 셸은 큰따옴표 안의 `$(`부터 따옴표를 새로 세는데 `without_non_commands`(48~94줄)와 `lexer`(40~45줄)는 안쪽의 `"`에서 바깥 따옴표를 닫는다. 그래서 `git commit -m "$(cat <<'EOF'`(줄바꿈)`Keep "don't" wording`(줄바꿈)`EOF`(줄바꿈)`)" && git push origin main`은 `don't`의 `'`가 닫히지 않은 따옴표로 읽혀 `segments`(99~102줄)가 빈 목록을 돌려준다. phase 3이 더한 주석 빼기는 같은 어긋남 위에서 `Close "issue #12" properly`의 `#12" properly`를 주석으로 지워 바깥 따옴표를 닫히지 않게 만들고, 같은 빈 목록이 된다(`without_non_commands`의 출력에서 `#12" properly`가 빠진 것을 봤다). 같은 스크래치의 `tasks/x`에서 두 명령은 지금의 훅에서 0이고 bash는 둘 다 `refs/heads/main:refs/heads/main`을 냈다. phase 1(`f8f219b`)과 phase 2(`5cdb2a0`)의 `push_guard.py`에 같은 명령을 넣으니 `issue #12` 쪽은 2로 막았고 `don't` 쪽은 0이었다. 안쪽 따옴표가 없는 `Fix #12`, 짝이 맞고 `#`·`'`가 없는 `Rename "foo" to "bar"`는 지금도 2다 (`plugins/plate/hooks/push_guard.py`, `docs/ARCHITECTURE.md`)

**통과 조건**
- 회고 3의 문제가 모두 고쳐졌다. 첫째와 둘째 문제는 `docs/ARCHITECTURE.md`의 막는 장치에 한계로 적힌 것이 고친 것이다.
  - 확인: 문제마다 적힌 곳을 다시 읽거나 돌린다
- 나누지 못한 명령은 셋업된 프로젝트에서 글에 `push`가 있으면 막히고, 셋업 안 된 프로젝트에서는 막히지 않는다. task 머리의 결정에 적은 한계 안의 꼴(같은 호출의 `cd`·`pushd` 뒤의 push, 명령 치환이나 변수로 적은 대상, 다른 명령이 감싼 push)은 이 phase의 통과를 가르지 않는다.
  - 확인: `tests/test_push_guard.py`에 회고 3의 셋째 문제의 두 명령이 막히는 테스트와 셋업 안 된 프로젝트에서 나누지 못한 명령이 막히지 않는 테스트가 있고, `python3 -m unittest discover -s tests`가 통과한다
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다
