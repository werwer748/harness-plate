# Phase 5: 검증 2의 문제를 고친다

**목표**: 검증 2에서 나온 문제를 모두 고친다.

**읽을 것**
- `docs/tasks/007-harness-issues/verify.md`의 `## 검증 2` 절
- `plugins/plate/skills/run/SKILL.md`

**TODO**
- [x] run 본문 "`docs/LESSONS.md`" 절의 "문서 지도"(273행)는 옛 셋업에서 LESSONS를 처음 만들기 전에 위치를 묻고 `docs/LESSONS.md`를 추천안으로 내지만, 사용자가 추천안이 아닌 위치를 답했을 때 무엇을 하는지는 본문에 없다. 본문의 나머지는 그 문서를 모두 `docs/LESSONS.md`로 가리킨다: 절대 규칙 5(20행)가 직접 고치는 파일을 `docs/LESSONS.md`로 한정하고, 6번(129, 131행), "통과하면"(177, 179행), 같은 뜻의 줄을 거르는 247행, 이미 옮겼는지 보는 248행의 `git log -S'(NNN-slug, 검증 ' -- docs/LESSONS.md`, 지도에 더할 행(276행)이 모두 그 경로다. 그래서 다른 위치를 고르면 run은 절대 규칙 5로 그 파일을 고치지 못하고, 적힌 대로 따르면 지도에 더하는 행이 고른 위치를 가리키지 않으며, 248행의 명령은 고른 위치의 이력을 보지 않아 이 작업이 막은 "옮긴 뒤 지운 줄이 돌아온다"가 그 프로젝트에서는 다시 난다. 다시 돌린 `run-oldsetup`의 물음도 "다른 위치가 좋으면 그 경로를 알려 주세요"라고 다른 답을 청했다(`~/plate-rail-test/logs/run-oldsetup.jsonl`) (`plugins/plate/skills/run/SKILL.md` 20행, 273행)

**통과 조건**
- 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다

## 한 일
- run 본문 "`docs/LESSONS.md`" 절의 "문서 지도"(273행)가 추천안이 아닌 위치를 답했을 때 무엇을 하는지 없다는 문제: 273행의 끝에 사용자가 다른 위치를 정하면 그 위치에 만들고 지도에 더할 행의 위치 칸에 그 위치를 적는다는 것, 그 뒤로는 문서 지도에서 내용 칸이 "회고에서 배운 것, 하네스의 문제점, 미룬 문제"인 행의 위치가 이 문서이고 이 스킬에 `docs/LESSONS.md`로 적힌 곳(절대 규칙 5, 6번, "통과하면", "옮기는 것"과 그 `git log -S` 명령의 경로)은 모두 그 위치로 읽는다는 것을 더했다. 절대 규칙 5(20행)의 `docs/LESSONS.md` 뒤에 "(옛 셋업에서 사용자가 다른 위치를 정했으면 그 파일)"을 더했다 (`plugins/plate/skills/run/SKILL.md`)
- 완료 조건 6의 실행 기록이 고친 run 본문보다 새것이어야 하므로 시험 폴더를 실행 전 상태로 되돌리고 다시 돌렸다: `~/plate-rail-test/run-oldsetup`에서 `git switch main`, `git branch -D task/001-gitignore`로 `bddcdfe`(main, 작업 브랜치 없음, 앞 실행의 `logs/run-oldsetup.base`와 reflog로 확인)로 되돌린 뒤 `zsh bin/run.sh claude run-oldsetup run run-oldsetup answers/run-vrule.md`(프롬프트 `/plate:run 001`) → `run-oldsetup exit=0 secs=282` (`~/plate-rail-test/logs/run-oldsetup.jsonl`)

