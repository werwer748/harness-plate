# 검증

## 검증 1

**확인**
- 1. 훅이 네 경우를 다룬다: (가) `__pycache__/` 아래와 `.pyc`는 테스트 변경이 아니다, (나) `docs/tasks/` 아래는 코드 파일이 아니다, (다) 막은 횟수는 그 phase의 계획 줄과 `plan.md`가 바뀌지 않은 동안 센다, (라) `hooks.json`의 명령은 스크립트 파일이 없으면 0, 있으면 스크립트의 종료 코드로 끝난다.
  - `python3 -m unittest discover -s tests -v` → 36개 모두 `ok`, `Ran 36 tests in 9.415s`, 마지막 줄 `OK`. 통과
  - `tests/test_edit_guard.py`를 읽음 → (가) `TestFirstTest.test_python_bytecode_is_not_a_test_change`가 `.gitignore` 없이 `tests/__pycache__/…pyc`, `tests/test_app.pyc`, `src/__pycache__/…pyc`만 생긴 상태에서 `src/app.py` 편집이 테스트 먼저로 막히고 `tests/test_app.py`를 바꾼 뒤에는 통과함을, (나) `SetupAndCodeFileTest.test_docs_tasks_files_are_not_code`가 남은 phase가 없을 때 `docs/tasks/.gitkeep`의 Write가 통과하고(같은 상태의 `src/app.py`는 막힘) 테스트 먼저 phase에서 `docs/tasks/001-a/notes.txt`가 통과함을, (다) `ThirdBlockTest.test_plan_md_change_resets_count`가 두 번 막은 뒤 `plan.md`만 고쳐 커밋하면 세 번째 편집이 멈춤 글 없이 테스트 먼저 글로 막힘을, (라) `HooksJsonCommandTest`가 `hooks.json`에서 읽은 명령 글을 `sh -c`로 돌려 없는 플러그인 폴더면 막을 호출도 0, 있는 폴더면 스크립트의 2와 0이 그대로 나옴을 단언한다. 통과
- 2. 이 레포의 `.gitignore`가 `__pycache__/`를 거른다.
  - `python3 -m unittest discover -s tests` 뒤 `git status --short --untracked-files=all | grep __pycache__` → 출력 없음(종료 코드 1). `tests/__pycache__/test_edit_guard.cpython-313.pyc`는 디스크에 있다. 통과
- 3. plan 본문에 넷이 있다: (가) "테스트가 있는 프로젝트"가 훅과 같은 기준, (나) 테스트 먼저 "예"의 범위, (다) 목표에 적은 것은 모두 어느 완료 조건에 든다, (라) 엣지케이스 후보에 이미 정한 동작을 내지 않는다.
  - `grep -n '동작을 바꾸는 phase는 "예"다' plugins/plate/skills/plan/SKILL.md` → 출력 없음(종료 코드 1). 통과
  - `plugins/plate/skills/plan/SKILL.md`를 읽음 → (가) 30행 낱말이 테스트 파일, `package.json`의 `scripts.test`(`no test specified` 빼고), `Makefile`의 `test` 대상으로 적고 테스트 파일의 기준이 훅(`plugins/plate/hooks/edit_guard.py`의 `TEST_DIRS`, `TEST_NAMES`, `manifest_has_test_command`)과 같다. (나) 201행이 "예"를 테스트가 있는 프로젝트에서 코드 파일(`.md`가 아닌 파일)의 동작을 바꾸는 phase로 적고, 테스트가 없는 프로젝트의 phase와 `.md`만 고치는 phase는 "아니오"와 이유다. (다) 184행. (라) 83행 "요청이나 완료 조건이 이미 정한 동작은 후보로 내지 않는다". 통과
- 4. phase 본문 2번에 둘이 있다: 고칠 문제는 동작을 바꾸는 문제에만 테스트부터 쓴다, 실패 출력이 없다는 문제는 구현 파일만 그 phase 커밋의 부모 것으로 잠깐 되돌려 실패 출력을 얻는다.
  - `grep -n '고칠 문제를 넘겨받았어도 같다' plugins/plate/skills/phase/SKILL.md` → 출력 없음(종료 코드 1). 통과
  - `plugins/plate/skills/phase/SKILL.md` 2번을 읽음 → 44행 "고칠 문제를 넘겨받았으면 동작을 바꾸는 문제에만 테스트부터 쓴다", 52행 `git checkout <커밋>^ -- <구현 파일>`로 잠깐 되돌려 테스트를 돌리고 다시 돌려놓는 규칙이 있다. 통과
