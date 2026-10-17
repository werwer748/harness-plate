# Phase 7: 시험으로만 닫히는 셋과 LESSONS 정리

**목표**: 시험으로만 닫히는 셋이 확인되어 `docs/TOOLS.md`에 적히고, `docs/LESSONS.md`에서 이 작업이 닫은 41줄이 지워진다.

**테스트 먼저**: 아니오 — 이 레포의 코드를 바꾸지 않고 시험을 돌리고 문서를 고친다

**읽을 것**
- `~/plate-rail-test/bin/vfmake.sh`, `bin/run.sh`, `bin/rerun.sh`
- `~/plate-rail-test/probe-plugin`과 `bin/a2.sh` (헤드리스에서 서브에이전트가 스킬을 부르는 시험의 꼴. `docs/TOOLS.md`의 "서브에이전트, 권한, worktree")
- `plugins/plate/skills/run/SKILL.md`의 3번(세 번째 막음 갈래)과 "`docs/LESSONS.md`" 절의 문서 지도(다른 위치)
- `plugins/plate/skills/phase/SKILL.md`의 2번과 적는 규칙(세 번째 막음 줄)
- `plugins/plate/hooks/edit_guard.py` (테스트 파일의 기준과 막은 횟수를 두는 곳. phase 1이 바꿨다)
- `docs/TOOLS.md`의 Claude Code 절
- code.claude.com/docs/en/skills, code.claude.com/docs/en/plugins/cli-reference (스킬 본문은 부를 때 대화에 한 번 들어가고 다시 읽히지 않는다. `/reload-plugins`는 디스크에서 고친 플러그인을 세션에 다시 싣는다)
- `git show ec2f192:docs/LESSONS.md` (지울 41줄의 원문. 하네스의 문제점 절의 (007-harness-issues, 검증 2) 줄, (008-tdd, phase 3)의 넷째 줄, (008-tdd, phase 4)의 셋째 줄, (008-tdd, 검증 1)의 둘째 줄이 이 phase가 시험으로 닫는 것이다)

**TODO**
- [x] `~/plate-rail-test/run-oldsetup`이 다시 만들어지고, `/plate:run 001`의 첫 턴이 LESSONS의 위치를 묻고 멈춘 뒤, `docs/notes/lessons.md`로 답한 둘째 턴에서 완료 조건 10대로 된다 (`~/plate-rail-test/run-oldsetup`)
- [x] `~/plate-rail-test/tdd-stop`이 완료 조건 11의 꼴로 생기고, `/plate:run`을 헤드리스로 한 턴 돌린 기록 `logs/tdd-stop.jsonl`에서 완료 조건 11대로 된다 (`~/plate-rail-test/tdd-stop`)
- [x] `probe-plugin`으로 세션 도중의 본문 고침과 `/reload-plugins`를 헤드리스로 시험한 기록이 `logs/reload-probe*.jsonl`에 있고, 그 결과(두 에이전트가 받은 본문, 돌린 명령의 꼴, 버전, 날짜)가 `docs/TOOLS.md`의 Claude Code 절에 적힌다 (`docs/TOOLS.md`)
- [x] `docs/LESSONS.md`에서 완료 조건 13의 41줄이 지워진다. 이 작업의 phase가 통과할 때 run이 더한 줄과 다른 줄은 그대로다 (`docs/LESSONS.md`)

**통과 조건**
- 완료 조건 10이 참이다.
  - 확인: 완료 조건 10의 확인을 모두 돌린다
- 완료 조건 11이 참이다.
  - 확인: 완료 조건 11의 확인을 모두 돌린다
- 완료 조건 12가 참이다.
  - 확인: 완료 조건 12의 확인을 돌린다
- 완료 조건 13이 참이다.
  - 확인: 완료 조건 13의 확인을 모두 돌린다
- 완료 조건 8이 참이다. 이 phase가 `docs/TOOLS.md`를 고친다.
  - 확인: 완료 조건 8의 확인을 모두 돌린다
