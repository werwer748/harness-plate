# Phase 1: 버전, README, 맥락 문서

**목표**: 버전이 0.15.0이 되고 README와 맥락 문서가 바뀐 동작과 맞는다.

**테스트 먼저**: 아니오 — 매니페스트의 버전과 `.md`만 고친다

**읽을 것**
- `plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json` (버전 줄)
- `README.md` (표의 `plan`, `run`, `check`, `retro`, `review`, `eval` 행과 그 아래 절)
- `docs/PRD.md` (핵심 기능 3~8)
- `docs/ARCHITECTURE.md` ("패턴과 규칙", "데이터 흐름")
- `docs/ADR.md` (ADR-024)
- `docs/TOOLS.md` ("Claude Code" 절)
- `plugins/plate/skills/plan/SKILL.md`, `plugins/plate/skills/check/SKILL.md`, `plugins/plate/skills/retro/SKILL.md`, `plugins/plate/skills/run/SKILL.md`, `plugins/plate/skills/review/SKILL.md`, `plugins/plate/skills/eval/SKILL.md` (앞 task들이 고친 본문. 읽기만 한다)

**TODO**
- [x] 두 매니페스트의 `"version"`이 `0.15.0`으로 바뀐다 (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)
- [x] README의 표에서 `plan`, `run`, `check`, `retro`, `review`, `eval` 행과 그 아래 절 가운데 바뀐 여섯 동작과 어긋나는 글이 맞게 바뀐다. 어긋나는 글이 없으면 그대로 둔다 (`README.md`)
- [x] `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`에서 바뀐 여섯 동작과 어긋나는 줄이 맞게 바뀐다. 어긋나는 줄이 없으면 그대로 둔다 (`docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`)

**통과 조건**
- 완료 조건 1이 참이다.
  - 확인: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json`의 두 줄이 모두 `0.15.0`
  - 확인: `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
  - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
- 완료 조건 2가 참이다.
  - 확인: `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `README.md`를 문서마다 따로 읽어, 여섯 동작(plan의 줄 번호 규칙, plan의 돌려 보는 확인과 `돌리지 않음` 줄, check와 retro의 "남은 것" 판정, run의 로컬 기본 브랜치 물음과 로컬 merge-base, review의 결과물인 마크다운 테스트 적절성, eval의 정해 둔 물음) 가운데 어느 것과도 어긋나는 줄이 없다. 어긋나는 줄이 하나라도 있으면 실패

## 한 일
- 두 매니페스트의 `"version"`이 `0.15.0`으로 바뀐다: `0.14.0`을 `0.15.0`으로 바꿨다 (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)
- README의 표에서 `plan`, `run`, `check`, `retro`, `review`, `eval` 행과 그 아래 절 가운데 바뀐 여섯 동작과 어긋나는 글이 맞게 바뀐다: 여섯 동작을 고친 스킬 본문(plan의 "줄 번호"·"돌리지 않음" 규칙, check 5절과 retro 4번의 "남은 것", run 시작의 로컬 기본 브랜치 물음과 작업 트리의 스킬 줄의 merge-base, review 테스트 적절성의 결과물인 마크다운 표, eval의 "정해 둔 물음" 낱말)에 대어 읽었다. `run` 행은 로컬 기본 브랜치를 되돌릴지 묻는 것을 이미 적고 있고, 다른 행과 "tasks 끝의 PR", "CI 워크플로", "훅" 절에는 여섯 동작과 어긋나는 글이 없어 그대로 뒀다. "이미 CI 워크플로를 둔 프로젝트"의 `0.14.0 전에`는 지난 버전을 가리키는 글이라 그대로 뒀다 (`README.md` 바꾸지 않음)
- `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`에서 바뀐 여섯 동작과 어긋나는 줄이 맞게 바뀐다: 문서마다 읽었다. ARCHITECTURE의 run 규칙 줄과 데이터 흐름은 로컬 기본 브랜치 물음을 이미 적고, 작업 트리의 스킬 줄은 갈라진 곳을 따로 적지 않아 어긋나지 않는다. ADR-024의 트레이드오프는 결과물인 마크다운뿐인 tasks의 테스트 적절성을 완료 조건으로 매긴다고 이미 적는다. PRD 핵심 기능 3~8은 여섯 동작의 세부를 적지 않아 어긋나는 줄이 없다. TOOLS "Claude Code" 절의 `ci-run` 줄("tasks 끝의 코드 평가는 갈라진 곳을 로컬 `main` 기준으로 셌다")은 2026-10-24에 본 사실이고 지금 동작(로컬 기본 브랜치의 merge-base)과도 맞는다. 어긋나는 줄이 없어 그대로 뒀다 (네 문서 바꾸지 않음)

## 확인 결과
- 완료 조건 1이 참이다.
  - `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → `"version": "0.15.0",` 두 줄. 통과
  - `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
  - `python3 -m unittest discover -s tests` → `Ran 104 tests in 17.253s`, 마지막 줄 `OK`. 통과
- 완료 조건 2가 참이다.
  - `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `README.md`를 문서마다 읽고, `grep -n '줄 번호\|돌리지 않음\|남은 것\|merge-base\|로컬 기본\|테스트 적절성\|정해 둔 물음\|물은 자리'`로 여섯 동작에 걸리는 줄을 다시 찾아 스킬 본문과 견줬다 → 어긋나는 줄 없음. 통과