- 5. retro와 verify 본문에 셋이 있다: (가) 4번의 다른 스킬 본문 예외, (나) retro 3번의 결정이 바꾸기로 한 맥락 문서의 줄, (다) 테스트 먼저 기록을 통과해도 "확인"에 적는다.
  - `plugins/plate/skills/retro/SKILL.md`와 `plugins/plate/skills/verify/SKILL.md`를 읽음 → (가) retro 64행과 verify 65행 "다만 그 본문이 … 바꾼 파일이거나 계획의 읽을 것이면 1번대로 읽고". (나) retro 58행. (다) retro 60행·99~100행·119~120행, verify 61행·100~101행·120~121행. 통과
- 6. context 본문 절대 규칙 5에 다른 스킬을 이름으로 불러 도구가 본문을 여는 것은 예외다.
  - `plugins/plate/skills/context/SKILL.md` 18행을 읽음 → "다른 스킬을 이름으로 불러 도구가 그 스킬의 본문을 여는 것(0번의 `plate:setup`)은 예외다". 통과
- 7. run 본문에 넷이 있다: (가) `LESSONS로 옮겼다` 줄, (나) 옮겼는지는 그 줄로 본다, (다) 0번의 worktree 갈래, (라) 고칠 phase 양식.
  - `grep -n 'git log -S\|git -C' plugins/plate/skills/run/SKILL.md` → 출력 없음(종료 코드 1). 통과
  - `plugins/plate/skills/run/SKILL.md`를 읽음 → (가) 182행이 옮긴 뒤 그 줄을 적고 옮길 줄이 없거나 모두 겹쳐도 적으며, 20행 절대 규칙 5와 184행 "통과하면" 3번에 그 줄이 든다. (나) 261행, git 레포가 아니어도 같다. (다) 51~54행이 원래 자리에서 worktree 안을 고치거나 커밋하지 않고, 그 줄이 있으면 "합친다", 닫힌 검증인데 없으면 안내하고 끝나며, 240행 "합친다"의 0번 갈래도 같은 기준이다. (라) 195~197행과 양식 209~223행에 plan과 같은 테스트 먼저 기준, 읽을 것의 맥락 문서, "검증 {K}의 문제가 모두 고쳐졌다"(확인: 문제마다 적힌 곳을 다시 읽거나 돌린다)와 머리의 완료 조건이 있다. 286행의 다른 위치로 읽는 곳의 목록에 `git log -S`가 없다. 통과
- 8. `docs/TOOLS.md`의 머리글·"지금 상태" 표·훅 묶음과 `docs/ADR.md`의 ADR-018·ADR-019가 바뀐다.
  - `grep -n '멈춘 이유는 없음' docs/ADR.md` → 출력 없음(종료 코드 1). 통과
  - `docs/TOOLS.md`와 `docs/ADR.md`를 읽음 → TOOLS 3행 머리글과 9행 표가 6단계까지 적는다. 72행 종료 코드는 2만 막고 1이나 127은 막지 않는다, 73행 `python3`는 스크립트 파일을 열지 못하면 2로 끝난다, 74행 명령은 macOS와 Linux에서 `sh -c`, Windows에서 Git Bash, 없으면 PowerShell로 돈다가 출처 문서(code.claude.com/docs/en/hooks)와 함께 있다. ADR 20행 이유 끝이 "멈춘 이유는 없다.", 26행 ADR-019 트레이드오프가 "`python3`가 없거나 스크립트 파일이 없을 때 훅이 돌지 않고 규칙 구간만 남는다"다. 통과
