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
- [ ] CI 양식의 verdict 단계가 바뀐 파일 목록을 `gh pr diff` 대신 파일 목록 API로 받고, 받지 못하면 request로 내린다 (`plugins/plate/skills/setup/SKILL.md`)
- [ ] 고친 양식의 verdict 단계를 시험 저장소에서 워크플로를 바꾼 PR과 바꾸지 않은 PR로 돌리고, setup의 CODEOWNERS 쓰기·건너뛰기를 임시 git 저장소에서 따라 해, 결과를 `docs/TOOLS.md`의 새 절에 적는다 (`docs/TOOLS.md`)
- [ ] 커버리지·중복·정적 분석 도구를 명령 절에 더하거나, 두지 않는다는 결정을 ADR로 적는다 (`docs/ARCHITECTURE.md`, `docs/ADR.md`)
- [ ] 장면 4 줄에 PR #20을 적는다 (`docs/TOOLS.md`)
- [ ] scratchpad의 조사 근거(PR #12~#17, 422 응답, ruleset JSON)를 `docs/TOOLS.md`의 그 절로 옮긴다 (`docs/TOOLS.md`)

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다
