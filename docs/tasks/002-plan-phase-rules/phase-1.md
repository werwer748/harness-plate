# Phase 1: plan과 phase 본문과 문서를 고친다

**목표**: plan과 phase 본문에 세 이슈의 해결이 들어가고 맥락 문서와 README가 맞춰진다.

**테스트 먼저**: 아니오 — `.md`(스킬 본문과 문서)만 고친다

**읽을 것**
- `plugins/plate/skills/plan/SKILL.md`, `plugins/plate/skills/phase/SKILL.md` (고칠 본문)
- `gh issue view 37 --repo werwer748/harness-plate`, 41, 42 (이슈마다의 원인과 해결책)
- `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `docs/BACKLOG.md`, `README.md` (맥락 문서와 README)

**TODO**
- [ ] plan 적는 규칙의 "조건" 절에 완료 조건이 갈래를 가지면 갈래마다 돌리는 확인을 두고, 요약 줄을 보는 확인에는 견줄 갈래를 적고, git 원격이 있는 장면은 `git clone --bare`로 푸시 없이 채운다는 글이 더해지고, "6. 초안을 보여 주고 승인받는다"의 점검 목록에 같은 점검이 더해진다 (#37) (`plugins/plate/skills/plan/SKILL.md`)
- [ ] plan 적는 규칙의 "TODO" 절(또는 "결정" 절)에 뒤 phase의 실행 조건(허용 목록, 차례)이 앞 phase의 산출물에 기대면 그 phase의 TODO 첫 항목에 "앞 phase의 산출물에 대어 조건을 맞춘다"를 두거나 결정에 "앞 phase의 결과로 정한다"고 적는다는 글이 더해지고, 6번의 점검 목록에 같은 점검이 더해진다 (#41) (`plugins/plate/skills/plan/SKILL.md`)
- [ ] phase 본문의 "1. 읽는다"에 앞 phase의 결과가 필요하면 계획의 읽을 것에 적힌 산출물 파일만 읽고, 그 밖의 앞 phase 기록이 필요하면 읽지 않고 "하네스에서 걸린 것"에 적는다는 글이 더해진다 (#42) (`plugins/plate/skills/phase/SKILL.md`)
- [ ] 두 본문 앞머리의 description, `docs/PRD.md`의 핵심 기능 3·4, `docs/ARCHITECTURE.md`의 "데이터 흐름"의 계획과 실행 갈래, `README.md`의 `plan`·`phase` 행 가운데 세 동작과 어긋나는 줄이 그 동작을 담게 바뀐다 (`plugins/plate/skills/plan/SKILL.md`, `plugins/plate/skills/phase/SKILL.md`, `docs/PRD.md`, `docs/ARCHITECTURE.md`, `README.md`)

**통과 조건**
- 완료 조건 1의 본문이 적혀 있다.
  - 확인: plan 본문의 "6. 초안을 보여 주고 승인받는다"와 적는 규칙의 "조건", "TODO" 절, phase 본문의 "1. 읽는다" 절을 읽어 세 해결이 저마다 적혀 있다. 하나라도 없으면 실패
  - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`, `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
- 완료 조건 2가 참이다.
  - 확인: `docs/PRD.md`의 핵심 기능 3·4, `docs/ARCHITECTURE.md`의 "데이터 흐름"의 계획과 실행 갈래, `README.md`의 `plan`·`phase` 행, 두 본문 앞머리의 description을 저마다 읽어 세 동작과 어긋나는 줄이 없다
