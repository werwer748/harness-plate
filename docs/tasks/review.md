# 코드 평가

## 평가 1

**대상**
- 범위: `807bfc6`(main에서 갈라진 곳)부터 `e2d1f0e`까지
- 결과물인 마크다운 절: `plugins/plate/skills/*/SKILL.md`
- 바뀐 코드 파일 7개, 새 줄 126줄, 잴 새 줄 85줄
  - `plugins/plate/.claude-plugin/plugin.json` +1
  - `plugins/plate/.codex-plugin/plugin.json` +1
  - `plugins/plate/ci/verdict.py` +23
  - `plugins/plate/hooks/edit_guard.py` +3
  - `tests/test_edit_guard.py` +21
  - `tests/test_verdict.py` +36
  - `plugins/plate/skills/setup/SKILL.md` +41 (결과물인 마크다운)

**잰 것**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 104 tests in 18.645s`, 마지막 줄 `OK` (Python 3.9.6). 통과
- 커버리지: 측정 못함 — `python3 -m coverage`가 `No module named coverage`. 명령 절도 커버리지 도구가 없다고 적는다
- 중복: 측정 못함 — 중복 검사 도구가 없다(명령 절, `which jscpd` 없음)
- 정적 분석: `python3 -m py_compile plugins/plate/ci/verdict.py plugins/plate/hooks/edit_guard.py tests/test_verdict.py tests/test_edit_guard.py` → 오류 없음. pyflakes, pylint, mypy는 설치돼 있지 않아 측정 못함
- 보안 검사: 측정 못함 — bandit, semgrep, pip-audit가 없고 의존성 목록도 없다

**완료 조건**
- 1. 시험 저장소의 다섯 장면 결과와 ruleset JSON이 `docs/TOOLS.md`에 있다
  - `docs/TOOLS.md`의 "ruleset과 CODEOWNERS로 워크플로 PR의 자동 머지를 막는지 본 것" 절을 읽었다 → ruleset JSON 있음. 장면 1: PR #18, `gh workflow run … -f pr=18`, 실행 `40352179658`, MERGED. 장면 2: PR #19, 실행 `40352503804` failure, 오류 글 `…the base branch policy prohibits the merge.`. 장면 3: PR #20, 실행 `40352605265`, MERGED. 장면 4: 장면 3과 같은 실행 `40352605265`(PR #20의 워크플로)의 `git push origin HEAD:main`, 오류 글 `GH013 … Changes must be made through a pull request.`. 장면 5: PR #19, `gh pr merge 19 … --admin`, MERGED. 통과 (장면 4의 줄에는 PR 번호가 직접 없고 장면 3의 실행 id로 PR #20을 가리킨다)
- 2. 판정 스크립트의 워크플로 검사
  - `python3 -m unittest discover -s tests` → `OK`. 통과
  - `tests/test_verdict.py:120-141`을 읽었다 → 워크플로 경로면 request(`test_workflow_path_turns_merge_into_request`), close와 request 그대로(`test_workflow_path_keeps_close_and_request`), 목록 없음·워크플로 없음은 그대로(`test_no_list_or_no_workflow_path_is_unchanged`). 통과
- 3. 편집 훅의 CODEOWNERS 예외
  - `python3 -m unittest discover -s tests` → `OK`. 통과
  - `tests/test_edit_guard.py:245-253, 278-287`을 읽었다 → 처음 쓰기는 통과, 이미 있으면 막음이 계획 먼저와 테스트 먼저 두 경우에 다 있다. 통과
- 4. setup의 CODEOWNERS와 ruleset 안내
  - `plugins/plate/skills/setup/SKILL.md`의 1번(52줄 login 판정), 2번 표(65줄: login을 보여 주고 CODEOWNERS 두 줄을 알림), 3번(87-92줄: 없을 때만 쓴다, 이미 있는 것은 고치지 않는다), 4번(118-143줄: 쓰지 않은 까닭과 넣을 줄, gh api 명령, Settings 경로, 비공개 저장소의 요금제 조건, 유일한 코드 소유자 한계와 닫는 법), 양식(426-427줄: `gh pr diff "$PR" --name-only > changed-files.txt`, `--changed-files changed-files.txt`)을 읽었다 → 네 곳이 모두 적는다. 통과
  - setup 보고의 JSON(SKILL.md 123-138줄)과 `docs/TOOLS.md`의 시험한 JSON을 견줬다 → `name`만 다르고 `target`, `conditions`, `rules`, `bypass_actors`가 같다. 통과
- 5. 버전, 마켓플레이스, 테스트, 맥락 문서와 README
  - `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "0.14.0",`. 통과
  - `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
  - `python3 -m unittest discover -s tests` → `OK`. 통과
  - `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`(ADR-023), `README.md`를 따로 읽었다 → CODEOWNERS와 ruleset, 판정의 워크플로 검사, 편집 훅의 CODEOWNERS 예외가 코드와 SKILL.md와 맞고 어긋나는 줄을 찾지 못했다. 통과

