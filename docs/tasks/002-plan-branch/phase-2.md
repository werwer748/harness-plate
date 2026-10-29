# Phase 2: 작업 트리의 plan을 헤드리스로 돌려 본다

**목표**: 작업 트리의 plan이 기본 브랜치에서는 `tasks/<이름>`에 커밋하고, 다른 브랜치에서는 쓰기 전에 바꿀지 묻는 것을 시험 저장소에서 본다.

**테스트 먼저**: 아니오 — 코드를 바꾸지 않고 스킬 본문을 돌려 본다

**읽을 것**
- `plugins/plate/skills/plan/SKILL.md` ("0. 셋업이 됐는지 본다", "1. 진행 중인 tasks가 있는지 본다", "2. 맥락 문서를 읽는다"의 안내 글 물음, "3." 명령 절, "7. 쓰고 커밋한다")
- `plugins/plate/skills/setup/SKILL.md` (문서 지도 구간과 `AGENTS.md`의 꼴. 시험 저장소를 차릴 때 가져온다)
- `docs/TOOLS.md` (Claude Code 절의 헤드리스 줄(`--resume`, 프롬프트는 `-p` 바로 뒤), "세션 도중의 스킬 본문 고침", "플러그인 폴더의 편집과 권한 모드", "셸의 `=` 확장")

**TODO**
- [x] 돌리기 전에 작업 트리에서 낸 `git hash-object plugins/plate/skills/plan/SKILL.md`가 기록에 적힌다 (`docs/tasks/002-plan-branch/phase-2.md`)
- [x] `mktemp -d`로 만든 두 시험 저장소가 차려진다. 저마다 `main` 브랜치의 git 저장소이고 origin은 없다. 문서 지도 구간이 있는 `AGENTS.md`, `@AGENTS.md`만 둔 `CLAUDE.md`, 안내 글 없이 채운 `docs/PRD.md`·`docs/ARCHITECTURE.md`(명령 절 네 줄 모두 "없음")·`docs/ADR.md`, `docs/tasks/.gitkeep`이 한 커밋으로 들어간다. 둘째 저장소는 그 뒤 `git switch -c feature/x`로 바꾼다 (시험 저장소)
- [x] (가) 첫째 저장소에서 돌리기 전의 `git rev-parse main`을 적고, 그 폴더에서 `claude -p "/plate:plan README.md에 한 줄 소개를 더한다" --plugin-dir <작업 트리>/plugins/plate --permission-mode bypassPermissions --output-format json`을 돌린다. 이어서 같은 폴더에서 `claude -p "<답>" --resume <session_id> …`로 물음에 답하고 초안마다 승인해 커밋까지 간다. 돌린 명령과 넣은 답, 끝의 `git branch --show-current`, `git log -1 --format=%s tasks/<이름>`, `git rev-parse main`이 기록에 붙는다. 브랜치가 `tasks/<이름>`이고, 제목이 `plan: <이름>`이고, 두 `main` 해시가 같아야 한다 (`docs/tasks/002-plan-branch/phase-2.md`)
- [x] (나) 둘째 저장소에서 돌리기 전의 `git log --oneline -1`을 적고, 같은 요청으로 첫 턴만 돌린다. 마지막 응답 글 전문과 그 자리의 `git branch --show-current`, `git log --oneline -1`, `git status --porcelain`이 기록에 붙는다. 응답이 `feature/x`와 `tasks/<이름>`을 들어 바꿀지 묻고, 브랜치가 `feature/x`이고, 마지막 커밋이 돌리기 전 그대로이고, `git status --porcelain`이 아무것도 내지 않아야 한다 (`docs/tasks/002-plan-branch/phase-2.md`)

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

## 한 일
- 돌리기 전에 작업 트리에서 낸 `git hash-object plugins/plate/skills/plan/SKILL.md`가 기록에 적힌다: 시험을 돌리기 전에 `git hash-object plugins/plate/skills/plan/SKILL.md` → `85a5bb1528ac6afabf3cce1741093fb2e5436585` (`docs/tasks/002-plan-branch/phase-2.md`)
- `mktemp -d`로 만든 두 시험 저장소가 차려진다: 스크래치패드의 스크립트로 `mktemp -d` 두 곳에 `git init -b main`, origin 없음. 문서 지도 구간(setup의 구간에서 `docs/DESIGN.md` 행을 뺀 것)이 있는 `AGENTS.md`, `@AGENTS.md` 한 줄의 `CLAUDE.md`, 안내 글 없는 `docs/PRD.md`(문제: README가 프로젝트를 소개하지 않는다)·`docs/ARCHITECTURE.md`(명령 절 네 줄 모두 "없음")·`docs/ADR.md`("없음"), `docs/tasks/.gitkeep`, `README.md`(`# demo`)를 한 커밋 `init`으로 넣었다. 둘째는 그 뒤 `git switch -c feature/x` (시험 저장소)
  - 첫째: `/var/folders/0j/cj37rxmj1mj73vhflqpgsxm00000gn/T/tmp.qjxbXaQhPP`, 둘째: `/var/folders/0j/cj37rxmj1mj73vhflqpgsxm00000gn/T/tmp.VMXMJ2OllR`. 두 저장소의 `init` 커밋은 같은 내용·같은 작성자로 `fbf9069`이다
