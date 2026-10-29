# Phase 4: 작업 트리의 eval을 헤드리스로 돌려 본다

**목표**: 작업 트리의 eval이 시험 저장소에서 등급만 낮춘 고칠 거리를 "eval에만"으로, 결과에 피해가 난 일반적인 고칠 거리를 기준을 넘은 것으로 적는 것을 본다.

**테스트 먼저**: 아니오 — 코드를 바꾸지 않고 스킬 본문을 돌려 본다

**읽을 것**
- `plugins/plate/skills/eval/SKILL.md` ("1. 읽는다"가 읽는 파일 모두, "5. 하네스 고칠 거리를 정한다", "기록의 양식")
- 시험 기록의 꼴: `plugins/plate/skills/plan/SKILL.md`의 "계획 파일의 양식", `plugins/plate/skills/phase/SKILL.md`의 "기록의 양식", `plugins/plate/skills/check/SKILL.md`의 "확인 절의 양식", `plugins/plate/skills/retro/SKILL.md`의 "기록의 양식"과 "`FRICTION.md`의 줄", `plugins/plate/skills/review/SKILL.md`의 "기록의 양식", `plugins/plate/skills/run/SKILL.md`의 "`RUNLOG.md`"
- `docs/TOOLS.md` (Claude Code 절의 헤드리스 줄, "스킬을 헤드리스로 돌려 볼 때의 허용 목록", "플러그인 폴더의 편집과 권한 모드")

**TODO**
- [x] `mktemp -d`로 만든 시험 저장소에 git 저장소, 문서 지도 구간이 있는 `AGENTS.md`, eval "1. 읽는다"가 읽는 파일(tasks 머리, task 머리, `done-phase-N.md`, `retro.md`, `FRICTION.md`, `RUNLOG.md`, `review.md`)이 위 꼴대로 차려지고, 계획과 phase와 회고의 커밋으로 들어간다. `docs/BACKLOG.md`는 두지 않는다. 기록에는 두 고칠 거리가 심긴다. A(등급만): 수행이 확인 명령을 다른 도구로 묶어 돌렸다가 적힌 차림으로 다시 돌려 통과했고, 확인 절의 "하네스에서 걸린 것"에만 적혔다. 결과물 결함이나 다시 수행은 없다. B(피해, 일반): plate:phase의 규칙 때문에 완료 조건이 이뤄지지 않은 것을 회고가 찾아 고칠 phase를 더해 다시 수행했고, 회고 1이 문제 있음, 회고 2가 통과이며 `FRICTION.md`에 적혔다 (시험 저장소)
- [x] 돌리기 전에 작업 트리에서 낸 `git hash-object plugins/plate/skills/eval/SKILL.md`가 기록에 적힌다 (`docs/tasks/001-issue-criteria/phase-4.md`)
- [x] 시험 저장소에서 `claude -p --plugin-dir <작업 트리>/plugins/plate --permission-mode bypassPermissions "/plate:eval"`이 돌고, 돌린 명령과 시험 저장소 `docs/tasks/eval.md`의 "하네스 고칠 거리" 절 전문이 기록에 붙는다. A는 기준이 "eval에만"이고 처리·문턱·이슈 줄이 없고, B는 기준이 넘음이고 처리 줄이 있어야 한다 (`docs/tasks/001-issue-criteria/phase-4.md`)

**통과 조건**
- 완료 조건 5가 참이다.
  - 확인: 기록에 적힌 해시가 작업 트리에서 다시 낸 `git hash-object plugins/plate/skills/eval/SKILL.md`와 같다
  - 확인: 기록에 붙은 "하네스 고칠 거리" 절에서 A의 항목은 `- 기준: eval에만`으로 시작하는 줄이 있고 처리·문턱·이슈 제목·이슈 본문 줄이 없으며, B의 항목은 `- 기준: 넘음`으로 시작하는 줄과 `- 처리:` 줄이 있다
- 시험이 이 저장소를 바꾸지 않았다.
  - 확인: `git status --porcelain -- . ':!docs/tasks/001-issue-criteria/phase-4.md' ':!docs/tasks/RUNLOG.md'`가 아무것도 내지 않는다
- 테스트가 모두 통과한다(완료 조건 6).
  - 확인: `python3 -m unittest discover -s tests`가 OK다

