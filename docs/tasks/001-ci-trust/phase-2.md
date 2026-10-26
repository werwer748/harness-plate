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
- [ ] review 잡에서 `anthropics/claude-code-action` 단계 앞에 `AGENTS.md`를 기준 브랜치(`origin/${{ github.base_ref }}`)의 것으로 되돌리는 단계가 생긴다. 기준 브랜치에 `AGENTS.md`가 없으면 PR의 것을 지운다 (`plugins/plate/skills/setup/SKILL.md`)
- [ ] review 단계가 실패하면(`if: failure()`) 액션의 실행 결과 파일에서 오류 줄(결과의 `is_error`와 오류 글)만 로그에 내는 단계가 생긴다. `show_full_output`은 켜지 않는다 (`plugins/plate/skills/setup/SKILL.md`)
- [ ] 양식 위의 설명이 두 단계를 적는다 (`plugins/plate/skills/setup/SKILL.md`)
- [ ] ADR-021의 이유 "PR 코드에 숨은 지시가 있어도 에이전트에게는 머지 권한이 없다"가 머지 권한만 막고 등급은 막지 않았다는 것과, 워크플로의 `AGENTS.md` 되돌림과 PR 모드의 규칙으로 막는다는 것이 트레이드오프에 적힌다. `CLAUDE.md`가 불러오는 다른 파일은 되돌리지 않는다는 남은 길도 적힌다 (`docs/ADR.md`)
- [ ] `docs/ARCHITECTURE.md`의 PR CI 문단과 데이터 흐름의 review 잡 줄이 되돌림 단계, 오류 줄 단계, PR 모드가 지침 파일을 기준 브랜치에서 읽는 것을 적고, 같은 문단의 "PR 코드에 숨은 지시가 있어도 에이전트에게는 머지 권한이 없다"가 바뀐 이유와 맞는다 (`docs/ARCHITECTURE.md`)

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