- 완료 조건 15가 참이다.
  - 확인: 완료 조건 15의 확인을 돌린다

## 한 일
- `~/plate-rail-test/run-oldsetup`이 다시 만들어지고, `/plate:run 001`의 첫 턴이 LESSONS의 위치를 묻고 멈춘 뒤, `docs/notes/lessons.md`로 답한 둘째 턴에서 완료 조건 10대로 된다: `zsh bin/vfmake.sh run-oldsetup`으로 다시 만들었다(`6053561`). 첫 턴 `zsh bin/run.sh claude run-oldsetup run run-oldsetup answers/run-vrule.md` → 206초, exit 0. run이 `task/001-gitignore`로 바꾸고 검증을 맡겨 판정 통과(`fdf675a [001] 검증`)를 받은 뒤, 옮길 줄 넷을 보이며 위치를 묻고 멈췄다. 둘째 턴은 답 파일 `answers/run-oldsetup-2.md`("`docs/notes/lessons.md`에 만든다.")를 새로 쓰고 `zsh bin/run.sh claude run-oldsetup run run-oldsetup-2 answers/run-oldsetup-2.md ba85d49d-9852-41d7-84ba-b7a36b979d82` → 35초, exit 0. run이 `docs/notes/lessons.md`를 LESSONS의 양식으로 만들고, 문서 지도에 그 행을 더하고, `verify.md`에 `LESSONS로 옮겼다`를 적어 `11d110c [001] 검증 통과`로 커밋한 뒤 합칠지 묻고 멈췄다 (`~/plate-rail-test/run-oldsetup`, `~/plate-rail-test/answers/run-oldsetup-2.md`, `~/plate-rail-test/logs/run-oldsetup.jsonl`, `~/plate-rail-test/logs/run-oldsetup-2.jsonl`)
- `~/plate-rail-test/tdd-stop`이 완료 조건 11의 꼴로 생기고, `/plate:run`을 헤드리스로 한 턴 돌린 기록 `logs/tdd-stop.jsonl`에서 완료 조건 11대로 된다: 손으로 만든 git 레포다. 셋업된 `AGENTS.md`(문서 지도 구간과 규칙 구간), `CLAUDE.md`, 맥락 문서 셋, `calc.py`(`add`), 테스트 `checks/add.md`(doctest), `Makefile`(`test:` 대상이 `python3 -m doctest checks/*.md`), `.gitignore`(`__pycache__/`)를 `23819e6 셋업 직후`로, 작업 `001-sub`(phase 하나, 테스트 먼저 "예", TODO는 `checks/sub.md`와 `calc.py`)의 계획을 `b625429 plan: 001-sub`로 커밋했다. 테스트 파일로 보이는 파일이 없어 테스트가 있는 프로젝트인 것은 `Makefile`로만 정해진다. 그 뒤 훅의 `count_block`을 두 번 불러 `.git/plate-test-first.json`의 `calc.py` 횟수를 2로 두었다(복사본에서 훅을 돌려 `checks/sub.md`는 0, `calc.py`는 세 번째 막음 글과 2로 끝나는 것을 먼저 봤다). `RUN_ALLOW='Bash(make:*)' zsh bin/run.sh claude tdd-stop run tdd-stop answers/tdd-stop.md`(답 파일은 `001` 한 줄) → 518초, exit 0. 수행 에이전트가 `checks/sub.md`를 쓰고 `make test`의 실패를 본 뒤 `calc.py`의 첫 Edit에서 세 번째 막음 글을 받아 막힘으로 멈췄고, run은 두 선택지를 내지 않고 까닭과 해결책을 보이며 논의했다 (`~/plate-rail-test/tdd-stop`, `~/plate-rail-test/answers/tdd-stop.md`, `~/plate-rail-test/logs/tdd-stop.jsonl`)
- `probe-plugin`으로 세션 도중의 본문 고침과 `/reload-plugins`를 헤드리스로 시험한 기록이 `logs/reload-probe*.jsonl`에 있고, 그 결과가 `docs/TOOLS.md`의 Claude Code 절에 적힌다: 프로세스 하나에 stream-json으로 메시지를 차례로 넣는 `bin/reload.py`를 새로 쓰고, 빈 git 레포 `reload-probe`(`2b131f6 init`)에서 `python3 bin/reload.py reload-probe reload-probe` → 377초, exit 0. 차례는 `/probe:lead 1`, work 본문의 표식을 `자두-7391`에서 `앵두-2604`로 고침, 에이전트 2, `/reload-plugins`, 에이전트 3이다. 에이전트 2가 받은 본문(기록 44행)은 `표식: 자두-7391`, `/reload-plugins`의 결과(64행)는 `Reloaded: 6 plugins · 172 skills · 6 agents · 24 hooks · 0 plugin LSP servers`, 에이전트 3이 받은 본문(73행)은 `표식: 앵두-2604`였고 `out-1.txt`, `out-2.txt`, `out-3.txt`의 표식도 같았다. 끝난 뒤 work 본문을 되돌렸다(`shasum` 2fca980…이 시험 전과 같다). `docs/TOOLS.md`의 "훅" 묶음 뒤에 "세션 도중의 스킬 본문 고침" 묶음을 더해 두 에이전트가 받은 본문, 돌린 명령의 꼴, 버전 2.1.302, 날짜 2026-10-17, 출처 문서, 확인하지 않은 것을 적었다 (`~/plate-rail-test/bin/reload.py`, `~/plate-rail-test/reload-probe`, `~/plate-rail-test/logs/reload-probe.jsonl`, `docs/TOOLS.md`)
- `docs/LESSONS.md`에서 완료 조건 13의 41줄이 지워진다: `git show ec2f192:docs/LESSONS.md`의 하네스의 문제점 32줄과 미룬 문제 5줄, 프로젝트에서 배운 것의 (004-context-rules, 검증 1) ADR-018 줄, (006-verify, 검증 1) 줄, (007-harness-issues, phase 4) `git -C` 줄, (008-tdd, phase 1) `.gitignore` 줄을 글자 그대로 맞춰 지웠다. 이 작업의 phase가 통과할 때 더한 (009-lessons-fixes, …) 줄과 다른 줄은 그대로다. 미룬 문제 절은 제목만 남았다 (`docs/LESSONS.md`)

