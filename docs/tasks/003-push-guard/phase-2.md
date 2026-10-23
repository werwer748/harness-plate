# Phase 2: 회고 1의 문제를 고친다

**목표**: 회고 1에서 나온 문제를 모두 고친다.

**테스트 먼저**: 예

**읽을 것**
- `docs/tasks/003-push-guard/retro.md`의 `## 회고 1` 절
- `plugins/plate/hooks/push_guard.py`
- `tests/test_push_guard.py`
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/ADR.md`
- `docs/TOOLS.md`

**TODO**
- [ ] 기본 브랜치를 이름으로 적지 않고 보내는 push를 막지 않는다. `git push --all origin`, `git push --mirror origin`, `git push origin 'refs/heads/*:refs/heads/*'`는 로컬의 기본 브랜치를 origin의 기본 브랜치로 보내는데, `push_guard.py`의 `push_args`(93~94줄)는 `--all`·`--mirror`를 다른 `--` 옵션처럼 넘기고, `blocked_branch`(166~167줄)는 refspec이 없으면 지금 브랜치만 보며, `target_branches`(136~146줄)는 `*`를 견주지 않는다. 스크래치에 origin(로컬 bare 레포)과 문서 지도 구간이 있는 레포를 만들고 로컬 `main`을 origin보다 한 커밋 앞서게 한 뒤 `tasks/x`에서 `git push --dry-run --porcelain --all origin`을 돌리니 `refs/heads/main:refs/heads/main 35caa9e..e7974f2`가 나왔고(`--mirror`도 같다), 같은 세 명령을 훅에 넣으니 모두 종료 코드 0이었다. task 머리의 목표("기본 브랜치에 푸시하면 plate의 훅이 막고")에 들지만 완료 조건 1이 이 꼴을 적지 않아 테스트도 없다 (`plugins/plate/hooks/push_guard.py`)
- [ ] 기본 브랜치에 있는 채 태그만 보내는 push를 막는다. 기본 브랜치에서 `git push --tags`, `git push --tags origin`, `git push origin --tags`는 태그만 보내는데(같은 스크래치의 `main`에서 `git push --dry-run --porcelain --tags`가 `refs/tags/v1:refs/tags/v1 [new tag]`만 냈다), `push_args`가 `--tags`를 넘겨 refspec이 없는 것으로 보고 `blocked_branch`(167줄)가 "plate: 기본 브랜치(`main`)로 푸시하지 않는다"와 종료 코드 2로 막았다. 기본 브랜치로 가지 않는 push를 막고 까닭도 틀리게 알린다. `test_push_to_other_branch`의 `git push --tags origin`은 `tasks/x`에서만 돈다 (`plugins/plate/hooks/push_guard.py`, `tests/test_push_guard.py`)
- [ ] 따옴표 없는 heredoc의 본문 줄을 명령으로 읽어 막는다. `segments`(30~54줄)는 줄바꿈을 명령의 경계로 나누고 `<<` 뒤에서는 구분자 낱말 하나만 빼서, 본문 줄을 따로 된 명령으로 본다. 같은 스크래치의 `tasks/x`에서 `cat > notes.md <<'EOF'`와 `git commit -F - <<'EOF'` 뒤의 본문에 `git push origin main` 줄이 있는 명령을 훅에 넣으니 둘 다 "plate: 기본 브랜치(`main`)로 푸시하지 않는다: `git push origin main`"과 종료 코드 2였다. push가 아닌 명령을 막는다. `git commit -m "$(cat <<'EOF' … EOF)"`처럼 따옴표 안의 heredoc은 0이었다 (`plugins/plate/hooks/push_guard.py`)

**통과 조건**
- 회고 1의 문제가 모두 고쳐졌다.
  - 확인: 문제마다 적힌 곳을 다시 읽거나 돌린다
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다
