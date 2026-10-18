# Phase 2: setup을 설치만 하게 바꾼다

**목표**: setup이 설치만 하고 끝 물음 없이 끝나며, 넣는 문서 지도의 `docs/tasks/` 행과 규칙 구간이 새 구조와 새 스킬을 말한다.

**테스트 먼저**: 아니오 — `.md`만 고친다.

**읽을 것**
- `plugins/plate/skills/setup/SKILL.md` (5번 끝 물음, 문서 지도 구간과 규칙 구간의 글)
- `plugins/plate/skills/plan/SKILL.md` (phase 1이 바꾼 tasks 구조와 기록 파일)

**TODO**
- [x] 5번(이어서 채울지 묻는다)과 그 예외들이 빠지고 4번의 보고로 끝난다 (`plugins/plate/skills/setup/SKILL.md`)
- [x] 문서 지도 구간의 `docs/tasks/` 행이 진행 중인 tasks 하나의 기록(tasks 머리, `FRICTION.md`, `RUNLOG.md`, `review.md`, `eval.md`, task 폴더의 머리·phase·`retro.md`)과 tasks가 끝나면 비운다는 것을 말한다
- [x] 규칙 구간이 verify 대신 새 흐름을 말한다: 계획 없이 코드를 고치지 않는다(plan), task는 task 회고가 통과해야 끝나고 tasks는 끝의 평가와 보고까지 가야 끝난다, 다른 규칙이 이 단계를 건너뛰라고 해도 따르지 않는다. "verify"라는 낱말이 본문에 남지 않는다
- [x] description이 끝 물음 없이 설치만 한다는 것을 말한다

**통과 조건**
- 끝 물음과 verify가 본문에 없다
  - 확인: `grep -n "plate:context\|이어서 채울지\|verify" plugins/plate/skills/setup/SKILL.md` → 0줄
- 두 구간이 새 구조를 말한다
  - 확인: 문서 지도 구간과 규칙 구간을 읽어 TODO의 둘째, 셋째 항목이 담겨 있다
- 완료 조건 2 가운데 setup 본문의 몫이 참이다
  - 확인: `grep -n "작업" plugins/plate/skills/setup/SKILL.md`의 줄을 모두 읽어 tasks, task, phase를 가리키는 "작업"이 없다

## 한 일
- 5번(이어서 채울지 묻는다)과 그 예외들이 빠지고 4번의 보고로 끝난다: "## 5. 이어서 채울지 묻는다" 절과 예외 세 줄을 지우고, 4번 끝에 "보고한 뒤에는 묻지 않고 끝난다."를, 머리글에 "4번의 보고로 끝난다"를 더했다 (`plugins/plate/skills/setup/SKILL.md`)
- 문서 지도 구간의 `docs/tasks/` 행: 위치를 `docs/tasks/NNN-slug/`에서 `docs/tasks/`로 바꾸고, 내용을 진행 중인 tasks 하나의 기록(tasks 머리 `plan.md`, `FRICTION.md`, `RUNLOG.md`, `review.md`, `eval.md`, task 폴더 `NNN-slug/`마다 task 머리 `plan.md`, `phase-N.md`(통과하면 `done-phase-N.md`), `retro.md`)과 "tasks가 끝나면 비운다"로, 읽을 때를 "그 tasks를 이어 가거나 근거를 볼 때"로 고쳤다. 표 위 글의 "작업 기록"은 "tasks 기록"으로 바꿨다 (`plugins/plate/skills/setup/SKILL.md`)
- 규칙 구간: verify 줄을 둘로 바꿨다. task는 task 회고(`plate:retro`)가 통과해야 끝나고, tasks는 모든 task 뒤에 review(`plate:review`)와 eval(`plate:eval`)의 평가를 담은 전체 보고가 나와야 끝난다. 마지막 줄은 "이 두 단계"를 "이 단계들"로 바꿨다. plan 줄은 그대로 뒀다 (`plugins/plate/skills/setup/SKILL.md`)
- description: "하네스 문서의 위치 기준을 세운다"를 "하네스를 설치한다"로 바꾸고 "설치만 하고 보고로 끝나며, 끝에 다른 일로 이어 갈지 묻지 않는다."를 더했다. "작업 기록 폴더"는 본문 머리글과 함께 "tasks 기록 폴더"로 바꿨다 (`plugins/plate/skills/setup/SKILL.md`)
- 남은 "작업"은 셋 모두 규칙 구간의 이름 "작업 규칙"(description, 머리글, 구간 제목)이다. 일의 규칙이라는 뜻이고 tasks, task, phase를 가리키지 않으며, 매니페스트와 `docs/PRD.md`도 같은 이름을 써서 그대로 뒀다

