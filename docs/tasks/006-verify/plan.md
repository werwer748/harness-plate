# 레일 5단계: 검증 스킬 (verify)

## 요청
다음 작업 시작하자

## 목표
작업 전체를 완료 조건에 대어 보고 `verify.md`를 남기는 검증 스킬(`plate:verify`)이 있고, run이 마지막 phase를 지운 뒤 묻지 않고 그것을 맡긴다. 검증을 통과하지 않은 작업은 기본 브랜치에 합쳐지지 않는다. setup이 `AGENTS.md`에 "계획부터, 검증까지"의 규칙 구간을 넣고, 이 레포의 `004-context-rules`가 run으로 검증된다.

## 범위 밖
- 훅(계획 없는 편집, 검증 없는 종료를 도구가 막는 장치). v1.0 뒤에 한다
- 종료 차단 훅이 없는 도구(Grok Build)에서 검증 증거를 지키는 방법, Codex에서의 확인. 도구를 넓힐 때 v1.0 뒤에 한다
- `005-run`의 검증. 005 완료 조건 20의 grep이 setup 양식의 `### ADR-001:`에 늘 걸리는 것도 함께 둔다
- 이 레포의 001~003, 005가 검증이 남은 작업으로 보이는 것. v1.0에서 지울 기록이라 손대지 않고, 이 레포에서는 run을 번호와 함께 부른다
- phase가 하나뿐인 작업에서 회고와 검증이 겹치는 것
- 끝나지 않은 작업이 쌓이는 것을 막는 것
- ADR 번호. 다음 항목은 있는 번호 뒤(ADR-019)에 잇는다
- 4단계 판정 가운데 바뀐 동작에 걸리지 않는 것(run-big, run-skip, run-fix, run-wrong, run-resume, run-rule, run-dirty, run-noplan, run-lessons, run-ev)을 다시 돌리는 것
- second brain 추천과 `docs/LESSONS.md`를 줄이는 일. 5단계 뒤의 추가 기능이다
- `main` 병합. 끝에 따로 확인받는다

## 완료 조건
1. `vf-pass`(run-small의 끝 상태를 복제한 폴더. phase가 모두 지워졌고 `verify.md`가 없다)에서 `/plate:verify 001`: `verify.md`가 생기고 `## 검증 1` 절에 완료 조건마다 돌린 확인과 결과, 문제, 배운 것, 하네스의 문제점, 판정 "통과"가 있다. 커밋이 하나 생기고 메시지가 `001-gitignore: 검증`이며 `verify.md`만 든다. 묻지 않는다.
   - 확인: `runcheck.py vf-pass` → 모두 통과
2. `vf-fail`(1번의 시작 상태에서 `.gitignore`의 `*.db` 줄을 지워 커밋): 판정이 "문제 있음"이고 실패한 확인이 문제에 기준 "확인 실패"로 적힌다. `verify.md` 말고 바뀐 파일이 없다.
   - 확인: `runcheck.py vf-fail` → 모두 통과
3. `vf-scope`(1번의 시작 상태에서 범위 밖의 무시 패턴 `*.log`를 `.gitignore`에 더해 커밋): 완료 조건의 확인은 모두 통과하고, 판정이 "문제 있음"이며 문제의 기준이 "범위"다.
   - 확인: `runcheck.py vf-scope` → 모두 통과
4. 스킬 일곱이 불린다.
   - 확인: `claude -p --plugin-dir plugins/plate --output-format stream-json --verbose`의 init 줄에 `plate:setup`, `plate:context`, `plate:plan`, `plate:run`, `plate:phase`, `plate:retro`, `plate:verify`가 있다
5. `run-verify`(1번의 시작 상태에서 `/plate:run 001`): 수행·점검 에이전트를 띄우지 않고 검증 에이전트 하나를 띄워 1번과 같은 `verify.md`와 검증 커밋이 생긴다. 메인은 확인을 직접 돌리지 않는다.
   - 확인: `runcheck.py run-verify` → 모두 통과
