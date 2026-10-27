# Phase 1: run 본문과 문서를 고친다

**목표**: run 본문에 다섯 이슈의 해결이 들어가고 맥락 문서와 README가 맞춰진다.

**테스트 먼저**: 아니오 — `.md`(스킬 본문과 문서)만 고친다

**읽을 것**
- `plugins/plate/skills/run/SKILL.md` (고칠 본문)
- `gh issue view 34 --repo werwer748/harness-plate`, 35, 38, 40, 44 (이슈마다의 원인과 해결책)
- `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `docs/BACKLOG.md`, `README.md` (맥락 문서와 README)

**TODO**
- [x] "1. 시작 조건을 본다"에 첫 에이전트를 띄우기 전의 권한 확인이 더해진다: plan 모드가 켜져 있거나 쓰기가 막힐 권한 모드면 알리고 바꿀지 묻고 멈추며, 확인할 수 없는 도구면 그렇다고 적고 잇는다. "`RUNLOG.md`" 절의 물은 자리 목록과 task에 걸리지 않는 물음 목록에 `권한`이 더해진다 (#40) (`plugins/plate/skills/run/SKILL.md`)
- [x] "7. task 회고를 맡긴다", "코드 평가를 맡긴다", "하네스 eval을 맡긴다"에서 돌아와 더한 `RUNLOG.md` 줄을 그 자리에서 그 파일만 넣는 커밋(회고 뒤 `NNN-slug: RUNLOG`, 평가 뒤 `<tasks 이름>: RUNLOG`)으로 넣는다는 글이 더해지고, "`RUNLOG.md`" 절의 커밋 자리 글이 이 자리를 담게 바뀐다 (#44) (`plugins/plate/skills/run/SKILL.md`)
- [x] "`RUNLOG.md`" 절의 사용량 줄이 돌아오지 않은 값은 단위 없이 `모름`(`시간 모름`)으로 적고, 돌아오지 않은 까닭을 알면 `docs/TOOLS.md`에 적는다로 바뀐다 (#35) (`plugins/plate/skills/run/SKILL.md`)
- [x] "8. 고칠 phase를 더한다"의 앞에 회고의 문제를 고치려면 계획 파일의 목표나 완료 조건을 바꾸거나 좁혀야 하면 고칠 phase를 더하지 않고 어느 실행 방식이든 "멈춘다"로 간다는 글이 더해지고, "멈춘다"의 자리 목록에 그 자리가 더해지며, 그때 물은 것은 `멈춤`이라고 "`RUNLOG.md`" 절과 맞는다 (#34, #38) (`plugins/plate/skills/run/SKILL.md`)
- [x] "8. 고칠 phase를 더한다"의 TODO 규칙에 고칠 동작을 적은 맥락 문서와 README의 줄도 TODO에 넣는다는 글과, 계획 커밋(`plan: NNN-slug 수정`)으로 이미 고친 문제는 TODO에 넣지 않고 통과 조건에 "계획 커밋 `{해시}`로 고쳤다"와 그 확인을 따로 적는다는 글이 더해지고, 고칠 phase의 양식 블록이 그 통과 조건 자리를 담게 바뀐다 (#38) (`plugins/plate/skills/run/SKILL.md`)
- [x] run 본문 앞머리의 description, `docs/PRD.md`의 핵심 기능 7, `docs/ARCHITECTURE.md`의 "패턴과 규칙"의 run 문단과 "데이터 흐름"의 실행 갈래와 그 아래 멈추는 자리 문단, `README.md`의 `run` 행이 시작할 때의 권한 물음, `RUNLOG.md`의 커밋 자리, 회고가 계획을 바꾸게 할 때 멈추는 것을 담게 바뀐다 (`plugins/plate/skills/run/SKILL.md`, `docs/PRD.md`, `docs/ARCHITECTURE.md`, `README.md`)

**통과 조건**
- 완료 조건 1의 본문이 적혀 있다.
  - 확인: run 본문의 "1. 시작 조건을 본다", "7. task 회고를 맡긴다", "8. 고칠 phase를 더한다", "멈춘다", "코드 평가를 맡긴다", "하네스 eval을 맡긴다", "`RUNLOG.md`" 절을 읽어 다섯 해결이 저마다 적혀 있다. 하나라도 없으면 실패
  - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`, `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
- 완료 조건 2가 참이다.
  - 확인: `docs/PRD.md`의 핵심 기능 7, `docs/ARCHITECTURE.md`의 "패턴과 규칙"의 run 문단과 "데이터 흐름"의 실행 갈래와 그 아래 멈추는 자리 문단, `README.md`의 `run` 행, run 본문 앞머리의 description을 저마다 읽어 세 동작과 어긋나는 줄이 없다

## 한 일
- "1. 시작 조건을 본다"에 권한 확인 (#40): 절 첫머리에 git 레포와 상관없이 첫 에이전트를 띄우기 전에 보는 "권한" 항목을 더했다. plan 모드나 쓰기가 막힐 권한 모드면 에이전트를 띄우지 않고 알리고 바꿀지 묻고 멈추며, 답은 물은 자리 `권한`으로 적고, 멈추자고 하면 끝난다. 도구가 모드를 알려 주지 않으면 묻지 않고 10번의 보고에 적고 잇는다. "`RUNLOG.md`" 절의 물은 자리 목록과 task에 걸리지 않는 물음 목록에 `권한`을 더했고, 10번 보고 목록에 확인할 수 없었던 것을 적는 줄을 더했다 (`plugins/plate/skills/run/SKILL.md`)
- 회고·코드 평가·하네스 eval 뒤의 RUNLOG 커밋 (#44): 7번, "코드 평가를 맡긴다", "하네스 eval을 맡긴다"의 돌아온 뒤 글에 그 자리에서 `RUNLOG.md`만 넣는 커밋(`NNN-slug: RUNLOG`, `<tasks 이름>: RUNLOG`, git 레포가 아니면 하지 않는다)을 더했고, "`RUNLOG.md`" 절의 커밋 자리 글을 이 세 자리를 담게 바꿨다 (`plugins/plate/skills/run/SKILL.md`)
- 사용량의 `모름` (#35): 돌아오지 않은 값은 단위 없이 `모름`(`시간 모름`)으로 적고, 까닭을 알면 10번의 보고와, 문서 지도에 `docs/TOOLS.md`가 있으면 거기에도 적어 다음 `RUNLOG.md` 커밋에 넣는다고 바꿨다. run이 `docs/TOOLS.md`를 직접 고치게 되므로 절대 규칙 5의 직접 고치는 파일에 그것을 더했다 (`plugins/plate/skills/run/SKILL.md`)
- 회고가 계획을 바꾸게 할 때 멈춤 (#34, #38): 8번 첫머리에 문제를 고치려면 계획 파일의 목표나 완료 조건을 바꾸거나 좁혀야 하면 고칠 phase를 더하지 않고 어느 실행 방식이든 "멈춘다"로 가고 물은 것은 `멈춤`이라는 글을 더했다. "멈춘다"의 자리 목록에 그 자리를, 4번 "다시 맡긴다"에 그 자리에서 계획을 고친 뒤 3번으로 가는 길을, 절대 규칙 4와 2번의 tasks 일괄 설명에 이 예외를, "`RUNLOG.md`" 절에 그 자리의 물음은 `멈춤`이고 `고칠 phase`가 아니라는 글을 더했다 (`plugins/plate/skills/run/SKILL.md`)
- 고칠 phase의 TODO와 계획 커밋으로 고친 문제 (#38): 8번 규칙에 고칠 동작을 적은 맥락 문서와 README의 줄도 TODO에 넣는다는 항목과, 마지막 회고 커밋 뒤의 `plan: NNN-slug 수정` 커밋으로 이미 고친 문제는 TODO에 넣지 않고 통과 조건에 "회고 K의 문제 {번호}는 계획 커밋 `{해시}`로 고쳤다"와 그 확인을 따로 적는다는 항목을 더했다. 양식 블록의 TODO 줄과 통과 조건에 그 자리를 더했다 (`plugins/plate/skills/run/SKILL.md`)
- description과 문서: run 앞머리의 description에 시작할 때의 권한 물음, 회고가 계획을 바꾸게 할 때의 멈춤, 회고·평가 뒤의 `RUNLOG.md` 커밋을 더했다. `docs/PRD.md`의 핵심 기능 7, `docs/ARCHITECTURE.md`의 "패턴과 규칙"(run 문단 앞에 세 동작을 적은 문단을 더함)과 "데이터 흐름"의 실행 갈래와 그 아래 멈추는 자리 문단, `README.md`의 `run` 행을 같은 동작으로 맞췄다 (`plugins/plate/skills/run/SKILL.md`, `docs/PRD.md`, `docs/ARCHITECTURE.md`, `README.md`)

## 확인 결과
- 완료 조건 1의 본문이 적혀 있다.
  - run 본문의 "1. 시작 조건을 본다"(권한 항목, #40), "7. task 회고를 맡긴다"(`NNN-slug: RUNLOG` 커밋, #44), "8. 고칠 phase를 더한다"(첫머리의 멈춤 #34·#38, TODO의 맥락 문서·README 줄과 계획 커밋 통과 조건 #38, 양식 블록), "멈춘다"(자리 목록의 새 줄, 다시 맡기는 길), "코드 평가를 맡긴다"와 "하네스 eval을 맡긴다"(`<tasks 이름>: RUNLOG` 커밋, #44), "`RUNLOG.md`"(커밋 자리, `권한`, `시간 모름` #35, `멈춤`) 절을 `git diff plugins/plate/skills/run/SKILL.md`로 읽음 → 다섯 해결이 저마다 있다. 통과
  - `python3 -m unittest discover -s tests` → `Ran 129 tests in 16.775s` / `OK`. `claude plugin validate .` → `✔ Validation passed`. 통과
- 완료 조건 2가 참이다.
  - `git diff docs/PRD.md docs/ARCHITECTURE.md README.md`와 run 앞머리 description을 읽음 → 네 곳 모두 시작할 때의 권한 물음, `RUNLOG.md`의 커밋 자리(PRD 7, ARCHITECTURE 패턴 문단과 데이터 흐름, README `run` 행, description), 회고가 계획을 바꾸게 할 때 멈추는 것을 담고, 이와 어긋나는 줄이 없다. 통과

## 계획과 달라진 점
- `docs/ARCHITECTURE.md`의 "패턴과 규칙"의 run 문단은 기본 브랜치·PR 문단 하나뿐이라, 그 문단을 늘리지 않고 그 앞에 세 동작(권한, 회고가 계획을 바꿀 때의 멈춤과 고칠 phase의 TODO, `RUNLOG.md` 커밋 자리)을 적은 run 문단을 하나 더했다. 문단이 너무 길어지지 않게 한 것이다
- #35의 "`docs/TOOLS.md`에 적는다"를 run이 하게 하려고 절대 규칙 5의 직접 고치는 파일 목록에 `docs/TOOLS.md`(문서 지도에 있을 때)를 더했다. 더하지 않으면 TODO의 글이 절대 규칙 5와 부딪힌다

## 남은 것
- 고친 동작은 글로만 맞췄고 실제로 돌려 보지 않았다. 장면 A~D는 phase 2, 3의 몫이다
- 권한 확인은 "쓰기를 막을 권한 모드"를 일반 글로 적었다. 어느 모드가 어느 경로를 막는지는 도구와 프로젝트마다 달라, 세션이 지금 모드를 알 수 없거나 막힐 경로를 모르면 묻지 않고 지나간다
- 계획 커밋으로 고친 문제를 찾는 명령은 `retro.md`를 마지막으로 바꾼 커밋 뒤의 `plan: NNN-slug 수정` 커밋을 본다. 회고 절을 더한 뒤 다른 커밋이 `retro.md`를 바꾸면 기준이 어긋날 수 있다

## 하네스에서 걸린 것
- 없음

## 확인 1

**통과 조건**
- 완료 조건 1의 본문이 적혀 있다.
  - `plugins/plate/skills/run/SKILL.md`의 "1. 시작 조건을 본다", "7. task 회고를 맡긴다", "8. 고칠 phase를 더한다", "멈춘다", "코드 평가를 맡긴다", "하네스 eval을 맡긴다", "`RUNLOG.md`" 절을 읽음 → #40: 1번 첫머리의 "권한" 항목(plan 모드나 쓰기를 막을 모드면 띄우지 않고 알리고 바꿀지 묻고 멈춤, 확인할 수 없으면 묻지 않고 10번 보고에 적고 잇는다). #44: 7번(`NNN-slug: RUNLOG`), "코드 평가를 맡긴다"와 "하네스 eval을 맡긴다"(`<tasks 이름>: RUNLOG`)의 그 자리 커밋과 "`RUNLOG.md`" 절의 커밋 자리 글. #35: 사용량 줄의 "단위 없이 `모름`(`시간 모름`)". #34·#38: 8번 첫머리의 멈춤과 "멈춘다" 자리 목록의 새 줄, "`RUNLOG.md`" 절의 `멈춤`이고 `고칠 phase`가 아니라는 글. #38: 8번 규칙의 맥락 문서·README 줄을 TODO에 넣는 항목과 계획 커밋으로 고친 문제를 통과 조건에 해시와 따로 적는 항목, 양식 블록의 그 자리. 다섯 해결이 저마다 있다. 통과
  - `python3 -m unittest discover -s tests` → `Ran 129 tests in 16.891s` / `OK`. `claude plugin validate .` → `✔ Validation passed`. 통과
- 완료 조건 2가 참이다.
  - `docs/PRD.md`의 핵심 기능 7, `docs/ARCHITECTURE.md`의 "패턴과 규칙"의 run 문단(새 문단과 기본 브랜치 문단)과 "데이터 흐름"의 실행 갈래와 그 아래 멈추는 자리 문단, `README.md`의 `run` 행, run 앞머리의 description을 읽음 → 모두 시작할 때의 권한 물음, `RUNLOG.md`의 그 자리 커밋, 회고가 계획을 바꾸게 할 때의 멈춤을 담고, 어긋나는 줄이 없다. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 129 tests` / `OK`. 통과

