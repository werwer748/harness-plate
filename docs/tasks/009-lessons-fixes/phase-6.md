# Phase 6: 006의 실행 시험 여섯을 다시 돌린다

**목표**: 006의 실행 시험 여섯이 바뀐 본문으로 다시 돌아 `runcheck.py`에 실패한 항목이 없다.

**테스트 먼저**: 아니오 — 이 레포의 코드를 바꾸지 않고 시험 폴더에서 시험을 돌린다

**읽을 것**
- `~/plate-rail-test/bin/vfmake.sh`, `bin/rerun.sh`, `bin/run.sh`, `bin/runcheck.py` (시험 폴더를 만들고, 돌리고, 판정하는 도구)
- `~/plate-rail-test/answers/` (시험마다 미리 주는 답)
- `git show a0be6c4^:docs/tasks/006-verify/plan.md`의 완료 조건 7~11 (여섯 시험이 보는 것과 run-wt-gate를 만드는 꼴)
- `git show ec2f192:docs/LESSONS.md`의 미룬 문제 절 (006-verify, 검증 1)의 네 줄과, 프로젝트에서 배운 것 절의 (006-verify, 검증 1) 줄
- `docs/TOOLS.md`의 Claude Code 절 (헤드리스 실행의 꼴, 허용 목록, 실행 시간, 폴더가 다르면 한꺼번에 돌려도 된다)
- `plugins/plate/skills/run/SKILL.md` (phase 4가 바꾼 0번, "통과하면", "고칠 phase를 더한다", "`docs/LESSONS.md`" 절)

**TODO**
- [x] run-vrule, run-nogit, run-small, run-all이 `bin/vfmake.sh`로 다시 만들어지고 바뀐 본문으로 돌아 `runcheck.py`에 실패한 항목이 없다. 옛 셋업을 바탕으로 한 폴더가 LESSONS의 위치를 물으면 `docs/LESSONS.md`로 답하는 턴을 잇는다 (`~/plate-rail-test/`)
- [x] run-wt와 run-wt-gate가 다시 만들어지고 돌아 `runcheck.py`에 실패한 항목이 없다. run-wt는 worktree에서 검증이 닫힌 뒤 원래 자리에서 부르면 합칠지 묻고, run-wt-gate는 worktree에 닫힌 검증이 없어 그 worktree에서 run을 부르라고 안내한다 (`~/plate-rail-test/`)
- [x] `runcheck.py`의 기대 가운데 이 작업의 결정이 바꾼 동작(`verify.md`의 `LESSONS로 옮겼다` 줄, 고칠 phase 양식, 0번의 worktree 갈래)에 걸리는 것만 고쳐지고, 고친 곳과 까닭이 phase 기록에 적힌다 (`~/plate-rail-test/bin/runcheck.py`)

**통과 조건**
- 완료 조건 9가 참이다.
  - 확인: 완료 조건 9의 확인을 모두 돌린다

