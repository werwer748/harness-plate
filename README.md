# harness-plate

레일 하네스 `plate`의 플러그인 레포다. 지금은 프로젝트에 하네스 문서의 위치 기준을 세우는 `setup` 스킬이 있다.

## 설치

`<폴더>`는 이 레포를 받은 폴더의 경로다.

### Claude Code

```bash
claude plugin marketplace add <폴더>
claude plugin install plate@harness-plate
```

설치하지 않고 한 세션에서만 쓰려면 `claude --plugin-dir <폴더>/plugins/plate`로 시작한다. 스킬은 `/plate:setup`으로 부른다.

### Codex

```bash
codex plugin marketplace add <폴더>
codex plugin add plate@harness-plate
```

스킬은 `$plate:setup`으로 부른다. Codex는 설치할 때 플러그인을 복사해 두므로, 스킬이 바뀌면 `codex plugin add plate@harness-plate`를 다시 실행한다.
