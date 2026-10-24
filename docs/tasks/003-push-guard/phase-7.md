# Phase 7: 회고 6의 문제를 고친다

**목표**: 회고 6에서 나온 문제를 모두 고친다.

**테스트 먼저**: 아니오 — task 머리의 결정대로 훅을 고치지 않고 `docs/ARCHITECTURE.md`만 고친다

**읽을 것**
- `docs/tasks/003-push-guard/retro.md`의 `## 회고 6` 절
- `plugins/plate/hooks/push_guard.py`
- `tests/test_push_guard.py`
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/ADR.md`
- `docs/TOOLS.md`

**TODO**
- [ ] 훅을 고치지 않고 약속 밖의 꼴로 적는다(task 머리의 결정). `docs/ARCHITECTURE.md`의 막는 장치에서 푸시 훅의 약속을 `tests/test_push_guard.py`의 시험이 다루는 꼴로 고쳐 적고, 그 밖의 셸 구문과 git의 표기는 약속하지 않는다고 적고, `heads/<이름>`으로 적은 대상을 약속 밖의 예로 든다. 문제: 기본 브랜치를 `heads/<이름>`으로 적은 push를 막지 않는다. git은 refspec의 이름을 `refs/<이름>` 규칙으로도 풀어 `heads/main`을 `refs/heads/main`으로 읽는데, `target_refs`(227~237줄)는 `refs/`로 시작하지 않는 대상에 `refs/heads/`를 붙여(237줄) `refs/heads/heads/main`으로 견준다. 스크래치에 로컬 bare origin과 문서 지도 구간이 있는 레포(`main`이 origin보다 한 커밋 앞서고 지금 브랜치는 `tasks/x`)를 만들고 `git push origin heads/main`, `git push origin tasks/x:heads/main`, `git push origin :heads/main`, `git push origin --delete heads/main`을 훅에 넣으니 넷 다 0이었고, 같은 명령의 `git push`를 `git push --dry-run --porcelain`으로 바꿔 bash에 돌리니 앞의 둘은 `refs/heads/main:refs/heads/main`과 `refs/heads/tasks/x:refs/heads/main`을, 뒤의 둘은 `:refs/heads/main [deleted]`를 냈다. phase 1(`f8f219b`)의 훅도 0이다. 완료 조건 1의 "기본 브랜치를 가리키는 push"와 "기본 브랜치를 지우는 push"에 들고, 셸 구문이 아니라 git의 refspec이라 task 머리 다섯째 결정의 약속 밖("그 밖의 셸 구문")에 들지 않는다 (`plugins/plate/hooks/push_guard.py`, `docs/ARCHITECTURE.md`)
- [ ] 훅을 고치지 않고 약속 밖의 꼴로 적는다(task 머리의 결정). 같은 글에 `--repo`로 적은 원격을 약속 밖의 예로 든다. 문제: 기본 브랜치에 있는 채 `--repo`로 origin 밖 원격을 적은 push를 막는다. `git push --repo=<원격>`은 위치 인자의 `<repository>`와 같은데, `push_args`(168~196줄)는 `--repo=…`를 다른 `--` 옵션처럼 넘기고(184~185줄) `--repo <원격>`은 값을 건너뛰기만 해서(28줄, 182~183줄), `blocked_branch`가 원격을 설정의 `origin`으로 보고(259줄) 대상이 없으니 기본 브랜치에 있다는 까닭으로 막는다(265줄). 같은 스크래치에 bare 원격 `fork`를 더하고 `main`에서 `git push --repo=fork`와 `git push --repo fork`를 훅에 넣으니 둘 다 "plate: 기본 브랜치(`main`)로 푸시하지 않는다"와 종료 코드 2였고, bash의 `--dry-run --porcelain`은 둘 다 `fork.git`으로만 `refs/heads/main:refs/heads/main [new branch]`를 냈다. 같은 자리의 `git push fork`는 0이다(`test_push_to_remote_other_than_origin`도 같다). phase 1(`f8f219b`)의 훅도 2다. 완료 조건 1의 "origin 밖 원격으로의 푸시는 막지 않는다"에 들고 셸 구문이 아니다 (`plugins/plate/hooks/push_guard.py`, `docs/ARCHITECTURE.md`)

**통과 조건**
- 회고 6의 문제가 모두 고쳐졌다. 두 문제는 `docs/ARCHITECTURE.md`의 막는 장치에 약속 밖의 꼴로 적힌 것이 고친 것이다.
  - 확인: 문제마다 적힌 곳을 다시 읽거나 돌린다
- `docs/ARCHITECTURE.md`의 막는 장치가 푸시 훅의 약속을 `tests/test_push_guard.py`의 시험이 다루는 꼴로 적고, 그 밖의 셸 구문과 git의 표기는 약속하지 않는다고 적는다. 약속 밖의 꼴은 이 phase의 통과를 가르지 않는다.
  - 확인: `docs/ARCHITECTURE.md`의 막는 장치를 읽어 task 머리의 결정과 견준다
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다
