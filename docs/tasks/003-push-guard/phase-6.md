# Phase 6: 회고 5의 문제를 고친다

**목표**: 회고 5에서 나온 문제를 모두 고친다.

**테스트 먼저**: 아니오 — task 머리의 결정대로 훅을 고치지 않고 `docs/ARCHITECTURE.md`만 고친다

**읽을 것**
- `docs/tasks/003-push-guard/retro.md`의 `## 회고 5` 절
- `plugins/plate/hooks/push_guard.py`
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/ADR.md`
- `docs/TOOLS.md`

**TODO**
- [ ] 훅을 고치지 않고 약속 밖의 꼴로 적는다(task 머리의 결정). `docs/ARCHITECTURE.md`의 막는 장치에서 푸시 훅의 글을, 훅이 막는다고 약속하는 꼴과 그 밖의 셸 구문은 약속하지 않는다는 것으로 고쳐 적고, 매개변수 확장 `${ … }`을 약속 밖의 꼴로 든다. 문제: 큰따옴표 안의 매개변수 확장 `"${ … }"`에서 안쪽 큰따옴표 사이에 `#`이 있는 한 줄 명령 뒤에 `&&`로 이은 push를 막지 않는다. 셸은 `"${X:-"fix #1"}"`의 안쪽 따옴표를 따로 세는데, `scan`은 `$(`와 백틱(75~81줄)만 따로 읽고 `${`는 따로 읽지 않아 안쪽의 `"`에서 바깥 따옴표가 닫힌다고 읽고(82~84줄), 그 뒤 낱말 첫머리의 `#`(89~92줄)를 주석으로 보아 줄 끝까지 지운다. 지운 글의 따옴표 짝이 맞아 `segments`(122~143줄)가 None이 아닌 목록을 돌려주므로 나누지 못한 명령의 막음(`check` 279~280줄)에 걸리지 않고, 뒤의 push는 지워진 채 통과한다. `echo "${X:-"fix #1"}" && git push origin main`을 넣으니 `without_non_commands`는 `echo "${X:-"fix `를, `segments`는 `[['echo', '${X:-fix']]`를 냈다. 스크래치에 로컬 bare origin과 문서 지도 구간이 있는 레포(`main`이 origin보다 한 커밋 앞서고 지금 브랜치는 `tasks/x`)를 만들고, 이 명령과 `git commit --allow-empty -m "${MSG:-"fix #1"}" && git push origin main`을 훅에 넣고 같은 명령의 `git push`를 `git push --dry-run --porcelain`으로 바꿔 bash에 돌리니, 둘 다 지금의 훅에서 0이고 bash는 둘 다 `refs/heads/main:refs/heads/main`을 냈다. phase 1(`f8f219b`)과 phase 2(`5cdb2a0`)의 훅은 둘 다 2로 막았고, phase 3(`8c3673b`)부터 phase 5(`fd12137`)까지의 훅은 0이다. 회고 4의 문제와 같은 오독(안쪽 따옴표를 바깥 것으로 읽고 주석 빼기가 짝을 맞춘다)이 phase 5가 따로 읽게 한 명령 치환 밖의 매개변수 확장에 남은 꼴이다. push는 `&&`로 이어진 명령이고 대상도 글로 적혀 있어, task 머리 결정의 한계(같은 호출의 `cd`·`pushd` 뒤, 명령 치환이나 변수로 적은 대상, 다른 명령이 감싼 push)에 들지 않는다. 안쪽에 `#`이 없는 `echo "${X:-"a"}" && git push origin main`은 지금도 2다 (`plugins/plate/hooks/push_guard.py`, `docs/ARCHITECTURE.md`)
- [ ] 훅을 고치지 않고 약속 밖의 꼴로 적는다(task 머리의 결정). 같은 글에 산술 명령 `(( … ))`을 약속 밖의 꼴로 든다. 문제: 산술 명령 `(( … << … ))` 뒤의 줄에 적은 push를 막지 않는다. 셸은 `(( ))` 안의 `<<`를 왼쪽 시프트로 읽는데, `scan`(95~102줄)은 따옴표 밖의 `<<`를 `((` 안이어도 heredoc의 시작으로 보고, 다음 줄바꿈에서(103~114줄) 구분자(`2`)와 같은 줄이 나올 때까지 뒤의 줄을 본문으로 건너뛴다. `(( x = 1 << 2 ))`(줄바꿈)`git push origin main`을 넣으니 `without_non_commands`는 `(( x = 1 << 2 ))\n`을, `segments`는 `[['x', '=']]`를 냈다. 같은 스크래치의 `tasks/x`에서 이 명령은 지금의 훅에서 0이고, bash는 `x`를 4로 두고 `--dry-run --porcelain`의 push가 `refs/heads/main:refs/heads/main`을 냈다. phase 1(`f8f219b`)의 훅은 2로 막았고, heredoc 빼기를 더한 phase 2(`5cdb2a0`)부터 phase 5(`fd12137`)까지의 훅은 0이다. phase 2의 기록(`done-phase-2.md`의 한 일)은 "산술 확장 `$((1<<2))`의 `<<`도 heredoc으로 읽어 그 뒤 줄을 건너뛴다"고 적었고, phase 5의 치환 읽기가 `$(( ))` 꼴은 고쳤지만(`echo $((1<<2))`(줄바꿈)`git push origin main`은 phase 2~4의 훅에서 0, 지금 2) `(( ))` 명령 꼴은 남았다. push는 줄바꿈으로 이어진 명령이고 대상도 글로 적혀 있어 task 머리 결정의 한계에 들지 않는다 (`plugins/plate/hooks/push_guard.py`, `docs/ARCHITECTURE.md`)

**통과 조건**
- 회고 5의 문제가 모두 고쳐졌다. 두 문제는 `docs/ARCHITECTURE.md`의 막는 장치에 약속 밖의 꼴로 적힌 것이 고친 것이다.
  - 확인: 문제마다 적힌 곳을 다시 읽거나 돌린다
- `docs/ARCHITECTURE.md`의 막는 장치가 task 머리의 결정에 적은 약속하는 꼴을 적고, 그 밖의 셸 구문은 약속하지 않는다고 적는다. 약속 밖의 꼴은 이 phase의 통과를 가르지 않는다.
  - 확인: `docs/ARCHITECTURE.md`의 막는 장치를 읽어 task 머리의 결정과 견준다
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다
