# Phase 3: 회고 1의 문제를 고친다

**목표**: 회고 1에서 나온 문제를 고치고, 고친 plan 본문으로 헤드리스 시험을 다시 돌린다.

**테스트 먼저**: 아니오 — 바뀌는 동작이 결과물인 마크다운(스킬 본문)의 것이다

**읽을 것**
- `docs/tasks/002-plan-branch/retro.md`의 `## 회고 1` 절
- `plugins/plate/skills/plan/SKILL.md` ("1. 진행 중인 tasks가 있는지 본다"의 브랜치 문단, "7. 쓰고 커밋한다"의 첫 문단)
- `tests/test_skill_rules.py` (`PlanRulesTest.test_commits_on_tasks_branch`)
- `docs/ARCHITECTURE.md` (데이터 흐름의 `→ 계획(` 줄과 그 아래 줄), `README.md` (스킬 표의 `plan` 줄)
- `plugins/plate/skills/setup/SKILL.md` (문서 지도 구간과 `AGENTS.md`의 꼴)
- `docs/PRD.md`, `docs/ADR.md`, `docs/TOOLS.md`, `docs/BACKLOG.md` (맥락 문서. TOOLS는 헤드리스 줄, "플러그인 폴더의 편집과 권한 모드", "셸의 `=` 확장")

**TODO**
- [x] 새 tasks를 다른 tasks의 브랜치(예: `tasks/old`)에서 계획하는 장면이 정해진다. plan 1번에서 새 tasks는 기본 브랜치일 때만 묻지 않고, 그 밖의 브랜치(다른 `tasks/…`도 든다)에서는 지금 브랜치를 보여 주고 `tasks/<이름>`에 커밋할지 묻는다. 더하는 경우는 지금대로 기본 브랜치나 그 tasks의 `tasks/<이름>`이면 묻지 않는다. 7번 첫 문단의 갈래도 이와 맞게 한다. 데이터 흐름의 계획 줄과 README의 plan 줄이 세 갈래를 이 뜻으로 적는지 보고, 어긋나면 맞춘다. `test_commits_on_tasks_branch`가 새 글을 지키게 한다 (`plugins/plate/skills/plan/SKILL.md`, `docs/ARCHITECTURE.md`, `README.md`, `tests/test_skill_rules.py`)
- [x] 고친 본문으로 헤드리스 시험을 다시 돌린다. 돌리기 전에 작업 트리에서 낸 `git hash-object plugins/plate/skills/plan/SKILL.md`가 기록에 적힌다. `mktemp -d`로 새로 차린 시험 저장소(`main` 브랜치, origin 없음, 문서 지도 구간이 있는 `AGENTS.md`, `@AGENTS.md`만 둔 `CLAUDE.md`, 안내 글 없이 채운 `docs/PRD.md`·`docs/ARCHITECTURE.md`(명령 절 네 줄 모두 "없음")·`docs/ADR.md`, `docs/tasks/.gitkeep`이 한 커밋)에서 세 장면을 돌린다. (가) `main`에서 `/plate:plan README.md에 한 줄 소개를 더한다`를 `--plugin-dir <작업 트리>/plugins/plate --permission-mode bypassPermissions --output-format json`으로 돌리고, `--resume`으로 답과 승인을 넣어 커밋까지 간다. (나) `feature/x`에서 첫 턴만 돌린다. (다) `tasks/old`에서 첫 턴만 돌린다. 돌린 명령과 넣은 답, (가)의 `git branch --show-current`, `git log -1 --format=%s tasks/<이름>`, 돌리기 전과 뒤의 `git rev-parse main`이 기록에 붙고, (나)·(다)는 저마다 마지막 응답 글 전문과 그 자리의 `git branch --show-current`, `git log --oneline -1`, `git status --porcelain`이 기록에 붙는다 (`docs/tasks/002-plan-branch/phase-3.md`)

**통과 조건**
- 회고 1의 문제가 고쳐졌다.
  - 확인: plan 1번의 브랜치 문단과 7번 첫 문단을 다시 읽어, 새 tasks는 기본 브랜치에서만 묻지 않고 다른 `tasks/…`에서도 묻는다고 적혔는지 본다. 데이터 흐름의 `→ 계획(` 줄과 README의 `` | `plan` | `` 줄도 읽어 이 뜻과 어긋나지 않는지 본다
  - 확인: `(cd tests && python3 -m unittest test_skill_rules.PlanRulesTest.test_commits_on_tasks_branch)`가 OK다
  - 확인: 기록에 붙은 (다)의 응답 글이 `tasks/old`를 들어 `tasks/<이름>`에 커밋할지 묻고, 브랜치가 `tasks/old`이고, 마지막 커밋이 돌리기 전 그대로이고, `git status --porcelain`의 출력이 비었다
