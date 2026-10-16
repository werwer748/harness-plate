# Phase 5: 이 레포에서 004를 검증한다 (자기 적용)

**목표**: `004-context-rules`가 run으로 검증돼 `verify.md`의 검증이 닫힌다(판정이 "통과"이거나, 사용자가 남은 문제를 나중에 다루기로 했다).

**읽을 것**
- `docs/tasks/004-context-rules/plan.md` (004의 완료 조건)
- `~/.claude/projects/-Users-gangjungi-Desktop-harness-plate/` (사용자가 연 세션의 기록 `<세션>.jsonl`)
- `~/plate-rail-test/bin/calls.py`, `~/plate-rail-test/bin/runcheck.py` (기록과 커밋을 보는 도구)

**TODO**
- [x] 사용자가 새 세션에 붙여 넣을 글이 답글의 맨 끝에 코드 블록 하나로 주어진다. 004의 번호를 주어 부르는 글이다
- [x] 사용자가 `claude --plugin-dir plugins/plate`로 연 새 세션에서 run을 직접 불러 004의 검증이 끝난다. 이 phase를 수행하는 세션은 run을 부르지 않는다
- [x] 그 세션의 기록과 커밋을 읽은 결과가 사용자에게 보여진다: 커밋과 메시지, 메인이 직접 고친 파일, 검증 에이전트에게 넘긴 글, `verify.md`의 판정, `docs/LESSONS.md`로 옮긴 줄
- [x] 기대와 다른 것이 있었으면 스킬이 고쳐지고 걸리는 판정이 다시 통과한다. 본문의 규칙을 바꿔야 하면 고치기 전에 사용자에게 묻는다 (`plugins/plate/skills/`)

**통과 조건**
- 완료 조건 14가 참이다.
  - 확인: 완료 조건 14의 확인을 돌린다

## 한 일
- 사용자가 `claude --plugin-dir plugins/plate`로 연 세션 둘에서 `/plate:run 004`를 불렀다. 첫 세션(`f7cfecb6`)은 검증 에이전트 하나를 띄워 검증 1이 "문제 있음"(문제 1개)으로 끝났다(`b660382`). 사용자가 그 문제를 나중에 다루겠다고 했는데 run에 그 길이 없어, 메인이 사용자의 뜻으로 LESSONS를 손으로 고쳤다(`f3a20b4`). 같은 세션이 사용자의 뜻으로 계획과 run, verify에 미루는 길을 더한 뒤 그 커밋을 되돌렸다(`7210b69`, `de62793`, `55dd705`). 둘째 세션(`cbf0b287`)은 고칠 phase 3의 안과 승인, 나중에 다룸, 멈춤의 물음을 보이고 멈췄다. "나중에 다룬다"는 답에 `verify.md`에 미룬다는 줄을 적고 LESSONS로 옮겨 `cbb3ce0`(`004-context-rules: 검증 1 미룸`)으로 커밋했다
- 미루는 길에 맞게 setup의 규칙 구간을 "작업은 검증이 닫혀야 끝난다"로 고쳤다(사용자 승인). 006 계획의 목표와 결정에서 검증 "통과"를 보던 다섯 곳(목표, 검증이 남은 작업, 합치기, `done-phase` 지우기, 규칙 구간)을 "닫힌" 검증으로 맞췄다 (`plugins/plate/skills/setup/SKILL.md`, `docs/tasks/006-verify/plan.md`, `29d8272`, `4b71590`)
- 바뀐 동작에 걸리는 판정을 헤드리스로 다시 돌려 통과했다(2.1.301): run-vfix 세 턴(43, 125, 362초), setup-fresh 174초와 다시 돌린 것 404초, setup-remap 두 턴(252, 18초). `runcheck.py`의 LESSONS 기대(문서 지도 행의 글, `## 미룬 문제` 절)를 새 양식에 맞췄다. LESSONS를 만드는 다른 경우(run-small 등)의 옛 결과를 다시 대조하면 그 두 줄이 실패한다 (`~/plate-rail-test/bin/runcheck.py`, `logs/run-vfix-*.jsonl`, `setup-fresh*.jsonl`, `setup-remap-*.jsonl`)

## 확인 결과
- 완료 조건 14가 참이다.
  - `ls docs/tasks/004-context-rules/` → `plan.md`, `verify.md`. 통과
  - `git log --format=%s | grep -c '^004-context-rules: 검증$'` → 1. `git branch --list 'task/004-context-rules'` → 출력 없음. 통과
  - `verify.md`의 마지막 검증 절은 `## 검증 1`(판정 "문제 있음")이고 그 아래에 "사용자가 남은 문제를 나중에 다루기로 했다"가 있다. 통과
  - 두 세션의 기록을 읽음 → 검증 에이전트에게 넘긴 글은 본문의 두 줄 그대로다(첫 세션). 메인은 완료 조건의 확인을 돌리지 않았다. run의 절차 안에서 메인이 직접 고친 파일은 둘째 세션의 `verify.md`(미룬다는 줄)와 `docs/LESSONS.md`뿐이고, 둘째 세션은 에이전트를 띄우지 않았다. LESSONS로 옮긴 줄은 배운 것 2줄, 하네스의 문제점 3줄, 새로 만든 `## 미룬 문제` 절의 1줄이다. 하네스의 문제점 셋째 줄의 "위 문제"만 "검증 1의 문제"로 바꿨다고 보고했다. 통과
- 완료 조건 6과 13이 다시 참이다(바뀐 run의 물음과 setup의 규칙 구간).
  - `runcheck.py run-vfix` → 모두 통과. 첫 턴이 고칠 phase의 안과 세 갈래 물음을 보이고 멈췄고, 그때 파일 변경이 없다. 통과
  - `setupcheck.py setup-fresh PRD,ARCHITECTURE,ADR` → 모두 통과. `셋업 직후`로 커밋하고 다시 돌린 뒤 `git status --short` → 출력 없음. 통과
  - setup-remap의 첫 턴이 할 일 표에 "규칙 구간 더하기 | 필요" 행과 새 글을 보이고 멈췄다. 그때 파일 변경이 없다. 승인한 둘째 턴 뒤 `git diff --numstat` → `7 0 AGENTS.md`, 규칙 구간만 더해졌다. 통과

## 계획과 달라진 점
- 첫 실행에서 사용자가 검증의 문제를 나중에 다루기로 해서 run에 미루는 길을 더했다. 계획에는 결정 한 줄을 더하고, 완료 조건 14와 이 phase의 목표를 "검증이 닫혔다"로 바꿨다. 그 뒤 004를 한 번 더 돌렸다. 이 고침은 이 phase를 판정하는 세션이 아니라 첫 실행의 세션이 했다.
- 둘째 실행의 메인은 미루는 길을 따르기 전에 되돌린 커밋 `f3a20b4`를 읽었다. 옮긴 줄은 그 커밋과 달리 `verify.md`의 글 그대로였고, 그 커밋의 다섯째 줄(run에 미루는 길이 없다)은 옮기지 않았다.

## 남은 것
없음

## 하네스에서 걸린 것
- run이 고칠 phase의 안 뒤에 양식에 없는 안내를 덧붙였다(004 첫 실행: bypass 모드로 바꿨는지, 계획의 결정과 부딪힐 수 있음. run-vfix 첫 턴: 고르기 전에 확인할 점). 006 phase 3의 run-all 첫 턴과 같은 일이다.