## 한 일
- `mktemp -d`로 만든 시험 저장소를 차렸다: `/var/folders/0j/cj37rxmj1mj73vhflqpgsxm00000gn/T/tmp.NzuCKG53PT`에 git 저장소(main), 문서 지도 구간이 있는 `AGENTS.md`(`docs/BACKLOG.md` 행은 있고 파일은 없다), `CLAUDE.md`, `docs/ARCHITECTURE.md`(명령 절), `greet.py`와 테스트, tasks 머리(`greet`), task 머리(`001-hello`), `done-phase-1.md`, 더한 phase인 `done-phase-2.md`(`# Phase 2: 회고 1의 문제를 고친다`), `retro.md`(회고 1 문제 있음, 회고 2 통과), `FRICTION.md`, `RUNLOG.md`(tasks 일괄, 에이전트 7줄, 물은 줄 1줄), `review.md`(평가 1)를 양식대로 두고 `plan: greet`부터 `greet: RUNLOG`까지 15커밋(init 포함)으로 넣었다. A(등급만): phase 1 수행이 확인을 `pytest -q tests`로 먼저 돌렸다가 적힌 `python3 -m unittest discover -s tests`로 다시 돌려 OK였고, 확인 1의 "하네스에서 걸린 것"에만 적혔다. B(피해, 일반): plate:phase 3번 "실패하면 고쳐서 다시 돌린다"대로 수행이 실패한 테스트의 입력을 `greet(None)`으로 바꿔 통과시켜, 회고 1이 완료 조건 1 실패로 찾고 phase 2를 더해 다시 수행했고, 회고 2가 통과이며 `FRICTION.md`에 문제 줄로 적혔다. 차림 스크립트는 세션 scratchpad의 `setup_eval_repo.sh`다 (시험 저장소)
- 돌리기 전 작업 트리의 해시: `git hash-object plugins/plate/skills/eval/SKILL.md` → `ac05dfe6b1a2ec0be73680e8e073566778c87c3e` (`docs/tasks/001-issue-criteria/phase-4.md`)
- 시험 저장소에서 `claude -p --plugin-dir /Users/hugo/Desktop/harness-plate/plugins/plate --permission-mode bypassPermissions "/plate:eval"`을 돌렸다(Claude Code 2.1.312, 종료 0). 돌려준 줄: `등급: 결과 성공 A, 일관성 C, 효율 D, 규칙 준수 A, 사람 개입률 A, 실패 양상 C`, `고칠 거리: plate 자체 3개, 이 프로젝트만 0개`. 시험 저장소에 `3fd428f greet: 하네스 eval`이 `docs/tasks/eval.md` 하나만 넣어 커밋됐다. A는 고칠 거리 3(기준 eval에만, 처리·문턱·이슈 줄 없음), B는 고칠 거리 1(기준 넘음, 처리·문턱·이슈 줄 있음)이다. eval은 B의 원인으로 plate:plan의 통과 조건(고칠 거리 2)도 따로 세웠다. 시험 저장소 `docs/tasks/eval.md`의 "하네스 고칠 거리" 절 전문 (`docs/tasks/001-issue-criteria/phase-4.md`):

**하네스 고칠 거리**
1. plate:phase 3번 "실패하면 고쳐서 다시 돌린다"가 무엇을 고칠지 정하도록 고친다 (근거: 실패 2). 갈래: plate 자체
   - 기준: 넘음 — 피해: 결함이 phase의 확인을 지나가 회고에서 잡혔고 고칠 phase를 더해 다시 수행했다(되풀이 몫 35.6%). 일반성: 테스트가 실패하면 테스트를 맞추는 일은 어느 프로젝트에서도 난다. 고침의 꼴: "계획이 정한 기대(통과 조건의 확인, 테스트의 입력과 기대값)는 바꾸지 않고 구현을 고친다. 기대가 틀렸다고 보면 계획이 틀림으로 멈춘다"는 원리로 적을 수 있다
   - 처리: 규칙을 더하거나 고친다 — 한 줄 규칙으로 막히고, 다시 날 때의 값(결함 통과, phase 다시 수행)이 크다
   - 문턱: 넘음 — 잡힌 곳이 task의 회고인 실패 2
   - 이슈 제목: plate:phase: 확인이 실패하면 기대가 아니라 구현을 고치도록 규칙을 정한다
   - 이슈 본문: phase 수행이 새로 쓴 테스트가 실패하자 구현 대신 테스트의 입력을 바꿔 통과시켰고, 결함이 phase 확인을 지나 task 회고에서야 완료 조건 실패로 잡혀 고칠 phase를 더해 다시 수행했다. 원인: plate:phase 3번 "실패하면 고쳐서 다시 돌린다"가 고칠 쪽(구현인지, 테스트나 확인의 기대인지)을 정하지 않는다. 해결책: 계획이 정한 기대(통과 조건의 확인, TODO가 정한 테스트의 입력과 기대값)는 바꾸지 않고 구현을 고치며, 기대가 틀렸다고 보면 고치지 않고 "계획이 틀림"으로 멈춘다는 원리를 3번에 더한다. 근거: `greet`, `8cc1436` `docs/tasks/001-hello/done-phase-1.md`, `017c7e6` `docs/tasks/001-hello/retro.md`
