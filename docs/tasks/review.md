# 코드 평가

## 평가 1

**대상**
- 범위: `7616256`(main에서 갈라진 곳)부터 `ee51e3d`까지
- 바뀐 코드 파일 9개, 새 줄 940줄
  - `plugins/plate/hooks/push_guard.py` +297
  - `tests/test_push_guard.py` +434
  - `tests/test_verdict.py` +114
  - `plugins/plate/ci/verdict.py` +51
  - `tests/test_edit_guard.py` +28
  - `plugins/plate/hooks/hooks.json` +9
  - `plugins/plate/hooks/edit_guard.py` +5
  - `plugins/plate/.claude-plugin/plugin.json` +1
  - `plugins/plate/.codex-plugin/plugin.json` +1

**잰 것**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 89 tests in 34.244s`, `OK`. 통과
- 커버리지: `PYTHONPATH=<scratchpad>/cov/site PLATE_COV_OUT=<scratchpad>/cov/data PLATE_COV_ROOT=<레포>/plugins/plate python3 -m unittest discover -s tests`(표준 라이브러리 `trace` 모듈을 `sitecustomize.py`로 모든 Python 프로세스에 걸었다. 테스트가 훅과 판정 스크립트를 subprocess로 돌리기 때문이다. 실행할 수 있는 줄은 `trace._find_executable_linenos`로, 새 줄은 `git diff -U0 7616256 HEAD`로 셌다) → 새 줄 가운데 커버리지 대상 255줄(소스 파일의 실행할 수 있는 새 줄. 테스트 파일과 JSON은 뺀다) 가운데 243줄, 95.3%. 파일마다 `push_guard.py` 218/230(빠진 줄 71, 72, 150, 161, 162, 176, 177, 183, 191, 192, 193, 223), `verdict.py` 22/22, `edit_guard.py` 3/3
- 중복: 측정 못함 — jscpd, PMD CPD, SonarQube 같은 중복 검사 도구가 이 환경에 없다(`which`, `npm ls -g`, `python3 -m pip list`로 봄)
- 정적 분석: `python3 -I -W error -c "compile(…)"`(바뀐 `.py` 여섯), `python3 -I -m json.tool`(바뀐 `.json` 셋), `PYTHONDEVMODE=1 python3 -m unittest discover -s tests` → 문법 오류와 컴파일 경고 없음, JSON 셋 모두 유효, 개발 모드 실행(89개 `OK`)에서 경고 없음. 타입 검사(mypy, pyright)와 복잡도 검사(radon, lizard) 도구는 없어 돌리지 못했다
- 보안 검사: 측정 못함 — pip-audit, bandit, semgrep 같은 도구가 이 환경에 없다. 의존성 목록 파일(`requirements*.txt`, `pyproject.toml`, `package.json`)도 없고 바뀐 코드는 표준 라이브러리만 쓴다

**완료 조건**
- 1. CI 워크플로를 둔 저장소에서 PR이 열리면 CI가 PR의 코드를 평가해 평가서를 PR 댓글로 달고, 세 판정 규칙대로 자동 머지, 머지 요청, 닫기 가운데 하나가 된다.
  - `python3 -m unittest discover -s tests` → 89개 `OK`. `tests/test_verdict.py`를 읽음 → 커버리지 79·79.9·80·80.0, 신뢰성·보안·유지보수성의 A와 B, 보안의 B와 C·D·E, `unmeasured`·`unjudged`, 빌드·린트·테스트의 `fail`, `skipped`, 닫기가 모름보다 앞서는 것을 본다. 통과
  - `gh pr view <번호> -R werwer748/plate-ci-test --json state,comments`(#2, #3, #4. 번호는 `docs/tasks/005-publish-verify/done-phase-3.md`의 기록) → #2 `MERGED`, #3 `OPEN`, #4 `CLOSED`. 셋 모두 댓글 하나, 작성자 `github-actions`, 첫 줄이 차례로 `판정: 자동 머지`, `판정: 머지 요청`, `판정: 닫기`이고 셋째 줄이 `# 코드 평가`. 통과
  - `git clone https://github.com/werwer748/plate-ci-test.git <scratchpad>/ci-test-clone`(HEAD `91b8060`) 뒤 `diff -r <scratchpad>/ci-test-clone/.plate plugins/plate` → `Only in /Users/gangjungi/Desktop/harness-plate/plugins/plate/hooks: __pycache__`(종료 코드 1). `diff -r -x __pycache__`로는 아무것도 나오지 않는다. 다른 것은 `.gitignore`의 `__pycache__/`에 걸린 `edit_guard.cpython-313.pyc`(10월 24일 20:56)뿐이다. 실패
