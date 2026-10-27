# Phase 2: 임시 복제본에서 두 장면으로 돌린다

**목표**: cleanup 스킬을 헤드리스로 돌려 장면 1(만들지 않음)과 장면 2(만든다)의 결과를 `docs/TOOLS.md`에 남긴다.

**테스트 먼저**: 아니오 — 스킬을 돌려 보고 `.md`에 적는다

**읽을 것**
- `plugins/plate/skills/cleanup/SKILL.md` (phase 1이 쓴 본문)
- `docs/TOOLS.md`의 "Claude Code" 절 (헤드리스 명령의 꼴, `--resume`, 허용 목록, 세션이 폴더에 묶이는 것, 막힌 명령 하나마다 기다리는 시간)

**TODO**
- [x] task 머리 결정의 "확인용 실행"대로 임시 복제본에서 첫 턴을 백그라운드로 돌리고, 묻는 자리에서 멈춘 것과 그 시점의 복제본 상태(`git show --name-only HEAD`, `git status --short`, 보고서의 여섯 기준 절, 지도 행)를 본다 (임시 폴더)
- [x] 장면 2를 `--resume <id> --fork-session`과 "만든다, 1번"으로 잇고, 기록에서 `plate:plan` 스킬 호출과 그 요청 글에 보고서 경로가 든 것을 본다. 복제본의 `git status --short`가 비었는지도 본다 (임시 폴더)
- [x] 장면 1을 원래 세션 id와 "만들지 않는다"로 잇고, 보고서가 "미룸" 표시와 함께 커밋되고 `docs/tasks/plan.md`가 생기지 않은 것을 본다 (임시 폴더)
- [x] 결과가 스킬의 결함을 보이면 `plugins/plate/skills/cleanup/SKILL.md`를 고치고 세 TODO를 새 복제본에서 다시 돈다 (`plugins/plate/skills/cleanup/SKILL.md`)
- [x] `docs/TOOLS.md`의 "Claude Code" 절 끝에 새 절이 더해진다. Claude Code 버전, 복제본의 main 커밋, 첫 턴 시각, 세션 id 둘, 1라운드와 2라운드에 띄운 에이전트 수, 장면마다의 결과(장면 1: 커밋된 파일 목록, 여섯 기준 절, 미룸 커밋. 장면 2: `plate:plan` 호출 줄), 걸린 시간, 막힌 명령을 적는다. 임시 폴더의 기록 경로도 적되 지워질 수 있다고 밝힌다 (`docs/TOOLS.md`)
- [x] `docs/TOOLS.md`의 "Claude Code" 절 첫 문단의 판정 버전 목록에 이 tasks의 시험 버전과 날짜가 더해진다 (`docs/TOOLS.md`)

**통과 조건**
- 두 장면의 결과가 남았다(완료 조건 2)
  - 확인: `docs/TOOLS.md`의 새 절을 읽어 두 장면이 저마다 Claude Code 버전, 돌린 시각, 세션 id, 결과를 적었다. 장면 1은 커밋된 파일 목록(보고서와 `AGENTS.md`뿐)과 보고서의 여섯 기준 절, 장면 2는 `plate:plan` 호출 줄이다. 하나라도 없으면 실패
  - 확인: 그 절의 첫 턴 시각이 `git log -1 --format=%cI -- plugins/plate/skills/cleanup/SKILL.md`보다 늦다
  - 확인: 그 절의 에이전트 수가 1라운드 6, 2라운드 6이다
- 스킬 본문이 여전히 맞다(완료 조건 1)
  - 확인: `head -3 plugins/plate/skills/cleanup/SKILL.md`에 `name: cleanup`이 있고, `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
  - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`

## 한 일
- task 머리 결정의 "확인용 실행"대로 첫 턴을 돌렸다: `mktemp -d`(`/var/folders/0j/cj37rxmj1mj73vhflqpgsxm00000gn/T/tmp.Qy3TXHzAsG`) 아래 `repo`에 main(`a3c1158`)을 복제하고 `claude -p "/plate:cleanup"`을 허용 목록과 옵션을 결정대로 주어 백그라운드로 돌렸다(15:39:37~15:56:47, 세션 `56d46cfa-e292-4f88-b6ed-f0d739b8951c`). 1라운드 6, 2라운드 6의 에이전트를 띄우고 커밋 `fd899a0 cleanup: 2026-10-27`(`AGENTS.md`, `docs/cleanup/2026-10-27.md`) 뒤 남은 발견 33개를 번호로 고르라며 멈췄다. `git status --short`는 비었고, 보고서에 여섯 기준 절이 차례대로 있고, 지도 행이 `docs/tasks/` 행 앞에 있었다 (임시 폴더)
- 장면 2: `--resume 56d46cfa-… --fork-session "만든다, 보안-1"`로 이었다(세션 `ce76bda6-d806-4368-a516-f7635a15461d`, 30초). 기록에 `plate:plan` 스킬 호출이 있고 그 `args`에 `docs/cleanup/2026-10-27.md`와 `보안-1`이 들었다. plan은 진행 중인 issue-sweep에 더할지 묻고 멈췄다. 그 앞에 미룸 커밋 `52443f2`가 들어갔고 `git status --short`는 비었다 (임시 폴더)
- 장면 1: 복제본을 `git reset --hard fd899a0`으로 첫 턴이 멈춘 상태로 돌린 뒤 `--resume 56d46cfa-… "만들지 않는다"`로 이었다(32초). 커밋 `f390dce cleanup: 2026-10-27 미룸`(보고서 하나)이 들어갔고 33개가 모두 `미룸`, `plate:plan` 호출 없음, `docs/tasks/plan.md` 블롭은 첫 턴 전과 같은 `63911a9`였다 (임시 폴더)
- 스킬의 결함: 세 턴의 결과가 SKILL.md의 절차대로였다. 고칠 결함을 찾지 못해 `plugins/plate/skills/cleanup/SKILL.md`는 고치지 않았고 다시 돌지 않았다
- `docs/TOOLS.md`의 "Claude Code" 절 끝(`## Codex` 앞)에 "cleanup 스킬을 두 장면으로 돌려 본 것" 절을 더했다. 버전 2.1.311, 복제본 main `a3c1158`, 첫 턴 시각, 세션 id 둘, 에이전트 수(1라운드 6, 2라운드 6), 장면마다의 결과, 걸린 시간, 막힌 명령, 임시 폴더의 기록 경로(지워질 수 있음)를 적었다 (`docs/TOOLS.md`)
- 첫 문단의 판정 버전 목록에 "tasks cleanup의 시험은 2.1.311(2026-10-27)"을 더했다 (`docs/TOOLS.md`)

