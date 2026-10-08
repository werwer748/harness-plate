# harness-plate

레일 하네스 `plate`의 플러그인 레포다. 지금은 스킬이 셋 있다.

| 스킬 | 하는 일 |
|---|---|
| `setup` | 프로젝트에 하네스 문서의 위치 기준을 세운다 |
| `context` | 셋업이 만든 문서의 남은 칸을 저장소 스캔과 질문으로 채운다 |
| `plan` | 요청 하나를 작업으로 계획해 `docs/tasks/NNN-slug/plan.md`로 쓰고 그 파일만 커밋한다 |

## 설치

`<폴더>`는 이 레포를 받은 폴더의 경로다.

### Claude Code

```bash
claude plugin marketplace add <폴더>
claude plugin install plate@harness-plate
```

설치하지 않고 한 세션에서만 쓰려면 `claude --plugin-dir <폴더>/plugins/plate`로 시작한다. 스킬은 `/plate:setup`, `/plate:context`, `/plate:plan`으로 부른다.

### Codex

```bash
codex plugin marketplace add <폴더>
codex plugin add plate@harness-plate
```

스킬은 `$plate:setup`, `$plate:context`, `$plate:plan`으로 부른다. Codex는 설치할 때 플러그인을 복사해 두므로, 스킬이 바뀌면 `codex plugin add plate@harness-plate`를 다시 실행한다.

Codex에서의 확인은 2026-10-08에 멈춘 상태다. 그 뒤에 고친 스킬과 새로 더한 `plan` 스킬은 Codex에서 확인하지 않았고, 확인해 둔 것과 남은 것은 `docs/TOOLS.md`에 있다.
