# Phase 2: 작업 트리의 plan을 헤드리스로 돌려 본다

**목표**: 작업 트리의 plan이 기본 브랜치에서는 `tasks/<이름>`에 커밋하고, 다른 브랜치에서는 쓰기 전에 바꿀지 묻는 것을 시험 저장소에서 본다.

**테스트 먼저**: 아니오 — 코드를 바꾸지 않고 스킬 본문을 돌려 본다

**읽을 것**
- `plugins/plate/skills/plan/SKILL.md` ("0. 셋업이 됐는지 본다", "1. 진행 중인 tasks가 있는지 본다", "2. 맥락 문서를 읽는다"의 안내 글 물음, "3." 명령 절, "7. 쓰고 커밋한다")
- `plugins/plate/skills/setup/SKILL.md` (문서 지도 구간과 `AGENTS.md`의 꼴. 시험 저장소를 차릴 때 가져온다)
- `docs/TOOLS.md` (Claude Code 절의 헤드리스 줄(`--resume`, 프롬프트는 `-p` 바로 뒤), "세션 도중의 스킬 본문 고침", "플러그인 폴더의 편집과 권한 모드", "셸의 `=` 확장")

**TODO**
- [ ] 돌리기 전에 작업 트리에서 낸 `git hash-object plugins/plate/skills/plan/SKILL.md`가 기록에 적힌다 (`docs/tasks/002-plan-branch/phase-2.md`)
- [ ] `mktemp -d`로 만든 두 시험 저장소가 차려진다. 저마다 `main` 브랜치의 git 저장소이고 origin은 없다. 문서 지도 구간이 있는 `AGENTS.md`, `@AGENTS.md`만 둔 `CLAUDE.md`, 안내 글 없이 채운 `docs/PRD.md`·`docs/ARCHITECTURE.md`(명령 절 네 줄 모두 "없음")·`docs/ADR.md`, `docs/tasks/.gitkeep`이 한 커밋으로 들어간다. 둘째 저장소는 그 뒤 `git switch -c feature/x`로 바꾼다 (시험 저장소)
- [ ] (가) 첫째 저장소에서 돌리기 전의 `git rev-parse main`을 적고, 그 폴더에서 `claude -p "/plate:plan README.md에 한 줄 소개를 더한다" --plugin-dir <작업 트리>/plugins/plate --permission-mode bypassPermissions --output-format json`을 돌린다. 이어서 같은 폴더에서 `claude -p "<답>" --resume <session_id> …`로 물음에 답하고 초안마다 승인해 커밋까지 간다. 돌린 명령과 넣은 답, 끝의 `git branch --show-current`, `git log -1 --format=%s tasks/<이름>`, `git rev-parse main`이 기록에 붙는다. 브랜치가 `tasks/<이름>`이고, 제목이 `plan: <이름>`이고, 두 `main` 해시가 같아야 한다 (`docs/tasks/002-plan-branch/phase-2.md`)
- [ ] (나) 둘째 저장소에서 돌리기 전의 `git log --oneline -1`을 적고, 같은 요청으로 첫 턴만 돌린다. 마지막 응답 글 전문과 그 자리의 `git branch --show-current`, `git log --oneline -1`, `git status --porcelain`이 기록에 붙는다. 응답이 `feature/x`와 `tasks/<이름>`을 들어 바꿀지 묻고, 브랜치가 `feature/x`이고, 마지막 커밋이 돌리기 전 그대로이고, `git status --porcelain`이 아무것도 내지 않아야 한다 (`docs/tasks/002-plan-branch/phase-2.md`)

**통과 조건**
- 완료 조건 4가 참이다.
  - 확인: 기록에 적힌 해시가 작업 트리에서 다시 낸 `git hash-object plugins/plate/skills/plan/SKILL.md`와 같다
  - 확인: 기록에 붙은 (가)의 출력에서 브랜치가 `tasks/<이름>`이고, 제목이 `plan: <이름>`이고, 돌리기 전과 뒤의 `main` 해시가 같다
  - 확인: 기록에 붙은 (나)의 응답 글이 `feature/x`와 `tasks/<이름>`을 들어 바꿀지 묻고, 브랜치가 `feature/x`이고, 마지막 커밋이 돌리기 전 그대로이고, `git status --porcelain`의 출력이 비었다
- 시험이 이 저장소를 바꾸지 않았다.
  - 확인: `git status --porcelain -- . ':!docs/tasks/002-plan-branch/phase-2.md' ':!docs/tasks/RUNLOG.md'`가 아무것도 내지 않는다
- 완료 조건 1, 2, 3이 그대로 참이다.
  - 확인: `grep -c -e '브랜치를 만들거나 바꾸지 않는다' plugins/plate/skills/plan/SKILL.md`가 `0`이다
  - 확인: `grep -c -e 'plan은 브랜치를 바꾸지 않아서' -e '계획의 커밋이 로컬 기본 브랜치에만' plugins/plate/skills/run/SKILL.md`가 `0`이다
  - 확인: `grep -c -e '계획의 커밋이 로컬 기본 브랜치에만' docs/ARCHITECTURE.md README.md`가 두 파일 모두 `0`이다
- 테스트가 모두 통과한다(완료 조건 5).
  - 확인: `python3 -m unittest discover -s tests`가 OK다
