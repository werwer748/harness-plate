# Phase 1: 공개와 0.11.0

**목표**: harness-plate가 공개 저장소가 되고, 두 매니페스트가 0.11.0이 되며, 맥락 문서와 README가 바뀐 동작과 공개 저장소를 적는다.

**테스트 먼저**: 아니오 — 문서(`.md`)와 매니페스트의 버전 줄만 고치고 동작은 바꾸지 않는다

**읽을 것**
- `README.md` (스킬 표, 설치)
- `docs/PRD.md` (목표, 핵심 기능 8), `docs/ARCHITECTURE.md` (기술 스택의 배포 줄, 디렉터리 구조, 패턴과 규칙, 데이터 흐름, 명령 절), `docs/ADR.md` (항목의 꼴, ADR-005)
- `plugins/plate/skills/run/SKILL.md`, `plugins/plate/skills/review/SKILL.md`, `plugins/plate/skills/setup/SKILL.md`, `plugins/plate/hooks/hooks.json` (이 tasks에서 바뀐 동작: tasks 끝의 PR, review의 PR 모드, setup의 CI 워크플로, 푸시 훅)
- `plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json` (버전)
- `.claude-plugin/marketplace.json` (마켓플레이스 목록)
- https://code.claude.com/docs/en/plugin-marketplaces (GitHub 저장소를 마켓플레이스로 더하는 꼴)

**TODO**
- [x] harness-plate 저장소가 공개가 된다 (GitHub의 `werwer748/harness-plate` 설정)
- [x] 두 매니페스트의 버전이 0.11.0이 된다 (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)
- [x] README가 tasks 끝의 PR, CI 워크플로와 그 판정, 푸시 훅을 적고, Claude Code 설치에 공개 저장소에서 받는 길이 생긴다 (`README.md`)
- [x] ARCHITECTURE의 배포 줄이 공개 저장소를 적고, PRD와 ARCHITECTURE에 옛 동작(GitHub 원격이 있어도 로컬로 합친다, 비공개 저장소)이 남지 않는다 (`docs/PRD.md`, `docs/ARCHITECTURE.md`)
- [x] ADR-022가 더해진다 (`docs/ADR.md`)

**통과 조건**
- 완료 조건 1, 2가 참이다.
  - 확인: 완료 조건 1, 2의 확인을 모두 돌린다
- 바꾼 뒤에도 기존 테스트가 모두 통과한다.
  - 확인: `python3 -m unittest discover -s tests`가 통과한다

## 한 일
- harness-plate 저장소가 공개가 된다: 바꾸기 전 `gh repo view werwer748/harness-plate --json visibility,defaultBranchRef`가 `PRIVATE main`이었고, `git log --all -p`에서 토큰·키 꼴(`sk-ant-`, `ghp_`, `github_pat_`, `gho_`, `AKIA`, `BEGIN … PRIVATE KEY`)을 찾아 아무것도 나오지 않은 것을 본 뒤 `gh repo edit werwer748/harness-plate --visibility public --accept-visibility-change-consequences`로 공개로 바꿨다 (GitHub의 `werwer748/harness-plate` 설정)
- 두 매니페스트의 버전이 0.11.0이 된다: `"version": "0.10.0"`을 `"0.11.0"`으로 바꿨다 (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)
- README가 tasks 끝의 PR, CI 워크플로와 그 판정, 푸시 훅을 적고, Claude Code 설치에 공개 저장소에서 받는 길이 생긴다: 스킬 표의 `setup`(CI 워크플로를 둘지 묻는다), `run`(PR을 열지, GitHub 원격이 없으면 합칠지 묻는다), `review`(CI가 PR 모드로 부른다) 행을 고치고, "tasks 끝의 PR", "CI 워크플로"(세 판정의 표와 시크릿 `CLAUDE_CODE_OAUTH_TOKEN`), "훅"(편집 훅과 푸시 훅) 절을 더했다. 설치 절에 공개 저장소라는 것을 적고 Claude Code의 첫 줄을 `claude plugin marketplace add werwer748/harness-plate`로 바꾸고, 받아 둔 폴더에서 더하는 길은 그 아래 글로 남겼다 (`README.md`)
- ARCHITECTURE의 배포 줄이 공개 저장소를 적고, PRD와 ARCHITECTURE에 옛 동작이 남지 않는다: 배포 줄의 "(비공개)"를 공개 저장소와 `claude plugin marketplace add werwer748/harness-plate`, CI 워크플로가 토큰 없이 여기서 받는다는 것(ADR-022)으로 바꿨다. "PR의 CI" 항목에 PR 모드가 명령 절의 설치를 먼저 돌린다는 것과 세 판정의 조건을 더했다. PRD 핵심 기능 8의 "PR과 CI는 011에서 만든다"를 "만들었다"로 바꿨다. GitHub 원격이 있어도 로컬로 합친다는 글은 두 문서에 이미 없었다(004-run-pr에서 고쳐짐) (`docs/ARCHITECTURE.md`, `docs/PRD.md`)
- ADR-022가 더해진다: "ADR-022: harness-plate는 공개 저장소로 배포한다"를 ADR-021 뒤에 더했다. 결정(공개 저장소, 설치 명령, CI가 토큰 없이 받는 곳, 시크릿을 넣지 않음, ADR-005와의 관계), 이유(ADR-021의 워크플로가 토큰 없이 받으려면 공개여야 한다), 트레이드오프(기록과 이력과 작성자 메일의 공개, 기본 브랜치의 변경이 곧바로 다른 프로젝트의 평가를 바꿈, 버전 고정 방식 없음)를 적었다 (`docs/ADR.md`)

