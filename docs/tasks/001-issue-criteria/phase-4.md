# Phase 4: 작업 트리의 eval을 헤드리스로 돌려 본다

**목표**: 작업 트리의 eval이 시험 저장소에서 등급만 낮춘 고칠 거리를 "eval에만"으로, 결과에 피해가 난 일반적인 고칠 거리를 기준을 넘은 것으로 적는 것을 본다.

**테스트 먼저**: 아니오 — 코드를 바꾸지 않고 스킬 본문을 돌려 본다

**읽을 것**
- `plugins/plate/skills/eval/SKILL.md` ("1. 읽는다"가 읽는 파일 모두, "5. 하네스 고칠 거리를 정한다", "기록의 양식")
- 시험 기록의 꼴: `plugins/plate/skills/plan/SKILL.md`의 "계획 파일의 양식", `plugins/plate/skills/phase/SKILL.md`의 "기록의 양식", `plugins/plate/skills/check/SKILL.md`의 "확인 절의 양식", `plugins/plate/skills/retro/SKILL.md`의 "기록의 양식"과 "`FRICTION.md`의 줄", `plugins/plate/skills/review/SKILL.md`의 "기록의 양식", `plugins/plate/skills/run/SKILL.md`의 "`RUNLOG.md`"
- `docs/TOOLS.md` (Claude Code 절의 헤드리스 줄, "스킬을 헤드리스로 돌려 볼 때의 허용 목록", "플러그인 폴더의 편집과 권한 모드")

**TODO**
- [ ] `mktemp -d`로 만든 시험 저장소에 git 저장소, 문서 지도 구간이 있는 `AGENTS.md`, eval "1. 읽는다"가 읽는 파일(tasks 머리, task 머리, `done-phase-N.md`, `retro.md`, `FRICTION.md`, `RUNLOG.md`, `review.md`)이 위 꼴대로 차려지고, 계획과 phase와 회고의 커밋으로 들어간다. `docs/BACKLOG.md`는 두지 않는다. 기록에는 두 고칠 거리가 심긴다. A(등급만): 수행이 확인 명령을 다른 도구로 묶어 돌렸다가 적힌 차림으로 다시 돌려 통과했고, 확인 절의 "하네스에서 걸린 것"에만 적혔다. 결과물 결함이나 다시 수행은 없다. B(피해, 일반): plate:phase의 규칙 때문에 완료 조건이 이뤄지지 않은 것을 회고가 찾아 고칠 phase를 더해 다시 수행했고, 회고 1이 문제 있음, 회고 2가 통과이며 `FRICTION.md`에 적혔다 (시험 저장소)
- [ ] 돌리기 전에 작업 트리에서 낸 `git hash-object plugins/plate/skills/eval/SKILL.md`가 기록에 적힌다 (`docs/tasks/001-issue-criteria/phase-4.md`)
- [ ] 시험 저장소에서 `claude -p --plugin-dir <작업 트리>/plugins/plate --permission-mode bypassPermissions "/plate:eval"`이 돌고, 돌린 명령과 시험 저장소 `docs/tasks/eval.md`의 "하네스 고칠 거리" 절 전문이 기록에 붙는다. A는 기준이 "eval에만"이고 처리·문턱·이슈 줄이 없고, B는 기준이 넘음이고 처리 줄이 있어야 한다 (`docs/tasks/001-issue-criteria/phase-4.md`)

**통과 조건**
- 완료 조건 5가 참이다.
  - 확인: 기록에 적힌 해시가 작업 트리에서 다시 낸 `git hash-object plugins/plate/skills/eval/SKILL.md`와 같다
  - 확인: 기록에 붙은 "하네스 고칠 거리" 절에서 A의 항목은 `- 기준: eval에만`으로 시작하는 줄이 있고 처리·문턱·이슈 제목·이슈 본문 줄이 없으며, B의 항목은 `- 기준: 넘음`으로 시작하는 줄과 `- 처리:` 줄이 있다
- 시험이 이 저장소를 바꾸지 않았다.
  - 확인: `git status --porcelain -- . ':!docs/tasks/001-issue-criteria/phase-4.md' ':!docs/tasks/RUNLOG.md'`가 아무것도 내지 않는다
- 테스트가 모두 통과한다(완료 조건 6).
  - 확인: `python3 -m unittest discover -s tests`가 OK다
