# FRICTION

- `001-ruleset-probe` 문제: task 머리의 결정 "장면의 결과가 기대와 다르면 계획이 틀린 것으로 보고 멈춘다"에 따라 phase 2의 첫 시도가 장면 2(werwer748이 연 워크플로 PR #11이 토큰으로 머지됨) 뒤에서 멈췄다. 계획이 "PR을 연 계정이 유일한 코드 소유자면 코드 소유자 리뷰 필수가 통과로 매겨진다"는 GitHub 동작을 모른 채 장면 2의 기대를 세웠다(`bb1c0c6`에서 tasks 머리 목표·결정, 001 머리, 001 phase-2, 002 phase-3, 003 phase-1을 고침)
- `001-ruleset-probe` 문제: 계획이 고쳐진 뒤 phase 2를 다시 수행할 때 `phase-2.md`의 TODO 체크박스는 비어 있고 첫 시도의 기록 다섯 절은 남아 있어, 수행 쪽이 다섯 절을 고쳐 쓰고 첫 시도를 "한 일" 첫 줄로 줄였다. 계획 수정(plan 스킬)이나 다시 수행(phase 스킬)에 이전 기록을 어떻게 다룰지 정한 규칙이 없다(`docs/tasks/001-ruleset-probe/done-phase-2.md`의 "하네스에서 걸린 것")
- `001-ruleset-probe` 문제: phase 2 계획의 "읽을 것"과 `docs/TOOLS.md`의 "막지 못한 다른 설정"(PR #12~#17, 422 응답)의 근거가 저장소 밖 세션 scratchpad의 `log/investigation.md`와 JSON·`.out` 파일에만 있다. 세션이 끝나면 사라지는 경로라 그 근거를 다시 볼 수 없다(`docs/tasks/001-ruleset-probe/done-phase-2.md`의 "읽을 것")
- `001-ruleset-probe` 멈춤: 계획(task 머리 결정 "사용자의 단계")이 phase 1 뒤 사용자가 시험 저장소 main을 올리고 ruleset을 걸게 했는데, 실행 중 누가 할지 물었고 에이전트가 `gh api`로 대행했다(RUNLOG "계획의 사용자 단계 … 누가 하나")
- `001-ruleset-probe` 멈춤: phase 2 계획이 틀림(작성자가 유일한 코드 소유자면 워크플로 PR이 토큰으로 머지됨). 사용자 사전 지시로 묻지 않고 해결 에이전트의 추천안(판정 검사를 주 장치로, 장면 2·3 기대 변경)을 채택했다(RUNLOG)
- `001-ruleset-probe` 스킬 후보: 장면마다와 확인마다 같은 묶음(`gh workflow run` → 실행 결론 → `gh pr view --json state,author,mergedBy` → rule suite 조회)을 손으로 되풀이했다(`done-phase-2.md`의 "한 일"과 확인 1). 시험 저장소에서 PR 하나의 머지 결과와 rule suite를 모아 내는 스킬이 있으면 장면 기록과 확인의 손일이 준다
- `002-guard-setup` 문제: task 머리 완료 조건 4와 phase 3 통과 조건의 확인이 `docs/ARCHITECTURE.md`를 "17·20·23줄, 49줄, 51줄(계획 커밋 시점 기준)"처럼 줄 번호로 가리켜, 같은 task가 그 문서를 고치는 동안 확인 쪽과 회고가 계획 커밋 `807bfc6`의 파일과 견줘 줄이 같은 항목인지부터 봐야 했다. 계획 스킬(`plate:plan`)의 확인 글이 고쳐질 문서를 줄 번호 대신 항목 이름으로 가리키면 이 손일이 준다(`docs/tasks/002-guard-setup/done-phase-3.md`의 확인 1)
