# Phase 2: 임시 복제본에서 두 장면으로 돌린다

**목표**: cleanup 스킬을 헤드리스로 돌려 장면 1(만들지 않음)과 장면 2(만든다)의 결과를 `docs/TOOLS.md`에 남긴다.

**테스트 먼저**: 아니오 — 스킬을 돌려 보고 `.md`에 적는다

**읽을 것**
- `plugins/plate/skills/cleanup/SKILL.md` (phase 1이 쓴 본문)
- `docs/TOOLS.md`의 "Claude Code" 절 (헤드리스 명령의 꼴, `--resume`, 허용 목록, 세션이 폴더에 묶이는 것, 막힌 명령 하나마다 기다리는 시간)

**TODO**
- [ ] task 머리 결정의 "확인용 실행"대로 임시 복제본에서 첫 턴을 백그라운드로 돌리고, 묻는 자리에서 멈춘 것과 그 시점의 복제본 상태(`git show --name-only HEAD`, `git status --short`, 보고서의 여섯 기준 절, 지도 행)를 본다 (임시 폴더)
- [ ] 장면 2를 `--resume <id> --fork-session`과 "만든다, 1번"으로 잇고, 기록에서 `plate:plan` 스킬 호출과 그 요청 글에 보고서 경로가 든 것을 본다. 복제본의 `git status --short`가 비었는지도 본다 (임시 폴더)
- [ ] 장면 1을 원래 세션 id와 "만들지 않는다"로 잇고, 보고서가 "미룸" 표시와 함께 커밋되고 `docs/tasks/plan.md`가 생기지 않은 것을 본다 (임시 폴더)
- [ ] 결과가 스킬의 결함을 보이면 `plugins/plate/skills/cleanup/SKILL.md`를 고치고 세 TODO를 새 복제본에서 다시 돈다 (`plugins/plate/skills/cleanup/SKILL.md`)
- [ ] `docs/TOOLS.md`의 "Claude Code" 절 끝에 새 절이 더해진다. Claude Code 버전, 복제본의 main 커밋, 첫 턴 시각, 세션 id 둘, 1라운드와 2라운드에 띄운 에이전트 수, 장면마다의 결과(장면 1: 커밋된 파일 목록, 여섯 기준 절, 미룸 커밋. 장면 2: `plate:plan` 호출 줄), 걸린 시간, 막힌 명령을 적는다. 임시 폴더의 기록 경로도 적되 지워질 수 있다고 밝힌다 (`docs/TOOLS.md`)
- [ ] `docs/TOOLS.md`의 "Claude Code" 절 첫 문단의 판정 버전 목록에 이 tasks의 시험 버전과 날짜가 더해진다 (`docs/TOOLS.md`)

**통과 조건**
- 두 장면의 결과가 남았다(완료 조건 2)
  - 확인: `docs/TOOLS.md`의 새 절을 읽어 두 장면이 저마다 Claude Code 버전, 돌린 시각, 세션 id, 결과를 적었다. 장면 1은 커밋된 파일 목록(보고서와 `AGENTS.md`뿐)과 보고서의 여섯 기준 절, 장면 2는 `plate:plan` 호출 줄이다. 하나라도 없으면 실패
  - 확인: 그 절의 첫 턴 시각이 `git log -1 --format=%cI -- plugins/plate/skills/cleanup/SKILL.md`보다 늦다
  - 확인: 그 절의 에이전트 수가 1라운드 6, 2라운드 6이다
- 스킬 본문이 여전히 맞다(완료 조건 1)
  - 확인: `head -3 plugins/plate/skills/cleanup/SKILL.md`에 `name: cleanup`이 있고, `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
  - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
