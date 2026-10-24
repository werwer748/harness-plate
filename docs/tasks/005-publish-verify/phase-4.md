# Phase 4: 원격 없는 합치기와 푸시 훅

**목표**: GitHub 원격이 없는 시험 폴더에서 run이 tasks 끝에 합칠지 묻고 합치며, 셋업된 시험 폴더에서 에이전트가 기본 브랜치로 하는 푸시를 푸시 훅이 막는다.

**테스트 먼저**: 아니오 — 시험 폴더에서 스킬과 훅을 돌려 보고, 이 저장소에서는 `docs/TOOLS.md`만 고친다

**읽을 것**
- `docs/TOOLS.md`의 Claude Code 절 (헤드리스 실행과 세션 잇기, "훅"의 막힌 호출이 기록에 남는 꼴, "tasks 실행의 판정에서 본 것"의 시험 폴더와 실행 스크립트)
- `plugins/plate/skills/run/SKILL.md` (tasks 끝, 합친다, `<tasks 이름>: 비움` 커밋)
- `plugins/plate/hooks/hooks.json`과 거기에 걸린 푸시 훅 (막는 경우와 막지 않는 경우)

**TODO**
- [x] 원격 없는 run 장면: 원격이 없고 기본 브랜치가 `main`인 시험 폴더에서 셋업하고 작은 tasks를 계획해 run을 끝까지 돌리면, tasks 끝에 PR 대신 합칠지 묻는다. 승인하면 `main`에 그 tasks의 `<이름>: 비움` 커밋이 들어온다. 실행 기록은 run 본문을 마지막으로 고친 뒤에 만든다
- [x] 푸시 훅 장면: origin이 있는 셋업된 시험 폴더에서 에이전트에게 기본 브랜치로 `git push`를 시키면 푸시 훅이 막는다. 실행 기록에 그 호출의 결과가 `is_error` `true`와 푸시 훅의 stderr로 남는다. 실행 기록은 푸시 훅 스크립트를 마지막으로 고친 뒤에 만든다
- [x] 이 phase의 기록에 장면마다 시험 폴더와 실행 기록의 경로가 적힌다 (`docs/tasks/005-publish-verify/phase-4.md`)
- [x] 이 phase에서 확인한 도구의 사실(Bash 호출을 막은 훅이 기록에 남는 꼴)이 시험 폴더와 실행 기록의 위치와 함께 적힌다 (`docs/TOOLS.md`)

**통과 조건**
- 완료 조건 5가 참이다.
  - 확인: 완료 조건 5의 확인을 모두 돌린다. `done-phase-4.md`는 이름이 바뀌기 전인 이 파일로 읽는다
- 이 phase에서 확인한 도구의 사실이 `docs/TOOLS.md`에 적혀 있다.
  - 확인: `docs/TOOLS.md`의 Claude Code 절을 읽어 이 phase의 장면에서 본 것이 시험 폴더와 실행 기록의 위치와 함께 있다

