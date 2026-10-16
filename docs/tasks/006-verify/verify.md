# 검증

## 검증 1

**확인**
- `vf-pass`(run-small의 끝 상태를 복제한 폴더. phase가 모두 지워졌고 `verify.md`가 없다)에서 `/plate:verify 001`: `verify.md`가 생기고 `## 검증 1` 절에 완료 조건마다 돌린 확인과 결과, 문제, 배운 것, 하네스의 문제점, 판정 "통과"가 있다. 커밋이 하나 생기고 메시지가 `001-gitignore: 검증`이며 `verify.md`만 든다. 묻지 않는다.
  - `python3 ~/plate-rail-test/bin/runcheck.py vf-pass` → 17항목 모두 통과, "=> 실행 대조: 모두 통과". 통과
- `vf-fail`(1번의 시작 상태에서 `.gitignore`의 `*.db` 줄을 지워 커밋): 판정이 "문제 있음"이고 실패한 확인이 문제에 기준 "확인 실패"로 적힌다. `verify.md` 말고 바뀐 파일이 없다.
  - `python3 ~/plate-rail-test/bin/runcheck.py vf-fail` → 17항목 모두 통과, "=> 실행 대조: 모두 통과". 통과
- `vf-scope`(1번의 시작 상태에서 범위 밖의 무시 패턴 `*.log`를 `.gitignore`에 더해 커밋): 완료 조건의 확인은 모두 통과하고, 판정이 "문제 있음"이며 문제의 기준이 "범위"다.
  - `python3 ~/plate-rail-test/bin/runcheck.py vf-scope` → 17항목 모두 통과, "=> 실행 대조: 모두 통과". 통과
- 스킬 일곱이 불린다.
  - 적힌 그대로의 `claude -p --plugin-dir plugins/plate --output-format stream-json --verbose` → 프롬프트가 없어 "Error: Input must be provided either through stdin or as a prompt argument when using --print"로 끝나고 init 줄이 없다. phase 1, 6처럼 프롬프트 `ok`를 더한 `claude -p ok --plugin-dir plugins/plate --output-format stream-json --verbose`(2.1.301) → 다섯째 줄의 init 줄 `skills`에 `plate:setup`, `plate:context`, `plate:plan`, `plate:run`, `plate:phase`, `plate:retro`, `plate:verify`가 모두 있다. 통과
- `run-verify`(1번의 시작 상태에서 `/plate:run 001`): 수행·점검 에이전트를 띄우지 않고 검증 에이전트 하나를 띄워 1번과 같은 `verify.md`와 검증 커밋이 생긴다. 메인은 확인을 직접 돌리지 않는다.
  - `python3 ~/plate-rail-test/bin/runcheck.py run-verify` → 모두 통과. 통과
- `run-vfix`(2번의 끝 상태에서 `/plate:run 001`, 답을 미리 주지 않고 여러 턴): 문제 목록을 TODO로 담은 `phase-2.md`의 안을 보여 주고 멈추며, 그때 파일이 바뀌지 않는다. 승인 뒤 `plan: 001-gitignore 수정` 커밋에 계획 파일만 들고, 새 에이전트가 수행한 뒤 회고나 확인을 거쳐 `phase-2.md`가 지워지고, 다시 검증해 `## 검증 2`의 판정이 "통과"다.
  - `python3 ~/plate-rail-test/bin/runcheck.py run-vfix` → 모두 통과. 통과
  - `logs/run-vfix-1.jsonl`의 마지막 답글을 읽음 → 검증 1의 문제 셋을 TODO 셋으로 담은 `phase-2.md`의 안을 보이고 승인, 나중에 다룸, 멈춤 가운데 묻고 멈췄다. `logs/run-vfix-stage-a.txt`는 그때의 대조가 모두 통과다. 통과
- `run-vrule`(run-rule의 끝 상태. `AGENTS.md`에 커밋 메시지 꼴 규칙이 있고 검증이 남음)에서 `/plate:run 001`: 검증 커밋의 메시지가 프로젝트의 꼴이고, `verify.md`의 하네스의 문제점에 "프로젝트의 규칙을 따름: …"이 있으며 그 줄이 `docs/LESSONS.md`로 옮겨진다.
  - `python3 ~/plate-rail-test/bin/runcheck.py run-vrule` → 두 항목이 실패한다. "LESSONS: 제목과 절 셋이 순서대로다"(절이 프로젝트에서 배운 것, 하네스의 문제점 둘뿐이다)와 "문서 지도에 LESSONS 행이 tasks 행의 앞에 있다"(행의 글이 옛 "회고에서 배운 것과 하네스의 문제점"이다). 프로젝트 꼴 메시지와 "프로젝트의 규칙을 따름" 줄을 옮긴 항목은 통과다. "=> 실행 대조: 실패한 곳이 있음". 실패
