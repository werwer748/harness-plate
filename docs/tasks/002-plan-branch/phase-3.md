# Phase 3: 회고 1의 문제를 고친다

**목표**: 회고 1에서 나온 문제를 고치고, 고친 plan 본문으로 헤드리스 시험을 다시 돌린다.

**테스트 먼저**: 아니오 — 바뀌는 동작이 결과물인 마크다운(스킬 본문)의 것이다

**읽을 것**
- `docs/tasks/002-plan-branch/retro.md`의 `## 회고 1` 절
- `plugins/plate/skills/plan/SKILL.md` ("1. 진행 중인 tasks가 있는지 본다"의 브랜치 문단, "7. 쓰고 커밋한다"의 첫 문단)
- `tests/test_skill_rules.py` (`PlanRulesTest.test_commits_on_tasks_branch`)
- `docs/ARCHITECTURE.md` (데이터 흐름의 `→ 계획(` 줄과 그 아래 줄), `README.md` (스킬 표의 `plan` 줄)
- `plugins/plate/skills/setup/SKILL.md` (문서 지도 구간과 `AGENTS.md`의 꼴)
- `docs/PRD.md`, `docs/ADR.md`, `docs/TOOLS.md`, `docs/BACKLOG.md` (맥락 문서. TOOLS는 헤드리스 줄, "플러그인 폴더의 편집과 권한 모드", "셸의 `=` 확장")

**TODO**
- [ ] 새 tasks를 다른 tasks의 브랜치(예: `tasks/old`)에서 계획하는 장면이 정해진다. plan 1번에서 새 tasks는 기본 브랜치일 때만 묻지 않고, 그 밖의 브랜치(다른 `tasks/…`도 든다)에서는 지금 브랜치를 보여 주고 `tasks/<이름>`에 커밋할지 묻는다. 더하는 경우는 지금대로 기본 브랜치나 그 tasks의 `tasks/<이름>`이면 묻지 않는다. 7번 첫 문단의 갈래도 이와 맞게 한다. 데이터 흐름의 계획 줄과 README의 plan 줄이 세 갈래를 이 뜻으로 적는지 보고, 어긋나면 맞춘다. `test_commits_on_tasks_branch`가 새 글을 지키게 한다 (`plugins/plate/skills/plan/SKILL.md`, `docs/ARCHITECTURE.md`, `README.md`, `tests/test_skill_rules.py`)
- [ ] 고친 본문으로 헤드리스 시험을 다시 돌린다. 돌리기 전에 작업 트리에서 낸 `git hash-object plugins/plate/skills/plan/SKILL.md`가 기록에 적힌다. `mktemp -d`로 새로 차린 시험 저장소(`main` 브랜치, origin 없음, 문서 지도 구간이 있는 `AGENTS.md`, `@AGENTS.md`만 둔 `CLAUDE.md`, 안내 글 없이 채운 `docs/PRD.md`·`docs/ARCHITECTURE.md`(명령 절 네 줄 모두 "없음")·`docs/ADR.md`, `docs/tasks/.gitkeep`이 한 커밋)에서 세 장면을 돌린다. (가) `main`에서 `/plate:plan README.md에 한 줄 소개를 더한다`를 `--plugin-dir <작업 트리>/plugins/plate --permission-mode bypassPermissions --output-format json`으로 돌리고, `--resume`으로 답과 승인을 넣어 커밋까지 간다. (나) `feature/x`에서 첫 턴만 돌린다. (다) `tasks/old`에서 첫 턴만 돌린다. 돌린 명령과 넣은 답, (가)의 `git branch --show-current`, `git log -1 --format=%s tasks/<이름>`, 돌리기 전과 뒤의 `git rev-parse main`이 기록에 붙고, (나)·(다)는 저마다 마지막 응답 글 전문과 그 자리의 `git branch --show-current`, `git log --oneline -1`, `git status --porcelain`이 기록에 붙는다 (`docs/tasks/002-plan-branch/phase-3.md`)

**통과 조건**
- 회고 1의 문제가 고쳐졌다.
  - 확인: plan 1번의 브랜치 문단과 7번 첫 문단을 다시 읽어, 새 tasks는 기본 브랜치에서만 묻지 않고 다른 `tasks/…`에서도 묻는다고 적혔는지 본다. 데이터 흐름의 `→ 계획(` 줄과 README의 `` | `plan` | `` 줄도 읽어 이 뜻과 어긋나지 않는지 본다
  - 확인: `(cd tests && python3 -m unittest test_skill_rules.PlanRulesTest.test_commits_on_tasks_branch)`가 OK다
  - 확인: 기록에 붙은 (다)의 응답 글이 `tasks/old`를 들어 `tasks/<이름>`에 커밋할지 묻고, 브랜치가 `tasks/old`이고, 마지막 커밋이 돌리기 전 그대로이고, `git status --porcelain`의 출력이 비었다
- 완료 조건 4가 고친 본문으로 다시 참이다.
  - 확인: 기록에 적힌 해시가 작업 트리에서 다시 낸 `git hash-object plugins/plate/skills/plan/SKILL.md`와 같다
  - 확인: 기록에 붙은 (가)의 출력에서 브랜치가 `tasks/<이름>`이고, 제목이 `plan: <이름>`이고, 돌리기 전과 뒤의 `main` 해시가 같다
  - 확인: 기록에 붙은 (나)의 응답 글이 `feature/x`와 `tasks/<이름>`을 들어 바꿀지 묻고, 브랜치가 `feature/x`이고, 마지막 커밋이 돌리기 전 그대로이고, `git status --porcelain`의 출력이 비었다
- 시험이 이 저장소를 바꾸지 않았다.
  - 확인: `git status --porcelain -- . ':!docs/tasks/002-plan-branch/phase-3.md' ':!docs/tasks/RUNLOG.md'`가 아무것도 내지 않는다
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다