6. `run-vfix`(2번의 끝 상태에서 `/plate:run 001`, 답을 미리 주지 않고 여러 턴): 문제 목록을 TODO로 담은 `phase-2.md`의 안을 보여 주고 멈추며, 그때 파일이 바뀌지 않는다. 승인 뒤 `plan: 001-gitignore 수정` 커밋에 계획 파일만 들고, 새 에이전트가 수행한 뒤 회고나 확인을 거쳐 `phase-2.md`가 지워지고, 다시 검증해 `## 검증 2`의 판정이 "통과"다.
   - 확인: `runcheck.py run-vfix` → 모두 통과
   - 확인: `logs/run-vfix-*.jsonl`에서 고칠 phase의 안을 보인 답글을 읽는다
7. `run-vrule`(run-rule의 끝 상태. `AGENTS.md`에 커밋 메시지 꼴 규칙이 있고 검증이 남음)에서 `/plate:run 001`: 검증 커밋의 메시지가 프로젝트의 꼴이고, `verify.md`의 하네스의 문제점에 "프로젝트의 규칙을 따름: …"이 있으며 그 줄이 `docs/LESSONS.md`로 옮겨진다.
   - 확인: `runcheck.py run-vrule` → 모두 통과
8. `run-nogit` 다시: 검증이 통과한 뒤 `done-phase-1.md`가 지워지고 작업 폴더에 `plan.md`와 `verify.md`만 남는다. `.git`이 생기지 않는다.
   - 확인: `runcheck.py run-nogit` → 모두 통과
9. `run-small` 다시(`plan-base`의 `main`에서, 회고와 합치기를 승인): `task/001-gitignore`가 생기고 그 위에 수행, 회고, 통과, 검증의 커밋이 차례로 있다. 검증을 묻지 않는다. 합친 뒤 `main`에 그 커밋들이 있고 브랜치가 없다. 작업 폴더에 `plan.md`와 `verify.md`만 남는다.
   - 확인: `runcheck.py run-small` → 모두 통과
10. `run-all` 다시: 회고도 이을지도 검증도 묻지 않고 검증까지 간다. 검증 에이전트가 작업의 모든 커밋이 바꾼 것을 읽는다. 합칠지는 묻고 멈춘다.
    - 확인: `runcheck.py run-all` → 모두 통과
    - 확인: `logs/run-all.jsonl`에서 검증 에이전트가 읽은 범위와 마지막 답글을 읽는다
11. `run-wt` 다시: worktree에서 모든 phase가 지워지면 그 자리에서 검증까지 끝난다. 원래 자리에서 부르면 합칠지 묻고, 승인 뒤 합쳐지고 worktree와 브랜치가 없다. `run-wt-gate`(worktree의 `verify.md`를 지운 커밋을 넣고 원래 자리에서 부름): 합치지 않고 worktree에서 run을 부르라고 안내한다.
    - 확인: `runcheck.py run-wt` → 모두 통과
    - 확인: `runcheck.py run-wt-gate` → 모두 통과
12. `plan-test`(run-all의 끝 상태처럼 테스트가 있는 프로젝트에 작은 요청을 계획): 완료 조건에 프로젝트 전체 테스트를 돌리는 조건이 있다.
    - 확인: `plancheck.py plan-test` → 모두 통과
13. setup이 규칙 구간을 넣는다. 새 프로젝트(`setup-fresh`)의 `AGENTS.md`에 표식으로 감싼 규칙 구간이 문서 지도 구간 뒤에 있고, 다시 돌려도 바뀌지 않는다. 구간이 없는 셋업된 프로젝트(`setup-remap`)에서는 더하는 행이 표에 나오고 승인 뒤 더해지며, 지도 구간의 사용자 행은 그대로다.
    - 확인: `setupcheck.py setup-fresh PRD,ARCHITECTURE,ADR` → 모두 통과
    - 확인: setup-fresh에서 다시 돌린 뒤 `git status --short` → 출력 없음
    - 확인: setup-remap의 `git diff` → 규칙 구간만 더해졌다
