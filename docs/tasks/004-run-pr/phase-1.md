# Phase 1: tasks 끝의 PR

**목표**: run이 tasks 끝에 PR을 열지 묻고, 승인하면 tasks 브랜치를 푸시해 PR을 연다.

**테스트 먼저**: 아니오 — 스킬 본문과 문서(`.md`)만 고친다

**읽을 것**
- `plugins/plate/skills/run/SKILL.md` (절대 규칙, 낱말의 기본 브랜치, tasks 끝, 비운다, 합친다, 10번 보고, `RUNLOG.md`)
- `plugins/plate/skills/eval/SKILL.md` (정해 둔 물음)
- `plugins/plate/skills/setup/SKILL.md`의 양식 절 (`002-ci-workflow`가 만든 plate 워크플로의 파일 이름)
- `docs/TOOLS.md`의 "tasks 실행의 판정에서 본 것" (`gh`로 이슈를 올린 꼴, 본문을 heredoc으로 넘기는 꼴)
- `docs/ARCHITECTURE.md` (패턴과 규칙의 run 규칙, 데이터 흐름), `docs/PRD.md` (핵심 기능 8)

**TODO**
- [ ] tasks 끝의 "비운다" 뒤에 PR 절이 생긴다. origin이 GitHub이면 푸시할 브랜치와 PR 제목·본문을 보여 주고 PR을 열지 묻는다. 승인하면 `tasks/<이름>`을 origin에 푸시하고 기본 브랜치로 가는 PR을 연다. 본문에는 tasks 머리의 요청과 목표, tasks 끝의 전체 보고가 들고, 둘은 비우기 전에 읽어 둔다. plate의 CI 워크플로가 없으면 `review.md`의 마지막 평가 절을 PR 댓글로 단다. 거절하면 브랜치를 그대로 둔다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] origin이 GitHub이 아니거나 없으면 지금의 "합친다"로 간다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] 절대 규칙 5가 tasks 브랜치를 PR로 열 때의 푸시를 허락하고, 10번 보고에 PR 주소와 댓글 주소(열지 않았으면 그 까닭)가 들며, 설명(description)이 PR을 적는다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] eval의 "정해 둔 물음"에 PR을 열지가 든다 (`plugins/plate/skills/eval/SKILL.md`)
- [ ] ARCHITECTURE의 run 규칙과 데이터 흐름, PRD의 핵심 기능 8이 PR로 가는 tasks 끝을 적는다 (`docs/ARCHITECTURE.md`, `docs/PRD.md`)

**통과 조건**
- 완료 조건 1, 2, 3이 참이다.
  - 확인: 완료 조건 1, 2, 3의 확인을 모두 돌린다
