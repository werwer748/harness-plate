# LESSONS의 하네스의 문제점 해결

## 요청
문제점 해결하자

## 목표
`docs/LESSONS.md`의 하네스의 문제점 17개가 스킬 본문(plan, run, verify, retro)에 반영되거나 그대로 두기로 정해져 LESSONS에서 지워지고, run이 닫힌 검증을 다시 만나도 LESSONS로 옮기기를 건너뛰지 않는다. 두 매니페스트의 버전이 0.8.1이다.

## 범위 밖
- `docs/LESSONS.md`의 프로젝트에서 배운 것 절과, run 결함을 뺀 미룬 문제 다섯
- run을 번호 없이 부를 때, 검증은 닫혔지만 LESSONS로 옮기지 않은 작업을 찾는 것
- 옛 셋업 한 경우 말고 다른 판정 경우를 다시 돌리거나 판정 도구(`runcheck.py` 등)의 기대를 고치는 것. 옛 셋업을 바탕으로 한 run-vfix, run-nogit은 다시 돌리면 LESSONS를 처음 만들 때 멈추고 묻는다

## 완료 조건
1. verify와 retro의 4번에, 하네스의 문제점은 그 스킬을 따르며 직접 읽거나 돌려서 본 것만 적는다는 규칙이 있다. 다른 스킬의 본문은 열지 않고 이름으로만 가리키며, 읽지 않은 파일이나 그 스킬 밖의 하네스 동작(예: 실행 스킬이 검증 뒤에 하는 일)은 짐작해 적지 않는다.
   - 확인: `plugins/plate/skills/verify/SKILL.md`와 `plugins/plate/skills/retro/SKILL.md`의 4번을 읽는다 → 두 곳 모두 직접 본 것만 적는다, 다른 스킬의 본문을 열지 않는다, 짐작해 적지 않는다는 세 가지가 있다
2. verify의 "작업의 커밋"이 작업 폴더의 파일을 바꾼 커밋과 메시지가 작업 폴더의 이름으로 시작하는 커밋이다. 메시지가 다른 작업 폴더의 이름으로 시작하는 커밋은 빼지 않고, 그 커밋에서는 이 작업 폴더의 변경만 본다. 수행·회고·통과·검증의 커밋은 작업 폴더의 파일을 함께 바꾸므로 메시지가 프로젝트의 꼴이어도 든다는 것이 정의에 적혀 있다.
   - 확인: `grep -n '다른 작업 폴더의 이름으로 시작하는 커밋은 뺀다' plugins/plate/skills/verify/SKILL.md` → 출력 없음
   - 확인: `plugins/plate/skills/verify/SKILL.md`의 낱말 "작업의 커밋"과 1번, 3번을 읽는다 → 다른 작업의 커밋은 이 작업 폴더의 변경만 보고, 메시지가 프로젝트의 꼴인 커밋도 작업 폴더의 파일로 잡힌다고 적혀 있다
3. plan의 "적는 규칙"에 두 규칙이 있다. 남은 결과(시험 폴더의 상태, 실행 기록처럼 앞서 만든 결과)를 읽는 확인에는, 그 결과를 만든 뒤에 그 결과에 걸리는 파일이 바뀌지 않았는지 보는 명령을 함께 적는다. 앞 phase가 이룬 완료 조건에 걸리는 파일을 뒤 phase가 고치면, 뒤 phase의 통과 조건이 그 완료 조건도 번호로 가리킨다.
   - 확인: `plugins/plate/skills/plan/SKILL.md`의 "적는 규칙"을 읽는다 → 두 규칙이 있다
4. run의 "`docs/LESSONS.md`" 절에 두 규칙이 있다. 옮길 줄과 같은 뜻의 줄이 LESSONS의 같은 절에 이미 있으면 더하지 않는다(회고 절과 검증 절에서 옮길 때 모두, 다른 작업에서 옮긴 줄과 겹칠 때도). 문서 지도 위의 글에 "하네스의 스킬이 위치를 정해 둔 기록은 묻지 않고"가 없는 프로젝트에서 LESSONS를 처음 만들 때는 위치를 묻고, `docs/LESSONS.md`를 추천안으로 내며, setup을 다시 돌리면 다음부터 묻지 않는다고 함께 알린다.
   - 확인: `plugins/plate/skills/run/SKILL.md`의 "`docs/LESSONS.md`" 절을 읽는다 → 두 규칙이 있다
5. run "검증을 맡긴다"의 첫 갈래가, 닫힌 검증이면 맡기지 않고 "통과하면"의 1번부터 한다. 1~3을 다시 해도 이미 옮긴 줄은 완료 조건 4의 규칙으로 겹치지 않고, 지울 파일이나 고친 파일이 없으면 그냥 지나간다.
   - 확인: `grep -n '"통과하면"의 4번으로 간다' plugins/plate/skills/run/SKILL.md` → 출력 없음
   - 확인: `plugins/plate/skills/run/SKILL.md`의 "검증을 맡긴다"를 읽는다 → 닫힌 검증이면 "통과하면"의 1번부터 한다
