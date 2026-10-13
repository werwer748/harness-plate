# Phase 5: 완성 판정을 돌린다

**목표**: 완료 조건 1~15가 실제 실행으로 참이다.

**읽을 것**
- `docs/TOOLS.md` ("Claude Code" 절)
- `~/plate-rail-test/bin/run.sh`, `bin/runcheck.py`, `bin/plancheck.py`, `answers/run-*.md` (Phase 4에서 준비한 것)

**TODO**
- [x] phase 하나짜리 작업의 판정 결과가 생긴다: 완료 조건 1, 4, 5, 6, 9, 11, 12, 13 (`~/plate-rail-test/logs/run-*.jsonl`)
- [x] 여러 phase와 이어 하기의 판정 결과가 생긴다: 완료 조건 2, 3, 7
- [x] worktree와 git 레포가 아닌 폴더의 판정 결과가 생긴다: 완료 조건 8, 10
- [x] plan 다시 판정과 excel-viewer의 판정 결과가 생긴다: 완료 조건 14, 15
- [x] 사용자에게 보인 글(다섯 줄, 세 줄, 물음, 보고)을 요청·답 파일과 나란히 놓은 표가 사용자에게 보여진다
- [x] 기대와 다른 경우가 있었으면 스킬이 고쳐지고 그 경우가 다시 통과한다. 본문의 규칙을 바꿔야 하면 고치기 전에 사용자에게 묻는다 (`plugins/plate/skills/`)
- [x] 판정하며 새로 확인한 도구 사실이 "Claude Code" 절에 적힌다 (`docs/TOOLS.md`)

**통과 조건**
- 완료 조건 1~15가 참이다.
  - 확인: 조건마다의 확인을 돌리고 읽어 기대와 같은지 본다
- 사용자가 표를 보고 확인했다.
  - 확인: 표를 적은 답글에 받은 답

## 한 일
- phase 하나짜리 작업, 여러 phase와 이어 하기, worktree와 git 레포가 아닌 폴더, plan 다시 판정과 excel-viewer의 판정 결과가 생긴다: 열다섯 경우를 헤드리스로 돌렸다. 본문을 고친 뒤 여섯(`run-small`, `run-big`, `run-fix`, `run-wrong`, `run-dirty`, `run-wt`)을 다시 돌렸고 첫 실행의 폴더와 기록은 `v1/`에 남겼다 (`~/plate-rail-test/logs/run-*.jsonl`, `logs/plan14-*.jsonl`, `v1/`)
- 사용자에게 보인 글을 요청·답 파일과 나란히 놓은 표가 사용자에게 보여진다: 첫 실행의 열다섯 조건을 표로, 다시 돌린 여섯을 달라진 것의 표로 보여 줬다
- 기대와 다른 경우가 있었으면 스킬이 고쳐지고 그 경우가 다시 통과한다: 사용자에게 하나씩 묻고 정한 대로 고쳤다 (`plugins/plate/skills/run/SKILL.md`, `plugins/plate/skills/phase/SKILL.md`)
  - 돌아온 다섯 줄과 세 줄은 바로 이어 멈춰서 물을 때만 그 물음과 함께 보이고, 그 밖에는 보고에 적는다. 이유: 첫 실행에서 다섯 줄은 수행 16번 가운데 2번, 세 줄은 회고 17번 가운데 9번만 전해졌고, 사용자가 읽고 정하는 자리가 물음과 보고뿐이다.
  - `docs/LESSONS.md`로 옮기는 것은 회고 절마다의 것이다. 이유: `run-fix`에서 회고 1의 "하네스의 문제점"이 빠졌다.
  - 수행 기록을 고쳐 쓸 때 "하네스에서 걸린 것"에 이미 있는 줄은 지우지 않고 더한다. 이유: `run-wrong`에서 첫 수행이 적은 줄이 둘째 수행에 덮였다.
- 판정하며 새로 확인한 도구 사실이 "Claude Code" 절에 적힌다: "실행 스킬의 판정에서 본 것" 아홉 줄을 더했다 (`docs/TOOLS.md`)

## 확인 결과
- 완료 조건 1~15가 참이다.
  - `python3 bin/runcheck.py <경우>`를 열네 경우에 → 모두 통과(실패 0줄). `run-big`, `run-wrong`, `run-wt`는 턴 사이에 돌린 `--stage`도 모두 통과. 통과
  - `python3 bin/plancheck.py`를 `plan14-adr`, `plan14-done`, `plan14-nogit`, `plan14-rule`에 → 모두 통과. 통과
  - 실행 기록에서 읽은 것: 회고할지와 이을지의 물음(`run-big`), 틀린 곳과 고칠 안(`run-wrong`), worktree의 안내 둘과 합칠지 묻는 글(`run-wt`), 파일 목록과 진행할지 묻는 글(`run-dirty`), 프로젝트의 규칙을 따른 곳(`run-rule`, `run-ev`), ADR 후보와 끝 물음과 보고(`plan14-*`), setup 뒤에 남은 지도의 행과 plan이 읽은 `docs/LESSONS.md`(`run-lessons`). 통과
  - `git -C ~/plate-rail-test/run-ev show 252a030:docs/tasks/001-change-notes/phase-1.md` → "읽을 것"의 다섯 경로가 실제 경로였고, 계획과 달라진 점은 `verifyPlugin`이 이 Mac에서 IDE 넷에만 댄다는 것 하나였다. 통과
