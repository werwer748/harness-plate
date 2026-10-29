# Phase 3: 워크플로 양식의 액션을 커밋 SHA로 고정한다

**목표**: 보안-4가 고쳐져, CI 워크플로 양식의 액션이 모두 커밋 SHA로 고정된다.

**테스트 먼저**: 아니오 — 스킬 본문(`.md`)만 고친다

**읽을 것**
- `docs/cleanup/2026-10-29.md` (보안-4의 근거, 좁힌 범위, 2라운드 판정)
- `plugins/plate/skills/setup/SKILL.md`의 CI 워크플로 양식 (`uses:` 줄 넷)
- `docs/ADR.md`의 ADR-021·022 (plate를 기본 브랜치에서 받는 것은 감수)

**TODO**
- [ ] 양식의 `uses:` 줄마다 지금 태그가 가리키는 커밋을 `git ls-remote`로 얻어, `@` 뒤를 40자리 SHA로 바꾸고 줄 끝에 `# {태그}`를 붙인다. 태그 이름과 그 밖의 줄은 그대로다 (`plugins/plate/skills/setup/SKILL.md`)
- [ ] `tests/`에서 바뀐 `uses:` 줄의 옛 글(`@v7`, `@v1`, `@v8`)을 찾아(`git grep -n -e '@v7' -e '@v1' -e '@v8' -- tests/`), 걸리는 테스트가 있으면 새 글을 지키게 고친다 (`tests/`)

**통과 조건**
- 모든 `uses:` 줄이 SHA로 고정된다(완료 조건 3).
  - 확인: `grep -nE 'uses: ' plugins/plate/skills/setup/SKILL.md` → 모든 줄이 `uses: <소유자>/<이름>@<40자리 16진수> # v<수>` 꼴
  - 확인: 그 줄마다 `git ls-remote https://github.com/<소유자>/<이름> 'refs/tags/<태그>' 'refs/tags/<태그>^{}'`를 돌려, `^{}` 줄이 있으면 그 해시, 없으면 태그 줄의 해시가 줄의 SHA와 같다
- 앞 phase의 동작이 그대로다(완료 조건 1·2).
  - 확인: `python3 -m unittest tests.test_verdict -v` → `OK`
- 테스트 묶음이 통과한다.
  - 확인: `python3 -m unittest discover -s tests` → 마지막 줄이 `OK`
