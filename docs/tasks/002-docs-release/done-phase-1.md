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
- [x] 두 매니페스트의 `version`이 `0.15.0`으로 바뀌고, 설명의 스킬 나열에 cleanup 스킬(저장소를 여섯 기준으로 살펴 보고서를 쓰고 tasks로 만들지 묻는다)이 더해진다 (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)
- [x] README의 3줄 스킬 수가 열로, 스킬 표에 `cleanup` 행이, 105줄과 114줄의 부르는 이름에 `/plate:cleanup`과 `$plate:cleanup`이, 116줄의 목록에 `cleanup`이 더해진다 (`README.md`)
- [x] PRD 19줄의 "9단계에서 만든다"가 cleanup 스킬로 만들었다는 글로 바뀐다. 21줄은 그대로 둔다 (`docs/PRD.md`)
- [x] ARCHITECTURE의 디렉터리 구조에 `cleanup/SKILL.md` 줄이, 48줄의 스킬 목록에 cleanup이(수도 함께), 49줄의 "푸시하지 않는다" 스킬 목록에 cleanup이, 데이터 흐름에 사용자가 부르는 정리 점검의 흐름(여섯 에이전트 1라운드 → 교차 검토 2라운드 → `docs/cleanup/YYYY-MM-DD.md` → 묻기 → 동의하면 계획)이 더해진다 (`docs/ARCHITECTURE.md`)

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

## 한 일
- 두 매니페스트의 `version`이 `0.15.0`으로 바뀌고, 설명의 스킬 나열에 cleanup 스킬이 더해진다: 두 파일 모두 `version`을 `0.14.0`에서 `0.15.0`으로 바꾸고, 설명의 eval 스킬 뒤에 "저장소를 여섯 기준으로 살펴 정리 점검 보고서를 쓰고 발견을 tasks로 만들지 묻는 cleanup 스킬"을 더했다 (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)
- README: 3줄을 "스킬이 열 있다"로, 스킬 표 끝에 `cleanup` 행(여섯 기준, 교차 검토, `docs/cleanup/YYYY-MM-DD.md`, tasks로 만들지 묻고 동의하면 `plan`에 넘김, 코드를 고치지 않음, 사용자가 부름)을, 부르는 이름에 `/plate:cleanup`과 `$plate:cleanup`을, Codex에서 확인하지 않은 스킬 목록에 `cleanup`을 더했다. 표에 행이 하나 늘어 부르는 이름 줄은 106줄과 115줄, 목록 줄은 117줄이 됐다 (`README.md`)
- PRD 19줄: "9단계에서 만든다"를 cleanup 스킬의 동작 요약과 "cleanup 스킬로 만들었다"로 바꿨다. 21줄은 그대로다 (`docs/PRD.md`)
- ARCHITECTURE: 디렉터리 구조의 skills 끝에 `cleanup/SKILL.md` 줄(eval 줄의 `└──`를 `├──`로), 49줄(전 48줄)을 "여덟 스킬(plan, run, phase, check, retro, review, eval, cleanup)"로, 50줄(전 49줄)의 "푸시하지 않는다" 목록에 cleanup을, 데이터 흐름 블록 끝에 정리 점검 흐름(1라운드 → 2라운드 → 보고서와 문서 지도 행 커밋 → 묻기 → 동의하면 plan, 고르지 않은 것은 "미룸")을 더했다 (`docs/ARCHITECTURE.md`)

## 확인 결과
- 버전과 매니페스트 설명(완료 조건 1)
  - `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → `"version": "0.15.0",` 두 줄. 통과
  - `grep -c cleanup plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 파일 모두 `1`. 통과
  - `claude plugin validate . 2>&1 | tail -1` → `✔ Validation passed`. 통과