- 사용자가 표를 보고 확인했다.
  - 표를 적은 답글에 받은 답 → "확인했다, 닫는다". 통과

## 계획과 달라진 점
- `run-dirty`와 `run-wt`의 합치는 실행은 그 물음의 답을 미리 주지 않고 두 턴으로 돌렸다. 미리 준 답으로는 묻는 글이 나오지 않아 조건 8과 11의 글을 볼 수 없었다. 판정 도구의 기록 이름은 `run-dirty-1`, `run-dirty-2`, `run-wt-c1`, `run-wt-c2`다.
- 판정 도구를 고쳤다. 에이전트에게 넘긴 글은 본문의 글로 시작하면 통과로 보고 더한 줄은 읽을 것으로 낸다. `run-ev`에서 run이 프로젝트의 규칙대로 규칙 파일의 경로 한 줄을 더했고, 본문은 프로젝트의 규칙이 앞선다고 한다. "하네스에서 걸린 것"에 앞서 있던 줄이 지워지지 않았는지 보는 줄도 더했다 (`~/plate-rail-test/bin/runcheck.py`, 다시 돌리는 `bin/rerun.sh`)
- 다시 돌리지 않은 아홉 경우(`run-all`, `run-skip`, `run-resume`, `run-rule`, `run-nogit`, `run-noplan`, `run-lessons`, `run-ev`, 조건 14)는 고치기 전 본문의 결과다. 고친 것이 보인 글의 자리와 `docs/LESSONS.md`로 옮기는 범위뿐이다.
- 조건 14 가운데 "범주 밖의 결정에는 ADR 항목을 더하는 TODO가 생기지 않는다"는 `plan14-adr`에서만 참이다. `base-big`의 계획은 "검색은 `LIKE` 부분 일치"와 "테스트 도구는 pytest"까지 후보로 냈고 초안을 통째로 승인해 TODO가 됐다. 사용자가 본문을 그대로 두기로 했다. 후보는 보여 주고 승인받는 것이라 사용자가 뺀다.

## 남은 것
없음

## 하네스에서 걸린 것
- 셋업이 만든 문서 지도의 "만들기 전에 위치를 묻는다"와 run의 `docs/LESSONS.md` "위치를 묻지 않는다"가 부딪힌다고 세 실행(`run-fix`, `run-big`, `run-ev`)이 보고에 적었다. 셋 다 묻지 않고 만들었다. 사용자가 그대로 두기로 했다.
- plan 스킬의 ADR 후보가 계획마다 갈린다. DB 파일의 위치를 `plan14-adr`은 후보로 내지 않았고 `base-big`은 냈다.
- retro 스킬 1번은 phase의 커밋을 `NNN-slug: phase N`으로 시작하는 메시지로 찾는다. 프로젝트의 커밋 규칙을 따른 커밋은 그 말로 찾아지지 않고(`run-rule`), 회고 커밋과 고침 커밋도 그 말에 맞는다(`run-fix`).
- phase 스킬에는 고칠 문제를 넘겨받은 수행이 "한 일"에 무엇을 적는지와 다섯 줄의 `TODO` 수가 무엇을 세는지가 없다(`run-fix`).
- retro 스킬에는 적힌 확인을 빌드 도구가 건너뛸 때(Gradle의 `UP-TO-DATE`) 어떻게 하는지가 없다. 점검 에이전트가 `--rerun`을 붙여 한 번 더 돌렸다(`run-ev`).
- 점검 에이전트는 다른 스킬의 본문을 읽지 못해 하네스의 문제점을 그 스킬의 규칙에 대어 보지 못한다(`run-fix`).
- run이 다음 phase를 이을지 물으면서 본문에 없는 선택지 "계획을 먼저 고친다"를 더했다(`run-big`의 둘째 턴).
- Phase 4의 기록이 "완료 조건 14에서 본다"로 넘긴 줄을 놓쳤다가 닫기 직전에 찾았다. 이 작업은 세션이 phase를 직접 수행해서 지워진 `phase-N.md`의 "하네스에서 걸린 것"이 `docs/LESSONS.md`로 옮겨지지 않고, 컨텍스트를 비운 세션은 그것을 읽을 곳이 없다.
