# Phase 1: run이 결과 없이 돌아온 에이전트를 세 번째에 멈춘다

**목표**: 신뢰성-3이 고쳐져, run이 결과 없이 돌아온 에이전트를 같은 자리에서 연달아 세 번째에 멈추고, `review.md` 없이 하네스 eval로 가지 않는다.

**테스트 먼저**: 아니오 — 스킬 본문(`.md`)과 그 글을 지키는 테스트만 고친다

**읽을 것**
- `docs/cleanup/2026-10-29.md` (신뢰성-3의 근거와 고치는 방향)
- `plugins/plate/skills/run/SKILL.md`의 "3. 갈 곳을 정한다", "4. 수행을 맡긴다", "5. 확인을 맡긴다", "7. task 회고를 맡긴다", "코드 평가를 맡긴다", "하네스 eval을 맡긴다", "멈춘다", "`RUNLOG.md`" 절
- `docs/PRD.md`의 핵심 기능 7
- `docs/ARCHITECTURE.md`의 데이터 흐름 절 뒤 "어느 실행 방식이든" 문단과 디렉터리 구조의 `test_skill_rules.py` 줄
- `tests/test_skill_rules.py` (`RunRulesTest`, `section`, `subsection`)

**TODO**
- [x] 4번, 5번, 7번, "코드 평가를 맡긴다", "하네스 eval을 맡긴다"의 돌아온 뒤에, 정한 결과(수행이면 `## 한 일` 기록 절, 확인이면 새 확인 절, 회고면 새 회고 절, 코드 평가면 `docs/tasks/review.md`, 하네스 eval이면 `docs/tasks/eval.md`)가 없으면 같은 자리를 다시 띄우고 에이전트 줄에 `| 다시 띄움: 결과 없음`을 덧붙이는 규칙이 더해진다. 같은 자리의 바로 앞 두 에이전트 줄이 모두 그 표시를 달았으면 다시 띄우지 않고 "멈춘다"로 간다 (`plugins/plate/skills/run/SKILL.md`)
- [x] "코드 평가를 맡긴다"의 돌아온 뒤가 `review.md`가 있을 때만 "하네스 eval을 맡긴다"로 가게 바뀐다 (`plugins/plate/skills/run/SKILL.md`)
- [x] "멈춘다"의 자리 목록에 결과 없이 돌아온 에이전트의 연달아 세 번째가 더해지고, "`RUNLOG.md`" 절의 `다시 띄움` 설명에 `결과 없음`이 더해진다 (`plugins/plate/skills/run/SKILL.md`)
- [x] 위 글을 지키는 `RunRulesTest.test_no_result_relaunch_limit`이 더해진다 (`tests/test_skill_rules.py`)
- [x] PRD 핵심 기능 7의 멈추는 자리와 ARCHITECTURE의 "어느 실행 방식이든" 문단에 결과 없는 에이전트의 세 번째가 더해지고, ARCHITECTURE의 `test_skill_rules.py` 줄에 새 시험이 더해진다 (`docs/PRD.md`, `docs/ARCHITECTURE.md`)

**통과 조건**
- run 본문이 다시 띄움과 상한을 적는다(완료 조건 1).
  - 확인: `grep -n '다시 띄움: 결과 없음' plugins/plate/skills/run/SKILL.md` → "멈춘다" 절과 "`RUNLOG.md`" 절에 저마다 한 줄 이상
  - 확인: `python3 -m unittest tests.test_skill_rules.RunRulesTest.test_no_result_relaunch_limit -v` → `OK`
- 맥락 문서가 맞다(완료 조건 8의 앞 절).
  - 확인: `grep -n '결과 없' docs/PRD.md docs/ARCHITECTURE.md` → 두 파일에 저마다 한 줄 이상
- 테스트 묶음이 통과한다.
  - 확인: `python3 -m unittest discover -s tests` → 마지막 줄이 `OK`

## 한 일
- 4번, 5번, 7번, "코드 평가를 맡긴다", "하네스 eval을 맡긴다"의 돌아온 뒤에 결과 없음 규칙: 낱말에 "결과 없이 돌아온 에이전트" 항목을 더해 남겨야 할 결과(수행 `## 한 일`, 확인·회고는 맡기기 전보다 하나 는 절, `review.md`, `eval.md`), 다시 띄울 때 그 에이전트 줄에 `| 다시 띄움: 결과 없음`을 덧붙임, 같은 자리의 마지막 두 에이전트 줄이 모두 그 표시면 "멈춘다"로 감을 한 곳에 적고, 다섯 절의 돌아온 뒤에 저마다 그 항목대로 하라는 한 줄을 더했다 (`plugins/plate/skills/run/SKILL.md`)
- "코드 평가를 맡긴다"의 돌아온 뒤: `docs/tasks/review.md`가 있을 때만 "하네스 eval을 맡긴다"로 가고, 없으면 결과 없음 규칙으로 간다고 바꿨다 (`plugins/plate/skills/run/SKILL.md`)
- "멈춘다" 목록에 같은 자리의 연달아 세 번째 결과 없음을 더하고, "`RUNLOG.md`" 절의 `다시 띄움` 설명에서 "에이전트가 결과 없이 끊겼다" 예를 `| 다시 띄움: 결과 없음`으로 적는 규칙으로 바꿨다 (`plugins/plate/skills/run/SKILL.md`)
- `RunRulesTest.test_no_result_relaunch_limit`을 더했다: 낱말 항목의 결과 다섯과 상한 글, 다섯 절의 가리킴, 코드 평가 뒤 `review.md` 조건(옛 글 "그다음 \"하네스 eval을 맡긴다\"로 간다"가 없음), "멈춘다"와 "`RUNLOG.md`" 절의 글을 본다 (`tests/test_skill_rules.py`)
- PRD 핵심 기능 7의 멈추는 자리와 ARCHITECTURE "어느 실행 방식이든" 문단에 결과 없는 에이전트의 세 번째를, ARCHITECTURE `test_skill_rules.py` 줄에 새 시험을 더했다 (`docs/PRD.md`, `docs/ARCHITECTURE.md`)

