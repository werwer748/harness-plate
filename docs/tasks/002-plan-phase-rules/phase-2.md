# Phase 2: plan 장면 E와 F를 돌린다

**목표**: 갈래마다의 확인(#37)과 앞 phase 산출물에 기대는 조건(#41)을 임시 복제본에서 plan으로 돌려 `docs/TOOLS.md`에 남긴다.

**테스트 먼저**: 아니오 — 스킬을 돌려 보고 `.md`에 적는다

**읽을 것**
- `plugins/plate/skills/plan/SKILL.md`의 "6. 초안을 보여 주고 승인받는다"와 적는 규칙의 "조건", "TODO" 절 (phase 1이 고친 동작)
- `docs/TOOLS.md`의 "Claude Code" 절 (헤드리스 명령의 꼴, `--resume`, "스킬을 헤드리스로 돌려 볼 때의 허용 목록", 장면 절의 꼴)

**TODO**
- [ ] 장면 E: 복제본에서 plan에 "setup이 `.github/CODEOWNERS`가 없으면 만들고, 있으면 줄을 더하게 바꾼다"를 넘기고, 물음마다 `--resume`으로 추천안을 골라 초안을 보여 주고 승인을 묻는 자리까지 잇는다. 보여 준 초안의 완료 조건이 없을 때와 있을 때의 두 갈래마다 돌리는 확인을 두고, git 원격이 있는 장면을 `git clone --bare`로 채운다고 적었는지 본다 (임시 폴더)
- [ ] 장면 F: 새 복제본에서 plan에 "새 스킬 하나를 더하고, 임시 복제본에서 그 스킬을 헤드리스로 돌려 본다"를 넘기고 같은 방법으로 task 초안을 보여 주는 자리까지 잇는다. 스킬을 돌려 보는 phase의 초안이 TODO 첫 항목이나 결정에 앞 phase의 산출물에 대어 조건을 맞춘다고 적었는지 본다 (임시 폴더)
- [ ] 결과가 plan 본문의 결함을 보이면 `plugins/plate/skills/plan/SKILL.md`를 고치고 두 장면을 새 복제본에서 다시 돈다 (`plugins/plate/skills/plan/SKILL.md`)
- [ ] `docs/TOOLS.md`의 "Claude Code" 절 끝에 plan 장면 E·F 절이 더해진다. task 머리의 결정에 적힌 필드를 장면마다 적는다 (`docs/TOOLS.md`)

**통과 조건**
- 장면 E와 F의 결과가 남았고 기대대로다(완료 조건 3의 E, F).
  - 확인: 더해진 절을 읽어 장면 E·F마다 Claude Code 버전, 돌린 시각, 세션 id, 기대한 결과와 본 결과가 있고 본 결과가 기대와 같다. 장면 E의 기대는 초안의 완료 조건이 두 갈래마다 돌리는 확인을 두고 git 원격 장면을 `git clone --bare`로 채운다고 적은 것, 장면 F의 기대는 스킬을 돌려 보는 phase의 초안이 TODO 첫 항목이나 결정에 앞 phase의 산출물에 대어 조건을 맞춘다고 적은 것이다
  - 확인: 그 절의 돌린 시각이 `git log -1 --format=%cI -- plugins/plate/skills/plan/SKILL.md`보다 늦다
- 완료 조건 1이 여전히 참이다(이 phase가 plan 본문을 고쳤을 때).
  - 확인: plan 본문의 "6. 초안을 보여 주고 승인받는다"와 적는 규칙의 "조건", "TODO" 절, phase 본문의 "1. 읽는다" 절을 읽어 세 해결이 저마다 적혀 있다
  - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`, `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
