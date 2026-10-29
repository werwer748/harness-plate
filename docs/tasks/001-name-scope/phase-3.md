# Phase 3: run이 고칠 쪽이 계획인 회고의 문제에서 멈추고 맥락 문서가 맞는다

**목표**: run 8번과 "멈춘다"가 고칠 쪽이 "계획"인 회고의 문제에서 고칠 phase를 더하지 않고 멈추고, PRD와 ARCHITECTURE가 바뀐 동작과 맞는다.

**테스트 먼저**: 아니오 — `.md`인 스킬 본문과 맥락 문서만 고치고, 테스트는 그 글을 지키는 시험이라 코드 파일의 동작을 바꾸지 않는다

**읽을 것**
- `plugins/plate/skills/run/SKILL.md` ("8. 고칠 phase를 더한다"의 첫 문단, "멈춘다"의 목록, "2. 실행 방식을 정한다"의 tasks 일괄 줄, `RUNLOG.md`의 `멈춤` 설명 줄)
- `tests/test_skill_rules.py` (`RunRulesTest`에서 `목표나 완료 조건을 바꾸거나 좁혀야 하는지 본다`를 보는 시험)
- `docs/PRD.md` (핵심 기능 7)
- `docs/ARCHITECTURE.md` (패턴과 규칙의 run 문단 가운데 "회고의 문제를 고치려면…" 대목, 데이터 흐름의 실행의 "회고의 문제는 고칠 phase를 더해 고친다" 줄, 데이터 흐름 아래의 멈춤 문단, 디렉터리 구조의 `test_skill_rules.py` 줄)
- `README.md` (`run` 행)
- `docs/ADR.md`, `docs/TOOLS.md`, `docs/BACKLOG.md`

**TODO**
- [x] 8번 첫 문단과 "멈춘다"의 계획이 틀린 자리 목록에, 마지막 회고 절에 고칠 쪽이 "계획"인 문제가 있으면 고칠 phase를 더하지 않고 실행 방식과 상관없이 멈춘다는 글이 더해진다. 2번의 tasks 일괄 줄도 맞춘다 (`plugins/plate/skills/run/SKILL.md`)
- [x] 그 글을 지키는 시험 `RunRulesTest.test_80_plan_side_problem_stops`가 더해진다. 이 시험은 8번과 "멈춘다"에 `고칠 쪽`과 `계획`이 든 글이 있는지 본다 (`tests/test_skill_rules.py`)
- [x] PRD 핵심 기능 7의 "계획이 틀림" 괄호, ARCHITECTURE의 run 문단, 데이터 흐름의 실행 줄, 멈춤 문단이 고칠 쪽이 계획인 회고의 문제를 든다. 디렉터리 구조의 `test_skill_rules.py` 줄에 이 규칙이 더해진다. README의 `run` 행이 멈추는 자리를 적으면 그것도 맞춘다 (`docs/PRD.md`, `docs/ARCHITECTURE.md`, `README.md`)

**통과 조건**
- 완료 조건 4가 참이다.
  - 확인: `grep -n '고칠 쪽' plugins/plate/skills/run/SKILL.md` → 8번과 "멈춘다"에 저마다 한 줄 이상
  - 확인: `cp -R` 사본에서 `sed -i '' '/고칠 쪽/d' plugins/plate/skills/run/SKILL.md` 뒤 `python3 -m unittest tests.test_skill_rules.RunRulesTest.test_80_plan_side_problem_stops` → `FAILED`
- 완료 조건 5가 참이다.
  - 확인: `grep -n '고칠 쪽' docs/PRD.md docs/ARCHITECTURE.md` → PRD 핵심 기능 7, ARCHITECTURE의 run 문단, 데이터 흐름의 실행, 멈춤 문단에 저마다 한 줄 이상
  - 확인: `grep -n -F 'test_skill_rules.py' docs/ARCHITECTURE.md` → 그 줄에 `합쳐지지 않은 다른 브랜치`, `task 머리를 마지막으로 더한 커밋`, `고칠 쪽이 계획`이 있다
- 완료 조건 3의 retro 본문이 그대로다.
  - 확인: `git diff --name-only HEAD -- plugins/plate/skills/retro/SKILL.md` → 아무것도 나오지 않는다
- 테스트 묶음이 모두 통과한다.
  - 확인: `python3 -m unittest discover -s tests` → 마지막 줄이 `OK`

