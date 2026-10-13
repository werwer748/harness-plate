# Phase 5: 완성 판정을 돌린다

**목표**: 완료 조건 1~15가 실제 실행으로 참이다.

**읽을 것**
- `docs/TOOLS.md` ("Claude Code" 절)
- `~/plate-rail-test/bin/run.sh`, `bin/runcheck.py`, `bin/plancheck.py`, `answers/run-*.md` (Phase 4에서 준비한 것)

**TODO**
- [ ] phase 하나짜리 작업의 판정 결과가 생긴다: 완료 조건 1, 4, 5, 6, 9, 11, 12, 13 (`~/plate-rail-test/logs/run-*.jsonl`)
- [ ] 여러 phase와 이어 하기의 판정 결과가 생긴다: 완료 조건 2, 3, 7
- [ ] worktree와 git 레포가 아닌 폴더의 판정 결과가 생긴다: 완료 조건 8, 10
- [ ] plan 다시 판정과 excel-viewer의 판정 결과가 생긴다: 완료 조건 14, 15
- [ ] 사용자에게 보인 글(다섯 줄, 세 줄, 물음, 보고)을 요청·답 파일과 나란히 놓은 표가 사용자에게 보여진다
- [ ] 기대와 다른 경우가 있었으면 스킬이 고쳐지고 그 경우가 다시 통과한다. 본문의 규칙을 바꿔야 하면 고치기 전에 사용자에게 묻는다 (`plugins/plate/skills/`)
- [ ] 판정하며 새로 확인한 도구 사실이 "Claude Code" 절에 적힌다 (`docs/TOOLS.md`)

**통과 조건**
- 완료 조건 1~15가 참이다.
  - 확인: 조건마다의 확인을 돌리고 읽어 기대와 같은지 본다
- 사용자가 표를 보고 확인했다.
  - 확인: 표를 적은 답글에 받은 답