14. 자기 적용(이 레포에서 `004-context-rules`를 run으로 검증): 004의 폴더에 `plan.md`와 `verify.md`가 있고 검증이 닫혔다(마지막 판정이 "통과"이거나, 마지막 검증 절 아래에 미룬다는 줄이 있다). 브랜치 `verify`에서 불렀으므로 새 브랜치가 생기지 않는다.
    - 확인: `ls docs/tasks/004-context-rules/` → `plan.md`, `verify.md`
    - 확인: `git log --format=%s`에 `004-context-rules: 검증`이 있고 `git branch`에 `task/004-context-rules`가 없다
    - 확인: 그 세션의 기록에서 메인이 직접 고친 파일과 검증 에이전트에게 넘긴 글을 읽는다
15. 이 레포의 문서가 스킬 일곱과 검증을 말하고, PRD가 규칙 수준의 막는 장치를 말한다.
    - 확인: `grep -c 'verify' README.md plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json docs/ARCHITECTURE.md` → 모두 1 이상
    - 확인: `grep -n '만들기 전\|강제로' docs/PRD.md docs/ARCHITECTURE.md` → 출력 없음
    - 확인: `grep -n '훅' docs/PRD.md` → 범위 밖에 "v1.0 뒤"의 줄이 있다
16. 두 매니페스트의 버전이 0.8.0이다.
    - 확인: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `0.8.0`
17. 이 레포의 `AGENTS.md`에 규칙 구간이 있고 문서 지도 구간은 그대로다.
    - 확인: setup 본문의 규칙 구간 블록이 `AGENTS.md`에 글자 그대로 있다
    - 확인: phase 6이 시작할 때의 커밋과 견준 `git diff -- AGENTS.md`에 규칙 구간만 더해졌다