**남은 것**
- 고친 동작은 글로만 맞췄고 실제로 돌려 보지 않았다(장면 A~D는 phase 2, 3) → 이 phase의 통과 조건은 본문과 문서의 글만 보고 돌린 동작을 보지 않는다. 하네스에서 걸린 것
- 권한 확인은 세션이 지금 모드나 막힐 경로를 모르면 묻지 않고 지나간다 → 통과 조건이 보는 것은 "확인할 수 없으면 적고 잇는다"는 글이 있는지이고, 이 꼴은 완료 조건 1이 정한 동작 그대로다. 걸리지 않는다. 하네스에서 걸린 것
- 계획 커밋으로 고친 문제를 찾는 명령이 `retro.md`를 마지막으로 바꾼 커밋을 기준으로 해서, 회고 절 뒤 다른 커밋이 `retro.md`를 바꾸면 기준이 어긋날 수 있다 → 통과 조건은 #38의 해결이 글로 적혀 있는지만 본다. 걸리지 않는다. 하네스에서 걸린 것

**실패**
- 없음

**하네스에서 걸린 것**
- 남은 것: 고친 동작은 글로만 맞췄고 장면으로 돌려 보지 않았다. phase 2, 3의 장면 A~D가 본다
- 남은 것: 권한 확인은 도구가 지금 모드를 알려 주지 않거나 막힐 경로를 모르면 묻지 않고 지나가, 그런 세션에서는 #40의 막힘이 그대로 남을 수 있다
- 남은 것: 8번의 계획 커밋 찾기 명령(`git log … $(git log -1 --format=%h -- docs/tasks/NNN-slug/retro.md)..HEAD …`)은 회고 절 뒤에 다른 커밋이 `retro.md`를 바꾸면 기준이 어긋날 수 있다

**판정**: 통과
