# Phase 1: 버전과 문서

**목표**: 두 매니페스트가 0.13.0이 되고, 맥락 문서와 README의 어긋난 줄이 바뀐 동작에 맞게 고쳐진다.

**테스트 먼저**: 아니오 — 버전 값과 `.md`만 고친다. 테스트는 매니페스트를 읽지 않는다

**읽을 것**
- `plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json` (3줄 버전)
- `git diff main -- plugins/plate/skills/plan/SKILL.md plugins/plate/skills/run/SKILL.md plugins/plate/skills/review/SKILL.md` (이 tasks가 바꾼 스킬 본문)
- `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md` (맥락 문서)
- `README.md` (1~16줄 개요, 17줄 tasks 끝의 PR, 21줄 CI 워크플로)

**TODO**
- [x] 두 매니페스트의 `"version"` 값이 `0.12.0`에서 `0.13.0`으로 바뀐다 (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)
- [x] 맥락 문서 넷 가운데 바뀐 동작과 어긋나는 줄이 바뀐다. 문서마다 어긋난 줄이 없으면 고치지 않고 기록에 그렇다고 적는다 (`docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`)
- [x] README의 개요, tasks 끝의 PR, CI 워크플로 절 가운데 바뀐 동작과 어긋나는 줄이 바뀐다. 어긋난 줄이 없으면 고치지 않고 기록에 그렇다고 적는다 (`README.md`)

**통과 조건**
- 완료 조건 1이 참이다.
  - 확인: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json`의 두 줄이 모두 `"version": "0.13.0",`
- 완료 조건 2가 참이다.
  - 확인: `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
- 완료 조건 3이 참이다.
  - 확인: `python3 -m unittest discover -s tests`가 `OK`
- 완료 조건 4가 참이다.
  - 확인: `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `README.md`를 문서마다 따로 읽어, 이 tasks가 바꾼 동작(plan의 초안 전 점검, run이 넘기는 작업 트리 경로, review의 결과물인 마크다운과 그 줄을 커버리지·중복에서 빼는 것)과 어긋나는 줄이 없다. 한 문서라도 어긋나는 줄이 있으면 실패
- 완료 조건 5가 참이다.
  - 확인: `grep -n -A3 '^## 결과물인 마크다운' docs/ARCHITECTURE.md`가 그 절과 `plugins/plate/skills/*/SKILL.md` 경로를 낸다

## 한 일
- 두 매니페스트의 `"version"` 값이 `0.12.0`에서 `0.13.0`으로 바뀐다: 두 파일의 3줄을 `"version": "0.13.0",`으로 바꿨다 (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)
- 맥락 문서 넷 가운데 바뀐 동작과 어긋나는 줄이 바뀐다:
  - `docs/ARCHITECTURE.md`: 패턴과 규칙의 "스킬이 다른 스킬의 절차를 써야 하면 그 스킬을 이름으로 부른다" 줄이 run의 작업 트리의 스킬 줄과 어긋나, 그 줄 끝에 run의 예외(맡길 스킬의 `SKILL.md`를 tasks 커밋이 바꿨으면 저장소 안 경로를 읽으라는 줄을 붙인다)와 이유를 더했다. 결과물인 마크다운 절과 CI 판정 줄은 이미 맞았다 (`docs/ARCHITECTURE.md`)
  - `docs/TOOLS.md`: "세션 도중의 스킬 본문 고침"의 끝 줄 "스킬의 절차를 바꾸는 tasks는 … 다음 단계를 새 세션에서 이어 간다"가 run이 넘기는 작업 트리 경로와 어긋나, 0.13.0부터 run이 작업 트리의 스킬 줄을 붙인다는 것과 그 줄이 닿지 않는 곳(run 자신, plan)은 여전히 새 세션이나 `/reload-plugins`로 싣는다는 것으로 바꿨다 (`docs/TOOLS.md`)
  - `docs/PRD.md`: 어긋난 줄 없음. 고치지 않았다
  - `docs/ADR.md`: 어긋난 줄 없음(plan의 확인 명령, run의 맡기는 글, review의 `.md` 제외를 적은 줄이 없다). 고치지 않았다
- README의 개요, tasks 끝의 PR, CI 워크플로 절 가운데 바뀐 동작과 어긋나는 줄이 바뀐다: CI 워크플로 절 25줄의 "새 줄이 20줄 미만인 PR은 … 보지 않음"이 결과물인 마크다운의 줄을 빼고 센다는 동작과 어긋나, 결과물인 마크다운 절(평가에 넣되 커버리지·중복에서 뺀다, PR 모드는 기준 브랜치에서 읽는다)을 적고 "결과물인 마크다운의 줄을 뺀 새 줄이 20줄 미만"으로 바꿨다. 개요 표와 tasks 끝의 PR 절은 어긋난 줄이 없어 고치지 않았다 (`README.md`)

## 확인 결과
- 완료 조건 1이 참이다.
  - `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → `  "version": "0.13.0",` 두 줄. 통과
- 완료 조건 2가 참이다.
  - `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
- 완료 조건 3이 참이다.
  - `python3 -m unittest discover -s tests` → `Ran 99 tests in 15.671s` / `OK`. 통과
- 완료 조건 4가 참이다.
  - `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `README.md`를 문서마다 읽고 `grep -n -E '새 줄|20줄|이름으로|세션을 띄울|미리 돌려|확인 명령|\.md'`로 걸리는 줄을 다시 봤다 → 고친 세 줄 뒤로 plan의 초안 전 점검, run의 작업 트리 경로, 결과물인 마크다운과 커버리지·중복 제외와 어긋나는 줄이 없다. 통과
- 완료 조건 5가 참이다.
  - `grep -n -A3 '^## 결과물인 마크다운' docs/ARCHITECTURE.md` → `81:## 결과물인 마크다운`, `83-- \`plugins/plate/skills/*/SKILL.md\``. 통과

## 계획과 달라진 점
없음

## 남은 것
- 완료 조건 4는 문서를 읽어 판단한 것이라 어긋남의 기준이 읽는 쪽에 따라 다를 수 있다. `docs/TOOLS.md`의 52줄("다른 스킬의 본문은 그 스킬을 이름으로 불러야 받는다")과 168줄(Codex에서 다른 스킬은 경로가 아니라 이름으로 가리킨다)은 플러그인 설치 경로에 대한 사실이라 저장소 안 경로를 쓰는 run의 줄과 어긋나지 않는다고 보고 두었다.

## 하네스에서 걸린 것
없음