## 확인 결과
- 머리의 완료 조건이 모두 참이다.
  - 완료 조건 1: `plugins/plate/skills/verify/SKILL.md`와 `plugins/plate/skills/retro/SKILL.md`의 4번에서 세 구절을 grep → 두 곳 모두 "이번 검증(회고)에서 직접 읽거나 돌려서 본 것만 적는다", "다른 스킬의 본문은 열지 않고 이름으로만 가리킨다", "… 짐작해 적지 않는다"가 있다. 통과
  - 완료 조건 2: `grep -n '다른 작업 폴더의 이름으로 시작하는 커밋은 뺀다' plugins/plate/skills/verify/SKILL.md` → 출력 없음(종료 코드 1). 통과
  - 완료 조건 2: verify 본문의 "작업의 커밋"(28행), 1번(41행), 3번(52행)을 읽음 → 28행에 프로젝트의 꼴(`[001] …`)이어도 작업 폴더의 파일을 바꾼 커밋은 들고 다른 작업 폴더의 이름으로 시작하는 커밋은 빼지 않고 이 작업 폴더의 변경만 본다는 것, 41행과 52행에 그 커밋에서는 이 작업 폴더의 변경만 읽고 모은다는 것이 있다. 통과
  - 완료 조건 3: `plugins/plate/skills/plan/SKILL.md`의 "적는 규칙"을 읽음 → 남은 결과를 읽는 확인에 결과를 만든 뒤 걸리는 파일이 바뀌지 않았는지 보는 명령을 함께 적는다는 항목과, 앞 phase가 이룬 완료 조건에 걸리는 파일을 뒤 phase가 고치면 뒤 phase의 통과 조건이 그 완료 조건도 번호로 가리킨다는 항목이 있다. 통과
  - 완료 조건 4: run 본문 "`docs/LESSONS.md`" 절을 읽음 → 247행에 같은 뜻의 줄이 같은 절에 이미 있으면 더하지 않는다(회고 절·검증 절, 다른 작업에서 옮긴 줄도)는 규칙, 273행에 "하네스의 스킬이 위치를 정해 둔 기록은 묻지 않고"가 없는 프로젝트에서는 처음 만들기 전에 위치를 묻고 `docs/LESSONS.md`를 추천안으로 내며 `plate:setup`을 다시 돌리면 다음부터 묻지 않는다고 알린다는 규칙이 있다. 통과
  - 완료 조건 5: `grep -n '"통과하면"의 4번으로 간다' plugins/plate/skills/run/SKILL.md` → 출력 없음(종료 코드 1). 통과
  - 완료 조건 5: run 본문 "검증을 맡긴다"를 읽음 → 162행 "닫힌 검증이면 맡기지 않고 아래 "통과하면"의 1번부터 한다"와, 이미 옮긴 줄은 다시 더하지 않고 지울 파일이나 고친 파일이 없으면 그 번호는 지나간다는 글이 있다. 통과
  - 완료 조건 6: `~/plate-rail-test/logs/run-oldsetup.jsonl`의 마지막 답글(메인의 마지막 assistant 글과 result 줄, success 278964ms)을 읽음 → 검증 통과를 알린 뒤 "**회고 문서를 어디에 만들까요?**"로 위치를 묻고, "추천: `docs/LESSONS.md`"를 내고, "plate의 setup 스킬(`plate:setup`)을 다시 돌리면 다음부터는 묻지 않습니다"라고 알리고 멈췄다. "다른 위치를 정하셔도 됩니다. 정한 위치를 문서 지도에 한 행으로 더하고 거기에 만듭니다"도 있다. init 줄의 plate는 `/Users/gangjungi/Desktop/harness-plate/plugins/plate`(0.8.1)에서 실렸다(2.1.301). 통과
  - 완료 조건 6: `ls ~/plate-rail-test/run-oldsetup/docs/` → `ADR.md ARCHITECTURE.md PRD.md tasks`. `LESSONS.md`가 없다. 통과
  - 완료 조건 6: `grep -c 'LESSONS' ~/plate-rail-test/run-oldsetup/AGENTS.md` → `0`. 통과
  - 완료 조건 6: `run-oldsetup`에서 `git show --stat --format=%s HEAD` → `[001] 검증`, `docs/tasks/001-gitignore/verify.md`만 든다(24줄 더함). 통과
  - 완료 조건 6: `test ~/plate-rail-test/logs/run-oldsetup.jsonl -nt plugins/plate/skills/run/SKILL.md -a ~/plate-rail-test/logs/run-oldsetup.jsonl -nt plugins/plate/skills/verify/SKILL.md && echo 새것` → `새것`(기록 16:45:43, run 본문 16:40:53, verify 본문 15:17:23). 통과
  - 완료 조건 7: `git diff 1f8e2ab -- docs/LESSONS.md | grep '^-- '` → 18줄. `1f8e2ab`의 하네스의 문제점 절에 있던 17줄(그 절의 항목 수도 17)과 미룬 문제 절의 `(006-verify, 검증 1) run 본문 "검증을 맡긴다"의 첫 갈래는 …` 줄이다. 같은 diff에서 `^-`로 시작하는 줄(`---` 빼고)도 18줄이라 다른 줄은 지워지지 않았다. 통과
  - 완료 조건 8: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "0.8.1",`. 통과

## 계획과 달라진 점
- 없음

## 남은 것
- 없음

## 하네스에서 걸린 것
- TODO는 문제만 옮기고 고치는 방향(다른 위치를 받아들인다 / `docs/LESSONS.md`만 허용한다)을 적지 않았다. 옛 셋업의 `AGENTS.md` 규칙이 "정한 위치를 이 표에 한 행으로 더한 뒤 만든다"이고 완료 조건 4가 위치를 묻게 하므로, 다른 위치를 받아들이는 쪽만 머리와 맞는다고 보고 진행했다.
- 통과 조건이 완료 조건 6을 가리켜서, run 본문을 고친 이 phase는 시험 폴더를 되돌리고 헤드리스 실행을 다시 돌려야 했다. 되돌리는 방법은 계획에도 시험 도구(`bin/rerun.sh`에 `run-oldsetup` 경우가 없다)에도 없어, 앞 실행의 `logs/run-oldsetup.base`와 시험 폴더의 reflog로 실행 전 상태(main의 `bddcdfe`, 작업 브랜치 없음)를 찾았다.