- 2. GitHub 원격이 있는 프로젝트에서 run이 tasks 끝에 `docs/tasks/`를 비운 뒤 PR을 열지 묻고, 승인하면 tasks 브랜치를 푸시해 기본 브랜치로 가는 PR을 연다. plate의 CI 워크플로가 없으면 로컬 평가서를 PR 댓글로 단다. GitHub 원격이 없으면 지금처럼 합칠지 묻는다.
  - 기록의 경로는 `done-phase-2.md`, `done-phase-3.md`, `done-phase-4.md`에서 읽음. `grep -c 'PR을 열까요' ~/plate-rail-test/logs/ci-norun-2.jsonl` → 2, `grep -c 'PR을 열까요' ~/plate-rail-test/logs/ci-run-2.jsonl` → 2, `grep -c 'Should I merge' ~/plate-rail-test/logs/ci-local-2.jsonl` → 2. 셋 모두 `test <기록> -nt plugins/plate/skills/run/SKILL.md` → 참. 통과
  - `gh pr view <번호> -R werwer748/plate-ci-test --json headRefName,baseRefName,comments`(#1 CI 없는 장면, #6 CI 있는 장면) → #1 `tasks/line-count` → `main`, 댓글 하나(작성자 `werwer748`, 첫 줄 `## 평가 1`인 평가서). #6 `tasks/unique-words` → `main`, 댓글 하나(작성자 `github-actions`). 통과
  - `git -C ~/plate-rail-test/ci-local log --format=%s main` → 첫 줄 `line-count: 비움`. 통과
- 3. 셋업된 프로젝트에서 에이전트가 기본 브랜치로 푸시하면 plate의 훅이 막는다. 기본 브랜치를 지우는 푸시, 이어진 명령과 `git -C` 안의 push도 막는다. 다른 브랜치나 origin 밖 원격으로의 푸시, 셋업 안 된 프로젝트의 푸시는 막지 않는다.
  - `python3 -m unittest discover -s tests` → 89개 `OK`. `tests/test_push_guard.py`를 읽음 → 대상 없는 push(90줄), 기본 브랜치를 가리키는 push(102줄), 지우는 push(123줄), 이어진 명령(198줄), `git -C`(228, 236줄), 다른 브랜치(269줄), origin 밖 원격(300줄), 셋업 안 된 프로젝트(345줄)의 시험이 있다. 통과
  - `~/plate-rail-test/logs/ci-push.jsonl`(경로는 `done-phase-4.md`) → `git push origin main` 호출의 `tool_result`가 `is_error: true`이고 내용이 `PreToolUse:Bash hook error: [f=".../plugins/plate/hooks/push_guard.py"; …]: plate: 기본 브랜치(`main`)로 푸시하지 않는다: `git push origin main``. `test ~/plate-rail-test/logs/ci-push.jsonl -nt plugins/plate/hooks/push_guard.py` → 참. 통과
- 4. GitHub 원격이 있는 프로젝트에서 setup이 CI 워크플로를 둘지 묻고, 승인하면 워크플로 파일을 쓰고 보고에 시크릿 등록 방법을 적는다.
  - `grep -c 'CI 에이전트를 둘까요' ~/plate-rail-test/logs/ci-setup-1.jsonl` → 2, `grep -c 'CLAUDE_CODE_OAUTH_TOKEN' ~/plate-rail-test/logs/ci-setup-2.jsonl` → 4, `ls ~/plate-rail-test/ci-setup/.github/workflows/` → `plate-review.yml`, 두 기록 모두 `test <기록> -nt plugins/plate/skills/setup/SKILL.md` → 참. 통과
- 5. harness-plate가 공개 저장소이고 그 마켓플레이스가 유효하다.
  - `gh repo view werwer748/harness-plate --json visibility -q .visibility` → `PUBLIC`. 통과
  - `GIT_TERMINAL_PROMPT=0 git -c credential.helper= ls-remote https://github.com/werwer748/harness-plate.git HEAD` → `d29c0144082039adc42cc5e07f65bbb499cd71be	HEAD` 한 줄. 통과
  - `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
- 6. 맥락 문서, README, 두 매니페스트가 바뀐 동작과 맞고 플러그인 버전이 0.11.0이다.
  - `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "0.11.0",`. 통과
  - `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `README.md`를 읽음 → PR(PRD 18줄, ARCHITECTURE 49줄과 데이터 흐름, README "tasks 끝의 PR"), CI 판정(ARCHITECTURE 50줄, ADR-021, README "CI 워크플로"의 표), 푸시 훅(PRD 4줄, ARCHITECTURE 5·48줄, README "훅"), 명령 절의 설치 줄(ARCHITECTURE 81줄 `- 설치: 없음`과 50줄 "PR 모드는 명령 절의 설치를 먼저 돌린 뒤"), 공개 저장소(ARCHITECTURE 7줄, ADR-022, README "설치")가 있다. 옛 동작은 ADR-022의 "비공개에서 공개로 바꿨다"는 이력 말고는 없다. 통과
  - 조건의 "두 매니페스트가 바뀐 동작과 맞고"를 보려 `plugins/plate/.claude-plugin/plugin.json:4`와 `plugins/plate/.codex-plugin/plugin.json:4`의 `description`을 읽음 → 훅을 "계획 없는 코드 편집과, 테스트 먼저인 phase에서 테스트보다 앞선 구현을 막는 훅"으로만 적고 푸시 훅을 적지 않는다(README 35줄은 "훅 둘이 함께 돈다"). review의 PR 모드와 판정 스크립트도 적지 않는다. 실패

**범주**
- 신뢰성
  - 근거: 문제 없음. `push_guard.py` 1~297줄, `verdict.py` 1~51줄, `edit_guard.py` 23·212~215줄, `hooks.json` 12~20줄의 새 줄을 모두 읽고 `docs/ARCHITECTURE.md`의 막는 장치(48줄)와 CI 흐름(50줄), task 머리의 결정에 대었다. `verdict.py:33`~42는 세 규칙과 그 우선(닫기 → 자동 머지 → 머지 요청)을 그대로 따르고, 모르는 값과 빠진 키는 머지 요청으로 간다. `push_guard.py:125`~128은 따옴표·이스케이프를 나누지 못하면 `ValueError`를 잡아 셋업된 프로젝트에서 막는 쪽(`UNSPLIT`)으로 가고, `scan`(67~119줄)의 반복은 갈래마다 `i`를 늘리거나 돌아와 멈춘다. 테스트 89개 통과, 개발 모드 실행에서 경고 없음. 시험이 다루지 않는 셸 구문과 git 표기에서 놓치거나 잘못 막는 것은 `003-push-guard`의 결정이 결함에서 뺐으므로 문제로 적지 않았다
  - 등급: A — 문제 0개
- 보안
  - 핫스팟: `plugins/plate/hooks/push_guard.py:159` 명령 글의 `git -C <폴더>`를 받아 `setup_root`(242줄)가 그 폴더에서 `git rev-parse`를 돌린다 → 안전: `subprocess.run`에 인자 목록으로 넘겨 셸을 거치지 않고(`edit_guard.py:46`~50), 읽기만 하는 하위 명령(`rev-parse`, `symbolic-ref`, `config --get`)만 돈다
  - 핫스팟: `plugins/plate/hooks/push_guard.py:217`~221 브랜치 이름으로 git 설정 키를 만들어 읽는다 → 안전: 인자 목록이고 `config --get`으로 읽기만 한다
  - 핫스팟: `plugins/plate/hooks/edit_guard.py:212`~215 아직 없는 `.github/workflows/plate-review.yml`의 쓰기는 편집 훅의 두 막음을 건너뛴다 → 안전: `002-ci-workflow`의 결정이 정한 예외이고, 이미 있는 그 파일과 다른 워크플로 파일은 그대로 막으며(`tests/test_edit_guard.py:234`~271), 편집 훅은 Bash를 보지 않아 처음부터 보안 경계가 아니다(`edit_guard.py:6`)
  - 핫스팟: `plugins/plate/ci/verdict.py:46` CI에서 PR 코드를 읽은 에이전트가 만든 등급 묶음을 stdin으로 받는다 → 안전: `json.load`로 읽어 정해 둔 값과 견주기만 하고, 정해 둔 값이 아니면 자동 머지로 가지 않는다(36~42줄)
  - 핫스팟: `plugins/plate/hooks/hooks.json:18` 훅 명령을 셸로 돌린다 → 안전: 경로를 큰따옴표로 감싸고 파일이 있을 때 `exec python3 "$f"`만 한다
  - 근거: 문제 없음. 위 핫스팟 다섯 말고 비밀, 주입, 권한을 다루는 새 줄이 없다. 보안 검사 도구로는 재지 못했다
  - 등급: A — 문제 0개
- 유지보수성
  - 근거: `plugins/plate/hooks/push_guard.py:62` `scan`의 인지 복잡도가 어림 67로 Sonar 규칙 python:S3776의 기준 15를 크게 넘는다. while 하나 안에서 이스케이프, 명령 치환(재귀), 따옴표, 괄호 깊이, `#` 주석, heredoc의 시작과 본문 건너뛰기가 상태 넷(`quote`, `depth`, `pending`, `word_start`)을 함께 쓰고 4단까지 겹친다. `003-push-guard`의 결정에 적힌 대로 셸 꼴 하나를 고칠 때마다 앞서 막던 꼴이 깨졌던 곳이다 (복잡도, 57분)
  - 근거: `plugins/plate/hooks/push_guard.py:168` `push_args`의 인지 복잡도가 어림 24로 기준 15를 넘는다. while 안의 갈래 일곱과 짧은 옵션 묶음의 for 안 if가 4단까지 겹친다 (복잡도, 14분)
  - 부채 비율: 71분 ÷ (940줄 × 30분) = 0.25%
  - 등급: A — 부채 비율 5% 이하
- 테스트 적절성
  - 근거: 새 줄 커버리지 95.3%(커버리지 대상 255줄 가운데 243줄)
  - 근거: `tests/test_verdict.py` 세 규칙의 경계(커버리지 79·80, A·B, 보안 B·C), 모름, `skipped`, 닫기의 우선을 본다. `tests/test_edit_guard.py:234`~271 CI 워크플로 예외를 남은 phase 없음, 테스트 먼저, 테스트 먼저 아님에서 보고 이미 있는 파일과 다른 워크플로의 막음도 본다. `tests/test_push_guard.py`는 완료 조건 3의 경우마다와 heredoc, 주석, 줄 잇기, 명령 치환, 나누지 못한 명령, `hooks.json`의 명령(419~430줄)을 본다
  - 근거: `plugins/plate/hooks/push_guard.py:71`~72, 150, 161~162, 176~177, 183, 191~193, 223 시험이 지나가지 않는 가지 일곱 곳이다. 따옴표 밖의 `\`+글자, `VAR=값 git push`, `git -c <설정> push` 같은 git 옵션의 값 건너뛰기, `--` 뒤의 위치 인자, `-o`·`--repo` 같은 push 옵션의 값 건너뛰기, 짧은 옵션 묶음 안의 `-o`, 설정(`branch.<이름>.pushRemote`, `remote.pushDefault`, `branch.<이름>.remote`)에서 원격 읽기다. 지금은 바르게 돈다(`git -c k=v push origin main`, `GIT_TRACE=1 git push origin main`, `git push -o ci.skip origin main`, `git commit -m "a \" b" && git push origin main`을 시험 프로젝트에서 훅에 주어 모두 종료 코드 2). 하지만 이 가지가 깨져도 실패하는 시험이 없다. 예를 들어 161~162줄이 빠지면 `git -c k=v push origin main`은 push로 읽히지 않아 통과한다. 모두 옵션과 설정의 엣지케이스다
  - 등급: B — 커버리지는 90% 이상(A 칸)이지만 시험이 빠진 동작이 있고 그것이 엣지케이스뿐이라(B 칸) 낮은 쪽으로 매김
- 기능 적합성
  - 근거: 완료 조건 1 실패: 셋째 확인의 `diff -r`가 `plugins/plate/hooks/__pycache__`를 다른 것으로 낸다. 추적되는 파일은 복사본과 같다(`-x __pycache__`로 아무것도 나오지 않음). 첫째와 둘째 확인은 통과
  - 근거: 완료 조건 2 통과: 세 기록의 물음과 시각, #1·#6의 브랜치와 댓글, `ci-local`의 `line-count: 비움`
  - 근거: 완료 조건 3 통과: 테스트 89개 통과, 경우마다 시험이 있음, `ci-push.jsonl`의 막힌 결과와 시각
  - 근거: 완료 조건 4 통과: 물음, 시크릿 안내, 워크플로 파일, 시각
  - 근거: 완료 조건 5 통과: `PUBLIC`, 자격 증명 없는 `ls-remote`, `✔ Validation passed`
  - 근거: 완료 조건 6 실패: 버전과 네 문서의 확인은 통과했지만 두 매니페스트의 `description`이 푸시 훅과 CI(review의 PR 모드, 판정 스크립트)를 적지 않아 바뀐 동작과 다 맞지 않는다
  - 등급: B — 실패한 확인이 있지만 결과물의 동작은 맞다(확인 명령이 `.gitignore`에 걸린 바이트코드까지 견준다, 매니페스트의 문서만 어긋난다)

**Sonar way 게이트**
- 새 문제 0개: 2개(신뢰성 0, 보안 0, 유지보수성 2). 실패
- 새 보안 핫스팟 모두 검토: 5/5. 통과
- 새 줄 커버리지 80% 이상: 95.3%. 통과
- 새 줄 중복 3% 이하: 측정 못함
- 게이트: 실패

**소스 문제**
1. `scan`의 인지 복잡도가 어림 67로 기준 15를 넘어, 셸 꼴 하나를 고칠 때 다른 꼴을 깨뜨리기 쉽다 (`plugins/plate/hooks/push_guard.py:62`). 범주: 유지보수성
2. `push_args`의 인지 복잡도가 어림 24로 기준 15를 넘는다 (`plugins/plate/hooks/push_guard.py:168`). 범주: 유지보수성
3. 푸시 훅의 옵션과 설정을 읽는 가지 일곱 곳(따옴표 밖 이스케이프, 환경 변수 앞붙임, `git -c` 같은 git 옵션, `--`, `-o`·`--repo` 같은 push 옵션, 짧은 옵션 묶음의 `-o`, 설정의 원격)에 시험이 없어 깨져도 알 수 없다 (`plugins/plate/hooks/push_guard.py:71`). 범주: 테스트 적절성
4. 완료 조건 1의 셋째 확인 `diff -r <복사본> plugins/plate`가 `.gitignore`에 걸린 `__pycache__`를 다른 것으로 내어 실패한다. 추적되는 파일은 같다 (`plugins/plate/hooks/__pycache__`). 범주: 기능 적합성
5. 두 매니페스트의 `description`이 0.11.0의 푸시 훅과 CI(review의 PR 모드, 판정 스크립트)를 적지 않는다 (`plugins/plate/.claude-plugin/plugin.json:4`, `plugins/plate/.codex-plugin/plugin.json:4`). 범주: 기능 적합성

**하네스에서 걸린 것**
- review 스킬 2번: 이 환경에 커버리지, 중복, 타입·복잡도, 보안 검사 도구가 하나도 없다. 테스트가 훅과 판정 스크립트를 subprocess로 돌려 한 프로세스만 재는 방법으로는 잴 수 없어, 커버리지는 표준 라이브러리 `trace`를 scratchpad의 `sitecustomize.py`로 모든 Python 프로세스에 걸어 쟀다. 인지 복잡도는 도구 없이 Sonar의 셈법으로 손으로 센 어림이다. 중복과 보안 검사는 측정 못함이다
- tasks 머리의 완료 조건 1 셋째 확인(`diff -r <복사본> plugins/plate`)은 `.gitignore`에 걸린 파일을 빼지 않는다. 같은 조건의 첫째 확인(`python3 -m unittest discover -s tests`)이 `push_guard.py`의 `from edit_guard import …`로 `plugins/plate/hooks/__pycache__/`를 만들 수 있어, 확인을 차례대로 돌리면 셋째 확인이 실패한다
- review 스킬 1번은 task 폴더의 기록을 읽지 않게 하지만, tasks 머리 완료 조건 1~4의 확인은 `docs/tasks/005-publish-verify/done-phase-2.md`~`done-phase-4.md`에 적힌 실행 기록의 경로와 PR 번호를 읽어야 돈다. 3번(확인을 모두 돌린다)을 따라 그 파일에서 경로와 PR 번호가 적힌 줄만 읽었고, 등급의 근거로는 쓰지 않았다