- `run-nogit` 다시: 검증이 통과한 뒤 `done-phase-1.md`가 지워지고 작업 폴더에 `plan.md`와 `verify.md`만 남는다. `.git`이 생기지 않는다.
  - `python3 ~/plate-rail-test/bin/runcheck.py run-nogit` → 위와 같은 두 항목이 실패한다. `.git`이 없고 작업 폴더에 `plan.md`와 `verify.md`만 있는 항목은 통과다. "=> 실행 대조: 실패한 곳이 있음". 실패
- `run-small` 다시(`plan-base`의 `main`에서, 회고와 합치기를 승인): `task/001-gitignore`가 생기고 그 위에 수행, 회고, 통과, 검증의 커밋이 차례로 있다. 검증을 묻지 않는다. 합친 뒤 `main`에 그 커밋들이 있고 브랜치가 없다. 작업 폴더에 `plan.md`와 `verify.md`만 남는다.
  - `python3 ~/plate-rail-test/bin/runcheck.py run-small` → 위와 같은 두 항목이 실패한다. 브랜치를 만들고 합친 항목과 커밋 순서의 항목은 통과다. "=> 실행 대조: 실패한 곳이 있음". 실패
- `run-all` 다시: 회고도 이을지도 검증도 묻지 않고 검증까지 간다. 검증 에이전트가 작업의 모든 커밋이 바꾼 것을 읽는다. 합칠지는 묻고 멈춘다.
  - `python3 ~/plate-rail-test/bin/runcheck.py run-all` → 위와 같은 두 항목이 실패한다. 커밋 순서, 고칠 phase, 검증 절, 합치지 않은 항목은 통과다. "=> 실행 대조: 실패한 곳이 있음". 실패
  - `logs/run-all.jsonl`에서 검증 에이전트의 도구 호출과 마지막 답글을 읽음 → 검증 에이전트는 본문 두 줄 그대로를 받았고, `git log --stat 59e704e^..HEAD`로 커밋을 모은 뒤 계획 커밋 `59e704e`와 phase 1~3의 수행·회고·통과 커밋을 모두 `git show`로 읽고 완료 조건의 테스트 넷을 돌렸다. 그 기록의 마지막 답글은 검증 1의 "문제 있음"에 고칠 `phase-4.md`의 안을 보이고 멈춘 것이고, 둘째 턴 `logs/run-all-2.jsonl`의 마지막 답글이 합칠 브랜치 `task/001-core-commands`와 합칠 곳 `main`을 보이고 묻는다. 통과
- `run-wt` 다시: worktree에서 모든 phase가 지워지면 그 자리에서 검증까지 끝난다. 원래 자리에서 부르면 합칠지 묻고, 승인 뒤 합쳐지고 worktree와 브랜치가 없다. `run-wt-gate`(worktree의 `verify.md`를 지운 커밋을 넣고 원래 자리에서 부름): 합치지 않고 worktree에서 run을 부르라고 안내한다.
  - `python3 ~/plate-rail-test/bin/runcheck.py run-wt` → 모두 통과. 통과
  - `python3 ~/plate-rail-test/bin/runcheck.py run-wt-gate` → 모두 통과. 통과
- `plan-test`(run-all의 끝 상태처럼 테스트가 있는 프로젝트에 작은 요청을 계획): 완료 조건에 프로젝트 전체 테스트를 돌리는 조건이 있다.
  - `python3 ~/plate-rail-test/bin/plancheck.py plan-test` → 15항목 모두 통과. 이 꼴에는 전체 테스트 조건을 보는 항목이 없어, phase 4가 쓴 `--base 157d775 --fulltest` 인자를 더해 다시 돌림 → 21항목 모두 통과("마지막 완료 조건의 확인이 전체 테스트다", "phase-1.md: 통과 조건이 완료 조건 5을 가리킨다"). `plan-test/docs/tasks/002-list-command/plan.md`의 완료 조건 5가 "프로젝트 전체 테스트가 모두 통과한다"이고 확인이 `.venv/bin/python -m pytest`다. 통과