## 확인 결과
- 완료 조건 10이 참이다.
  - `ls ~/plate-rail-test/run-oldsetup/docs/notes/lessons.md ~/plate-rail-test/run-oldsetup/docs/LESSONS.md` → `run-oldsetup/docs/notes/lessons.md`만 나오고 `docs/LESSONS.md`는 `No such file or directory`. 통과
  - `grep -c 'docs/notes/lessons.md' ~/plate-rail-test/run-oldsetup/AGENTS.md` → `1`. 그 행의 내용 칸은 "회고에서 배운 것, 하네스의 문제점, 미룬 문제", 읽을 때 칸은 "작업을 계획하거나 회고할 때"다. 통과
  - `tail -3 ~/plate-rail-test/run-oldsetup/docs/tasks/001-gitignore/verify.md` → `**판정**: 통과`, 빈 줄, `LESSONS로 옮겼다`. 통과
  - run-oldsetup에서 `git log -1 --stat` → `[001] 검증 통과`(`11d110c`), `AGENTS.md`, `docs/notes/lessons.md`, `docs/tasks/001-gitignore/verify.md`가 든다. `docs/notes/lessons.md`는 세 절 제목(프로젝트에서 배운 것, 하네스의 문제점, 미룬 문제)과 `(001-gitignore, 검증 1)` 줄 넷인 LESSONS의 양식이다. 통과
  - 완료 조건 9의 둘째 확인(`N=$(ls -t plugins/plate/skills/*/SKILL.md plugins/plate/hooks/* | head -1); find ~/plate-rail-test/logs -name '*.jsonl' -newer "$N"`) → `N`은 `plugins/plate/skills/run/SKILL.md`이고, 출력에 `run-oldsetup.jsonl`과 `run-oldsetup-2.jsonl`이 든다. 통과
