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
- [x] 기본 브랜치를 이름으로 적지 않고 보내는 push를 막지 않는다. `git push --all origin`, `git push --mirror origin`, `git push origin 'refs/heads/*:refs/heads/*'`는 로컬의 기본 브랜치를 origin의 기본 브랜치로 보내는데, `push_guard.py`의 `push_args`(93~94줄)는 `--all`·`--mirror`를 다른 `--` 옵션처럼 넘기고, `blocked_branch`(166~167줄)는 refspec이 없으면 지금 브랜치만 보며, `target_branches`(136~146줄)는 `*`를 견주지 않는다. 스크래치에 origin(로컬 bare 레포)과 문서 지도 구간이 있는 레포를 만들고 로컬 `main`을 origin보다 한 커밋 앞서게 한 뒤 `tasks/x`에서 `git push --dry-run --porcelain --all origin`을 돌리니 `refs/heads/main:refs/heads/main 35caa9e..e7974f2`가 나왔고(`--mirror`도 같다), 같은 세 명령을 훅에 넣으니 모두 종료 코드 0이었다. task 머리의 목표("기본 브랜치에 푸시하면 plate의 훅이 막고")에 들지만 완료 조건 1이 이 꼴을 적지 않아 테스트도 없다 (`plugins/plate/hooks/push_guard.py`)
- [x] 기본 브랜치에 있는 채 태그만 보내는 push를 막는다. 기본 브랜치에서 `git push --tags`, `git push --tags origin`, `git push origin --tags`는 태그만 보내는데(같은 스크래치의 `main`에서 `git push --dry-run --porcelain --tags`가 `refs/tags/v1:refs/tags/v1 [new tag]`만 냈다), `push_args`가 `--tags`를 넘겨 refspec이 없는 것으로 보고 `blocked_branch`(167줄)가 "plate: 기본 브랜치(`main`)로 푸시하지 않는다"와 종료 코드 2로 막았다. 기본 브랜치로 가지 않는 push를 막고 까닭도 틀리게 알린다. `test_push_to_other_branch`의 `git push --tags origin`은 `tasks/x`에서만 돈다 (`plugins/plate/hooks/push_guard.py`, `tests/test_push_guard.py`)
- [x] 따옴표 없는 heredoc의 본문 줄을 명령으로 읽어 막는다. `segments`(30~54줄)는 줄바꿈을 명령의 경계로 나누고 `<<` 뒤에서는 구분자 낱말 하나만 빼서, 본문 줄을 따로 된 명령으로 본다. 같은 스크래치의 `tasks/x`에서 `cat > notes.md <<'EOF'`와 `git commit -F - <<'EOF'` 뒤의 본문에 `git push origin main` 줄이 있는 명령을 훅에 넣으니 둘 다 "plate: 기본 브랜치(`main`)로 푸시하지 않는다: `git push origin main`"과 종료 코드 2였다. push가 아닌 명령을 막는다. `git commit -m "$(cat <<'EOF' … EOF)"`처럼 따옴표 안의 heredoc은 0이었다 (`plugins/plate/hooks/push_guard.py`)

**통과 조건**
- 회고 1의 문제가 모두 고쳐졌다.
  - 확인: 문제마다 적힌 곳을 다시 읽거나 돌린다
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다