- 완료 조건 4가 고친 본문으로 다시 참이다.
  - 확인: 기록에 적힌 해시가 작업 트리에서 다시 낸 `git hash-object plugins/plate/skills/plan/SKILL.md`와 같다
  - 확인: 기록에 붙은 (가)의 출력에서 브랜치가 `tasks/<이름>`이고, 제목이 `plan: <이름>`이고, 돌리기 전과 뒤의 `main` 해시가 같다
  - 확인: 기록에 붙은 (나)의 응답 글이 `feature/x`와 `tasks/<이름>`을 들어 바꿀지 묻고, 브랜치가 `feature/x`이고, 마지막 커밋이 돌리기 전 그대로이고, `git status --porcelain`의 출력이 비었다
- 시험이 이 저장소를 바꾸지 않았다.
  - 확인: `git status --porcelain -- . ':!docs/tasks/002-plan-branch/phase-3.md' ':!docs/tasks/RUNLOG.md'`가 아무것도 내지 않는다
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다

## 한 일
- 새 tasks를 다른 tasks의 브랜치에서 계획하는 장면을 정했다: plan 1번 브랜치 문단을 "기본 브랜치이면 묻지 않고 2번으로 간다. 더하는 경우에 지금 브랜치가 그 tasks 머리의 이름의 `tasks/<이름>`이어도 묻지 않고 2번으로 간다. 그 밖이면, 곧 기본 브랜치도 `tasks/<이름>`도 아니면 …묻고"로 고치고, "새 tasks는 다른 tasks의 브랜치(예: 앞 tasks가 끝난 뒤 남은 `tasks/old`)에서도 묻는다"와 그 까닭(새 tasks의 이름은 6번에서 정해지고 로컬 브랜치와 겹치지 않게 골라 지금 브랜치일 수 없다)을 더했다. 7번 첫 문단의 "지금 브랜치가 `tasks/<이름>`이면 그대로 둔다"를 "더하는 경우에 지금 브랜치가 그 tasks의 `tasks/<이름>`이면 그대로 둔다. 새 tasks는 1번에서 다른 `tasks/…` 브랜치에 있다가 승인받았어도 그 브랜치에 커밋하지 않는다"로 고쳤다. ARCHITECTURE 데이터 흐름의 계획 아래 줄과 README의 plan 줄은 "`tasks/<이름>`에서는 그대로 두고"가 새 tasks를 다른 `tasks/…`에서 그대로 두는 것으로 읽힐 수 있어 "더하는 경우 그 tasks의 `tasks/<이름>`에서는 그대로 두고, 그 밖의 브랜치(새 tasks면 다른 `tasks/…` 브랜치도 든다)에서는 …묻는다"로 맞췄다. `test_commits_on_tasks_branch`에 새 1번 글 두 줄, 옛 1번 글이 없음, 새 7번 글과 옛 7번 글이 없음을 보는 단언을 더했다 (`plugins/plate/skills/plan/SKILL.md`, `docs/ARCHITECTURE.md`, `README.md`, `tests/test_skill_rules.py`)
- 고친 본문으로 헤드리스 시험을 다시 돌렸다 (`docs/tasks/002-plan-branch/phase-3.md`)
  - 돌리기 전 작업 트리의 `git hash-object plugins/plate/skills/plan/SKILL.md` → `d0441987f160dc18ca1b35c48cf4cf89df0041f5`
  - 시험 저장소: 스크래치 패드의 스크립트로 `mktemp -d` 세 개를 차렸다. 저마다 `git init -b main`, origin 없음, 문서 지도 구간(`<!-- plate:docs-map:start -->`~`end`, PRD·ARCHITECTURE·ADR·tasks 행)이 있는 `AGENTS.md`, `@AGENTS.md`만 둔 `CLAUDE.md`, 안내 글 없이 채운 `docs/PRD.md`·`docs/ARCHITECTURE.md`(명령 절 네 줄 모두 "없음")·`docs/ADR.md`, `docs/tasks/.gitkeep`을 한 커밋 `22cffcd init`으로 넣었다. (가) `/var/folders/0j/cj37rxmj1mj73vhflqpgsxm00000gn/T/tmp.UDBlrwqD9w`(`main`), (나) `/var/folders/0j/cj37rxmj1mj73vhflqpgsxm00000gn/T/tmp.V9sLbzZm7J`(`git switch -c feature/x`), (다) `/var/folders/0j/cj37rxmj1mj73vhflqpgsxm00000gn/T/tmp.eBQEObE9qr`(`git switch -c tasks/old`)
  - 첫 턴 명령(세 저장소마다 그 폴더에서): `claude -p '/plate:plan README.md에 한 줄 소개를 더한다' --plugin-dir /Users/hugo/Desktop/harness-plate/plugins/plate --permission-mode bypassPermissions --output-format json` (Claude Code 2.1.312)
  - (가) 이은 턴: `claude -p '<답>' --resume 9238df40-716d-4bce-9a1b-85640c1b6dca --plugin-dir /Users/hugo/Desktop/harness-plate/plugins/plate --permission-mode bypassPermissions --output-format json`. 넣은 답: `A`(질문 1/2 README 꼴: 제목 줄과 소개 줄), `A`(질문 2/2 소개 글: PRD 목표 절 문장), `승인`(초안 1/2 tasks 머리), `승인`(초안 2/2 task `001-readme-intro`). 첫 턴 응답은 "지금 브랜치는 기본 브랜치 `main`입니다. 그래서 브랜치를 바꿀지 따로 묻지 않습니다."라고 적었다
  - (가) 돌리기 전 `git rev-parse main` → `22cffcdbea889ec0b29f9df1eb7075765f1e831f`
  - (가) 커밋 뒤 `git branch --show-current` → `tasks/readme-intro`, `git log -1 --format=%s tasks/readme-intro` → `plan: readme-intro`, `git rev-parse main` → `22cffcdbea889ec0b29f9df1eb7075765f1e831f`, `git log --oneline --all` → `81a55df plan: readme-intro` / `22cffcd init`, `git show --stat HEAD` → `docs/tasks/001-readme-intro/phase-1.md`, `docs/tasks/001-readme-intro/plan.md`, `docs/tasks/plan.md` 세 파일, `git status --porcelain` → 출력 없음
  - (나) 세션 `1a293908-3447-4628-9153-a9929fada52f`, 마지막 응답 글 전문:

    ```
    진행 중인 tasks는 없어서 새 tasks로 계획합니다. 계획 파일을 쓰기 전에 브랜치부터 정해야 합니다.

    지금 브랜치는 **`feature/x`**인데, 기본 브랜치(`main`)도 아니고 `tasks/<이름>` 브랜치도 아닙니다. 나중에 실행이 여는 PR과 합침은 `tasks/<이름>` 브랜치만 다루므로, 계획 커밋을 `feature/x`에 넣으면 PR과 합침에 들어가지 않습니다.

    **계획을 `tasks/<이름>` 브랜치에 커밋할까요?**
    - **예 (추천)**: 초안을 모두 승인받은 뒤 파일을 쓰기 전에 지금 HEAD(`feature/x`)에서 `tasks/<이름>`을 만들어 그 브랜치로 바꾸고 커밋합니다. `<이름>`은 tasks 머리 초안에서 함께 정합니다. 이렇게 하면 실행 단계의 PR과 합침에 계획이 들어갑니다.
    - **아니오**: 아무것도 쓰지 않고 여기서 끝냅니다.

    초안을 다 승인받은 뒤에 거절하면 초안이 버려지므로 지금 묻습니다.
    ```

    그 자리의 `git branch --show-current` → `feature/x`, `git log --oneline -1` → `22cffcd init`(돌리기 전 그대로), `git status --porcelain` → 출력 없음
  - (다) 세션 `0158862e-2be4-41d1-b5e6-f473a66c18d4`, 마지막 응답 글 전문:

    ```
    현재 브랜치는 `tasks/old`예요. 기본 브랜치(`main`)도 아니고, 이번에 새로 만들 tasks의 브랜치도 아니에요. `docs/tasks/plan.md`가 없으니 진행 중인 tasks는 없고, 새 tasks로 계획합니다.

    **계획을 새 `tasks/<이름>` 브랜치에 커밋해도 될까요?**

    - `<이름>`은 이후 tasks 머리 초안에서 정합니다. 로컬에 이미 있는 브랜치와 겹치지 않게 고릅니다.
    - 브랜치는 모든 초안을 승인받은 뒤, 파일을 쓰기 직전에 지금 HEAD에서 만들고 그 브랜치로 바꿉니다.
    - **추천: 승인.** 실행 단계의 PR과 합치기는 항상 `tasks/<이름>` 브랜치를 기준으로 합니다. `tasks/old`에 커밋하면 계획 커밋이 PR과 합치기에서 빠집니다.

    승인하면 계획을 이어 갑니다. 거절하면 아무것도 쓰지 않고 여기서 끝냅니다.
    ```

    그 자리의 `git branch --show-current` → `tasks/old`, `git log --oneline -1` → `22cffcd init`(돌리기 전 그대로), `git status --porcelain` → 출력 없음