## 한 일
- 8번 첫 문단과 "멈춘다"의 계획이 틀린 자리 목록, 2번의 tasks 일괄 줄: 8번 첫 문단에 `회고가 "고칠 쪽: 계획"으로 적은 문제(결정이나 완료 조건이 정한 동작이 목표를 해친다)도 계획을 바꾸게 하는 문제다`를 더해 고칠 phase를 더하지 않고 실행 방식과 상관없이 "멈춘다"로 가게 했다. "멈춘다" 목록의 계획 줄에 `마지막 회고 절에 고칠 쪽이 "계획"인 문제가 있을 때도 든다(8번)`, 2번 tasks 일괄 줄에 `회고가 고칠 쪽을 "계획"으로 적은 문제가 있으면 더하지 않고 멈춘다`를 더했다. `RUNLOG.md` 절의 물은 자리 줄에도 `멈춤`에 고칠 쪽이 계획인 문제가 든다고 더했다 (`plugins/plate/skills/run/SKILL.md`)
- 시험 `RunRulesTest.test_80_plan_side_problem_stops`: 8번, "멈춘다", 2번에 위 글이 있는지 본다 (`tests/test_skill_rules.py`)
- 맥락 문서와 README: PRD 핵심 기능 7의 "계획이 틀림" 괄호, ARCHITECTURE의 run 문단(55행), 데이터 흐름의 실행 줄(75행), 멈춤 문단(101행)에 고칠 쪽이 계획인 회고의 문제를 더했다. 디렉터리 구조의 `test_skill_rules.py` 줄에 run의 이 규칙을 더했다. README의 `run` 행이 멈추는 자리를 적어 같은 글을 더했다 (`docs/PRD.md`, `docs/ARCHITECTURE.md`, `README.md`)

## 확인 결과
- 완료 조건 4가 참이다.
  - `grep -n '고칠 쪽' plugins/plate/skills/run/SKILL.md` → 108(2번), 209(8번), 298("멈춘다"), 593(`RUNLOG.md` 절)행. 8번과 "멈춘다"에 저마다 한 줄. 통과
  - `cp -R` 사본(`mktemp -d` 아래)에서 `sed -i '' '/고칠 쪽/d' plugins/plate/skills/run/SKILL.md` 뒤 `python3 -m unittest tests.test_skill_rules.RunRulesTest.test_80_plan_side_problem_stops` → `FAILED (failures=1)`. 통과
- 완료 조건 5가 참이다.
  - `grep -n '고칠 쪽' docs/PRD.md docs/ARCHITECTURE.md` → PRD 17행(핵심 기능 7), ARCHITECTURE 40, 55(run 문단), 75(데이터 흐름의 실행), 101(멈춤 문단)행. 통과
  - `grep -n -F 'test_skill_rules.py' docs/ARCHITECTURE.md` → 40행 한 줄. 그 줄을 `grep -c -F`로 `합쳐지지 않은 다른 브랜치`, `task 머리를 마지막으로 더한 커밋`, `고칠 쪽이 계획` 저마다 → 1, 1, 1. 통과
- 완료 조건 3의 retro 본문이 그대로다.
  - `git diff --name-only HEAD -- plugins/plate/skills/retro/SKILL.md` → 출력 없음. 통과
- 테스트 묶음이 모두 통과한다.
  - `python3 -m unittest discover -s tests` → `Ran 275 tests` … 마지막 줄 `OK`. 통과

## 계획과 달라진 점
- 없음

## 남은 것
- `docs/ADR.md`에는 run의 멈춤 자리를 적은 결정이 없어(`grep -n '고칠 쪽\|고칠 phase' docs/ADR.md` 결과 없음) 고치지 않았다.

## 하네스에서 걸린 것
- 없음

## 확인 1

**통과 조건**
- 완료 조건 4가 참이다.
  - `grep -n '고칠 쪽' plugins/plate/skills/run/SKILL.md` → 108(2번), 209(8번 첫 문단), 298("멈춘다" 목록), 593(`RUNLOG.md` 절)행. 8번과 "멈춘다"에 저마다 한 줄. 통과
  - `mktemp -d` 아래 `cp -R` 사본에서 `sed -i '' '/고칠 쪽/d' plugins/plate/skills/run/SKILL.md` 뒤 `python3 -m unittest tests.test_skill_rules.RunRulesTest.test_80_plan_side_problem_stops` → `FAILED (failures=1)`. 통과
- 완료 조건 5가 참이다.
  - `grep -n '고칠 쪽' docs/PRD.md docs/ARCHITECTURE.md` → PRD 17행(핵심 기능 7), ARCHITECTURE 40행(디렉터리 구조), 55행(패턴과 규칙의 run 문단), 75행(데이터 흐름의 실행 "회고의 문제는 고칠 phase를 더해 고친다" 줄), 101행(데이터 흐름 아래 멈춤 문단). 네 곳에 저마다 한 줄. 통과
  - `grep -n -F 'test_skill_rules.py' docs/ARCHITECTURE.md` → 40행(디렉터리 구조) 한 줄. 그 줄에서 `grep -c -F`로 `합쳐지지 않은 다른 브랜치`, `task 머리를 마지막으로 더한 커밋`, `고칠 쪽이 계획` → 1, 1, 1. 통과
- 완료 조건 3의 retro 본문이 그대로다.
  - `git diff --name-only HEAD -- plugins/plate/skills/retro/SKILL.md` → 출력 없음. 통과
- 테스트 묶음이 모두 통과한다.
  - `python3 -m unittest discover -s tests` → `Ran 275 tests`, 마지막 줄 `OK`. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 275 tests`, `OK`. 통과

**남은 것**
- 없음

**실패**
- 없음

**하네스에서 걸린 것**
- 없음

**판정**: 통과
