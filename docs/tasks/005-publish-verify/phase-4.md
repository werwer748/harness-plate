# Phase 4: 원격 없는 합치기와 푸시 훅

**목표**: GitHub 원격이 없는 시험 폴더에서 run이 tasks 끝에 합칠지 묻고 합치며, 셋업된 시험 폴더에서 에이전트가 기본 브랜치로 하는 푸시를 푸시 훅이 막는다.

**테스트 먼저**: 아니오 — 시험 폴더에서 스킬과 훅을 돌려 보고, 이 저장소에서는 `docs/TOOLS.md`만 고친다

**읽을 것**
- `docs/TOOLS.md`의 Claude Code 절 (헤드리스 실행과 세션 잇기, "훅"의 막힌 호출이 기록에 남는 꼴, "tasks 실행의 판정에서 본 것"의 시험 폴더와 실행 스크립트)
- `plugins/plate/skills/run/SKILL.md` (tasks 끝, 합친다, `<tasks 이름>: 비움` 커밋)
- `plugins/plate/hooks/hooks.json`과 거기에 걸린 푸시 훅 (막는 경우와 막지 않는 경우)

**TODO**
- [ ] 원격 없는 run 장면: 원격이 없고 기본 브랜치가 `main`인 시험 폴더에서 셋업하고 작은 tasks를 계획해 run을 끝까지 돌리면, tasks 끝에 PR 대신 합칠지 묻는다. 승인하면 `main`에 그 tasks의 `<이름>: 비움` 커밋이 들어온다. 실행 기록은 run 본문을 마지막으로 고친 뒤에 만든다
- [ ] 푸시 훅 장면: origin이 있는 셋업된 시험 폴더에서 에이전트에게 기본 브랜치로 `git push`를 시키면 푸시 훅이 막는다. 실행 기록에 그 호출의 결과가 `is_error` `true`와 푸시 훅의 stderr로 남는다. 실행 기록은 푸시 훅 스크립트를 마지막으로 고친 뒤에 만든다
- [ ] 이 phase의 기록에 장면마다 시험 폴더와 실행 기록의 경로가 적힌다 (`docs/tasks/005-publish-verify/phase-4.md`)
- [ ] 이 phase에서 확인한 도구의 사실(Bash 호출을 막은 훅이 기록에 남는 꼴)이 시험 폴더와 실행 기록의 위치와 함께 적힌다 (`docs/TOOLS.md`)

**통과 조건**
- 완료 조건 5가 참이다.
  - 확인: 완료 조건 5의 확인을 모두 돌린다. `done-phase-4.md`는 이름이 바뀌기 전인 이 파일로 읽는다
- 이 phase에서 확인한 도구의 사실이 `docs/TOOLS.md`에 적혀 있다.
  - 확인: `docs/TOOLS.md`의 Claude Code 절을 읽어 이 phase의 장면에서 본 것이 시험 폴더와 실행 기록의 위치와 함께 있다