6. 옛 셋업이고 `docs/LESSONS.md`가 없는 프로젝트에서 run이 LESSONS로 옮길 줄을 처음 얻으면, 검증이 `verify.md`를 커밋한 뒤 LESSONS를 만들기 전에 위치를 묻고, `docs/LESSONS.md`를 추천안으로 내며, setup을 다시 돌리면 다음부터 묻지 않는다고 알리고 멈춘다. 그때 `docs/LESSONS.md`도 문서 지도의 LESSONS 행도 없다. 시험 폴더는 `~/plate-rail-test/run-oldsetup`(`vrule-base`에 `docs/LESSONS.md`와 문서 지도의 LESSONS 행을 지운 커밋을 얹은 것)이다. `AGENTS.md`에 커밋 메시지 꼴 규칙이 있어 검증이 "프로젝트의 규칙을 따름" 줄을 적으므로, 옮길 줄이 반드시 생긴다. 거기서 `/plate:run 001`을 헤드리스로 한 턴 돌린다.
   - 확인: `~/plate-rail-test/logs/run-oldsetup.jsonl`의 마지막 답글을 읽는다 → LESSONS의 위치를 묻고, `docs/LESSONS.md`를 추천안으로 내고, setup을 다시 돌리면 다음부터 묻지 않는다고 알린다
   - 확인: `ls ~/plate-rail-test/run-oldsetup/docs/` → `LESSONS.md`가 없다
   - 확인: `grep -c 'LESSONS' ~/plate-rail-test/run-oldsetup/AGENTS.md` → 0
   - 확인: `run-oldsetup`에서 `git show --stat --format=%s HEAD` → 메시지가 `[001]`로 시작하고 `docs/tasks/001-gitignore/verify.md`만 든다
   - 확인: `test ~/plate-rail-test/logs/run-oldsetup.jsonl -nt plugins/plate/skills/run/SKILL.md -a ~/plate-rail-test/logs/run-oldsetup.jsonl -nt plugins/plate/skills/verify/SKILL.md && echo 새것` → `새것`
7. `docs/LESSONS.md`에서 하네스의 문제점 절에 있던 17줄과, 미룬 문제 절의 run "검증을 맡긴다" 첫 갈래 줄이 지워졌다. 다른 줄은 그대로다.
   - 확인: `git diff 1f8e2ab -- docs/LESSONS.md | grep '^-- '` → 18줄이고, 하네스의 문제점 절에 있던 17줄과 미룬 문제 절의 `(006-verify, 검증 1) run 본문 "검증을 맡긴다"의 첫 갈래는 …` 줄이다
8. 두 매니페스트의 버전이 0.8.1이다.
   - 확인: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "0.8.1",`

## 결정
- 다루는 것은 `docs/LESSONS.md`의 하네스의 문제점 17개다. 이유: 요청의 "문제점"은 처음부터 그 절을 가리켰다.
- 004-context-rules 검증 1의 "결정과 완료 조건 4가 다른 범위를 본다", 006-verify phase 6의 "지워진 phase 파일에 기댄 TODO", 006-verify 검증 1의 "완료 조건 12의 확인이 일부만 본다"와 "완료 조건 4의 확인 명령이 돌지 않는다"는 본문을 고치지 않는다. 이유: plan의 "조건의 일부만 보는 확인" 규칙, "다른 phase의 파일에 적힌 글에 기대지 않는다", phase 스킬의 "계획이 틀림"이 이미 막는다. 004의 계획은 그 규칙이 생기기 전에 쓰였고, 006은 규칙을 어겼거나 세션이 phase를 직접 수행했다.
- 006-verify phase 2의 "고칠 phase의 TODO가 문제 하나에 항목 하나라 원인 하나가 TODO 셋이 된다"는 고치지 않는다. 이유: 항목마다 고쳐졌는지 따로 체크되고, 원인을 가르는 판단을 조율만 하는 run에 지우지 않는다. 틀린 결과는 없었다. (추천안으로 정함)
- 006-verify phase 3의 "고치는 방법 둘을 TODO에 옮기고 선택지를 더해 물음"과 phase 5의 "고칠 phase의 안 뒤에 안내를 덧붙임"은 고치지 않는다. 이유: 지금 상태로 충분하고 문제가 없으면, 더 빡빡한 규칙보다 자유도를 주는 쪽이 낫다.
- 006-verify phase 4의 "setup이 견주려고 프로젝트 밖에 쓰려 함"은 고치지 않는다. 이유: 막는 규칙("다른 파일은 만들지도 고치지도 않는다")이 이미 있고, 쓰기는 권한에 막혔고, 결과 파일은 틀리지 않았다.
- 미룬 문제 가운데 run "검증을 맡긴다" 첫 갈래의 결함을 함께 고친다. 이유: 옛 셋업에서 LESSONS의 위치를 묻고 멈추는 자리가 바로 그 결함이 나는 자리다.
- 버전은 0.8.1로 올린다. 이유: 스킬의 동작이 바뀌고, 1.0이 다가와 버전 관리를 철저히 한다.
