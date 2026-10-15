# Phase 2: run이 검증으로 잇는다

**목표**: run이 검증이 남은 작업을 알아보고 검증 에이전트에게 맡기며, 결과에 따라 LESSONS로 옮기거나 고칠 phase의 안을 승인받는다.

**읽을 것**
- `plugins/plate/skills/run/SKILL.md` (상태 표, 계획을 고친다, LESSONS 절)
- `plugins/plate/skills/verify/SKILL.md` (phase 1의 결과. 돌려주는 줄)
- `~/plate-rail-test/vf-fail/`, `~/plate-rail-test/run-rule/`, `~/plate-rail-test/run-nogit/` (시작 상태)
- `~/plate-rail-test/bin/runcheck.py`, `~/plate-rail-test/bin/run.sh`, `~/plate-rail-test/bin/rerun.sh`

**TODO**
- [x] run이 "검증이 남은 작업"을 알아보고(0번의 대상 찾기, 2번의 상태 표), 남은 phase가 없으면 묻지 않고 새 에이전트에게 검증을 맡긴다. 그 에이전트는 수행·점검한 에이전트와 다르다 (`plugins/plate/skills/run/SKILL.md`)
- [x] 검증이 통과하면 run이 `verify.md`의 배운 것과 하네스의 문제점을 `docs/LESSONS.md`로 옮기고, git 레포가 아니면 `done-phase-N.md`를 지운다 (`plugins/plate/skills/run/SKILL.md`)
- [x] 검증이 "문제 있음"이면 run이 문제 목록을 TODO로 담은 새 `phase-M.md`의 안을 보여 주고 멈추며, 승인 뒤 계획 파일만 커밋하고 그 phase를 수행에 맡긴다. 전체 지시여도 멈춘다 (`plugins/plate/skills/run/SKILL.md`)
- [x] `runcheck.py`가 `run-verify`, `run-vfix`, `run-vrule`을 판정하고, `run-nogit`의 기대가 새 동작으로 바뀐다 (`~/plate-rail-test/bin/runcheck.py`)
- [x] 네 경우를 헤드리스로 돌려 통과한다

**통과 조건**
- 완료 조건 5, 6, 7, 8이 참이다.
  - 확인: 완료 조건 5, 6, 7, 8의 확인을 돌린다

## 한 일
- run이 "검증이 남은 작업"을 알아보고 검증을 맡긴다: 낱말에 "검증이 남은 작업"(verify와 같은 정의)과 "검증 에이전트"를 더하고, 0번은 끝나지 않은 작업과 검증이 남은 작업을 함께 찾고, 2번과 7번은 남은 phase가 없으면 새 절 "검증을 맡긴다"로 간다. 그 절은 `verify.md`의 마지막 판정이 통과면 8번, "문제 있음"이고 그 뒤에 통과한 phase가 없으면 고칠 phase로 가고(다시 검증하지 않는다), 그 밖이면 두 줄의 글을 새 에이전트에게 넘긴다. 절대 규칙 1, 2, 4와 첫머리, description도 맞췄다 (`plugins/plate/skills/run/SKILL.md`)
- 검증이 통과하면 LESSONS로 옮기고 `done-phase-N.md`를 지운다: "통과하면"에서 검증 절마다의 배운 것과 하네스의 문제점을 `- (작업, 검증 K) …` 꼴로 옮기고, git 레포가 아니면 `done-phase-N.md`를 지우고, 고친 파일만 `NNN-slug: 검증 통과`로 커밋한다. 검증 에이전트는 `verify.md`만 커밋하므로 옮긴 것은 그 뒤의 커밋 하나다 (`plugins/plate/skills/run/SKILL.md`)
- 검증이 "문제 있음"이면 고칠 phase의 안을 보여 주고 멈춘다: "고칠 phase를 더한다"에 번호(쓴 phase 번호의 다음), 양식(`# Phase M: 검증 K의 문제를 고친다`, TODO는 문제 하나에 항목 하나, 통과 조건은 머리의 완료 조건 모두)을 두고, 승인 뒤 그 파일만 `plan: NNN-slug 수정`으로 커밋하고 2번으로 간다. `plan.md`는 고치지 않는다 (`plugins/plate/skills/run/SKILL.md`)
- `runcheck.py`가 세 경우를 판정하고 `run-nogit`의 기대를 바꾼다: 커밋 가르기에 V(검증)와 L(검증 통과), 프로젝트 꼴 메시지의 X를 더하고, 검증 에이전트의 글, 실행이 더한 phase, 검증 커밋의 순서와 든 파일, 검증 절이 LESSONS로 옮겨졌는지, 메인이 완료 조건의 확인 명령을 돌리지 않았는지, `run-vfix`의 단계 a·b를 본다. `run-nogit`은 작업 폴더에 `plan.md`와 `verify.md`만 남고 띄운 순서가 수행, 확인, 검증인지 본다. 손으로 쓴 표본으로 통과와 실패를 가르는 것을 먼저 봤고, 앞서 통과한 열 경우(vf 셋, run-small 등)가 그대로 통과한다 (`~/plate-rail-test/bin/runcheck.py`)
- 네 경우를 헤드리스로 돌려 통과한다: 2.1.300에서 넷을 한꺼번에 돌렸다. `run-verify` 143초, `run-vrule` 246초, `run-nogit` 398초, `run-vfix` 세 턴 44초, 206초, 568초 (`~/plate-rail-test/logs/run-verify.jsonl`, `run-vrule.jsonl`, `run-nogit.jsonl`, `run-vfix-*.jsonl`)

