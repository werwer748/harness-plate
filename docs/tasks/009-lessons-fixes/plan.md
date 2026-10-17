# LESSONS의 문제점과 미룬 문제 해결

## 요청
일단 여기에 기록된 문제점이랑 미룬것들 모두 수정하자

## 목표
`docs/LESSONS.md`의 하네스의 문제점 32줄과 미룬 문제 5줄이 훅, 스킬 본문(plan, phase, retro, verify, context, run), 맥락 문서, 시험으로 고쳐지거나 그대로 두기로 정해져 LESSONS에서 지워진다. 바뀐 본문으로 다시 돌린 시험이 통과하고, 두 매니페스트의 버전이 0.9.1이다.

## 범위 밖
- `docs/LESSONS.md`의 프로젝트에서 배운 것 절 가운데 지우기로 한 넷을 뺀 11줄
- 이 작업이 다시 돌리지 않는 판정 경우(vf 셋, run-verify, run-vfix, 셋업·맥락·계획의 판정)
- context 절대 규칙 5의 예외를 Codex에서 돌려 보는 것(ADR-018)
- 훅이 Bash 명령으로 하는 편집을 보는 것
- 루트 `TODO.md`의 작업 관리 방법 바꾸기

## 완료 조건
1. 훅이 네 경우를 다룬다. (가) 커밋되지 않은 변경 가운데 `__pycache__/` 아래 파일과 `.pyc` 파일은 테스트 변경으로 세지 않는다. (나) `docs/tasks/` 아래 파일은 코드 파일이 아니다. (다) 테스트 먼저로 막은 횟수는 그 phase의 계획 줄과 `plan.md`가 바뀌지 않은 동안 센다. `plan.md`만 바뀌어도 다시 센다. (라) `hooks.json`의 명령은 스크립트 파일이 없으면 종료 코드 0으로 끝나고, 있으면 스크립트의 종료 코드로 끝난다.
   - 확인: `python3 -m unittest discover -s tests -v` → 마지막 줄이 `OK`
   - 확인: `tests/test_edit_guard.py`를 읽는다 → (가)~(라)마다 그 상황을 만들고 막음이나 통과를 단언하는 테스트가 있고, (라)는 `hooks.json`의 명령 글을 `sh -c`로 돌린다
2. 이 레포의 `.gitignore`가 `__pycache__/`를 거른다.
   - 확인: `python3 -m unittest discover -s tests` 뒤 `git status --short --untracked-files=all | grep __pycache__` → 출력 없음
3. plan 본문(`plugins/plate/skills/plan/SKILL.md`)에 넷이 있다. (가) 낱말 "테스트가 있는 프로젝트"가 훅과 같은 기준이다: 테스트 파일이 있거나, `package.json`의 `scripts.test`(npm의 기본 자리표시 글은 빼고)나 `Makefile`의 `test` 대상이 있다. (나) 테스트 먼저 "예"는 테스트가 있는 프로젝트에서 코드 파일(`.md`가 아닌 파일)의 동작을 바꾸는 phase다. 테스트가 없는 프로젝트의 phase와 `.md`만 고치는 phase는 "아니오"와 그 이유다. (다) 목표에 적은 것은 모두 어느 완료 조건에 든다. (라) 엣지케이스 후보에 요청이나 완료 조건이 이미 정한 동작을 내지 않는다.
   - 확인: `grep -n '동작을 바꾸는 phase는 "예"다' plugins/plate/skills/plan/SKILL.md` → 출력 없음
   - 확인: plan 본문의 낱말, 5번, 적는 규칙을 읽는다 → (가)~(라)가 있다
4. phase 본문(`plugins/plate/skills/phase/SKILL.md`)의 2번에 둘이 있다. 고칠 문제를 넘겨받았으면 동작을 바꾸는 문제에만 테스트부터 쓴다. 테스트 먼저 기록에 실패 출력이 없다는 문제는, 구현 파일만 git으로 그 phase 커밋의 부모 것으로 잠깐 되돌려 테스트를 돌려 실패 출력을 얻고 다시 돌려놓는다.
   - 확인: `grep -n '고칠 문제를 넘겨받았어도 같다' plugins/plate/skills/phase/SKILL.md` → 출력 없음
   - 확인: phase 본문 2번을 읽는다 → 둘이 있다
