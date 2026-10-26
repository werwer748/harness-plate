# Phase 1: 시험 준비 브랜치와 ruleset JSON

**목표**: 시험 저장소의 브랜치 `probe-setup`에 두 시험 파일이 올라가고, 사용자가 돌릴 두 명령(main 올리기, ruleset 걸기)이 기록에 있다.

**테스트 먼저**: 아니오 — 이 저장소의 코드를 바꾸지 않고 시험 저장소의 브랜치만 만든다

**읽을 것**
- `gh issue view 18 --repo werwer748/harness-plate` (고칠 길)
- `docs/TOOLS.md`의 "CI의 세 판정과 CI 있는 PR에서 본 것"과 "AGENTS.md 되돌림과 실패 까닭 단계에서 본 것" (시험 저장소의 지금 상태, 푸시에 든 `workflow` 범위, 푸시 훅이 시험 저장소 main 푸시를 막은 것)

**TODO**
- [x] 시험 저장소의 지금 main 커밋 sha가 기록에 적힌다
- [x] 임시 복제본에서 main을 바탕으로 만든 브랜치 `probe-setup`에 `.github/CODEOWNERS`(task 머리의 두 줄)와 `.github/workflows/merge-probe.yml`(task 머리의 꼴)이 더해지고, 그 커밋이 origin의 `probe-setup`으로 푸시된다
- [x] ruleset JSON(task 머리의 꼴)이 기록에 더해진다
- [x] 사용자가 돌릴 두 명령이 기록에 더해진다: `probe-setup` 커밋으로 main을 앞당기는 명령, 그 JSON으로 ruleset을 만드는 `gh api` 명령

**통과 조건**
- 시험 저장소의 `probe-setup`에 두 파일이 있고, CODEOWNERS가 task 머리의 두 줄이다
  - 확인: `gh api 'repos/werwer748/plate-ci-test/contents/.github/CODEOWNERS?ref=probe-setup' --jq .content | base64 -d`가 `/.github/workflows/ @werwer748`와 `/.github/CODEOWNERS @werwer748` 두 줄을 낸다
  - 확인: `gh api 'repos/werwer748/plate-ci-test/contents/.github/workflows/merge-probe.yml?ref=probe-setup' --jq .content | base64 -d`를 읽어 `workflow_dispatch`의 PR 번호 입력, contents·pull-requests 쓰기 권한, 그 PR을 merge commit으로 머지하는 단계가 저마다 있다
- 에이전트가 main을 바꾸지 않았다
  - 확인: `gh api repos/werwer748/plate-ci-test/commits/main --jq .sha`가 기록에 적힌 처음 main sha와 같다
- 기록에 ruleset JSON과 사용자의 두 명령이 있다
  - 확인: 이 파일의 기록을 읽어 JSON에 기본 브랜치 대상, PR 규칙(승인 수 0, 코드 소유자 리뷰 필수), 우회 목록(저장소 관리자, PR로만)이 저마다 있고, 두 명령이 있다

## 한 일
- 시험 저장소의 지금 main 커밋 sha가 기록에 적힌다: `gh api repos/werwer748/plate-ci-test/commits/main --jq '.sha + " " + .commit.committer.date'` → `31a01435bf58220a0a28d52e2608a6df5f34d75a 2026-10-26T07:17:16Z`. 처음 main sha는 `31a01435bf58220a0a28d52e2608a6df5f34d75a`다. 그때 `gh api repos/werwer748/plate-ci-test/rulesets`는 `[]`였다 (시험 저장소, 이 저장소의 파일은 바꾸지 않음)
- 임시 복제본에서 `probe-setup`에 두 파일을 더하고 푸시한다: `mktemp -d`의 복제본(main `31a0143`)에서 `git switch -c probe-setup`, `.github/CODEOWNERS`(두 줄 `/.github/workflows/ @werwer748`, `/.github/CODEOWNERS @werwer748`)와 `.github/workflows/merge-probe.yml`(`workflow_dispatch` 입력 `pr`(number, 필수), `permissions: contents: write, pull-requests: write`, 단계 하나가 `GH_TOKEN: ${{ github.token }}`으로 `gh pr merge "$PR" --merge --repo "$GITHUB_REPOSITORY"`)을 커밋 `65e95474527b7e9e9e7880ee8f8c90d2100a914a`("merge-probe: CODEOWNERS와 머지 시험 워크플로")로 넣고 `git push origin probe-setup`. 푸시는 오류 없이 됐고 복제본은 지웠다. `probe-setup`은 main `31a0143`의 바로 위 커밋 하나라 main을 fast-forward로 앞당길 수 있다 (시험 저장소의 `.github/CODEOWNERS`, `.github/workflows/merge-probe.yml`)
- ruleset JSON이 기록에 더해진다: 아래 "사용자가 돌릴 명령" 2의 heredoc 안이 그 JSON이다. 대상은 `~DEFAULT_BRANCH`, 규칙은 `pull_request` 하나(`required_approving_review_count: 0`, `require_code_owner_review: true`), 우회 목록은 `RepositoryRole` `actor_id: 5`(저장소 관리자 역할), `bypass_mode: "pull_request"`(PR로만)다
- 사용자가 돌릴 두 명령이 기록에 더해진다: 아래와 같다

### 사용자가 돌릴 명령

1. main을 `probe-setup` 커밋으로 앞당긴다(fast-forward만, 강제 아님). 워크플로 파일이 든 커밋이라 `gh auth`의 토큰에 `workflow` 범위가 있어야 한다(지금 활성 토큰에 있다).