**범주**
- 신뢰성
  - 근거: `plugins/plate/skills/setup/SKILL.md:426` 양식의 verdict 단계가 판정 전에 `gh pr diff "$PR" --name-only`를 돌린다. 이 명령은 PR의 diff 전체를 받아 이름을 뽑으므로, GitHub이 diff를 내주지 않는 큰 PR(diff API의 파일 수·크기 한도를 넘는 PR)에서는 실패하고, Actions의 `bash -e`로 단계가 그 자리에서 끝나 판정 댓글도 닫기도 일어나지 않는다. 이 줄이 들어가기 전에는 그런 PR도 판정을 받았다. 안전한 쪽(자동 머지 안 함)으로 틀리지만 판정이 사라진다 (기능, 중간)
  - `plugins/plate/ci/verdict.py:53-65`의 검사는 merge일 때만 목록을 읽고, 빈 목록·`docs/.github/workflows/` 같은 접두가 아닌 경로·close/request 유지를 시험이 확인한다. `plugins/plate/hooks/edit_guard.py:214`의 예외는 기존 CI 워크플로 예외와 같은 조건(파일이 없을 때만)이라 새 결함을 찾지 못했다
  - 등급: C — 가장 무거운 문제가 중간
- 보안
  - 핫스팟: `plugins/plate/ci/verdict.py:63` 인자로 받은 경로의 파일을 연다 → 안전 (워크플로가 만든 `changed-files.txt`를 넘기고, 내용은 `startswith` 비교에만 쓴다)
  - 핫스팟: `plugins/plate/skills/setup/SKILL.md:426` PR이 정한 파일 이름이 목록에 들어간다 → 안전 (이름은 셸로 풀리지 않고 파일로만 넘어간다. 줄바꿈이 든 이름이 워크플로 경로처럼 보여도 결과는 request 쪽이다)
  - 핫스팟: `plugins/plate/skills/setup/SKILL.md:123-138` 보고가 권하는 ruleset의 우회 목록 `actor_id: 5`(Repository admin), `bypass_mode: pull_request` → 안전 (`docs/TOOLS.md`의 장면 5에서 관리자만 PR로 우회했고 github-actions는 막혔다)
  - 근거: 문제 없음. PR이 워크플로 자체를 고쳐 검사를 건너뛰는 길과 유일한 코드 소유자 한계는 tasks 머리의 결정이 정한 것이라 문제로 적지 않는다
  - 등급: A — 문제 0개
- 유지보수성
  - 근거: 문제 없음. `verdict.py`는 docstring에 새 인자를 적었고 상수(`WORKFLOW_PREFIX`)와 작은 함수(`touches_workflow`)로 나눴다. `edit_guard.py`는 `SETUP_FILES` 튜플로 예외를 한곳에 모았다. 시험 도우미 `verdict(changed_files=None, …)`는 기존 호출을 바꾸지 않는다. SKILL.md의 새 글은 맥락 문서(ARCHITECTURE의 패턴과 규칙, ADR-023)와 맞고, "일곱 가지를 판정"으로 개수도 고쳤다
  - 부채 비율: 0분 ÷ (126줄 × 30분) = 0%
  - 등급: A — 부채 비율 5% 이하
