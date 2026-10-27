# Phase 3: phase 장면 G를 돌린다

**목표**: phase가 앞 phase의 기록을 읽지 않는 것(#42)을 임시 복제본에서 돌려 `docs/TOOLS.md`에 남긴다.

**테스트 먼저**: 아니오 — 스킬을 돌려 보고 `.md`에 적는다

**읽을 것**
- `plugins/plate/skills/phase/SKILL.md`의 "1. 읽는다" 절 (phase 1이 고친 동작)
- `docs/TOOLS.md`의 "Claude Code" 절 (헤드리스 명령의 꼴, 허용 목록, phase 2가 더한 plan 장면 E·F 절)

**TODO**
- [ ] 장면 G: 복제본에 `done-phase-1.md`(기록 절과 판정 통과인 확인 절)와, 읽을 것에 phase 1의 산출물 파일이 적힌 `phase-2.md`가 있는 작은 task를 차려 phase 스킬로 phase 2를 수행한다. 그 세션 기록(`~/.claude/projects/` 아래의 그 세션 id의 `.jsonl`)에서 `done-phase-1.md`를 읽은 도구 호출이 없는지와 phase 2의 TODO가 끝나 커밋됐는지 본다 (임시 폴더)
- [ ] 결과가 phase 본문의 결함을 보이면 `plugins/plate/skills/phase/SKILL.md`를 고치고 장면 G를 새 복제본에서 다시 돈다 (`plugins/plate/skills/phase/SKILL.md`)
- [ ] plan 본문을 고쳤으면 장면 E(복제본에서 plan에 "setup이 `.github/CODEOWNERS`가 없으면 만들고, 있으면 줄을 더하게 바꾼다"를 넘겨 추천안으로 답하면 초안의 완료 조건이 두 갈래마다 돌리는 확인을 두고 git 원격 장면을 `git clone --bare`로 채운다)와 장면 F(plan에 "새 스킬 하나를 더하고, 임시 복제본에서 그 스킬을 헤드리스로 돌려 본다"를 넘기면 그 phase의 초안이 TODO 첫 항목이나 결정에 앞 phase의 산출물에 대어 조건을 맞춘다)를 새 복제본에서 다시 돌고 phase 2의 절 아래에 결과를 더한다 (`docs/TOOLS.md`)
- [ ] `docs/TOOLS.md`의 plan 장면 E·F 절 뒤에 phase 장면 G 절이 더해진다. task 머리의 결정에 적힌 필드를 적는다 (`docs/TOOLS.md`)

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건 1~3의 확인을 모두 돌린다. 완료 조건 3의 장면 E~G는 그 조건에 적힌 기대로 본다
