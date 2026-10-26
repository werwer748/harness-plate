# Phase 1: retro의 고칠 쪽, 경계, 남은 것

**목표**: retro가 어긋남의 고칠 쪽을 적고, 경계 밖의 꼴을 `FRICTION.md`의 `경계 밖` 줄로 돌리고, `done-phase-N.md`의 "남은 것"을 점검에 대어 본다.

**테스트 먼저**: 아니오 — `.md`만 고친다

**읽을 것**
- `plugins/plate/skills/retro/SKILL.md` 전체
- `plugins/plate/skills/eval/SKILL.md`의 낱말 "`FRICTION.md`"와 `FRICTION.md`의 줄을 읽는 곳
- `git show c2a983c^:docs/tasks/003-push-guard/retro.md` (회고 1~6이 시험 밖 꼴을 결함으로 찾은 곳, 회고 5가 "한 일"의 부작용을 늦게 찾은 곳)
- `git show c2a983c^:docs/tasks/002-ci-workflow/retro.md` (고칠 쪽을 적지 않아 같은 예외를 두 번 오간 곳)
- `git show c2a983c^:docs/tasks/FRICTION.md` (11, 13, 19, 21, 23, 24, 26, 33줄)
- `docs/ARCHITECTURE.md`의 푸시 훅 문단 (맥락 문서가 약속하는 꼴의 경계를 정한 예)

**TODO**
- [x] 4번에 생긴다. 문서와 코드(또는 계획과 코드)의 어긋남을 문제로 적을 때, task 머리와 tasks 머리의 목표와 결정에 비춰 어느 쪽을 고칠지와 그 근거를 적는다. 목표와 결정으로 가를 수 없으면 "고칠 쪽: 정하지 못함"과 까닭을 적는다 (`plugins/plate/skills/retro/SKILL.md`)
- [x] 회고 절 양식의 "문제" 줄에 `고칠 쪽: {문서 | 코드 | 정하지 못함}`을 더하고, 적는 규칙에 어긋남이 아닌 문제에서는 이 칸을 적지 않는다고 적는다 (`plugins/plate/skills/retro/SKILL.md`)
- [x] 4번에 생긴다. tasks 머리나 task 머리의 결정, 맥락 문서가 약속하는 꼴의 경계를 정했으면 "결함"은 그 경계 안에서만 찾는다. 경계 밖에서 찾은 꼴은 문제로 적지 않고 5번에서 `경계 밖`으로 모은다 (`plugins/plate/skills/retro/SKILL.md`)
- [x] 5번의 갈래에 `경계 밖`(약속한 경계 밖에서 찾은 꼴과, 그 꼴을 약속에 넣을지 볼 까닭)을 더하고, `FRICTION.md` 줄 양식의 갈래를 `{문제 | 멈춤 | 스킬 후보 | 경계 밖}`으로 고친다 (`plugins/plate/skills/retro/SKILL.md`)
- [x] 4번에 생긴다. `done-phase-N.md`마다 "남은 것"에 적힌 부작용과 한계를 넷에 대어 보고, 걸리면 문제로 적는다 (`plugins/plate/skills/retro/SKILL.md`)
- [x] eval에서 `FRICTION.md`의 갈래를 늘어놓은 곳을 `경계 밖`이 든 넷으로 맞춘다. 등급 기준과 3번 표는 건드리지 않는다 (`plugins/plate/skills/eval/SKILL.md`)

**통과 조건**
- 완료 조건 1의 첫째 확인(retro 셋)이 참이다.
  - 확인: retro의 4번, 5번, 회고 절 양식, `FRICTION.md` 줄 양식, 적는 규칙을 읽어 셋을 하나씩 찾는다. 셋 모두 있어야 통과다
- 완료 조건 2가 참이다.
  - 확인: `grep -rn '스킬 후보' plugins/plate/skills docs/ARCHITECTURE.md`가 낸 줄을 하나씩 읽어, 넷을 늘어놓는 줄에는 모두 `경계 밖`이 있다
- 테스트가 모두 통과한다.
  - 확인: `python3 -m unittest discover -s tests`가 `OK`

