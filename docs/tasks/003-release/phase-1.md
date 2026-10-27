# Phase 1: 버전, README, 맥락 문서

**목표**: 버전이 0.14.0이 되고 README와 맥락 문서가 바뀐 동작과 맞는다.

**테스트 먼저**: 아니오 — 매니페스트의 버전과 `.md`만 고친다

**읽을 것**
- `plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json` (버전 줄)
- `README.md`의 표 `setup` 행(7줄), "CI 워크플로" 절, "훅" 절
- `docs/PRD.md` 핵심 기능 8 (PR과 CI의 판정)
- `docs/ADR.md`의 ADR-021 트레이드오프와 ADR-023
- `docs/TOOLS.md`에서 `001-ruleset-probe`가 더한 절 (ruleset JSON, 무엇이 막았는지)
- `plugins/plate/skills/setup/SKILL.md`의 4번 (ruleset 안내의 글)

**TODO**
- [x] 두 매니페스트의 `"version"`이 `0.14.0`으로 바뀐다 (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)
- [x] README 표의 `setup` 행에 CI를 둘 때 CODEOWNERS를 쓰고 ruleset 거는 법을 알린다는 것이 더해진다 (`README.md`)
- [x] README "CI 워크플로" 절에 세 가지가 더해진다. 판정 표의 자동 머지 조건에 워크플로를 바꾸지 않았다는 것, ruleset과 CODEOWNERS가 무엇을 막고 무엇을 막지 못하는지(PR을 연 계정이 유일한 코드 소유자일 때)와 닫는 법(setup의 4번과 같은 ruleset 꼴), 이미 워크플로를 둔 프로젝트가 할 세 가지(CODEOWNERS 두 줄, ruleset, verdict 단계의 `--changed-files`)다 (`README.md`)
- [x] README "훅" 절의 편집 훅 설명에 아직 없는 `.github/CODEOWNERS`를 setup이 쓰는 것은 막지 않는다는 것이 더해진다 (`README.md`)
- [x] `docs/PRD.md` 핵심 기능 8의 CI 판정 문장에 워크플로를 바꾼 PR은 판정이 머지 요청으로 내려 사람이 머지한다는 것이 더해진다 (`docs/PRD.md`)
- [x] ADR-021의 트레이드오프에 #18의 길과 ADR-023이 그것을 어디까지 막는지 적은 줄이 더해진다 (`docs/ADR.md`)

**통과 조건**
- (완료 조건 1) 버전, 마켓플레이스, 테스트
  - 확인: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json`의 두 줄이 모두 `0.14.0`
  - 확인: `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
  - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
- (완료 조건 2) README
  - 확인: `README.md`의 표 `setup` 행, "CI 워크플로" 절, "훅" 절을 하나씩 읽어 세 곳이 저마다 위 TODO의 것을 적는다
  - 확인: "CI 워크플로" 절에 이미 워크플로를 둔 프로젝트가 할 세 가지(CODEOWNERS 두 줄, ruleset, `--changed-files`)가 저마다 있다
