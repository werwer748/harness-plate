# harness-plate

레일 하네스 `plate`의 플러그인 레포다. 지금은 스킬이 아홉 있다.

| 스킬 | 하는 일 |
|---|---|
| `setup` | 프로젝트에 하네스 문서의 위치 기준을 세운다. 설치만 하고 묻지 않고 끝난다 |
| `context` | 셋업이 만든 문서의 남은 칸을 저장소 스캔과 질문으로 채운다 |
| `plan` | 요청 하나를 tasks로 계획해 `docs/tasks/`에 tasks 머리 `plan.md`와, task 폴더 `NNN-slug/`마다 task 머리 `plan.md`와 phase마다의 `phase-N.md`로 쓰고 한 커밋으로 넣는다 |
| `run` | 계획된 tasks를 phase 하나씩 실행한다. 시작할 때 실행 방식(task 하나씩, tasks 일괄)을 묻고, 수행, 확인, 회고, 평가를 저마다 새 에이전트에게 맡기고, tasks 끝에서 보고하고 고칠지 묻는다 |
| `phase` | 계획의 phase 하나를 수행하고 한 일의 기록을 `phase-N.md`에 덧붙인다. `run`이 띄운 에이전트가 부른다 |
| `check` | 수행이 끝난 phase 하나의 통과 조건과 빌드·린트·테스트를 돌려 `phase-N.md`에 확인 절을 더한다. `run`이 띄운 에이전트가 부른다 |
| `retro` | phase가 모두 통과한 task 하나를 회고해 task 폴더의 `retro.md`와 `docs/tasks/FRICTION.md`에 적는다. `run`이 띄운 에이전트가 부른다 |
| `review` | 모든 task가 끝난 tasks에서 바뀐 코드를 다섯 범주로 A~E로 평가해 `docs/tasks/review.md`에 적는다. `run`이 띄운 에이전트가 부른다 |
| `eval` | 모든 task가 끝난 tasks에서 하네스가 어떻게 돌았는지 여섯 기준으로 A~E로 평가해 `docs/tasks/eval.md`에 적는다. `run`이 띄운 에이전트가 부른다 |

## 설치

`<폴더>`는 이 레포를 받은 폴더의 경로다.

### Claude Code

```bash
claude plugin marketplace add <폴더>
claude plugin install plate@harness-plate
```

설치하지 않고 한 세션에서만 쓰려면 `claude --plugin-dir <폴더>/plugins/plate`로 시작한다. 스킬은 `/plate:setup`, `/plate:context`, `/plate:plan`, `/plate:run`, `/plate:phase`, `/plate:check`, `/plate:retro`, `/plate:review`, `/plate:eval`로 부른다.

### Codex

```bash
codex plugin marketplace add <폴더>
codex plugin add plate@harness-plate
```

스킬은 `$plate:setup`, `$plate:context`, `$plate:plan`, `$plate:run`, `$plate:phase`, `$plate:check`, `$plate:retro`, `$plate:review`, `$plate:eval`로 부른다. Codex는 설치할 때 플러그인을 복사해 두므로, 스킬이 바뀌면 `codex plugin add plate@harness-plate`를 다시 실행한다.

Codex에서의 확인은 2026-10-08에 멈춘 상태다. 그 뒤에 고친 스킬과 새로 더한 `plan`, `run`, `phase`, `check`, `retro`, `review`, `eval` 스킬은 Codex에서 확인하지 않았고, 확인해 둔 것과 남은 것은 `docs/TOOLS.md`에 있다.
