# Phase 2: 고친 retro, eval, phase를 네 장면으로 돌린다

**목표**: 장면 R, E, P1, P2를 임시 복제본에서 돌린 결과가 `docs/TOOLS.md`의 새 절에 남고, 저마다 기대와 같다.

**테스트 먼저**: 아니오 — 이 phase는 스킬을 돌려 본 결과를 `docs/TOOLS.md`에 적기만 한다

**읽을 것**
- `plugins/plate/skills/retro/SKILL.md`, `plugins/plate/skills/eval/SKILL.md`, `plugins/plate/skills/phase/SKILL.md` (phase 1이 고친 본문. 장면의 대상이고, 돌릴 때 이 셋의 `git hash-object`를 적는다)
- `plugins/plate/skills/run/SKILL.md`의 4번, 7번, "하네스 eval을 맡긴다" 코드 블록 (장면의 프롬프트로 옮길 맡기는 글. 001이 마지막 줄 `부른 쪽: plate:run`을 더했다)
- `docs/TOOLS.md`의 "스킬을 헤드리스로 돌려 볼 때의 허용 목록"의 "차림에서 지킬 것"과 "description을 줄이고 `docs/TOOLS.md` 커밋 규칙을 한 곳에 모은 run을 장면 A~D로 다시 돌려 본 것" (차림의 사실과 장면 절의 꼴)
- `git show 44f2790^:docs/tasks/002-plan-phase-rules/done-phase-1.md`, `done-phase-2.md`, `done-phase-3.md` (장면 R의 자료. 확인 절의 `남은 것:` 줄 다섯), `git show 44f2790 -- docs/tasks/FRICTION.md` (지난 회고가 `문제`로 넣은 줄)
- `git show f080761:docs/tasks/eval.md` (장면 E의 자료로 돈 지난 eval이 "하네스에서 걸린 것"에 적은 두 줄)

**TODO**
- [x] phase 1의 산출물에 대어 장면의 조건을 맞춘다: 고친 retro, eval, phase 본문과 run의 맡기는 글을 읽어, task 머리 결정의 장면 프롬프트와 기대가 그 글과 맞는지 본다. 맞지 않으면 장면을 돌리지 않고 "계획이 틀림"으로 돌아온다 (읽기만 한다)
- [x] task 머리 결정의 공통 차림과 장면 R, E, P1, P2의 차림대로 장면 넷이 돌고, `docs/TOOLS.md`의 "Claude Code" 절 끝(Codex 절 앞)에 "고친 retro·eval·phase를 장면 R·E·P1·P2로 돌려 본 것" 절이 더해진다. 절 머리에 Claude Code 버전, 돌린 날, 공통 차림, 돌리기 전과 뒤의 원본 `git rev-parse HEAD`와 `git status --short`가 있다. 장면마다 명령, 돌린 시각과 `duration_ms`, 세션 id, 복제본과 기록 경로, 대상 본문 해시, 차림, 기대한 결과, 본 결과, 막힌 명령이 있다 (`docs/TOOLS.md`)

**통과 조건**
- 완료 조건 4가 참이다
  - 확인: `docs/TOOLS.md`의 새 장면 절을 읽어 장면 R, E, P1, P2마다 Claude Code 버전, 돌린 시각, 세션 id, 대상 본문 해시, 차림, 기대한 결과, 본 결과, 막힌 명령이 있고, 본 결과가 task 머리 결정의 기대와 같다. 하나라도 빠지거나 다르면 실패
  - 확인: 장면마다 적힌 본문 해시가 `git rev-parse HEAD:plugins/plate/skills/<retro|eval|phase>/SKILL.md`와 같다
  - 확인: 절 머리에 적힌, 돌리기 전과 뒤의 원본 `git rev-parse HEAD`가 같고 `git status --short`의 출력이 같다
