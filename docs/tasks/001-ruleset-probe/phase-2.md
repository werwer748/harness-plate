# Phase 2: 다섯 장면을 돌리고 기록한다

**목표**: ruleset과 CODEOWNERS가 걸린 시험 저장소에서 다섯 장면의 결과와 오류 글, ruleset JSON이 `docs/TOOLS.md`에 남는다.

**테스트 먼저**: 아니오 — `docs/TOOLS.md`만 고친다

**읽을 것**
- `docs/TOOLS.md`의 "AGENTS.md 되돌림과 실패 까닭 단계에서 본 것" (시험을 적는 꼴: 버전, 날짜, PR 번호, 실행 id)
- `docs/tasks/001-ruleset-probe/done-phase-1.md` (ruleset JSON, 처음 main sha)
- 이 파일의 아래 기록(첫 시도의 PR #10·#11, rule suite)과 계획을 고칠 때의 조사 기록 `/private/tmp/claude-501/-Users-hugo-Desktop-harness-plate/02098b8e-c6ca-47f0-9084-5888a2489f05/scratchpad/log/investigation.md`(PR #12~#17, 오류 글. 같은 폴더의 JSON과 `.out` 파일이 ruleset JSON과 422 응답이다)

**TODO**
- [x] 시작할 때 main에 `.github/CODEOWNERS`와 `.github/workflows/merge-probe.yml`이 있고 활성 ruleset이 하나(승인 수 0, 코드 소유자 리뷰 필수)인지 본다. 하나라도 없으면 막힘으로 멈춘다
- [x] 장면 1: `mktemp -d` 복제본에서 새 브랜치에 README만 바꾼 PR을 열고, `gh workflow run merge-probe.yml -f pr=<번호>`의 결과가 기록에 더해진다(머지됐는지, 누가 머지했는지)
- [x] 장면 2: 시험 저장소의 `actions/permissions/workflow`에서 `can_approve_pull_request_reviews`를 true로 켠다. 새 브랜치에 `merge-probe.yml` 주석 한 줄만 더해 푸시한다. 그 머리 브랜치로 `gh pr create`를 하도록 `merge-probe.yml`의 단계만 바꾼 도구 브랜치를 `gh workflow run merge-probe.yml --ref <도구 브랜치>`로 돌려, github-actions가 연 PR을 만든다. 곧바로 그 설정을 false로 되돌린다. main의 `merge-probe`를 그 번호로 돌린 결과, 오류 글, 관련 rule suite가 기록에 더해진다
- [x] 장면 3·4: werwer748이 새 워크플로 `.github/workflows/self-merge.yml`을 더한 PR을 연다. 그 워크플로는 `pull_request`로 돌고, `if: github.head_ref == '<그 브랜치>'`로 자기 PR에서만 돈다. contents·pull-requests 쓰기 권한으로 두 단계를 차례로 한다(둘 다 `continue-on-error`). 장면 4는 README를 바꾼 커밋을 main에 직접 푸시하는 단계, 장면 3은 그 PR 자신을 머지하는 단계다. 단계마다의 결과, 오류 글, rule suite가 기록에 더해진다
- [x] 장면 3의 PR이 머지됐으면, `self-merge.yml`을 지우는 PR을 열어 werwer748이 머지하고 그 결과를 적는다
- [x] 장면 5: 장면 2의 PR을 `gh pr merge --merge --admin`으로 머지한 결과와, 그 머지의 rule suite(`bypass`와 details)가 기록에 더해진다
- [x] PR마다 `plate-review`가 돌았으면 그 실행 id와 판정이 기록에 더해진다
- [x] `docs/TOOLS.md`의 "AGENTS.md 되돌림과 실패 까닭 단계에서 본 것" 절 뒤, "원격 없는 합치기와 푸시 훅에서 본 것" 앞에 새 굵은 제목 절이 더해진다. 내용은 다음과 같다
  - gh 버전, 날짜, 장면마다의 PR 번호·명령이나 실행 id·결과·오류 글, ruleset JSON, 무엇이 막았는지
  - PR을 연 계정이 유일한 코드 소유자면 코드 소유자 리뷰 필수가 통과로 매겨진다는 것(첫 시도의 #11과 rule suite 4728049352)
  - 막지 못한 다른 설정: 승인 수 1과 Actions 승인(#12, #13), push ruleset과 `file_path_restriction`의 422 오류 글, 쓰기 권한 없는 소유자가 무시된 것(#15)
- [x] 장면의 결과가 task 머리의 기대와 다르면 거기서 멈추고 무엇이 달랐는지 기록에 적는다
- [x] 끝나면 장면에 쓴 브랜치를 지우고, 임시 복제본을 지우고, `can_approve_pull_request_reviews`가 false인지 본다

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
- 첫 시도(계획을 고치기 전): 장면 1은 PR #10(실행 `40349220427`, github-actions가 머지, rule suite `4728035290 pass`), 장면 2는 `werwer748`이 연 워크플로 주석 PR #11(실행 `40349319119`, github-actions가 머지, rule suite `4728049352`의 `pull_request` 규칙 `pass`)이었다. 장면 2가 기대와 달라 멈췄고, 계획이 고쳐진 뒤(`bb1c0c6`) 아래를 새로 했다. PR #10의 `plate-review`는 실행 `40349218043`, PR #11은 `40349311286`, 둘 다 `판정: 머지 요청`
- 시작할 때 main에 두 파일과 활성 ruleset이 있는지 본다: `gh api '…/contents/.github/CODEOWNERS?ref=main' --jq .path` → `.github/CODEOWNERS`, `…/merge-probe.yml?ref=main` → `.github/workflows/merge-probe.yml`, `gh api repos/werwer748/plate-ci-test/rulesets` → `25891047 workflow-guard-probe active`, 규칙은 `pull_request` 하나(`required_approving_review_count: 0`, `require_code_owner_review: true`). main `82dd247`, `can_approve_pull_request_reviews: false`. gh 2.103.0, 2026-10-27 00:43 KST (시험 저장소만 봄)
- 장면 1: 복제본의 `probe-v1`에 README 한 줄을 더해 PR #18을 열고 `gh workflow run merge-probe.yml --repo werwer748/plate-ci-test -f pr=18` → 실행 `40352179658` `success`, PR #18 `MERGED`, 머지한 계정 `app/github-actions`, 머지 커밋 `6dabb2c`, rule suite `4728423096 pass`. 기대(막히지 않음)와 같다
- 장면 2: `can_approve_pull_request_reviews`를 true로 켜고, `merge-probe.yml` 끝에 주석 한 줄만 더한 `probe-v2`와 단계만 `gh pr create --head probe-v2`로 바꾼 `probe-v2-tool`을 푸시하고 `gh workflow run merge-probe.yml --ref probe-v2-tool -f pr=0`(실행 `40352422589` `success`)으로 github-actions가 연 PR #19를 만든 뒤 곧바로 false로 되돌렸다. `gh workflow run merge-probe.yml -f pr=19` → 실행 `40352503804` `failure`, `X Pull request werwer748/plate-ci-test#19 is not mergeable: the base branch policy prohibits the merge.`, PR은 `OPEN`·`BLOCKED`. push가 일어나지 않아 이 장면의 rule suite는 없다. 기대(막힘)와 같다
- 장면 3·4: `werwer748`이 `.github/workflows/self-merge.yml`(`pull_request`, `if: github.head_ref == 'probe-v3'`, contents·pull-requests 쓰기, 두 단계 `continue-on-error`)을 더한 PR #20을 열었다. 실행 `40352605265`: 장면 4의 main 직접 푸시는 `GH013 … Changes must be made through a pull request.`로 거절(rule suite `4728477612 fail`), 장면 3의 자기 머지는 됨(PR #20 `MERGED`, 머지한 계정 `app/github-actions`, 머지 커밋 `38df5d3`, rule suite `4728479977 pass`). 기대(장면 3 막히지 않음, 장면 4 막힘)와 같다
- 장면 3의 PR이 머지됐으면 `self-merge.yml`을 지우는 PR: PR #21을 `werwer748`이 `gh pr merge probe-v3-cleanup --merge`로 머지 → `MERGED`, 머지한 계정 `werwer748`, 머지 커밋 `41e5d26`, rule suite `4728493711 pass`
- 장면 5: `gh pr merge 19 --repo werwer748/plate-ci-test --merge --admin` → 오류 없음, PR #19 `MERGED`, 작성자 `app/github-actions`, 머지한 계정 `werwer748`, 머지 커밋 `326e30c`, rule suite `4728498479` `bypass`, `pull_request` 규칙 `fail` "Waiting on code owner review from werwer748." 기대(막히지 않음)와 같다
- PR마다 `plate-review`: #18 실행 `40352171181` `success` `판정: 머지 요청`, #19 실행 `40352450823` `failure`(잡 0개, "workflow file issue"), #20 실행 `40352605307` `success` `판정: 머지 요청`, #21 실행 `40352739286` `success` `판정: 머지 요청`
- `docs/TOOLS.md`에 새 절: "AGENTS.md 되돌림과 실패 까닭 단계에서 본 것" 뒤, "원격 없는 합치기와 푸시 훅에서 본 것" 앞에 "ruleset과 CODEOWNERS로 워크플로 PR의 자동 머지를 막는지 본 것"을 더했다. gh 버전·날짜, ruleset JSON, 장면 1~5와 뒷정리의 PR 번호·명령·실행 id·결과·오류 글·rule suite, 유일한 코드 소유자가 연 PR이 통과로 매겨지는 것(#11, `4728049352`), 막지 못한 다른 설정(#12·#13의 승인 수 1과 Actions 승인, push ruleset과 branch `file_path_restriction`의 422 오류 글, #15의 `Unknown owner`)을 적었다 (`docs/TOOLS.md`)
- 장면의 결과가 기대와 다르면 멈춘다: 다섯 장면 모두 task 머리의 기대와 같아 멈추지 않았다
- 뒷정리: 시험 저장소의 `probe-v1`, `probe-v2`, `probe-v2-tool`, `probe-v3`, `probe-v3-cleanup`과 첫 시도의 `probe-s1`, `probe-s2`를 `gh api -X DELETE …/git/refs/heads/<브랜치>`로 지웠고 임시 복제본을 지웠다. `can_approve_pull_request_reviews` → `false`

## 확인 결과
- (완료 조건 1) main에 두 파일이 있고 활성 ruleset이 하나 있다
  - `gh api 'repos/werwer748/plate-ci-test/contents/.github/CODEOWNERS?ref=main' --jq .path` → `.github/CODEOWNERS`, `gh api 'repos/werwer748/plate-ci-test/contents/.github/workflows/merge-probe.yml?ref=main' --jq .path` → `.github/workflows/merge-probe.yml`. 통과
  - `gh api repos/werwer748/plate-ci-test/rulesets --jq '.[].name'` → `workflow-guard-probe` 하나, `gh api repos/werwer748/plate-ci-test/rulesets/25891047 --jq .enforcement` → `active`. 통과
- (완료 조건 2) 다섯 장면의 기록이 `docs/TOOLS.md`에 있다
  - `docs/TOOLS.md`의 새 절을 읽음 → 장면 1(#18, 실행 `40352179658`, 머지됨), 장면 2(#19, 실행 `40352503804`, 막힘, 오류 글), 장면 3(#20, 실행 `40352605265`, 머지됨), 장면 4(#20의 같은 실행, 막힘, GH013 오류 글), 장면 5(#19, `gh pr merge 19 --merge --admin`, 머지됨, rule suite `4728498479`)가 저마다 있고 ruleset JSON이 있다. 통과
- 장면의 PR 상태가 기록과 맞다
  - `gh pr view <번호> --repo werwer748/plate-ci-test --json state,author,mergedBy -q '.state+" "+.author.login+" "+(.mergedBy.login // "")'` → 18 `MERGED werwer748 app/github-actions`(장면 1, github-actions가 머지), 19 `MERGED app/github-actions werwer748`(장면 2=5), 20 `MERGED werwer748 app/github-actions`(장면 3), 21 `MERGED werwer748 werwer748`. 통과
  - `gh api repos/werwer748/plate-ci-test/actions/permissions/workflow --jq .can_approve_pull_request_reviews` → `false`. 통과
- 테스트가 그대로 통과한다
  - `python3 -m unittest discover -s tests` → `Ran 99 tests in 16.100s`, `OK`. 통과

## 계획과 달라진 점
- 장면 2에서 `gh workflow run`에 PR 번호가 필요해 도구 브랜치는 `-f pr=0`으로 돌렸다(도구 브랜치의 워크플로는 입력을 쓰지 않는다)
- 장면 2의 rule suite: TODO는 "관련 rule suite"를 적으라 했지만 `gh pr merge`가 머지 전에 거절해 rule suite가 생기지 않았다. 그 사실을 적었다
- 뒷정리에서 첫 시도의 장면 브랜치 `probe-s1`, `probe-s2`도 지웠다. phase 1의 `probe-setup`은 장면 브랜치가 아니라 남겼다

## 남은 것
- 시험 저장소의 main이 `82dd247` → `6dabb2c`(#18, README) → `38df5d3`(#20, `self-merge.yml`) → `41e5d26`(#21, 지움) → `326e30c`(#19, `merge-probe.yml` 주석)로 바뀌었다. ruleset `25891047`과 시험 파일은 범위 밖대로 남겼다
- 도구 브랜치의 첫 푸시는 `run:` 줄의 `": "` 때문에 YAML이 깨져 push 실행 `40352280865`(`failure`)이 생겼고, 그 사이 `can_approve_pull_request_reviews`가 한 번 true로 켜졌다가(디스패치 422 `Workflow does not have 'workflow_dispatch' trigger`) false로 되돌려졌다. 고친 뒤 다시 켜고 돌렸다
- 장면 3·4의 두 단계는 `continue-on-error`라 잡의 단계 결과가 `success`로 남는다. 실패는 로그와 rule suite로만 보인다
- PR #19의 `plate-review`는 잡 없이 `failure`(workflow file issue)였다. 까닭은 보지 않았다(범위 밖)
- 장면 3의 한계(유일한 코드 소유자가 연 PR은 막지 못함)는 확인만 했고 고칠 길은 이 task 밖이다

## 하네스에서 걸린 것
- task 머리의 결정 "장면의 결과가 기대와 다르면 계획이 틀린 것으로 보고 멈춘다"에 따라 장면 2 뒤에서 멈췄다. 상태는 계획이 틀림
- 계획이 고쳐진 뒤 다시 수행할 때 TODO의 체크박스가 모두 비어 있고 첫 시도의 기록 다섯 절이 남아 있었다. 다섯 절을 지금 상태로 고쳐 쓰면서 첫 시도의 결과는 "한 일"의 첫 줄로 줄여 남겼다
