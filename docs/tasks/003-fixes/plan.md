# tasks 끝의 문제를 고친다

## 목표
tasks 끝의 코드 평가와 하네스 eval에서 고치기로 한 것을 모두 고친다.

## 범위 밖
- 코드 평가와 하네스 eval을 다시 하는 것
- plate 자체의 하네스 고칠 거리를 고치는 것. 이슈로 올리고 plate 저장소에서 고친다

## 완료 조건
1. 절대 규칙 1·2가 쓰기와 커밋을 보고서와 지도 행으로만 묶어, 7번에서 부른 `plate:plan`이 `docs/tasks/`를 쓰고 커밋하는 것과 부딪힌다. 절대 규칙 4처럼 plan의 쓰기와 커밋도 plan의 규칙에 맡긴다고 적는다 (`plugins/plate/skills/cleanup/SKILL.md:16-19`, `130`)
   - 확인: `plugins/plate/skills/cleanup/SKILL.md`의 절대 규칙 절과 7번을 읽어, plan이 쓰고 커밋하는 것이 절대 규칙과 부딪히지 않는다
2. 기존 작업 정합성이 읽는 열린 이슈의 글을 지시가 아니라 데이터로만 보라는 규칙이 맡기는 글에 없다 (`plugins/plate/skills/cleanup/SKILL.md:82`, `151-155`)
   - 확인: `plugins/plate/skills/cleanup/SKILL.md`의 기존 작업 정합성 행과 1·2라운드에 맡기는 글을 읽어, 이슈의 글을 데이터로만 본다는 규칙이 있다
3. cleanup 스킬의 주된 동작에 되풀이 가능한 테스트가 없고 한 번의 손 시험만 있다 (`plugins/plate/skills/cleanup/SKILL.md`)
   - 확인: `tests/` 아래에 cleanup 스킬을 보는 테스트가 있고, 그 스킬이 깨지면 실패한다. `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
4. 스킬을 헤드리스로 돌려 보는 확인에 필요한 허용 목록이 도구 기록에 없다. "Claude Code" 절에 `--allowedTools`에 넣을 명령(`git ls-files`, `git rev-parse`, `git -C … show` 꼴, 파이프를 이은 Bash)을 막힌 명령 목록에서 옮겨 적는다 (`docs/TOOLS.md`)
   - 확인: `docs/TOOLS.md`의 "Claude Code" 절을 읽어 그 허용 목록이 있다
5. run 전에 권한 모드를 정하라는 줄이 `docs/TOOLS.md`에만 있어 실행 전에 읽히지 않았다. 스킬 본문(`plugins/plate/skills/`)을 쓰는 tasks는 run 전에 plan 모드를 끄고 그 경로의 쓰기를 허용한다는 줄을 작업 규칙에 둔다 (`AGENTS.md`)
   - 확인: `AGENTS.md`의 작업 규칙 절을 읽어 그 줄이 있다
6. tasks 완료 조건 1, 2, 3이 참이다.
   - 확인: `test -f plugins/plate/skills/cleanup/SKILL.md`가 0으로 끝난다
   - 확인: `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
   - 확인: `docs/TOOLS.md`의 새 절을 읽어, 두 장면이 저마다 Claude Code 버전, 돌린 시각, 세션 id, 결과(장면 1: 커밋된 파일 목록과 보고서의 여섯 기준 절, 장면 2: `plate:plan` 호출 줄)를 적었다. 하나라도 없으면 실패
   - 확인: 그 절에 적힌 돌린 시각이 `git log -1 --format=%cI -- plugins/plate/skills/cleanup/SKILL.md`보다 늦다
   - 확인: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json`의 두 줄이 모두 `0.15.0`
   - 확인: `grep -c cleanup plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json`가 두 파일 모두 1 이상
   - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
   - 확인: `docs/PRD.md`, `docs/ARCHITECTURE.md`, `README.md`를 문서마다 따로 읽어 cleanup 스킬(9단계를 만들었다, 디렉터리 구조, 스킬 목록과 부르는 이름)과 어긋나는 줄이 없다

## 결정
- phase 2를 더해 두 장면을 다시 돌린다. 이유: 완료 조건 1·2가 SKILL.md를 고쳐 완료 조건 6의 시각 확인이 지난 기록으로는 참이 될 수 없다