- 9. 006의 실행 시험 여섯이 바뀐 본문으로 통과한다.
  - `python3 ~/plate-rail-test/bin/runcheck.py ~/plate-rail-test/<폴더>`를 run-vrule, run-nogit, run-small, run-all, run-wt, run-wt-gate마다 돌림 → 여섯 모두 종료 코드 0, `실패` 줄 0개, 마지막 줄 `=> 실행 대조: 모두 통과`. run-all이 낸 `(참고)` 줄 다섯(검증 2의 둘, 검증 3의 셋)은 `~/plate-rail-test/run-all/docs/LESSONS.md`에 대어 읽어 모두 같은 뜻의 줄(검증 1의 배운 것 넷과 24행, 검증 2의 9행)이 있다. 통과
  - `N=$(ls -t plugins/plate/skills/*/SKILL.md plugins/plate/hooks/* | head -1); find ~/plate-rail-test/logs -name '*.jsonl' -newer "$N"` → `N`은 `plugins/plate/skills/run/SKILL.md`(2026-10-17 19:34:37). 출력에 `run-vrule`, `run-nogit`·`run-nogit-2`, `run-small`, `run-all`·`run-all-2`·`run-all-3`, `run-wt-a`·`-b`·`-c1`·`-c2`, `run-wt-gate`가 모두 든다(그 밖에 `run-oldsetup`·`run-oldsetup-2`, `tdd-stop`, `reload-probe`). 통과
- 10. 옛 셋업에서 LESSONS 위치를 `docs/notes/lessons.md`로 답하면 run이 그 위치에 만든다.
  - `ls ~/plate-rail-test/run-oldsetup/docs/notes/lessons.md ~/plate-rail-test/run-oldsetup/docs/LESSONS.md` → 앞의 것만 있고 뒤의 것은 `No such file or directory`. 파일은 제목과 절 셋(미룬 문제는 제목만)의 LESSONS 양식이다. 통과
  - `grep -c 'docs/notes/lessons.md' ~/plate-rail-test/run-oldsetup/AGENTS.md` → `1`(11행, `docs/tasks/NNN-slug/` 행 바로 앞). 통과
  - `tail -3 ~/plate-rail-test/run-oldsetup/docs/tasks/001-gitignore/verify.md` → `**판정**: 통과`, 빈 줄, `LESSONS로 옮겼다`. 통과
  - run-oldsetup에서 `git log -1 --stat` → `11d110c [001] 검증 통과`에 `AGENTS.md`, `docs/notes/lessons.md`, `docs/tasks/001-gitignore/verify.md`가 든다. 통과
  - 완료 조건 9의 둘째 확인 → `run-oldsetup.jsonl`(위치를 묻고 멈춤)과 `run-oldsetup-2.jsonl`(`docs/notes/lessons.md`에 만들고 커밋)이 든다. 통과
- 11. 테스트 먼저 phase에서 훅이 같은 파일을 세 번째 막으면 수행은 막힘으로 멈추고 run은 정해 둔 선택지 없이 논의한다.
  - `cat ~/plate-rail-test/tdd-stop/docs/tasks/*/phase-*.md | grep -c '훅이 테스트 먼저 때문에 세 번째 막음:'` → `2`("남은 것"과 "하네스에서 걸린 것"). `.git/plate-test-first.json`의 `calc.py`는 3이다. 통과
  - `~/plate-rail-test/logs/tdd-stop.jsonl`의 마지막 `result`를 읽음 → "이 막힘에는 '다시 맡긴다 / 멈춘다' 선택지를 내지 않습니다"라고 하고, 막힌 까닭(`phase-1.md`의 "남은 것")과 수행 에이전트가 적은 해결책 둘을 보이며 까닭을 확인할 길과 고를 길을 논의한다. 통과
  - 완료 조건 9의 둘째 확인 → `tdd-stop.jsonl`이 든다. 통과
- 12. 세션 도중에 스킬 본문을 고쳤을 때 띄운 에이전트가 받는 본문이 시험으로 확인되어 `docs/TOOLS.md`에 적힌다.
  - `~/plate-rail-test/logs/reload-probe.jsonl`에서 `parent_tool_use_id`가 에이전트인 `Base directory for this skill:` 줄(17행, 45행, 74행)을 읽음 → 에이전트 1과 디스크를 고친 뒤 띄운 에이전트 2는 `표식: 자두-7391`, `/reload-plugins`가 `Reloaded: 6 plugins · 172 skills · 6 agents · 24 hooks · 0 plugin LSP servers`를 낸 뒤 띄운 에이전트 3은 `표식: 앵두-2604`를 받았다. `~/plate-rail-test/reload-probe/out-1.txt`~`out-3.txt`의 표식도 같다. `docs/TOOLS.md` 81행의 결과와 같다. 통과