## 한 일
- 원격 없는 run 장면: 새로 쓴 `~/plate-rail-test/bin/localmake.sh ci-local`이 `ci-src`의 `ae98f75`(textkit. plate 복사본과 워크플로가 들어가기 전) 파일로 원격이 없고 기본 브랜치가 `main`인 시험 폴더 `~/plate-rail-test/ci-local`을 만들었다(`c344f55`). `tturn.sh ci-local setup ci-local-setup`으로 setup을 돌렸고(258초, "GitHub 원격이 없어서 묻지 않았고 쓰지 않았습니다"), 새로 쓴 `~/plate-rail-test/bin/cilocal-plan.sh`가 setup의 변경을 `셋업`(`dd3c554`)으로, phase 2와 같은 tasks `line-count`(task `001-line-count`, phase 하나, 테스트 먼저)의 계획 파일을 `plan: line-count`(`3670ef6`)로 `main`에 커밋했다. `RUN_ALLOW='Bash(git remote:*)'`로 run을 세 턴 돌렸다: "tasks 일괄로 한다."(1184초, 에이전트 5, 고칠지 물음에서 멈춤), "아무것도 고치지 않고 이슈도 올리지 않는다."(123초, `line-count: BACKLOG`, `line-count: RUNLOG`, `line-count: 비움`(`c3f87c1`) 커밋 뒤 "Should I merge `tasks/line-count` into `main`?"에서 멈춤), "승인한다."(36초, `git switch main && git merge tasks/line-count && git branch -d tasks/line-count`, fast-forward). 둘째 턴의 물음은 "This repo has no origin remote, so there's no PR step; the next step is merging into `main`."로 PR 단계가 없다고 적었다. 시험 폴더는 `~/plate-rail-test/ci-local`, 실행 기록은 `~/plate-rail-test/logs/ci-local-setup.jsonl`, `~/plate-rail-test/logs/ci-local-1.jsonl`, `~/plate-rail-test/logs/ci-local-2.jsonl`(합칠지 물은 턴), `~/plate-rail-test/logs/ci-local-3.jsonl`(합친 턴)이다
- 푸시 훅 장면: `localmake.sh ci-push`가 같은 파일로 만든 `ci-push-src`를 bare로 복제한 `~/plate-rail-test/ci-push-origin.git`을 다시 복제해 origin이 있는 `~/plate-rail-test/ci-push`를 만들었다(origin/HEAD `origin/main`). 훅이 막지 못해도 GitHub의 시험 저장소가 바뀌지 않게 origin을 로컬 bare 저장소로 했다. `tturn.sh ci-push setup ci-push-setup`으로 setup을 돌리고(273초, origin이 GitHub이 아니어서 CI를 묻지 않았다) 그 변경을 `main`에 `셋업`(`64f5581`)으로 커밋해 origin보다 하나 앞서게 했다. 새로 쓴 `~/plate-rail-test/bin/pushprobe.sh ci-push ci-push`가 스킬 없이 `--allowedTools "Bash(git push:*)"`로 에이전트에게 `git push origin main` 한 번을 시켰다(10초). 그 호출의 `tool_result`는 `is_error` `true`이고 내용이 `PreToolUse:Bash hook error: [f="/Users/gangjungi/Desktop/harness-plate/plugins/plate/hooks/push_guard.py"; [ -f "$f" ] || exit 0; exec python3 "$f"]: plate: 기본 브랜치(`main`)로 푸시하지 않는다: `git push origin main``과 푸시 훅의 둘째 줄, `This hook comes from the plate@inline plugin.`이다. origin의 `main`은 앞뒤 모두 `f0fa749`다. 시험 폴더는 `~/plate-rail-test/ci-push`, 실행 기록은 `~/plate-rail-test/logs/ci-push-setup.jsonl`, `~/plate-rail-test/logs/ci-push.jsonl`(푸시를 시킨 실행)이다
- 이 phase의 기록에 장면마다 시험 폴더와 실행 기록의 경로를 적었다(위의 두 항목) (`docs/tasks/005-publish-verify/phase-4.md`)
- `docs/TOOLS.md`: Claude Code 절의 "CI의 세 판정과 CI 있는 PR에서 본 것" 뒤에 "원격 없는 합치기와 푸시 훅에서 본 것"을 더했다. 스크립트, 시험 폴더, 기록의 위치와 함께 setup이 GitHub이 아닌 원격에서 CI를 묻지 않은 것, 원격 없는 run이 합칠지 묻고 fast-forward로 합친 것, Bash 호출을 막은 훅이 기록에 남는 꼴(`tool_result`, `tool_result_meta`의 `non_execution_kind`와 `permission_decision`, `result`의 `permission_denials`), 훅이 허용 목록보다 앞서는 것, 실행 시간을 적었다 (`docs/TOOLS.md`)

## 확인 결과
- 완료 조건 5가 참이다.
  - 원격 없는 장면의 실행 기록 `~/plate-rail-test/logs/ci-local-2.jsonl`에 "Should I merge `tasks/line-count` into `main`?"가 있다(`grep -c` → 2. 답글 줄과 `result` 줄). `test ~/plate-rail-test/logs/ci-local-2.jsonl -nt plugins/plate/skills/run/SKILL.md` → 참(`ci-local-1.jsonl`, `ci-local-3.jsonl`도 참. run 본문은 18:24:36, 기록은 21:21:01~21:24:16). `git -C ~/plate-rail-test/ci-local log --format=%s main` → 첫 줄이 `line-count: 비움`이다(`main`은 `c3f87c1`, `tasks/line-count`는 지워졌고 원격은 없다). 통과
  - 푸시 훅 장면의 실행 기록 `~/plate-rail-test/logs/ci-push.jsonl`에서 `git push origin main` 호출의 `tool_result`가 `"is_error": true`이고 내용에 푸시 훅의 stderr(`plate: 기본 브랜치(`main`)로 푸시하지 않는다: `git push origin main``과 그 다음 줄)가 있다. `tool_result_meta`의 `permission_decision`은 `{"decision": "reject", "source": "hook", "reason_type": "hook"}`다. `test ~/plate-rail-test/logs/ci-push.jsonl -nt plugins/plate/hooks/push_guard.py` → 참(`edit_guard.py`, `hooks.json`에도 참. 푸시 훅은 17:15:54, 기록은 21:01:28). 통과
- 이 phase에서 확인한 도구의 사실이 `docs/TOOLS.md`에 적혀 있다.
  - `docs/TOOLS.md`의 Claude Code 절을 읽음 → "원격 없는 합치기와 푸시 훅에서 본 것"에 이 phase의 두 장면에서 본 것이 스크립트(`bin/localmake.sh`, `bin/cilocal-plan.sh`, `bin/tturn.sh`, `bin/pushprobe.sh`), 시험 폴더(`ci-local`, `ci-push`, `ci-push-origin.git`), 기록(`logs/ci-local-setup.jsonl`, `logs/ci-local-1.jsonl`~`logs/ci-local-3.jsonl`, `logs/ci-push-setup.jsonl`, `logs/ci-push.jsonl`)의 위치와 함께 있다. 통과

