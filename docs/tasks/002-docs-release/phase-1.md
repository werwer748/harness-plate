# Phase 1: 매니페스트와 문서

**목표**: 버전이 0.15.0이 되고, 매니페스트 설명·README·PRD·ARCHITECTURE가 cleanup 스킬을 담는다.

**테스트 먼저**: 아니오 — JSON 매니페스트의 글과 `.md`만 고치고 동작을 바꾸지 않는다

**읽을 것**
- `plugins/plate/skills/cleanup/SKILL.md` (앞머리의 description과 절차. 문서에 옮길 동작의 근거)
- `plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json` (버전과 스킬을 늘어놓은 설명)
- `README.md`의 3줄(스킬 수), 5~15줄(스킬 표), 105줄과 114줄(부르는 이름), 116줄(Codex에서 확인하지 않은 스킬 목록)
- `docs/PRD.md`의 19줄(9단계)
- `docs/ARCHITECTURE.md`의 22~31줄(디렉터리 구조의 skills), 48줄("일곱 스킬"), 49줄(스킬마다의 푸시 규칙 목록), 52~80줄(데이터 흐름)

**TODO**
- [ ] 두 매니페스트의 `version`이 `0.15.0`으로 바뀌고, 설명의 스킬 나열에 cleanup 스킬(저장소를 여섯 기준으로 살펴 보고서를 쓰고 tasks로 만들지 묻는다)이 더해진다 (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)
- [ ] README의 3줄 스킬 수가 열로, 스킬 표에 `cleanup` 행이, 105줄과 114줄의 부르는 이름에 `/plate:cleanup`과 `$plate:cleanup`이, 116줄의 목록에 `cleanup`이 더해진다 (`README.md`)
- [ ] PRD 19줄의 "9단계에서 만든다"가 cleanup 스킬로 만들었다는 글로 바뀐다. 21줄은 그대로 둔다 (`docs/PRD.md`)
- [ ] ARCHITECTURE의 디렉터리 구조에 `cleanup/SKILL.md` 줄이, 48줄의 스킬 목록에 cleanup이(수도 함께), 49줄의 "푸시하지 않는다" 스킬 목록에 cleanup이, 데이터 흐름에 사용자가 부르는 정리 점검의 흐름(여섯 에이전트 1라운드 → 교차 검토 2라운드 → `docs/cleanup/YYYY-MM-DD.md` → 묻기 → 동의하면 계획)이 더해진다 (`docs/ARCHITECTURE.md`)

**통과 조건**
- 버전과 매니페스트 설명(완료 조건 1)
  - 확인: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json`의 두 줄이 모두 `0.15.0`
  - 확인: `grep -c cleanup plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json`가 두 파일 모두 1 이상
  - 확인: `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
- 문서(완료 조건 2)
  - 확인: `README.md`, `docs/PRD.md`, `docs/ARCHITECTURE.md`를 문서마다 따로 읽어, 스킬 수·스킬 목록·부르는 이름·9단계의 상태·디렉터리 구조·규칙 문단의 스킬 목록에서 cleanup과 어긋나는 줄이 없다. 한 문서라도 있으면 실패
  - 확인: `grep -c 'plate:cleanup' README.md`가 2 이상
  - 확인: `grep -n '9단계까지 만든 뒤 1.0.0을 낸다' docs/PRD.md`가 한 줄을 낸다
- 앞 task가 그대로이고 테스트가 통과한다(완료 조건 3)
  - 확인: `git diff --name-only $(git log -1 --format=%H -- docs/tasks/001-cleanup-skill/retro.md) HEAD -- plugins/plate/skills/cleanup/SKILL.md docs/TOOLS.md`가 아무것도 내지 않는다
  - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
