# 회고에서 배운 것

## 프로젝트에서 배운 것
- (004-context-rules, phase 2) 완료 조건 4의 확인은 `~/plate-rail-test/ctx-cells`의 커밋하지 않은 변경과 `~/plate-rail-test/logs/ctx-cells-*.jsonl`을 본다. 작업 전체를 검증하기 전에 그 폴더를 되돌리거나 같은 로그 이름으로 다시 돌리면 결과가 바뀐다(`run.sh`는 `logs/<로그 이름>.jsonl`을 덮어쓴다).
- (004-context-rules, 검증 1) `~/plate-rail-test/ctx-cells`의 결과와 `~/plate-rail-test/logs/ctx-cells-*.jsonl`은 커밋 `d169a15`의 context 본문으로 돌린 것이다. 그 뒤 커밋 `e2b6444`가 같은 본문의 59행(초안을 보이는 규칙)과 76행(여럿을 묻는 칸이 문장 중간에 있을 때의 꼴)을 바꿨고, 바뀐 본문으로는 이 시험을 다시 돌리지 않았다.
- (004-context-rules, 검증 1) `docs/ADR.md`의 ADR-018 이유 끝 "멈춘 이유는 없음"은 이 작업이 더한 문장 중간 칸의 규칙에 맞지 않는 꼴로 남아 있다(계획의 범위 밖). 범위 밖에 함께 적힌 2단계 완성 판정 항목은 커밋 `9b0dfb6`에서 항목째 지워졌다.
- (006-verify, 검증 1) `~/plate-rail-test`에서 완료 조건 1~3, 5, 7~11의 시험 폴더는 run-vfix를 빼고 모두 `de62793`(run과 verify에 미루는 길) 전의 본문으로 만든 상태다. 지금의 판정 도구로 대조해 통과한 경우(vf 셋, run-verify, run-wt, run-wt-gate)도 바뀐 본문으로 돌린 결과는 아니다. 다시 돌리려면 `bin/vfmake.sh`로 폴더를 다시 만들고 `bin/rerun.sh`로 돌린다. run-nogit은 `rerun.sh`에 갈래가 없어 `bin/run.sh`에 `answers/run-nogit.md`를 주어 돌린다.

