# Phase 2: 다섯 장면을 돌리고 기록한다

**목표**: ruleset과 CODEOWNERS가 걸린 시험 저장소에서 다섯 장면의 결과와 오류 글, ruleset JSON이 `docs/TOOLS.md`에 남는다.

**테스트 먼저**: 아니오 — `docs/TOOLS.md`만 고친다

**읽을 것**
- `docs/TOOLS.md`의 "AGENTS.md 되돌림과 실패 까닭 단계에서 본 것" (시험을 적는 꼴: 버전, 날짜, PR 번호, 실행 id)
- `docs/tasks/001-ruleset-probe/done-phase-1.md` (ruleset JSON, 처음 main sha)

**TODO**
- [ ] 시작할 때 main에 `.github/CODEOWNERS`와 `.github/workflows/merge-probe.yml`이 있고 활성 ruleset이 있는지 본다. 하나라도 없으면 막힘으로 멈추고, 사용자가 phase 1 기록의 두 명령을 돌려야 한다고 적는다
- [ ] 장면 1: README만 바꾼 PR을 열고 `merge-probe`를 그 번호로 돌린 결과가 기록에 더해진다(머지됐는지, 누가 머지했는지)
- [ ] 장면 2: `merge-probe.yml`에 주석 한 줄만 더한 PR을 열고 `merge-probe`를 그 번호로 돌린 결과와 오류 글이 기록에 더해진다
- [ ] 장면 3·4: 새 워크플로 `.github/workflows/self-merge.yml`을 더한 PR의 결과와 오류 글이 단계마다 기록에 더해진다. 그 워크플로는 `pull_request`로 돌며 contents·pull-requests 쓰기 권한으로 두 단계를 한다. 장면 3은 그 PR 자신을 머지하는 단계이고, 장면 4는 워크플로 파일이 아닌 파일 하나를 바꾼 커밋을 main에 직접 푸시하는 단계다. 끝나면 PR을 닫고 브랜치를 지운다
- [ ] 장면 5: 장면 2의 PR을 `gh pr merge --merge --admin`으로 머지한 결과가 기록에 더해진다
- [ ] PR마다 `plate-review`가 돌았으면 그 실행 id와 판정이 기록에 더해진다
- [ ] `docs/TOOLS.md`의 "AGENTS.md 되돌림과 실패 까닭 단계에서 본 것" 절 뒤, "원격 없는 합치기와 푸시 훅에서 본 것" 앞에 새 굵은 제목 절이 더해진다. 내용은 gh 버전, 날짜, 다섯 장면마다의 PR 번호·명령이나 실행 id·결과·오류 글, ruleset JSON, 무엇이 막았는지(ruleset인지, 토큰의 workflows 권한인지)다
- [ ] 장면의 결과가 task 머리의 기대와 다르면 거기서 멈추고 무엇이 달랐는지 기록에 적는다

**통과 조건**
- (완료 조건 1) main에 두 파일이 있고 활성 ruleset이 하나 있다
  - 확인: `gh api 'repos/werwer748/plate-ci-test/contents/.github/CODEOWNERS?ref=main' --jq .path`와 `gh api 'repos/werwer748/plate-ci-test/contents/.github/workflows/merge-probe.yml?ref=main' --jq .path`가 저마다 그 경로를 낸다
  - 확인: `gh api repos/werwer748/plate-ci-test/rulesets --jq '.[].name'`이 이름 하나를 내고, `gh api repos/werwer748/plate-ci-test/rulesets/<그 id> --jq .enforcement`가 `active`
- (완료 조건 2) 다섯 장면의 기록이 `docs/TOOLS.md`에 있다
  - 확인: `docs/TOOLS.md`의 새 절을 읽어 다섯 장면이 저마다 PR 번호, 돌린 명령이나 실행 id, 결과, 막혔으면 오류 글을 적었고, ruleset JSON이 있다. 하나라도 없으면 실패
- 장면의 PR 상태가 기록과 맞다
  - 확인: 기록의 PR 번호마다 `gh pr view <번호> --repo werwer748/plate-ci-test --json state,mergedBy -q '.state+" "+(.mergedBy.login // "")'`를 돌린다. 장면 1은 `MERGED`이고 머지한 계정이 github-actions다. 장면 5(장면 2의 PR)는 `MERGED`이고 머지한 계정이 `werwer748`이다. 장면 3·4의 PR은 `CLOSED`다
- 테스트가 그대로 통과한다
  - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
