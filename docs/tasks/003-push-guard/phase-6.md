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
- [x] 훅을 고치지 않고 약속 밖의 꼴로 적는다(task 머리의 결정). `docs/ARCHITECTURE.md`의 막는 장치에서 푸시 훅의 글을, 훅이 막는다고 약속하는 꼴과 그 밖의 셸 구문은 약속하지 않는다는 것으로 고쳐 적고, 매개변수 확장 `${ … }`을 약속 밖의 꼴로 든다. 문제: 큰따옴표 안의 매개변수 확장 `"${ … }"`에서 안쪽 큰따옴표 사이에 `#`이 있는 한 줄 명령 뒤에 `&&`로 이은 push를 막지 않는다. 셸은 `"${X:-"fix #1"}"`의 안쪽 따옴표를 따로 세는데, `scan`은 `$(`와 백틱(75~81줄)만 따로 읽고 `${`는 따로 읽지 않아 안쪽의 `"`에서 바깥 따옴표가 닫힌다고 읽고(82~84줄), 그 뒤 낱말 첫머리의 `#`(89~92줄)를 주석으로 보아 줄 끝까지 지운다. 지운 글의 따옴표 짝이 맞아 `segments`(122~143줄)가 None이 아닌 목록을 돌려주므로 나누지 못한 명령의 막음(`check` 279~280줄)에 걸리지 않고, 뒤의 push는 지워진 채 통과한다. `echo "${X:-"fix #1"}" && git push origin main`을 넣으니 `without_non_commands`는 `echo "${X:-"fix `를, `segments`는 `[['echo', '${X:-fix']]`를 냈다. 스크래치에 로컬 bare origin과 문서 지도 구간이 있는 레포(`main`이 origin보다 한 커밋 앞서고 지금 브랜치는 `tasks/x`)를 만들고, 이 명령과 `git commit --allow-empty -m "${MSG:-"fix #1"}" && git push origin main`을 훅에 넣고 같은 명령의 `git push`를 `git push --dry-run --porcelain`으로 바꿔 bash에 돌리니, 둘 다 지금의 훅에서 0이고 bash는 둘 다 `refs/heads/main:refs/heads/main`을 냈다. phase 1(`f8f219b`)과 phase 2(`5cdb2a0`)의 훅은 둘 다 2로 막았고, phase 3(`8c3673b`)부터 phase 5(`fd12137`)까지의 훅은 0이다. 회고 4의 문제와 같은 오독(안쪽 따옴표를 바깥 것으로 읽고 주석 빼기가 짝을 맞춘다)이 phase 5가 따로 읽게 한 명령 치환 밖의 매개변수 확장에 남은 꼴이다. push는 `&&`로 이어진 명령이고 대상도 글로 적혀 있어, task 머리 결정의 한계(같은 호출의 `cd`·`pushd` 뒤, 명령 치환이나 변수로 적은 대상, 다른 명령이 감싼 push)에 들지 않는다. 안쪽에 `#`이 없는 `echo "${X:-"a"}" && git push origin main`은 지금도 2다 (`plugins/plate/hooks/push_guard.py`, `docs/ARCHITECTURE.md`)
- [x] 훅을 고치지 않고 약속 밖의 꼴로 적는다(task 머리의 결정). 같은 글에 산술 명령 `(( … ))`을 약속 밖의 꼴로 든다. 문제: 산술 명령 `(( … << … ))` 뒤의 줄에 적은 push를 막지 않는다. 셸은 `(( ))` 안의 `<<`를 왼쪽 시프트로 읽는데, `scan`(95~102줄)은 따옴표 밖의 `<<`를 `((` 안이어도 heredoc의 시작으로 보고, 다음 줄바꿈에서(103~114줄) 구분자(`2`)와 같은 줄이 나올 때까지 뒤의 줄을 본문으로 건너뛴다. `(( x = 1 << 2 ))`(줄바꿈)`git push origin main`을 넣으니 `without_non_commands`는 `(( x = 1 << 2 ))\n`을, `segments`는 `[['x', '=']]`를 냈다. 같은 스크래치의 `tasks/x`에서 이 명령은 지금의 훅에서 0이고, bash는 `x`를 4로 두고 `--dry-run --porcelain`의 push가 `refs/heads/main:refs/heads/main`을 냈다. phase 1(`f8f219b`)의 훅은 2로 막았고, heredoc 빼기를 더한 phase 2(`5cdb2a0`)부터 phase 5(`fd12137`)까지의 훅은 0이다. phase 2의 기록(`done-phase-2.md`의 한 일)은 "산술 확장 `$((1<<2))`의 `<<`도 heredoc으로 읽어 그 뒤 줄을 건너뛴다"고 적었고, phase 5의 치환 읽기가 `$(( ))` 꼴은 고쳤지만(`echo $((1<<2))`(줄바꿈)`git push origin main`은 phase 2~4의 훅에서 0, 지금 2) `(( ))` 명령 꼴은 남았다. push는 줄바꿈으로 이어진 명령이고 대상도 글로 적혀 있어 task 머리 결정의 한계에 들지 않는다 (`plugins/plate/hooks/push_guard.py`, `docs/ARCHITECTURE.md`)