## 한 일
- run-vrule, run-nogit, run-small, run-all이 다시 만들어지고 돌았다: `zsh bin/vfmake.sh run-vrule run-nogit run-small run-all run-wt`로 다시 만들고, 2.1.302에서 폴더마다 한꺼번에 돌렸다. 모두 `runcheck.py`에 실패한 항목이 없다 (`~/plate-rail-test/bin/vfmake.sh`, `~/plate-rail-test/answers/run-nogit-2.md`, `~/plate-rail-test/answers/run-all-3.md`, `~/plate-rail-test/logs/run-*.jsonl`)
  - run-vrule(`rerun.sh`, 202초): 검증 1 통과. LESSONS로 옮기고 `LESSONS로 옮겼다`를 적어 `[001] 검증 통과`로 커밋했다. vrule-base의 LESSONS가 옛 양식이라 `vfmake.sh`의 run-vrule 갈래에서 그 양식을 지금 것으로 맞췄다(계획과 달라진 점).
  - run-nogit(`bin/run.sh`. `rerun.sh`에 갈래가 없다): 첫 턴(105초)은 phase 1을 확인만으로 통과시킨 뒤 옛 셋업이라 LESSONS의 위치를 묻고 멈췄다. `--resume`으로 "`docs/LESSONS.md`에 만든다."를 보낸 둘째 턴(111초, `logs/run-nogit-2.jsonl`)이 문서 지도에 행을 더해 LESSONS를 만들고, 검증 1 통과 뒤 `done-phase-1.md`를 지우고 `LESSONS로 옮겼다`를 적었다.
  - run-small(`rerun.sh`, 511초): 수행, 회고, 통과, 검증, 검증 통과의 커밋 다섯 뒤 `main`에 합치고 브랜치를 지웠다.
  - run-all(`rerun.sh` 1617초 + 셋째 턴 689초): 검증 1이 "문제 있음"(테스트가 DB를 직접 연다)이라 둘째 턴이 phase 4의 안을 승인했다. phase 4는 고친 뒤 테스트를 약하게 만들어 검증 2도 "문제 있음"이었고, run이 phase 5의 안(테스트 먼저 "예")을 보이고 멈췄다. 같은 세션에 "승인한다."를 보낸 셋째 턴(`logs/run-all-3.jsonl`)이 phase 5를 수행하고 검증 3이 통과해, `LESSONS로 옮겼다`를 적고 합칠지 묻고 멈췄다.
- run-wt와 run-wt-gate가 다시 만들어지고 돌았다 (`zsh bin/rerun.sh run-wt`. `~/plate-rail-test/logs/run-wt-*.jsonl`)
  - run-wt-a(28초): 원래 자리에서 worktree `.worktrees/002-readme`를 만들고 그 폴더에서 다시 부르라고 안내했다. `logs/run-wt-stage-a.txt`는 모두 통과다.
  - run-wt-b(528초): worktree에서 phase 1, 검증 1 통과, LESSONS로 옮김, `LESSONS로 옮겼다`, `002-readme: 검증 통과`까지 했다. `logs/run-wt-stage-b.txt`는 모두 통과다(합친 뒤에는 worktree가 없어 `--stage b`를 다시 돌리면 실패한다).
  - run-wt-gate(162초): worktree의 `verify.md`를 지운 커밋을 넣은 복제에서, 원래 자리의 run이 파일을 고치지 않고 에이전트도 띄우지 않고 "그 worktree에서 `/plate:run 002`를 부르라"고 안내했다.
  - run-wt-c1(182초): 원래 자리에서 worktree의 `verify.md`에 `LESSONS로 옮겼다`가 있는 것을 보고 합칠지 물었다. run-wt-c2(30초): 합치고 worktree와 브랜치를 지웠다.
