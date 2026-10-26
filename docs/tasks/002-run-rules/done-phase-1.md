# Phase 1: 본문을 `--body-file`로 넘긴다

**목표**: run에서 `gh`로 본문을 넘기는 네 곳이 모두 `--body-file`을 쓴다.

**테스트 먼저**: 아니오 — `.md`만 고친다

**읽을 것**
- `plugins/plate/skills/run/SKILL.md`의 "이슈를 올린다" 3·4번과 "PR을 연다" 3·4번
- `docs/TOOLS.md`의 "PR에서 본 것" 부근 (`--body "$( … )"`가 권한 검사에 막힌 것, `gh pr comment --body-file`이 댓글 주소 한 줄을 낸 것)
- `git show c2a983c^:docs/tasks/005-publish-verify/done-phase-2.md` (run이 `--body-file -`로 바꿔 단 장면)

**TODO**
- [x] "PR을 연다" 3번(`gh pr create`)과 4번(`gh pr comment`)이 본문을 파일이나 표준 입력으로 넘기는 `--body-file`을 쓰고, 큰따옴표 안의 명령 치환(`"$( … )"`)을 쓰지 않는다. 파일을 쓰면 프로젝트 밖의 임시 경로에 쓰고 끝난 뒤 지운다는 것도 적힌다 (`plugins/plate/skills/run/SKILL.md`)
- [x] "이슈를 올린다" 3번(`gh issue comment`)과 4번(`gh issue create`)도 같은 방식으로 `--body-file`을 쓴다 (`plugins/plate/skills/run/SKILL.md`)

**통과 조건**
- 완료 조건 1이 참이다.
  - 확인: `grep -n -- '--body ' plugins/plate/skills/run/SKILL.md`가 아무것도 내지 않는다
  - 확인: `grep -c -- '--body-file' plugins/plate/skills/run/SKILL.md`가 `4` 이상이고, 네 곳을 하나씩 읽어 모두 `--body-file`이다
  - 확인: `grep -n '"\$(' plugins/plate/skills/run/SKILL.md`가 네 곳의 줄을 내지 않는다
- 테스트가 모두 통과한다.
  - 확인: `python3 -m unittest discover -s tests`가 `OK`

## 한 일
- "PR을 연다" 3번과 4번이 `--body-file`을 쓴다: 3번은 PR 본문을, 4번은 `review.md`의 마지막 평가 절을 임시 파일에 써서 `gh pr create … --body-file {본문 파일}`, `gh pr comment {PR 주소} --body-file {댓글 파일}`로 넘긴다. 4번 아래에 임시 파일은 프로젝트 밖의 임시 경로(`mktemp`가 만든 경로)에 쓰고 명령이 끝나면 성공과 실패에 상관없이 지우며, 따옴표 안이나 명령 치환으로 본문을 넘기지 않는다는 문단을 더했다. heredoc 명령 치환 꼴은 지웠다 (`plugins/plate/skills/run/SKILL.md`)
- "이슈를 올린다" 3번과 4번도 `--body-file`을 쓴다: 댓글과 이슈 본문을 임시 파일에 써서 `gh issue comment … --body-file {댓글 파일}`, `gh issue create … --body-file {본문 파일}`로 넘긴다. 5번 아래에 같은 임시 파일 규칙 문단을 더했다 (`plugins/plate/skills/run/SKILL.md`)

## 확인 결과
- 완료 조건 1이 참이다.
  - `grep -n -- '--body ' plugins/plate/skills/run/SKILL.md` → 아무것도 내지 않음. 통과
  - `grep -c -- '--body-file' plugins/plate/skills/run/SKILL.md` → `6`(네 명령 줄과 임시 파일 규칙 문단 둘). 네 곳(310·311·426·427줄)을 하나씩 읽어 모두 `--body-file`. 통과
  - `grep -n '"\$(' plugins/plate/skills/run/SKILL.md` → 아무것도 내지 않음. 통과
- 테스트가 모두 통과한다.
  - `python3 -m unittest discover -s tests` → `Ran 99 tests in 15.482s` / `OK`. 통과

## 계획과 달라진 점
없음

## 남은 것
없음

## 하네스에서 걸린 것
- 임시 파일 규칙 문단에 금지하는 꼴을 `"$( … )"`로 그대로 적으면 통과 조건의 `grep -n '"\$('`에 걸린다. 그래서 그 꼴을 글("따옴표 안의 명령 치환")로만 적었다

## 확인 1

**통과 조건**
- 완료 조건 1이 참이다.
  - `grep -n -- '--body ' plugins/plate/skills/run/SKILL.md` → 아무것도 내지 않음. 통과
  - `grep -c -- '--body-file' plugins/plate/skills/run/SKILL.md` → `6`. 네 곳을 하나씩 읽음: 309줄 `gh issue comment … --body-file {댓글 파일}`, 310줄 `gh issue create … --body-file {본문 파일}`, 426줄 `gh pr create … --body-file {본문 파일}`, 427줄 `gh pr comment {PR 주소} --body-file {댓글 파일}`. 모두 `--body-file`. 통과
  - `grep -n '"\$(' plugins/plate/skills/run/SKILL.md` → 아무것도 내지 않음. 통과
- 테스트가 모두 통과한다.
  - `python3 -m unittest discover -s tests` → `Ran 99 tests in 15.582s` / `OK`. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 99 tests` / `OK`. 통과

**실패**
- 없음

**하네스에서 걸린 것**
- 없음

**판정**: 통과