## 결정
- 검증은 새 스킬 `plate:verify`가 맡고, run이 마지막 phase를 지운 뒤 묻지 않고 새 에이전트에게 맡긴다. 이유: 수행한 쪽이 완료를 선언하지 않게 한다. 검증을 거절할 수 있으면 아무것도 남지 않아 "검증 없는 완료 선언"이 열린다.
- 검증은 완료 조건의 확인을 모두 다시 돌리고, 작업 전체의 변경을 머리(목표, 범위 밖, 결정)·맥락 문서·결함에 대어 점검하며, 바뀐 구조가 맥락 문서에 빠졌는지 본다. 이유: 전체 지시로 실행하면 코드 점검이 한 번도 없고, phase 회고는 phase 사이에 걸친 어긋남과 계획이 빠뜨린 문서 고치기를 보지 못한다.
- 프로젝트 전체 테스트는 plan이 테스트가 있는 프로젝트의 완료 조건에 넣고, 검증은 완료 조건에 적힌 것만 돌린다. 이유: 사용자가 초안에서 명령을 보고 승인하고, 검증이 명령을 추측하지 않는다.
- `verify.md`는 회고 절과 같은 꼴의 `## 검증 N` 절을 쌓고, 마지막 판정이 작업의 상태다. 통과하면 run이 배운 것과 하네스의 문제점을 `docs/LESSONS.md`로 옮긴다. 이유: 꼴을 하나 더 익히지 않아도 되고, 작업 단위에서 찾은 하네스의 문제도 남는다.
- 검증이 "문제 있음"이면 run이 문제 목록을 TODO로 담은 새 phase의 안을 보여 주고 승인받는다. 전체 지시여도 멈춘다. 이유: 코드를 고치는 일은 모두 phase를 거치고, 계획은 승인 없이 고치지 않는다.
- 검증의 문제를 사용자가 나중에 다루겠다고 하면 run은 고칠 phase를 더하지 않는다. `verify.md`의 마지막 검증 절 아래에 "사용자가 남은 문제를 나중에 다루기로 했다"를 적어 검증을 닫고, 통과했을 때처럼 `docs/LESSONS.md`로 옮긴 뒤(문제는 새 절 "미룬 문제"로) 합칠지 묻는다. 이유: 지난 작업 폴더에 phase가 쌓이지 않고, 미룬 문제는 회고 때 다룬다. 004의 자기 적용에서 사용자가 정했다.
- phase 파일이 없고 마지막 판정이 통과인 `verify.md`도 없는 작업 폴더를 "검증이 남은 작업"으로 보고, run이 그것을 찾아 검증으로 간다. "끝나지 않은 작업"과 worktree의 기준은 그대로다. 이유: worktree는 두 작업의 코드 변경이 섞이는 것을 막으려는 것이라 phase 기준이 맞다.
- run은 기본 브랜치에서 시작하면 `task/NNN-slug`를 만들어 실행하고, 검증이 통과하면 합칠지 묻는다. worktree의 합치기도 판정이 통과인 `verify.md`가 있을 때만 묻는다. 이유: 검증하지 않은 작업이 기본 브랜치에 들어가지 않게 하고, 실행 환경의 기본 안내("기본 브랜치면 브랜치부터")와 phase 스킬이 부딪힌 일(4단계 판정에서 세 번)을 없앤다.
- 합칠지는 전체 지시여도 묻는다. 이유: 기본 브랜치를 바꾸는 일이다. (추천안으로 정함)
- git 레포가 아니면 검증이 통과한 뒤 `done-phase-N.md`를 지운다. 이유: 기록이 쌓이는 것을 막는다.
- 막는 장치는 setup이 `AGENTS.md`에 넣는 규칙 구간(코드를 고치는 요청은 계획부터, 작업은 검증이 통과해야 끝난다)이고 훅은 만들지 않는다. 이유: 세 도구가 모두 `AGENTS.md`를 읽고 서브에이전트에도 실린다. 훅은 Claude Code에서만 도는 코드이고, 탈출구가 없어 잘못 막으면 판정과 setup까지 멈춘다.
- 프로젝트의 규칙이 단계를 건너뛰라고 해도 따르지 않는다. verify와 규칙 구간도 같다. 이유: PRD가 파이프라인을 건너뛰는 예외 경로를 범위 밖에 두었다.
- 이 레포의 `AGENTS.md`에도 마지막 phase에서 setup을 다시 돌려 규칙 구간을 넣는다. 이유: 이 레포도 하네스를 쓰는 프로젝트이고, 006의 phase는 그 전에 끝나므로 직접 수행과 부딪히지 않는다.
- 이 작업의 phase는 세션이 `phase-N.md`를 읽고 직접 수행하고, 통과 커밋에서 "하네스에서 걸린 것"을 `docs/LESSONS.md`로 옮긴다. 이유: 5단계는 run과 그 짝 스킬을 고치는 단계이고, 4단계 phase 8의 두 항목이 파일과 함께 지워졌다.
- 판정은 헤드리스 실행에 요청과 답 파일을 주어 돌리고 판정 도구(`~/plate-rail-test/bin/`의 `runcheck.py`, `plancheck.py`, `setupcheck.py`)로 본다. 4단계 경우는 바뀐 동작에 걸리는 것만 기대를 고쳐 다시 돌린다. 이유: 경우 하나가 80~1300초였고, 바뀌지 않은 동작은 다시 볼 까닭이 없다.
- 자기 적용은 사용자가 `claude --plugin-dir plugins/plate`로 연 새 세션에서 `/plate:run 004`를 불러서 하고, 확인은 다른 세션이 그 세션의 기록과 커밋을 읽어서 한다. 이유: 기대값이 적힌 계획을 읽지 않은 세션이 돌려야 "스킬만 보고 그렇게 했다"가 근거가 된다.
- 커밋은 브랜치 `verify`에 하고 phase가 통과할 때마다 `origin/verify`로 푸시한다. 버전은 0.8.0이다. 이유: 4단계와 같은 방식이다.
