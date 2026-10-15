# 회고에서 배운 것

## 프로젝트에서 배운 것
- (004-context-rules, phase 2) 완료 조건 4의 확인은 `~/plate-rail-test/ctx-cells`의 커밋하지 않은 변경과 `~/plate-rail-test/logs/ctx-cells-*.jsonl`을 본다. 작업 전체를 검증하기 전에 그 폴더를 되돌리거나 같은 로그 이름으로 다시 돌리면 결과가 바뀐다(`run.sh`는 `logs/<로그 이름>.jsonl`을 덮어쓴다).

## 하네스의 문제점
- (006-verify, phase 1) verify 본문 4번의 "어느 스킬의 어느 규칙인지를 적는다"를 따르려고 `vf-scope`의 검증이 프로젝트 밖의 `plugins/plate/skills/plan/SKILL.md`를 두 번 읽으려다 막혀, 실행이 179초로 늘었다(다른 둘은 44초, 63초). retro의 점검 에이전트와 같은 일이다(`docs/TOOLS.md`의 "에이전트는 프로젝트 폴더 밖의 파일을 읽지 못한다").
- (006-verify, phase 2) verify 낱말의 "작업의 커밋"은 메시지가 작업 폴더의 이름으로 시작하는 커밋을 넣는데, 프로젝트의 커밋 꼴(`[001] …`)을 따른 커밋은 그 말로 찾아지지 않는다. run-vrule에서는 모두 작업 폴더를 바꾼 커밋이라 다른 기준으로 잡혔다(verify가 스스로 적었다). retro 1번과 같은 결이다.
- (006-verify, phase 2) run-nogit의 검증이 `AGENTS.md`를 읽지 않고 "LESSONS가 문서 지도에 없다"는 하네스의 문제점을 적었다. run은 검증을 맡기기 전(phase 1 통과 때)에 이미 행을 더했다. 세션이 시작될 때 실린, 행을 더하기 전의 지침으로 판단한 것으로 보인다. run이 이 틀린 줄을 그대로 LESSONS로 옮겼다.
- (006-verify, phase 2) run-vfix의 검증 2가 "검증 절의 배운 것과 하네스의 문제점을 옮기는 단계가 하네스에 없다"고 적었는데, run은 검증이 통과한 뒤에 옮긴다(69c877b). 검증 에이전트는 프로젝트 밖의 스킬 본문을 읽지 못해 검증 뒤의 단계를 모른다. 이 줄도 LESSONS로 옮겨졌다.
- (006-verify, phase 2) run 본문 "고칠 phase를 더한다"가 TODO를 검증의 문제 하나에 항목 하나로 옮기게 해서, 원인 하나(`*.db` 줄)에서 나온 문제 셋이 TODO 셋이 됐다(run-vfix의 수행 에이전트가 적었다).
- (006-verify, phase 2) run 본문 LESSONS 절이 검증 절마다 배운 것을 옮기게 해서, 검증 1과 검증 2가 같은 사실(`booklog/`와 `tests/`가 아직 없다)을 적은 run-vfix의 LESSONS에 같은 사실이 두 줄 들어갔다.
