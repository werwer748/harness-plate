# Phase 1: 훅의 네 결함

**목표**: 훅이 테스트 실행 부산물, 하네스 기록 폴더, 계획 고침, 없는 스크립트를 바르게 다루고 이 레포가 `__pycache__/`를 거른다.

**테스트 먼저**: 예

**읽을 것**
- `plugins/plate/hooks/edit_guard.py` (코드 파일과 테스트 파일의 기준, 막은 횟수를 세는 `count_block`)
- `plugins/plate/hooks/hooks.json` (훅 명령)
- `tests/test_edit_guard.py` (시험 프로젝트를 만들고 훅에 JSON을 주는 틀)
- `docs/TOOLS.md`의 Claude Code 절 훅 묶음 (`${CLAUDE_PLUGIN_ROOT}`가 `--plugin-dir`의 폴더가 된다)
- code.claude.com/docs/en/hooks (명령은 `sh -c`로 돌고, `${CLAUDE_PLUGIN_ROOT}`는 글로 바뀌고 환경 변수로도 넘어간다. 2가 아닌 0이 아닌 종료 코드는 막지 않는다)
- `git show ec2f192:docs/LESSONS.md`의 하네스의 문제점 절에서 (008-tdd, phase 1)의 첫째·둘째 줄, (008-tdd, phase 3)의 첫째 줄, (008-tdd, phase 4)의 둘째 줄, (008-tdd, 검증 1)의 첫째 줄 (고칠 문제의 원문)

**TODO**
- [ ] 커밋되지 않은 변경 가운데 `__pycache__/` 아래 파일과 `.pyc` 파일은 테스트 변경으로 세지 않는다. `.gitignore`가 없는 Python 프로젝트에서 테스트를 돌리기만 해서는 테스트 먼저 검사가 풀리지 않는다 (`plugins/plate/hooks/edit_guard.py`)
- [ ] `docs/tasks/` 아래 파일은 코드 파일이 아니다. 문서 지도가 있고 남은 phase가 없는 프로젝트에서 `docs/tasks/.gitkeep`을 써도 막지 않는다 (`plugins/plate/hooks/edit_guard.py`)
- [ ] 테스트 먼저로 막은 횟수는 그 phase의 계획 줄과 `plan.md`가 바뀌지 않은 동안 센다. `plan.md`만 바뀌어도(결정에 한 줄을 더해도) 다시 센다 (`plugins/plate/hooks/edit_guard.py`)
- [ ] `hooks.json`의 명령은 스크립트 파일이 없으면 종료 코드 0으로 끝나고, 있으면 스크립트의 종료 코드로 끝난다 (`plugins/plate/hooks/hooks.json`)
- [ ] 위 넷마다 그 상황을 만들고 막음이나 통과를 단언하는 테스트가 있다. `hooks.json`의 명령은 그 글을 `sh -c`로 돌려 본다 (`tests/test_edit_guard.py`)
- [ ] 이 레포의 `.gitignore`가 `__pycache__/`를 거른다 (`.gitignore`)

**통과 조건**
- 완료 조건 1이 참이다.
  - 확인: 완료 조건 1의 확인을 모두 돌린다
- 완료 조건 2가 참이다.
  - 확인: 완료 조건 2의 확인을 돌린다