2. phase의 통과 조건이 그 phase가 이루는 task 완료 조건의 확인을 담도록 plate:plan을 고친다 (근거: 실패 3). 갈래: plate 자체
   - 기준: 넘음 — 피해: 통과 조건이 테스트 통과만 봐 결과물의 결함이 phase의 확인을 지나갔다. 일반성: 테스트 통과만 통과 조건으로 두는 phase는 어느 프로젝트에서도 흔하다. 고침의 꼴: "phase가 이루는 task 완료 조건이 있으면 그 확인을 phase의 통과 조건에 그대로 넣는다"는 원리로 적을 수 있다
   - 처리: 규칙을 더하거나 고친다 — 계획을 쓸 때 한 줄을 옮기는 값이 결함이 회고까지 가는 값보다 작다
   - 문턱: 넘음 — 잡힌 곳이 task의 회고인 실패 3
   - 이슈 제목: plate:plan: phase 통과 조건에 그 phase가 이루는 task 완료 조건의 확인을 넣는다
   - 이슈 본문: phase의 통과 조건이 테스트 통과만 보고 task 완료 조건의 직접 확인을 넣지 않아, 테스트를 바꿔 통과시킨 결과물이 phase 확인을 지나 task 회고에서 완료 조건 실패로 잡혔다. 원인: plate:plan이 phase의 통과 조건을 쓸 때 그 phase가 이루는 task 완료 조건의 확인을 넣으라고 정하지 않는다. 해결책: phase가 이루는(또는 마지막으로 이루는) task 완료 조건이 있으면 그 확인을 phase의 통과 조건에 그대로 넣는다는 원리를 plan의 phase 양식 규칙에 더한다. 근거: `greet`, `e5592ff` `docs/tasks/001-hello/done-phase-1.md`, `017c7e6` `docs/tasks/001-hello/retro.md`
3. phase 수행이 통과 조건의 확인을 적힌 명령 대신 다른 도구로 돌린 줄을 기록에 남기지 않게 한다 (근거: 실패 1). 갈래: plate 자체
   - 기준: eval에만 — 피해를 넘지 않는다. 확인이 적힌 차림으로 다시 돌려 결과가 같았고 다시 수행이나 멈춤이 없었다

## 확인 결과
- 완료 조건 5가 참이다.
  - `git hash-object plugins/plate/skills/eval/SKILL.md`를 시험 뒤 작업 트리에서 다시 냄 → `ac05dfe6b1a2ec0be73680e8e073566778c87c3e`, 기록의 값과 같다. 통과
  - 위에 붙인 절 → A(고칠 거리 3)는 `- 기준: eval에만`으로 시작하는 줄만 있고 처리·문턱·이슈 제목·이슈 본문 줄이 없다. B(고칠 거리 1)는 `- 기준: 넘음`으로 시작하는 줄과 `- 처리:` 줄이 있다. 통과
- 시험이 이 저장소를 바꾸지 않았다.
  - `git status --porcelain -- . ':!docs/tasks/001-issue-criteria/phase-4.md' ':!docs/tasks/RUNLOG.md'` → 출력 없음(이 기록을 쓰기 전에 돌렸고 쓴 뒤에도 phase-4.md 말고는 같다). 통과
- 테스트가 모두 통과한다(완료 조건 6).
  - `python3 -m unittest discover -s tests` → `Ran 205 tests in 18.083s` `OK`. 통과

## 계획과 달라진 점
- 없음

## 남은 것
- 시험은 한 번 돌렸다. 같은 기록에서 eval이 A와 B를 늘 같게 가르는지는 보지 않았다
- 시험 저장소는 시스템 임시 폴더(`/var/folders/0j/cj37rxmj1mj73vhflqpgsxm00000gn/T/tmp.NzuCKG53PT`)에 남아 있다. 지우지 않았다

## 하네스에서 걸린 것
- 없음