5. retro와 verify 본문에 셋이 있다. (가) 4번: 다른 스킬의 본문이 그 phase(verify는 작업)의 커밋이 바꾼 파일이거나 계획의 읽을 것이면 1번대로 읽는다. (나) retro 3번: 머리의 결정이나 완료 조건이 바꾸기로 한 맥락 문서의 줄과 어긋나는 것은 문제로 적지 않는다. (다) 회고 방식의 회고 절과 검증 절의 "확인"에, 테스트 먼저가 "예"인 phase이면 그 기록을 본 줄(본 곳, 실패 출력과 통과 출력이 순서대로 있는지, 통과 | 실패)을 통과해도 적는다.
   - 확인: `plugins/plate/skills/retro/SKILL.md`와 `plugins/plate/skills/verify/SKILL.md`의 3번, 4번, 양식, 적는 규칙을 읽는다 → (가)와 (다)는 두 곳에, (나)는 retro에 있다
6. context 본문(`plugins/plate/skills/context/SKILL.md`)의 절대 규칙 5에, 다른 스킬을 이름으로 불러 도구가 그 스킬의 본문을 여는 것은 예외라는 것이 있다.
   - 확인: 절대 규칙 5를 읽는다 → 예외가 있다
7. run 본문(`plugins/plate/skills/run/SKILL.md`)에 넷이 있다. (가) "통과하면" 1번이 옮긴 뒤 `verify.md`의 마지막 검증 절 아래에 `LESSONS로 옮겼다`를 적는다. 옮길 줄이 없거나 모두 겹쳐도 적는다. 절대 규칙 5의 직접 고치는 파일과 "통과하면" 3번의 커밋에 그 줄이 든다. (나) "`docs/LESSONS.md`" 절에서 이 작업의 검증 절의 줄을 옮겼는지는 그 줄이 있는지로 본다. git 레포가 아니어도 같다. (다) 0번의 worktree 갈래: 원래 자리에서 worktree 안의 파일을 고치거나 커밋하지 않는다. worktree의 `verify.md`에 그 줄이 있으면 "합친다"로 가고, 닫힌 검증인데 그 줄이 없으면 그 worktree에서 세션을 열어 이 스킬을 부르라고 안내하고 끝난다. (라) 고칠 phase 양식: 테스트 먼저는 완료 조건 3의 (나)와 같은 기준이고, 읽을 것에 문서 지도의 맥락 문서가 있고, 통과 조건에 검증 K의 문제가 모두 고쳐졌다는 조건(확인: 문제마다 적힌 곳을 다시 읽거나 돌린다)이 머리의 완료 조건과 함께 있다.
   - 확인: `grep -n 'git log -S\|git -C' plugins/plate/skills/run/SKILL.md` → 출력 없음
   - 확인: run 본문의 절대 규칙 5, 0번, "통과하면", "고칠 phase를 더한다", "합친다", "`docs/LESSONS.md`" 절을 읽는다 → (가)~(라)가 있고, 문서 지도 절에서 다른 위치로 읽는 곳의 목록이 바뀐 기준과 맞는다
8. 맥락 문서가 바뀐다. `docs/TOOLS.md`의 머리글과 "지금 상태" 표가 6단계까지 적는다. TOOLS.md의 훅 묶음에 종료 코드와 명령 실행의 사실이 출처 문서와 함께 있다: 2만 막고 1이나 127 같은 다른 0이 아닌 코드는 막지 않는다, `python3`는 스크립트 파일을 열지 못하면 2로 끝난다, 명령은 macOS와 Linux에서 `sh -c`로 돌고, Windows에서는 Git Bash, Git Bash가 없으면 PowerShell로 돈다. `docs/ADR.md`의 ADR-019 트레이드오프가 `python3`가 없거나 스크립트 파일이 없을 때 훅이 돌지 않고 규칙 구간만 남는다고 적고, ADR-018의 이유 끝이 "멈춘 이유는 없다."다.
   - 확인: `grep -n '멈춘 이유는 없음' docs/ADR.md` → 출력 없음
   - 확인: `docs/TOOLS.md`의 머리글, "지금 상태" 표, 훅 묶음과 `docs/ADR.md`의 ADR-019를 읽는다 → 위의 것이 있다