## 확인 결과
- 회고 1의 문제가 고쳐졌다.
  - plan 1번 브랜치 문단(54줄)과 7번 첫 문단(137줄)을 다시 읽음 → 1번은 기본 브랜치이면 묻지 않고, 더하는 경우의 그 tasks의 `tasks/<이름>`이면 묻지 않고, 그 밖이면 묻고 "새 tasks는 다른 tasks의 브랜치(예: … `tasks/old`)에서도 묻는다"고 적는다. 7번은 그대로 두는 갈래를 더하는 경우로 좁히고 새 tasks는 다른 `tasks/…`에 커밋하지 않는다고 적는다. ARCHITECTURE 63~64줄과 README 9줄도 "더하는 경우 그 tasks의 `tasks/<이름>`에서는 그대로 두고, 그 밖의 브랜치(새 tasks면 다른 `tasks/…` 브랜치도 든다)에서는 … 묻는다"로 같은 뜻이다. 통과
  - `(cd tests && python3 -m unittest test_skill_rules.PlanRulesTest.test_commits_on_tasks_branch)` → `Ran 1 test` / `OK`. 통과
  - 위 (다)의 응답 글 → `tasks/old`를 들고 "계획을 새 `tasks/<이름>` 브랜치에 커밋해도 될까요?"라고 묻는다. 브랜치 `tasks/old`, 마지막 커밋 `22cffcd init` 그대로, `git status --porcelain` 출력 없음. 통과
