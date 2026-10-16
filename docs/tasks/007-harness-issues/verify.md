# 검증

## 검증 1

**확인**
- verify와 retro의 4번에, 하네스의 문제점은 그 스킬을 따르며 직접 읽거나 돌려서 본 것만 적는다는 규칙이 있다. 다른 스킬의 본문은 열지 않고 이름으로만 가리키며, 읽지 않은 파일이나 그 스킬 밖의 하네스 동작(예: 실행 스킬이 검증 뒤에 하는 일)은 짐작해 적지 않는다.
  - `plugins/plate/skills/verify/SKILL.md`와 `plugins/plate/skills/retro/SKILL.md`의 4번을 읽음 → 두 곳 모두 하네스의 문제점 항목 끝에 "이번 검증(회고)에서 직접 읽거나 돌려서 본 것만 적는다", "다른 스킬의 본문은 열지 않고 이름으로만 가리킨다", "읽지 않은 파일과 이 스킬 밖의 하네스 동작(예: 실행 스킬이 검증(회고) 뒤에 하는 일)은 짐작해 적지 않는다"가 있다. 통과
- verify의 "작업의 커밋"이 작업 폴더의 파일을 바꾼 커밋과 메시지가 작업 폴더의 이름으로 시작하는 커밋이다. 메시지가 다른 작업 폴더의 이름으로 시작하는 커밋은 빼지 않고, 그 커밋에서는 이 작업 폴더의 변경만 본다. 수행·회고·통과·검증의 커밋은 작업 폴더의 파일을 함께 바꾸므로 메시지가 프로젝트의 꼴이어도 든다는 것이 정의에 적혀 있다.
  - `grep -n '다른 작업 폴더의 이름으로 시작하는 커밋은 뺀다' plugins/plate/skills/verify/SKILL.md` → 출력 없음(종료 코드 1). 통과
  - `plugins/plate/skills/verify/SKILL.md`의 낱말 "작업의 커밋"(28행), 1번(41행), 3번(52행)을 읽음 → 낱말에 수행·회고·통과·검증의 커밋은 메시지가 프로젝트의 꼴(예: `[001] …`)이어도 든다는 것과 다른 작업 폴더의 이름으로 시작하는 커밋은 빼지 않고 이 작업 폴더의 변경만 본다는 것이 있고, 1번은 그런 커밋에서 이 작업 폴더의 변경만 읽고 3번은 그것만 모은다. 통과
- plan의 "적는 규칙"에 두 규칙이 있다. 남은 결과(시험 폴더의 상태, 실행 기록처럼 앞서 만든 결과)를 읽는 확인에는, 그 결과를 만든 뒤에 그 결과에 걸리는 파일이 바뀌지 않았는지 보는 명령을 함께 적는다. 앞 phase가 이룬 완료 조건에 걸리는 파일을 뒤 phase가 고치면, 뒤 phase의 통과 조건이 그 완료 조건도 번호로 가리킨다.
  - `plugins/plate/skills/plan/SKILL.md`의 "적는 규칙"(158~208행)을 읽음 → "조건"에 남은 결과를 읽는 확인에는 결과를 만든 뒤 걸리는 파일이 바뀌지 않았는지 보는 명령을 함께 적는다는 항목(174행)과, 앞 phase가 이룬 완료 조건에 걸리는 파일을 뒤 phase가 고치면 뒤 phase의 통과 조건이 그 완료 조건도 번호로 가리킨다는 항목(179행)이 있다. 통과
- run의 "`docs/LESSONS.md`" 절에 두 규칙이 있다. 옮길 줄과 같은 뜻의 줄이 LESSONS의 같은 절에 이미 있으면 더하지 않는다(회고 절과 검증 절에서 옮길 때 모두, 다른 작업에서 옮긴 줄과 겹칠 때도). 문서 지도 위의 글에 "하네스의 스킬이 위치를 정해 둔 기록은 묻지 않고"가 없는 프로젝트에서 LESSONS를 처음 만들 때는 위치를 묻고, `docs/LESSONS.md`를 추천안으로 내며, setup을 다시 돌리면 다음부터 묻지 않는다고 함께 알린다.
  - `plugins/plate/skills/run/SKILL.md`의 "`docs/LESSONS.md`" 절(236~278행)을 읽음 → "옮기는 것"의 끝(247행)에 같은 뜻의 줄이 같은 절에 있으면 더하지 않고 회고 절·검증 절에서 옮길 때와 다른 작업에서 옮긴 줄도 같다는 규칙이 있고, "문서 지도"(272행)에 그 글이 없는 프로젝트에서는 처음 만들기 전에 위치를 묻고 멈추며 `docs/LESSONS.md`를 추천안으로 내고 `plate:setup`을 다시 돌리면 다음부터 묻지 않는다고 알린다는 규칙이 있다. `plugins/plate/skills/setup/SKILL.md` 120행의 지도 위의 글에 같은 구절이 그대로 있다. 통과
