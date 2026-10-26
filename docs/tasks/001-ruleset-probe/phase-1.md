# Phase 1: 시험 준비 브랜치와 ruleset JSON

**목표**: 시험 저장소의 브랜치 `probe-setup`에 두 시험 파일이 올라가고, 사용자가 돌릴 두 명령(main 올리기, ruleset 걸기)이 기록에 있다.

**테스트 먼저**: 아니오 — 이 저장소의 코드를 바꾸지 않고 시험 저장소의 브랜치만 만든다

**읽을 것**
- `gh issue view 18 --repo werwer748/harness-plate` (고칠 길)
- `docs/TOOLS.md`의 "CI의 세 판정과 CI 있는 PR에서 본 것"과 "AGENTS.md 되돌림과 실패 까닭 단계에서 본 것" (시험 저장소의 지금 상태, 푸시에 든 `workflow` 범위, 푸시 훅이 시험 저장소 main 푸시를 막은 것)

**TODO**
- [ ] 시험 저장소의 지금 main 커밋 sha가 기록에 적힌다
- [ ] 임시 복제본에서 main을 바탕으로 만든 브랜치 `probe-setup`에 `.github/CODEOWNERS`(task 머리의 두 줄)와 `.github/workflows/merge-probe.yml`(task 머리의 꼴)이 더해지고, 그 커밋이 origin의 `probe-setup`으로 푸시된다
- [ ] ruleset JSON(task 머리의 꼴)이 기록에 더해진다
- [ ] 사용자가 돌릴 두 명령이 기록에 더해진다: `probe-setup` 커밋으로 main을 앞당기는 명령, 그 JSON으로 ruleset을 만드는 `gh api` 명령

**통과 조건**
- 시험 저장소의 `probe-setup`에 두 파일이 있고, CODEOWNERS가 task 머리의 두 줄이다
  - 확인: `gh api 'repos/werwer748/plate-ci-test/contents/.github/CODEOWNERS?ref=probe-setup' --jq .content | base64 -d`가 `/.github/workflows/ @werwer748`와 `/.github/CODEOWNERS @werwer748` 두 줄을 낸다
  - 확인: `gh api 'repos/werwer748/plate-ci-test/contents/.github/workflows/merge-probe.yml?ref=probe-setup' --jq .content | base64 -d`를 읽어 `workflow_dispatch`의 PR 번호 입력, contents·pull-requests 쓰기 권한, 그 PR을 merge commit으로 머지하는 단계가 저마다 있다
- 에이전트가 main을 바꾸지 않았다
  - 확인: `gh api repos/werwer748/plate-ci-test/commits/main --jq .sha`가 기록에 적힌 처음 main sha와 같다
- 기록에 ruleset JSON과 사용자의 두 명령이 있다
  - 확인: 이 파일의 기록을 읽어 JSON에 기본 브랜치 대상, PR 규칙(승인 수 0, 코드 소유자 리뷰 필수), 우회 목록(저장소 관리자, PR로만)이 저마다 있고, 두 명령이 있다
