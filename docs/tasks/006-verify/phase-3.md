# Phase 3: 브랜치와 합치기

**목표**: run이 기본 브랜치에서 시작하면 작업 브랜치에서 실행하고, 검증을 통과한 작업만 합칠지 묻는다.

**읽을 것**
- `plugins/plate/skills/run/SKILL.md` (시작 조건, 합친다)
- `~/plate-rail-test/plan-base/` (run-small, run-all의 시작 상태)
- `~/plate-rail-test/answers/run-wt-*.md`, `~/plate-rail-test/bin/runcheck.py`

**TODO**
- [x] run이 기본 브랜치에서 시작하면 `task/NNN-slug`를 만들어 바꾸고 실행한다. 기본 브랜치가 아니면 만들지 않는다 (`plugins/plate/skills/run/SKILL.md`)
- [x] 검증이 통과하면 run이 합칠 브랜치와 합칠 곳을 보여 주고 합칠지 묻는다. 전체 지시여도 묻는다. worktree가 없어도 "합친다" 절차로 합치고 브랜치를 지운다 (`plugins/plate/skills/run/SKILL.md`)
- [x] worktree의 합치기는 판정이 통과인 `verify.md`가 있을 때만 묻고, 없으면 worktree에서 run을 부르라고 안내한다 (`plugins/plate/skills/run/SKILL.md`)
- [x] `runcheck.py`의 `run-small`, `run-all`, `run-wt` 기대가 새 동작으로 바뀌고 `run-wt-gate`를 판정한다 (`~/plate-rail-test/bin/runcheck.py`)
- [x] 네 경우를 헤드리스로 돌려 통과한다

**통과 조건**
- 완료 조건 9, 10, 11이 참이다.
  - 확인: 완료 조건 9, 10, 11의 확인을 돌린다

## 한 일
- run이 기본 브랜치에서 시작하면 작업 브랜치에서 실행한다: 낱말에 "기본 브랜치"(`origin`의 HEAD, 없으면 `main`, 그다음 `master`)를 더하고, 주 작업 트리도 `task/NNN-slug`에 있을 수 있게 되어 "원래 자리"를 브랜치 이름이 아니라 최상위 폴더가 `.worktrees/` 아래인지로 가른다. 1번에 넷째 "작업 브랜치"를 더해, 커밋하지 않은 변경을 물은 뒤 기본 브랜치이면 `git switch -c task/NNN-slug`(이미 있으면 `git switch`)로 바꾼다 (`plugins/plate/skills/run/SKILL.md`)
- 검증이 통과하면 합칠지 묻는다: "통과하면"의 4번이 원래 자리에서 `task/NNN-slug`에 있으면 "합친다"로 가고, 판정이 이미 통과인 `verify.md`가 있을 때도 그 4번으로 간다. "합친다"는 두 곳("통과하면", 0번의 worktree)에서 오고 합칠 곳은 각각 기본 브랜치와 원래 자리의 브랜치다. 전체 지시여도 묻고, worktree가 없으면 합칠 곳으로 바꾼 뒤 합치고 브랜치를 지운다. 8번의 보고에 합친 것이나 합치지 않은 까닭을 더했다 (`plugins/plate/skills/run/SKILL.md`)
- worktree의 합치기는 판정이 통과인 `verify.md`가 있을 때만 묻는다: 0번에서 그것이 없으면 그 폴더에서 run을 부르라고 안내한다. 보고의 worktree 줄도 "검증이 통과했으면"으로 바꿨다 (`plugins/plate/skills/run/SKILL.md`)
- `runcheck.py`의 기대가 바뀌고 `run-wt-gate`를 판정한다: `run-small`(합침), `run-all`(합치지 않음), `run-wt`에 검증을 더하고, 브랜치는 원래 자리의 HEAD reflog로 본다(main에서 `task/…`로 가서 커밋 n개, main으로 돌아와 합침). 고칠 phase가 같은 실행의 검증 뒤에 더해지는 경우(run-all)를 받게 계획 고침 커밋의 자리, 제목의 K와 번호 M, 견줄 계획의 글, 검증 커밋의 순서를 넓혔다. 손으로 만든 표본으로 브랜치 판정의 통과와 실패를 먼저 봤고, 앞서 통과한 열넷 경우가 그대로 통과한다 (`~/plate-rail-test/bin/runcheck.py`)
- 네 경우를 헤드리스로 돌려 통과한다: 2.1.300. `run-small` 631초, `run-all` 1823초와 둘째 턴 565초, `run-wt` a 26초, b 480초, c1 160초, c2 19초, `run-wt-gate` 162초 (`~/plate-rail-test/logs/run-small.jsonl`, `run-all.jsonl`, `run-all-2.jsonl`, `run-wt-*.jsonl`, `run-wt-gate.jsonl`)

