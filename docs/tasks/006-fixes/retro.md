# 회고

## 회고 1

**확인**
- 1. `scan`의 인지 복잡도가 어림 67로 기준 15를 넘어, 셸 꼴 하나를 고칠 때 다른 꼴을 깨뜨리기 쉽다 (`plugins/plate/hooks/push_guard.py:62`)
  - `plugins/plate/hooks/push_guard.py`의 `scan`(62줄)과 거기서 나눈 `Scanner`(71~179줄)를 읽어 Sonar의 셈법(if·for·while·조건식은 1에 겹친 깊이를 더하고, elif·else는 1, and·or 묶음마다 1)으로 셈 → `scan` 2, `Scanner.step` 9, `unquoted` 9, `heredoc_body` 7, `paren` 3, `substitution` 2, `take`·`escape`·`comment`·`at_heredoc`·`heredoc_start`·`heredoc_bodies` 1, `__init__`·`close` 0. `tests/test_push_guard.py`의 `cognitive_complexity`로 센 값도 같다. 모두 15 이하. 통과
  - `python3 -m unittest discover -s tests` → `Ran 99 tests in 39.798s`, `OK`. 통과
- 2. `push_args`의 인지 복잡도가 어림 24로 기준 15를 넘는다 (`plugins/plate/hooks/push_guard.py:168`)
  - `push_args`(228줄)와 거기서 나눈 `short_options`(255줄)를 같은 셈법으로 셈 → `push_args` 12(while 1, 안의 if 둘 2·2, elif 넷 4, `and` 1, `delete or deletes` 1, else 1), `short_options` 6(for 1, if 2, 조건식 3). 통과
  - 테스트는 위와 같이 `OK`. 통과
- 3. 푸시 훅의 옵션과 설정을 읽는 가지 일곱 곳(따옴표 밖 이스케이프, 환경 변수 앞붙임, `git -c` 같은 git 옵션, `--`, `-o`·`--repo` 같은 push 옵션, 짧은 옵션 묶음의 `-o`, 설정의 원격)에 시험이 없어 깨져도 알 수 없다 (`plugins/plate/hooks/push_guard.py:71`)
  - `tests/test_push_guard.py`를 읽음 → 따옴표 밖 이스케이프 `test_escaped_character`(261줄)·`test_escaped_quote_does_not_open_quote`(430줄), 환경 변수 앞붙임 `test_assignment_before_git`(273줄), git 옵션 `test_git_option_value_is_not_subcommand`(283줄, `-c`·`--git-dir`), `--` `test_positional_after_double_dash`(295줄), push 옵션 `test_push_option_value_is_not_positional`(306줄, `-o`·`--push-option`·`--receive-pack`·`--repo`), 짧은 옵션 묶음의 `-o` `test_o_in_short_option_bundle`(320줄, `-uo`·`-uoci.skip`·`-do`), 설정의 원격 `test_configured_push_remote_is_origin`(332줄)·`test_configured_remote_other_than_origin`(421줄). 일곱 가지 모두 그 가지를 지나는 시험이 있다. 통과
  - 테스트는 위와 같이 `OK`. 통과
- 4. 완료 조건 1의 셋째 확인 `diff -r <복사본> plugins/plate`가 `.gitignore`에 걸린 `__pycache__`를 다른 것으로 내어 실패한다. 추적되는 파일은 같다 (`plugins/plate/hooks/__pycache__`)
  - 테스트(`OK`)를 돌린 뒤 `git clone https://github.com/werwer748/plate-ci-test.git <scratchpad>/ci-test-clone`(`main` `91b8060`), `git archive 72dcfcf plugins/plate | tar -x -C <scratchpad>/tasks-end`, `diff -r -x __pycache__ <scratchpad>/ci-test-clone/.plate <scratchpad>/tasks-end/plugins/plate` → 출력 없음, 종료 코드 0. 복사본 자리는 시험 저장소 워크플로의 `--plugin-dir ${{ github.workspace }}/.plate`(32줄)로 봤다. 통과
