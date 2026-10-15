# 회고에서 배운 것

## 프로젝트에서 배운 것
- (004-context-rules, phase 2) 완료 조건 4의 확인은 `~/plate-rail-test/ctx-cells`의 커밋하지 않은 변경과 `~/plate-rail-test/logs/ctx-cells-*.jsonl`을 본다. 작업 전체를 검증하기 전에 그 폴더를 되돌리거나 같은 로그 이름으로 다시 돌리면 결과가 바뀐다(`run.sh`는 `logs/<로그 이름>.jsonl`을 덮어쓴다).

## 하네스의 문제점
- (006-verify, phase 1) verify 본문 4번의 "어느 스킬의 어느 규칙인지를 적는다"를 따르려고 `vf-scope`의 검증이 프로젝트 밖의 `plugins/plate/skills/plan/SKILL.md`를 두 번 읽으려다 막혀, 실행이 179초로 늘었다(다른 둘은 44초, 63초). retro의 점검 에이전트와 같은 일이다(`docs/TOOLS.md`의 "에이전트는 프로젝트 폴더 밖의 파일을 읽지 못한다").