- 완료 조건 11이 참이다.
  - `cat ~/plate-rail-test/tdd-stop/docs/tasks/*/phase-*.md | grep -c '훅이 테스트 먼저 때문에 세 번째 막음:'` → `2`("남은 것"과 "하네스에서 걸린 것"에 하나씩). 통과
  - `python3 bin/summ.py logs/tdd-stop.jsonl 4000`으로 마지막 답글을 읽었다 → "이 막힘에는 "다시 맡긴다 / 멈춘다" 선택지를 내지 않습니다"라고 적고, 수행 에이전트의 다섯 줄(상태: 막힘), 막힌 까닭(`checks/sub.md`를 먼저 쓰고 실패를 본 뒤 `calc.py`의 첫 Edit가 세 번째 막음으로 막혔다), 수행 에이전트가 적은 해결책 둘(훅이 먼저 생긴 테스트를 알아본다, 횟수를 수행마다 새로 센다)을 보이고, 제 짐작과 함께 까닭 확인 / 훅을 고침 / 계획을 바꿈의 세 길을 추천과 함께 내며 "어느 길로 갈까요?"로 논의를 물었다. 정해 둔 두 선택지는 묻지 않았다. 통과
  - 완료 조건 9의 둘째 확인 → 출력에 `tdd-stop.jsonl`이 든다. 통과
- 완료 조건 12가 참이다.
  - `logs/reload-probe.jsonl`에서 `parent_tool_use_id`가 에이전트인 `Base directory for this skill:` 줄을 읽었다 → 에이전트 2(44행)는 `표식: 자두-7391`, 에이전트 3(73행)은 `표식: 앵두-2604`, 그 사이 64행의 결과는 `Reloaded: 6 plugins · 172 skills · 6 agents · 24 hooks · 0 plugin LSP servers`다. `docs/TOOLS.md`의 "세션 도중의 스킬 본문 고침" 묶음에 적은 결과와 같다. 통과
- 완료 조건 13이 참이다.
  - `git diff ec2f192 -- docs/LESSONS.md | grep -c '^-- '` → `41`. 통과
  - `git diff ec2f192 -- docs/LESSONS.md | grep '^-- '`를 읽었다 → 프로젝트에서 배운 것의 넷((004-context-rules, 검증 1) ADR-018, (006-verify, 검증 1), (007-harness-issues, phase 4) `git -C`, (008-tdd, phase 1) `.gitignore`), 하네스의 문제점 32줄((007-harness-issues, phase 2)부터 (008-tdd, 검증 1)까지), 미룬 문제 5줄((004-context-rules, 검증 1) 하나와 (006-verify, 검증 1) 넷)이다. 더한 줄(`^+`)은 이 작업의 phase가 통과할 때 더한 (009-lessons-fixes, …) 15줄뿐이다. 통과
- 완료 조건 8이 참이다. 이 phase가 `docs/TOOLS.md`를 고친다.
  - `grep -n '멈춘 이유는 없음' docs/ADR.md` → 출력 없음(종료 코드 1). 통과
  - `docs/TOOLS.md`의 머리글(3행에 "6단계에서 확인한 것은 마지막 phase에서 판정을 돌리면서 적었다"), "지금 상태" 표(Claude Code 행이 "… 5단계(검증), 6단계(TDD와 엣지케이스)의 판정"), 훅 묶음(2만 막고 1이나 127 같은 다른 0이 아닌 코드는 막지 않는다, `python3`는 스크립트 파일을 열지 못하면 2로 끝난다, macOS와 Linux는 `sh -c`, Windows는 Git Bash, 없으면 PowerShell. 출처 code.claude.com/docs/en/hooks)와 `docs/ADR.md`의 ADR-019(트레이드오프 "`python3`가 없거나 스크립트 파일이 없을 때 훅이 돌지 않고 규칙 구간만 남는다."), ADR-018의 이유 끝("멈춘 이유는 없다.")을 읽었다 → 모두 있다. 이 phase가 더한 묶음은 그 사이에 들어가 셋을 바꾸지 않았다. 통과
