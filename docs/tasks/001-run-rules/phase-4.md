# Phase 4: 회고 1의 문제를 고친다

**목표**: 회고 1에서 나온 문제를 모두 고친다.

**테스트 먼저**: 아니오 — 고칠 문제가 `.md`(스킬 본문과 문서)만 고치고 코드 파일의 동작을 바꾸지 않는다

**읽을 것**
- `docs/tasks/001-run-rules/retro.md`의 `## 회고 1`부터 `## 회고 1`까지의 절
- `plugins/plate/skills/run/SKILL.md`
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/ADR.md`
- `docs/TOOLS.md`
- `docs/BACKLOG.md`
- `README.md`

**TODO**
- [x] run 본문이 #35를 고치며 `docs/TOOLS.md`에 적은 까닭을 "다음 `RUNLOG.md` 커밋에 함께 넣는다"(512행)고 했는데, 그 커밋 자리는 모두 다른 파일을 막는다: 회고·코드 평가·하네스 eval 뒤는 "`RUNLOG.md`만 한 커밋"(167·292·302·501행), phase 통과는 "이 변경과 `RUNLOG.md`만"(154행), 고칠 phase는 "그 파일과 `RUNLOG.md`만"(195행)이다. 어느 쪽을 따르든 한 글을 어기고, 커밋 자리의 글을 따르면 `docs/TOOLS.md`가 커밋되지 않은 채 남아 "고칠지"에서 작업 트리가 깨끗하다는 #44의 목표와 어긋난다. 고칠 동작을 적은 맥락 문서와 README의 줄(`docs/PRD.md` 17행의 핵심 기능 7, `docs/ARCHITECTURE.md` 52행의 run 문단과 69행의 데이터 흐름, `README.md` 10행의 `run` 행)도 고친 뒤 그 동작과 맞게 한다 (`plugins/plate/skills/run/SKILL.md`, `docs/PRD.md`, `docs/ARCHITECTURE.md`, `README.md`)
- [x] 고친 run으로 장면 B를 task 머리의 결정대로 다시 돌려, 회고 뒤와 하네스 eval 뒤에 `RUNLOG.md`만 바꾼 커밋이 있고 "고칠지"에서 `git status --short`가 비었는지 보고, 결과를 `docs/TOOLS.md`의 장면 B 절에 새 시각, 세션 id, 돌릴 때의 run 본문 해시(`git hash-object plugins/plate/skills/run/SKILL.md`)와 함께 더한다 (`docs/TOOLS.md`)

**통과 조건**
- 회고 1의 문제가 모두 고쳐졌다.
  - 확인: TODO에 넣은 문제마다 적힌 곳(run 본문의 `docs/TOOLS.md`를 커밋에 넣는 글과 154·167·195·292·302·501행 근처의 커밋 자리 글)을 다시 읽어 서로 어긋나지 않고, `docs/TOOLS.md`에 적은 까닭이 커밋되지 않은 채 남는 길이 없다. 그 동작을 적은 `docs/PRD.md`, `docs/ARCHITECTURE.md`, `README.md`의 줄을 다시 읽어 고친 동작과 어긋나지 않는다
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다

## 한 일
- run 본문의 `docs/TOOLS.md` 커밋 자리와 맥락 문서·README의 줄을 맞춘다: 사용량이 돌아오지 않은 까닭을 적고 아직 커밋하지 않은 `docs/TOOLS.md`는 `RUNLOG.md`를 넣는 커밋 자리마다 함께 넣는다고 정했다. run 본문의 "`RUNLOG.md`" 절(501행)에 커밋 자리 목록(6번, 8번, "멈춘다", 회고·코드 평가·하네스 eval 뒤, "비운다"의 첫 커밋)과 "`RUNLOG.md`만", "그 파일과 `RUNLOG.md`만"이라고 할 때도 이 파일이 든다는 글을 더하고, 512행의 "다음 `RUNLOG.md` 커밋"에 "(위 문단의 커밋 자리)"를 붙이고, 154·167·195·267·292·302·441행의 커밋 글마다 "(사용량이 돌아오지 않은 까닭을 적고 아직 커밋하지 않은 `docs/TOOLS.md`가 있으면 그것도 넣는다. "`RUNLOG.md`" 절)"을 더했다. `docs/PRD.md` 핵심 기능 7, `docs/ARCHITECTURE.md` 52행 run 문단과 69행 데이터 흐름, `README.md` `run` 행에도 `docs/TOOLS.md`를 함께 넣는다는 글을 더했다 (`plugins/plate/skills/run/SKILL.md`, `docs/PRD.md`, `docs/ARCHITECTURE.md`, `README.md`)
- 고친 run으로 장면 B를 다시 돌린다: `mktemp -d`(`/var/folders/0j/cj37rxmj1mj73vhflqpgsxm00000gn/T/tmp.71t7Bghboj`)에 main을 복제하고 `git remote set-head origin main`을 한 뒤, 지난 장면 B 복제본의 `afc02b9`~`8a0925d`를 가져와 `tasks/scene-b`로 두고, 작업 트리의 `plugins/plate`(run 본문 해시 `b218c23ea8929eaf1189f22d01250c55dabd0cc4`)를 실어 `claude -p "/plate:run" --permission-mode acceptEdits`로 돌렸다(2026-10-27T20:31:28+09:00~20:35:54, 세션 id `78a952b6-2751-4118-89d7-f146a07a4d94`). 회고·코드 평가·하네스 eval 뒤에 `RUNLOG.md`만 바꾼 커밋(`67d07cb`, `9fdeca9`, `aab8846`)이 저마다 있고, 멈춘 자리의 `git status --short`가 비었다. 결과를 `docs/TOOLS.md`의 장면 B 절 끝에 한 항목으로 더했다 (`docs/TOOLS.md`)

## 확인 결과
- 회고 1의 문제가 모두 고쳐졌다.
  - run 본문의 154·167·195·267·292·302·441·501·512행을 다시 읽음(`git diff --word-diff`) → 커밋 자리마다 `docs/TOOLS.md`를 함께 넣는다고 적혀 있고 512행의 "다음 `RUNLOG.md` 커밋(위 문단의 커밋 자리)"과 어긋나지 않는다. 사용량 까닭을 적는 것은 에이전트가 돌아와 `RUNLOG.md` 줄을 더할 때라 그 줄이 들어가는 커밋에 함께 들어간다. `docs/PRD.md` 17행, `docs/ARCHITECTURE.md` 52·69행, `README.md` 10행을 다시 읽음 → 고친 동작과 어긋나지 않는다. 통과
- task 머리의 완료 조건이 모두 참이다.
  - 완료 조건 1: run 본문의 다섯 해결이 그대로 있다(바꾼 것은 커밋 자리 글의 괄호와 "`RUNLOG.md`" 절의 한 문단뿐). `python3 -m unittest discover -s tests` → `Ran 129 tests in 17.092s` / `OK`. `claude plugin validate .` → `✔ Validation passed`. 통과
  - 완료 조건 2: `docs/PRD.md` 핵심 기능 7, `docs/ARCHITECTURE.md` run 문단·데이터 흐름, `README.md` `run` 행, run description을 읽음 → 시작할 때의 권한 물음, `RUNLOG.md`의 커밋 자리, 회고가 계획을 바꾸게 할 때 멈추는 것과 어긋나는 줄이 없다. 통과
  - 완료 조건 3의 첫 확인: `docs/TOOLS.md`의 장면 A~D 절과 새 장면 B 항목을 읽음 → 장면마다 Claude Code 버전, 돌린 시각, 세션 id, 기대한 결과와 본 결과가 있다. 새 장면 B는 세 에이전트 뒤의 `RUNLOG.md`만 바꾼 커밋과 깨끗한 작업 트리가 기대와 같다(고칠 것이 없어 "고칠지"를 묻지 않은 것은 "남은 것"에 적었다). 통과
  - 완료 조건 3의 둘째 확인: 장면 B 절의 해시 `b218c23ea8929eaf1189f22d01250c55dabd0cc4`와 `git hash-object plugins/plate/skills/run/SKILL.md`가 같고, 이 커밋 뒤 `git rev-parse HEAD:plugins/plate/skills/run/SKILL.md`가 같아진다(이 phase는 그 파일을 장면을 돌린 뒤 고치지 않았다). 장면 A 18:40:01, C 19:30:40, D 19:32:30이 `dfb0852`(18:38:03)보다 늦다. `git diff dfb0852 -- plugins/plate/skills/run/SKILL.md` → 바뀐 16줄(8줄 빼고 8줄 더함)이 모두 `docs/TOOLS.md`를 커밋 자리에 넣는 글이다. 통과

## 계획과 달라진 점
- 장면 B의 작은 tasks를 새로 쓰지 않고 지난 장면 B 복제본의 차린 커밋 넷을 그대로 가져왔다. 차림이 같아야 지난 결과와 견줄 수 있어서다

## 남은 것
- 이번 장면 B에서는 회고·코드 평가·하네스 eval이 모두 고칠 것을 내지 않아 run이 "고칠지"를 묻지 않고 "비운다"로 넘어갔다. 그래서 "고칠지를 묻고 멈춘 자리"는 보지 못했고, 그 자리에 해당하는 `aab8846` 뒤의 작업 트리가 깨끗했다는 것(다음 커밋이 `docs/BACKLOG.md` 하나만 넣고 끝난 뒤 `git status --short`가 비었다)과 멈춘 자리("비운다"의 `git rm -r`이 승인 대기로 막힘)의 `git status --short`가 비었다는 것을 보았다
- 사용량이 모두 돌아와 `docs/TOOLS.md`에 까닭을 적어 `RUNLOG.md`와 함께 커밋하는 길은 장면에서 돌지 않았다
- 한계: 사용량 까닭을 `docs/TOOLS.md`에 적었는데 그 자리에 `RUNLOG.md` 커밋이 오지 않고 멈추는 경우(확인 실패로 "멈춘다"에서 사용자가 멈추기로 한 경우)는 `RUNLOG.md` 줄과 함께 커밋되지 않은 채 남는다. 고치기 전 `RUNLOG.md`의 줄도 같다
- 장면의 허용 목록에 `"Bash(git remote:*)" "Bash(git rm:*)"`가 없어 run의 "비운다"가 막혔다

## 하네스에서 걸린 것
- run 스킬의 8번이 고칠 phase의 통과 조건에 "task 머리의 완료 조건이 모두 참이다"를 넣는데, task 머리의 완료 조건 3이 run `SKILL.md`의 마지막 커밋 시각을 기준으로 해 run `SKILL.md`를 고치는 고칠 phase는 그 조건을 커밋 뒤에 참으로 둘 수 없다. 회고가 문제를 run `SKILL.md`에 두었을 때 run의 8번 첫 판단("고치려면 계획 파일의 완료 조건을 바꾸거나 좁혀야 하는지")이 이 시각 조건을 보지 못했다
- 헤드리스 장면의 허용 목록(`docs/TOOLS.md`의 "스킬을 헤드리스로 돌려 볼 때의 허용 목록")에 `git remote`와 `git rm`이 없어 run이 "비운다"에서 승인 대기로 멈췄다. 장면 B가 보는 것은 그 앞이라 결과에는 걸리지 않았다