## 확인 결과
- run 본문이 다시 띄움과 상한을 적는다(완료 조건 1).
  - `grep -n '다시 띄움: 결과 없음' plugins/plate/skills/run/SKILL.md` → 59(낱말), 293("멈춘다" 절), 570("`RUNLOG.md`" 절). 통과
  - `python3 -m unittest tests.test_skill_rules.RunRulesTest.test_no_result_relaunch_limit -v` → `Ran 1 test`, `OK`. 통과
- 맥락 문서가 맞다(완료 조건 8의 앞 절).
  - `grep -n '결과 없' docs/PRD.md docs/ARCHITECTURE.md` → `docs/PRD.md:17`, `docs/ARCHITECTURE.md:39`, `docs/ARCHITECTURE.md:98`. 통과
- 테스트 묶음이 통과한다.
  - `python3 -m unittest discover -s tests` → `Ran 230 tests in 20.765s`, `OK`. 통과

## 계획과 달라진 점
- TODO 1은 다섯 절의 돌아온 뒤에 규칙을 더한다고 했으나, 규칙 전체는 낱말의 한 항목("결과 없이 돌아온 에이전트")에 한 번 적고 다섯 절에는 그 항목을 가리키는 한 줄만 두었다. 같은 규칙이 다섯 번 복사되지 않게 한 것이다(이 본문의 "양식을 읽는 법"처럼 낱말 한 곳 + 가리킴).

## 남은 것
- 수행의 "남겨야 할 결과"는 `## 한 일` 기록 절의 유무로만 본다. 고칠 문제를 넘겨받은 수행처럼 기록 절이 이미 있는 phase에서 에이전트가 아무것도 바꾸지 않고 돌아오면 결과 없음으로 잡지 못하고, 그 뒤 확인이 다시 실패해 확인 절 수의 상한으로 멈춘다.
- 3번 "갈 곳을 정한다"의 표는 바꾸지 않았다. 세션을 끊고 다시 불러 3번 표로 같은 자리를 다시 맡길 때도 상한은 `RUNLOG.md`의 줄로 세지만, 그 다시 맡김 자체에 `결과 없음` 표시를 달지는 이 phase가 정하지 않았다.
- 동작은 헤드리스로 돌려 보지 않았다(task 머리의 돌리지 않음 줄).

## 하네스에서 걸린 것
없음

## 확인 1

**통과 조건**
- run 본문이 다시 띄움과 상한을 적는다(완료 조건 1).
  - `grep -n '다시 띄움: 결과 없음' plugins/plate/skills/run/SKILL.md` → 59(낱말), 293("멈춘다" 절, 285~305행), 570("`RUNLOG.md`" 절, 555행부터). 두 절에 저마다 한 줄 이상. 통과
  - `python3 -m unittest tests.test_skill_rules.RunRulesTest.test_no_result_relaunch_limit -v` → `Ran 1 test`, `OK`. 통과
- 맥락 문서가 맞다(완료 조건 8의 앞 절).
  - `grep -n '결과 없' docs/PRD.md docs/ARCHITECTURE.md` → `docs/PRD.md:17`, `docs/ARCHITECTURE.md:39`, `docs/ARCHITECTURE.md:98`. 두 파일에 저마다 한 줄 이상. 통과
- 테스트 묶음이 통과한다.
  - `python3 -m unittest discover -s tests` → `Ran 230 tests`, 마지막 줄 `OK`. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 230 tests in 20.635s`, `OK`. 통과

**남은 것**
- 수행의 "남겨야 할 결과"를 `## 한 일` 유무로만 봐, 기록 절이 이미 있는 phase에서 아무것도 바꾸지 않고 돌아온 수행을 결과 없음으로 잡지 못함 → 통과 조건은 본문의 글(grep 줄)과 그 글을 지키는 테스트, 맥락 문서의 줄, 테스트 묶음을 보고 이 꼴의 동작은 보지 않는다. 기록대로 확인 절 수의 상한으로는 멈춘다. 하네스에서 걸린 것
- 3번 "갈 곳을 정한다"로 다시 맡길 때 `결과 없음` 표시를 달지 정하지 않음 → 통과 조건의 어느 확인도 3번 표의 다시 맡김을 보지 않는다. 하네스에서 걸린 것
- 동작을 헤드리스로 돌려 보지 않음 → task 머리 완료 조건 1의 `- 돌리지 않음: 에이전트가 결과 없이 돌아오는 장면은 run을 헤드리스로 돌려 일부러 만들 수 없다`가 돌리지 않기로 정한 동작이다. 하네스에서 걸린 것

**실패**
없음

**하네스에서 걸린 것**
- 남은 것: 수행의 "남겨야 할 결과"를 `## 한 일` 유무로만 봐, 고칠 문제를 넘겨받은 수행처럼 기록 절이 이미 있는 phase에서 아무것도 바꾸지 않고 돌아온 에이전트를 결과 없음으로 잡지 못한다(확인 절 수의 상한으로 멈춘다).
- 남은 것: 세션을 끊고 3번 표로 같은 자리를 다시 맡길 때 그 다시 맡김에 `결과 없음` 표시를 달지는 이 phase가 정하지 않았다.
- 남은 것: 동작은 헤드리스로 돌려 보지 않았다(완료 조건 1의 `돌리지 않음` 줄).
- 명령 절의 빌드·린트가 "없음"이라 돌리지 않았다.

**판정**: 통과
