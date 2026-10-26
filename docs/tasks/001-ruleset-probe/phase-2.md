# Phase 2: 다섯 장면을 돌리고 기록한다

**목표**: ruleset과 CODEOWNERS가 걸린 시험 저장소에서 다섯 장면의 결과와 오류 글, ruleset JSON이 `docs/TOOLS.md`에 남는다.

**테스트 먼저**: 아니오 — `docs/TOOLS.md`만 고친다

**읽을 것**
- `docs/TOOLS.md`의 "AGENTS.md 되돌림과 실패 까닭 단계에서 본 것" (시험을 적는 꼴: 버전, 날짜, PR 번호, 실행 id)
- `docs/tasks/001-ruleset-probe/done-phase-1.md` (ruleset JSON, 처음 main sha)
- 이 파일의 아래 기록(첫 시도의 PR #10·#11, rule suite)과 계획을 고칠 때의 조사 기록 `/private/tmp/claude-501/-Users-hugo-Desktop-harness-plate/02098b8e-c6ca-47f0-9084-5888a2489f05/scratchpad/log/investigation.md`(PR #12~#17, 오류 글. 같은 폴더의 JSON과 `.out` 파일이 ruleset JSON과 422 응답이다)

**TODO**
- [ ] 시작할 때 main에 `.github/CODEOWNERS`와 `.github/workflows/merge-probe.yml`이 있고 활성 ruleset이 하나(승인 수 0, 코드 소유자 리뷰 필수)인지 본다. 하나라도 없으면 막힘으로 멈춘다
- [ ] 장면 1: `mktemp -d` 복제본에서 새 브랜치에 README만 바꾼 PR을 열고, `gh workflow run merge-probe.yml -f pr=<번호>`의 결과가 기록에 더해진다(머지됐는지, 누가 머지했는지)
- [ ] 장면 2: 시험 저장소의 `actions/permissions/workflow`에서 `can_approve_pull_request_reviews`를 true로 켠다. 새 브랜치에 `merge-probe.yml` 주석 한 줄만 더해 푸시한다. 그 머리 브랜치로 `gh pr create`를 하도록 `merge-probe.yml`의 단계만 바꾼 도구 브랜치를 `gh workflow run merge-probe.yml --ref <도구 브랜치>`로 돌려, github-actions가 연 PR을 만든다. 곧바로 그 설정을 false로 되돌린다. main의 `merge-probe`를 그 번호로 돌린 결과, 오류 글, 관련 rule suite가 기록에 더해진다
- [ ] 장면 3·4: werwer748이 새 워크플로 `.github/workflows/self-merge.yml`을 더한 PR을 연다. 그 워크플로는 `pull_request`로 돌고, `if: github.head_ref == '<그 브랜치>'`로 자기 PR에서만 돈다. contents·pull-requests 쓰기 권한으로 두 단계를 차례로 한다(둘 다 `continue-on-error`). 장면 4는 README를 바꾼 커밋을 main에 직접 푸시하는 단계, 장면 3은 그 PR 자신을 머지하는 단계다. 단계마다의 결과, 오류 글, rule suite가 기록에 더해진다
- [ ] 장면 3의 PR이 머지됐으면, `self-merge.yml`을 지우는 PR을 열어 werwer748이 머지하고 그 결과를 적는다
- [ ] 장면 5: 장면 2의 PR을 `gh pr merge --merge --admin`으로 머지한 결과와, 그 머지의 rule suite(`bypass`와 details)가 기록에 더해진다
- [ ] PR마다 `plate-review`가 돌았으면 그 실행 id와 판정이 기록에 더해진다
- [ ] `docs/TOOLS.md`의 "AGENTS.md 되돌림과 실패 까닭 단계에서 본 것" 절 뒤, "원격 없는 합치기와 푸시 훅에서 본 것" 앞에 새 굵은 제목 절이 더해진다. 내용은 다음과 같다
  - gh 버전, 날짜, 장면마다의 PR 번호·명령이나 실행 id·결과·오류 글, ruleset JSON, 무엇이 막았는지
  - PR을 연 계정이 유일한 코드 소유자면 코드 소유자 리뷰 필수가 통과로 매겨진다는 것(첫 시도의 #11과 rule suite 4728049352)
  - 막지 못한 다른 설정: 승인 수 1과 Actions 승인(#12, #13), push ruleset과 `file_path_restriction`의 422 오류 글, 쓰기 권한 없는 소유자가 무시된 것(#15)
- [ ] 장면의 결과가 task 머리의 기대와 다르면 거기서 멈추고 무엇이 달랐는지 기록에 적는다
- [ ] 끝나면 장면에 쓴 브랜치를 지우고, 임시 복제본을 지우고, `can_approve_pull_request_reviews`가 false인지 본다

**통과 조건**
- (완료 조건 1) main에 두 파일이 있고 활성 ruleset이 하나 있다
  - 확인: `gh api 'repos/werwer748/plate-ci-test/contents/.github/CODEOWNERS?ref=main' --jq .path`와 `gh api 'repos/werwer748/plate-ci-test/contents/.github/workflows/merge-probe.yml?ref=main' --jq .path`가 저마다 그 경로를 낸다
  - 확인: `gh api repos/werwer748/plate-ci-test/rulesets --jq '.[].name'`이 이름 하나를 내고, `gh api repos/werwer748/plate-ci-test/rulesets/<그 id> --jq .enforcement`가 `active`
- (완료 조건 2) 다섯 장면의 기록이 `docs/TOOLS.md`에 있다
  - 확인: `docs/TOOLS.md`의 새 절을 읽어 다섯 장면이 저마다 PR 번호, 돌린 명령이나 실행 id, 결과, 막혔으면 오류 글을 적었고, ruleset JSON이 있다. 하나라도 없으면 실패
- 장면의 PR 상태가 기록과 맞다
  - 확인: 기록의 PR 번호마다 `gh pr view <번호> --repo werwer748/plate-ci-test --json state,author,mergedBy -q '.state+" "+.author.login+" "+(.mergedBy.login // "")'`를 돌린다. 장면 1은 `MERGED`, 머지한 계정이 github-actions다. 장면 2(=장면 5)의 PR은 작성자가 github-actions이고 `MERGED`, 머지한 계정이 `werwer748`이다. 장면 3의 PR은 작성자가 `werwer748`이고 `MERGED`, 머지한 계정이 github-actions다
  - 확인: `gh api repos/werwer748/plate-ci-test/actions/permissions/workflow --jq .can_approve_pull_request_reviews`가 `false`
- 테스트가 그대로 통과한다
  - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`

## 한 일
- 시작할 때 main에 두 파일과 활성 ruleset이 있는지 본다: `gh api 'repos/werwer748/plate-ci-test/contents/.github/CODEOWNERS?ref=main' --jq .path` → `.github/CODEOWNERS`, `…/merge-probe.yml?ref=main` → `.github/workflows/merge-probe.yml`, `gh api repos/werwer748/plate-ci-test/rulesets` → `25891047 workflow-guard-probe active`. 그때 main sha는 `65e95474527b7e9e9e7880ee8f8c90d2100a914a`(phase 1의 `probe-setup` 커밋)였다. gh 2.103.0, 2026-10-27(KST). 걸린 ruleset의 `gh api repos/werwer748/plate-ci-test/rulesets/25891047`에서 phase 1의 JSON에 없던 기본값 `required_reviewers: []`, `require_extra_approval_for_unattributed_changes: true`, `allowed_merge_methods: ["merge","squash","rebase"]`가 붙어 있었고 `current_user_can_bypass`는 `pull_requests_only`였다. 저장소의 `actions/permissions/workflow`는 `default_workflow_permissions: read`, `can_approve_pull_request_reviews: false`, 협력자는 `werwer748 admin` 하나다 (시험 저장소만 봄)
- 장면 1: `mktemp -d` 복제본에서 `probe-s1` 브랜치에 README 끝에 한 줄을 더해 푸시하고 PR #10을 열었다. `gh workflow run merge-probe.yml --repo werwer748/plate-ci-test -f pr=10` → 실행 `40349220427`, `success`. PR #10은 `MERGED`, 머지한 계정은 `app/github-actions`, 머지 커밋 `a308eb2ba5f606c265d2ea886f4186fa32d0f6b9`. 기대(막히지 않음)와 같다 (시험 저장소의 `README.md`)
- 장면 2: 같은 복제본에서 origin/main(`a308eb2`)을 바탕으로 한 `probe-s2` 브랜치에 `.github/workflows/merge-probe.yml` 끝에 `# probe scene 2: 주석 한 줄`을 더해 푸시하고 PR #11을 열었다(바뀐 파일은 그 하나). `gh workflow run merge-probe.yml --repo werwer748/plate-ci-test -f pr=11` → 실행 `40349319119`, `success`. 로그에 오류 글은 없다. PR #11은 `MERGED`, 머지한 계정은 `app/github-actions`, `reviewDecision`은 빈 값, 머지 커밋 `2c7ea6c2e61152d4bc40f297bcf0da9f39115814`(지금 main). **기대(막힘)와 다르다.** 오류 글은 없다
  - 그 머지의 rule suite: `gh api 'repos/werwer748/plate-ci-test/rulesets/rule-suites?ref=main&time_period=day'` → `4728049352 github-actions[bot] a308eb2->2c7ea6c pass`(장면 1의 머지는 `4728035290 … 65e9547->a308eb2 pass`). `gh api repos/werwer748/plate-ci-test/rulesets/rule-suites/4728049352` → `rule_evaluations`에 ruleset `25891047`의 `pull_request` 규칙이 `enforcement: active`, `result: pass`. 곧 ruleset은 평가됐고 코드 소유자 리뷰 필수 규칙이 승인 없이 통과로 매겨졌다
  - `gh api repos/werwer748/plate-ci-test/codeowners/errors` → `{"errors":[]}`(CODEOWNERS 문법 오류 없음)
- 장면의 결과가 task 머리의 기대와 다르면 거기서 멈춘다: task 머리 결정("장면 2~4 가운데 막히지 않는 것이 있는 것")에 걸려 장면 2 뒤에서 멈췄다. 장면 3·4, 장면 5, `docs/TOOLS.md`의 새 절은 하지 않았다. 임시 복제본은 지웠다
- PR마다 `plate-review`가 돌았으면 그 실행 id와 판정: PR #10은 실행 `40349218043`(review·verdict 잡 `success`), PR 댓글 `판정: 머지 요청`(바뀐 코드 파일 0개). PR #11은 실행 `40349311286`(review·verdict 잡 `success`, PR이 이미 머지된 뒤 끝남), PR 댓글 `판정: 머지 요청`(바뀐 코드 파일 0개). 범위 밖대로 장면의 결과로 보지 않는다

## 확인 결과
- (완료 조건 1) main에 두 파일이 있고 활성 ruleset이 하나 있다
  - `gh api 'repos/werwer748/plate-ci-test/contents/.github/CODEOWNERS?ref=main' --jq .path` → `.github/CODEOWNERS`, `gh api 'repos/werwer748/plate-ci-test/contents/.github/workflows/merge-probe.yml?ref=main' --jq .path` → `.github/workflows/merge-probe.yml`. 통과
  - `gh api repos/werwer748/plate-ci-test/rulesets --jq '.[].name'` → `workflow-guard-probe` 하나, `gh api repos/werwer748/plate-ci-test/rulesets/25891047 --jq .enforcement` → `active`. 통과
- (완료 조건 2) 다섯 장면의 기록이 `docs/TOOLS.md`에 있다
  - 새 절을 쓰지 않았다(장면 2에서 멈춤). 실패
- 장면의 PR 상태가 기록과 맞다
  - `gh pr view 10 --repo werwer748/plate-ci-test --json state,mergedBy -q '.state+" "+(.mergedBy.login // "")'` → `MERGED app/github-actions`. 장면 1은 맞다
  - `gh pr view 11 …` → `MERGED app/github-actions`. 장면 5가 기대한 `MERGED werwer748`이 아니다(장면 2에서 토큰이 이미 머지). 장면 3·4의 PR은 없다. 실패
- 테스트가 그대로 통과한다
  - `python3 -m unittest discover -s tests` → `Ran 99 tests`, `OK`. 통과

## 계획과 달라진 점
- 계획은 장면 2가 막히고 그 PR을 장면 5에서 관리자 우회로 머지하는 것이었다. 실제로는 장면 2의 PR #11이 `GITHUB_TOKEN`으로 머지됐다. task 머리의 결정대로 계획이 틀린 것으로 보고 멈췄다

## 남은 것
- 장면 3·4(`self-merge.yml` PR), 장면 5, `docs/TOOLS.md`의 새 절을 하지 않았다. 장면 2의 결과가 기대와 달라 task 머리의 결정대로 멈췄다
- 장면 5는 그대로는 할 수 없다. 장면 2의 PR #11이 이미 머지됐으니 다시 하려면 새 PR이 필요하다
- 시험 저장소의 main이 바뀌었다: `65e9547` → `a308eb2`(PR #10, README 한 줄) → `2c7ea6c`(PR #11, `merge-probe.yml` 끝에 주석 한 줄). origin의 `probe-s1`, `probe-s2` 브랜치는 남아 있다
- 막히지 않은 까닭은 확인하지 않았다. 생각할 수 있는 것(확인 안 함): PR 작성자 `werwer748`이 유일한 코드 소유자라 GitHub가 코드 소유자 리뷰를 채워진 것으로 본다. 또는 `required_approving_review_count: 0`일 때 코드 소유자 리뷰 필수가 승인 수를 끌어올리지 않는다. 어느 쪽이든 rule suite `4728049352`가 `pull_request` 규칙을 `pass`로 매겼으니 토큰 권한이 아니라 규칙 평가에서 통과했다. 고칠 길(예: 승인 수 1, 다른 계정이 연 PR로 다시 보기, ruleset에 `file_path_restriction`이나 다른 규칙 쓰기)은 계획을 다시 세울 때 정할 일이다
- 이 파일 말고 이 저장소에서 바꾼 것은 없다. 커밋하지 않았다

## 하네스에서 걸린 것
- task 머리의 결정 "장면의 결과가 기대와 다르면 계획이 틀린 것으로 보고 멈춘다"에 따라 장면 2 뒤에서 멈췄다. 상태는 계획이 틀림