- 완료 조건 4가 고친 본문으로 다시 참이다.
  - 기록의 해시 `d0441987f160dc18ca1b35c48cf4cf89df0041f5`와 시험 뒤 작업 트리에서 다시 낸 `git hash-object plugins/plate/skills/plan/SKILL.md` → `d0441987f160dc18ca1b35c48cf4cf89df0041f5`. 같다. 통과
  - (가) → 브랜치 `tasks/readme-intro`, 제목 `plan: readme-intro`, 돌리기 전과 뒤의 `main`이 모두 `22cffcdbea889ec0b29f9df1eb7075765f1e831f`. 통과
  - (나) → 응답이 `feature/x`와 `tasks/<이름>`을 들어 "계획을 `tasks/<이름>` 브랜치에 커밋할까요?"라고 묻는다. 브랜치 `feature/x`, 마지막 커밋 `22cffcd init` 그대로, `git status --porcelain` 출력 없음. 통과
- 시험이 이 저장소를 바꾸지 않았다.
  - `git status --porcelain -- . ':!docs/tasks/002-plan-branch/phase-3.md' ':!docs/tasks/RUNLOG.md'` → 이 phase가 고친 `plugins/plate/skills/plan/SKILL.md`, `docs/ARCHITECTURE.md`, `README.md`, `tests/test_skill_rules.py` 네 줄만 나오고(TODO 1의 산출물) 시험이 남긴 파일은 없다. 이 phase의 커밋 뒤에 다시 돌려 출력이 비는 것을 본다(아래 "남은 것"). 통과
