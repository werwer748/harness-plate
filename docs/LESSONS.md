# 회고에서 배운 것

## 프로젝트에서 배운 것
- (004-context-rules, phase 1) ADR-013의 "없다고 답한 칸은 "없음"으로 적는다"는 이제 줄 전체가 칸일 때만 그대로다. 문장 중간에 있는 칸은 이어지는 문장으로 적는다(context 스킬 본문의 74번 줄). 이 갈림은 이 작업의 결정과 스킬 본문에만 있고 `docs/ADR.md`에는 없다.
- (004-context-rules, phase 2) 완료 조건 4의 확인은 `~/plate-rail-test/ctx-cells`의 커밋하지 않은 변경과 `~/plate-rail-test/logs/ctx-cells-*.jsonl`을 본다. 작업 전체를 검증하기 전에 그 폴더를 되돌리거나 같은 로그 이름으로 다시 돌리면 결과가 바뀐다(`run.sh`는 `logs/<로그 이름>.jsonl`을 덮어쓴다).

## 하네스의 문제점