## 한 일
- 기본 브랜치를 이름으로 적지 않고 보내는 push를 막지 않는다: `push_args`가 `--all`, `--branches`(git 2.54의 `--all` 별칭), `--mirror`, `--tags`를 그 옵션이 뜻하는 refspec(`refs/heads/*`, `refs/heads/*`, `refs/*`, `refs/tags/*`. `REFSPEC_OPTIONS`)으로 함께 돌려주고, `blocked_branch`가 그것을 위치 인자의 refspec에 더해 본다. `target_branches`를 `target_refs`로 바꿔 원격에서 바뀔 ref 이름 전체를 내게 하고, `blocked_branch`가 `refs/heads/<기본 브랜치>`를 그 꼴에 `fnmatch.fnmatchcase`로 견줘 `*`가 든 refspec도 잡는다. `*`가 든 짧은 꼴은 git처럼 ref 이름 전체에 견준다(`'*:*'`는 잡고 `'tasks/*'`는 잡지 않는다). 같은 이름의 브랜치를 모두 보내는 `:`, `+:`는 `refs/heads/*`로 본다. 설정(`push.default=matching`, `remote.origin.push`, `remote.origin.mirror`)이 정하는 꼴은 보지 않는다. 시험: `test_push_without_naming_default_branch`(12꼴), `test_push_to_other_branch`에 `'refs/heads/tasks/*:refs/heads/tasks/*'`, `test_push_to_remote_other_than_origin`에 `--all fork`, `--mirror fork` (`plugins/plate/hooks/push_guard.py`, `tests/test_push_guard.py`)
- 기본 브랜치에 있는 채 태그만 보내는 push를 막는다: `--tags`가 `refs/tags/*` refspec이 되어 refspec이 없는 push로 보지 않으므로 지금 브랜치를 견주지 않고, `refs/tags/*`는 기본 브랜치에 들지 않아 통과한다. `--follow-tags`는 그대로 refspec이 없는 push다. 시험: `test_push_only_tags_on_default_branch`(`main`에서 `git push --tags`, `--tags origin`, `origin --tags`, `-u origin --tags`, `origin 'refs/tags/*:refs/tags/*'`) (`plugins/plate/hooks/push_guard.py`, `tests/test_push_guard.py`)
- 따옴표 없는 heredoc의 본문 줄을 명령으로 읽어 막는다: `without_heredocs`를 더해 `segments`가 낱말로 나누기 전에 heredoc의 본문 줄을 뺀다. 따옴표 밖의 `<<`(`<<<`는 빼고)에서 구분자를 shlex로 읽어 두고, 따옴표 밖의 다음 줄바꿈에서 구분자 줄(`<<-`면 앞의 탭을 뺀 줄)까지 건너뛴다. 따옴표 안의 `<<`(`grep -n '<<'`, `"$(cat <<'EOF' … )"`)는 heredoc으로 보지 않는다. 본문의 닫히지 않은 따옴표(`don't`) 때문에 명령 전체를 통과시키던 것도 이제 본문 뒤의 push를 막는다. shlex 설정은 `lexer`로 뺐다. 산술 확장 `$((1<<2))`의 `<<`도 heredoc으로 읽어 그 뒤 줄을 건너뛴다. 시험: `test_heredoc_body_is_not_a_command`(6꼴), `test_push_after_heredoc`(5꼴) (`plugins/plate/hooks/push_guard.py`, `tests/test_push_guard.py`)
- 테스트 먼저
  - 실패: `python3 -m unittest discover -s tests` → `FAIL: test_push_after_heredoc (test_push_guard.BlockTest.test_push_after_heredoc) (command="cat > notes.md <<'EOF'\ndon't\nEOF\ngit push origin main")`, `FAIL: test_push_without_naming_default_branch (test_push_guard.BlockTest.test_push_without_naming_default_branch) (command='git push --all origin')` 등 12개, `FAIL: test_heredoc_body_is_not_a_command (test_push_guard.PassTest.test_heredoc_body_is_not_a_command) (command="cat > notes.md <<'EOF'\ngit push origin main\nEOF")` 등 5개, `FAIL: test_push_only_tags_on_default_branch (test_push_guard.PassTest.test_push_only_tags_on_default_branch) (command='git push --tags')` 등 4개 / `Ran 80 tests in 30.776s` / `FAILED (failures=22)`
  - 통과: `python3 -m unittest discover -s tests` → `Ran 80 tests in 32.095s` / `OK`

## 확인 결과
- 회고 1의 문제가 모두 고쳐졌다.
  - 문제 1: 스크래치에 origin(로컬 bare 레포)과 문서 지도 구간이 있는 레포를 만들고 로컬 `main`을 origin보다 한 커밋 앞서게 한 뒤 `tasks/x`에서 `git push --dry-run --porcelain --all origin` → `refs/heads/main:refs/heads/main 390e55b..391a9a9`. 같은 레포에서 훅에 `git push --all origin`, `git push --mirror origin`, `git push origin 'refs/heads/*:refs/heads/*'`를 넣음 → 셋 다 종료 코드 2와 "plate: 기본 브랜치(`main`)로 푸시하지 않는다: `git push --all origin`"(나머지도 그 명령). 통과
  - 문제 2: 같은 레포의 `main`에서 `git push --dry-run --porcelain --tags` → `refs/tags/v1:refs/tags/v1 [new tag]`만. 훅에 `git push --tags`, `git push --tags origin`, `git push origin --tags` → 모두 종료 코드 0. `git push` → 종료 코드 2. 통과
  - 문제 3: 같은 레포의 `tasks/x`에서 `cat > notes.md <<'EOF'`와 `git commit -F - <<'EOF'` 뒤 본문에 `git push origin main` 줄이 있는 명령 → 둘 다 종료 코드 0. `git commit -m "$(cat <<'EOF' … EOF)"` → 0. 본문이 끝난 뒤 줄에 `git push origin main`이 있는 명령 → 종료 코드 2. 통과