## 계획과 달라진 점
- 없음

## 남은 것
- README와 맥락 문서는 여섯 동작 가운데 넷(plan의 줄 번호 규칙과 돌려 보는 확인, check와 retro의 "남은 것" 판정, eval의 정해 둔 물음)과 run의 갈라진 곳이 로컬 merge-base라는 것을 따로 적지 않는다. 어긋나지 않아 TODO대로 더하지 않았다. 문서가 이 동작들을 설명해야 하는지는 이 phase에서 정하지 않았다

## 하네스에서 걸린 것
- 없음

## 확인 1

**통과 조건**
- 완료 조건 1이 참이다.
  - `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → `"version": "0.15.0",` 두 줄. 통과
  - `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
  - `python3 -m unittest discover -s tests` → `Ran 104 tests in 17.414s`, 마지막 줄 `OK`. 통과
- 완료 조건 2가 참이다.
  - `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `README.md`를 문서마다 읽고 여섯 동작에 걸리는 줄을 스킬 본문(run의 "작업 트리의 스킬 줄" 낱말과 시작 단계, eval의 "정해 둔 물음" 낱말, review의 테스트 적절성 행)에 견줬다 → ARCHITECTURE의 run 규칙 줄과 데이터 흐름, README의 `run` 행은 run 본문의 로컬 기본 브랜치 물음(모두 tasks 브랜치에 있으면 묻고, 없는 커밋이 있으면 묻지 않고 그대로 둔다)과 같다. ADR-024 트레이드오프의 결과물인 마크다운뿐인 tasks의 테스트 적절성은 review 본문과 같다. TOOLS "Claude Code" 절의 "기본 브랜치에서 갈라진 곳부터"는 origin과 로컬을 가리지 않아 로컬 merge-base와 어긋나지 않고, `ci-run` 줄의 "로컬 `main` 기준"은 2026-10-24에 본 사실이다. ARCHITECTURE 데이터 흐름의 "물은 자리마다 RUNLOG.md에 한 줄"은 eval의 정해 둔 물음과 어긋나지 않는다. PRD 핵심 기능 3~8과 README의 `plan`, `check`, `retro`, `review`, `eval` 행은 여섯 동작의 세부를 적지 않아 어긋나는 줄이 없다. 어긋나는 줄 없음. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 104 tests`, `OK`. 통과

**남은 것**
- 없음

**실패**
- 없음

**하네스에서 걸린 것**
- 없음

**판정**: 통과
