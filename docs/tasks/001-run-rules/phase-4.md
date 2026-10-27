# Phase 4: 회고 1의 문제를 고친다

**목표**: 회고 1에서 나온 문제를 모두 고친다.

**테스트 먼저**: 아니오 — 고칠 문제가 `.md`(스킬 본문과 문서)만 고치고 코드 파일의 동작을 바꾸지 않는다

**읽을 것**
- `docs/tasks/001-run-rules/retro.md`의 `## 회고 1`부터 `## 회고 1`까지의 절
- `plugins/plate/skills/run/SKILL.md`
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/ADR.md`
- `docs/TOOLS.md`
- `docs/BACKLOG.md`
- `README.md`

**TODO**
- [ ] run 본문이 #35를 고치며 `docs/TOOLS.md`에 적은 까닭을 "다음 `RUNLOG.md` 커밋에 함께 넣는다"(512행)고 했는데, 그 커밋 자리는 모두 다른 파일을 막는다: 회고·코드 평가·하네스 eval 뒤는 "`RUNLOG.md`만 한 커밋"(167·292·302·501행), phase 통과는 "이 변경과 `RUNLOG.md`만"(154행), 고칠 phase는 "그 파일과 `RUNLOG.md`만"(195행)이다. 어느 쪽을 따르든 한 글을 어기고, 커밋 자리의 글을 따르면 `docs/TOOLS.md`가 커밋되지 않은 채 남아 "고칠지"에서 작업 트리가 깨끗하다는 #44의 목표와 어긋난다. 고칠 동작을 적은 맥락 문서와 README의 줄(`docs/PRD.md` 17행의 핵심 기능 7, `docs/ARCHITECTURE.md` 52행의 run 문단과 69행의 데이터 흐름, `README.md` 10행의 `run` 행)도 고친 뒤 그 동작과 맞게 한다 (`plugins/plate/skills/run/SKILL.md`, `docs/PRD.md`, `docs/ARCHITECTURE.md`, `README.md`)
- [ ] 고친 run으로 장면 B를 task 머리의 결정대로 다시 돌려, 회고 뒤와 하네스 eval 뒤에 `RUNLOG.md`만 바꾼 커밋이 있고 "고칠지"에서 `git status --short`가 비었는지 보고, 결과를 `docs/TOOLS.md`의 장면 B 절에 새 시각, 세션 id, 돌릴 때의 run 본문 해시(`git hash-object plugins/plate/skills/run/SKILL.md`)와 함께 더한다 (`docs/TOOLS.md`)

**통과 조건**
- 회고 1의 문제가 모두 고쳐졌다.
  - 확인: TODO에 넣은 문제마다 적힌 곳(run 본문의 `docs/TOOLS.md`를 커밋에 넣는 글과 154·167·195·292·302·501행 근처의 커밋 자리 글)을 다시 읽어 서로 어긋나지 않고, `docs/TOOLS.md`에 적은 까닭이 커밋되지 않은 채 남는 길이 없다. 그 동작을 적은 `docs/PRD.md`, `docs/ARCHITECTURE.md`, `README.md`의 줄을 다시 읽어 고친 동작과 어긋나지 않는다
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다
