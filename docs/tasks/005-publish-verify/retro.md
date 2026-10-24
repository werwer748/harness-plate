# 회고

## 회고 1

**확인**
- 1. harness-plate가 공개 저장소이고 그 마켓플레이스가 유효하다.
  - `gh repo view werwer748/harness-plate --json visibility -q .visibility` → `PUBLIC`. 통과
  - `GIT_TERMINAL_PROMPT=0 git -c credential.helper= ls-remote https://github.com/werwer748/harness-plate.git HEAD` → `d29c0144082039adc42cc5e07f65bbb499cd71be	HEAD` 한 줄, 종료 코드 0. 통과
  - `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
- 2. 두 매니페스트의 버전이 0.11.0이다. `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `README.md`가 PR, CI 판정, 푸시 훅, 명령 절의 설치 줄, 공개 저장소를 적고, `docs/ADR.md`에 ADR-022가 있다.
  - `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → `"version": "0.11.0",` 두 줄. 통과
  - `grep -c "^### ADR-022: " docs/ADR.md` → `1`. 통과
  - 네 문서를 읽음 → 네 문서를 합쳐 보면 다섯이 모두 있다. PR은 PRD 핵심 기능 8, ARCHITECTURE의 run 항목과 데이터 흐름, ADR-021, README "tasks 끝의 PR"에 있다. CI 판정은 PRD 핵심 기능 8, ARCHITECTURE "PR의 CI" 항목, ADR-021, README의 판정 표에 있다. 푸시 훅은 PRD 목표, ARCHITECTURE의 기술 스택·디렉터리 구조·막는 장치, README "훅"에 있다. 명령 절의 설치 줄은 ARCHITECTURE 명령 절의 `- 설치: 없음`과 "PR의 CI" 항목에 있다. 공개 저장소는 ARCHITECTURE 배포 줄, ADR-021, ADR-022, README 설치 절에 있다. 문서마다로 읽으면 PRD에 설치 줄과 공개 저장소가, ADR에 푸시 훅과 설치 줄이, README에 설치 줄이 없다. `grep -n -E "비공개|private|로컬로 합|로컬에서 합|PR과 CI는 011에서 만든다"`를 네 문서에 돌리면 ADR-022의 "2026-10-24에 비공개에서 공개로 바꿨다" 한 줄만 나온다. "합친/합칠/합치/합쳐"가 든 줄은 모두 지금 동작(원격이 없거나 GitHub이 아니면 합칠지 묻는다, CI의 자동 머지)이나 ADR-021의 이유다. 옛 동작은 남지 않았다. 통과
- 3. 시험 저장소를 origin으로 둔 시험 폴더에서 setup이 CI 워크플로를 둘지 묻고, 승인하면 워크플로 파일을 쓰고 보고에 시크릿 등록 방법을 적는다. plate 워크플로가 없는 시험 저장소로 run이 tasks 끝에 PR을 열지 묻고, 승인하면 `tasks/`로 시작하는 브랜치에서 `main`으로 가는 PR을 열고 평가서 댓글을 단다.
  - `done-phase-2.md`에 적힌 setup 장면의 기록 → `~/plate-rail-test/logs/ci-setup-1.jsonl`의 `result`에 할 일 표의 "CI 워크플로 쓰기 | `.github/workflows/plate-review.yml` | **필요**", "**CI 에이전트를 둘까요?**", 시크릿 `CLAUDE_CODE_OAUTH_TOKEN`이 있어야 돈다는 글이 있다(`grep -c 'CI 에이전트를 둘까요'` → 2). 같은 세션의 `ci-setup-2.jsonl`의 `result`에 "## CI 시크릿 등록" 절(`CLAUDE_CODE_OAUTH_TOKEN`, `claude setup-token`, `gh secret set CLAUDE_CODE_OAUTH_TOKEN`)이 있다. `ls -la ~/plate-rail-test/ci-setup/.github/workflows/` → `plate-review.yml`(3136바이트). `test <기록> -nt plugins/plate/skills/setup/SKILL.md` → 두 기록 모두 참(기록 10-24 18:59:59, 19:07:11, 본문 10-23 21:55:30). 통과
  - run 장면의 기록 → `~/plate-rail-test/logs/ci-norun-2.jsonl`의 `result`에 "## PR을 열까요?"와 "**`tasks/line-count`를 푸시하고 위 내용으로 PR을 열고 댓글을 달까요?**"가 있다(`grep -c 'PR을 열까요'` → 2). `test <기록> -nt plugins/plate/skills/run/SKILL.md` → `ci-norun-1`~`3` 모두 참(본문 10-24 18:24:36). 통과
  - `gh pr view 1 -R werwer748/plate-ci-test --json headRefName,baseRefName,state,comments` → 머리 브랜치 `tasks/line-count`, 기준 브랜치 `main`, `OPEN`, 댓글 하나(작성자 `werwer748`, 첫 줄 `## 평가 1`, 그 아래 `**대상**`과 범위 줄). 통과