## 계획과 달라진 점
- 원격 없는 run 장면의 "작은 tasks를 계획해"는 plan 스킬을 부르지 않고 `cilocal-plan.sh`가 계획 파일을 손으로 써서 했다. phase 2(`cinorun-plan.sh`)와 phase 3(`cirun-plan.sh`)의 run 장면과 같은 방식이고, tasks도 phase 2와 같은 `line-count`다
- 푸시 훅 장면의 origin은 GitHub의 시험 저장소가 아니라 로컬 bare 저장소(`ci-push-origin.git`)로 했다. 훅이 막지 못하면 그 푸시가 origin의 `main`을 바꾸므로, 시험 저장소의 `main`이 바뀌지 않게 했다. 푸시 훅은 원격의 이름(`origin`)과 기본 브랜치만 보고 URL은 보지 않는다

## 남은 것
- 없음

## 하네스에서 걸린 것
- 원격 없는 run의 둘째 턴(합칠지 물은 턴)의 답글이 영어였다. 첫 턴과 셋째 턴의 답글, 프로젝트의 문서는 한국어다. 물음의 뜻은 분명해 판정에는 걸리지 않았다
- 원격 없는 run의 마지막 보고는 `review.md`의 소스 문제에 든 U+2028 문자를 BACKLOG에 ` `로 적었다고 했지만, `docs/BACKLOG.md`에는 그 문자가 그대로 들어 있다(`ci-local`의 `efbc90d`). 보고가 한 일과 다르다

## 확인 1

**통과 조건**
- 완료 조건 5가 참이다.
  - 이 파일(`phase-4.md`)의 "한 일"에 원격 없는 장면의 시험 폴더 `~/plate-rail-test/ci-local`과 실행 기록 `~/plate-rail-test/logs/ci-local-2.jsonl`(합칠지 물은 턴)이 적혀 있음. 그 기록에서 "Should I merge `tasks/line-count` into `main`?"를 `grep -c`로 셈 → 2. `result` 줄이 "This repo has no origin remote, so there's no PR step; the next step is merging into `main`." 뒤에 그 물음으로 끝난다. 통과
  - `test ~/plate-rail-test/logs/ci-local-2.jsonl -nt plugins/plate/skills/run/SKILL.md` → 참(`ci-local-setup`, `ci-local-1`, `ci-local-3`도 참. run 본문 2026-10-24 18:24:36, 기록 21:00:41~21:24:16). 통과
  - `git -C ~/plate-rail-test/ci-local log --format=%s main` → 첫 줄이 `line-count: 비움`(`c3f87c1`). `git remote`는 아무것도 내지 않고 브랜치는 `main` 하나다. 통과
  - 이 파일의 "한 일"에 푸시 훅 장면의 시험 폴더 `~/plate-rail-test/ci-push`와 실행 기록 `~/plate-rail-test/logs/ci-push.jsonl`이 적혀 있음. 그 기록의 `git push origin main` 호출의 `tool_result`가 `is_error` `true`이고 내용이 `PreToolUse:Bash hook error: [f="…/plugins/plate/hooks/push_guard.py"; …]: ` 뒤에 `push_guard.py`의 `BLOCK` 글(`plate: 기본 브랜치(`main`)로 푸시하지 않는다: `git push origin main``과 둘째 줄) 그대로다. `tool_result_meta`의 `permission_decision`은 `{"decision": "reject", "source": "hook", "reason_type": "hook"}`. origin(`ci-push-origin.git`)의 `main`은 `f0fa749`로 로컬 `main`(`64f5581 셋업`)보다 하나 뒤다. 통과
  - `test ~/plate-rail-test/logs/ci-push.jsonl -nt plugins/plate/hooks/push_guard.py` → 참(`hooks.json`에도 참. 푸시 훅 17:15:54, 기록 21:01:28). 통과
- 이 phase에서 확인한 도구의 사실이 `docs/TOOLS.md`에 적혀 있다.
  - `docs/TOOLS.md`의 Claude Code 절(15~139줄)을 읽음 → 122~129줄 "원격 없는 합치기와 푸시 훅에서 본 것"에 원격 없는 run이 합칠지 묻고 fast-forward로 합친 것, Bash 호출을 막은 훅이 기록에 남는 꼴(`tool_result`, `tool_result_meta`, `permission_denials`), 훅이 허용 목록보다 앞서는 것이 시험 폴더(`ci-local`, `ci-push`, `ci-push-origin.git`), 스크립트(`bin/localmake.sh`, `bin/cilocal-plan.sh`, `bin/tturn.sh`, `bin/pushprobe.sh`. 넷 다 있다), 기록(`logs/ci-local-setup.jsonl`, `logs/ci-local-1.jsonl`~`logs/ci-local-3.jsonl`, `logs/ci-push-setup.jsonl`, `logs/ci-push.jsonl`)의 위치와 함께 있다. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 89 tests`, `OK`. 통과

**실패**
- 없음

**하네스에서 걸린 것**
- 없음

**판정**: 통과