9. 006의 실행 시험 여섯이 바뀐 본문으로 통과한다. `~/plate-rail-test`의 run-vrule, run-nogit, run-small, run-all, run-wt, run-wt-gate를 `bin/vfmake.sh`로 다시 만들어 돌린다. `bin/runcheck.py`의 기대는 이 작업의 결정이 바꾼 동작에 걸리는 것만 고치고, 고쳤으면 고친 곳과 까닭을 phase 기록에 적는다.
   - 확인: `python3 ~/plate-rail-test/bin/runcheck.py <폴더>`를 여섯 폴더마다 돌린다 → 실패한 항목이 없다
   - 확인: `N=$(ls -t plugins/plate/skills/*/SKILL.md plugins/plate/hooks/* | head -1); find ~/plate-rail-test/logs -name '*.jsonl' -newer "$N"` → 여섯 시험의 기록이 모두 든다
10. 옛 셋업에서 LESSONS의 위치를 추천안이 아닌 곳으로 답하면 run이 그 위치에 만든다. `~/plate-rail-test/run-oldsetup`을 `bin/vfmake.sh`로 다시 만들어 `/plate:run 001`을 헤드리스로 돌리고, 위치 물음에 `docs/notes/lessons.md`로 답하는 턴을 잇는다. 그 파일이 LESSONS의 양식으로 생기고, 문서 지도에 그 위치의 행이 생기고, `docs/LESSONS.md`는 없고, `verify.md`의 마지막 검증 절 아래에 `LESSONS로 옮겼다`가 있다.
   - 확인: `ls ~/plate-rail-test/run-oldsetup/docs/notes/lessons.md ~/plate-rail-test/run-oldsetup/docs/LESSONS.md` → 앞의 것만 있다
   - 확인: `grep -c 'docs/notes/lessons.md' ~/plate-rail-test/run-oldsetup/AGENTS.md` → 1
   - 확인: `tail -3 ~/plate-rail-test/run-oldsetup/docs/tasks/001-gitignore/verify.md` → `LESSONS로 옮겼다`가 있다
   - 확인: run-oldsetup에서 `git log -1 --stat` → `docs/notes/lessons.md`, `AGENTS.md`, `verify.md`가 든다
   - 확인: 완료 조건 9의 둘째 확인 → run-oldsetup의 두 턴의 기록이 든다
11. 테스트 먼저 phase에서 훅이 같은 파일을 세 번째 막으면 수행 에이전트는 막힘으로 멈춰 기록에 그 줄을 적고, run은 정해 둔 선택지 없이 막힌 까닭과 해결책을 보여 주고 논의한다. 시험 폴더는 `~/plate-rail-test/tdd-stop`이다. 테스트가 있는 프로젝트이고, 테스트 먼저 "예"인 phase가 하나 있고, 수행 에이전트가 테스트를 쓴 뒤에도 훅이 그 테스트를 테스트 파일로 보지 않는다(예: 테스트가 `checks/`에 있고 `Makefile`에 `test` 대상이 있다). 고칠 코드 파일의 막은 횟수를 미리 2로 둔다. 거기서 `/plate:run`을 헤드리스로 한 턴 돌리고 기록은 `logs/tdd-stop.jsonl`이다.
   - 확인: `cat ~/plate-rail-test/tdd-stop/docs/tasks/*/phase-*.md | grep -c '훅이 테스트 먼저 때문에 세 번째 막음:'` → 2
   - 확인: `logs/tdd-stop.jsonl`의 마지막 답글을 읽는다 → "새 에이전트에게 다시 맡긴다 / 멈춘다"를 묻지 않고, 막힌 까닭과 수행 에이전트가 적은 해결책을 보이며 논의한다
   - 확인: 완료 조건 9의 둘째 확인 → tdd-stop의 기록이 든다
12. 세션 도중에 스킬 본문을 고쳤을 때 띄운 에이전트가 받는 본문이 시험으로 확인되어 `docs/TOOLS.md`의 Claude Code 절에 적힌다. 한 헤드리스 세션에서 `~/plate-rail-test/probe-plugin`의 스킬을 부른 뒤 디스크의 본문을 고치고 띄운 에이전트가 받은 본문과, 같은 세션에서 `/reload-plugins` 뒤에 띄운 에이전트가 받은 본문이다. 기록은 `logs/reload-probe*.jsonl`이다.
   - 확인: 기록에서 두 에이전트가 받은 스킬 본문을 읽는다 → `docs/TOOLS.md`에 적힌 결과와 같다