## 확인 결과
- 완료 조건 9, 10, 11이 참이다.
  - `runcheck.py run-small` → 모두 통과. HEAD가 main에서 `task/001-gitignore`로 가서 수행, 회고, 통과, 검증, 검증 통과를 커밋하고 main으로 돌아와 fast-forward로 합쳤고, 브랜치가 없다. 검증을 묻지 않았고 작업 폴더에 `plan.md`와 `verify.md`만 남았다. 통과
  - `runcheck.py run-all` → 모두 통과. 첫 턴에서 회고도 이을지도 검증도 묻지 않고 phase 1~3을 지나 검증까지 갔다. 검증 1이 "문제 있음"이어서 `phase-4.md`의 안을 보이고 멈췄고 그때 파일 변경이 없었다(`logs/run-all-stage-a.txt`). 승인한 둘째 턴에서 phase 4, 검증 2(통과), 검증 통과를 커밋한 뒤 합칠지 묻고 멈췄다. main은 실행 전 그대로이고 HEAD는 `task/001-core-commands`다. 통과
  - `logs/run-all.jsonl`의 검증 에이전트 → 계획 커밋(59e704e)과 phase 1~3의 수행·회고·통과 커밋을 모두 `git show`로 읽고 완료 조건의 테스트 넷을 돌렸다. `logs/run-all-2.jsonl`의 마지막 답글은 합칠 브랜치와 합칠 곳(main)을 보이고 묻는다. 통과
  - `runcheck.py run-wt` → 모두 통과(단계 a, b도). worktree에서 phase 1과 검증까지 끝나고 원래 자리에서 부르라고 안내했다. 원래 자리에서 부르자 합칠 브랜치와 합칠 곳을 보이고 물었고, 승인 뒤 합쳐지고 worktree와 브랜치가 없다. 통과
  - `runcheck.py run-wt-gate` → 모두 통과. worktree의 `verify.md`를 지운 커밋을 넣고 원래 자리에서 부르자, 합치지 않고 에이전트도 띄우지 않고 그 worktree 폴더에서 run을 부르라고 안내했다. 통과

## 계획과 달라진 점
- phase 2의 `run-verify`, `run-vfix`, `run-vrule`도 다시 돌렸다. 세 바탕이 main에 있어 작업 브랜치를 만드는 새 동작에 걸린다. 세 기대에 "작업 브랜치에서 커밋하고 합치지 않는다"를 더했고 모두 통과했다(337초, 44·119·336초, 260초). 마지막 답글은 모두 합칠지 묻는다.
- `run-all`이 두 턴이 됐다. 검증 1이 `tests/test_note.py`가 `store.py` 밖에서 SQL을 돌리는 것을 ARCHITECTURE의 규칙과 어긋난다고 짚었다. run-vfix처럼 "승인한다."를 둘째 턴으로 줬고(`answers/run-all-2.md`), `rerun.sh`는 검증 1이 "문제 있음"일 때만 둘째 턴을 잇는다.
- `run-small`, `run-all`, `run-wt`의 바탕에 지금 setup의 문서 지도 문장을 더했다. 바탕이 005 phase 7 전의 setup으로 셋업돼, 처음 돌린 run-small이 `docs/LESSONS.md`를 만들기 전에 위치를 묻고 멈췄다. `vfmake.sh`가 문장을 더해 `셋업을 다시 돌린 직후`로 커밋한다. run-wt의 시작 상태는 run-wt에서 9282be4로 되살려 `wt-base`로 두었다.
- `run.sh`의 허용 목록에 `git switch`, `git checkout`, `git symbolic-ref`를 더했다. 처음 띄운 실행이 목록에 없는 명령에서 기다려, 멈추고 다시 띄웠다.

## 남은 것
없음

## 하네스에서 걸린 것
- 005 phase 7 전에 셋업된 프로젝트(문서 지도에 "하네스의 스킬이 위치를 정해 둔 기록은 묻지 않고 …"가 없다)에서 run이 `docs/LESSONS.md`를 처음 만들 때 갈린다. 처음 돌린 run-small은 프로젝트의 규칙을 따른다며 위치를 묻고 멈췄고, run-vfix는 묻지 않고 만든 뒤 "프로젝트 규칙을 어겼다"고 보고했다. setup을 다시 돌리면 없어지지만 run은 그것을 안내하지 않는다.
- 검증의 문제 글에 고치는 방법이 둘(테스트를 고친다 / ARCHITECTURE에 적는다) 들어 있으면, run이 TODO에 그 글을 그대로 옮긴 뒤 양식에 없는 선택지와 추천안을 더해 물었다(run-all 첫 턴).