- setup이 규칙 구간을 넣는다. 새 프로젝트(`setup-fresh`)의 `AGENTS.md`에 표식으로 감싼 규칙 구간이 문서 지도 구간 뒤에 있고, 다시 돌려도 바뀌지 않는다. 구간이 없는 셋업된 프로젝트(`setup-remap`)에서는 더하는 행이 표에 나오고 승인 뒤 더해지며, 지도 구간의 사용자 행은 그대로다.
  - `python3 ~/plate-rail-test/bin/setupcheck.py setup-fresh PRD,ARCHITECTURE,ADR` → 11항목 모두 통과. 통과
  - `git -C ~/plate-rail-test/setup-fresh status --short` → 출력 없음. HEAD는 `5c2246e 셋업 직후`(11:36:41)이고 다시 돌린 기록 `logs/setup-fresh-rerun.jsonl`은 그 뒤 11:36~11:43이다. 통과
  - `git -C ~/plate-rail-test/setup-remap diff` → `AGENTS.md`의 끝 표식 뒤에 빈 줄과 규칙 구간 6줄만 더해졌다. 지도 구간의 사용자 행(`docs/LESSONS.md` | 회고에서 배운 것과 하네스의 문제점)은 그대로다. 통과
- 자기 적용(이 레포에서 `004-context-rules`를 run으로 검증): 004의 폴더에 `plan.md`와 `verify.md`가 있고 검증이 닫혔다(마지막 판정이 "통과"이거나, 마지막 검증 절 아래에 미룬다는 줄이 있다). 브랜치 `verify`에서 불렀으므로 새 브랜치가 생기지 않는다.
  - `ls docs/tasks/004-context-rules/` → `plan.md`, `verify.md`. 통과
  - `git log --format=%s | grep '^004-context-rules: 검증'` → `004-context-rules: 검증`이 있다(그 밖에 `… 검증 1의 문제를 미룸`, `… 검증 1 미룸`). `git branch` → `context`, `fix-lessons`, `main`, `plan`, `rail`, `run`, `verify`. `task/004-context-rules`가 없다. 통과
  - 두 세션의 기록(`~/.claude/projects/-Users-gangjungi-Desktop-harness-plate/f7cfecb6-….jsonl`, `cbf0b287-….jsonl`)에서 메인 세션의 도구 호출을 읽음 → 첫 세션은 검증 에이전트 하나에 본문 두 줄 그대로를 넘겼고 완료 조건의 확인을 돌리지 않았다. 그 뒤 메인이 고친 파일은 사용자의 지시에 따른 `docs/LESSONS.md`(`f3a20b4`, 되돌림 `55dd705`)와 사용자가 고치라고 한 계획(`plan.md`, `phase-5.md`), run과 verify의 본문, `AGENTS.md`다. 둘째 세션은 에이전트를 띄우지 않았고 메인이 고친 파일은 `verify.md`(미룬다는 줄)와 `docs/LESSONS.md`뿐이다(`cbb3ce0`). `verify.md`의 마지막 검증 절 아래에 "사용자가 남은 문제를 나중에 다루기로 했다"가 있다. 통과
- 이 레포의 문서가 스킬 일곱과 검증을 말하고, PRD가 규칙 수준의 막는 장치를 말한다.
  - `grep -c 'verify' README.md plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json docs/ARCHITECTURE.md` → 4, 1, 1, 5. 통과
  - `grep -n '만들기 전\|강제로' docs/PRD.md docs/ARCHITECTURE.md` → 출력 없음. 통과
  - `grep -n '훅' docs/PRD.md` → 23행, 범위 밖의 "훅(계획 없는 편집, 검증 없는 종료를 도구가 막는 장치). v1.0 뒤에 한다." 통과
- 두 매니페스트의 버전이 0.8.0이다.
  - `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "0.8.0",`. 통과
- 이 레포의 `AGENTS.md`에 규칙 구간이 있고 문서 지도 구간은 그대로다.
  - setup 본문 "규칙 구간" 절의 코드 블록 안쪽이 `AGENTS.md`의 부분 문자열인지 파이썬으로 봄 → 참. 통과
  - `git diff 0def138 -- AGENTS.md`(phase 5 통과 커밋) → 끝 표식 뒤의 빈 줄과 규칙 구간 6줄만 더해졌다. 통과

