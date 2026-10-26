# Phase 1: 본문을 `--body-file`로 넘긴다

**목표**: run에서 `gh`로 본문을 넘기는 네 곳이 모두 `--body-file`을 쓴다.

**테스트 먼저**: 아니오 — `.md`만 고친다

**읽을 것**
- `plugins/plate/skills/run/SKILL.md`의 "이슈를 올린다" 3·4번과 "PR을 연다" 3·4번
- `docs/TOOLS.md`의 "PR에서 본 것" 부근 (`--body "$( … )"`가 권한 검사에 막힌 것, `gh pr comment --body-file`이 댓글 주소 한 줄을 낸 것)
- `git show c2a983c^:docs/tasks/005-publish-verify/done-phase-2.md` (run이 `--body-file -`로 바꿔 단 장면)

**TODO**
- [ ] "PR을 연다" 3번(`gh pr create`)과 4번(`gh pr comment`)이 본문을 파일이나 표준 입력으로 넘기는 `--body-file`을 쓰고, 큰따옴표 안의 명령 치환(`"$( … )"`)을 쓰지 않는다. 파일을 쓰면 프로젝트 밖의 임시 경로에 쓰고 끝난 뒤 지운다는 것도 적힌다 (`plugins/plate/skills/run/SKILL.md`)
- [ ] "이슈를 올린다" 3번(`gh issue comment`)과 4번(`gh issue create`)도 같은 방식으로 `--body-file`을 쓴다 (`plugins/plate/skills/run/SKILL.md`)

**통과 조건**
- 완료 조건 1이 참이다.
  - 확인: `grep -n -- '--body ' plugins/plate/skills/run/SKILL.md`가 아무것도 내지 않는다
  - 확인: `grep -c -- '--body-file' plugins/plate/skills/run/SKILL.md`가 `4` 이상이고, 네 곳을 하나씩 읽어 모두 `--body-file`이다
  - 확인: `grep -n '"\$(' plugins/plate/skills/run/SKILL.md`가 네 곳의 줄을 내지 않는다
- 테스트가 모두 통과한다.
  - 확인: `python3 -m unittest discover -s tests`가 `OK`
