# Phase 1: tasks 끝의 문제를 고친다

**목표**: task 머리의 완료 조건에 적힌 것을 모두 고친다.

**테스트 먼저**: 아니오 — 고칠 파일이 `plugins/plate/skills/setup/SKILL.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`로 모두 `.md`다

**읽을 것**
- `docs/tasks/review.md`의 `## 평가 1` 절
- `docs/tasks/eval.md`의 `## eval 1` 절
- `plugins/plate/skills/setup/SKILL.md`
- `/private/tmp/claude-501/-Users-hugo-Desktop-harness-plate/02098b8e-c6ca-47f0-9084-5888a2489f05/scratchpad/log/investigation.md`와 같은 폴더의 JSON·`.out` 파일 (완료 조건 5에서 옮길 근거)
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/ADR.md`
- `docs/TOOLS.md`

**TODO**
- [x] CI 양식의 verdict 단계가 바뀐 파일 목록을 `gh pr diff` 대신 파일 목록 API로 받고, 받지 못하면 request로 내린다 (`plugins/plate/skills/setup/SKILL.md`)
- [x] 고친 양식의 verdict 단계를 시험 저장소에서 워크플로를 바꾼 PR과 바꾸지 않은 PR로 돌리고, setup의 CODEOWNERS 쓰기·건너뛰기를 임시 git 저장소에서 따라 해, 결과를 `docs/TOOLS.md`의 새 절에 적는다 (`docs/TOOLS.md`)
- [x] 커버리지·중복·정적 분석 도구를 명령 절에 더하거나, 두지 않는다는 결정을 ADR로 적는다 (`docs/ARCHITECTURE.md`, `docs/ADR.md`)
- [x] 장면 4 줄에 PR #20을 적는다 (`docs/TOOLS.md`)
- [x] scratchpad의 조사 근거(PR #12~#17, 422 응답, ruleset JSON)를 `docs/TOOLS.md`의 그 절로 옮긴다 (`docs/TOOLS.md`)

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다

## 한 일
- CI 양식의 verdict 단계가 바뀐 파일 목록을 `gh pr diff` 대신 파일 목록 API로 받고, 받지 못하면 request로 내린다: 양식의 `gh pr diff "$PR" --name-only > changed-files.txt` 한 줄을 `if ! gh api --paginate "repos/$GH_REPO/pulls/$PR/files" --jq '.[].filename' > changed-files.txt; then echo '.github/workflows/' > changed-files.txt; fi`로 바꿨다. 실패하면 목록에 워크플로 경로 한 줄이 들어가 판정 스크립트가 merge를 request로 내린다(close는 그대로). 양식 위의 설명 글, `docs/ARCHITECTURE.md`의 CI 설명, `README.md`의 바뀐 파일 목록 설명과 0.14.0 전 프로젝트의 손 작업 3번도 같은 글로 맞췄다 (`plugins/plate/skills/setup/SKILL.md`, `docs/ARCHITECTURE.md`, `README.md`)
- 고친 양식의 verdict 단계를 시험 저장소에서 돌리고, setup의 CODEOWNERS 쓰기·건너뛰기를 임시 git 저장소에서 따라 해 결과를 적었다: `werwer748/plate-ci-test`에 고친 verdict 단계와 새 `verdict.py`를 PR #22(머지 커밋 `2a9f0eb`)로 넣은 뒤, 워크플로를 바꾸지 않은 코드 PR #25(실행 `40431626685`, 모두 A → 자동 머지, `MERGED` by `app/github-actions`)와 워크플로를 바꾼 PR #24(실행 `40431431712`, 모두 A → 머지 요청, `OPEN`)를 돌렸다. README만 바꾼 PR #23(실행 `40431424749`)은 등급 `unjudged`라 장면에서 뺐다. 목록 API 실패 길은 로컬에서 `PR=999999`로 돌려 `request`를 봤다. CODEOWNERS는 `mktemp -d`의 새 git 저장소 둘에서 셸 스크립트(`/private/tmp/claude-501/-Users-hugo-Desktop-harness-plate/02098b8e-c6ca-47f0-9084-5888a2489f05/scratchpad/codeowners-sim.sh`)로 setup 1~4번을 따라 해, 없을 때 두 줄을 쓰고 있을 때 기존 내용을 두고 보고 줄을 내는 것을 봤다. 새 절 "verdict 단계의 바뀐 파일 목록과 setup의 CODEOWNERS를 돌려 본 것"에 적었다. 시험 뒤 PR #23, #24는 닫고 브랜치를 지웠다 (`docs/TOOLS.md`)
- 커버리지·중복·정적 분석 도구를 명령 절에 더하거나, 두지 않는다는 결정을 ADR로 적는다: 두지 않기로 하고 ADR-024를 더했다(이유: 표준 라이브러리만 쓴다는 ADR-019, 이 Mac의 python3에 `coverage`, `pyflakes`가 없음). 명령 절의 기존 "두지 않는다" 줄 끝에 `(ADR-024)`를 달았다 (`docs/ADR.md`, `docs/ARCHITECTURE.md`)
- 장면 4 줄에 PR #20을 적는다: "PR #20의 같은 실행 `40352605265`"로 고쳤다 (`docs/TOOLS.md`)
- scratchpad의 조사 근거(PR #12~#17, 422 응답, ruleset JSON)를 `docs/TOOLS.md`의 그 절로 옮긴다: "막지 못한 다른 설정" 아래에 `investigation.md`의 PR 표(#11~#17), 422가 난 두 ruleset JSON과 응답 전문, `probe-base` ruleset의 차이, 조사가 끝난 상태를 옮겼다 (`docs/TOOLS.md`)

## 확인 결과
- 완료 조건 1: verdict 단계가 `gh pr diff`로 받지 않고, 못 받으면 request로 내리는 길
  - `sed -n 418,432p plugins/plate/skills/setup/SKILL.md` → `gh api --paginate "repos/$GH_REPO/pulls/$PR/files"`와 실패 때 `echo '.github/workflows/' > changed-files.txt`. `grep -nF "pr diff"`는 330줄의 "`gh pr diff`는 diff가 너무 큰 PR에서 실패한다" 설명만 낸다. 통과
- 완료 조건 2: `docs/TOOLS.md`의 새 절
  - 새 절을 읽었다 → 워크플로를 바꾼 PR #24(실행 `40431431712`, 머지 요청), 바꾸지 않은 PR #25(실행 `40431626685`, 자동 머지), CODEOWNERS 쓰기(없을 때)와 건너뛰기(있을 때)의 결과가 저마다 있다. 통과
- 완료 조건 3: ADR 또는 명령
  - `grep -n "ADR-024" docs/ADR.md docs/ARCHITECTURE.md` → ADR 절과 명령 절의 참조가 있다. 도구를 더하지 않아 돌릴 명령은 없다. 통과
- 완료 조건 4: 장면 4 줄의 `#20`
  - `grep -n "장면 4" docs/TOOLS.md | grep -c "#20"` → `1`. 통과