## 한 일
- 4번의 고칠 쪽: 4번에 문서와 코드(또는 계획과 코드)의 어긋남을 문제로 적을 때 task 머리와 tasks 머리의 목표와 결정에 비춰 고칠 쪽(문서 | 코드)과 근거를 적고, 가를 수 없으면 "고칠 쪽: 정하지 못함"과 까닭을 적는 문단을 더했다 (`plugins/plate/skills/retro/SKILL.md`)
- 회고 절 양식의 "문제" 줄: `고칠 쪽: {문서 | 코드 | 정하지 못함} ({근거가 된 목표나 결정, 정하지 못했으면 그 까닭})`을 더하고, 적는 규칙에 어긋남이 아닌 문제에서는 이 칸을 적지 않는다는 줄을 더했다 (`plugins/plate/skills/retro/SKILL.md`)
- 4번의 경계: 결정이나 맥락 문서가 약속하는 꼴의 경계를 정했으면 "결함"은 경계 안에서만 찾고, 경계 밖의 꼴은 5번에서 `경계 밖`으로 모으는 문단을 더했다. 경계를 정한 곳이 없으면 "결함"으로 적는다는 문장도 넣었다(task 머리의 결정 둘째). 적는 규칙에도 경계 밖의 꼴은 `경계 밖` 줄로 적는다는 줄을 더했다 (`plugins/plate/skills/retro/SKILL.md`)
- 5번의 갈래와 `FRICTION.md` 줄 양식: 5번을 "네 갈래"로 고치고 `경계 밖` 갈래를 더했으며, 줄 양식의 갈래를 `{문제 | 멈춤 | 스킬 후보 | 경계 밖}`으로 고치고 뒤의 설명에 경계 밖의 꼴과 볼 까닭을 더했다 (`plugins/plate/skills/retro/SKILL.md`)
- 4번의 남은 것: `done-phase-N.md`마다 "남은 것"에 적힌 부작용과 한계를 넷에 대어 보고 걸리면 문제로 적는 문단을 더했다 (`plugins/plate/skills/retro/SKILL.md`)
- eval의 갈래 나열: 낱말 "`FRICTION.md`"의 줄 꼴을 `{문제 | 멈춤 | 스킬 후보 | 경계 밖}`으로 맞췄다. 등급 기준과 3번 표는 건드리지 않았다 (`plugins/plate/skills/eval/SKILL.md`)

## 확인 결과
- 완료 조건 1의 첫째 확인(retro 셋)이 참이다.
  - `grep -n '고칠 쪽\|경계 밖\|"남은 것"' plugins/plate/skills/retro/SKILL.md`로 찾아 읽음 → 고칠 쪽: 4번(73줄)과 회고 절 양식 "문제" 줄(145줄), 적는 규칙(166줄). 경계 밖: 4번(75줄), 5번(88줄), `FRICTION.md` 줄 양식(153줄), 적는 규칙(167줄). 남은 것: 4번(77줄). 셋 모두 있음. 통과
- 완료 조건 2가 참이다.
  - `grep -rn '스킬 후보' plugins/plate/skills docs/ARCHITECTURE.md` → 세 줄. retro 153줄과 eval 31줄은 넷을 늘어놓고 `경계 밖`이 있음. eval 161줄은 스킬 후보 줄 하나만 가리킴. 통과
- 테스트가 모두 통과한다.
  - `python3 -m unittest discover -s tests` → `Ran 99 tests in 16.533s`, `OK`. 통과

## 계획과 달라진 점
- retro의 description(3줄)에 적힌 tasks 끝에 볼 것의 나열 "(문제, 멈춤, 스킬로 만들 후보)"에도 `경계 밖`을 더했다. TODO에 따로 적히지 않았지만 같은 파일에서 5번의 갈래를 넷으로 늘리며 나열이 셋으로 남으면 어긋나기 때문이다

## 남은 것
- eval은 `FRICTION.md`의 `경계 밖` 줄을 2번의 실패 모으기 표에 넣지 않으므로 실패로 세지 않지만, `경계 밖` 줄을 따로 모으거나 보고에 싣는 규칙은 없다. 등급 기준과 3번 표는 `005-eval-rules`의 일이라 건드리지 않았다

## 하네스에서 걸린 것
- 없음

## 확인 1

**통과 조건**
- 완료 조건 1의 첫째 확인(retro 셋)이 참이다.
  - `plugins/plate/skills/retro/SKILL.md`의 4번, 5번, 회고 절 양식, `FRICTION.md` 줄 양식, 적는 규칙을 읽음 → 고칠 쪽: 4번(73줄)에 고칠 쪽(문서 | 코드)과 근거, "정하지 못함" 규칙이 있고 회고 절 양식 "문제" 줄(145줄)에 `고칠 쪽:` 칸이 있음. 경계 밖: 4번(75줄), 5번의 `경계 밖` 갈래(88줄), `FRICTION.md` 줄 양식(153줄)에 있음. 남은 것: 4번(77줄)에 `done-phase-N.md`의 "남은 것"을 넷에 대어 보는 규칙이 있음. 셋 모두 있음. 통과
- 완료 조건 2가 참이다.
  - `grep -rn '스킬 후보' plugins/plate/skills docs/ARCHITECTURE.md` → 세 줄. retro 153줄과 eval 31줄은 넷을 늘어놓고 `경계 밖`이 있음. eval 161줄은 스킬 후보 줄 하나만 가리킴. 통과
- 테스트가 모두 통과한다.
  - `python3 -m unittest discover -s tests` → `Ran 99 tests in 16.172s`, `OK`. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 99 tests`, `OK`. 통과

**실패**
- 없음

**하네스에서 걸린 것**
- 없음

**판정**: 통과
