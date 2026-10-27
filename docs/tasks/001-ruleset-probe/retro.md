# 회고

## 회고 1

**확인**
- 1. 시험 저장소의 main에 `.github/CODEOWNERS`와 `.github/workflows/merge-probe.yml`이 있고, 활성 ruleset이 하나 있다.
  - `gh api 'repos/werwer748/plate-ci-test/contents/.github/CODEOWNERS?ref=main' --jq .path` → `.github/CODEOWNERS`. `gh api 'repos/werwer748/plate-ci-test/contents/.github/workflows/merge-probe.yml?ref=main' --jq .path` → `.github/workflows/merge-probe.yml`. 통과
  - `gh api repos/werwer748/plate-ci-test/rulesets --jq '.[].name'` → `workflow-guard-probe` 하나(id `25891047`). `gh api repos/werwer748/plate-ci-test/rulesets/25891047 --jq .enforcement` → `active`. 통과
- 2. (tasks 완료 조건 1) 다섯 장면의 결과와 오류 글, ruleset JSON이 `docs/TOOLS.md`에 있다.
  - `docs/TOOLS.md`의 "ruleset과 CODEOWNERS로 워크플로 PR의 자동 머지를 막는지 본 것" 절을 읽음 → ruleset JSON이 있다. 장면 1(PR #18, `gh workflow run merge-probe.yml … -f pr=18`, 실행 `40352179658`, 머지됨), 장면 2(PR #19, 실행 `40352503804`, 막힘, 오류 글 `…the base branch policy prohibits the merge.`), 장면 3(PR #20, 실행 `40352605265`, 머지됨), 장면 4(PR #20의 같은 실행, 막힘, `GH013 … Changes must be made through a pull request.`), 장면 5(PR #19, `gh pr merge 19 --merge --admin`, 머지됨, rule suite `4728498479` bypass)가 저마다 PR 번호, 명령이나 실행 id, 결과를 적었고 막힌 장면 2·4는 오류 글이 있다. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 99 tests in 15.605s`, `OK`. 통과

**문제**
- 없음

**판정**: 통과
