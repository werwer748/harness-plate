# Phase 5: 헤드리스 판정과 TOOLS

**목표**: 시험 폴더 셋의 실제 실행이 plan의 엣지케이스 물음, 테스트 먼저 기록, 계획 없는 편집 차단을 보이고, TOOLS에 훅 사실이 적힌다.

**읽을 것**
- `docs/TOOLS.md` (Claude Code 절: 헤드리스 명령의 꼴, 여러 턴, 서브에이전트 기록의 `parent_tool_use_id`, 허용 목록)
- `~/plate-rail-test/bin/vfmake.sh`, `~/plate-rail-test/bin/run.sh`, `~/plate-rail-test/bin/summ.py` (시험 폴더 만들기, 헤드리스 실행, 기록 읽기)
- `~/plate-rail-test/test-base` (booklog. 테스트가 있고 001이 검증 통과. 전체 테스트는 `.venv/bin/python -m pytest`)
- `plugins/plate/skills/plan/SKILL.md` (phase 2가 바꾼 양식과 5번)
- `plugins/plate/hooks/` (phase 1의 훅)

**TODO**
- [ ] `bin/vfmake.sh`가 tdd-plan, tdd-run, tdd-edit을 만든다. tdd-run에는 테스트 먼저 "예"인 phase 하나의 계획(작업 002)을 얹는다 (`~/plate-rail-test/bin/vfmake.sh`)
- [ ] 완료 조건 9의 tdd-plan 기록과 답 파일이 있다 (`~/plate-rail-test/logs/`, `~/plate-rail-test/answers/`)
- [ ] 완료 조건 10의 tdd-run 기록이 있다 (`~/plate-rail-test/logs/tdd-run.jsonl`)
- [ ] 완료 조건 11의 tdd-edit 기록이 있다 (`~/plate-rail-test/logs/tdd-edit.jsonl`)
- [ ] TOOLS의 Claude Code 절에 완료 조건 12의 사실이 날짜·버전과 함께 적힌다 (`docs/TOOLS.md`)

**통과 조건**
- 머리의 완료 조건 1~13이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다