## 확인 결과
- 두 장면의 결과가 남았다(완료 조건 2)
  - `docs/TOOLS.md` 237줄부터의 새 절을 읽음 → 버전 2.1.311(절 머리), 첫 턴·장면 2·장면 1의 시각, 세션 id `56d46cfa-…`(첫 턴·장면 1)와 `ce76bda6-…`(장면 2), 장면 1의 커밋된 파일(`AGENTS.md`, `docs/cleanup/2026-10-27.md`)과 여섯 기준 절, 장면 2의 `plate:plan` 호출 줄이 있다. 통과
  - 첫 턴 시각 `2026-10-27T15:39:37+09:00` > `git log -1 --format=%cI -- plugins/plate/skills/cleanup/SKILL.md` → `2026-10-27T15:37:12+09:00`. 통과
  - 새 절의 에이전트 수 → 1라운드 6, 2라운드 6. 통과
- 스킬 본문이 여전히 맞다(완료 조건 1)
  - `head -3 plugins/plate/skills/cleanup/SKILL.md` → `name: cleanup` 있음. `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
  - `python3 -m unittest discover -s tests` → 마지막 줄 `OK`. 통과

## 계획과 달라진 점
- 결정은 장면 2를 먼저 이으면 "plan은 승인 전에 아무것도 쓰지 않으므로 폴더가 바뀌지 않는다"고 봤으나, 스킬 7번이 plan을 부르기 전에 미룸 커밋(`52443f2`)을 넣어 HEAD가 옮겨졌다. 장면 1이 첫 턴이 멈춘 상태에서 시작하도록 장면 1 전에 임시 복제본을 `git reset --hard fd899a0`으로 돌렸다. 복제본에서만 한 일이고 task 머리와 스킬은 바꾸지 않았다.
- TODO 2의 "만든다, 1번"은 발견 번호가 `보안-1` 꼴이라 "만든다, 보안-1"로 보냈다.
- TODO 3의 "`docs/tasks/plan.md`가 생기지 않은 것"은 복제한 main에 진행 중인 tasks issue-sweep의 `docs/tasks/plan.md`가 이미 있어, 그 블롭이 첫 턴 전과 같은지로 봤다. 같은 까닭으로 장면 2의 plan은 진행 중인 tasks에 더할지 묻는 자리에서 멈췄다.

## 남은 것
- 허용 목록에 `git ls-files`, `git rev-parse`, 파이프·`;`를 이은 Bash, `git -C … show`가 맞지 않아 메인과 서브에이전트의 명령이 막혔다. 일부 2라운드 에이전트는 git 이력의 지난 tasks 기록을 다시 읽지 못하고 작업 트리로만 판정했다. 보고서에도 적혔다. 스킬 본문의 결함이 아니라 시험의 허용 목록 탓으로 봤다.
- origin이 로컬 경로라 열린 GitHub 이슈 확인은 측정 못함이었다. GitHub origin에서 `gh issue list`가 도는 장면은 돌리지 않았다.
- 첫 턴과 장면 1의 답글이 영어였다(보고서는 한국어). 까닭은 확인하지 않았다.
- 같은 날 다시 불러 `-2` 번호가 붙는 것, 지난 보고서와 견주는 것은 돌리지 않았다.

## 하네스에서 걸린 것
- 계획의 결정 "plan은 승인 전에 아무것도 쓰지 않으므로 폴더가 바뀌지 않는다"가 스킬 7번의 차례(미룸 커밋 뒤 plan 호출, phase 1이 정함)와 맞지 않아 복제본을 되돌려야 했다.
- 결정의 허용 목록에 스킬이 쓰는 `git ls-files`가 없어 첫 턴에서 막혔다.
- phase 스킬의 1번은 다른 phase의 파일을 읽지 않는다고 하는데, 시작할 때 `done-phase-1.md`를 읽었다. 그 내용으로 바꾼 것은 없다.