- `runcheck.py`의 기대가 바뀐 동작에 맞춰 고쳐졌다 (`~/plate-rail-test/bin/runcheck.py`. 고치기 전의 파일은 `/private/tmp/claude-501/-Users-gangjungi-Desktop-harness-plate/b192ee3b-310c-4aa4-8b55-b5691a600b2d/scratchpad/runcheck.py.orig`)
  - `LESSONS로 옮겼다` 줄(완료 조건 7의 (가)): 메인이 직접 고쳐도 되는 파일에 `verify.md`를 더했다(`MAIN_MAY_EDIT`). 검증 통과 커밋에 `verify.md`가 들어도 되고 꼭 들어야 하게 했다. 통과로 끝나는 실행에서는 검증 통과 커밋이 꼭 하나 있게 했다(전에는 0개도 됐다). 마지막 검증 절 아래에 그 줄이 하나 있는지 보는 항목(`check_moved_line`)을 run과 run-nogit의 검증에 더했다. 프로젝트의 커밋 꼴을 쓰는 경우(run-vrule)는 든 파일로 커밋을 가르는데, 검증 통과 커밋도 `verify.md`만 들 수 있어 검증 절(`+## 검증 N`)을 더한 커밋만 검증 커밋으로 보게 했다. 고친 판정 도구를 다시 만들기 전의 옛 상태에 돌려 새 항목들이 실패하는 것을 먼저 봤다.
  - worktree의 세션이 고친 파일(완료 조건 7의 (가)): worktree의 세션도 `verify.md`에 그 줄을 적는데, 끝 판정이 그 기록의 편집 경로를 원래 자리에 대어 읽어 `.worktrees/002-readme/…`로 보고 실패했다. 그 기록만 worktree에 대어 읽게 했다(`check_logs`의 `edit_root`, `check_git_run`의 `log_root`). 원래 자리의 실행들이 worktree 안을 고치지 않았는지 보는 항목은 그대로다.
  - 고칠 phase 양식(완료 조건 7의 (라)): 더한 phase마다 `**테스트 먼저**:` 줄, 읽을 것에 그때 문서 지도의 맥락 문서가 모두 있는지, 통과 조건에 "검증 K의 문제가 모두 고쳐졌다"와 머리의 완료 조건이 함께 있는지 보는 항목을 더했다.
  - 검증 절의 "테스트 먼저 기록" 항목(완료 조건 5의 (다)): 확인 블록에서 `- 테스트 먼저 기록: phase N` 항목은 완료 조건의 항목으로 세지 않고, 그 아래 줄이 "→ 결과. 통과|실패"로 끝나는지 따로 보게 했다. run-all의 검증 3이 phase 5의 그 항목을 적었다.
  - run-all이 고칠 phase를 두 번 더한 것(계획과 달라진 점): 계획 고침 커밋마다 새 phase 파일 하나를 더했는지와 위의 양식 항목을 커밋마다 보게 했고, run-all의 경우에 `run-all-3` 기록과 검증 절 셋을 적었다.
  - LESSONS로 옮긴 줄의 수(계획과 달라진 점): 검증 절의 줄 수와 꼭 같기를 바라던 것을 그보다 많지 않기로 바꾸고, LESSONS에 글자 그대로 없는 줄을 읽을 것으로 내게 했다. run은 같은 뜻의 줄이 같은 절에 이미 있으면 더하지 않는다(007-harness-issues phase 2). run-all에서 빠진 다섯 줄(검증 2에서 둘, 검증 3에서 셋)을 읽었다. 모두 앞서 옮긴 줄을 다시 적은 것이다: 검증 1의 배운 것 넷이 그대로 맞다는 줄(둘), 검증 1의 "테스트 먼저 항목이 없을 때" 줄(둘), 검증 2의 "테스트가 DB를 직접 열지 않는다" 줄(하나).
  - run-nogit이 두 턴으로 돈 것(계획과 달라진 점): run-nogit의 경우에 `run-nogit-2` 기록을 더했다.

## 확인 결과
- 완료 조건 9가 참이다.
  - `python3 ~/plate-rail-test/bin/runcheck.py <폴더>`를 여섯 폴더마다 돌렸다 → run-vrule 37 통과 0 실패, run-nogit 20 통과 0 실패, run-small 50 통과 0 실패, run-all 127 통과 0 실패, run-wt 50 통과 0 실패, run-wt-gate 7 통과 0 실패. 여섯 모두 마지막 줄이 `=> 실행 대조: 모두 통과`이고 종료 코드 0. 통과
  - `N=$(ls -t plugins/plate/skills/*/SKILL.md plugins/plate/hooks/* | head -1); find ~/plate-rail-test/logs -name '*.jsonl' -newer "$N"` → `N`은 `plugins/plate/skills/run/SKILL.md`(19:34)이고, `run-vrule`, `run-nogit`, `run-nogit-2`, `run-small`, `run-all`, `run-all-2`, `run-all-3`, `run-wt-a`, `run-wt-b`, `run-wt-gate`, `run-wt-c1`, `run-wt-c2`의 `.jsonl` 12개가 나왔다. 여섯 시험의 기록이 모두 든다. 통과