- 5. 두 매니페스트의 `description`이 0.11.0의 푸시 훅과 CI(review의 PR 모드, 판정 스크립트)를 적지 않는다 (`plugins/plate/.claude-plugin/plugin.json:4`, `plugins/plate/.codex-plugin/plugin.json:4`)
  - 두 `plugin.json`의 `description`을 읽음 → 둘 다 "setup이 승인받아 두는 CI 워크플로는 PR마다 review의 PR 모드로 평가하고 판정 스크립트로 자동 머지, 머지 요청, 닫기 가운데 하나를 고른다."와 "에이전트가 기본 브랜치에 하는 푸시를 막는 푸시 훅"이 있다. 통과
- 6. 띄운 에이전트에 실린 plate 스킬 본문이 tasks가 고친 저장소의 본문을 따라오지 않는다는 사실과, 스킬의 절차를 바꾸는 tasks는 그 절차에 기대는 다음 단계를 새 세션에서 이어 간다는 것을 적는다 (`docs/TOOLS.md`)
  - `docs/TOOLS.md` 83·84줄을 읽음 → "세션에 실린 plate 스킬 본문은 세션을 띄울 때의 것이라, 같은 세션에서 띄운 에이전트에는 tasks가 고치기 전의 본문이 실린다."와 "그래서 스킬의 절차를 바꾸는 tasks는 그 절차에 기대는 다음 단계(확인, 회고, tasks 끝의 평가)를 새 세션에서 이어 간다."가 있다. 통과
- 7. 테스트와 `--plugin-dir` 세션의 훅이 `plugins/plate/hooks/__pycache__`를 만든다는 것을 적고, `plugins/plate`를 복사본과 견주는 확인은 `diff -r -x __pycache__`로 쓴다 (`docs/ARCHITECTURE.md`)
  - `docs/ARCHITECTURE.md` 47줄을 읽음 → 테스트와 `--plugin-dir`로 이 레포의 plate를 실은 세션의 푸시 훅이 `edit_guard`를 불러와 `plugins/plate/hooks/__pycache__/`를 만든다는 것과, `plugins/plate`를 복사본과 견주는 확인은 `diff -r -x __pycache__`로 쓴다는 것이 있다. 테스트를 돌린 뒤 `find plugins -name __pycache__`는 `plugins/plate/hooks/__pycache__` 하나(`edit_guard.cpython-313.pyc`)였다. 통과
- 8. 시험 폴더의 run 허용 목록에 `Bash(git push:*)`를 넣는다 (`~/plate-rail-test/bin/run.sh`)
  - `~/plate-rail-test/bin/run.sh`를 읽음 → 27~28줄, `run|phase|check|retro|review|eval|verify`의 `--allowedTools`에 `"Bash(git push:*)"`가 있다. 통과
