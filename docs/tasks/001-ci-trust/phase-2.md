# Phase 2: 워크플로 양식의 되돌림과 오류 줄 단계

**목표**: setup의 워크플로 양식이 review 잡 전에 `AGENTS.md`를 기준 브랜치의 것으로 되돌리고 review 단계가 실패하면 오류 줄만 로그에 내며, ADR과 ARCHITECTURE가 바뀐 것을 적는다.

**테스트 먼저**: 아니오 — 워크플로 양식은 `.md`인 setup 본문 안에 있고, 실제 동작은 phase 3이 시험 저장소에서 본다

**읽을 것**
- `plugins/plate/skills/setup/SKILL.md`의 양식 절 `.github/workflows/plate-review.yml`과 그 위 설명
- https://raw.githubusercontent.com/anthropics/claude-code-action/main/action.yml (출력 `execution_file`, `structured_output`과 입력 `show_full_output`)
- `docs/TOOLS.md`의 "CI의 세 판정과 CI 있는 PR에서 본 것" (토큰이 폐기됐을 때 로그에 남은 글과 진단 PR에서 본 결과의 꼴)
- `docs/ADR.md`의 ADR-021
- `docs/ARCHITECTURE.md`의 패턴과 규칙에서 PR의 CI 문단, 데이터 흐름의 PR 부분

**TODO**
- [x] review 잡에서 `anthropics/claude-code-action` 단계 앞에 `AGENTS.md`를 기준 브랜치(`origin/${{ github.base_ref }}`)의 것으로 되돌리는 단계가 생긴다. 기준 브랜치에 `AGENTS.md`가 없으면 PR의 것을 지운다 (`plugins/plate/skills/setup/SKILL.md`)
- [x] review 단계가 실패하면(`if: failure()`) 액션의 실행 결과 파일에서 오류 줄(결과의 `is_error`와 오류 글)만 로그에 내는 단계가 생긴다. `show_full_output`은 켜지 않는다 (`plugins/plate/skills/setup/SKILL.md`)
- [x] 양식 위의 설명이 두 단계를 적는다 (`plugins/plate/skills/setup/SKILL.md`)
- [x] ADR-021의 이유 "PR 코드에 숨은 지시가 있어도 에이전트에게는 머지 권한이 없다"가 머지 권한만 막고 등급은 막지 않았다는 것과, 워크플로의 `AGENTS.md` 되돌림과 PR 모드의 규칙으로 막는다는 것이 트레이드오프에 적힌다. `CLAUDE.md`가 불러오는 다른 파일은 되돌리지 않는다는 남은 길도 적힌다 (`docs/ADR.md`)
- [x] `docs/ARCHITECTURE.md`의 PR CI 문단과 데이터 흐름의 review 잡 줄이 되돌림 단계, 오류 줄 단계, PR 모드가 지침 파일을 기준 브랜치에서 읽는 것을 적고, 같은 문단의 "PR 코드에 숨은 지시가 있어도 에이전트에게는 머지 권한이 없다"가 바뀐 이유와 맞는다 (`docs/ARCHITECTURE.md`)

**통과 조건**
- 완료 조건 1의 둘째, 셋째 확인이 참이다.
  - 확인: 양식 절의 워크플로에서 review 잡의 액션 단계보다 앞에 `AGENTS.md`를 되돌리는 단계가 있고, 그 단계에 기준 브랜치에 없을 때 지우는 것이 있다
  - 확인: `docs/ADR.md`의 ADR-021과 `docs/ARCHITECTURE.md`의 CI 문단을 따로 읽어, 둘 다 이 길과 막는 방법을 적는다
- 완료 조건 4의 첫 확인이 참이고 오류 줄 단계가 있다.
  - 확인: `grep -c show_full_output plugins/plate/skills/setup/SKILL.md`가 `0`
  - 확인: 양식 절의 워크플로에 `if: failure()`로 도는, 액션의 실행 결과에서 오류 줄을 내는 단계가 있다