- (완료 조건 3) 맥락 문서
  - 확인: `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `README.md`를 문서마다 따로 읽어, CODEOWNERS와 ruleset, 판정의 워크플로 검사, 편집 훅의 CODEOWNERS 예외와 어긋나는 줄이 없다

## 한 일
- 두 매니페스트의 `"version"`이 `0.14.0`으로 바뀐다: `0.13.0` → `0.14.0` (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)
- README 표의 `setup` 행: CI를 두면 `.github/CODEOWNERS`가 없을 때 쓰고(이미 있거나 login을 못 얻으면 넣을 줄을 알린다) 기본 브랜치에 ruleset 거는 법을 보고에 알린다는 문장을 더했다 (`README.md`)
- README "CI 워크플로" 절: 판정 표의 자동 머지 조건에 "PR이 워크플로(`.github/workflows/`로 시작하는 경로)를 바꾸지 않음"을 더하고 `--changed-files`로 본다는 문단을 더했다. 새 소절 "ruleset과 CODEOWNERS"에 #18의 길, 막는 것(코드 소유자가 아닌 계정이 연 워크플로 PR의 토큰 머지, 토큰의 기본 브랜치 직접 푸시), 막지 못하는 것(PR을 연 계정이 유일한 코드 소유자일 때), setup 4번과 같은 ruleset JSON의 `gh api` 명령과 화면에서 거는 법을 적었다. 새 소절 "이미 CI 워크플로를 둔 프로젝트"에 세 가지(CODEOWNERS 두 줄, ruleset, verdict 단계의 `--changed-files` 두 줄)를 번호로 적었다 (`README.md`)
- README "훅" 절: 편집 훅이 setup이 아직 없는 `plate-review.yml`과 `.github/CODEOWNERS`를 쓰는 것은 막지 않고, 이미 있는 두 파일의 편집은 막는다는 문장을 더했다 (`README.md`)
- `docs/PRD.md` 핵심 기능 8: 판정 문장 뒤에 "워크플로를 바꾼 PR은 판정이 머지 요청으로 내려 사람이 머지한다. setup은 CODEOWNERS를 쓰고 ruleset 거는 법을 알린다, ADR-023"을 괄호로 더했다 (`docs/PRD.md`)
- ADR-021 트레이드오프: 끝에 #18의 길(PR이 `plate-review.yml`을 고쳐 평가와 판정을 건너뜀)과 ADR-023이 막는 곳(판정 검사는 건너뛸 수 있음, ruleset·CODEOWNERS는 코드 소유자가 아닌 계정의 PR과 토큰 직접 푸시를 막음, 유일한 코드 소유자가 연 PR과 ruleset 없는 저장소는 남음)을 적은 줄을 더했다 (`docs/ADR.md`)

## 확인 결과
- (완료 조건 1) 버전, 마켓플레이스, 테스트
  - `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → `"version": "0.14.0",` 두 줄. 통과
  - `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
  - `python3 -m unittest discover -s tests` → `Ran 104 tests in 16.238s`, 마지막 줄 `OK`. 통과
- (완료 조건 2) README
  - `README.md`의 표 `setup` 행(CODEOWNERS 쓰기와 ruleset 안내), "CI 워크플로" 절(판정 표의 워크플로 조건, `--changed-files` 문단, "ruleset과 CODEOWNERS" 소절의 막는 것·막지 못하는 것·ruleset 꼴), "훅" 절(편집 훅의 `plate-review.yml`·CODEOWNERS 예외)을 하나씩 읽음 → 세 곳이 저마다 TODO의 것을 적는다. 통과
  - "이미 CI 워크플로를 둔 프로젝트" 소절을 읽음 → 1. CODEOWNERS 두 줄 넣기, 2. ruleset 걸기, 3. verdict 단계에 `--changed-files` 넘기기가 저마다 있다. 통과
- (완료 조건 3) 맥락 문서
  - `docs/PRD.md`(목표, 핵심 기능 8), `docs/ARCHITECTURE.md`(디렉터리 구조의 `verdict.py`·`setup/SKILL.md` 줄, 패턴과 규칙의 훅·CI 문단, 데이터 흐름), `docs/ADR.md`(ADR-021, ADR-023), `docs/TOOLS.md`(지금 상태, ruleset 절, CI 절), `README.md`를 따로 읽고 `grep -n '판정\|verdict\|edit_guard\|편집 훅\|CODEOWNERS\|ruleset'`으로 걸리는 줄을 봄 → CODEOWNERS와 ruleset, 판정의 워크플로 검사, 편집 훅의 CODEOWNERS 예외와 어긋나는 줄이 없다. 통과

## 계획과 달라진 점
- 없음

## 남은 것
- ADR-021의 이유 "판정의 세 규칙은 숫자와 등급만 보므로"는 그대로 두었다. 세 규칙 자체는 여전히 숫자와 등급만 보고 워크플로 검사는 그 위에서 자동 머지를 머지 요청으로 내리는 것이라 어긋나지 않는다고 보았고, 트레이드오프에 더한 줄이 ADR-023을 가리킨다
- `docs/ARCHITECTURE.md` 디렉터리 구조의 `edit_guard.py` 주석은 CODEOWNERS 예외를 적지 않지만 패턴과 규칙 문단이 적으므로 고치지 않았다(TODO에 없다)
- README의 "이미 CI 워크플로를 둔 프로젝트" 3번은 setup 양식의 verdict 단계와 같은 두 줄을 보이며, 양식이 바뀌면 README도 함께 맞춰야 한다

## 하네스에서 걸린 것
- 없음

## 확인 1

**통과 조건**
- (완료 조건 1) 버전, 마켓플레이스, 테스트
  - `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → `"version": "0.14.0",` 두 줄. 통과
  - `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
  - `python3 -m unittest discover -s tests` → `Ran 104 tests in 16.985s`, 마지막 줄 `OK`. 통과
- (완료 조건 2) README
  - `README.md` 7줄 표의 `setup` 행 → CI를 두면 `.github/CODEOWNERS`가 없을 때 쓰고(있거나 login을 못 얻으면 넣을 줄을 알림) 기본 브랜치에 ruleset 거는 법을 보고에 알린다고 적음. "CI 워크플로" 절 → 판정 표의 자동 머지 조건에 "PR이 워크플로(`.github/workflows/`로 시작하는 경로)를 바꾸지 않음", `--changed-files` 문단, "ruleset과 CODEOWNERS" 소절에 막는 것·막지 못하는 것(PR을 연 계정이 유일한 코드 소유자일 때)·`gh api` ruleset JSON과 화면에서 거는 법이 있음. "훅" 절(88줄) → 편집 훅이 아직 없는 `plate-review.yml`과 `.github/CODEOWNERS`를 setup이 쓰는 것은 막지 않고 이미 있는 두 파일의 편집은 막는다고 적음(`edit_guard.py` 25·214줄의 `SETUP_FILES`와 맞음). 통과
  - "이미 CI 워크플로를 둔 프로젝트" 소절 → 1. CODEOWNERS 두 줄 넣기, 2. ruleset 걸기, 3. verdict 단계에 `--changed-files` 넘기기가 저마다 있음. 통과
- (완료 조건 3) 맥락 문서
  - `docs/PRD.md` 핵심 기능 8(워크플로를 바꾼 PR은 머지 요청, setup의 CODEOWNERS와 ruleset 안내, ADR-023), `docs/ARCHITECTURE.md`(17·23줄 디렉터리 구조, 49줄 편집 훅의 CODEOWNERS 예외, 51줄 CI·CODEOWNERS·ruleset·`--changed-files`, 55·74줄 데이터 흐름), `docs/ADR.md`(ADR-021 트레이드오프의 #18 줄, ADR-023), `docs/TOOLS.md`(131줄부터의 ruleset과 CODEOWNERS 절), `README.md`를 따로 읽고 `판정|verdict|edit_guard|편집 훅|CODEOWNERS|ruleset|자동 머지`로 걸리는 줄을 봄. `verdict.py`의 `WORKFLOW_PREFIX`·`--changed-files` 처리와도 대어 봄 → 어긋나는 줄이 없음. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 104 tests`, `OK`. 통과

**실패**
- 없음

**하네스에서 걸린 것**
- 없음

**판정**: 통과