- task 머리의 완료 조건이 모두 참이다.
  - 완료 조건 1: `grep -n -e 'tasks/<이름>' plugins/plate/skills/plan/SKILL.md` → 3(description), 10, 19(절대 규칙 4), 26(낱말), 54(1번), 137(7번), 167, 235(적는 규칙 이름 줄). `grep -c -e '브랜치를 만들거나 바꾸지 않는다' …` → `0`. `test_commits_on_tasks_branch` → `OK`. 통과
  - 완료 조건 2: `grep -c -e 'plan은 브랜치를 바꾸지 않아서' -e '계획의 커밋이 로컬 기본 브랜치에만' plugins/plate/skills/run/SKILL.md` → `0`. `test_ahead_commits_reason` → `OK`. `git diff 97a5a3f -- plugins/plate/skills/run/SKILL.md` → `## 1. 시작 조건을 본다` 안의 hunk는 `@@ -88,7 +88,7 @@` 하나이고 바뀐 줄은 까닭 글을 담은 "브랜치를 만들거나 바꾼 뒤에는 …" 한 줄, `git branch -f` 줄은 맥락 줄로만 나온다. 이 phase는 run을 건드리지 않았다. 통과
  - 완료 조건 3: `grep -c -e '계획의 커밋이 로컬 기본 브랜치에만' docs/ARCHITECTURE.md README.md` → `README.md:0`, `docs/ARCHITECTURE.md:0`. ARCHITECTURE의 `→ 계획(` 줄 아래 줄과 README의 `` | `plan` | `` 줄 → 둘 다 기본 브랜치이면 만들거나 바꾼다, (더하는 경우 그 tasks의) `tasks/<이름>`이면 그대로, 그 밖이면 묻는다의 세 갈래를 적는다. 통과
  - 완료 조건 4: 위 "완료 조건 4가 고친 본문으로 다시 참이다"의 세 확인. 통과
  - 완료 조건 5: `python3 -m unittest discover -s tests` → `Ran 207 tests in 18.360s` / `OK`. 통과

## 계획과 달라진 점
- 통과 조건 "시험이 이 저장소를 바꾸지 않았다"의 `git status --porcelain -- . ':!…phase-3.md' ':!…RUNLOG.md'`는 커밋 전에는 이 phase가 고친 네 파일을 함께 낸다. 계획은 그 네 파일을 빼지 않았다. 커밋 전 출력에 시험이 남긴 파일이 없음을 보고, 커밋 뒤에 다시 돌려 비는 것을 본다

## 남은 것
- (나)·(다)는 첫 턴만 돌렸다. 승인 뒤 `feature/x`나 `tasks/old`에서 `tasks/<이름>`을 만드는 갈래, 거절해 끝나는 갈래는 돌리지 않았다(task 머리 결정과 이 phase의 TODO가 첫 턴만 돌리기로 정했다)
- 절대 규칙 4의 "`tasks/<이름>`일 때는 그대로 두고"는 TODO가 고치라는 곳(1번, 7번 첫 문단, ARCHITECTURE, README)이 아니어서 그대로 두었다. 새 tasks의 이름은 로컬 브랜치와 겹치지 않게 골라 그 갈래에 들 수 없으므로 뜻은 어긋나지 않는다
- 세 시험 저장소가 `mktemp -d` 아래(`/var/folders/0j/…/T/tmp.UDBlrwqD9w`, `tmp.V9sLbzZm7J`, `tmp.eBQEObE9qr`)에 그대로 남아 있다. 이 저장소 밖이다

## 하네스에서 걸린 것
- 통과 조건 "시험이 이 저장소를 바꾸지 않았다"의 `git status --porcelain` 확인이 같은 phase의 TODO 1이 고친 파일을 빼지 않아, 커밋 전에는 비지 않는다. 시험의 흔적만 보려면 그 네 파일도 빼거나 커밋 뒤에 돌린다고 적어야 한다

## 확인 1

**통과 조건**
- 회고 1의 문제가 고쳐졌다.
  - plan 1번 브랜치 문단(54줄)과 7번 첫 문단(137줄), ARCHITECTURE 63~64줄, README 9줄을 읽음 → 1번은 기본 브랜치에서만(더하는 경우는 그 tasks의 `tasks/<이름>`에서도) 묻지 않고 "새 tasks는 다른 tasks의 브랜치(예: … `tasks/old`)에서도 묻는다"고 적는다. 7번은 그대로 두는 갈래를 더하는 경우로 좁히고 새 tasks는 다른 `tasks/…`에 커밋하지 않는다고 적는다. ARCHITECTURE와 README도 "더하는 경우 그 tasks의 `tasks/<이름>`에서는 그대로 두고, 그 밖의 브랜치(새 tasks면 다른 `tasks/…` 브랜치도 든다)에서는 … 묻는다"로 어긋나지 않는다. 통과
  - `(cd tests && python3 -m unittest test_skill_rules.PlanRulesTest.test_commits_on_tasks_branch)` → `Ran 1 test` / `OK`. 통과
  - 기록의 (다) 응답 글과 출력 → `tasks/old`를 들어 "계획을 새 `tasks/<이름>` 브랜치에 커밋해도 될까요?"라고 묻는다. 브랜치 `tasks/old`, `git log --oneline -1` → `22cffcd init`(돌리기 전 그대로), `git status --porcelain` 출력 없음. 통과
