# Phase 2: plan과 phase의 테스트 먼저 규칙

**목표**: plan과 phase 본문의 테스트 먼저 규칙이 훅의 범위와 맞고, plan이 목표를 모두 완료 조건에 담고, 엣지케이스 후보에서 이미 정한 동작을 뺀다.

**테스트 먼저**: 아니오 — 스킬 본문(`.md`)만 고친다

**읽을 것**
- `plugins/plate/skills/plan/SKILL.md` (낱말, 5번, 적는 규칙)
- `plugins/plate/skills/phase/SKILL.md` (2번의 테스트 먼저 규칙)
- `plugins/plate/hooks/edit_guard.py`의 `has_tests`와 `manifest_has_test_command` (훅이 보는 테스트가 있는 프로젝트의 기준)
- `git show ec2f192:docs/LESSONS.md`의 하네스의 문제점 절에서 (007-harness-issues, 검증 1)의 첫째 줄, (008-tdd, phase 1)의 셋째 줄, (008-tdd, phase 2)의 둘째 줄, (008-tdd, phase 3)의 둘째·셋째 줄, (008-tdd, phase 5)의 둘째 줄 (고칠 문제의 원문)

**TODO**
- [ ] plan의 낱말 "테스트가 있는 프로젝트"가 훅과 같은 기준이다: 테스트 파일이 있거나, `package.json`의 `scripts.test`(npm의 기본 자리표시 글은 빼고)나 `Makefile`의 `test` 대상이 있다 (`plugins/plate/skills/plan/SKILL.md`)
- [ ] plan 적는 규칙의 테스트 먼저에서 "예"는 테스트가 있는 프로젝트에서 코드 파일(`.md`가 아닌 파일)의 동작을 바꾸는 phase이고, 테스트가 없는 프로젝트의 phase와 `.md`만 고치는 phase는 "아니오"와 그 이유다 (`plugins/plate/skills/plan/SKILL.md`)
- [ ] plan 적는 규칙에 목표에 적은 것은 모두 어느 완료 조건에 든다는 규칙이 있다 (`plugins/plate/skills/plan/SKILL.md`)
- [ ] plan 5번에서 엣지케이스 후보에 요청이나 완료 조건이 이미 정한 동작을 내지 않는다 (`plugins/plate/skills/plan/SKILL.md`)
- [ ] phase 2번에서 고칠 문제를 넘겨받았으면 동작을 바꾸는 문제에만 테스트부터 쓰고, 테스트 먼저 기록에 실패 출력이 없다는 문제는 구현 파일만 git으로 그 phase 커밋의 부모 것으로 잠깐 되돌려 테스트를 돌려 실패 출력을 얻고 다시 돌려놓는다 (`plugins/plate/skills/phase/SKILL.md`)

**통과 조건**
- 완료 조건 3이 참이다.
  - 확인: 완료 조건 3의 확인을 모두 돌린다
- 완료 조건 4가 참이다.
  - 확인: 완료 조건 4의 확인을 모두 돌린다
