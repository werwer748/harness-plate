# Phase 7: 이 레포에서 004를 실행한다 (자기 적용)

**목표**: `004-context-rules`가 run 스킬로 실행돼 두 phase가 통과하고 context 스킬에 규칙 둘이 들어 있다.

**읽을 것**
- `docs/tasks/004-context-rules/plan.md` (004의 완료 조건)
- `~/.claude/projects/-Users-gangjungi-Desktop-harness-plate/` (사용자가 연 세션의 기록 `<세션>.jsonl`)
- `~/plate-rail-test/bin/calls.py`, `~/plate-rail-test/bin/runcheck.py` (기록과 커밋을 보는 도구)

**TODO**
- [x] 사용자가 새 세션에 붙여 넣을 글이 답글의 맨 끝에 코드 블록 하나로 주어진다. 004의 번호를 주어 부르는 글이다(005에도 `phase-N.md`가 남아 있어 번호 없이 부르면 run이 둘 가운데 묻는다)
- [x] 사용자가 `claude --plugin-dir plugins/plate`로 연 새 세션에서 run을 직접 불러 004의 두 phase가 통과한다. 이 phase를 수행하는 세션은 run을 부르지 않는다
- [x] 그 세션의 기록과 커밋을 읽은 결과가 사용자에게 보여진다: 커밋의 순서와 메시지, 메인이 직접 고친 파일, 에이전트에게 넘긴 글, 옮길 것이 있었으면 `docs/LESSONS.md`와 지도의 행
- [x] 기대와 다른 것이 있었으면 스킬이 고쳐지고 걸리는 판정이 다시 통과한다. 본문의 규칙을 바꿔야 하면 고치기 전에 사용자에게 묻는다 (`plugins/plate/skills/`)

**통과 조건**
- 완료 조건 16이 참이다.
  - 확인: 완료 조건 16의 확인 넷을 돌리고 읽어 기대와 같은지 본다

## 한 일
- 붙여 넣을 글: 앞 세션들이 `/plate:run 004`를 부르는 글을 줬고, 사용자가 그 글로 새 세션에서 run을 불렀다.
- 004의 두 phase 통과: 세션 `78d5961f`, `400a1081`, `f35fbf4a`(phase 1, `d169a15`~`33233d0`)와 `0cff8f08`(phase 2, `292b184`~`5ed9314`). 앞의 셋에서 수행 넷이 `plugins/plate/` 편집의 권한에 막혔다.
- 기록과 커밋을 읽은 결과를 사용자에게 보였다: 커밋 여섯의 순서와 든 파일, 에이전트에게 넘긴 글(수행 6번, 회고 2번 모두 본문의 글 그대로), 메인이 직접 고친 파일(레포 안은 `docs/LESSONS.md`와 `AGENTS.md`의 지도 행, 레포 밖은 도구의 메모 파일 6번), `docs/LESSONS.md`와 지도의 행(`33233d0`).
- 기대와 다른 것 둘을 사용자에게 묻고 고쳤다. run 1번 3이 대상 phase의 `phase-N.md`를 세지 않는다(`plugins/plate/skills/run/SKILL.md`). setup의 지도 문구에 하네스가 위치를 정한 기록은 묻지 않는다는 예외를 더했다(`plugins/plate/skills/setup/SKILL.md`, `AGENTS.md`, 머리의 범위 밖과 결정).

## 확인 결과
- 완료 조건 16이 참이다.
  - `ls docs/tasks/004-context-rules/` → `plan.md`. 통과
  - `git log --format=%s` → 004의 phase 1, phase 1 회고, phase 1 통과, phase 2, phase 2 회고, phase 2 통과가 순서대로 있다. 통과
  - 004의 완료 조건의 확인 → 기계로 보는 확인 14개가 모두 기대대로다. 본문 74~76번 줄, 절대 규칙 5, 2번 절, `logs/ctx-cells-1.jsonl`의 마지막 답글(빠진 갈래 하나만 묻는다)을 읽었다. 통과
  - 세션 기록 → 메인이 레포 안에서 직접 고친 파일은 `docs/LESSONS.md`와 `AGENTS.md`의 지도 행뿐이고, 에이전트에게 넘긴 글은 본문의 글 그대로다. 통과
- 고친 본문에 걸리는 판정(TODO 넷째)
  - `runcheck.py run-dirty` → 모두 통과. 첫 턴이 ` M NOTES.md`를 보이고 진행할지 물었다. 통과
  - `runcheck.py run-reblock --as run-skip --logs run-reblock` → 모두 통과. 물음 0개, 손으로 넣은 막힘 줄이 수행 커밋의 `phase-1.md`와 `docs/LESSONS.md`에 남았다. 통과
  - `setupcheck.py setup-fresh PRD,ARCHITECTURE,ADR` → 모두 통과. 통과
  - `git -C setup-remap diff` → `AGENTS.md` 4행 한 줄이 새 문구로 바뀌고 `docs/LESSONS.md` 행이 남았다. 통과

## 계획과 달라진 점
- TODO 첫째와 둘째는 이 phase를 수행하기 전에 앞 세션들과 사용자가 했다. 이 세션은 결과를 읽어 확인했다.
- 머리의 범위 밖이 setup을 고치는 것을 뺐는데 TODO 넷째에서 setup을 고쳤다. 사용자의 승인을 받아 범위 밖 줄을 고치고 결정에 한 줄을 더했다.
- 판정 `run-reblock`(막힌 기록만 남은 채 다시 부름)은 완료 조건에 없는 새 경우다. `run-small`의 계획 커밋에서 떠서 지도 문구를 새 것으로 맞춘 뒤 돌렸다.

## 남은 것
없음

## 하네스에서 걸린 것
- `run-lessons` 판정은 같은 지도 문구에서 위치를 묻지 않았고 자기 적용은 물었다. 같은 본문과 문구인데 실행마다 갈렸고, 판정 한 번으로는 이 갈림을 잡지 못했다.