- 완료 조건 5: scratchpad를 가리키지 않고 근거가 있다
  - `grep -n scratchpad docs/TOOLS.md` → 출력 없음(rc 1). 그 절에 PR #12~#17의 표와 422 오류 글 `Source only org-owned repos can have push rules`, `Invalid rule 'file_path_restriction': `가 있다. 통과
- 완료 조건 6
  - TOOLS.md의 ruleset 절을 읽었다 → 장면 1 PR #18·실행 `40352179658`·MERGED, 장면 2 PR #19·실행 `40352503804`·오류 글, 장면 3 PR #20·실행 `40352605265`·MERGED, 장면 4 PR #20·실행 `40352605265`·`GH013` 오류 글, 장면 5 PR #19·`gh pr merge 19 … --admin`·MERGED, ruleset JSON 있음. 통과
  - `python3 -m unittest discover -s tests` → `Ran 104 tests in 17.435s`, 마지막 줄 `OK`. 통과
  - `tests/test_verdict.py:123,129,134` → 워크플로 경로면 request, close·request 그대로, 목록 없음은 그대로의 세 시험. 통과
  - `tests/test_edit_guard.py:246-253, 279-287` → 처음 쓰기 통과, 이미 있으면 막음. 통과
  - setup SKILL.md의 2번 표(login 보이기, CODEOWNERS 알림), 3번(없을 때만 쓰기), 4번(쓰지 못하면 넣을 줄, ruleset 거는 법과 한계), 양식(verdict 단계가 `--changed-files`로 목록을 넘김)을 읽었다 → 네 곳이 모두 적는다. 통과
  - SKILL.md 보고의 JSON과 TOOLS.md의 시험한 JSON을 python으로 견줬다 → `target`, `conditions`, `rules`, `bypass_actors`, `enforcement` 모두 `True`(`name`만 다름). 통과
  - `grep -h '"version"' …/.claude-plugin/plugin.json …/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "0.14.0",`. 통과
  - `claude plugin validate .` → `✔ Validation passed`. 통과
  - `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `README.md`를 따로 읽고 `grep -nF "pr diff"`를 돌렸다 → 옛 `gh pr diff` 글은 남지 않았고 CODEOWNERS·ruleset·워크플로 검사·편집 훅 예외와 어긋나는 줄을 찾지 못했다. 통과

## 계획과 달라진 점
- TODO 1의 파일은 `plugins/plate/skills/setup/SKILL.md`뿐이었지만, `docs/ARCHITECTURE.md`와 `README.md`가 `gh pr diff --name-only`를 적고 있어 완료 조건 6의 마지막 확인(문서가 바뀐 동작과 어긋나지 않음)을 위해 같은 글로 고쳤다
- TODO 2의 "워크플로를 바꾸지 않은 PR"은 처음 README만 바꾼 PR #23으로 돌렸으나 바뀐 코드 파일이 없어 등급이 `unjudged`(머지 요청)라 목록 검사를 보이지 못해, 코드 PR #25를 더 열었다. 고친 양식을 시험 저장소에 넣으려고 PR #22를 머지했다

## 남은 것
- 파일 목록 API는 PR 하나에 파일 3000개까지만 낸다(GitHub 문서). 그보다 큰 PR은 잘린 목록을 받고, 잘린 뒤쪽에만 워크플로 경로가 있으면 검사가 놓친다. diff가 너무 큰 PR과 3000개를 넘는 PR은 시험하지 않았다
- setup의 CODEOWNERS는 Claude가 setup 스킬을 부른 것이 아니라 셸 스크립트로 단계를 따라 한 것이다. login을 얻지 못하는 경우는 돌리지 않았다
- 시험 저장소의 main이 `b416470`으로 바뀌었다(PR #22, #25 머지)

## 하네스에서 걸린 것
- 시작할 때 `docs/tasks/RUNLOG.md`에 커밋되지 않은 변경이 있어 커밋에 넣지 않았다
- 완료 조건 3은 도구를 더할지 ADR로 둘지 고르게 해, 수행 쪽이 ADR(두지 않음)을 골랐다. 사용자가 말한 이유가 없어 ADR-024의 이유에 그렇다고 적었다

## 확인 1

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 완료 조건 1: `sed -n 415,440p plugins/plate/skills/setup/SKILL.md`와 `grep -nF "pr diff"` → verdict 단계(426~428줄)가 `gh api --paginate "repos/$GH_REPO/pulls/$PR/files" --jq '.[].filename'`로 목록을 받고, 실패하면 `echo '.github/workflows/' > changed-files.txt`로 워크플로 경로를 적어 `--changed-files`로 넘긴다. `gh pr diff`는 330줄의 설명 글에만 있다. 통과
  - 완료 조건 2: `docs/TOOLS.md`의 "verdict 단계의 바뀐 파일 목록과 setup의 CODEOWNERS를 돌려 본 것" 절을 읽었다 → 워크플로를 바꾼 PR #24(실행 `40431431712`, 머지 요청), 바꾸지 않은 PR #25(실행 `40431626685`, 자동 머지), `mktemp -d` 임시 git 저장소에서 CODEOWNERS 없을 때 쓰기와 있을 때 건너뛰기의 결과가 저마다 있다. `gh pr view`로 시험 저장소를 봤다 → #24 `CLOSED`(파일 `.github/workflows/merge-probe.yml`, 댓글 `판정: 머지 요청`), #25 `MERGED` by `app/github-actions`(댓글 `판정: 자동 머지`), 두 실행 모두 `success`. 통과
  - 완료 조건 3: `grep -n "ADR-024" docs/ADR.md docs/ARCHITECTURE.md` → ADR.md 48줄에 두지 않는다는 ADR-024(결정·이유·트레이드오프), ARCHITECTURE.md 90줄 명령 절에 참조. 도구를 더하지 않아 돌릴 명령은 없다. 통과
  - 완료 조건 4: `grep -n "장면 4" docs/TOOLS.md` → 156줄 "PR #20의 같은 실행 `40352605265`". 통과
  - 완료 조건 5: `grep -n scratchpad docs/TOOLS.md` → 출력 없음(rc 1). 그 절 166~179줄에 PR #11~#17의 표, 163·164·189·200줄에 422 오류 글 `Source only org-owned repos can have push rules`와 `Invalid rule 'file_path_restriction': `, 그 두 ruleset JSON이 있다. 통과
  - 완료 조건 6, 다섯 장면: `docs/TOOLS.md` 152~157줄을 읽었다 → 장면 1~5가 저마다 PR 번호(#18, #19, #20, #20, #19), 명령이나 실행 id, 결과, 막힌 장면의 오류 글을 적었고 시험한 ruleset JSON이 있다. 통과
  - 완료 조건 6, 테스트: `python3 -m unittest discover -s tests` → `Ran 104 tests in 17.394s`, 마지막 줄 `OK`. 통과
  - 완료 조건 6, `tests/test_verdict.py` 124~142줄 → 워크플로 경로면 request, close·request 그대로, 목록 없음·워크플로 경로 없음은 그대로의 세 시험이 있다. 통과
  - 완료 조건 6, `tests/test_edit_guard.py` 246~253, 279~287줄 → 없는 CODEOWNERS 쓰기 통과, 이미 있으면 막음이 두 경우 모두 있다. 통과
  - 완료 조건 6, setup SKILL.md: 52줄(login 읽기), 65줄 2번 표(login 보이기, CODEOWNERS 알림), 87~92줄 3번(없을 때만 쓰기), 118~143줄 4번(쓰지 못하면 넣을 줄, ruleset 거는 법과 한계), 426~429줄 양식(목록을 `--changed-files`로 넘김) → 네 곳이 모두 적는다. 통과
  - 완료 조건 6, ruleset JSON: python으로 SKILL.md 보고의 JSON과 TOOLS.md의 시험한 JSON을 견줬다 → `target`, `conditions`, `rules`, `bypass_actors`, `enforcement`가 같고 `name`만 다르다. 통과
  - 완료 조건 6, 버전: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "0.14.0",`. 통과
  - 완료 조건 6, `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
  - 완료 조건 6, 문서: `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `README.md`에서 `pr diff|CODEOWNERS|ruleset|changed-files|워크플로 경로|자동 머지`를 찾아 문서마다 읽었다 → CODEOWNERS·ruleset(ADR-023, ARCHITECTURE 51줄, README 37~84줄), 판정의 워크플로 검사(ARCHITECTURE 17·74줄, README 29·33줄), 편집 훅의 CODEOWNERS 예외(README 90줄, ARCHITECTURE 49줄)가 바뀐 동작과 맞고, 옛 `gh pr diff --name-only` 글은 남지 않았다. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 104 tests`, `OK`. 통과

**실패**
- 없음

**하네스에서 걸린 것**
- 없음

**판정**: 통과
