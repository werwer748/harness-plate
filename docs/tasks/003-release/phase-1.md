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
- [ ] 두 매니페스트의 `"version"`이 `0.14.0`으로 바뀐다 (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)
- [ ] README 표의 `setup` 행에 CI를 둘 때 CODEOWNERS를 쓰고 ruleset 거는 법을 알린다는 것이 더해진다 (`README.md`)
- [ ] README "CI 워크플로" 절에 세 가지가 더해진다. 판정 표의 자동 머지 조건에 워크플로를 바꾸지 않았다는 것, ruleset과 CODEOWNERS가 무엇을 막고 무엇을 막지 못하는지(PR을 연 계정이 유일한 코드 소유자일 때)와 닫는 법(setup의 4번과 같은 ruleset 꼴), 이미 워크플로를 둔 프로젝트가 할 세 가지(CODEOWNERS 두 줄, ruleset, verdict 단계의 `--changed-files`)다 (`README.md`)
- [ ] README "훅" 절의 편집 훅 설명에 아직 없는 `.github/CODEOWNERS`를 setup이 쓰는 것은 막지 않는다는 것이 더해진다 (`README.md`)
- [ ] `docs/PRD.md` 핵심 기능 8의 CI 판정 문장에 워크플로를 바꾼 PR은 판정이 머지 요청으로 내려 사람이 머지한다는 것이 더해진다 (`docs/PRD.md`)
- [ ] ADR-021의 트레이드오프에 #18의 길과 ADR-023이 그것을 어디까지 막는지 적은 줄이 더해진다 (`docs/ADR.md`)

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
