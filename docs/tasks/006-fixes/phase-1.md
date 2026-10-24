# Phase 1: tasks 끝의 문제를 고친다

**목표**: task 머리의 완료 조건에 적힌 것을 모두 고친다.

**테스트 먼저**: 예

**읽을 것**
- `docs/tasks/review.md`의 `## 평가 1` 절
- `docs/tasks/eval.md`의 `## eval 1` 절
- `plugins/plate/hooks/push_guard.py`
- `plugins/plate/.claude-plugin/plugin.json`
- `plugins/plate/.codex-plugin/plugin.json`
- `~/plate-rail-test/bin/run.sh`
- `~/plate-rail-test/bin/pushprobe.sh`
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/ADR.md`
- `docs/TOOLS.md`

**TODO**
- [x] `scan`의 인지 복잡도가 어림 67로 기준 15를 넘어, 셸 꼴 하나를 고칠 때 다른 꼴을 깨뜨리기 쉽다 (`plugins/plate/hooks/push_guard.py:62`)
- [x] `push_args`의 인지 복잡도가 어림 24로 기준 15를 넘는다 (`plugins/plate/hooks/push_guard.py:168`)
- [x] 푸시 훅의 옵션과 설정을 읽는 가지 일곱 곳(따옴표 밖 이스케이프, 환경 변수 앞붙임, `git -c` 같은 git 옵션, `--`, `-o`·`--repo` 같은 push 옵션, 짧은 옵션 묶음의 `-o`, 설정의 원격)에 시험이 없어 깨져도 알 수 없다 (`plugins/plate/hooks/push_guard.py:71`)
- [x] 완료 조건 1의 셋째 확인 `diff -r <복사본> plugins/plate`가 `.gitignore`에 걸린 `__pycache__`를 다른 것으로 내어 실패한다. 추적되는 파일은 같다 (`plugins/plate/hooks/__pycache__`)
- [x] 두 매니페스트의 `description`이 0.11.0의 푸시 훅과 CI(review의 PR 모드, 판정 스크립트)를 적지 않는다 (`plugins/plate/.claude-plugin/plugin.json:4`, `plugins/plate/.codex-plugin/plugin.json:4`)
- [x] 띄운 에이전트에 실린 plate 스킬 본문이 tasks가 고친 저장소의 본문을 따라오지 않는다. 세션에 실린 plate 스킬 본문은 세션을 띄울 때의 것이라 같은 세션에서 띄운 에이전트에는 tasks가 고치기 전의 본문이 실린다는 사실을 적고, 스킬의 절차를 바꾸는 tasks는 그 절차에 기대는 다음 단계를 새 세션에서 이어 간다고 적는다 (`docs/TOOLS.md`)
- [x] 복사본과 견주는 `diff -r`가 git이 무시하는 `__pycache__`를 다른 것으로 낸다. 테스트와 `--plugin-dir` 세션의 훅이 `plugins/plate/hooks/__pycache__`를 만든다는 것을 적고, `plugins/plate`를 복사본과 견주는 확인은 `diff -r -x __pycache__`로 쓴다 (`docs/ARCHITECTURE.md`)
- [x] 시험 폴더의 run 허용 목록에 푸시가 없다. run의 허용 목록에 `Bash(git push:*)`를 넣어 장면마다 `RUN_ALLOW`로 더하지 않게 한다 (`~/plate-rail-test/bin/run.sh`)
- [x] 푸시 훅을 고친 뒤 `~/plate-rail-test/bin/pushprobe.sh ci-push ci-push`로 푸시 훅 장면을 다시 돌려, 기본 브랜치로의 `git push`가 훅에 막힌 실행 기록이 푸시 훅 스크립트보다 새롭게 한다(task 머리의 결정) (`~/plate-rail-test/logs/ci-push.jsonl`)

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다


## 한 일
- `scan`의 인지 복잡도가 어림 67로 기준 15를 넘어, 셸 꼴 하나를 고칠 때 다른 꼴을 깨뜨리기 쉽다: 읽는 자리와 상태(`out`, `pending`, `quote`, `depth`, `word_start`)를 `Scanner` 클래스로 옮기고 셸의 꼴마다 메서드 하나(`escape`, `substitution`, `unquoted`, `paren`, `comment`, `at_heredoc`, `heredoc_start`, `heredoc_bodies`, `heredoc_body`)로 나눴다. `scan`은 `Scanner`를 만들어 닫는 글자나 글의 끝까지 `step`을 돌리는 반복만 남았다. 셈은 `scan` 66 → 2, 메서드는 `step` 9, `unquoted` 9, `heredoc_body` 7, 나머지 3 이하다. 동작은 바꾸지 않았다 (`plugins/plate/hooks/push_guard.py`)
- `push_args`의 인지 복잡도가 어림 24로 기준 15를 넘는다: 짧은 옵션 묶음을 읽는 반복을 `short_options`(지우는가, -o의 값으로 건너뛸 낱말 수를 돌려준다)로 나눴다. 셈은 `push_args` 24 → 12, `short_options` 6이다 (`plugins/plate/hooks/push_guard.py`)
- 푸시 훅의 옵션과 설정을 읽는 가지 일곱 곳에 시험이 없어 깨져도 알 수 없다: 가지마다 시험을 더했다. 따옴표 밖 이스케이프는 `test_escaped_character`(막음)와 `test_escaped_quote_does_not_open_quote`(통과), 환경 변수 앞붙임은 `test_assignment_before_git`, git 옵션은 `test_git_option_value_is_not_subcommand`, `--`는 `test_positional_after_double_dash`, push 옵션은 `test_push_option_value_is_not_positional`, 짧은 옵션 묶음의 `-o`는 `test_o_in_short_option_bundle`, 설정의 원격은 `test_configured_push_remote_is_origin`(막음)과 `test_configured_remote_other_than_origin`(통과)이다. 깨지면 알 수 있는지 scratchpad의 복사본에서 가지마다 하나씩 망가뜨려(`--` 뒤를 한 낱말 늦게 읽기, 옵션 값을 건너뛰지 않기, 설정의 원격 대신 origin 돌려주기 등 아홉 꼴) `python3 -m unittest test_push_guard`를 돌렸고, 아홉 모두 그 가지의 시험이 실패했다 (`tests/test_push_guard.py`)
- 완료 조건 1의 셋째 확인이 `__pycache__`를 다른 것으로 내어 실패한다: task 머리의 결정대로 코드는 고치지 않았다. 견주는 법(`72dcfcf`의 `plugins/plate`와 `diff -r -x __pycache__`)은 아래 확인 결과에서 돌렸고, 문서는 완료 조건 7의 항목에서 고쳤다
- 두 매니페스트의 `description`이 0.11.0의 푸시 훅과 CI를 적지 않는다: "setup이 승인받아 두는 CI 워크플로는 PR마다 review의 PR 모드로 평가하고 판정 스크립트로 자동 머지, 머지 요청, 닫기 가운데 하나를 고른다."를 더하고, 훅 문장을 편집 훅과 "에이전트가 기본 브랜치에 하는 푸시를 막는 푸시 훅"이 함께 돈다로 고쳤다. 버전은 0.11.0 그대로다 (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)
- 띄운 에이전트에 실린 plate 스킬 본문이 tasks가 고친 저장소의 본문을 따라오지 않는다: "세션 도중의 스킬 본문 고침"에 tasks `pr-ci`의 run에서 고치기 전의 check, retro 본문이 실린 사실(커밋 `72dcfcf`의 `docs/tasks/eval.md` 실패 3, 6, 14)과, 세션에 실린 본문은 세션을 띄울 때의 것이라는 것, 스킬의 절차를 바꾸는 tasks는 그 절차에 기대는 다음 단계를 새 세션에서 이어 간다는 것을 두 줄로 더했다 (`docs/TOOLS.md`)
- 복사본과 견주는 `diff -r`가 `__pycache__`를 다른 것으로 낸다: "패턴과 규칙"에 테스트와 `--plugin-dir` 세션의 푸시 훅이 `edit_guard`를 불러와 `plugins/plate/hooks/__pycache__/`를 만든다는 것과, `plugins/plate`를 복사본과 견주는 확인은 `diff -r -x __pycache__`로 쓴다는 것을 한 줄로 더했다. 그 폴더를 scratchpad로 옮긴 뒤 `python3 -m unittest test_push_guard.BlockTest.test_message_names_command`를 돌리면 `edit_guard.cpython-313.pyc`가 다시 생기는 것을 봤다 (`docs/ARCHITECTURE.md`)
- 시험 폴더의 run 허용 목록에 푸시가 없다: run, phase, check, retro, review, eval, verify가 함께 쓰는 허용 목록에 `"Bash(git push:*)"`를 넣고 그 까닭을 주석 한 줄로 적었다. 이 레포 밖이라 커밋하지 않는다 (`~/plate-rail-test/bin/run.sh`)
- 푸시 훅을 고친 뒤 푸시 훅 장면을 다시 돌린다: `zsh ~/plate-rail-test/bin/pushprobe.sh ci-push ci-push > ~/plate-rail-test/logs/ci-push.out 2>&1` → `ci-push exit=0 secs=14`. 기록의 init 줄은 Claude Code 2.1.310, 플러그인 `plate@inline`(0.11.0, 이 레포의 `plugins/plate`)이고, 에이전트의 `git push origin main` 호출의 `tool_result`가 `is_error: true`, 내용 `PreToolUse:Bash hook error: [f=".../plugins/plate/hooks/push_guard.py"; …]: plate: 기본 브랜치(`main`)로 푸시하지 않는다: `git push origin main``이다. `ci-push.state`의 origin `main`은 전과 뒤 모두 `f0fa749…`다 (`~/plate-rail-test/logs/ci-push.jsonl`, `ci-push.state`, `ci-push.out`)
- 테스트 먼저
  - 실패: `python3 -m unittest discover -s tests` → `FAIL: test_split_functions_within_limit (test_push_guard.ComplexityTest.test_split_functions_within_limit) (name='scan')` `AssertionError: 66 not less than or equal to 15 : {'scan': 66}`, `(name='Scanner')` `AssertionError: 'Scanner' not found in ['blocked_branch', …, 'without_non_commands']`, `(name='push_args')` `AssertionError: 24 not less than or equal to 15 : {'push_args': 24}`, `(name='short_options')` `AssertionError: 'short_options' not found in […]`, `Ran 99 tests in 42.208s`, `FAILED (failures=4)`
  - 통과: `python3 -m unittest discover -s tests` → `Ran 99 tests in 42.968s`, `OK`

## 확인 결과
- task 머리의 완료 조건이 모두 참이다.
  - 완료 조건 1: `plugins/plate/hooks/push_guard.py`의 `scan`(62줄)과 `Scanner`(71~179줄)를 다시 읽어 Sonar의 셈법(if·while·for·조건식은 1에 깊이를 더하고, elif·else는 1, and·or 묶음마다 1)으로 셈 → `scan` 2, `Scanner.step` 9, `Scanner.unquoted` 9, `Scanner.heredoc_body` 7, `Scanner.paren` 3, `Scanner.substitution` 2, 나머지 메서드 0~1. `tests/test_push_guard.py`의 `cognitive_complexity`로 센 값과 같다. `python3 -m unittest discover -s tests` → `Ran 99 tests`, `OK`. 통과
  - 완료 조건 2: `push_args`(228줄)와 `short_options`(255줄)를 다시 읽어 같은 셈법으로 셈 → `push_args` 12(while 1, if 2, if 2, elif 넷 4, and 1, or 1, else 1), `short_options` 6. 테스트는 위와 같이 `OK`. 통과
  - 완료 조건 3: `tests/test_push_guard.py`를 읽음 → 따옴표 밖 이스케이프 261·430줄, 환경 변수 앞붙임 273줄, git 옵션 283줄, `--` 295줄, push 옵션 306줄, 짧은 옵션 묶음의 `-o` 320줄, 설정의 원격 332·421줄의 시험이 그 가지를 지난다. 테스트는 `OK`. 통과
  - 완료 조건 4: `python3 -m unittest discover -s tests`(`OK`) 뒤 `git clone https://github.com/werwer748/plate-ci-test.git <scratchpad>/ci-test-clone`(HEAD `91b8060`), `git archive 72dcfcf plugins/plate | tar -x -C <scratchpad>/tasks-end`, `diff -r -x __pycache__ <scratchpad>/ci-test-clone/.plate <scratchpad>/tasks-end/plugins/plate` → 출력 없음, 종료 코드 0. 통과
  - 완료 조건 5: 두 `plugin.json`의 `description`을 읽음 → 둘 다 "CI 워크플로는 PR마다 review의 PR 모드로 평가하고 판정 스크립트로 자동 머지, 머지 요청, 닫기 가운데 하나를 고른다"와 "에이전트가 기본 브랜치에 하는 푸시를 막는 푸시 훅"이 있다. 통과
  - 완료 조건 6: `docs/TOOLS.md` 83·84줄을 읽음 → 세션에 실린 plate 스킬 본문은 세션을 띄울 때의 것이라 같은 세션에서 띄운 에이전트에는 tasks가 고치기 전의 본문이 실린다는 것과, 스킬의 절차를 바꾸는 tasks는 그 절차에 기대는 다음 단계를 새 세션에서 이어 간다는 것이 있다. 통과
  - 완료 조건 7: `docs/ARCHITECTURE.md` 47줄을 읽음 → 테스트와 `--plugin-dir` 세션의 훅이 `plugins/plate/hooks/__pycache__/`를 만든다는 것과 견주는 확인은 `diff -r -x __pycache__`로 쓴다는 것이 있다. 통과
  - 완료 조건 8: `~/plate-rail-test/bin/run.sh`를 읽음 → 28줄, run이 쓰는 허용 목록에 `"Bash(git push:*)"`가 있다. `zsh -n` 통과. 통과
  - 완료 조건 9 (PR 번호와 실행 기록의 경로는 `docs/tasks/review.md` 평가 1에 옮겨 적힌 것을 썼다. 아래 "하네스에서 걸린 것")
    - `python3 -m unittest discover -s tests` → `OK`. `tests/test_verdict.py`를 읽음 → 커버리지 79·79.9·80·80.0(57줄), A와 B(71줄), 보안 B와 C·D·E(77줄), `unmeasured`·`unjudged`, `fail`, `skipped`, 닫기가 모름보다 앞서는 것(108줄)을 본다. 통과
    - `gh pr view <번호> -R werwer748/plate-ci-test --json state,comments`(#2, #3, #4) → `MERGED`, `OPEN`, `CLOSED`. 셋 모두 댓글 하나(작성자 `github-actions`), 첫 줄이 차례로 `판정: 자동 머지`, `판정: 머지 요청`, `판정: 닫기`, 셋째 줄 `# 코드 평가`. 통과
    - 시험 저장소의 복사본 견주기 → 완료 조건 4와 같이 출력 없음. 통과
    - `grep -c 'PR을 열까요'` → `ci-norun-2.jsonl` 2, `ci-run-2.jsonl` 2. `grep -c 'Should I merge' ci-local-2.jsonl` → 2(`Should I merge `tasks/line-count` into `main`?`). 셋 모두 `test <기록> -nt plugins/plate/skills/run/SKILL.md` → 참. 통과
    - `gh pr view <번호> -R werwer748/plate-ci-test --json headRefName,baseRefName,comments` → #1 `tasks/line-count` → `main`, 댓글 하나(작성자 `werwer748`, 첫 줄 `## 평가 1`). #6 `tasks/unique-words` → `main`, 댓글 하나(작성자 `github-actions`, `판정: 자동 머지`). 통과
    - `git -C ~/plate-rail-test/ci-local log --format=%s main` → 첫 줄 `line-count: 비움`. 통과
    - `python3 -m unittest discover -s tests` → `OK`. 대상 없는 push, 기본 브랜치를 가리키는 push, 지우는 push, 이어진 명령, `git -C`, 다른 브랜치, origin 밖 원격, 셋업 안 된 프로젝트의 시험이 그대로 있다. 통과
    - `~/plate-rail-test/logs/ci-push.jsonl` → `git push origin main`의 `tool_result`가 `is_error: true`, 훅의 막는 글. `test ~/plate-rail-test/logs/ci-push.jsonl -nt plugins/plate/hooks/push_guard.py` → 참. 통과
    - `grep -c 'CI 에이전트를 둘까요' ci-setup-1.jsonl` → 2, `grep -c 'CLAUDE_CODE_OAUTH_TOKEN' ci-setup-2.jsonl` → 4(`gh secret set CLAUDE_CODE_OAUTH_TOKEN`으로 넣는다는 안내), `ls ~/plate-rail-test/ci-setup/.github/workflows/` → `plate-review.yml`, 두 기록 모두 `test <기록> -nt plugins/plate/skills/setup/SKILL.md` → 참. 통과
    - `gh repo view werwer748/harness-plate --json visibility -q .visibility` → `PUBLIC`. 통과
    - `GIT_TERMINAL_PROMPT=0 git -c credential.helper= ls-remote https://github.com/werwer748/harness-plate.git HEAD` → `d29c0144082039adc42cc5e07f65bbb499cd71be	HEAD` 한 줄. 통과
    - `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
    - `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "0.11.0",`. 통과
    - `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `README.md`를 읽음 → PR(PRD 18줄, ARCHITECTURE 50줄, README "tasks 끝의 PR"), CI 판정(ARCHITECTURE 51줄, ADR-021, README "CI 워크플로"의 표), 푸시 훅(PRD 4줄, ARCHITECTURE 5·49줄, README "훅"), 명령 절의 설치 줄(ARCHITECTURE 82줄 `- 설치: 없음`), 공개 저장소(ARCHITECTURE 7줄, ADR-022, README 39·43줄)가 있다. 옛 동작은 ADR-022의 "비공개에서 공개로 바꿨다"는 이력 말고는 없다. 통과

## 계획과 달라진 점
- TODO의 `~/plate-rail-test/bin/pushprobe.sh ci-push ci-push`는 그 파일에 실행 권한이 없어 `(eval):1: permission denied: /Users/gangjungi/plate-rail-test/bin/pushprobe.sh`로 돌지 않았다. `zsh ~/plate-rail-test/bin/pushprobe.sh ci-push ci-push`로 돌렸다. 그 첫 시도의 출력이 `ci-push.out`을 덮었고, 다시 돌린 결과로 다시 덮였다

## 남은 것
- 없음

## 하네스에서 걸린 것
- task 머리의 완료 조건 1·2·5(`plugins/plate` 안의 파일을 바꾼다)와 4·9(시험 저장소의 복사본과 `plugins/plate`가 같고, 푸시 훅 장면의 기록이 푸시 훅 스크립트보다 새롭다)가 맞물려 모두 참이 될 수 없다. 완료 조건 9가 tasks 끝의 장면을 고정해 견주는 확인을 tasks 머리에서 그대로 옮겼고, 이 task가 그 대상 파일을 바꾸는 것을 셈하지 않았다
- task 머리의 완료 조건 4(코드로 `__pycache__`를 만들지 않게)와 7(만든다고 적고 `-x __pycache__`로 견준다)이 같은 문제를 서로 다른 길로 고치라고 한다. 리뷰의 소스 문제와 eval의 고칠 거리를 각각 완료 조건으로 옮겨 생겼다
- phase 스킬 1번(tasks 머리를 읽지 않는다): `.gitignore`와 커밋을 보려던 명령에 `docs/tasks/plan.md`의 앞 60줄을 함께 읽었다. 판단에는 쓰지 않았다
- phase 스킬 2번의 테스트 먼저(바뀔 동작의 실패하는 테스트 → 구현): 완료 조건 1·2는 동작을 바꾸지 않는 나누기라 동작으로 실패하는 테스트를 쓸 수 없다. 완료 조건의 "Sonar의 셈법으로 센 인지 복잡도"를 세는 시험(`ComplexityTest`)을 실패하는 테스트로 썼다. 완료 조건 3의 시험 아홉은 고치기 전에도 통과했다(지금 동작을 지키는 시험이다)
- phase 스킬 1번(다른 phase의 파일은 읽지 않는다)과 완료 조건 9의 확인: 확인이 PR 번호와 실행 기록의 경로를 `docs/tasks/005-publish-verify/done-phase-2.md`~`done-phase-4.md`에서 읽게 한다. 그 파일은 읽지 않고, 읽을 것에 든 `docs/tasks/review.md` 평가 1이 그 파일에서 옮겨 적은 번호(#1~#4, #6)와 경로(`ci-norun-2`, `ci-run-2`, `ci-local-2`, `ci-push`, `ci-setup-1`, `ci-setup-2`)를 썼다
- 코드 평가(`docs/tasks/review.md` 평가 1)는 인지 복잡도로 `scan`과 `push_args`만 문제로 적었지만, 같은 셈법으로 `target_refs`(`plugins/plate/hooks/push_guard.py:292`)가 16으로 기준 15를 넘는다(for 1, 조건식 셋 2·2·3, if 셋 2·2·2, or 둘). 이 task의 완료 조건 밖이라 고치지 않았고, `ComplexityTest`도 `scan`, `push_args`와 거기서 나눈 함수만 센다
- TODO의 `pushprobe.sh`는 실행 권한이 없어 적힌 명령 그대로는 돌지 않는다(위 "계획과 달라진 점")

## 확인 1

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 완료 조건 1: `plugins/plate/hooks/push_guard.py`의 `scan`(62줄)과 `Scanner`(71~179줄)를 읽어 Sonar의 셈법(if·for·while·조건식은 1에 깊이, elif·else는 1, and·or 묶음마다 1)으로 셈 → `scan` 2, `Scanner.step` 9, `unquoted` 9, `heredoc_body` 7, `paren` 3, `substitution` 2, `take`·`escape`·`comment`·`at_heredoc`·`heredoc_start`·`heredoc_bodies` 1, `close`·`__init__` 0. 모두 15 이하. `python3 -m unittest discover -s tests` → `Ran 99 tests in 40.184s`, `OK`. 통과
  - 완료 조건 2: `push_args`(228줄)와 `short_options`(255줄)를 같은 셈법으로 셈 → `push_args` 12(while 1, 안의 if 2, if 2, elif 넷 4, and 1, or 1, else 1), `short_options` 6(for 1, if 2, 조건식 3). 테스트는 위와 같이 `OK`. 통과
  - 완료 조건 3: `tests/test_push_guard.py`를 읽음 → 따옴표 밖 이스케이프 `test_escaped_character`(261줄)·`test_escaped_quote_does_not_open_quote`(430줄), 환경 변수 앞붙임 `test_assignment_before_git`(273줄), git 옵션 `test_git_option_value_is_not_subcommand`(283줄, `-c`·`--git-dir`), `--` `test_positional_after_double_dash`(295줄), push 옵션 `test_push_option_value_is_not_positional`(306줄, `-o`·`--push-option`·`--receive-pack`·`--repo`), 짧은 옵션 묶음의 `-o` `test_o_in_short_option_bundle`(320줄, `-uo`·`-uoci.skip`·`-do`), 설정의 원격 `test_configured_push_remote_is_origin`(332줄)·`test_configured_remote_other_than_origin`(421줄). 일곱 가지 모두 그 가지를 지나는 시험이 있다. 테스트는 `OK`. 통과
  - 완료 조건 4: 테스트(`OK`)를 마친 뒤 `git clone https://github.com/werwer748/plate-ci-test.git <scratchpad>/ci-test-clone`(`main` `91b8060`, `git fetch` 뒤에도 같음), `git archive 72dcfcf plugins/plate | tar -x -C <scratchpad>/tasks-end`, `diff -r -x __pycache__ <scratchpad>/ci-test-clone/.plate <scratchpad>/tasks-end/plugins/plate` → 출력 없음, 종료 코드 0. 복사본 자리는 시험 저장소 워크플로의 `--plugin-dir ${{ github.workspace }}/.plate`로 봤다. 통과
  - 완료 조건 5: 두 `plugin.json`의 4줄 `description`을 읽음 → 둘 다 "setup이 승인받아 두는 CI 워크플로는 PR마다 review의 PR 모드로 평가하고 판정 스크립트로 자동 머지, 머지 요청, 닫기 가운데 하나를 고른다."와 "에이전트가 기본 브랜치에 하는 푸시를 막는 푸시 훅"이 있다. 통과
  - 완료 조건 6: `docs/TOOLS.md` 83·84줄을 읽음 → "세션에 실린 plate 스킬 본문은 세션을 띄울 때의 것이라, 같은 세션에서 띄운 에이전트에는 tasks가 고치기 전의 본문이 실린다."와 "그래서 스킬의 절차를 바꾸는 tasks는 그 절차에 기대는 다음 단계(확인, 회고, tasks 끝의 평가)를 새 세션에서 이어 간다."가 있다. 통과
  - 완료 조건 7: `docs/ARCHITECTURE.md` 47줄을 읽음 → 테스트와 `--plugin-dir` 세션의 푸시 훅이 `plugins/plate/hooks/__pycache__/`를 만든다는 것과 `plugins/plate`를 복사본과 견주는 확인은 `diff -r -x __pycache__`로 쓴다는 것이 있다. 통과
  - 완료 조건 8: `~/plate-rail-test/bin/run.sh`를 읽음 → 27~28줄, `run|phase|check|retro|review|eval|verify`의 `--allowedTools`에 `"Bash(git push:*)"`가 있다. 통과
  - 완료 조건 9 (PR 번호와 실행 기록은 `docs/tasks/005-publish-verify/done-phase-2.md`~`done-phase-4.md`의 "한 일"에서 읽었다)
    - `python3 -m unittest discover -s tests` → `OK`. `tests/test_verdict.py`를 읽음 → 닫기(명령 `fail`, 보안 B는 머지 요청·C·D·E는 닫기), 자동 머지(`pass`·`none`, 커버리지 79·79.9는 머지 요청·80·80.0은 자동 머지, `skipped`, 등급 A와 B), 머지 요청(`unmeasured`, `unjudged`), 닫기가 모름보다 앞서는 것을 본다. 통과
    - `done-phase-3.md`의 세 장면 #2, #3, #4에 `gh pr view <번호> -R werwer748/plate-ci-test --json state,comments` → `MERGED`, `OPEN`, `CLOSED`. 셋 모두 댓글 하나, 작성자 `github-actions`, 첫 줄 차례로 `판정: 자동 머지`, `판정: 머지 요청`, `판정: 닫기`, 셋째 줄 `# 코드 평가`. 통과
    - 시험 저장소의 복사본 견주기 → 완료 조건 4와 같이 출력 없음, 종료 코드 0. 통과
    - run 장면의 실행 기록: `grep -c 'PR을 열까요'` → `ci-norun-2.jsonl` 2(phase 2), `ci-run-2.jsonl` 2(phase 3). `grep -c 'Should I merge' ci-local-2.jsonl` → 2(phase 4, 원격 없는 장면). `ci-norun-1~3`, `ci-run-1~3`, `ci-local-1~3`의 아홉 기록 모두 `test <기록> -nt plugins/plate/skills/run/SKILL.md` → 참(run 본문 10월 24일 18:24:36, 묻는 기록 19:36:09, 20:46:22, 21:23:24). 통과
    - run 장면의 PR에 `gh pr view <번호> -R werwer748/plate-ci-test --json headRefName,baseRefName,comments` → #1 `tasks/line-count` → `main`, 댓글 하나(작성자 `werwer748`, 첫 줄 `## 평가 1`. CI 워크플로가 없던 장면). #6 `tasks/unique-words` → `main`, 댓글 하나(작성자 `github-actions`, `판정: 자동 머지`). 통과
    - `git -C ~/plate-rail-test/ci-local log --format=%s main` → 첫 줄 `line-count: 비움`. 통과
    - `python3 -m unittest discover -s tests` → `OK`. `tests/test_push_guard.py`에 기본 브랜치로의 푸시(`test_push_to_default_branch` 등), 지우는 푸시(`test_delete_default_branch`), 이어진 명령(`test_push_inside_chained_command`), `git -C`(`test_push_inside_git_c_uses_that_folder`), 다른 브랜치(`test_push_to_other_branch`), origin 밖 원격(`test_push_to_remote_other_than_origin`), 셋업 안 된 프로젝트(`test_project_not_set_up`)의 시험이 있다. 통과
    - `done-phase-4.md`의 푸시 훅 장면 기록 `~/plate-rail-test/logs/ci-push.jsonl` → init의 plate는 `/Users/gangjungi/Desktop/harness-plate/plugins/plate`, `git push origin main` 호출의 `tool_result`가 `is_error: True`, 내용 `PreToolUse:Bash hook error: […push_guard.py…]: plate: 기본 브랜치(`main`)로 푸시하지 않는다: `git push origin main``. `ci-push.state`의 origin `main`은 전과 뒤 모두 `f0fa749…`. `test ~/plate-rail-test/logs/ci-push.jsonl -nt plugins/plate/hooks/push_guard.py` → 참(훅 22:39:32, 기록 22:43:08). 통과
    - `done-phase-2.md`의 setup 장면 기록 → `grep -c 'CI 에이전트를 둘까요' ci-setup-1.jsonl` 2, `ci-setup-2.jsonl`의 `result`에 "## CI 시크릿 등록"과 `claude setup-token`, `gh secret set CLAUDE_CODE_OAUTH_TOKEN`이 있다. `ls ~/plate-rail-test/ci-setup/.github/workflows/` → `plate-review.yml`. 두 기록 모두 `test <기록> -nt plugins/plate/skills/setup/SKILL.md` → 참. 통과
    - `gh repo view werwer748/harness-plate --json visibility -q .visibility` → `PUBLIC`. 통과
    - `GIT_TERMINAL_PROMPT=0 git -c credential.helper= ls-remote https://github.com/werwer748/harness-plate.git HEAD` → `d29c0144082039adc42cc5e07f65bbb499cd71be	HEAD` 한 줄, 종료 코드 0. 통과
    - `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
    - `grep -h '"version"' …` → 두 줄 모두 `"version": "0.11.0",`. 통과
    - `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `README.md`를 읽음 → PR(PRD 18줄, ARCHITECTURE 50·69·72줄, README "tasks 끝의 PR"), CI 판정(PRD 18줄, ARCHITECTURE 17·74줄, ADR-021, README 23~28줄), 푸시 훅(PRD 4줄, ARCHITECTURE 5줄, README 35줄), 설치 줄(ARCHITECTURE 82줄 `- 설치: 없음`), 공개 저장소(ARCHITECTURE 7줄, ADR-022, README 39·43줄)가 있다. "비공개"는 ADR-022의 "비공개에서 공개로 바꿨다"뿐이고, GitHub 원격이 있어도 로컬로 합친다는 글은 없다(합칠지 묻는 것은 원격이 없거나 GitHub이 아닐 때로 적혀 있다). 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 99 tests in 40.184s`, `OK`. 통과

**테스트 먼저 기록**
- "한 일"의 "테스트 먼저" 항목 → 실패 출력(`FAIL: test_split_functions_within_limit … (name='scan') AssertionError: 66 not less than or equal to 15`, `… (name='push_args') AssertionError: 24 not less than or equal to 15`, `FAILED (failures=4)`)이 먼저, 통과 출력(`Ran 99 tests in 42.968s`, `OK`)이 그 뒤에 있다. 통과

**실패**
- 없음

**하네스에서 걸린 것**
- task 머리의 완료 조건 9는 tasks 머리 완료 조건의 확인 줄만 옮겨 와 "세 규칙의 경계", "이 경우들", "그 물음"이 무엇인지 task 머리에 없다. tasks 머리(`docs/tasks/plan.md`)의 완료 조건 1~4를 읽어 풀었다
- 완료 조건 9의 확인이 PR 번호와 실행 기록을 `docs/tasks/005-publish-verify/done-phase-2.md`~`done-phase-4.md`에서 읽게 해 check 스킬 1번의 읽을 것(task 머리, `phase-N.md`, 명령 절) 밖의 파일을 읽었다

**판정**: 통과