- 13. `docs/LESSONS.md`에서 정한 41줄이 지워졌고 다른 줄은 그대로다.
  - `git diff ec2f192 -- docs/LESSONS.md | grep -c '^-- '` → `41`. 통과
  - `git diff ec2f192 -- docs/LESSONS.md | grep '^-- '`를 읽음 → `ec2f192`의 하네스의 문제점 32줄, 미룬 문제 5줄, 프로젝트에서 배운 것의 (004-context-rules, 검증 1) ADR-018 줄, (006-verify, 검증 1) 줄, (007-harness-issues, phase 4) `git -C` 줄, (008-tdd, phase 1) `.gitignore` 줄이다. 프로젝트에서 배운 것의 나머지 11줄은 그대로 있고, 더해진 줄은 이 작업의 phase가 통과할 때 옮긴 `(009-lessons-fixes, …)` 19줄뿐이다. 통과
- 14. 두 매니페스트의 버전이 0.9.1이다.
  - `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `  "version": "0.9.1",`. 통과
- 15. 프로젝트 전체 테스트가 모두 통과한다.
  - `python3 -m unittest discover -s tests` → `Ran 36 tests in 9.478s`, 마지막 줄 `OK`. 통과
- 테스트 먼저 기록: phase 1
  - `git show 5969331:docs/tasks/009-lessons-fixes/phase-1.md`(지운 커밋 `b5bc6c9`의 부모)의 "한 일" → 실패 출력(`FAILED (failures=4)`와 네 테스트의 단언 글) 뒤에 통과 출력(`Ran 36 tests`, `OK`)이 이 순서로 있다. phase 2~7은 "아니오"다. 통과

**문제**
- run 본문 "`docs/LESSONS.md`" 절의 옮겼는지 보는 기준(261행)은 `verify.md`의 `LESSONS로 옮겼다` 줄만 보는데, 이 줄이 생기기 전에 검증이 닫힌 작업에는 그 줄이 없다. 그런 작업에 run을 다시 부르면 "검증을 맡긴다"(167행)가 "통과하면" 1번으로 보내고, 1번(182행)은 검증 절의 줄을 다시 옮기므로, 처음 옮긴 뒤 LESSONS에서 지운 줄이 돌아온다. 261행이 적은 목적("옮긴 뒤 LESSONS에서 지운 줄이 돌아오지 않게 하는 것이다")과 반대로 된다. 이 레포의 `docs/tasks/007-harness-issues/verify.md`와 `docs/tasks/008-tdd/verify.md`가 그렇다. 두 파일 모두 그 줄이 0개이고, 이 작업이 그 검증 절에서 옮긴 하네스의 문제점 줄((007-harness-issues, 검증 1)·(검증 2), (008-tdd, 검증 1))을 LESSONS에서 지웠다. 바꾸기 전의 기준이던 `git log -S'(008-tdd, 검증 ' -- docs/LESSONS.md`는 `ec2f192` 등을 내어 옮긴 것으로 봤다 (`plugins/plate/skills/run/SKILL.md`). 기준: 결함

**배운 것**
- 없음

**하네스의 문제점**
- 이 검증의 에이전트가 `plate:verify`를 불러 받은 본문은 디스크의 `plugins/plate/skills/verify/SKILL.md`가 아니라 `9bd206e`(이 작업의 phase 3)가 고치기 전의 판이었다. 61행의 "본 결과는 통과해도 … 적는다", 65행의 다른 스킬 본문 예외, 양식 100~101행과 적는 규칙 120~121행이 없었다. 이 검증은 받은 본문대로 하되, 디스크의 판대로 "테스트 먼저 기록" 항목을 "확인"에 적었고 작업의 커밋이 바꾼 다른 스킬의 본문을 1번대로 읽었다. 이 작업이 `docs/TOOLS.md` 82행에 적은 사실(본문을 고친 세션에서 띄운 에이전트는 고치기 전의 본문을 받는다)과 같은 일이 검증에서도 되풀이됐다.
- 계획의 완료 조건 7의 (나)와 phase 4의 TODO 2는 옮겼는지 보는 기준을 `verify.md`의 줄로 바꾸면서, 그 줄 없이 이미 닫힌 작업을 어떻게 볼지 정하지 않았다. phase 4는 "확인만"으로 지나 이 갈래를 점검하지 않았고, 완료 조건 9와 10의 시험은 모두 바뀐 본문으로 다시 만든 폴더에서 새로 닫힌 작업이라 이 경우를 지나지 않는다. 위의 문제는 작업 전체를 점검하며 처음 드러났다.

**판정**: 문제 있음