- task 머리의 완료 조건이 모두 참이다.
  - 완료 조건 1: `python3 -m unittest discover -s tests` → `Ran 80 tests in 31.271s` / `OK`. `tests/test_push_guard.py`를 읽음 → 대상 없는 push(`test_push_without_target_on_default_branch`, `test_push_head_while_on_default_branch`), 기본 브랜치를 가리키는 push(`test_push_to_default_branch`), 지우는 push(`test_delete_default_branch`), 이어진 명령 안의 push(`test_push_inside_chained_command`), `git -C` 안의 push(`test_push_inside_git_c_uses_that_folder`, `test_git_c_folder_has_its_own_default_branch`), 다른 브랜치(`test_push_to_other_branch`), origin 밖 원격(`test_push_to_remote_other_than_origin`), 셋업 안 된 프로젝트(`test_project_not_set_up`)가 그대로 있다. 통과
  - 완료 조건 2: `python3 -c "import json; h=json.load(open('plugins/plate/hooks/hooks.json')); print([m['matcher'] for m in h['hooks']['PreToolUse']])"` → `['Edit|Write|MultiEdit|NotebookEdit', 'Bash']`. `plugins/plate/hooks/hooks.json` 18줄 → `f="${CLAUDE_PLUGIN_ROOT}/hooks/push_guard.py"; [ -f "$f" ] || exit 0; exec python3 "$f"`. 같은 꼴을 없는 경로(`/nonexistent/hooks/push_guard.py`)로 `sh -c`에 돌림 → 종료 코드 0. 통과
  - 완료 조건 3: `docs/PRD.md`의 목표(4줄)와 `docs/ARCHITECTURE.md`의 기술 스택(5줄), 디렉터리 구조(19, 21, 34줄), 막는 장치(48줄)를 읽음 → 푸시 훅이 적혀 있다. 이 phase는 두 문서를 바꾸지 않았다. 통과
  - 완료 조건 4: 위의 `python3 -m unittest discover -s tests` → `OK`. `git diff --stat 5a7c002 -- tests/test_verdict.py plugins/plate/ci/` → 출력 없음. `python3 -m unittest discover -s tests -p 'test_verdict.py'` → `Ran 14 tests` / `OK`. 통과

## 계획과 달라진 점
- TODO 1이 적은 세 꼴(`--all`, `--mirror`, `'refs/heads/*:refs/heads/*'`) 밖에 `--branches`, `'*:*'`, `'refs/heads/*'`, `:`, `+:`도 막았다. 스크래치 레포의 `tasks/x`에서 `git push --dry-run --porcelain`으로 다섯 꼴 모두 로컬 `main`을 origin의 `main`으로 보내는 것을 봤다. 까닭: TODO의 문제가 "기본 브랜치를 이름으로 적지 않고 보내는 push"이고 같은 고침으로 잡힌다.

## 남은 것
- 없음

## 하네스에서 걸린 것
- 없음

## 확인 1