- 완료 조건 15가 참이다.
  - `python3 -m unittest discover -s tests` → `Ran 36 tests in 9.494s`, 마지막 줄 `OK`. 뒤의 `git status --short --untracked-files=all`에 `__pycache__`가 없다. 통과

## 계획과 달라진 점
- 완료 조건 11의 시험 폴더: 계획은 테스트가 `checks/`에 있고 `Makefile`에 `test` 대상이 있는 꼴을 예로 들었다. 테스트를 `checks/`의 `.py`로 두면 테스트 먼저인 phase에서 그 파일이 코드 파일이고 테스트 파일이 아니어서 훅이 테스트를 쓰는 편집부터 막는다. 그래서 테스트를 `checks/*.md`의 doctest로 두고 `make test`가 `python3 -m doctest checks/*.md`로 돌게 했다. 수행 에이전트가 테스트를 쓴 뒤에도 훅이 그것을 테스트 파일로 보지 않는 것은 계획과 같다. 폴더는 `bin/vfmake.sh`의 갈래가 아니라 손으로 만들었다.
- 완료 조건 12의 시험: 읽을 것은 `bin/a2.sh`를 시험의 꼴로 들었지만, `a2.sh`는 프롬프트 하나로 프로세스 하나를 돌려 세션 도중에 디스크를 고칠 틈이 없고, `--resume`으로 잇는 턴은 프로세스를 새로 띄워 한 세션 도중과 같은 조건인지 알 수 없다. 그래서 `claude -p --input-format stream-json`으로 프로세스 하나에 메시지를 차례로 넣고 그 사이에 본문을 고치는 `bin/reload.py`를 새로 썼다. 기록은 `logs/reload-probe.jsonl` 하나다.

## 남은 것
없음

## 하네스에서 걸린 것
- `~/plate-rail-test`는 git 레포가 아니라서 이 phase가 만들거나 고친 `bin/reload.py`, `answers/run-oldsetup-2.md`, `answers/tdd-stop.md`, 시험 폴더 `run-oldsetup`, `tdd-stop`, `reload-probe`와 기록은 커밋에 들지 않는다. 커밋에는 `docs/LESSONS.md`, `docs/TOOLS.md`, `phase-7.md`만 든다.
- 계획의 읽을 것이 시험의 꼴로 든 `bin/a2.sh`는 세션 도중에 본문을 고치는 시험에 맞지 않았다(위의 "계획과 달라진 점").
- tdd-stop의 수행 에이전트와 run은 훅의 소스(`plugins/plate/hooks/edit_guard.py`)를 읽지 못해(프로젝트 밖의 파일) 첫 Edit가 세 번째 막음이 된 까닭을 짐작으로만 적었다. 이 시험은 횟수를 미리 2로 둔 것이라 실제 사용과 다르지만, 막은 글이 왜 막았는지(테스트 파일의 기준)를 담지 않으면 프로젝트 밖의 훅을 읽지 못하는 에이전트는 까닭을 확인할 수 없다. 이번 글에는 "테스트 파일은 … 꼴인 파일이다"가 TEST_FIRST에만 있고 세 번째 막음 글(STOP)에는 없다.

## 회고 1: 회고