**통과 조건**
- 회고 5의 문제가 모두 고쳐졌다. 두 문제는 `docs/ARCHITECTURE.md`의 막는 장치에 약속 밖의 꼴로 적힌 것이 고친 것이다.
  - 확인: 문제마다 적힌 곳을 다시 읽거나 돌린다
- `docs/ARCHITECTURE.md`의 막는 장치가 task 머리의 결정에 적은 약속하는 꼴을 적고, 그 밖의 셸 구문은 약속하지 않는다고 적는다. 약속 밖의 꼴은 이 phase의 통과를 가르지 않는다.
  - 확인: `docs/ARCHITECTURE.md`의 막는 장치를 읽어 task 머리의 결정과 견준다
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다

## 한 일
- 훅을 고치지 않고 약속 밖의 꼴로 적는다(매개변수 확장 `${ … }`): `docs/ARCHITECTURE.md` 패턴과 규칙의 막는 장치(48줄)에서 푸시 훅의 글을 고쳐 적었다. 명령을 나눌 때 heredoc의 본문과 `#` 주석을 명령으로 보지 않고 줄 잇기를 경계로 보지 않는다는 것을 더하고, 명령 치환의 읽기와 나누지 못한 명령의 막음 뒤에 "푸시 훅이 막는다고 약속하는 꼴은 여기까지 적은 것뿐이고, 그 밖의 셸 구문은 약속하지 않는다"를 두었다. 앞에 있던 셸 구문의 한계(`cd`·`pushd` 뒤, 명령 치환이나 변수로 적은 대상, `sh -c`·`eval`)는 그 뒤로 옮겨 약속 밖의 꼴로 묶고, 매개변수 확장(`${ … }`)을 약속 밖의 꼴로 들었다. 끝에 "에이전트의 푸시를 막는 기본은 스킬마다의 "푸시하지 않는다" 규칙이고, 푸시 훅은 흔한 꼴을 한 번 더 막는다"를 더했다. `push_guard.py`는 고치지 않았다 (`docs/ARCHITECTURE.md`)
- 훅을 고치지 않고 약속 밖의 꼴로 적는다(산술 명령 `(( … ))`): 같은 문장에 산술 명령(`(( … ))`)을 매개변수 확장과 함께 약속 밖의 꼴로 들었다. `push_guard.py`는 고치지 않았다 (`docs/ARCHITECTURE.md`)

## 확인 결과
- 회고 5의 문제가 모두 고쳐졌다. 두 문제는 `docs/ARCHITECTURE.md`의 막는 장치에 약속 밖의 꼴로 적힌 것이 고친 것이다.
  - `docs/ARCHITECTURE.md` 48줄을 다시 읽음 → "푸시 훅이 막는다고 약속하는 꼴은 여기까지 적은 것뿐이고, 그 밖의 셸 구문은 약속하지 않는다"와 "매개변수 확장(`${ … }`), 산술 명령(`(( … ))`) 같은 구문에서 놓치거나 잘못 막는 것은 결함으로 보지 않는다"가 있다. 스크래치에 로컬 bare origin과 문서 지도 구간(`<!-- plate:docs-map:start -->`)이 있는 레포(`main`이 origin보다 앞서고 지금 브랜치는 `tasks/x`)를 만들고 지금의 훅에 넣음 → `echo "${X:-"fix #1"}" && git push origin main` 0, `git commit --allow-empty -m "${MSG:-"fix #1"}" && git push origin main` 0, `(( x = 1 << 2 ))`(줄바꿈)`git push origin main` 0으로 회고 5에 적힌 대로이고, 셋 다 적은 약속 밖의 꼴(매개변수 확장, 산술 명령)에 든다. 견줌으로 `echo "${X:-"a"}" && git push origin main` 2, `git push origin main` 2, `git push origin tasks/x` 0. 통과