## 하네스의 문제점
- (006-verify, phase 1) verify 본문 4번의 "어느 스킬의 어느 규칙인지를 적는다"를 따르려고 `vf-scope`의 검증이 프로젝트 밖의 `plugins/plate/skills/plan/SKILL.md`를 두 번 읽으려다 막혀, 실행이 179초로 늘었다(다른 둘은 44초, 63초). retro의 점검 에이전트와 같은 일이다(`docs/TOOLS.md`의 "에이전트는 프로젝트 폴더 밖의 파일을 읽지 못한다").
- (006-verify, phase 2) verify 낱말의 "작업의 커밋"은 메시지가 작업 폴더의 이름으로 시작하는 커밋을 넣는데, 프로젝트의 커밋 꼴(`[001] …`)을 따른 커밋은 그 말로 찾아지지 않는다. run-vrule에서는 모두 작업 폴더를 바꾼 커밋이라 다른 기준으로 잡혔다(verify가 스스로 적었다). retro 1번과 같은 결이다.
- (006-verify, phase 2) run-nogit의 검증이 `AGENTS.md`를 읽지 않고 "LESSONS가 문서 지도에 없다"는 하네스의 문제점을 적었다. run은 검증을 맡기기 전(phase 1 통과 때)에 이미 행을 더했다. 세션이 시작될 때 실린, 행을 더하기 전의 지침으로 판단한 것으로 보인다. run이 이 틀린 줄을 그대로 LESSONS로 옮겼다.
- (006-verify, phase 2) run-vfix의 검증 2가 "검증 절의 배운 것과 하네스의 문제점을 옮기는 단계가 하네스에 없다"고 적었는데, run은 검증이 통과한 뒤에 옮긴다(69c877b). 검증 에이전트는 프로젝트 밖의 스킬 본문을 읽지 못해 검증 뒤의 단계를 모른다. 이 줄도 LESSONS로 옮겨졌다.
- (006-verify, phase 2) run 본문 "고칠 phase를 더한다"가 TODO를 검증의 문제 하나에 항목 하나로 옮기게 해서, 원인 하나(`*.db` 줄)에서 나온 문제 셋이 TODO 셋이 됐다(run-vfix의 수행 에이전트가 적었다).
- (006-verify, phase 2) run 본문 LESSONS 절이 검증 절마다 배운 것을 옮기게 해서, 검증 1과 검증 2가 같은 사실(`booklog/`와 `tests/`가 아직 없다)을 적은 run-vfix의 LESSONS에 같은 사실이 두 줄 들어갔다.
- (006-verify, phase 3) 005 phase 7 전에 셋업된 프로젝트(문서 지도에 "하네스의 스킬이 위치를 정해 둔 기록은 묻지 않고 …"가 없다)에서 run이 `docs/LESSONS.md`를 처음 만들 때 갈린다. 처음 돌린 run-small은 프로젝트의 규칙을 따른다며 위치를 묻고 멈췄고, run-vfix는 묻지 않고 만든 뒤 "프로젝트 규칙을 어겼다"고 보고했다. setup을 다시 돌리면 없어지지만 run은 그것을 안내하지 않는다.
- (006-verify, phase 3) 검증의 문제 글에 고치는 방법이 둘(테스트를 고친다 / ARCHITECTURE에 적는다) 들어 있으면, run이 TODO에 그 글을 그대로 옮긴 뒤 양식에 없는 선택지와 추천안을 더해 물었다(run-all 첫 턴).
- (006-verify, phase 4) setup을 다시 돌릴 때 있는 구간을 표준 글과 견주려고 프로젝트 밖(`/tmp/plate-setup-check/`)에 파일을 쓰려 했다(setup-remap의 처음 실행, setup-fresh를 다시 돌린 것). 권한에 막혀 만들어지지 않았지만 3번의 "다른 파일은 만들지도 고치지도 않는다"에서 벗어난다.
- (004-context-rules, 검증 1) verify 스킬 2번("완료 조건에 적힌 확인을 하나도 빼지 않고 직접 돌린다")과 계획의 완료 조건 4: 그 확인은 실제 실행을 다시 하지 않고 남은 결과(시험 폴더의 커밋하지 않은 변경, 실행 기록)를 읽는 명령이다. 그래서 검증에서 다시 돌려도 phase 2 때의 결과를 다시 읽을 뿐이고, 그 사이 다른 작업(`e2b6444`)이 같은 본문을 고친 뒤의 동작은 보이지 않는다.
- (004-context-rules, 검증 1) verify 스킬 "낱말"의 "작업의 커밋": 다른 작업 폴더의 이름으로 시작하는 커밋을 빼서, 이 작업의 머리를 고친 커밋 `9b0dfb6`(`005-run: phase 8`. ADR 번호를 지우며 범위 밖, 완료 조건 4, 결정의 글을 바꿨다)이 점검 대상에서 빠진다. 이번에는 번호를 풀어 쓴 것뿐이라 뜻이 같았다.
- (004-context-rules, 검증 1) 계획(결정의 "저장소 밖 규칙은 여는 것과 근거로 쓰는 것을 둘 다 막는다"와 완료 조건 4의 "저장소 밖" 확인): 확인은 `$HOME/Desktop/harness-plate/plugins/plate` 아래의 경로를 빼서 플러그인 파일을 여는 것을 허용하는 쪽인데, 결정과 완료 조건 3에는 그 예외가 없다. 확인과 규칙이 다른 범위를 봐서 검증 1의 문제(다른 스킬의 파일을 여는 도구)가 phase의 회고에서도 걸리지 않았다.
- (006-verify, phase 5) run이 고칠 phase의 안 뒤에 양식에 없는 안내를 덧붙였다(004 첫 실행: bypass 모드로 바꿨는지, 계획의 결정과 부딪힐 수 있음. run-vfix 첫 턴: 고르기 전에 확인할 점). 006 phase 3의 run-all 첫 턴과 같은 일이다.
- (006-verify, phase 6) TODO "TOOLS에 판정에서 확인한 사실"을 하려면 지워진 `phase-1.md`~`phase-5.md`를 git 이력에서 읽어야 했는데, 읽을 것에 없었다. 5단계는 4단계와 달리 판정하면서 TOOLS에 적지 않았고, 통과한 phase의 파일이 지워져 사실이 git 이력과 LESSONS에만 남았다.
- (006-verify, 검증 1) 계획의 phase 5: 같은 phase에서 run 본문(LESSONS 양식, 미루는 길)을 고쳤는데 통과 조건이 완료 조건 14만 가리켰고, TODO의 "걸리는 판정이 다시 통과한다"는 run-vfix와 setup 둘만 다시 돌렸다. phase 5의 기록이 "LESSONS를 만드는 다른 경우(run-small 등)의 옛 결과를 다시 대조하면 그 두 줄이 실패한다"고 적고도 통과로 지워져, 완료 조건 7~10의 실패가 검증에서야 드러났다. 이 작업의 phase는 세션이 직접 수행해 따로 점검하는 에이전트가 없었다(머리의 결정).
- (006-verify, 검증 1) 계획의 완료 조건 12: 확인 `plancheck.py plan-test`를 적힌 대로 돌리면 전체 테스트 조건을 보는 항목이 없어, 그 조건이 없어도 통과한다. plan 스킬 "적는 규칙"의 "조건의 일부만 보는 확인은 그 조건을 확인하지 못한다"에 걸린다. phase 4는 `--base`, `--fulltest` 인자를 더해 돌렸다.
- (006-verify, 검증 1) 계획의 완료 조건 4: 확인 명령에 프롬프트가 없어 적힌 대로는 init 줄이 나오지 않고 오류로 끝난다. phase 1과 6은 `ok`를 더해 돌렸다.
- (007-harness-issues, phase 2) `~/plate-rail-test`는 git 레포가 아니라서 이 phase에서 고친 `bin/vfmake.sh`와 새로 생긴 `run-oldsetup`, `logs/run-oldsetup.*`는 커밋에 넣지 못했다. 커밋에는 `plugins/plate/skills/run/SKILL.md`와 `phase-2.md`만 든다.
- (007-harness-issues, phase 2) `run-oldsetup`의 바탕인 `vrule-base`는 LESSONS를 이 작업(001)의 `[001] phase 1 통과`(`4aa1686`)에서 만든 상태라, 그것을 지운 `a4d2a8d`를 검증이 "작업 밖의 커밋이 작업의 변경을 되돌렸다"는 하네스의 문제점으로 적었다(`run-oldsetup/docs/tasks/001-gitignore/verify.md`). 시험 폴더를 만든 방식에서 나온 줄이고, 사용자가 위치에 답하면 run이 이 줄도 LESSONS로 옮긴다.
- (007-harness-issues, phase 2) 같은 검증이 "작업의 커밋"의 메시지 기준이 `[001] …` 아래에서 하나도 맞지 않는다는 줄을 다시 적었다. phase 1이 고친 정의(작업 폴더의 파일을 바꾼 커밋도 든다)로 빠진 커밋은 없었다고 함께 적었다.

