# Phase 4: 검증 1의 문제를 고친다

**목표**: 검증 1에서 나온 문제를 모두 고친다.

**읽을 것**
- `docs/tasks/007-harness-issues/verify.md`의 `## 검증 1` 절
- `plugins/plate/skills/run/SKILL.md`

**TODO**
- [x] run 본문 0번의 worktree 갈래는 원래 자리에서 부르면 worktree 안의 작업 폴더에 닫힌 검증이 있을 때 바로 "합친다"로 가고, "합친다"는 `docs/LESSONS.md`로 옮기지 않는다. worktree의 세션에서 검증 에이전트가 `verify.md`를 커밋한 뒤 run이 "통과하면"의 1~3을 하기 전에 끊기고 원래 자리에서 `/plate:run NNN`을 부르면, 검증 절의 줄을 옮기지 않은 채 합치고 worktree와 브랜치를 지운다. 머리의 목표 "run이 닫힌 검증을 다시 만나도 LESSONS로 옮기기를 건너뛰지 않는다"가 이 갈래에서는 이뤄지지 않았다 (`plugins/plate/skills/run/SKILL.md` 49~51행)
- [x] run 본문 "검증을 맡긴다"의 첫 갈래는 앞 세션이 1~3을 이미 했어도 "통과하면"의 1번부터 다시 옮기고, 이미 옮긴 줄인지는 `docs/LESSONS.md`의 같은 절에 같은 뜻의 줄이 있는지로만 가린다(247행). 그래서 옮긴 뒤 LESSONS에서 지운 줄은 다시 더해진다. 이 레포에서 지금 `/plate:run 006`을 부르면 이 작업이 완료 조건 7로 지운 `(006-verify, 검증 1)` 하네스의 문제점 세 줄과, 이 작업이 고친 첫 갈래의 결함을 적은 미룬 문제 한 줄이 LESSONS에 돌아오고, `/plate:run 004`를 부르면 `(004-context-rules, 검증 1)` 하네스의 문제점 세 줄이 돌아온다. 같은 162행의 "이미 옮긴 줄은 다시 더하지 않고"와 어긋난다 (`plugins/plate/skills/run/SKILL.md` 162행, 247행)

**통과 조건**
- 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다

## 한 일
- run 본문 0번의 worktree 갈래는 원래 자리에서 부르면 worktree 안의 작업 폴더에 닫힌 검증이 있을 때 바로 "합친다"로 가고, "합친다"는 `docs/LESSONS.md`로 옮기지 않는다 …: 0번의 첫 갈래를 "그 worktree에서 "통과하면"의 1~3을 한 뒤 "합친다"로 간다"로 바꾸고, 고치는 파일은 worktree 안의 것이고 커밋도 worktree에서 한다(`git -C .worktrees/NNN-slug`)는 것과 까닭(worktree의 세션이 검증 뒤에 끊겼어도 옮기지 않은 채 합치지 않게)을 적었다. 이미 옮겼으면 아래 둘째 항목의 규칙으로 지나간다 (`plugins/plate/skills/run/SKILL.md` 51행)
- run 본문 "검증을 맡긴다"의 첫 갈래는 앞 세션이 1~3을 이미 했어도 "통과하면"의 1번부터 다시 옮기고 …: "`docs/LESSONS.md`" 절의 "옮기는 것"에 "마지막 검증 절을 더한 커밋 뒤에 `docs/LESSONS.md`를 바꾼 커밋이 있으면 검증 절의 줄(미룬 문제도)은 이미 옮긴 것이라 옮기지 않는다, git 레포가 아니면 `docs/LESSONS.md`가 `verify.md`보다 나중에 바뀌었는지로 본다"를 더했다. 첫 갈래의 "1번부터 한다"는 그대로 두고, 1번이 이 규칙으로 지나간다. 이 레포에서 `git log --oneline 308d622..HEAD -- docs/LESSONS.md`(006의 검증 커밋 뒤)와 `git log --oneline b660382..HEAD -- docs/LESSONS.md`(004의 검증 커밋 뒤)가 모두 `1f8e2ab` 등을 내므로, 지금 `/plate:run 006`이나 `/plate:run 004`를 불러도 지운 줄이 돌아오지 않는다 (`plugins/plate/skills/run/SKILL.md` 248행)
- run 본문을 고쳐 완료 조건 6의 마지막 확인이 실패하므로 시험을 다시 돌렸다: `zsh bin/vfmake.sh run-oldsetup`(`5b8bfbc [000] LESSONS가 없던 옛 셋업으로 되돌린다`) 뒤 `zsh bin/run.sh claude run-oldsetup run run-oldsetup answers/run-vrule.md` → 175초, exit 0 (`~/plate-rail-test/run-oldsetup`, `~/plate-rail-test/logs/run-oldsetup.jsonl`)