- 9. tasks 완료 조건 1, 2, 3, 4, 5, 6이 참이다.
  - `python3 -m unittest discover -s tests` → `OK`. `tests/test_verdict.py`를 읽음 → 커버리지 79·79.9는 머지 요청, 80·80.0은 자동 머지(57줄), 등급 A는 자동 머지·B는 머지 요청(71줄), 보안 B는 머지 요청·C·D·E는 닫기(77줄), `skipped`, `unmeasured`·`unjudged`는 머지 요청, `fail`은 닫기, 닫기가 모름보다 앞서는 것(108줄)을 본다. 통과
  - `docs/tasks/005-publish-verify/done-phase-3.md`의 세 장면 #2, #3, #4에 `gh pr view <번호> -R werwer748/plate-ci-test --json state,comments` → `MERGED`, `OPEN`, `CLOSED`. 셋 모두 댓글 하나, 작성자 `github-actions`, 첫 줄이 차례로 `판정: 자동 머지`, `판정: 머지 요청`, `판정: 닫기`, 셋째 줄이 `# 코드 평가`. 통과
  - 시험 저장소의 복사본 견주기 → 완료 조건 4와 같이 출력 없음, 종료 코드 0. 통과
  - `done-phase-2.md`~`done-phase-4.md`의 run 장면 기록: `grep -c 'PR을 열까요'` → `ci-norun-2.jsonl` 2, `ci-run-2.jsonl` 2. `grep -c 'Should I merge' ci-local-2.jsonl` → 2(원격 없는 장면). `ci-norun-1~3`, `ci-run-1~3`, `ci-local-1~3`의 아홉 기록 모두 `test <기록> -nt plugins/plate/skills/run/SKILL.md` → 참(run 본문 10-24 18:24:36, 묻는 기록 19:36:09, 20:46:22, 21:23:24). 통과
  - run 장면의 PR에 `gh pr view <번호> -R werwer748/plate-ci-test --json headRefName,baseRefName,comments` → #1 `tasks/line-count` → `main`, 댓글 하나(작성자 `werwer748`, 첫 줄 `## 평가 1`. CI 워크플로가 없던 장면). #6 `tasks/unique-words` → `main`, 댓글 하나(작성자 `github-actions`, 첫 줄 `판정: 자동 머지`). 통과
  - `git -C ~/plate-rail-test/ci-local log --format=%s main` → 첫 줄 `line-count: 비움`(원격 없음). 통과
  - 테스트 `OK`. `tests/test_push_guard.py`에 기본 브랜치로의 푸시(`test_push_to_default_branch`, `test_push_without_target_on_default_branch` 등), 지우는 푸시(`test_delete_default_branch`), 이어진 명령(`test_push_inside_chained_command`), `git -C`(`test_push_inside_git_c_uses_that_folder`), 다른 브랜치(`test_push_to_other_branch`), origin 밖 원격(`test_push_to_remote_other_than_origin`), 셋업 안 된 프로젝트(`test_project_not_set_up`)의 시험이 있다. 통과
  - `done-phase-4.md`의 푸시 훅 장면 기록 `~/plate-rail-test/logs/ci-push.jsonl` → init의 Claude Code 2.1.310, plate는 `/Users/gangjungi/Desktop/harness-plate/plugins/plate`. `git push origin main` 호출의 `tool_result`가 `is_error: true`, 내용 `PreToolUse:Bash hook error: [f=".../plugins/plate/hooks/push_guard.py"; …]: plate: 기본 브랜치(`main`)로 푸시하지 않는다: `git push origin main``. `ci-push.state`의 origin `main`은 전과 뒤 모두 `f0fa749…`. `test ~/plate-rail-test/logs/ci-push.jsonl -nt plugins/plate/hooks/push_guard.py` → 참(훅 22:39:32, 기록 22:43:08. 작업 트리는 깨끗해 훅은 커밋된 것과 같다). 통과
  - `done-phase-2.md`의 setup 장면 기록 → `grep -c 'CI 에이전트를 둘까요' ci-setup-1.jsonl` 2, `ci-setup-2.jsonl`에 `gh secret set CLAUDE_CODE_OAUTH_TOKEN` 2, `claude setup-token` 2. `ls ~/plate-rail-test/ci-setup/.github/workflows/` → `plate-review.yml`. 두 기록 모두 `test <기록> -nt plugins/plate/skills/setup/SKILL.md` → 참. 통과
  - `gh repo view werwer748/harness-plate --json visibility -q .visibility` → `PUBLIC`. 통과
  - `GIT_TERMINAL_PROMPT=0 git -c credential.helper= ls-remote https://github.com/werwer748/harness-plate.git HEAD` → `d29c0144082039adc42cc5e07f65bbb499cd71be	HEAD` 한 줄, 종료 코드 0. 통과
  - `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
  - `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "0.11.0",`. 통과
  - `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `README.md`를 읽음 → PR(PRD 18줄, ARCHITECTURE 50·69줄, README 17~19줄), CI 판정(PRD 18줄, ARCHITECTURE 51줄, ADR-021, README 21~31줄), 푸시 훅(PRD 4줄, ARCHITECTURE 5·49줄, README 35줄), 명령 절의 설치 줄(ARCHITECTURE 82줄 `- 설치: 없음`), 공개 저장소(ARCHITECTURE 7줄, ADR-022, README 39·43줄)가 있다. "비공개"는 ADR-022의 "비공개에서 공개로 바꿨다"뿐이고, 합칠지 묻는 것은 origin이 없거나 GitHub의 것이 아닐 때로만 적혀 있다. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 99 tests in 39.798s`, `OK`. 통과
- 테스트 먼저 기록: phase 1
  - `done-phase-1.md`의 "한 일"의 "테스트 먼저" 항목 → 실패 출력(`FAIL: test_split_functions_within_limit … (name='scan') AssertionError: 66 not less than or equal to 15`, `(name='push_args') AssertionError: 24 not less than or equal to 15`, `FAILED (failures=4)`)이 먼저, 통과 출력(`Ran 99 tests in 42.968s`, `OK`)이 그 뒤에 있다. 통과

**문제**
- 없음

**판정**: 통과
