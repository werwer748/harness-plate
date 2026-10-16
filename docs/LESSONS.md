# 회고에서 배운 것

## 프로젝트에서 배운 것
- (004-context-rules, phase 2) 완료 조건 4의 확인은 `~/plate-rail-test/ctx-cells`의 커밋하지 않은 변경과 `~/plate-rail-test/logs/ctx-cells-*.jsonl`을 본다. 작업 전체를 검증하기 전에 그 폴더를 되돌리거나 같은 로그 이름으로 다시 돌리면 결과가 바뀐다(`run.sh`는 `logs/<로그 이름>.jsonl`을 덮어쓴다).
- (004-context-rules, 검증 1) `~/plate-rail-test/ctx-cells`의 결과와 `~/plate-rail-test/logs/ctx-cells-*.jsonl`은 커밋 `d169a15`의 context 본문으로 돌린 것이다. 그 뒤 커밋 `e2b6444`가 같은 본문의 59행(초안을 보이는 규칙)과 76행(여럿을 묻는 칸이 문장 중간에 있을 때의 꼴)을 바꿨고, 바뀐 본문으로는 이 시험을 다시 돌리지 않았다.
- (004-context-rules, 검증 1) `docs/ADR.md`의 ADR-018 이유 끝 "멈춘 이유는 없음"은 이 작업이 더한 문장 중간 칸의 규칙에 맞지 않는 꼴로 남아 있다(계획의 범위 밖). 범위 밖에 함께 적힌 2단계 완성 판정 항목은 커밋 `9b0dfb6`에서 항목째 지워졌다.
- (006-verify, 검증 1) `~/plate-rail-test`에서 완료 조건 1~3, 5, 7~11의 시험 폴더는 run-vfix를 빼고 모두 `de62793`(run과 verify에 미루는 길) 전의 본문으로 만든 상태다. 지금의 판정 도구로 대조해 통과한 경우(vf 셋, run-verify, run-wt, run-wt-gate)도 바뀐 본문으로 돌린 결과는 아니다. 다시 돌리려면 `bin/vfmake.sh`로 폴더를 다시 만들고 `bin/rerun.sh`로 돌린다. run-nogit은 `rerun.sh`에 갈래가 없어 `bin/run.sh`에 `answers/run-nogit.md`를 주어 돌린다.

## 하네스의 문제점
- (007-harness-issues, phase 2) `~/plate-rail-test`는 git 레포가 아니라서 이 phase에서 고친 `bin/vfmake.sh`와 새로 생긴 `run-oldsetup`, `logs/run-oldsetup.*`는 커밋에 넣지 못했다. 커밋에는 `plugins/plate/skills/run/SKILL.md`와 `phase-2.md`만 든다.
- (007-harness-issues, phase 2) `run-oldsetup`의 바탕인 `vrule-base`는 LESSONS를 이 작업(001)의 `[001] phase 1 통과`(`4aa1686`)에서 만든 상태라, 그것을 지운 `a4d2a8d`를 검증이 "작업 밖의 커밋이 작업의 변경을 되돌렸다"는 하네스의 문제점으로 적었다(`run-oldsetup/docs/tasks/001-gitignore/verify.md`). 시험 폴더를 만든 방식에서 나온 줄이고, 사용자가 위치에 답하면 run이 이 줄도 LESSONS로 옮긴다.
- (007-harness-issues, phase 2) 같은 검증이 "작업의 커밋"의 메시지 기준이 `[001] …` 아래에서 하나도 맞지 않는다는 줄을 다시 적었다. phase 1이 고친 정의(작업 폴더의 파일을 바꾼 커밋도 든다)로 빠진 커밋은 없었다고 함께 적었다.

## 미룬 문제
- (004-context-rules, 검증 1) 절대 규칙 5의 "저장소 밖의 파일을 열지 않는다"에는 다른 스킬을 이름으로 부를 때 도구가 여는 스킬 파일의 예외가 없다. `docs/TOOLS.md`의 Codex 절에는 Codex가 플러그인을 `~/.codex/plugins/cache/…`에 복사해 읽고, 본문에 "plate의 setup 스킬(`plate:setup`)을 불러"라고만 있으면 그 `SKILL.md`를 열어 따른다고 적혀 있다. 그래서 같은 본문의 0번(셋업이 안 됐으면 `plate:setup`을 부른다)을 Codex에서 따르면 절대 규칙 5를 어긴다. 본문 하나가 도구가 바뀌어도 같게 작동한다는 ADR-004, 본문을 계속 도구에 기대지 않게 쓴다는 ADR-018과 어긋난다 (`plugins/plate/skills/context/SKILL.md` 18행). 기준: 맥락 문서
- (006-verify, 검증 1) 완료 조건 7의 확인 `runcheck.py run-vrule`이 실패한다. 시험 폴더의 `docs/LESSONS.md`에 `## 미룬 문제` 절이 없고 문서 지도의 LESSONS 행이 옛 글이다. 이 상태는 run 본문에 미루는 길과 새 LESSONS 양식을 더한 `de62793`(2026-10-16 11:25) 전인 2026-10-15 23:35에 만든 것이고, 바뀐 본문으로 다시 돌리지 않았다 (`~/plate-rail-test/run-vrule/`, `plugins/plate/skills/run/SKILL.md`). 기준: 확인 실패
- (006-verify, 검증 1) 완료 조건 8의 확인 `runcheck.py run-nogit`이 같은 두 항목에서 실패한다. 상태는 `de62793` 전인 2026-10-15 23:08에 만든 것이다 (`~/plate-rail-test/run-nogit/`, `plugins/plate/skills/run/SKILL.md`). 기준: 확인 실패
- (006-verify, 검증 1) 완료 조건 9의 확인 `runcheck.py run-small`이 같은 두 항목에서 실패한다. 상태는 `de62793` 전인 2026-10-15 23:38~23:48에 만든 것이다 (`~/plate-rail-test/run-small/`, `plugins/plate/skills/run/SKILL.md`). 기준: 확인 실패
- (006-verify, 검증 1) 완료 조건 10의 확인 `runcheck.py run-all`이 같은 두 항목에서 실패한다. 상태는 `de62793` 전인 2026-10-15 23:38~10-16 00:19에 만든 것이다 (`~/plate-rail-test/run-all/`, `plugins/plate/skills/run/SKILL.md`). 기준: 확인 실패
