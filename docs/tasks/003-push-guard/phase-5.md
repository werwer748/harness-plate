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
- [ ] 명령 치환을 따로 읽는다(task 머리의 결정). 명령을 나눌 때 `$( … )`와 백틱 치환은 그 안에서 따옴표, 주석, heredoc을 새로 세고, 닫는 `)`나 백틱에서 바깥(바깥 큰따옴표 안이었으면 그 안)으로 돌아온다. 치환 안의 push는 읽지 않는다. `docs/ARCHITECTURE.md`의 막는 장치에도 적는다. 문제: `"$( … )"` 안의 큰따옴표 사이에 `#`이 있는 한 줄 명령 뒤에 `&&`나 `;`로 이은 push를 막지 않는다. `without_non_commands`(53~99줄)는 `"$( … )"` 안쪽의 `"`에서 바깥 따옴표가 닫힌다고 읽고, 그 뒤 낱말 첫머리의 `#`(69~72줄)를 주석으로 보아 줄 끝까지 지운다. 지운 글에 `"`가 짝수 개면 남은 글의 따옴표 짝이 맞아 `segments`(102~123줄)가 None이 아닌 목록을 돌려주므로 phase 4가 더한 나누지 못한 명령의 막음(`check` 259~260줄)에 걸리지 않고, 뒤의 push는 지워진 채 통과한다. `git commit -m "$(echo "fix #1")" && git push origin main`을 넣으니 `without_non_commands`는 `git commit -m "$(echo "fix `를, `segments`는 `[['git', 'commit', '-m', '$(echo fix']]`를 냈다. 스크래치에 로컬 bare origin과 문서 지도 구간이 있는 레포(`main`이 origin보다 한 커밋 앞서고 지금 브랜치는 `tasks/x`)를 만들고, 이 명령과 `echo "$(echo "fix #1")" && git push origin main`, `echo "$(git log -1 --format="%h #%s")"; git push origin main`을 훅에 넣고 같은 명령의 `git push`를 `git push --dry-run --porcelain`으로 바꿔 bash에 돌리니, 셋 다 지금의 훅에서 0이고 bash는 셋 다 `refs/heads/main:refs/heads/main`을 냈다. phase 1(`f8f219b`)과 phase 2(`5cdb2a0`)의 훅은 셋 다 2로 막았고 phase 3(`8c3673b`)의 훅부터 0이다. 회고 3의 셋째 문제와 같은 오독 위에서 주석 빼기가 따옴표 짝을 맞추는 꼴이다. push는 명령 치환이나 다른 명령 안이 아니라 `&&`·`;`로 이어진 명령이고 대상도 글로 적혀 있어, task 머리 결정의 한계에 들지 않는다. 안쪽 따옴표가 없는 `git commit --allow-empty -m "fix #1" && git push origin main`과 `echo "$(echo "a")" && git push origin main`은 지금도 2다 (`plugins/plate/hooks/push_guard.py`, `docs/ARCHITECTURE.md`)

**통과 조건**
- 회고 4의 문제가 모두 고쳐졌다.
  - 확인: 문제마다 적힌 곳을 다시 읽거나 돌린다
- 셋업된 프로젝트에서 기본 브랜치가 아닌 브랜치에 있을 때, 회고 4의 문제에 적힌 세 명령과 `git commit -m "$(cat <<'EOF'`(줄바꿈)`Keep "don't" wording`(줄바꿈)`EOF`(줄바꿈)`)" && git push origin main`, `git commit -m "$(cat <<'EOF'`(줄바꿈)`Close "issue #12" properly`(줄바꿈)`EOF`(줄바꿈)`)" && git push origin main`은 막히고, push가 없는 `git commit -m "$(cat <<'EOF'`(줄바꿈)`Keep "don't" push wording`(줄바꿈)`EOF`(줄바꿈)`)"`는 막히지 않는다. 막힌 명령의 까닭은 나누지 못한 명령의 글이 아니라 기본 브랜치로 가는 push의 글이다. task 머리의 결정에 적은 한계 안의 꼴은 이 phase의 통과를 가르지 않는다.
  - 확인: `tests/test_push_guard.py`에 이 명령마다 테스트가 있고, `python3 -m unittest discover -s tests`가 통과한다
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다