**확인**
- 완료 조건 10이 참이다.
  - `ls ~/plate-rail-test/run-oldsetup/docs/notes/lessons.md ~/plate-rail-test/run-oldsetup/docs/LESSONS.md` → `docs/notes/lessons.md`만 있고 `docs/LESSONS.md`는 `No such file or directory`. 통과
  - `grep -c 'docs/notes/lessons.md' ~/plate-rail-test/run-oldsetup/AGENTS.md` → `1`(문서 지도 11행, `docs/tasks/NNN-slug/` 행 앞). 통과
  - `tail -3 ~/plate-rail-test/run-oldsetup/docs/tasks/001-gitignore/verify.md` → `**판정**: 통과`, 빈 줄, `LESSONS로 옮겼다`. 통과
  - run-oldsetup에서 `git log -1 --stat` → `11d110c [001] 검증 통과`에 `AGENTS.md`, `docs/notes/lessons.md`, `docs/tasks/001-gitignore/verify.md`가 든다. `docs/notes/lessons.md`는 run 본문의 LESSONS 양식(제목, 세 절, `(001-gitignore, 검증 1)` 줄 넷)이다. 통과
  - 완료 조건 9의 둘째 확인 → `N`은 `plugins/plate/skills/run/SKILL.md`이고 출력에 `run-oldsetup.jsonl`, `run-oldsetup-2.jsonl`이 든다. 첫 턴의 마지막 답글(`python3 bin/summ.py logs/run-oldsetup.jsonl 3000`)은 `docs/LESSONS.md`를 추천안으로 위치를 묻고 멈췄고, 둘째 턴의 답 파일은 "`docs/notes/lessons.md`에 만든다."다. 통과
- 완료 조건 11이 참이다.
  - `cat ~/plate-rail-test/tdd-stop/docs/tasks/*/phase-*.md | grep -c '훅이 테스트 먼저 때문에 세 번째 막음:'` → `2`. 통과
  - `logs/tdd-stop.jsonl`의 마지막 답글(`python3 bin/summ.py logs/tdd-stop.jsonl 6000`) → "다시 맡긴다 / 멈춘다" 선택지를 내지 않는다고 적고, 수행 에이전트의 다섯 줄, 막힌 까닭, 수행 에이전트가 적은 해결책 둘을 보인 뒤 짐작과 세 길을 추천과 함께 내며 "어느 길로 갈까요?"로 논의를 묻는다. 같은 기록에서 수행 에이전트의 `calc.py` 첫 Edit(71행)가 세 번째 막음 글을 받았다. 통과
  - 완료 조건 9의 둘째 확인 → 출력에 `tdd-stop.jsonl`이 든다. 통과
- 완료 조건 12가 참이다.
  - `logs/reload-probe.jsonl`에서 `parent_tool_use_id`가 에이전트인 `Base directory for this skill:` 줄 → 에이전트 1(17행)과 2(45행)는 `표식: 자두-7391`, 3(74행)은 `표식: 앵두-2604`이고, 2와 3 사이 64행이 `Reloaded: 6 plugins · 172 skills · 6 agents · 24 hooks · 0 plugin LSP servers`다. `reload-probe/out-1~3.txt`의 표식도 같고 work 본문은 `자두-7391`로 돌아와 있다. `docs/TOOLS.md`의 "세션 도중의 스킬 본문 고침" 묶음과 같다. 그 묶음이 인용한 code.claude.com/docs/en/plugins/create와 plugins/cli-reference에도 적힌 글이 있다. 통과
- 완료 조건 13이 참이다.
  - `git diff ec2f192 -- docs/LESSONS.md | grep -c '^-- '` → `41`. 통과
  - 같은 차이의 `^-- ` 줄을 읽고 `git show ec2f192:docs/LESSONS.md`와 절마다 견줬다 → 하네스의 문제점 32줄과 미룬 문제 5줄이 모두 지워졌고, 프로젝트에서 배운 것에서 지운 넷이 완료 조건 13의 넷이며 남은 11줄은 순서도 그대로다. 더한 줄은 (009-lessons-fixes, …) 15줄뿐이다. 통과