## 확인 결과
- 머리의 완료 조건이 모두 참이다.
  - 완료 조건 1: `plugins/plate/skills/verify/SKILL.md` 63행과 `plugins/plate/skills/retro/SKILL.md` 62행의 4번을 읽음 → 두 곳 모두 "이번 검증(회고)에서 직접 읽거나 돌려서 본 것만 적는다", "다른 스킬의 본문은 열지 않고 이름으로만 가리킨다", "읽지 않은 파일과 이 스킬 밖의 하네스 동작(예: 실행 스킬이 검증(회고) 뒤에 하는 일)은 짐작해 적지 않는다"가 있다. 통과
  - 완료 조건 2: `grep -n '다른 작업 폴더의 이름으로 시작하는 커밋은 뺀다' plugins/plate/skills/verify/SKILL.md` → 출력 없음(종료 코드 1). 통과
  - 완료 조건 2: verify 본문의 낱말 "작업의 커밋"(28행), 1번(41행), 3번(52행)을 읽음 → 수행·회고·통과·검증의 커밋은 메시지가 프로젝트의 꼴(예: `[001] …`)이어도 들고, 다른 작업 폴더의 이름으로 시작하는 커밋은 빼지 않고 이 작업 폴더의 변경만 본다/읽는다/모은다. 통과
  - 완료 조건 3: `plugins/plate/skills/plan/SKILL.md`의 "적는 규칙"을 읽음 → 174행(남은 결과를 읽는 확인에 결과를 만든 뒤 걸리는 파일이 바뀌지 않았는지 보는 명령을 함께 적는다)과 179행(앞 phase가 이룬 완료 조건에 걸리는 파일을 뒤 phase가 고치면 뒤 phase의 통과 조건이 그 완료 조건도 번호로 가리킨다)이 있다. 통과
  - 완료 조건 4: run 본문 "`docs/LESSONS.md`" 절을 읽음 → 247행(같은 뜻의 줄이 같은 절에 있으면 더하지 않는다, 회고 절·검증 절·다른 작업의 줄 모두)과 273행(표 위의 글에 "하네스의 스킬이 위치를 정해 둔 기록은 묻지 않고"가 없으면 처음 만들기 전에 위치를 묻고 멈춘다, `docs/LESSONS.md`를 추천안으로 낸다, `plate:setup`을 다시 돌리면 다음부터 묻지 않는다고 알린다)이 있다. 통과
  - 완료 조건 5: `grep -n '"통과하면"의 4번으로 간다' plugins/plate/skills/run/SKILL.md` → 출력 없음(종료 코드 1). 통과
  - 완료 조건 5: run 본문 "검증을 맡긴다"를 읽음 → 162행 "닫힌 검증이면 맡기지 않고 아래 "통과하면"의 1번부터 한다. 앞 세션이 1~3을 이미 했어도 같다."가 있다. 통과
  - 완료 조건 6: `~/plate-rail-test/logs/run-oldsetup.jsonl`의 마지막 답글(메인의 마지막 assistant 글과 result 줄)을 읽음 → 검증 판정 통과를 보인 뒤 "**회고 문서를 어디에 만들까요?**"로 위치를 묻고, "**추천: `docs/LESSONS.md`**"를 내고, "`plate:setup`을 다시 돌리면 문서 지도의 글이 바뀌어 다음부터는 이 위치를 묻지 않습니다"라고 알리고 "여기서 멈추고 묻습니다"로 멈췄다. init 줄의 plate는 `/Users/gangjungi/Desktop/harness-plate/plugins/plate`(0.8.1)에서 실렸다. 통과
  - 완료 조건 6: `ls ~/plate-rail-test/run-oldsetup/docs/` → `ADR.md ARCHITECTURE.md PRD.md tasks`. `LESSONS.md`가 없다. 통과
  - 완료 조건 6: `grep -c 'LESSONS' ~/plate-rail-test/run-oldsetup/AGENTS.md` → `0`. 통과
  - 완료 조건 6: `run-oldsetup`에서 `git show --stat --format=%s HEAD` → `[001] 검증`, `docs/tasks/001-gitignore/verify.md`만 든다(22줄 더함). 통과
  - 완료 조건 6: `test ~/plate-rail-test/logs/run-oldsetup.jsonl -nt plugins/plate/skills/run/SKILL.md -a ~/plate-rail-test/logs/run-oldsetup.jsonl -nt plugins/plate/skills/verify/SKILL.md && echo 새것` → `새것`(기록 16:05:38, run 본문 16:02:28, verify 본문 15:17:23). 통과
  - 완료 조건 7: `git diff 1f8e2ab -- docs/LESSONS.md | grep '^-- '` → 18줄. 하네스의 문제점 절에 있던 `(006-verify, phase 1)`~`(006-verify, phase 6)` 열하나, `(004-context-rules, 검증 1)` 셋, `(006-verify, 검증 1)` 셋과 미룬 문제 절의 `(006-verify, 검증 1) run 본문 "검증을 맡긴다"의 첫 갈래는 …` 줄이다. 더한 줄은 `(007-harness-issues, phase 2)` 세 줄뿐이다. 통과
  - 완료 조건 8: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "0.8.1",`. 통과

## 계획과 달라진 점
- TODO에는 run 본문만 적혀 있지만, run 본문을 고치면 완료 조건 6의 마지막 확인(실행 기록이 run 본문보다 새것)이 실패하므로 `bin/vfmake.sh run-oldsetup`으로 시험 폴더를 다시 만들고 `/plate:run 001`을 헤드리스로 다시 돌렸다. 통과 조건이 완료 조건의 확인을 모두 돌리게 하므로 그 확인을 통과시키려고 한 것이다.

## 남은 것
없음

## 하네스에서 걸린 것
- 두 TODO가 문제의 글만 옮겨 고치는 방법을 정하지 않아, 방법은 수행이 골랐다: 0번은 원래 자리에서 worktree 안의 파일을 고치고 worktree에서 커밋하는 길로, 이미 옮겼는지는 마지막 검증 절을 더한 커밋 뒤에 LESSONS를 바꾼 커밋이 있는지로. 같은 뜻의 줄이 모두 이미 있어 LESSONS가 바뀌지 않은 채 닫힌 검증은 이 기준으로 가려지지 않아, 그 뒤 LESSONS에서 그 줄을 지우면 다시 더해질 수 있다.
- 다시 돌린 `run-oldsetup`의 검증이 하네스의 문제점으로 "verify 스킬은 "작업의 커밋이 바꾼 것"과 지금의 트리가 다를 때 어느 쪽에 대어 볼지 정해 두지 않았다(`4aa1686`의 변경을 `5b8bfbc`가 되돌린 경우)"를 적었다. 시험 폴더를 만드는 `[000]` 커밋이 작업의 커밋이 만든 LESSONS를 지운 데서 온 것이다.

## 회고 1: 회고

**확인**
- 머리의 완료 조건이 모두 참이다.
  - 완료 조건 1: `plugins/plate/skills/verify/SKILL.md`와 `plugins/plate/skills/retro/SKILL.md`(62행)의 4번을 읽음 → 두 곳 모두 "직접 읽거나 돌려서 본 것만 적는다", "다른 스킬의 본문은 열지 않고 이름으로만 가리킨다", "읽지 않은 파일과 이 스킬 밖의 하네스 동작(예: 실행 스킬이 검증(회고) 뒤에 하는 일)은 짐작해 적지 않는다"가 있다. 통과
  - 완료 조건 2: `grep -n '다른 작업 폴더의 이름으로 시작하는 커밋은 뺀다' plugins/plate/skills/verify/SKILL.md` → 출력 없음(종료 코드 1). 통과
  - 완료 조건 2: verify 본문의 낱말 "작업의 커밋", 1번, 3번을 읽음 → 수행·회고·통과·검증의 커밋은 메시지가 프로젝트의 꼴(`[001] …`)이어도 들고, 다른 작업 폴더의 이름으로 시작하는 커밋은 빼지 않고 이 작업 폴더의 변경만 본다/읽는다/모은다. 통과
  - 완료 조건 3: `plugins/plate/skills/plan/SKILL.md`의 "적는 규칙"을 읽음 → 174행(남은 결과를 읽는 확인에 결과를 만든 뒤 걸리는 파일이 바뀌지 않았는지 보는 명령을 함께 적는다)과 179행(앞 phase가 이룬 완료 조건에 걸리는 파일을 뒤 phase가 고치면 그 완료 조건도 번호로 가리킨다)이 있다. 통과
  - 완료 조건 4: run 본문 "`docs/LESSONS.md`" 절을 읽음 → 247행(같은 뜻의 줄이 같은 절에 있으면 더하지 않는다. 회고 절·검증 절·다른 작업의 줄 모두)과 273행(표 위의 글에 그 구절이 없으면 처음 만들기 전에 위치를 묻고 멈추며, `docs/LESSONS.md`를 추천안으로 내고 `plate:setup`을 다시 돌리면 다음부터 묻지 않는다고 알린다)이 있다. 통과
  - 완료 조건 5: `grep -n '"통과하면"의 4번으로 간다' plugins/plate/skills/run/SKILL.md` → 출력 없음(종료 코드 1). 통과
  - 완료 조건 5: run 본문 "검증을 맡긴다"를 읽음 → 162행 "닫힌 검증이면 맡기지 않고 아래 "통과하면"의 1번부터 한다. 앞 세션이 1~3을 이미 했어도 같다."가 있다. 통과
  - 완료 조건 6: `~/plate-rail-test/logs/run-oldsetup.jsonl`의 메인 마지막 assistant 글과 result 줄을 읽음 → "**회고 문서를 어디에 만들까요?**"로 묻고, "**추천: `docs/LESSONS.md`**"를 내고, "`plate:setup`을 다시 돌리면 문서 지도의 글이 바뀌어 다음부터는 이 위치를 묻지 않습니다"라고 알리고 멈췄다. init 줄의 plate는 `/Users/gangjungi/Desktop/harness-plate/plugins/plate`(0.8.1)다. 통과
  - 완료 조건 6: `ls ~/plate-rail-test/run-oldsetup/docs/` → `ADR.md ARCHITECTURE.md PRD.md tasks`. 통과
  - 완료 조건 6: `grep -c 'LESSONS' ~/plate-rail-test/run-oldsetup/AGENTS.md` → `0`. 통과
  - 완료 조건 6: `git -C ~/plate-rail-test/run-oldsetup show --stat --format=%s HEAD` → `[001] 검증`, `docs/tasks/001-gitignore/verify.md`만 든다(22줄 더함). 통과
  - 완료 조건 6: `test … -nt … -a … -nt … && echo 새것` → `새것`(기록 16:05:38, run 본문 16:02:28, verify 본문 15:17:23). 통과
  - 완료 조건 7: `git diff 1f8e2ab -- docs/LESSONS.md | grep '^-- '` → 18줄. 하네스의 문제점 절의 17줄과 미룬 문제 절의 `(006-verify, 검증 1) run 본문 "검증을 맡긴다"의 첫 갈래는 …` 줄이다. 더한 줄은 `(007-harness-issues, phase 2)` 세 줄뿐이다. 통과
  - 완료 조건 8: `grep -h '"version"' …` → 두 줄 모두 `"version": "0.8.1",`. 통과

**문제**
- 248행에 더한 기준("마지막 검증 절을 더한 커밋 뒤에 `docs/LESSONS.md`를 바꾼 커밋이 있으면 검증 절의 줄은 이미 옮긴 것이라 옮기지 않는다")은 이 작업의 줄을 옮겼는지가 아니라 LESSONS가 바뀌었는지를 본다. 검증 에이전트가 `verify.md`를 커밋한 뒤 run이 "통과하면"의 1~3을 하기 전에 세션이 끊기고, 다시 부르기 전에 그 브랜치에서 다른 작업의 phase 통과나 손으로 고친 커밋이 LESSONS를 바꾸면, 다시 부른 run은 옮기지 않은 검증 절의 줄을 건너뛴다. git 레포가 아니면 그 사이에 LESSONS가 고쳐지기만 해도 같다. 이 레포에서도 `git log --oneline b660382..HEAD -- docs/LESSONS.md`에 004의 검증 커밋 뒤의 다른 작업 커밋(`0def138 006-verify: phase 5 통과`, `04418fa 006-verify: phase 6 통과`)이 든다. 머리의 목표 "run이 닫힌 검증을 다시 만나도 LESSONS로 옮기기를 건너뛰지 않는다"와 51행의 까닭(세션이 끊겼어도 옮기지 않은 채 합치지 않게)에 어긋난다. 이 phase의 "하네스에서 걸린 것"이 적은 경우(같은 뜻의 줄이 이미 있어 LESSONS가 바뀌지 않음)는 그 줄을 LESSONS에서 지운 커밋이 뒤의 LESSONS 커밋이 되어 가려진다 (`plugins/plate/skills/run/SKILL.md` 248행). 기준: 결함

**배운 것**
- 0번의 worktree 갈래에 더한 `git -C .worktrees/NNN-slug` 커밋은 `docs/TOOLS.md`가 원래 자리의 세션에서 막힌다고 적은 꼴이다("`git -C <worktree> status`도 `cd <worktree> && git status`도 막힌다", "`-C`를 붙인 꼴은 읽기만 하는 명령이어도 승인을 요구했다"). 이 갈래를 돌리는 확인은 완료 조건에 없다.
- 이 회고 에이전트가 `plate:retro`를 불러 받은 본문은 디스크의 `plugins/plate/skills/retro/SKILL.md`와 달랐다. 4번에 phase 1이 더한 세 문장이 없었다. 검증 1의 배운 것(verify 본문)과 같은 일이다.

**하네스의 문제점**
- run 본문 "고칠 phase를 더한다"의 양식(189행, 201~203행)은 TODO에 검증의 문제 글만 옮기고 읽을 것에 `verify.md`의 절과 문제에 적힌 파일만 넣어, 고치는 방법은 수행이 정한다. 이번에 수행이 고른 두 방법 가운데 LESSONS 커밋의 유무로 가리는 기준은 위 문제를 낳았고, worktree에서 `git -C`로 커밋하는 방법은 읽을 것에 없던 `docs/TOOLS.md`가 막힌다고 적은 꼴이다.
- 같은 양식의 통과 조건(208~210행)은 "머리의 완료 조건이 모두 참이다" 하나라, 검증의 문제가 완료 조건 밖에서 나오면 고친 것을 보는 확인이 없다. 이번 두 TODO(0번의 worktree 갈래, 248행의 기준)가 그랬고, 완료 조건 5의 확인은 162행의 글만 본다.

**판정**: 문제 있음
