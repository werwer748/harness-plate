# Phase 2: 고친 cleanup 스킬을 임시 복제본에서 두 장면으로 다시 돌린다

**목표**: phase 1이 고친 `SKILL.md`로 장면 1(만들지 않음)과 장면 2(만든다)를 다시 돌려 `docs/TOOLS.md`에 새 기록을 남긴다.

**테스트 먼저**: 아니오 — 스킬을 돌려 보고 `.md`에 적는다

**읽을 것**
- `plugins/plate/skills/cleanup/SKILL.md`
- `docs/TOOLS.md`의 "Claude Code" 절 (헤드리스 명령의 꼴, `--resume`/`--fork-session`, 허용 목록, 지난 두 장면 기록 "cleanup 스킬을 두 장면으로 돌려 본 것")

**TODO**
- [ ] 이 레포를 `mktemp -d`에 복제한 곳(main)에서 worktree의 plugins/plate를 `--plugin-dir`로 실어, "Claude Code" 절의 허용 목록으로 첫 턴을 헤드리스로 돌리고, 묻는 자리에서 멈춘 것과 그 시점의 복제본 상태(`git show --name-only HEAD`, `git status --short`, 보고서의 여섯 기준 절, 지도 행)를 본다 (임시 폴더)
- [ ] 장면 2를 `--resume <id> --fork-session`과 "만든다, 1번"으로 잇고, 기록에서 `plate:plan` 스킬 호출 줄을 본다 (임시 폴더)
- [ ] 장면 1을 원래 세션 id와 "만들지 않는다"로 잇고, 보고서와 지도 행만 커밋되고 다른 파일이 바뀌지 않은 것을 본다 (임시 폴더)
- [ ] `docs/TOOLS.md`의 "Claude Code" 절 끝에 새 절을 더한다. Claude Code 버전, 복제본의 main 커밋, 장면마다 돌린 시각과 세션 id, 장면마다의 결과(장면 1: 커밋된 파일 목록과 보고서의 여섯 기준 절, 장면 2: `plate:plan` 호출 줄), 새 허용 목록으로 막힌 명령을 적는다 (`docs/TOOLS.md`)

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다. 완료 조건 6의 "새 절"은 이 phase가 더한 절이다