- 완료 조건 8이 참이다.
  - `grep -n '멈춘 이유는 없음' docs/ADR.md` → 출력 없음(종료 코드 1). 통과
  - `docs/TOOLS.md`의 머리글(3행), "지금 상태" 표(9행), 훅 묶음(72~74행)과 `docs/ADR.md`의 ADR-019 트레이드오프(26행), ADR-018 이유 끝(20행 "멈춘 이유는 없다.")을 읽었다 → 모두 있다. 이 phase의 TOOLS.md 차이는 77~84행의 묶음을 더한 것뿐이다. 통과
- 완료 조건 15가 참이다.
  - `python3 -m unittest discover -s tests` → `Ran 36 tests`, 마지막 줄 `OK`. 뒤의 `git status --short --untracked-files=all` → 출력 없음. 통과

**문제**
없음

**배운 것**
- `~/plate-rail-test/tdd-stop`은 수행이 막힌 채 멈춘 상태다. `task/001-sub`에 커밋이 없고 `docs/tasks/001-sub/phase-1.md`(기록)와 `checks/sub.md`가 커밋되지 않았으며 `.git/plate-test-first.json`의 `calc.py` 횟수는 3이다. 완료 조건 11의 첫 확인은 그 커밋되지 않은 `phase-1.md`를 읽으므로 검증 전에 그 폴더에서 run을 다시 부르면 결과가 바뀐다. `~/plate-rail-test/run-oldsetup`은 합칠지 묻고 멈춘 상태(`task/001-gitignore`의 `11d110c`)라 그 물음에 답하면 완료 조건 10의 `git log -1 --stat`이 바뀐다.

**하네스의 문제점**
- 훅(`plugins/plate/hooks/edit_guard.py`)의 세 번째 막음 글(`STOP`)은 막은 까닭인 테스트 파일의 기준을 담지 않고, 그 기준은 `TEST_FIRST` 글에만 있다. 막은 횟수는 git 폴더에 남아 수행이 바뀌어도 이어지므로 새 수행 에이전트가 첫 편집에서 바로 `STOP`을 받을 수 있고, 에이전트는 프로젝트 밖의 훅 소스를 읽지 못한다(`docs/TOOLS.md`). tdd-stop에서 수행 에이전트와 run은 훅 소스 읽기를 거부당해(`logs/tdd-stop.jsonl` 80행, 103행) 까닭(`checks/sub.md`가 `.md`라 커밋되지 않은 테스트 변경으로 세지 않는다)을 확인하지 못하고 짐작으로 논의했다.
- 계획의 phase 7이 시험의 꼴로 든 둘이 그대로 쓰이지 않아 수행이 바꿨다("계획과 달라진 점"). 읽을 것의 `bin/a2.sh`는 프롬프트 하나로 프로세스 하나를 돌려(`claude -p "$prompt" … < /dev/null`) 세션 도중에 디스크를 고칠 틈이 없다. 완료 조건 11의 예("테스트가 `checks/`에 있고")는, 훅이 테스트 파일로 보지 않는 `.md`가 아닌 파일이면 코드 파일이라(`is_code_file`, `is_test_file`) 테스트를 쓰는 편집부터 막힌다.
- 이 회고를 부를 때 받은 retro 본문은 디스크의 판이 아니라 `9bd206e`(이 작업의 phase 3) 전의 판이었다. 3번 58행의 둘째 문장, 60행의 "본 결과는 통과해도 …", 4번 64행의 예외, 양식 99~100행과 적는 규칙 119~120행이 없었다. 이 phase가 `docs/TOOLS.md`에 적은 사실(본문을 고친 뒤 `/reload-plugins` 없이 띄운 에이전트는 고치기 전의 본문을 받는다)과 맞는데, `plugins/plate/skills/`의 어느 본문에도 `/reload-plugins`나 세션을 새로 여는 것이 없어서, 이 작업이 그 사실을 적는 것으로 닫은 (008-tdd, phase 4)·(008-tdd, 검증 1) 줄과 같은 일이 이 작업 안에서 되풀이된다. 이 phase는 테스트 먼저가 "아니오"이고 맥락 문서와 어긋나는 것이 없어 두 판의 차이가 판정을 바꾸지 않는다.

**판정**: 통과