- 4. 시험 저장소의 `main`에 plate 복사본과 그것을 `--plugin-dir`로 싣는 CI 워크플로가 있다. CI가 PR마다 평가서를 PR 댓글로 달고 판정대로 하며, 세 판정마다 그 판정이 나오게 바꾼 PR이 하나씩 있다. plate 워크플로가 있는 시험 저장소로 run이 PR을 열면 run은 평가서 댓글을 달지 않고 CI가 단다.
  - `gh pr view <번호> -R werwer748/plate-ci-test --json state,comments` → #2(`is-blank`) `MERGED`, #3(`avg-word-length`) `OPEN`, #4(`sentence-count`) `CLOSED`. 셋 모두 댓글 하나, 작성자 `github-actions`, 첫 줄이 차례로 `판정: 자동 머지`, `판정: 머지 요청`, `판정: 닫기`이고 셋째 줄이 `# 코드 평가`다. 통과
  - 시험 저장소를 scratchpad의 `ci-retro`에 새로 복제(`main` `91b8060`). `diff -r <ci-retro>/.plate plugins/plate` → `Only in plugins/plate/hooks: __pycache__` 한 줄, 종료 코드 1. 그 폴더는 git이 무시하는 `edit_guard.cpython-313.pyc` 하나(10-24 20:56:31, phase 4 때 생김)이고 `git status --ignored`로 `!!`다. `diff -r -x __pycache__ <ci-retro>/.plate plugins/plate` → 출력 없음, 종료 코드 0. 추적되는 파일은 두 쪽 모두 15개다. 복사본의 내용은 같다. `git log -1 --format=%cI -- .plate` → `2026-10-24T19:51:08+09:00`(10:51:08Z). `gh run list -R werwer748/plate-ci-test --json headBranch,createdAt` → `is-blank` 10:52:06Z, `avg-word-length` 10:52:11Z, `sentence-count` 10:52:18Z로 셋 모두 그 뒤다. 통과
  - run 장면의 기록 → `~/plate-rail-test/logs/ci-run-2.jsonl`의 `result`에 "## PR을 열까요?"와 "이대로 푸시하고 PR을 열까요?"가 있다(`grep -c` → 2). 평가 댓글은 `.github/workflows/plate-review.yml`이 있어 따로 달지 않는다고 적혀 있다. `test <기록> -nt plugins/plate/skills/run/SKILL.md` → `ci-run-1`~`3` 모두 참. 통과
  - `gh pr view 6 -R werwer748/plate-ci-test --json headRefName,baseRefName,comments` → 머리 브랜치 `tasks/unique-words`, 기준 브랜치 `main`, 댓글 하나(작성자 `github-actions`, 첫 줄 `판정: 자동 머지`, 셋째 줄 `# 코드 평가`). 작성자가 `werwer748`인 댓글은 0개다. 통과
- 5. GitHub 원격이 없는 시험 폴더에서 run이 tasks 끝에 PR 대신 합칠지 묻고, 승인하면 `main`에 그 tasks의 `<이름>: 비움` 커밋이 들어온다. 셋업된 시험 폴더에서 에이전트가 기본 브랜치로 `git push`하면 푸시 훅이 막는다.
  - `done-phase-4.md`에 적힌 원격 없는 장면의 기록 → `~/plate-rail-test/logs/ci-local-2.jsonl`의 `result`가 "This repo has no origin remote, so there's no PR step; the next step is merging into `main`." 뒤에 "Should I merge `tasks/line-count` into `main`?"로 끝난다(`grep -c` → 2). `test <기록> -nt plugins/plate/skills/run/SKILL.md` → `ci-local-1`~`3` 모두 참. `git -C ~/plate-rail-test/ci-local log --format=%s main` → 첫 줄 `line-count: 비움`(`c3f87c1`). `git remote`는 아무것도 내지 않고 브랜치는 `main` 하나다. 통과
  - 푸시 훅 장면의 기록 → `~/plate-rail-test/logs/ci-push.jsonl`의 `git push origin main` 호출의 `tool_result`가 `is_error` `True`이고 내용이 `PreToolUse:Bash hook error: [f="…/plugins/plate/hooks/push_guard.py"; …]: ` 뒤에 `plate: 기본 브랜치(`main`)로 푸시하지 않는다: `git push origin main``과 둘째 줄이다. 두 줄은 `plugins/plate/hooks/push_guard.py` 37~38줄의 글이다. `tool_result_meta`의 `permission_decision`은 `{'decision': 'reject', 'source': 'hook', 'reason_type': 'hook'}`. `ci-push`는 `AGENTS.md`에 규칙 구간이 있는 셋업된 폴더다. origin(`ci-push-origin.git`)의 `main`은 `f0fa749`로 로컬 `main`(`64f5581 셋업`)보다 하나 뒤다. `test <기록> -nt plugins/plate/hooks/push_guard.py` → 참(기록 10-24 21:01:28, 훅 17:15:54). 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 89 tests in 34.281s`, `OK`, 종료 코드 0. 통과

**문제**
- 없음

**판정**: 통과
