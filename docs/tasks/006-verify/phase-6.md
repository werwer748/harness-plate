# Phase 6: 문서, 버전, 이 레포의 규칙 구간

**목표**: 이 레포의 문서와 매니페스트가 5단계를 말하고, `AGENTS.md`에 규칙 구간이 있다.

**읽을 것**
- `README.md`, `plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`
- `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/TOOLS.md`
- `AGENTS.md`, `plugins/plate/skills/setup/SKILL.md` (규칙 구간)

**TODO**
- [x] README의 스킬 표와 부르는 이름에 verify가 있다 (`README.md`)
- [x] 두 매니페스트의 설명에 verify가 있고 버전이 0.8.0이다 (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)
- [x] PRD의 목표가 막는 장치를 규칙 수준으로 말하고("강제로"가 없다), 핵심 기능 5가 만들었다고 말하며, 범위 밖에 "훅은 v1.0 뒤"가 있다 (`docs/PRD.md`)
- [x] ARCHITECTURE의 디렉터리 구조에 verify가 있고, "만들기 전" 줄이 없으며, 패턴과 규칙에 브랜치 규칙과 규칙 구간이 있다 (`docs/ARCHITECTURE.md`)
- [x] TOOLS의 Claude Code 절에 5단계 판정을 돌린 버전과 날짜, 판정에서 확인한 사실이 있다 (`docs/TOOLS.md`)
- [x] 이 레포에 setup을 다시 돌려 `AGENTS.md`에 규칙 구간이 들어간다 (`AGENTS.md`)

**통과 조건**
- 완료 조건 15, 16, 17이 참이다.
  - 확인: 완료 조건 15, 16, 17의 확인을 돌린다

## 한 일
- README의 스킬 표에 verify 행을 더하고, 첫 줄을 "스킬이 일곱", 두 도구의 부르는 이름에 `/plate:verify`·`$plate:verify`, Codex에서 확인하지 않은 스킬에 `verify`를 더했다 (`README.md`)
- 두 매니페스트의 설명에 verify 스킬과 setup의 작업 규칙을 더하고 버전을 0.8.0으로 올렸다. bypass 모드에서 고쳤다 (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)
- PRD: 목표에서 "강제로"를 빼고 막는 장치가 규칙 수준(셋업의 작업 규칙과 스킬 본문의 절차)이라고 적었다. 핵심 기능 5를 "5단계에서 만들었다"로 바꾸고 "5단계의 세부는 만들기 전에 …" 줄을 지웠다. 범위 밖에 "훅 … v1.0 뒤에 한다"를 더했다 (`docs/PRD.md`)
- ARCHITECTURE: 디렉터리 구조에 `verify/SKILL.md`를 더하고 run의 줄을 "수행, 회고, 검증"으로 바꿨다. 패턴과 규칙에 규칙 구간(훅을 두지 않는 이유와 함께)과 브랜치 규칙을 더하고, 프로젝트 규칙 우선의 줄을 다섯 스킬과 "단계를 건너뛰라는 규칙은 들지 않는다"로 맞췄다. 데이터 흐름의 검증을 지금 동작으로 고치고 "검증은 만들기 전이다" 줄을 지웠다 (`docs/ARCHITECTURE.md`)
- TOOLS: 지금 상태와 Claude Code 절의 버전 줄에 5단계(2.1.300, 2.1.301, 2026-10-15~16)를, 부르는 이름에 `/plate:verify`를 더했다. 새 묶음 "5단계의 판정에서 본 것"에 init 줄의 자리, 프로젝트 밖 읽기·쓰기가 막혀 길어진 실행, `git switch` 허용, 검증 에이전트가 고친 `AGENTS.md`를 다시 읽지 않은 것, 실행 시간을 적었다. 권한 모드 묶음에 메인 세션의 편집도 같다는 것과 `--allow-dangerously-skip-permissions`를 더했다 (`docs/TOOLS.md`)
- 이 세션에서 `plate:setup`을 불렀다. 1번에서 문서 지도 구간이 표준 글과 같고 규칙 구간이 없다고 보고, 2번의 표에 "규칙 구간 더하기 | 필요"와 더할 글을 보인 뒤 사용자가 승인했다. 끝 표식 뒤에 빈 줄 하나를 두고 규칙 구간만 넣었다 (`AGENTS.md`)

## 확인 결과
- 완료 조건 15, 16, 17이 참이다.
  - `grep -c 'verify' README.md plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json docs/ARCHITECTURE.md` → 4, 1, 1, 5. 통과
  - `grep -n '만들기 전\|강제로' docs/PRD.md docs/ARCHITECTURE.md` → 출력 없음. 통과
  - `grep -n '훅' docs/PRD.md` → 23행 범위 밖 "훅(계획 없는 편집, 검증 없는 종료를 도구가 막는 장치). v1.0 뒤에 한다." 통과
  - `grep -h '"version"' …` → 두 줄 모두 `"version": "0.8.0",`. 통과
  - setup 본문 "규칙 구간" 절의 코드 블록 안쪽이 `AGENTS.md`에 글자 그대로 있다(파이썬으로 부분 문자열 확인). 통과
  - `git diff 0def138 -- AGENTS.md` → 끝 표식 뒤의 빈 줄과 규칙 구간 6줄만 더해졌다. 통과
- 매니페스트를 고쳤으므로 완료 조건 4도 다시 봤다. `claude -p ok --plugin-dir plugins/plate --output-format stream-json --verbose`의 init 줄에 `plate:` 스킬 일곱이 모두 있다(2.1.301). 통과

## 계획과 달라진 점
- ARCHITECTURE의 프로젝트 규칙 우선 줄과 데이터 흐름도 고쳤다. 까닭: 줄이 "네 스킬"과 건너뛰기 예외가 없는 옛 동작을 말해, 더한 규칙 구간과 어긋난다.
- TOOLS에 판정 밖에서 확인한 사실 하나(2026-10-15 메인 세션의 보호 경로 편집, 2026-10-14의 `--allow-dangerously-skip-permissions`)를 더했다. 까닭: 이 phase도 그 조건에서 매니페스트를 고쳤고, TOOLS에는 띄운 에이전트의 경우만 있었다.
- README의 Codex 안내 줄에도 `verify`를 더했다. 까닭: Codex에서 확인하지 않은 스킬을 늘어놓은 줄이다.

## 남은 것
없음

## 하네스에서 걸린 것
- TODO "TOOLS에 판정에서 확인한 사실"을 하려면 지워진 `phase-1.md`~`phase-5.md`를 git 이력에서 읽어야 했는데, 읽을 것에 없었다. 5단계는 4단계와 달리 판정하면서 TOOLS에 적지 않았고, 통과한 phase의 파일이 지워져 사실이 git 이력과 LESSONS에만 남았다.