## 계획과 달라진 점
- 계획은 `vfmake.sh`로 폴더를 다시 만들어 돌리면 된다고 했지만, run-vrule은 `vfmake.sh`의 run-vrule 갈래를 고쳐 만들었다. vrule-base의 `docs/LESSONS.md`에 `## 미룬 문제` 절이 없고 문서 지도의 행이 옛 글(`회고에서 배운 것과 하네스의 문제점`)이다. run은 이미 있는 LESSONS의 절과 지도의 행을 고치지 않으므로, 다시 돌려도 그 두 판정 항목이 실패한다(006 검증 1의 실패 원인이 이것이다). 그래서 그 갈래가 절을 더하고 행을 지금 글로 바꿔 `[000] LESSONS를 지금의 양식으로 맞춘다`로 커밋한다. 시험 폴더의 시작 상태를 지금의 본문이 만든 것처럼 맞춘 것이다.
- run-all은 계획의 두 턴이 아니라 세 턴이 걸렸고, 그래서 `runcheck.py`를 TODO에 적힌 세 동작 밖에서도 고쳤다. 검증 2가 "문제 있음"이 된 것은 phase 4의 수행이 고친 방법(테스트가 `store.search("")`를 읽게 했다) 때문이고, 이 작업의 결정이 바꾼 동작이 아니다. run이 멈추고 고칠 안을 보인 것은 본문대로다. 판정 도구는 고칠 phase를 하나만 더하고 검증 절이 둘이라고 정해 두고 있어서, 계획 고침 커밋마다 보게 하고 검증 절 셋과 셋째 기록을 적었다. 고친 동작을 덜 보게 바꾼 항목은 없다.
- LESSONS로 옮긴 줄의 수를 보는 항목도 TODO에 적힌 세 동작 밖에서 고쳤다. 같은 뜻의 줄을 더하지 않는 규칙은 007에서 생겼고, 이 작업의 결정 (가)가 그 경우에도 `LESSONS로 옮겼다`를 적으라고 했다. 검증 절이 셋이 되면서 앞 절의 줄을 다시 적은 줄이 나와 꼭 같은 수를 바라는 항목이 실패했다. 빠진 줄은 읽어서 같은 뜻의 줄이 이미 있는 것을 확인했다(한 일).
- "테스트 먼저 기록" 항목은 TODO의 괄호에 없지만 이 작업의 결정(완료 조건 5의 (다))이 바꾼 동작이라 고쳤다.
- run-nogit은 `rerun.sh`에 갈래가 없어 `bin/run.sh`로 두 턴을 돌렸고, 판정 도구의 run-nogit 경우에 둘째 기록을 더했다. 둘째 턴은 TODO가 말한 "위치를 물으면 답하는 턴"이다.

## 남은 것
- 없음

## 하네스에서 걸린 것
- 계획의 읽을 것이 가리킨 (006-verify, 검증 1)의 줄들은 run-vrule이 다시 돌리지 않아서 실패했다고 적었지만, 바탕 폴더 vrule-base의 LESSONS 자체가 옛 양식이라 다시 돌리는 것만으로는 풀리지 않았다. 이것은 하네스에도 걸린다. 옛 run으로 만든 LESSONS가 있는 프로젝트는 run이 그 절(`## 미룬 문제`)과 문서 지도의 행을 지금 양식으로 고치지 않아 옛 꼴로 남는다.
- 완료 조건 9는 판정 도구의 기대를 이 작업의 결정이 바꾼 동작에 걸리는 것만 고치라고 하지만, run-all의 판정 도구 경우는 검증이 몇 번 도는지(검증 절의 수, 턴의 수)를 정해 두어서 그 실행의 검증이 무엇을 찾느냐에 따라 맞거나 틀린다. 이번에는 세 턴이 걸려 그 경우를 고쳐야 했다(계획과 달라진 점).
- run-all의 검증 2와 3이 시험 폴더의 하네스의 문제점으로 적은 것이 있다. 고칠 phase 양식의 통과 조건("문제마다 적힌 곳을 다시 읽거나 돌린다")과 테스트 먼저 기록 점검(실패 출력 뒤 통과 출력)은 테스트를 고치는 phase가 테스트를 약하게 만든 것을 가려내지 못한다. phase 4는 테스트 파일만 고치는 고칠 phase였고, run이 테스트 먼저를 "아니오"로 적었다. 이 줄들은 `~/plate-rail-test/run-all/docs/LESSONS.md`에 있다.