- run "검증을 맡긴다"의 첫 갈래가, 닫힌 검증이면 맡기지 않고 "통과하면"의 1번부터 한다. 1~3을 다시 해도 이미 옮긴 줄은 완료 조건 4의 규칙으로 겹치지 않고, 지울 파일이나 고친 파일이 없으면 그냥 지나간다.
  - `grep -n '"통과하면"의 4번으로 간다' plugins/plate/skills/run/SKILL.md` → 출력 없음(종료 코드 1). 통과
  - `plugins/plate/skills/run/SKILL.md`의 "검증을 맡긴다"를 읽음 → 162행 "닫힌 검증이면 맡기지 않고 아래 "통과하면"의 1번부터 한다. 앞 세션이 1~3을 이미 했어도 같다."와 이미 옮긴 줄은 다시 더하지 않고 지울 파일이나 고친 파일이 없으면 지나간다는 글이 있다. 통과
- 옛 셋업이고 `docs/LESSONS.md`가 없는 프로젝트에서 run이 LESSONS로 옮길 줄을 처음 얻으면, 검증이 `verify.md`를 커밋한 뒤 LESSONS를 만들기 전에 위치를 묻고, `docs/LESSONS.md`를 추천안으로 내며, setup을 다시 돌리면 다음부터 묻지 않는다고 알리고 멈춘다. 그때 `docs/LESSONS.md`도 문서 지도의 LESSONS 행도 없다. 시험 폴더는 `~/plate-rail-test/run-oldsetup`(`vrule-base`에 `docs/LESSONS.md`와 문서 지도의 LESSONS 행을 지운 커밋을 얹은 것)이다. `AGENTS.md`에 커밋 메시지 꼴 규칙이 있어 검증이 "프로젝트의 규칙을 따름" 줄을 적으므로, 옮길 줄이 반드시 생긴다. 거기서 `/plate:run 001`을 헤드리스로 한 턴 돌린다.
  - `~/plate-rail-test/logs/run-oldsetup.jsonl`의 마지막 답글(메인의 마지막 assistant 글과 result 줄)을 읽음 → "회고 기록 문서를 어디에 만들까요?"로 위치를 묻고, "추천: `docs/LESSONS.md`"를 내고, "`plate:setup`을 다시 돌리면 다음부터는 이 위치를 묻지 않아요"라고 알리고 "여기서 멈추고 답을 기다릴게요"로 멈췄다. init 줄의 plate는 `/Users/gangjungi/Desktop/harness-plate/plugins/plate`에서 실렸다(2.1.301). 통과
  - `ls ~/plate-rail-test/run-oldsetup/docs/` → `ADR.md ARCHITECTURE.md PRD.md tasks`. `LESSONS.md`가 없다. 통과
  - `grep -c 'LESSONS' ~/plate-rail-test/run-oldsetup/AGENTS.md` → `0`. 통과
  - `run-oldsetup`에서 `git show --stat --format=%s HEAD` → `[001] 검증`, `docs/tasks/001-gitignore/verify.md`만 든다(24줄 더함). 통과
  - `test ~/plate-rail-test/logs/run-oldsetup.jsonl -nt plugins/plate/skills/run/SKILL.md -a ~/plate-rail-test/logs/run-oldsetup.jsonl -nt plugins/plate/skills/verify/SKILL.md && echo 새것` → `새것`(기록 15:25:59, run 본문 15:23:21, verify 본문 15:17:23. 두 본문은 그 뒤 커밋에서 바뀌지 않았다). 통과
- `docs/LESSONS.md`에서 하네스의 문제점 절에 있던 17줄과, 미룬 문제 절의 run "검증을 맡긴다" 첫 갈래 줄이 지워졌다. 다른 줄은 그대로다.
  - `git diff 1f8e2ab -- docs/LESSONS.md | grep '^-- '` → 18줄. 하네스의 문제점 절에 있던 `(006-verify, phase 1)`~`(006-verify, phase 6)` 열하나, `(004-context-rules, 검증 1)` 셋, `(006-verify, 검증 1)` 셋과 미룬 문제 절의 `(006-verify, 검증 1) run 본문 "검증을 맡긴다"의 첫 갈래는 …` 줄이다. 같은 diff에서 더한 줄은 phase 2의 통과(`d5a69c2`)가 옮긴 `(007-harness-issues, phase 2)` 세 줄뿐이고, 프로젝트에서 배운 것 절과 미룬 문제 절의 나머지 다섯 줄은 그대로다. 통과
- 두 매니페스트의 버전이 0.8.1이다.
  - `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "0.8.1",`. 통과

