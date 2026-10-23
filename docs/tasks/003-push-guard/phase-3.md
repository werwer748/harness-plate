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
- [ ] 줄 잇기(`\` 바로 뒤의 줄바꿈)를 명령의 경계로 읽는다. 셸은 `\`+줄바꿈을 지우고 한 명령으로 잇는데, `lexer`(39~44줄)는 그것을 줄바꿈 낱말 하나로 내고 `segments`(95줄)가 `SEPARATORS`에 든 낱말로 보아 명령을 나눈다. `segments('git push \\\n  origin main')`이 `[['git', 'push'], ['origin', 'main']]`을 냈다. 스크래치에 로컬 bare origin과 문서 지도 구간이 있는 레포를 만들고 `main`을 origin보다 한 커밋 앞서게 한 뒤, `tasks/x`에서 `git push \`(줄바꿈)`  origin main`을 훅에 넣으니 종료 코드 0이었고 같은 명령을 `git push --dry-run --porcelain`으로 bash에 돌리니 `refs/heads/main:refs/heads/main`이 나왔다. 거꾸로 `main`에서 `git push \`(줄바꿈)`  origin tasks/x`는 origin의 `main`을 바꾸지 않는데 종료 코드 2로 막았다 (`plugins/plate/hooks/push_guard.py`)
- [ ] `#` 주석을 명령의 글로 읽는다. `lexer`가 `lex.commenters = ""`(43줄)로 주석을 두지 않고 `without_heredocs`(47~82줄)도 주석 안의 따옴표를 센다. 그래서 주석에 짝 없는 따옴표가 있으면 `lexer`가 `ValueError`를 내고 `segments`(89~90줄)가 빈 목록을 돌려 명령 전체를 통과시킨다. 같은 스크래치의 `tasks/x`에서 `# push it (it's ready)`(줄바꿈)`git push origin main`과 `echo "it's" # don't`(줄바꿈)`git push origin main`을 훅에 넣으니 둘 다 종료 코드 0이었고, bash의 `--dry-run --porcelain`은 둘 다 `refs/heads/main:refs/heads/main`을 냈다. 거꾸로 `echo hi # ; git push origin main`은 셸이 `#` 뒤를 주석으로 버려 푸시하지 않는데 종료 코드 2로 막았다 (`plugins/plate/hooks/push_guard.py`)

**통과 조건**
- 회고 2의 문제가 모두 고쳐졌다.
  - 확인: 문제마다 적힌 곳을 다시 읽거나 돌린다
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다