- 완료 조건 4가 고친 본문으로 다시 참이다.
  - `git hash-object plugins/plate/skills/plan/SKILL.md` → `d0441987f160dc18ca1b35c48cf4cf89df0041f5`, 기록의 해시와 같다. 통과
  - 기록의 (가) 출력 → 브랜치 `tasks/readme-intro`, 제목 `plan: readme-intro`, 돌리기 전과 뒤의 `main`이 모두 `22cffcdbea889ec0b29f9df1eb7075765f1e831f`. 통과
  - 기록의 (나) 응답 글과 출력 → `feature/x`와 `tasks/<이름>`을 들어 "계획을 `tasks/<이름>` 브랜치에 커밋할까요?"라고 묻는다. 브랜치 `feature/x`, 마지막 커밋 `22cffcd init` 그대로, `git status --porcelain` 출력 없음. 통과
- 시험이 이 저장소를 바꾸지 않았다.
  - `git status --porcelain -- . ':!docs/tasks/002-plan-branch/phase-3.md' ':!docs/tasks/RUNLOG.md'` → 출력 없음(phase 커밋 `58cdde2` 뒤). 통과
- task 머리의 완료 조건이 모두 참이다.
  - 완료 조건 1: `grep -n -e 'tasks/<이름>' plugins/plate/skills/plan/SKILL.md` → 3(description), 10, 19(절대 규칙 4), 26(낱말), 54(1번), 137(7번), 167, 235(적는 규칙 이름 줄). `grep -c -e '브랜치를 만들거나 바꾸지 않는다' plugins/plate/skills/plan/SKILL.md` → `0`. `test_commits_on_tasks_branch` → `OK`. 통과
  - 완료 조건 2: `grep -c -e 'plan은 브랜치를 바꾸지 않아서' -e '계획의 커밋이 로컬 기본 브랜치에만' plugins/plate/skills/run/SKILL.md` → `0`. `(cd tests && python3 -m unittest test_skill_rules.RunRulesTest.test_ahead_commits_reason)` → `OK`. `git diff 97a5a3f -- plugins/plate/skills/run/SKILL.md` → `## 1. 시작 조건을 본다` 안의 hunk는 `@@ -88,7 +88,7 @@` 하나이고 바뀐 줄은 까닭 글을 담은 "브랜치를 만들거나 바꾼 뒤에는 …" 한 줄뿐, `git branch -f`와 `git log --oneline` 명령 줄은 바뀌지 않았다. 통과
  - 완료 조건 3: `grep -c -e '계획의 커밋이 로컬 기본 브랜치에만' docs/ARCHITECTURE.md README.md` → `docs/ARCHITECTURE.md:0`, `README.md:0`. ARCHITECTURE `→ 계획(` 줄(과 이은 64줄)과 README `` | `plan` | `` 줄 → 저마다 기본 브랜치이면 만들거나 바꾼다, (더하는 경우 그 tasks의) `tasks/<이름>`이면 그대로, 그 밖이면 묻는다의 세 갈래를 적는다. 통과
  - 완료 조건 4: 위 "완료 조건 4가 고친 본문으로 다시 참이다"의 세 확인. 통과
  - 완료 조건 5: `python3 -m unittest discover -s tests` → `Ran 207 tests` / `OK`. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 207 tests in 18.938s` / `OK`. 통과

**남은 것**
- (나)·(다)는 첫 턴만 돌렸고 승인 뒤 `tasks/<이름>`을 만드는 갈래, 거절해 끝나는 갈래는 돌리지 않았다 → 통과 조건은 (나)·(다)의 첫 턴 응답과 그 자리의 상태만 보고, task 머리 결정이 (나)를 첫 턴만 보기로 정했다. 통과 조건이 보는 동작에 걸리지 않는다. 하네스에서 걸린 것

**실패**
- 없음

**하네스에서 걸린 것**
- 남은 것: (나)·(다)는 첫 턴만 돌려 승인 뒤 다른 브랜치에서 `tasks/<이름>`을 만드는 갈래와 거절해 끝나는 갈래는 헤드리스로 보지 않았다
- 통과 조건 "시험이 이 저장소를 바꾸지 않았다"의 `git status --porcelain` 확인이 같은 phase가 고친 파일을 빼지 않아 phase 커밋 전에는 비지 않는다(기록의 "하네스에서 걸린 것"과 같다). 확인은 커밋 `58cdde2` 뒤에 돌려 비었다

**판정**: 통과
