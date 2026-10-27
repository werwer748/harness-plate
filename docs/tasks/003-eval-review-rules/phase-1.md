# Phase 1: eval 본문과 문서를 고친다

**목표**: eval 본문에 #36의 해결이 들어가고 맥락 문서와 README가 맞춰진다.

**테스트 먼저**: 아니오 — `.md`(스킬 본문과 문서)만 고친다

**읽을 것**
- `plugins/plate/skills/eval/SKILL.md` (고칠 본문)
- `plugins/plate/skills/check/SKILL.md`의 "5." 절 (check가 `남은 것:` 줄을 옮기는 꼴)
- `gh issue view 36 --repo werwer748/harness-plate` (원인과 해결책)
- `git show e3836b2:docs/tasks/eval.md` (이슈가 나온 eval 절과 실패 목록)
- `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `docs/BACKLOG.md`, `README.md` (맥락 문서와 README)

**TODO**
- [ ] eval의 "2. 실패를 모아 MAST 유형으로 나눈다"에서 표 아래의 "실패가 아닌 줄" 목록에, `남은 것:`으로 시작하는 줄은 그 task의 회고 절에서 "문제"로 판정된 것만 실패로 센다(잡힌 곳은 그 자리)는 글과, 명령 절의 사실이나 판단을 적은 메모 줄은 실패가 아니라는 글이 더해진다 (#36) (`plugins/plate/skills/eval/SKILL.md`)
- [ ] eval 본문 앞머리의 description, `docs/PRD.md`의 핵심 기능 8, `docs/ARCHITECTURE.md`의 "데이터 흐름"의 tasks 끝 갈래, `README.md`의 `eval` 행 가운데 실패로 세는 줄과 어긋나는 줄이 그 동작을 담게 바뀐다 (`plugins/plate/skills/eval/SKILL.md`, `docs/PRD.md`, `docs/ARCHITECTURE.md`, `README.md`)

**통과 조건**
- 완료 조건 1이 참이다.
  - 확인: eval 본문의 "2. 실패를 모아 MAST 유형으로 나눈다"를 읽어 `남은 것:` 줄의 글과 메모 줄의 글이 저마다 있다. 하나라도 없으면 실패
  - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`, `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
- 완료 조건 2가 참이다.
  - 확인: `docs/PRD.md`의 핵심 기능 8, `docs/ARCHITECTURE.md`의 "데이터 흐름"의 tasks 끝 갈래, `README.md`의 `eval` 행, eval 본문 앞머리의 description을 저마다 읽어 실패로 세는 줄과 어긋나는 줄이 없다