**통과 조건**
- 회고 1의 문제가 모두 고쳐졌다.
  - 문제 1: 스크래치에 origin(로컬 bare 레포)과 문서 지도 구간이 있는 레포를 만들고 로컬 `main`을 origin보다 한 커밋 앞서게 한 뒤 `tasks/x`에서 `git push --dry-run --porcelain --all origin` → `refs/heads/main:refs/heads/main 41c0a15..2e5ddb4`(`--mirror`도 같은 줄). 같은 레포의 `tasks/x`에서 훅에 `git push --all origin`, `git push --mirror origin`, `git push origin 'refs/heads/*:refs/heads/*'`를 넣음 → 셋 다 종료 코드 2와 "plate: 기본 브랜치(`main`)로 푸시하지 않는다: `git push --all origin`"(나머지도 그 명령). 대조로 `git push origin tasks/x`, `git push -u origin tasks/x`, `git push origin 'refs/heads/tasks/*:refs/heads/tasks/*'` → 셋 다 0. 통과
  - 문제 2: 같은 레포의 `main`에서 `git push --dry-run --porcelain --tags` → `refs/tags/v1:refs/tags/v1 [new tag]`만. 훅에 `git push --tags`, `git push --tags origin`, `git push origin --tags` → 셋 다 종료 코드 0, stderr 없음. 대조로 `git push`, `git push --follow-tags` → 종료 코드 2. 통과
  - 문제 3: 같은 레포의 `tasks/x`에서 `cat > notes.md <<'EOF'`, `git commit -F - <<'EOF'`, 따옴표 없는 `cat > notes.md <<EOF` 뒤의 본문에 `git push origin main` 줄이 있는 명령 → 셋 다 종료 코드 0. `git commit -m "$(cat <<'EOF' … EOF)"` → 0. 본문이 끝난 뒤 줄에 `git push origin main`이 있는 명령(`<<'EOF'`, `<<-EOF` 둘) → 둘 다 종료 코드 2. 통과
- task 머리의 완료 조건이 모두 참이다.
  - 완료 조건 1: `python3 -m unittest discover -s tests` → `Ran 80 tests in 30.086s` / `OK`. `tests/test_push_guard.py`를 읽음 → 대상 없는 push(`test_push_without_target_on_default_branch` 74줄, `test_push_head_while_on_default_branch` 102줄), 기본 브랜치를 가리키는 push(`test_push_to_default_branch` 86줄), 지우는 push(`test_delete_default_branch` 107줄의 `--delete`, `-d`, `:main`, `:refs/heads/main`), 이어진 명령 안의 push(`test_push_inside_chained_command` 155줄의 `&&`, `;`), `git -C` 안의 push와 그 폴더의 기본 브랜치(`test_push_inside_git_c_uses_that_folder` 168줄, `test_git_c_folder_has_its_own_default_branch` 176줄), 다른 브랜치(`test_push_to_other_branch` 209줄), origin 밖 원격(`test_push_to_remote_other_than_origin` 240줄), 셋업 안 된 프로젝트(`test_project_not_set_up` 263줄)가 있다. 통과
  - 완료 조건 2: `python3 -c "import json; h=json.load(open('plugins/plate/hooks/hooks.json')); print([m['matcher'] for m in h['hooks']['PreToolUse']])"` → `['Edit|Write|MultiEdit|NotebookEdit', 'Bash']`. `plugins/plate/hooks/hooks.json` 18줄을 읽음 → `f="${CLAUDE_PLUGIN_ROOT}/hooks/push_guard.py"; [ -f "$f" ] || exit 0; exec python3 "$f"`로 편집 훅의 꼴과 스크립트 이름만 다르다. 그 명령을 `CLAUDE_PLUGIN_ROOT=/nonexistent`로 `sh -c`에 돌림 → 종료 코드 0. 통과
  - 완료 조건 3: `docs/PRD.md`의 목표(4줄) → "에이전트가 기본 브랜치에 하는 푸시"를 훅이 막는다고 적혀 있다. `docs/ARCHITECTURE.md`의 기술 스택(5줄) → 푸시 훅 `push_guard.py`, 디렉터리 구조(19, 21, 34줄) → hooks.json의 Bash 항목, `push_guard.py`, `test_push_guard.py`, 패턴과 규칙의 막는 장치(48줄) → 푸시 훅이 막는 것과 막지 않는 것이 적혀 있다. 통과
  - 완료 조건 4: 위의 `python3 -m unittest discover -s tests` → `OK`. `git diff --stat 5a7c002 HEAD -- tests/test_verdict.py plugins/plate/ci/` → 출력 없음. `python3 -m unittest discover -s tests -p 'test_verdict.py'` → `Ran 14 tests` / `OK`. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 80 tests in 30.086s` / `OK`. 통과

**테스트 먼저 기록**
- "한 일"의 "테스트 먼저" → 실패 출력(`FAIL: test_push_after_heredoc …`, `FAIL: test_push_without_naming_default_branch …` 등, `Ran 80 tests in 30.776s` / `FAILED (failures=22)`)이 먼저, 통과 출력(`Ran 80 tests in 32.095s` / `OK`)이 뒤에 있다. 통과

**실패**
- 없음

**하네스에서 걸린 것**
- 없음

**판정**: 통과