## 확인 결과
- 완료 조건 5, 6, 7, 8이 참이다.
  - `runcheck.py run-verify` → 모두 통과. 검증 에이전트 하나만 띄웠고 `001-gitignore: 검증`(verify.md만)과 `001-gitignore: 검증 통과`(LESSONS, AGENTS.md)가 생겼다. 메인은 확인 명령을 돌리지 않았다. 통과
  - `runcheck.py run-vfix` → 모두 통과. 커밋이 `plan: 001-gitignore 수정`(phase-2.md만), phase 2, 회고, 통과, 검증, 검증 통과의 차례이고 `## 검증 2`의 판정이 통과다. 통과
  - `logs/run-vfix-1.jsonl`의 마지막 답글 → 검증 1의 문제 셋을 TODO로 담은 `phase-2.md`의 안을 보여 주고 승인을 물으며 멈췄다. 그때 커밋과 파일 변경, 띄운 에이전트가 없다(`logs/run-vfix-stage-a.txt`). 통과
  - `runcheck.py run-vrule` → 모두 통과. 커밋이 `[001] 검증`, `[001] 검증 통과`이고, verify.md의 "프로젝트의 규칙을 따름: …" 줄이 LESSONS의 하네스의 문제점에 `(001-gitignore, 검증 1)`로 옮겨졌다. 통과
  - `runcheck.py run-nogit` → 모두 통과. 작업 폴더에 `plan.md`와 `verify.md`만 남고 `.git`이 없다. 통과

## 계획과 달라진 점
- TODO에 없던 `vfmake.sh`와 `rerun.sh`를 고치고 바탕 폴더 둘을 만들었다. `vfix-base`는 vf-fail의 검증 뒤 상태(4e839c4), `vrule-base`는 run-rule의 끝 상태(4aa1686)를 복제했다. 까닭: `vfmake.sh vf-fail`이 vf-fail을 다시 만들면 run-vfix의 시작 상태(검증 1이 있는 상태)가 사라지고, run-vfix는 run-wrong처럼 턴 사이에 단계를 본다.
- 검증이 통과한 뒤 LESSONS로 옮긴 것은 따로 `NNN-slug: 검증 통과` 커밋이 된다. 옮길 것이 있으면 phase 3의 run-small도 검증 커밋 뒤에 이 커밋이 하나 더 붙는다.

## 남은 것
없음

## 하네스에서 걸린 것
- verify 낱말의 "작업의 커밋"은 메시지가 작업 폴더의 이름으로 시작하는 커밋을 넣는데, 프로젝트의 커밋 꼴(`[001] …`)을 따른 커밋은 그 말로 찾아지지 않는다. run-vrule에서는 모두 작업 폴더를 바꾼 커밋이라 다른 기준으로 잡혔다(verify가 스스로 적었다). retro 1번과 같은 결이다.
- run-nogit의 검증이 `AGENTS.md`를 읽지 않고 "LESSONS가 문서 지도에 없다"는 하네스의 문제점을 적었다. run은 검증을 맡기기 전(phase 1 통과 때)에 이미 행을 더했다. 세션이 시작될 때 실린, 행을 더하기 전의 지침으로 판단한 것으로 보인다. run이 이 틀린 줄을 그대로 LESSONS로 옮겼다.
- run-vfix의 검증 2가 "검증 절의 배운 것과 하네스의 문제점을 옮기는 단계가 하네스에 없다"고 적었는데, run은 검증이 통과한 뒤에 옮긴다(69c877b). 검증 에이전트는 프로젝트 밖의 스킬 본문을 읽지 못해 검증 뒤의 단계를 모른다. 이 줄도 LESSONS로 옮겨졌다.
- run 본문 "고칠 phase를 더한다"가 TODO를 검증의 문제 하나에 항목 하나로 옮기게 해서, 원인 하나(`*.db` 줄)에서 나온 문제 셋이 TODO 셋이 됐다(run-vfix의 수행 에이전트가 적었다).
- run 본문 LESSONS 절이 검증 절마다 배운 것을 옮기게 해서, 검증 1과 검증 2가 같은 사실(`booklog/`와 `tests/`가 아직 없다)을 적은 run-vfix의 LESSONS에 같은 사실이 두 줄 들어갔다.