- 양식의 YAML이 구문으로 읽힌다.
  - 확인: 양식 절의 `yaml` 코드 블록을 뽑아 `ruby -ryaml -e 'YAML.load_file(ARGV[0])' <뽑은 파일>`이 오류 없이 끝난다
- 테스트가 모두 통과한다.
  - 확인: `python3 -m unittest discover -s tests`가 `OK`

## 한 일
- review 잡의 액션 앞 `AGENTS.md` 되돌림 단계: `actions/checkout` 다음, `id: review` 앞에 "AGENTS.md를 기준 브랜치의 것으로 되돌린다" 단계를 넣었다. `BASE_REF`를 env로 받아 `git cat-file -e "origin/$BASE_REF:AGENTS.md"`가 참이면 `git checkout "origin/$BASE_REF" -- AGENTS.md`, 아니면 `rm -f AGENTS.md` (`plugins/plate/skills/setup/SKILL.md`)
- 실패 때 오류 줄 단계: review 단계 뒤에 `if: failure()`인 "review가 실패한 까닭을 낸다" 단계를 넣었다. `steps.review.outputs.execution_file`(비면 `$RUNNER_TEMP/claude-execution-output.json`, 액션의 `base-action/src/execution-file.ts`가 쓰는 곳)을 읽어 `type`이 `result`인 메시지의 `subtype`, `is_error`, `api_error_status`, `errors`와, `is_error`일 때만 `result` 글을 한 줄 JSON으로 낸다. 파일이 없으면 그 말만 낸다. `show_full_output`은 쓰지 않았다 (`plugins/plate/skills/setup/SKILL.md`)
- 양식 위 설명: 되돌림 단계(까닭: `@AGENTS.md`로 PR의 지시가 실림)와 오류 줄 단계(메시지 전부를 내는 입력을 켜지 않는 까닭)를 적었다 (`plugins/plate/skills/setup/SKILL.md`)
- ADR-021 트레이드오프: 머지 권한만 막고 등급은 막지 않았다는 것(#11), 워크플로의 되돌림과 PR 모드 규칙으로 막는다는 것, `CLAUDE.md`와 그것이 불러오는 `AGENTS.md` 밖의 파일은 되돌리지 않는 남은 길, 오류 줄 단계(#13)를 더했다 (`docs/ADR.md`)
- ARCHITECTURE: PR CI 문단에 되돌림 단계, PR 모드가 지침 파일을 기준 브랜치에서 읽는 것, 남은 길, 오류 줄 단계를 넣고 문단 끝 이유를 "머지 권한이 없는 것은 등급을 막지 않으므로 … 되돌림과 PR 모드의 규칙으로 막는다"로 바꿨다. 데이터 흐름의 review 잡 줄에도 같은 것을 적었다 (`docs/ARCHITECTURE.md`)

## 확인 결과
- 완료 조건 1의 둘째 확인: 양식의 액션 단계 앞 되돌림 단계와 없을 때 지우기
  - 양식 `yaml` 블록을 뽑아 `ruby -ryaml`로 review 잡 단계 순서를 냄 → `actions/checkout@v7`, `AGENTS.md를 기준 브랜치의 것으로 되돌린다`, `review | anthropics/claude-code-action@v1`, `review가 실패한 까닭을 낸다 | failure()`, `actions/upload-artifact@v7`. 되돌림 단계에 `else rm -f AGENTS.md`가 있다. 통과
- 완료 조건 1의 셋째 확인: ADR-021과 ARCHITECTURE CI 문단
  - `docs/ADR.md` ADR-021 트레이드오프를 읽음 → `AGENTS.md`의 지시가 `@AGENTS.md`로 실려 등급을 바꾸는 길과, 되돌림·PR 모드 규칙으로 막는 방법이 있다. 통과
  - `docs/ARCHITECTURE.md` 패턴과 규칙의 PR CI 문단을 읽음 → 같은 길(#11)과 막는 방법이 있다. 통과
- 완료 조건 4의 첫 확인
  - `grep -c show_full_output plugins/plate/skills/setup/SKILL.md` → `0`. 통과
- `if: failure()` 오류 줄 단계
  - 위 단계 순서 출력에 `review가 실패한 까닭을 낸다 | failure()`. 그 `run`을 뽑아 가짜 실행 결과 파일(`is_error: true`, `api_error_status: 401`)로 `RUNNER_TEMP=<scratchpad> bash err.sh` → `{"subtype": "success", "is_error": true, "api_error_status": 401, "result": "Failed to authenticate: OAuth token revoked."}`. 통과
- 양식의 YAML 구문
  - `awk`로 `yaml` 블록을 뽑아 `ruby -ryaml -e 'YAML.load_file(ARGV[0])' wf.yml` → 오류 없이 끝남(`RUBY_OK`). 통과
- 테스트
  - `python3 -m unittest discover -s tests` → `Ran 99 tests in 15.410s` / `OK`. 통과

## 계획과 달라진 점
- 없음

## 남은 것
- 없음. 실패 때 `steps.review.outputs.execution_file`이 실제로 채워지는지는 액션 소스만 읽어 알 수 없어 `$RUNNER_TEMP/claude-execution-output.json`을 대신 보게 했다. 실제 동작은 phase 3이 시험 저장소에서 본다

## 하네스에서 걸린 것
- 없음

## 확인 1

**통과 조건**
- 완료 조건 1의 둘째, 셋째 확인이 참이다.
  - `plugins/plate/skills/setup/SKILL.md` 299~403줄(양식 `yaml` 블록)을 뽑아 `ruby -ryaml`로 review 잡 단계 순서를 냄 → `actions/checkout@v7`, `AGENTS.md를 기준 브랜치의 것으로 되돌린다`, `anthropics/claude-code-action@v1`(id `review`), `review가 실패한 까닭을 낸다`(if `failure()`), `actions/upload-artifact@v7`. 되돌림 단계가 액션 앞에 있고 `git cat-file -e "origin/$BASE_REF:AGENTS.md"`가 거짓이면 `rm -f AGENTS.md`를 한다. 통과
  - `docs/ADR.md` ADR-021의 트레이드오프를 읽음 → PR이 `AGENTS.md`에 넣은 지시가 `@AGENTS.md`로 실려 등급을 바꾸는 길(#11)과, 워크플로의 되돌림(없으면 지움)·PR 모드 규칙으로 막는 방법, 남은 길이 있다. 통과
  - `docs/ARCHITECTURE.md` 51줄 PR CI 문단을 읽음 → 같은 길(#11)과 되돌림·PR 모드가 지침 파일을 기준 브랜치에서 읽는 것으로 막는다는 것, 문단 끝 이유가 "머지 권한이 없는 것은 등급을 막지 않으므로 … 막는다(ADR-021)"로 맞춰져 있다. 73줄 데이터 흐름 review 잡 줄에도 있다. 통과
- 완료 조건 4의 첫 확인이 참이고 오류 줄 단계가 있다.
  - `grep -c show_full_output plugins/plate/skills/setup/SKILL.md` → `0`. 통과
  - 양식 블록을 읽음 → `if: failure()`인 "review가 실패한 까닭을 낸다" 단계가 `steps.review.outputs.execution_file`(비면 `$RUNNER_TEMP/claude-execution-output.json`)에서 `type: result` 메시지의 `subtype`, `is_error`, `api_error_status`, `errors`, 오류일 때 `result`만 낸다. 통과
- 양식의 YAML이 구문으로 읽힌다.
  - `ruby -ryaml -e 'YAML.load_file(ARGV[0])' <scratchpad>/wf.yml` → 오류 없이 끝남(`RUBY_OK`). 통과
- 테스트가 모두 통과한다.
  - `python3 -m unittest discover -s tests` → `Ran 99 tests in 15.286s` / `OK`. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 99 tests` / `OK`. 통과

**실패**
- 없음

**하네스에서 걸린 것**
- 없음

**판정**: 통과