**문제**
- 완료 조건 7의 확인 `runcheck.py run-vrule`이 실패한다. 시험 폴더의 `docs/LESSONS.md`에 `## 미룬 문제` 절이 없고 문서 지도의 LESSONS 행이 옛 글이다. 이 상태는 run 본문에 미루는 길과 새 LESSONS 양식을 더한 `de62793`(2026-10-16 11:25) 전인 2026-10-15 23:35에 만든 것이고, 바뀐 본문으로 다시 돌리지 않았다 (`~/plate-rail-test/run-vrule/`, `plugins/plate/skills/run/SKILL.md`). 기준: 확인 실패
- 완료 조건 8의 확인 `runcheck.py run-nogit`이 같은 두 항목에서 실패한다. 상태는 `de62793` 전인 2026-10-15 23:08에 만든 것이다 (`~/plate-rail-test/run-nogit/`, `plugins/plate/skills/run/SKILL.md`). 기준: 확인 실패
- 완료 조건 9의 확인 `runcheck.py run-small`이 같은 두 항목에서 실패한다. 상태는 `de62793` 전인 2026-10-15 23:38~23:48에 만든 것이다 (`~/plate-rail-test/run-small/`, `plugins/plate/skills/run/SKILL.md`). 기준: 확인 실패
- 완료 조건 10의 확인 `runcheck.py run-all`이 같은 두 항목에서 실패한다. 상태는 `de62793` 전인 2026-10-15 23:38~10-16 00:19에 만든 것이다 (`~/plate-rail-test/run-all/`, `plugins/plate/skills/run/SKILL.md`). 기준: 확인 실패
- run 본문 "검증을 맡긴다"의 첫 갈래는 닫힌 검증이면 "통과하면"의 1~3(LESSONS로 옮기기, `done-phase-N.md` 지우기, 커밋)을 건너뛰고 4번으로 간다. 검증 에이전트가 판정 "통과"의 `verify.md`를 커밋한 뒤 run이 1~3을 하기 전에 세션이 끊기면, 다시 부른 run은 검증 절을 LESSONS로 옮기지 않고, git 레포가 아니면 `done-phase-N.md`를 지우지 않는다. 그 작업은 끝나지 않은 작업도 검증이 남은 작업도 아니라서 번호 없이 부르면 찾지도 않는다. 같은 본문의 "세션을 끊고 다시 불러도 파일만 보고 잇는다"와 머리의 결정 "git 레포가 아니면 검증이 닫힌 뒤 `done-phase-N.md`를 지운다"에 어긋난다 (`plugins/plate/skills/run/SKILL.md`). 기준: 결함

**배운 것**
- `~/plate-rail-test`에서 완료 조건 1~3, 5, 7~11의 시험 폴더는 run-vfix를 빼고 모두 `de62793`(run과 verify에 미루는 길) 전의 본문으로 만든 상태다. 지금의 판정 도구로 대조해 통과한 경우(vf 셋, run-verify, run-wt, run-wt-gate)도 바뀐 본문으로 돌린 결과는 아니다. 다시 돌리려면 `bin/vfmake.sh`로 폴더를 다시 만들고 `bin/rerun.sh`로 돌린다. run-nogit은 `rerun.sh`에 갈래가 없어 `bin/run.sh`에 `answers/run-nogit.md`를 주어 돌린다.

**하네스의 문제점**
- 계획의 phase 5: 같은 phase에서 run 본문(LESSONS 양식, 미루는 길)을 고쳤는데 통과 조건이 완료 조건 14만 가리켰고, TODO의 "걸리는 판정이 다시 통과한다"는 run-vfix와 setup 둘만 다시 돌렸다. phase 5의 기록이 "LESSONS를 만드는 다른 경우(run-small 등)의 옛 결과를 다시 대조하면 그 두 줄이 실패한다"고 적고도 통과로 지워져, 완료 조건 7~10의 실패가 검증에서야 드러났다. 이 작업의 phase는 세션이 직접 수행해 따로 점검하는 에이전트가 없었다(머리의 결정).
- 계획의 완료 조건 12: 확인 `plancheck.py plan-test`를 적힌 대로 돌리면 전체 테스트 조건을 보는 항목이 없어, 그 조건이 없어도 통과한다. plan 스킬 "적는 규칙"의 "조건의 일부만 보는 확인은 그 조건을 확인하지 못한다"에 걸린다. phase 4는 `--base`, `--fulltest` 인자를 더해 돌렸다.
- 계획의 완료 조건 4: 확인 명령에 프롬프트가 없어 적힌 대로는 init 줄이 나오지 않고 오류로 끝난다. phase 1과 6은 `ok`를 더해 돌렸다.

**판정**: 문제 있음