## 확인 결과
- 완료 조건 1, 2가 참이다.
  - `gh repo view werwer748/harness-plate --json visibility -q .visibility` → `PUBLIC`. 통과
  - `GIT_TERMINAL_PROMPT=0 git -c credential.helper= ls-remote https://github.com/werwer748/harness-plate.git HEAD` → `d29c0144082039adc42cc5e07f65bbb499cd71be	HEAD` 한 줄, 종료 코드 0. 통과
  - `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
  - `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → `"version": "0.11.0",` 두 줄. 통과
  - `grep -c "^### ADR-022: " docs/ADR.md` → `1`. 통과
  - 네 문서를 읽음 → PR은 PRD 핵심 기능 8, ARCHITECTURE의 run 항목과 데이터 흐름, README의 "tasks 끝의 PR"에, CI 판정은 ARCHITECTURE의 "PR의 CI" 항목(세 조건), ADR-021, README의 판정 표에, 푸시 훅은 PRD 목표, ARCHITECTURE의 기술 스택·디렉터리 구조·막는 장치 항목, README의 "훅"에, 명령 절의 설치 줄은 ARCHITECTURE 명령 절의 `- 설치: 없음`과 "PR의 CI" 항목에, 공개 저장소는 ARCHITECTURE의 배포 줄, ADR-021, ADR-022, README의 설치 절에 있다. `grep -n -E "비공개|private|로컬로 합|PR과 CI는 011에서 만든다" docs/PRD.md docs/ARCHITECTURE.md docs/ADR.md README.md` → ADR-022의 "2026-10-24에 비공개에서 공개로 바꿨다" 한 줄만 나오고 옛 동작을 적은 줄은 없다. 통과
- 바꾼 뒤에도 기존 테스트가 모두 통과한다.
  - `python3 -m unittest discover -s tests` → `Ran 89 tests in 34.316s`, `OK`. 통과

## 계획과 달라진 점
- TODO의 ARCHITECTURE 항목은 배포 줄과 옛 동작만 적었지만, 완료 조건 2의 "CI 판정"과 "명령 절의 설치 줄"이 네 문서에 적혀 있도록 "PR의 CI" 항목에 세 판정의 조건과 PR 모드가 명령 절의 설치를 먼저 돌린다는 것을 더했다. README의 스킬 표에서 `setup` 행의 "설치만 하고 묻지 않고 끝난다"는 CI 워크플로를 묻는 지금 동작과 달라 함께 고쳤다.

## 남은 것
- TODO는 모두 끝냈다. 두 매니페스트의 `description`은 편집 훅만 적고 푸시 훅을 적지 않는다. 이 phase의 TODO 밖이라 고치지 않았다.

## 하네스에서 걸린 것
- 이 phase의 TODO "ADR-022가 더해진다"와 task 머리는 ADR-022가 무엇을 정하는지 적지 않았다. 읽을 것이 ADR-005(배포)를 가리키고 ADR-021의 트레이드오프가 "harness-plate가 공개여야 워크플로가 돈다(`005-publish-verify`에서 공개로 돌린다)"라고 적은 것으로 공개 저장소로 배포하는 결정이라고 보고 적었다. tasks 머리는 읽지 않았다. ADR-022의 "시크릿을 넣지 않는다"와 "작성자 메일은 그대로 두기로 했다"는 task 머리나 이 phase에 없고, 이 세션에 실린 사용자 메모리(011을 계획할 때 정한 것)에서 가져왔다.