- (가) 첫째 저장소에서 계획 커밋까지 갔다 (`docs/tasks/002-plan-branch/phase-2.md`)
  - 돌리기 전: `git rev-parse main` → `fbf90696422c93080b39905472ecd054162bd276`, `git branch --show-current` → `main`, `git remote -v` → 출력 없음
  - 1턴: `claude -p "/plate:plan README.md에 한 줄 소개를 더한다" --plugin-dir /Users/hugo/Desktop/harness-plate/plugins/plate --permission-mode bypassPermissions --output-format json` → session_id `3d1038bd-fc53-4da9-8fec-dc47361900df`. 응답이 "브랜치: 지금은 `main`입니다. 원격이 없어서 `main`을 기본 브랜치로 보고, 쓸 때 `tasks/<이름>` 브랜치를 만듭니다."라고 적고 브랜치를 묻지 않은 채 질문 1(소개 문장)을 냈다
  - 2턴: `claude -p "1. 자리도 그대로 좋다." --resume 3d1038bd-fc53-4da9-8fec-dc47361900df --plugin-dir … --permission-mode bypassPermissions --output-format json` → tasks 머리 초안(이름 `readme-intro`, "브랜치 `tasks/readme-intro`는 아직 없습니다")
  - 3턴: `claude -p "승인한다." --resume …`(같은 옵션) → task `001-readme-intro` 초안
  - 4턴: `claude -p "승인한다." --resume …`(같은 옵션) → "브랜치: `main`에서 `tasks/readme-intro`를 만들어 바꿨습니다. 커밋: `a132ba7 plan: readme-intro`에 아래 세 계획 파일만 넣었습니다."
  - 끝: `git branch --show-current` → `tasks/readme-intro`, `git log -1 --format=%s tasks/readme-intro` → `plan: readme-intro`, `git rev-parse main` → `fbf90696422c93080b39905472ecd054162bd276`, `git status --porcelain` → 출력 없음, `git show --stat HEAD` → `docs/tasks/001-readme-intro/phase-1.md`, `docs/tasks/001-readme-intro/plan.md`, `docs/tasks/plan.md` 세 파일
- (나) 둘째 저장소에서 첫 턴만 돌렸다 (`docs/tasks/002-plan-branch/phase-2.md`)
  - 돌리기 전: `git log --oneline -1` → `fbf9069 init`
  - `claude -p "/plate:plan README.md에 한 줄 소개를 더한다" --plugin-dir /Users/hugo/Desktop/harness-plate/plugins/plate --permission-mode bypassPermissions --output-format json`
  - 마지막 응답 글 전문:

    > setup은 되어 있고(`AGENTS.md`에 문서 지도 구간이 있습니다) 진행 중인 tasks도 없습니다(`docs/tasks/plan.md` 없음). 그래서 새 tasks로 계획합니다.
    >
    > 다만 지금 브랜치가 `feature/x`입니다. 기본 브랜치(`main`, origin이 없어 `main`으로 봅니다)도 아니고 `tasks/<이름>`도 아닙니다.
    >
    > **계획을 `tasks/<이름>` 브랜치에 커밋해도 될까요?** `<이름>`은 tasks 머리 초안에서 정해 함께 승인받습니다(예: `readme-intro`).
    >
    > - **추천: 예.** 실행 스킬(`plate:run`)의 PR과 합침은 늘 `tasks/<이름>`을 기준으로 다룹니다. 그래서 `feature/x`에 넣은 계획 커밋은 PR과 합침에 들어가지 않습니다. 승인하시면 모든 초안을 승인받은 뒤, 파일을 쓰기 전에 지금 HEAD(`feature/x`)에서 `tasks/<이름>`을 만들어 바꿉니다.
    > - **아니오**를 고르시면 아무 파일도 쓰지 않고 여기서 끝냅니다.

  - 그 자리: `git branch --show-current` → `feature/x`, `git log --oneline -1` → `fbf9069 init`, `git status --porcelain` → 출력 없음

## 확인 결과
- 완료 조건 4가 참이다.
  - 다시 낸 `git hash-object plugins/plate/skills/plan/SKILL.md` → `85a5bb1528ac6afabf3cce1741093fb2e5436585`, 기록의 값과 같다. 통과
  - (가)의 출력: 브랜치 `tasks/readme-intro`, 제목 `plan: readme-intro`, 돌리기 전과 뒤의 `main`이 모두 `fbf90696422c93080b39905472ecd054162bd276`. 통과
  - (나)의 응답이 `feature/x`와 `tasks/<이름>`을 들어 커밋(바꿀지)을 묻고, 브랜치 `feature/x`, 마지막 커밋 `fbf9069 init`(돌리기 전 그대로), `git status --porcelain` 출력 없음. 통과