**문제**
- run 본문 0번의 worktree 갈래는 원래 자리에서 부르면 worktree 안의 작업 폴더에 닫힌 검증이 있을 때 바로 "합친다"로 가고, "합친다"는 `docs/LESSONS.md`로 옮기지 않는다. worktree의 세션에서 검증 에이전트가 `verify.md`를 커밋한 뒤 run이 "통과하면"의 1~3을 하기 전에 끊기고 원래 자리에서 `/plate:run NNN`을 부르면, 검증 절의 줄을 옮기지 않은 채 합치고 worktree와 브랜치를 지운다. 머리의 목표 "run이 닫힌 검증을 다시 만나도 LESSONS로 옮기기를 건너뛰지 않는다"가 이 갈래에서는 이뤄지지 않았다 (`plugins/plate/skills/run/SKILL.md` 49~51행). 기준: 계획
- run 본문 "검증을 맡긴다"의 첫 갈래는 앞 세션이 1~3을 이미 했어도 "통과하면"의 1번부터 다시 옮기고, 이미 옮긴 줄인지는 `docs/LESSONS.md`의 같은 절에 같은 뜻의 줄이 있는지로만 가린다(247행). 그래서 옮긴 뒤 LESSONS에서 지운 줄은 다시 더해진다. 이 레포에서 지금 `/plate:run 006`을 부르면 이 작업이 완료 조건 7로 지운 `(006-verify, 검증 1)` 하네스의 문제점 세 줄과, 이 작업이 고친 첫 갈래의 결함을 적은 미룬 문제 한 줄이 LESSONS에 돌아오고, `/plate:run 004`를 부르면 `(004-context-rules, 검증 1)` 하네스의 문제점 세 줄이 돌아온다. 같은 162행의 "이미 옮긴 줄은 다시 더하지 않고"와 어긋난다 (`plugins/plate/skills/run/SKILL.md` 162행, 247행). 기준: 결함

**배운 것**
- 이 검증 에이전트가 `plate:verify`를 불러 받은 본문은 이 작업의 phase 1(`214466b`) 전의 글이었다. 낱말 "작업의 커밋"에 "메시지가 다른 작업 폴더의 이름으로 시작하는 커밋은 뺀다"가 있었고 4번에 phase 1이 더한 세 문장이 없었다. 디스크의 `plugins/plate/skills/verify/SKILL.md`는 고친 글이다. 이번 작업의 커밋은 두 정의에서 같았다(메시지가 다른 작업 폴더의 이름으로 시작하는 커밋이 없다).
- 완료 조건 6의 마지막 확인은 `~/plate-rail-test/logs/run-oldsetup.jsonl`이 run과 verify 본문보다 새것이어야 통과한다. 고칠 phase가 둘 가운데 하나를 고치면 `bin/vfmake.sh run-oldsetup`으로 폴더를 다시 만들고 다시 돌려야 한다(돌린 꼴은 `c6ff0e6`의 `phase-2.md` "한 일"). `run-oldsetup`은 위치 물음에서 멈춘 상태라 그 물음에 답하면 완료 조건 6의 다른 확인도 바뀐다.

**하네스의 문제점**
- 계획의 완료 조건 5: 목표의 "run이 닫힌 검증을 다시 만나도"를 "검증을 맡긴다"의 첫 갈래 하나로 좁혀 적어, 같은 본문 0번의 worktree 갈래(닫힌 검증이면 "합친다"로 간다)는 어느 완료 조건의 확인도 보지 않았다.
- 계획의 완료 조건 5는 다시 옮겨도 겹치지 않는 근거를 완료 조건 4의 겹침 규칙에 두었는데, 같은 계획의 완료 조건 7은 옮긴 줄을 LESSONS에서 지운다. 두 조건은 phase 2와 phase 3에 나뉘었고 세 phase가 모두 "확인만"으로 지나, 둘이 만나는 곳은 검증에서 처음 점검됐다. phase 3이 고친 것은 run 본문이 아니라 run이 기대는 LESSONS의 내용이라, plan "적는 규칙"의 새 규칙(앞 phase가 이룬 완료 조건에 걸리는 파일을 뒤 phase가 고치면 그 완료 조건도 가리킨다)에도 걸리지 않는다.
- verify 4번의 "다른 스킬의 본문은 열지 않고 이름으로만 가리킨다"는 하네스 저장소 자신의 작업처럼 다른 스킬의 본문이 작업의 커밋이 바꾼 파일일 때를 말하지 않는다. 이번 검증은 1번("작업의 커밋이 바꾼 것 전부")을 따라 run, plan, retro의 본문을 읽었고, 위 두 문제는 그렇게 읽은 run 본문에서 나왔다.

**판정**: 문제 있음