## 미룬 문제
- (004-context-rules, 검증 1) 절대 규칙 5의 "저장소 밖의 파일을 열지 않는다"에는 다른 스킬을 이름으로 부를 때 도구가 여는 스킬 파일의 예외가 없다. `docs/TOOLS.md`의 Codex 절에는 Codex가 플러그인을 `~/.codex/plugins/cache/…`에 복사해 읽고, 본문에 "plate의 setup 스킬(`plate:setup`)을 불러"라고만 있으면 그 `SKILL.md`를 열어 따른다고 적혀 있다. 그래서 같은 본문의 0번(셋업이 안 됐으면 `plate:setup`을 부른다)을 Codex에서 따르면 절대 규칙 5를 어긴다. 본문 하나가 도구가 바뀌어도 같게 작동한다는 ADR-004, 본문을 계속 도구에 기대지 않게 쓴다는 ADR-018과 어긋난다 (`plugins/plate/skills/context/SKILL.md` 18행). 기준: 맥락 문서
- (006-verify, 검증 1) 완료 조건 7의 확인 `runcheck.py run-vrule`이 실패한다. 시험 폴더의 `docs/LESSONS.md`에 `## 미룬 문제` 절이 없고 문서 지도의 LESSONS 행이 옛 글이다. 이 상태는 run 본문에 미루는 길과 새 LESSONS 양식을 더한 `de62793`(2026-10-16 11:25) 전인 2026-10-15 23:35에 만든 것이고, 바뀐 본문으로 다시 돌리지 않았다 (`~/plate-rail-test/run-vrule/`, `plugins/plate/skills/run/SKILL.md`). 기준: 확인 실패
- (006-verify, 검증 1) 완료 조건 8의 확인 `runcheck.py run-nogit`이 같은 두 항목에서 실패한다. 상태는 `de62793` 전인 2026-10-15 23:08에 만든 것이다 (`~/plate-rail-test/run-nogit/`, `plugins/plate/skills/run/SKILL.md`). 기준: 확인 실패
- (006-verify, 검증 1) 완료 조건 9의 확인 `runcheck.py run-small`이 같은 두 항목에서 실패한다. 상태는 `de62793` 전인 2026-10-15 23:38~23:48에 만든 것이다 (`~/plate-rail-test/run-small/`, `plugins/plate/skills/run/SKILL.md`). 기준: 확인 실패
- (006-verify, 검증 1) 완료 조건 10의 확인 `runcheck.py run-all`이 같은 두 항목에서 실패한다. 상태는 `de62793` 전인 2026-10-15 23:38~10-16 00:19에 만든 것이다 (`~/plate-rail-test/run-all/`, `plugins/plate/skills/run/SKILL.md`). 기준: 확인 실패
- (006-verify, 검증 1) run 본문 "검증을 맡긴다"의 첫 갈래는 닫힌 검증이면 "통과하면"의 1~3(LESSONS로 옮기기, `done-phase-N.md` 지우기, 커밋)을 건너뛰고 4번으로 간다. 검증 에이전트가 판정 "통과"의 `verify.md`를 커밋한 뒤 run이 1~3을 하기 전에 세션이 끊기면, 다시 부른 run은 검증 절을 LESSONS로 옮기지 않고, git 레포가 아니면 `done-phase-N.md`를 지우지 않는다. 그 작업은 끝나지 않은 작업도 검증이 남은 작업도 아니라서 번호 없이 부르면 찾지도 않는다. 같은 본문의 "세션을 끊고 다시 불러도 파일만 보고 잇는다"와 머리의 결정 "git 레포가 아니면 검증이 닫힌 뒤 `done-phase-N.md`를 지운다"에 어긋난다 (`plugins/plate/skills/run/SKILL.md`). 기준: 결함
