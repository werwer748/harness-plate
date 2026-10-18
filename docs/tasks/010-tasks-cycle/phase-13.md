# Phase 13: 검증 1의 문제를 고친다

**목표**: 검증 1에서 나온 문제를 모두 고친다.

**테스트 먼저**: 아니오 — 고칠 문제가 모두 `.md`(`plugins/plate/skills/eval/SKILL.md`, `plugins/plate/skills/run/SKILL.md`, `docs/TOOLS.md`)만 고친다.

**읽을 것**
- `docs/tasks/010-tasks-cycle/verify.md`의 `## 검증 1` 절
- `plugins/plate/skills/eval/SKILL.md`
- `plugins/plate/skills/run/SKILL.md`
- `plugins/plate/skills/phase/SKILL.md`
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/ADR.md`
- `docs/TOOLS.md`
- `~/plate-rail-test/bin/` (네 장면을 다시 돌릴 실행 도구와 시험 폴더를 만드는 도구)

**TODO**
- [ ] 하네스 eval의 낱말 "더한 phase"는 "메시지가 `plan:`으로 시작하는 커밋이 만들지 않은 phase"인데(`eval/SKILL.md` 36줄), 실행은 회고의 문제를 고칠 phase를 `plan: NNN-slug 수정`으로(`run/SKILL.md` 172줄), 고침 task의 phase를 `plan: NNN-fixes 더함`으로(345줄) 커밋한다. 글대로 따르면 실행이 더한 phase가 늘 0개라 eval 절 "대상"의 더한 phase 수와 효율의 되풀이 줄(`eval/SKILL.md` 117줄)이 틀린다 (`plugins/plate/skills/eval/SKILL.md`, `plugins/plate/skills/run/SKILL.md`)
- [ ] 실행이 쓰는 고칠 phase와 고침 task의 꼴이 수행에게 읽지 않는다는 파일을 읽게 한다. 고칠 phase의 읽을 것에 "{문제에 적힌 파일의 경로}"(`run/SKILL.md` 185줄)를 옮기면 회고가 근거로 든 `done-phase-N.md`가 들어가고, 고침 task 머리의 마지막 완료 조건의 확인이 "`docs/tasks/plan.md`의 그 완료 조건에 적힌 확인을 모두 돌린다"(374~375줄)라 `phase-1.md`의 통과 조건(399~401줄)을 돌리려면 tasks 머리를 읽어야 한다. 수행 스킬 1번은 tasks 머리와 다른 phase의 파일을 읽지 않는다고 하고(`phase/SKILL.md` 34줄), 하네스 eval은 수행이나 확인이 읽기 범위 밖을 읽은 곳을 규칙 준수 C·D로 센다(`eval/SKILL.md` 152~153줄) (`plugins/plate/skills/run/SKILL.md`)
- [ ] `docs/TOOLS.md` 21줄이 스킬을 `/plate:setup`, `/plate:context`, `/plate:plan`, `/plate:run`, `/plate:phase`, `/plate:retro`, `/plate:verify`로 부른다고 적는다. 이 tasks가 verify를 없애고 check, review, eval을 더했는데 그 줄이 그대로다 (`docs/TOOLS.md`)
- [ ] 바뀐 본문으로 네 장면(setup·plan, run task 하나씩, run 일괄 끝까지와 다시 돌림, check 세 번 실패)을 다시 돌려 기록을 `~/plate-rail-test/logs/`에 남긴다. 다시 올린 이슈는 확인한 뒤 지운다

**통과 조건**
- 검증 1의 문제가 모두 고쳐졌다.
  - 확인: 문제마다 적힌 곳을 다시 읽거나 돌린다
- 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다