13. `docs/LESSONS.md`에서 41줄이 지워졌다: `ec2f192`의 하네스의 문제점 32줄과 미룬 문제 5줄, 프로젝트에서 배운 것 가운데 (004-context-rules, 검증 1)의 ADR-018 줄, (006-verify, 검증 1)의 줄, (007-harness-issues, phase 4)의 run 0번 `git -C` 줄, (008-tdd, phase 1)의 `.gitignore` 줄. 다른 줄은 그대로다.
   - 확인: `git diff ec2f192 -- docs/LESSONS.md | grep -c '^-- '` → 41
   - 확인: `git diff ec2f192 -- docs/LESSONS.md | grep '^-- '`를 읽는다 → 위의 41줄이다
14. 두 매니페스트의 버전이 0.9.1이다.
   - 확인: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "0.9.1",`
15. 프로젝트 전체 테스트가 모두 통과한다.
   - 확인: `python3 -m unittest discover -s tests` → 마지막 줄이 `OK`

## 결정
- 37줄은 줄마다 고치거나 그대로 두기로 정한 뒤 모두 LESSONS에서 지운다. 프로젝트에서 배운 것 절은 이 작업으로 사실이 아니게 되는 넷만 지우고, 그 가운데 문제를 적은 둘(ADR-018의 꼴, run 0번의 `git -C`)은 고친다. 이유: 요청이 모두 고치자고 했다.
- (007-harness-issues, phase 2)의 세 줄은 고치지 않는다. 이유: 첫째는 시험 환경의 사실, 둘째는 시험 폴더를 만든 방식에서 나온 줄이고, 셋째는 007의 phase 1이 "작업의 커밋"의 정의를 이미 고쳤다.
- (007-harness-issues, phase 5)의 첫째 줄(고칠 phase의 TODO가 고치는 방향을 적지 않는다)은 고치지 않는다. 이유: 고치는 방향은 지금처럼 수행이 정한다(자유도).
- (007-harness-issues, phase 5)의 둘째 줄(시험 폴더를 되돌리는 방법이 없다)은 고치지 않는다. 이유: 지금은 `bin/vfmake.sh run-oldsetup`이 그 폴더를 다시 만든다.
- (007-harness-issues, 검증 1)의 둘째 줄(두 phase에 나뉜 완료 조건의 어긋남)은 고치지 않는다. 이유: phase 사이의 어긋남을 찾는 것이 검증의 일이고 실제로 찾았다.
- (008-tdd, phase 2)의 첫째 줄(엣지케이스 물음과 추천안의 이유)은 고치지 않는다. 이유: 008이 plan 본문 5번에 "추천안의 이유에도 적지 않는다"를 이미 더했다.
- ADR-019의 번호는 바꾸지 않는다. 이유: ADR은 지금 유효한 결정만 담고, 지금 문서 안에서 ADR-019는 하나뿐이다. git 이력을 볼 때만 헷갈린다.
- 테스트 먼저의 범위는 표시를 적는 plan과 run에서 좁히고, 표시를 따르는 phase 본문 2번의 순서 규칙은 그대로 둔다. 이유: 훅이 검사하는 범위와 같아진다.
- 이 계획에서도 스킬 본문, 문서, 매니페스트만 고치거나 시험만 돌리는 phase는 테스트 먼저 "아니오"로 적는다. 이유: 완료 조건 3의 (나)를 이 계획에도 바로 쓰기로 했다.
- 테스트 먼저인 phase에서 동작을 바꾸지 않는 문제를 고치려고 코드 파일을 편집하면 커밋되지 않은 테스트 변경이 없어 훅에 막힐 수 있는데, 훅은 그대로 둔다. 이유: 훅은 문제의 종류를 알 수 없고, 되돌리기는 git으로 하며, 세 번 막히면 논의로 간다. (추천안으로 정함)
- 훅 phase의 엣지케이스는 논의하지 않고 수행 에이전트가 정한다. 이유: 고칠 동작은 이 계획의 답으로 이미 정해졌다.
- 버전은 0.9.1로 올린다. 이유: 스킬의 동작이 바뀌면 단계 밖의 작업이어도 버전을 올리고, 단계 안의 고침은 patch다. (추천안으로 정함)
- TOOLS.md의 훅 명령 실행 사실에 Windows의 셸을 함께 적는다. 이유: phase 1 회고가 출처 문서에서 Windows는 `sh`로 돌지 않는다는 것을 찾았다. 바뀐 명령이 PowerShell에서 어떻게 끝나는지는 이 작업이 다루지 않는다.