- 시험이 이 저장소를 바꾸지 않았다.
  - `git status --porcelain -- . ':!docs/tasks/002-plan-branch/phase-2.md' ':!docs/tasks/RUNLOG.md'` → 출력 없음. 통과
- 완료 조건 1, 2, 3이 그대로 참이다.
  - `grep -c -e '브랜치를 만들거나 바꾸지 않는다' plugins/plate/skills/plan/SKILL.md` → `0`. 통과
  - `grep -c -e 'plan은 브랜치를 바꾸지 않아서' -e '계획의 커밋이 로컬 기본 브랜치에만' plugins/plate/skills/run/SKILL.md` → `0`. 통과
  - `grep -c -e '계획의 커밋이 로컬 기본 브랜치에만' docs/ARCHITECTURE.md README.md` → `README.md:0`, `docs/ARCHITECTURE.md:0`. 통과
- 테스트가 모두 통과한다(완료 조건 5).
  - `python3 -m unittest discover -s tests` → `Ran 207 tests in 18.435s`, `OK`. 통과

## 계획과 달라진 점
- TODO의 시험 저장소 첫 커밋에 든 파일 목록에 `README.md`가 없지만, 요청("README.md에 한 줄 소개를 더한다")이 고칠 파일이 있어야 plan이 3번에서 그 파일을 읽을 수 있어 `README.md`(`# demo`)도 같은 커밋에 넣었다. 문서 지도에서는 시험 저장소에 없는 `docs/DESIGN.md` 행을 뺐다

## 남은 것
- (나)는 물음까지만 봤다. 승인한 뒤 `feature/x`에서 `tasks/<이름>`을 만드는 갈래와 거절해 끝나는 갈래는 돌리지 않았다(task 머리의 결정과 범위 밖대로)
- 두 시험 저장소는 `mktemp -d` 아래에 그대로 남아 있다

## 하네스에서 걸린 것
- 없음

## 확인 1

**통과 조건**
- 완료 조건 4가 참이다.
  - `git hash-object plugins/plate/skills/plan/SKILL.md` → `85a5bb1528ac6afabf3cce1741093fb2e5436585`, 기록의 값과 같다. 통과
  - 기록의 (가) 출력을 읽음 → 끝의 브랜치 `tasks/readme-intro`, 제목 `plan: readme-intro`, 돌리기 전과 뒤의 `git rev-parse main`이 모두 `fbf90696422c93080b39905472ecd054162bd276`. 남아 있는 첫째 시험 저장소에서 `git -C … branch --show-current`, `git -C … log -1 --format=%s tasks/readme-intro`, `git -C … rev-parse main`을 다시 내도 같다. 통과
  - 기록의 (나) 응답 글 전문을 읽음 → `feature/x`가 기본 브랜치도 `tasks/<이름>`도 아니라고 들고 "계획을 `tasks/<이름>` 브랜치에 커밋해도 될까요?"라고 묻는다. 그 자리의 브랜치 `feature/x`, 마지막 커밋 `fbf9069 init`(돌리기 전 그대로), `git status --porcelain` 출력 없음. 둘째 시험 저장소에서 다시 내도 같고 `tasks/` 브랜치가 없다. 통과
- 시험이 이 저장소를 바꾸지 않았다.
  - `git status --porcelain -- . ':!docs/tasks/002-plan-branch/phase-2.md' ':!docs/tasks/RUNLOG.md'` → 출력 없음. 통과
- 완료 조건 1, 2, 3이 그대로 참이다.
  - `grep -c -e '브랜치를 만들거나 바꾸지 않는다' plugins/plate/skills/plan/SKILL.md` → `0`. 통과
  - `grep -c -e 'plan은 브랜치를 바꾸지 않아서' -e '계획의 커밋이 로컬 기본 브랜치에만' plugins/plate/skills/run/SKILL.md` → `0`. 통과
  - `grep -c -e '계획의 커밋이 로컬 기본 브랜치에만' docs/ARCHITECTURE.md README.md` → `docs/ARCHITECTURE.md:0`, `README.md:0`. 통과
- 테스트가 모두 통과한다(완료 조건 5).
  - `python3 -m unittest discover -s tests` → `Ran 207 tests`, `OK`. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 207 tests in 18.322s`, `OK`. 통과

**남은 것**
- (나)는 물음까지만 봤다. 승인한 뒤 `feature/x`에서 `tasks/<이름>`을 만드는 갈래와 거절해 끝나는 갈래는 돌리지 않았다 → 통과 조건(완료 조건 4의 (나))은 첫 턴의 물음과 그 자리의 상태만 보므로 걸리지 않는다. 하네스에서 걸린 것

**실패**
- 없음

**하네스에서 걸린 것**
- 남은 것: (나)의 승인 뒤 `feature/x`에서 `tasks/<이름>`을 만드는 갈래와 거절해 끝나는 갈래는 헤드리스로 돌리지 않았다. task 머리의 `돌리지 않음` 줄에 이 두 갈래는 이름으로 들어 있지 않고, 결정의 "두 장면만 돌린다"가 덮는다

**판정**: 통과
