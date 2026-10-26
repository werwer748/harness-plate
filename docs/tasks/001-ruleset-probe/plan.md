# 시험 저장소에서 ruleset이 워크플로 PR의 자동 머지를 막는지 확인한다

## 목표
시험 저장소 `werwer748/plate-ci-test`에 CODEOWNERS, 머지 시험 워크플로, ruleset을 건 상태에서 다섯 장면을 돌린다. 결과, 오류 글, 쓴 ruleset JSON을 `docs/TOOLS.md`에 남긴다.

## 범위 밖
- plate의 스킬, 훅, 판정 스크립트를 고치는 것
- 시험 저장소의 `plate-review.yml`이 낸 평가와 판정을 장면의 결과로 보는 것. PR마다 돌아도 기록만 한다
- 시험이 끝난 뒤 시험 저장소의 ruleset과 파일을 걷는 것

## 완료 조건
1. 시험 저장소의 main에 `.github/CODEOWNERS`와 `.github/workflows/merge-probe.yml`이 있고, 활성 ruleset이 하나 있다.
   - 확인: `gh api 'repos/werwer748/plate-ci-test/contents/.github/CODEOWNERS?ref=main' --jq .path`와 `gh api 'repos/werwer748/plate-ci-test/contents/.github/workflows/merge-probe.yml?ref=main' --jq .path`가 저마다 그 경로를 낸다
   - 확인: `gh api repos/werwer748/plate-ci-test/rulesets --jq '.[].name'`이 이름 하나를 내고, `gh api repos/werwer748/plate-ci-test/rulesets/<그 id> --jq .enforcement`가 `active`
2. (tasks 완료 조건 1) 다섯 장면의 결과와 오류 글, ruleset JSON이 `docs/TOOLS.md`에 있다.
   - 확인: `docs/TOOLS.md`의 새 절을 읽어 다섯 장면이 저마다 PR 번호, 돌린 명령이나 실행 id, 결과, 막혔으면 오류 글을 적었고, ruleset JSON이 있다. 하나라도 없으면 실패

## 결정
- 시험 작업은 phase마다 `mktemp -d`로 만든 임시 복제본에서 하고, 끝나면 지운다. 이유: 저장소 밖의 고정 경로에 기대지 않는다 (추천안으로 정함)
- CODEOWNERS는 두 줄이다: `/.github/workflows/ @werwer748`, `/.github/CODEOWNERS @werwer748`. 이유: tasks 머리의 결정과 같다
- `merge-probe.yml`은 `workflow_dispatch`로 PR 번호를 받아 `GITHUB_TOKEN`(contents·pull-requests 쓰기)으로 그 PR을 merge commit으로 머지한다. 이유: main에 있는 믿을 수 있는 워크플로로 토큰의 머지만 따로 본다 (추천안으로 정함)
- ruleset은 대상이 기본 브랜치, PR 필수, 승인 수 0, 코드 소유자 리뷰 필수, 우회 목록에 저장소 관리자(PR로만)다. 이유: tasks 머리의 결정과 같다
- 사용자의 단계: phase 1이 통과한 뒤 사용자가 `probe-setup`을 main에 올리고 ruleset을 건다. 명령은 phase 1의 기록에 있다. 이유: 에이전트의 main 푸시는 푸시 훅이 막고, 저장소 설정은 사람이 한다
- 장면의 결과가 기대와 다르면 계획이 틀린 것으로 보고 멈춘다. 기대와 다른 경우는 장면 1·3이 막히는 것, 장면 2·4가 막히지 않는 것, 장면 5가 막히는 것, ruleset을 걸 수 없는 것이다. 이유: tasks 머리의 결정과 같다
- 장면 2는 github-actions가 연 PR로, 장면 3은 werwer748이 연 PR로 본다(장면 3은 막히지 않는 한계를 적는 장면). 이유: phase 2의 PR #11이 막히지 않은 까닭이 작성자가 유일한 코드 소유자라서였다(조사의 #14, rule suite 4728318110 "Waiting on code owner review from werwer748.") (사용자가 미리 정한 대로 해결 에이전트의 추천안으로 정함)
- 사용자의 단계는 이번 실행에서 사용자가 정한 대로 에이전트가 `gh api`로 했다(main `65e9547`, ruleset `25891047`). 이유: 사용자가 개입 없이 끝까지 돌리기로 했다
