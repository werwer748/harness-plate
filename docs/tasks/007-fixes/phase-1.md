# Phase 1: tasks 끝의 문제를 고친다

**목표**: task 머리의 완료 조건에 적힌 것을 모두 고친다.

**테스트 먼저**: 아니오 — 시험 저장소의 장면과 `.md`만 고치고, 이 저장소의 코드 파일은 바꾸지 않는다

**읽을 것**
- `docs/tasks/review.md`의 `## 평가 1` 절
- `docs/tasks/eval.md`의 `## eval 1` 절
- `plugins/plate`
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/ADR.md`
- `docs/TOOLS.md`

**TODO**
- [ ] 시험 저장소 `main`의 `.plate`를 지금의 `plugins/plate`로 맞추는 커밋을 `~/plate-rail-test/ci-src`에 만들고, 사용자가 `main`에 푸시한 뒤 #11 장면 PR을 다시 열어 tasks 완료 조건 2의 세 확인을 이 phase의 기록에 PR 번호, 실행 id와 함께 적는다 (`werwer748/plate-ci-test`, `plugins/plate`)
- [ ] auto mode에서 스킬 본문 Edit가 분류기에 막힌 사실, 날짜, run 전 권한 모드의 안내를 Claude Code 절에 적는다 (`docs/TOOLS.md`)
- [ ] 명령 절에 커버리지·중복·보안 검사 도구를 두지 않는다는 줄을 더한다 (`docs/ARCHITECTURE.md`)

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다