- 테스트 적절성
  - 근거: `tests/test_verdict.py:120-141` 판정 스크립트의 새 동작(워크플로 경로 → request, close·request 유지, 목록 없음·워크플로 없음 그대로)마다 시험이 있고, `touches_workflow`나 `main`의 분기가 깨지면 실패한다
  - 근거: `tests/test_edit_guard.py:245-253, 278-287` CODEOWNERS 처음 쓰기 통과와 기존 파일 막음을 계획 먼저·테스트 먼저 두 경로에서 본다. `SETUP_FILES`에서 CODEOWNERS를 빼면 실패한다
  - 근거: `plugins/plate/skills/setup/SKILL.md:52, 87-92, 426` setup의 주된 새 동작(login 읽기, CODEOWNERS 쓰기·건너뛰기, 양식의 바뀐 파일 목록 단계)은 자동 시험도 시험 저장소에서 돌린 기록도 이 tasks의 코드에 없다. 시험 저장소의 장면은 손으로 넣은 CODEOWNERS와 ruleset을 봤고, setup이 쓴 파일이나 새 양식의 verdict 단계는 돌리지 않았다
  - 등급: C — 커버리지는 측정 못함이라 판단만으로 매겼다. 주된 동작 가운데 테스트가 없는 것이 있다
- 기능 적합성
  - 근거: 완료 조건 1 통과: 다섯 장면과 ruleset JSON이 있다(장면 4는 장면 3의 실행 id로 PR #20을 가리킨다)
  - 근거: 완료 조건 2 통과: 테스트 OK, 세 경우의 시험이 있다
  - 근거: 완료 조건 3 통과: 테스트 OK, 두 경우의 시험이 있다
  - 근거: 완료 조건 4 통과: SKILL.md의 네 곳이 적고 JSON이 같다
  - 근거: 완료 조건 5 통과: 버전 0.14.0 두 줄, `✔ Validation passed`, 테스트 OK, 문서 넷이 어긋나지 않는다
  - 등급: A — 완료 조건의 확인이 모두 통과한다

**Sonar way 게이트**
- 새 문제 0개: 1개. 실패
- 새 보안 핫스팟 모두 검토: 3/3. 통과
- 새 줄 커버리지 80% 이상: 측정 못함 (잴 새 줄 85줄). 측정 못함
- 새 줄 중복 3% 이하: 측정 못함 (잴 새 줄 85줄). 측정 못함
- 게이트: 실패

**소스 문제**
1. CI 양식의 verdict 단계가 판정 전에 `gh pr diff "$PR" --name-only`를 돌려, diff를 받지 못하는 큰 PR에서는 단계가 실패해 판정 댓글과 닫기가 사라진다. 바뀐 파일 목록은 diff가 아니라 파일 목록 API(`gh api --paginate repos/$GH_REPO/pulls/$PR/files --jq '.[].filename'` 같은 것)로 받거나, 실패하면 워크플로 경로가 있는 것으로 보고 request로 내리는 편이 안전하다 (`plugins/plate/skills/setup/SKILL.md:426`). 범주: 신뢰성
2. setup의 새 동작(login 읽기, CODEOWNERS 쓰기·건너뛰기)과 양식의 바뀐 파일 목록 단계가 자동 시험이나 시험 저장소 실행으로 확인되지 않았다 (`plugins/plate/skills/setup/SKILL.md:52`, `:87-92`, `:426`). 범주: 테스트 적절성

**하네스에서 걸린 것**
- 명령 절이 커버리지·중복·보안 검사 도구를 두지 않는다고 적어, 게이트의 커버리지와 중복이 측정 못함으로 남았다. 정적 분석도 `py_compile`밖에 돌릴 것이 없었다
- 완료 조건 1의 확인은 "다섯 장면이 저마다 PR 번호를 적었다"인데 `docs/TOOLS.md`의 장면 4 줄은 장면 3의 실행 id로만 PR을 가리킨다. 실행 id로 PR #20이 정해지므로 통과로 봤다
- 완료 조건이 setup 스킬의 새 동작을 "SKILL.md를 읽어 적혀 있다"로만 확인해, setup이 실제로 CODEOWNERS를 쓰는지와 새 양식의 verdict 단계가 도는지는 tasks 안에서 한 번도 돌지 않았다
- 평가를 시작할 때 작업 트리에 이 평가와 무관한 `docs/tasks/RUNLOG.md` 변경이 있었다. 커밋에는 `review.md`만 넣었다