- `docs/ARCHITECTURE.md`의 막는 장치가 task 머리의 결정에 적은 약속하는 꼴을 적고, 그 밖의 셸 구문은 약속하지 않는다고 적는다. 약속 밖의 꼴은 이 phase의 통과를 가르지 않는다.
  - `docs/ARCHITECTURE.md` 48줄을 task 머리의 결정과 견줌 → 완료 조건 1의 꼴(`&&`, `||`, `;`, `|`, 줄바꿈으로 나눈 명령 안의 push, `git -C <폴더>`, 기본 브랜치를 바꾸거나 지우는 push, 대상 없이 하는 push, 다른 브랜치·origin 밖 원격·셋업 안 된 프로젝트는 막지 않음), heredoc 본문과 `#` 주석을 명령으로 보지 않고 줄 잇기를 경계로 보지 않는 것, `$( … )`·백틱 치환의 읽기, 나누지 못한 명령의 막음이 적혀 있고, 그 밖의 셸 구문은 약속하지 않는다고 적었다. 셋째 결정의 한계(`cd`·`pushd` 뒤, 명령 치환이나 변수로 적은 대상, `sh -c`·`eval`)와 첫째 결정의 사람의 푸시를 다루지 않는 것도 있다. 통과
- task 머리의 완료 조건이 모두 참이다.
  - 완료 조건 1: `python3 -m unittest discover -s tests` → `Ran 89 tests in 34.899s` / `OK`. `tests/test_push_guard.py`를 읽음 → 대상 없이 하는 push(`test_push_without_target_on_default_branch` 90줄, `test_push_head_while_on_default_branch` 118줄), 기본 브랜치를 가리키는 push(`test_push_to_default_branch` 102줄), 지우는 push(`test_delete_default_branch` 123줄의 `--delete`, `-d`, `:main`, `:refs/heads/main`), 이어진 명령 안의 push(`test_push_inside_chained_command` 198줄의 `&&`, `;`, `||`, 줄바꿈), `git -C` 안의 push와 그 폴더의 기본 브랜치(228줄, 236줄), 다른 브랜치(269줄), origin 밖 원격(300줄), 셋업 안 된 프로젝트(345줄)가 있고, 막는 시험은 `assertBlocked`(81줄)로 종료 코드 2와 stderr를 본다. 통과
  - 완료 조건 2: `python3 -c "import json; h=json.load(open('plugins/plate/hooks/hooks.json')); print([m['matcher'] for m in h['hooks']['PreToolUse']])"` → `['Edit|Write|MultiEdit|NotebookEdit', 'Bash']`. `plugins/plate/hooks/hooks.json` 9줄과 18줄을 읽음 → 18줄은 `f="${CLAUDE_PLUGIN_ROOT}/hooks/push_guard.py"; [ -f "$f" ] || exit 0; exec python3 "$f"`로 9줄과 스크립트 이름만 다르다. 그 명령을 `CLAUDE_PLUGIN_ROOT=/nonexistent`로 `sh -c`에 돌림 → `exit=0`. 통과
  - 완료 조건 3: `docs/PRD.md` 목표(4줄)에 "에이전트가 기본 브랜치에 하는 푸시", `docs/ARCHITECTURE.md` 기술 스택(5줄)에 `push_guard.py`, 디렉터리 구조(19, 21, 34줄)에 hooks.json의 Bash 항목, `push_guard.py`, `test_push_guard.py`, 막는 장치(48줄)에 푸시 훅이 있다. 통과
  - 완료 조건 4: 위의 `python3 -m unittest discover -s tests` → `OK`. `git diff --stat f8f219b^ HEAD -- tests/test_verdict.py plugins/plate/ci/`와 `git diff --stat -- tests/test_verdict.py plugins/plate/ci/` → 둘 다 출력 없음. `python3 -m unittest discover -s tests -p 'test_verdict.py'` → `Ran 14 tests in 0.742s` / `OK`. 통과

## 계획과 달라진 점
- 없음

## 남은 것
- 없음

## 하네스에서 걸린 것
- TODO 두 항목 끝의 파일 목록에 `plugins/plate/hooks/push_guard.py`가 있지만, 같은 항목의 "훅을 고치지 않고"와 테스트 먼저 줄의 "`docs/ARCHITECTURE.md`만 고친다"를 따라 훅은 고치지 않았다. 목록은 회고 5의 문제 글에서 옮겨 온 것으로 보았다.