- 문서(완료 조건 2)
  - `README.md`, `docs/PRD.md`, `docs/ARCHITECTURE.md`를 문서마다 따로 읽음(스킬 수, 표, 부르는 이름, Codex 목록 / 9단계 줄 / 디렉터리 구조, 규칙 문단의 스킬 목록, 푸시 규칙 목록, 데이터 흐름), `grep -nE '아홉|여덟|일곱|9단계'`로 남은 수·목록도 훑음 → cleanup과 어긋나는 줄 없음. 통과
  - `grep -c 'plate:cleanup' README.md` → `2`. 통과
  - `grep -n '9단계까지 만든 뒤 1.0.0을 낸다' docs/PRD.md` → `21:9단계까지 만든 뒤 1.0.0을 낸다.` 한 줄. 통과
- 앞 task가 그대로이고 테스트가 통과한다(완료 조건 3)
  - `git diff --name-only $(git log -1 --format=%H -- docs/tasks/001-cleanup-skill/retro.md) HEAD -- plugins/plate/skills/cleanup/SKILL.md docs/TOOLS.md` → 출력 없음. 통과
  - `python3 -m unittest discover -s tests 2>&1 | tail -1` → `OK`. 통과

## 계획과 달라진 점
- 읽을 것과 TODO의 README 105·114·116줄, ARCHITECTURE 48·49줄은 실제로는 README 105·114·116줄(표에 행을 더한 뒤 106·115·117줄), ARCHITECTURE 디렉터리 구조에 줄을 더한 뒤 49·50줄이 됐다. 같은 줄을 고쳤고 줄 번호만 밀렸다

## 남은 것
- 마켓플레이스 목록(`.claude-plugin/marketplace.json`, `.agents/plugins/marketplace.json`)에는 버전 칸이 없어 고칠 것이 없었다(`grep -n 'version\|0.14'` 출력 없음)
- 커밋하지 않은 채 있던 `docs/tasks/RUNLOG.md`는 이 phase의 것이 아니라 커밋에 넣지 않았다

## 하네스에서 걸린 것
- 없음

## 확인 1

**통과 조건**
- 버전과 매니페스트 설명(완료 조건 1)
  - `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → `"version": "0.15.0",` 두 줄. 통과
  - `grep -c cleanup plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 파일 모두 `1`. 통과
  - `claude plugin validate . 2>&1 | tail -1` → `✔ Validation passed`. 통과
- 문서(완료 조건 2)
  - `README.md`, `docs/PRD.md`, `docs/ARCHITECTURE.md`를 문서마다 따로 읽음 → README: 3줄 "스킬이 열 있다"(skills 폴더 10개와 맞음), 16줄 `cleanup` 행, 106줄 `/plate:cleanup`, 115줄 `$plate:cleanup`, 117줄 Codex 목록에 `cleanup`. PRD: 19줄 9단계가 cleanup 스킬로 만들었다고 적고 동작 요약이 `cleanup/SKILL.md` description과 맞음. ARCHITECTURE: 32줄 `cleanup/SKILL.md`(31줄 eval이 `├──`), 49줄 "여덟 스킬(…, cleanup)"과 50줄 푸시 규칙 목록의 cleanup이 SKILL.md 14·18줄과 맞음, 79~84줄 정리 점검 흐름이 SKILL.md 0~6번(셋업 확인, 1·2라운드, 보고서와 문서 지도 행 커밋, 묻기, 미룸)과 맞음. 세 문서 모두 cleanup과 어긋나는 줄 없음. 통과
  - `grep -c 'plate:cleanup' README.md` → `2`. 통과
  - `grep -n '9단계까지 만든 뒤 1.0.0을 낸다' docs/PRD.md` → `21:9단계까지 만든 뒤 1.0.0을 낸다.` 한 줄. 통과
- 앞 task가 그대로이고 테스트가 통과한다(완료 조건 3)
  - `git diff --name-only $(git log -1 --format=%H -- docs/tasks/001-cleanup-skill/retro.md) HEAD -- plugins/plate/skills/cleanup/SKILL.md docs/TOOLS.md` → 출력 없음. 통과
  - `python3 -m unittest discover -s tests 2>&1 | tail -1` → `OK`(104개). 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 104 tests`, `OK`. 통과

**실패**
- 없음

**하네스에서 걸린 것**
- 없음

**판정**: 통과