- 완료 조건 3이 이 phase의 커밋 뒤에도 참이다
  - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`

## 한 일
- phase 1의 산출물에 대어 장면의 조건을 맞춘다: retro 5번(문제 갈래의 `남은 것:` 줄 규칙, 멈춤 갈래의 `권한`)·9번, eval 낱말 "정해 둔 물음"(`권한`)·3번 규칙 준수 표(`NNN-slug: RUNLOG`, `<tasks 이름>: RUNLOG` 행)·8번, phase 6번, run 4번·7번·"하네스 eval을 맡긴다"의 맡기는 글(마지막 줄 `부른 쪽: plate:run`)을 읽어, task 머리 결정의 네 장면 프롬프트와 기대가 그 글과 맞는 것을 봤다. 장면 R의 자료(`44f2790^`의 확인 절 `남은 것:` 줄 다섯, `44f2790`의 `FRICTION.md`)와 장면 E의 자료(`f080761`의 `eval.md` "하네스에서 걸린 것" 두 줄), 커밋 `7ea7eef`, `509b234`가 있는 것도 봤다 (읽기만 함)
- 장면 넷을 돌리고 `docs/TOOLS.md`에 절을 더한다: 장면마다 `mktemp -d`에 복제하고 `git remote set-head origin main`, R·E는 결정대로 브랜치와 `main`을 두고, P1·P2는 작은 tasks를 손으로 써 `6e1732c plan: scene-p`로 넣은 뒤, 네 장면을 `claude -p "<프롬프트>" --plugin-dir /Users/hugo/Desktop/harness-plate/plugins/plate --permission-mode bypassPermissions --output-format stream-json --verbose`로 함께 띄웠다(2026-10-28T00:37:08~00:41:17). 결과는 R `84c1f06 002-plan-phase-rules: 회고`(판정 통과, 문제 0), E `51e104b release-prep: 하네스 eval`, P1 `59610b8 001-hello: phase 1`(다섯 줄뿐), P2 `4fd9c1b 001-hello: phase 1`(다섯 줄 아래 run 안내)이다. `docs/TOOLS.md`의 "Claude Code" 절 끝(Codex 절 앞)에 "고친 retro·eval·phase를 장면 R·E·P1·P2로 돌려 본 것" 절을 더했다 (`docs/TOOLS.md`)

## 확인 결과
- 완료 조건 4가 참이다
  - `docs/TOOLS.md`의 새 절을 읽음 → 절 머리에 Claude Code 2.1.311, 돌린 날, 공통 차림, 원본의 전과 뒤 HEAD·status가 있고, R·E·P1·P2마다 명령(프롬프트), 돌린 시각과 `duration_ms`, 세션 id, 복제본과 기록 경로, 대상 본문 해시, 차림, 기대한 결과, 본 결과, 막힌 명령이 있다. 본 결과는 저마다 출력 기록(`turn<장면>.jsonl`의 결과 줄)과 복제본의 `git log --name-only`, `retro.md`, `FRICTION.md`, `eval.md`, `RUNLOG.md`를 직접 대어 본 것이고 task 머리 결정의 기대와 같다. 통과
  - `git rev-parse HEAD:plugins/plate/skills/{retro,eval,phase}/SKILL.md` → `f1d13ac4…`, `9414c9dc…`, `69385efa…`. 절에 적힌 해시(돌릴 때의 `git hash-object`)와 같다. 통과
  - 원본 `git rev-parse HEAD` 전(00:36:37과 장면을 띄우기 직전) `34280136ff018c57e3fb17fdd4c03b973217604a`, 뒤(00:41:49) 같음. `git status --short`는 00:36:37에 빈 출력, 뒤(00:41:49)에 ` M docs/tasks/003-agent-rules/phase-2.md`. 그 사이 원본에 한 변경은 TODO 1 체크 하나(`git diff --stat` → 그 파일 1줄)라 장면을 띄우기 직전의 값은 뒤와 같다. 통과
- 완료 조건 3이 이 phase의 커밋 뒤에도 참이다
  - `python3 -m unittest discover -s tests` → `Ran 161 tests`, 마지막 줄 `OK`. 통과

## 계획과 달라진 점
- 없음

## 남은 것
- 원본의 "돌리기 전" `git status --short`는 장면을 띄우기 직전(TODO 1 체크 뒤)의 것으로 적었다. 그보다 앞 00:36:37의 것은 비었다. 그 차이는 이 phase의 체크박스 한 줄이고 장면이 원본을 바꾼 것은 없다
- 장면 E의 eval은 "하네스에서 걸린 것"에 "`FRICTION.md`의 문제 줄과 회고 절의 "문제 아님"을 어느 쪽으로 셀지 갈렸다"를 적었다. 그 기록(release-prep)은 #49를 고치기 전의 retro가 쓴 것이라 이번 고침의 장면 기대에는 걸리지 않지만, eval 2번이 고치기 전의 `FRICTION.md`를 만났을 때의 셈은 정하지 않은 채다
- 장면 R의 retro는 `문제` 0개로 판정하면서 `FRICTION.md`에 `문제` 줄 여섯을 더했다. 모두 기록·확인 절의 "하네스에서 걸린 것"과 계획 수정에서 온 것이라 retro 5번대로이고 기대에 걸리지 않는다
- 복제본과 출력 기록은 임시 폴더라 지워질 수 있다

## 하네스에서 걸린 것
- 결정의 장면 R 프롬프트 "run 7번의 맡기는 글에 task 폴더를 넣은 세 줄과 `부른 쪽: plate:run`"은, run 7번의 코드 블록이 이미 `부른 쪽: plate:run`을 셋째 줄로 담고 있어 "세 줄과" 한 줄을 더하면 네 줄로 읽힌다. 코드 블록 그대로의 세 줄(마지막이 `부른 쪽: plate:run`)로 돌렸다
- 통과 조건의 "돌리기 전과 뒤의 `git status --short`가 같다"는 TODO 1의 체크(이 스킬 2번의 "항목 하나를 끝낼 때마다 `- [x]`로 바꾼다")가 장면 앞에 원본을 바꾸는 것과 맞물린다. 처음 적은 "전"(00:36:37, 빈 출력)은 체크 앞이라, 장면을 띄우기 직전의 것을 "전"으로 적었다
