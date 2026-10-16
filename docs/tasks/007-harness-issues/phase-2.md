# Phase 2: run의 LESSONS와 닫힌 검증

**목표**: run이 LESSONS에 같은 뜻의 줄을 겹쳐 넣지 않고, 옛 셋업에서는 위치를 묻고, 닫힌 검증을 다시 만나도 "통과하면"의 1번부터 하며, 옛 셋업의 시험 폴더에서 묻고 멈추는 것이 확인된다.

**읽을 것**
- `docs/LESSONS.md` (하네스의 문제점 절의 `(006-verify, phase 2)` 다섯째 줄(같은 사실이 두 줄)과 `(006-verify, phase 3)` 첫째 줄(옛 셋업), 미룬 문제 절의 `(006-verify, 검증 1)` 마지막 줄(첫 갈래의 결함))
- `plugins/plate/skills/run/SKILL.md` ("검증을 맡긴다"와 "`docs/LESSONS.md`" 절)
- `plugins/plate/skills/setup/SKILL.md` ("문서 지도 구간" 절: 지금의 지도 위의 글)
- `~/plate-rail-test/bin/vfmake.sh` (시험 폴더를 만드는 꼴과 `vrule-base`)
- `~/plate-rail-test/bin/run.sh` (헤드리스 실행의 꼴과 허용 목록)
- `~/plate-rail-test/answers/run-vrule.md` (run에 줄 글 `001`)
- `docs/TOOLS.md` ("Claude Code" 절의 헤드리스 실행과 권한)

**TODO**
- [x] run "`docs/LESSONS.md`" 절에서, 옮길 줄과 같은 뜻의 줄이 LESSONS의 같은 절에 이미 있으면 더하지 않는다. 회고 절과 검증 절에서 옮길 때 모두, 다른 작업에서 옮긴 줄과 겹칠 때도 같다 (`plugins/plate/skills/run/SKILL.md`)
- [x] run "`docs/LESSONS.md`" 절에서, 문서 지도 위의 글에 "하네스의 스킬이 위치를 정해 둔 기록은 묻지 않고"가 없는 프로젝트에서 LESSONS를 처음 만들 때는 위치를 묻고, `docs/LESSONS.md`를 추천안으로 내며, setup을 다시 돌리면 다음부터 묻지 않는다고 함께 알린다 (`plugins/plate/skills/run/SKILL.md`)
- [x] run "검증을 맡긴다"의 첫 갈래가, 닫힌 검증이면 맡기지 않고 "통과하면"의 1번부터 하게 바뀐다 (`plugins/plate/skills/run/SKILL.md`)
- [x] `bin/vfmake.sh`가 시험 폴더 `run-oldsetup`을 만든다. `vrule-base`에 `docs/LESSONS.md`와 문서 지도의 LESSONS 행을 지운 커밋을 얹은 것이다 (`~/plate-rail-test/bin/vfmake.sh`)
- [x] run과 verify의 본문을 마지막으로 고친 뒤 `run-oldsetup`에서 `/plate:run 001`을 헤드리스로 한 턴 돌린 기록이 `logs/run-oldsetup.jsonl`에 있다. run은 검증이 `verify.md`를 커밋한 뒤 LESSONS를 만들기 전에 위치를 묻고 멈췄고, `docs/LESSONS.md`도 지도의 행도 생기지 않았다 (`~/plate-rail-test/bin/run.sh`)

**통과 조건**
- 완료 조건 4, 5, 6이 참이다.
  - 확인: 완료 조건 4, 5, 6의 확인을 모두 돌린다

## 한 일
- run "`docs/LESSONS.md`" 절에서, 옮길 줄과 같은 뜻의 줄이 LESSONS의 같은 절에 이미 있으면 더하지 않는다: "옮기는 것"의 끝에 회고 절·검증 절에서 옮길 때와 다른 작업에서 옮긴 줄과 겹칠 때를 함께 적은 한 줄을 더했다 (`plugins/plate/skills/run/SKILL.md`)
- run "`docs/LESSONS.md`" 절에서, 옛 셋업이면 위치를 묻는다: "문서 지도"의 첫 문단에 "다만 표 위의 글에 「하네스의 스킬이 위치를 정해 둔 기록은 묻지 않고」가 없으면 처음 만들기 전에 위치를 묻고 멈춘다, 전체 지시여도 묻는다, `docs/LESSONS.md`를 추천안으로 내고 `plate:setup`을 다시 돌리면 다음부터 묻지 않는다고 알린다"를 더했다 (`plugins/plate/skills/run/SKILL.md`)
- run "검증을 맡긴다"의 첫 갈래: "통과하면"의 4번으로 가던 것을 1번부터 하게 바꾸고, 1~3을 이미 했어도 옮긴 줄은 다시 더하지 않고 지울 파일이나 고친 파일이 없으면 지나간다고 적었다 (`plugins/plate/skills/run/SKILL.md`)
- `bin/vfmake.sh`가 `run-oldsetup`을 만든다: `vrule-base`를 복제해 `git rm docs/LESSONS.md`, `AGENTS.md`에서 `` `docs/LESSONS.md` `` 행을 지우고 `[000] LESSONS가 없던 옛 셋업으로 되돌린다`로 커밋한다(`a4d2a8d`). 사용법 줄과 머리 주석도 더했다 (`~/plate-rail-test/bin/vfmake.sh`)
- `run-oldsetup`에서 `/plate:run 001`을 헤드리스로 한 턴 돌렸다: `zsh bin/run.sh claude run-oldsetup run run-oldsetup answers/run-vrule.md` → 126초, exit 0. run이 `task/001-gitignore`를 만들어 바꾸고 검증을 맡겼고, 검증이 판정 통과로 `[001] 검증`(`027e830`)을 커밋한 뒤 run이 LESSONS의 위치를 묻고 멈췄다 (`~/plate-rail-test/logs/run-oldsetup.jsonl`)