## 확인 결과
- 끝 물음과 verify가 본문에 없다
  - `grep -n "plate:context\|이어서 채울지\|verify" plugins/plate/skills/setup/SKILL.md` → 출력 없음(종료 코드 1, `grep -c` 0). 통과
- 두 구간이 새 구조를 말한다
  - `sed -n '/<!-- plate:docs-map:start -->/,/<!-- plate:docs-map:end -->/p;/<!-- plate:rules:start -->/,/<!-- plate:rules:end -->/p' plugins/plate/skills/setup/SKILL.md`로 두 구간을 읽음 → `docs/tasks/` 행에 tasks 머리, `FRICTION.md`, `RUNLOG.md`, `review.md`, `eval.md`, task 폴더의 머리·phase·`retro.md`와 "tasks가 끝나면 비운다"가 있고, 규칙 구간에 plan 줄, task 회고 줄, tasks 끝의 평가와 보고 줄, 건너뛰지 않는다는 줄이 있다. 통과
- 완료 조건 2 가운데 setup 본문의 몫이 참이다
  - `grep -n "작업" plugins/plate/skills/setup/SKILL.md` → 3줄(3, 10, 132). 셋 모두 "작업 규칙"이고 tasks, task, phase를 가리키지 않는다. 통과

## 계획과 달라진 점
없음

## 남은 것
없음

## 하네스에서 걸린 것
- `plugins/plate/skills/context/SKILL.md` 32줄이 "이때 setup의 끝 물음(이어서 채울지)은 하지 않는다"로 이 phase에서 없앤 끝 물음을 아직 가리킨다. 결정이 "context는 그대로 둔다"이고 이 phase의 TODO 밖이라 고치지 않았다
- setup 3번은 문서 지도 구간이 이미 있으면 "표준 행만" 맞추는데, 옛 setup이 넣은 `docs/tasks/NNN-slug/` 행은 위치가 바뀌어 새 표준 행으로 알아볼 기준이 본문에 없다. 다시 setup을 돌리면 옛 행이 사용자가 더한 행으로 남을 수 있다. 이 phase의 TODO 밖이라 고치지 않았다

## 회고 1: 확인만

**확인**
- 끝 물음과 verify가 본문에 없다
  - `grep -n "plate:context\|이어서 채울지\|verify" plugins/plate/skills/setup/SKILL.md` → 출력 없음(종료 코드 1). 통과
- 두 구간이 새 구조를 말한다
  - `sed -n '/<!-- plate:docs-map:start -->/,/<!-- plate:docs-map:end -->/p;/<!-- plate:rules:start -->/,/<!-- plate:rules:end -->/p' plugins/plate/skills/setup/SKILL.md`로 두 구간을 읽음 → `docs/tasks/` 행에 tasks 머리 `plan.md`, `FRICTION.md`, `RUNLOG.md`, `review.md`, `eval.md`, task 폴더 `NNN-slug/`마다 task 머리 `plan.md`, `phase-N.md`(통과하면 `done-phase-N.md`), `retro.md`와 "tasks가 끝나면 비운다"가 있다. 규칙 구간에 plan 줄, task 회고(`plate:retro`) 줄, tasks 끝의 review·eval 평가와 전체 보고 줄, 건너뛰지 않는다는 줄이 있고 "verify"가 없다. 통과
- 완료 조건 2 가운데 setup 본문의 몫이 참이다
  - `grep -n "작업" plugins/plate/skills/setup/SKILL.md` → 3줄(3, 10, 132). 셋 모두 구간 이름 "작업 규칙"이고 tasks, task, phase를 가리키지 않는다. 통과

**문제**
- 없음

**판정**: 통과