```sh
gh api -X PATCH repos/werwer748/plate-ci-test/git/refs/heads/main \
  -f sha=65e95474527b7e9e9e7880ee8f8c90d2100a914a -F force=false
```

2. ruleset을 만든다. 나온 `id`가 다음 phase의 확인에 쓰인다.

```sh
gh api -X POST repos/werwer748/plate-ci-test/rulesets --input - <<'EOF'
{
  "name": "workflow-guard-probe",
  "target": "branch",
  "enforcement": "active",
  "conditions": {
    "ref_name": {
      "include": ["~DEFAULT_BRANCH"],
      "exclude": []
    }
  },
  "rules": [
    {
      "type": "pull_request",
      "parameters": {
        "required_approving_review_count": 0,
        "require_code_owner_review": true,
        "dismiss_stale_reviews_on_push": false,
        "require_last_push_approval": false,
        "required_review_thread_resolution": false
      }
    }
  ],
  "bypass_actors": [
    {
      "actor_id": 5,
      "actor_type": "RepositoryRole",
      "bypass_mode": "pull_request"
    }
  ]
}
EOF
```

## 확인 결과
- 시험 저장소의 `probe-setup`에 두 파일이 있고, CODEOWNERS가 task 머리의 두 줄이다
  - `gh api 'repos/werwer748/plate-ci-test/contents/.github/CODEOWNERS?ref=probe-setup' --jq .content | base64 -d` → `/.github/workflows/ @werwer748`, `/.github/CODEOWNERS @werwer748` 두 줄. 통과
  - `gh api 'repos/werwer748/plate-ci-test/contents/.github/workflows/merge-probe.yml?ref=probe-setup' --jq .content | base64 -d` → `workflow_dispatch.inputs.pr`(number, required), `permissions`의 `contents: write`, `pull-requests: write`, 단계 `gh pr merge "$PR" --merge --repo "$GITHUB_REPOSITORY"`(`GH_TOKEN: ${{ github.token }}`)가 저마다 있다. 통과
- 에이전트가 main을 바꾸지 않았다
  - `gh api repos/werwer748/plate-ci-test/commits/main --jq .sha` → `31a01435bf58220a0a28d52e2608a6df5f34d75a`, 처음 sha와 같다. 통과
- 기록에 ruleset JSON과 사용자의 두 명령이 있다
  - 이 파일의 "사용자가 돌릴 명령"을 읽음 → JSON에 `conditions.ref_name.include: ["~DEFAULT_BRANCH"]`, `pull_request` 규칙의 `required_approving_review_count: 0`과 `require_code_owner_review: true`, `bypass_actors`의 `RepositoryRole` 5와 `bypass_mode: "pull_request"`가 있고, main을 앞당기는 `gh api -X PATCH …/git/refs/heads/main`과 ruleset을 만드는 `gh api -X POST …/rulesets` 두 명령이 있다. 통과

## 계획과 달라진 점
- 없음

## 남은 것
- 두 명령은 돌려 보지 않았다. ruleset JSON이 API에 받아들여지는지와 `actor_id: 5`가 이 저장소에서 관리자 역할로 풀리는지는 사용자가 명령 2를 돌릴 때 처음 드러난다(`RepositoryRole` 5가 admin이라는 것은 GitHub 문서의 관례로 적었고 이 저장소에서 확인하지 않았다)
- 시험 저장소의 main에 이미 있는 `plate-review.yml`은 그대로라 장면 PR마다 돈다(task 머리의 범위 밖대로 기록만 할 것)

## 하네스에서 걸린 것
- 없음

## 확인 1

**통과 조건**
- 시험 저장소의 `probe-setup`에 두 파일이 있고, CODEOWNERS가 task 머리의 두 줄이다
  - `gh api 'repos/werwer748/plate-ci-test/contents/.github/CODEOWNERS?ref=probe-setup' --jq .content | base64 -d` → `/.github/workflows/ @werwer748`, `/.github/CODEOWNERS @werwer748` 두 줄. 통과
  - `gh api 'repos/werwer748/plate-ci-test/contents/.github/workflows/merge-probe.yml?ref=probe-setup' --jq .content | base64 -d` → `workflow_dispatch.inputs.pr`(type number, required true), `permissions`의 `contents: write`와 `pull-requests: write`, 단계 `gh pr merge "$PR" --merge --repo "$GITHUB_REPOSITORY"`(`GH_TOKEN: ${{ github.token }}`)가 저마다 있다. 통과
- 에이전트가 main을 바꾸지 않았다
  - `gh api repos/werwer748/plate-ci-test/commits/main --jq .sha` → `31a01435bf58220a0a28d52e2608a6df5f34d75a`, 기록의 처음 main sha와 같다. 통과
- 기록에 ruleset JSON과 사용자의 두 명령이 있다
  - 이 파일의 "사용자가 돌릴 명령"을 읽음 → JSON에 `conditions.ref_name.include: ["~DEFAULT_BRANCH"]`, `pull_request` 규칙의 `required_approving_review_count: 0`과 `require_code_owner_review: true`, `bypass_actors`의 `RepositoryRole` `actor_id: 5`와 `bypass_mode: "pull_request"`가 있고, main을 앞당기는 `gh api -X PATCH …/git/refs/heads/main`과 ruleset을 만드는 `gh api -X POST …/rulesets` 두 명령이 있다. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 99 tests`, `OK`. 통과

**실패**
- 없음

**하네스에서 걸린 것**
- 없음

**판정**: 통과