## 확인 결과
- 완료 조건 4: run의 "`docs/LESSONS.md`" 절에 두 규칙이 있다
  - `plugins/plate/skills/run/SKILL.md`의 "`docs/LESSONS.md`" 절을 읽었다 → "옮기는 것"에 "옮길 줄과 같은 뜻의 줄이 `docs/LESSONS.md`의 같은 절에 이미 있으면 더하지 않는다. 회고 절에서 옮길 때도 검증 절에서 옮길 때도, 이미 있는 줄을 다른 작업에서 옮겼어도 같다."가 있고, "문서 지도"에 표 위의 글에 "하네스의 스킬이 위치를 정해 둔 기록은 묻지 않고"가 없으면 위치를 묻고, `docs/LESSONS.md`를 추천안으로 내고, setup을 다시 돌리면 다음부터 묻지 않는다고 알린다는 글이 있다. 통과
- 완료 조건 5: "검증을 맡긴다"의 첫 갈래
  - `grep -n '"통과하면"의 4번으로 간다' plugins/plate/skills/run/SKILL.md` → 출력 없음(종료 코드 1). 통과
  - "검증을 맡긴다"를 읽었다 → 162행 "닫힌 검증이면 맡기지 않고 아래 "통과하면"의 1번부터 한다."와 이미 옮긴 줄은 다시 더하지 않고 지울 파일·고친 파일이 없으면 지나간다는 글이 있다. 통과
- 완료 조건 6: 옛 셋업에서 묻고 멈춘다
  - `~/plate-rail-test/logs/run-oldsetup.jsonl`의 마지막 답글(`bin/summ.py`로 읽음) → "회고 기록 문서를 어디에 만들까요?"로 위치를 묻고, "추천: `docs/LESSONS.md`"를 내고, "`plate:setup`을 다시 돌리면 다음부터는 이 위치를 묻지 않아요"라고 알리고 멈췄다. 통과
  - `ls ~/plate-rail-test/run-oldsetup/docs/` → `ADR.md ARCHITECTURE.md PRD.md tasks`. `LESSONS.md`가 없다. 통과
  - `grep -c 'LESSONS' ~/plate-rail-test/run-oldsetup/AGENTS.md` → `0`. 통과
  - `run-oldsetup`에서 `git show --stat --format=%s HEAD` → `[001] 검증`, `docs/tasks/001-gitignore/verify.md`만 든다(24줄 더함). 통과
  - `test ~/plate-rail-test/logs/run-oldsetup.jsonl -nt plugins/plate/skills/run/SKILL.md -a ~/plate-rail-test/logs/run-oldsetup.jsonl -nt plugins/plate/skills/verify/SKILL.md && echo 새것` → `새것`. 통과

## 계획과 달라진 점
없음

## 남은 것
없음

## 하네스에서 걸린 것
- `~/plate-rail-test`는 git 레포가 아니라서 이 phase에서 고친 `bin/vfmake.sh`와 새로 생긴 `run-oldsetup`, `logs/run-oldsetup.*`는 커밋에 넣지 못했다. 커밋에는 `plugins/plate/skills/run/SKILL.md`와 이 파일만 든다.
- `run-oldsetup`의 바탕인 `vrule-base`는 LESSONS를 이 작업(001)의 `[001] phase 1 통과`(`4aa1686`)에서 만든 상태라, 그것을 지운 `a4d2a8d`를 검증이 "작업 밖의 커밋이 작업의 변경을 되돌렸다"는 하네스의 문제점으로 적었다(`run-oldsetup/docs/tasks/001-gitignore/verify.md`). 시험 폴더를 만든 방식에서 나온 줄이고, 사용자가 위치에 답하면 run이 이 줄도 LESSONS로 옮긴다.
- 같은 검증이 "작업의 커밋"의 메시지 기준이 `[001] …` 아래에서 하나도 맞지 않는다는 줄을 다시 적었다. phase 1이 고친 정의(작업 폴더의 파일을 바꾼 커밋도 든다)로 빠진 커밋은 없었다고 함께 적었다.
