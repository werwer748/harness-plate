# Phase 1: tasks 끝의 문제를 고친다

**목표**: task 머리의 완료 조건에 적힌 것을 모두 고친다.

**테스트 먼저**: 아니오 — 고칠 문제가 `plugins/plate/skills/check/SKILL.md`, `plugins/plate/skills/review/SKILL.md`(`.md`)의 글뿐이라 코드 파일의 동작을 바꾸지 않는다

**읽을 것**
- `docs/tasks/review.md`의 `## 평가 1` 절
- `docs/tasks/eval.md`의 `## eval 1` 절
- `plugins/plate/skills/check/SKILL.md`
- `plugins/plate/skills/review/SKILL.md`
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/ADR.md`
- `docs/TOOLS.md`

**TODO**
- [x] check 5번이 계획의 `- 돌리지 않음: {까닭}` 줄로 돌리지 않기로 정한 동작에 대한 "돌려 보지 않은 위험" 줄까지 실패로 해, 수행이 고칠 길 없는 실패와 세 번 실패의 멈춤으로 이어질 수 있다 (`plugins/plate/skills/check/SKILL.md`)
- [x] 결과물인 마크다운만 바뀐 경우의 테스트 적절성 표가 실행 경로 없는 파일(매니페스트 버전 줄)이 함께 바뀌면 쓰이지 않는다 (`plugins/plate/skills/review/SKILL.md`)
- [x] "기능 적합성은 돌린 확인으로 매긴다" 줄이 새 표 뒤에 붙어 일반 등급표의 줄인지 새 표의 줄인지 흐려진다 (`plugins/plate/skills/review/SKILL.md`)

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다

## 한 일
- check 5번이 계획의 `- 돌리지 않음: {까닭}` 줄로 돌리지 않기로 정한 동작에 대한 "돌려 보지 않은 위험" 줄까지 실패로 해, 수행이 고칠 길 없는 실패와 세 번 실패의 멈춤으로 이어질 수 있다: 5번에 "돌려 보지 않은 위험을 적은 줄이 task 머리의 완료 조건에 딸린 `돌리지 않음` 줄이 돌리지 않기로 정한 동작에 대한 것이면 통과 조건이 보는 동작에 걸려도 실패가 아니고 '하네스에서 걸린 것'으로 옮긴다(결함을 적은 줄은 들지 않는다)" 갈래를 더하고, 첫 갈래에 "아래의 `돌리지 않음` 갈래는 빼고"를 붙였다. 같은 뜻을 description, 절대 규칙 3, 확인 절 양식의 "남은 것" 줄, 적는 규칙의 "남은 것: …" 줄에도 맞췄다 (`plugins/plate/skills/check/SKILL.md`)
- 결과물인 마크다운만 바뀐 경우의 테스트 적절성 표가 실행 경로 없는 파일(매니페스트 버전 줄)이 함께 바뀌면 쓰이지 않는다: 낱말에 "실행 경로 없는 파일"(바뀐 줄이 매니페스트의 `"version"` 줄처럼 실행되지 않는 값뿐인 파일)을 더하고, 4번 표의 테스트 적절성 줄, 5번의 표를 쓰는 조건, PR 모드의 판단 못함 조건을 "결과물인 마크다운과 실행 경로 없는 파일뿐이면"으로 바꾸고, 5번에 "실행 경로 없는 파일이 함께 바뀌어도 이 표를 쓴다"를 적었다 (`plugins/plate/skills/review/SKILL.md`)
- "기능 적합성은 돌린 확인으로 매긴다" 줄이 새 표 뒤에 붙어 일반 등급표의 줄인지 새 표의 줄인지 흐려진다: 그 줄을 새 표 뒤에서 빼 등급표 아래 목록(부채 비율 줄 다음)으로 옮겼다 (`plugins/plate/skills/review/SKILL.md`)
- 통과 조건의 문서 확인을 위해 ADR-024 트레이드오프의 "바뀐 코드 파일이 결과물인 마크다운뿐이면"을 "결과물인 마크다운과 실행 경로 없는 파일(매니페스트의 버전 줄 같은 것)뿐이면"으로 맞췄다 (`docs/ADR.md`)

## 확인 결과
- task 머리의 완료 조건이 모두 참이다.
  - 완료 조건 1: check 5번을 다시 읽음 → 셋째 갈래에 `돌리지 않음` 줄로 돌리지 않기로 정한 동작의 돌려 보지 않은 위험은 실패가 아니라고 적혀 있다. 통과
  - 완료 조건 2: review 5번의 표 조건을 다시 읽음 → "결과물인 마크다운과 실행 경로 없는 파일뿐이면 … 실행 경로 없는 파일(매니페스트의 버전 줄 같은 것)이 함께 바뀌어도 이 표를 쓴다". 통과
  - 완료 조건 3: review 5번을 다시 읽음 → "기능 적합성은 돌린 확인으로 매긴다" 줄이 등급표 아래 목록(부채 비율 줄과 테스트 적절성 줄 사이)에 있다. 통과
  - 완료 조건 4, plan의 "phase의 파일" 읽을 것 줄(270줄), "조건"(234줄), 6번(98줄)을 읽음 → 세 곳 모두 줄 번호 대신 절·항목 이름으로 가리키는 규칙이 있다. 통과
  - 완료 조건 4, plan의 "조건"(233줄), 6번(99줄), tasks 머리 양식(156줄), task 머리 양식(179줄)을 읽음 → 네 곳 모두 돌려 보는 확인과 `돌리지 않음` 줄의 규칙과 맞는다. 통과
  - 완료 조건 4, check의 절대 규칙 3, 5번, 확인 절 양식, 적는 규칙을 읽음 → 걸리면 실패, 걸리지 않거나 `돌리지 않음`으로 정한 동작의 위험이면 "하네스에서 걸린 것"으로 서로 어긋나지 않는다. 통과
  - 완료 조건 4, retro 4번과 회고 절 양식을 읽음 → 바뀌지 않았고 "남은 것"을 모아 판정한다. 통과
  - 완료 조건 4, eval의 낱말 `done-phase-N.md`, `retro.md`(29~30줄)를 읽음 → 확인 절의 "남은 것", 회고 절의 "남은 것"이 들어 있어 꼴과 맞는다. 통과
  - 완료 조건 4, `mktemp -d`에 seed를 만들고 `git clone --bare`로 원격, 그 복제본의 `main`에 커밋 `plan`을 더한 뒤 `git switch -c tasks/x`, `git remote get-url origin`, `git rev-parse --verify --quiet refs/remotes/origin/main`, `git log --oneline refs/remotes/origin/main..main`, `git log --oneline tasks/x..main`, `git branch -f main refs/remotes/origin/main` → 되돌리기 전 1개(tasks..main 0개), 되돌린 뒤 0개, `git merge-base main tasks/x`가 `refs/remotes/origin/main`과 같음, `git log tasks/x`에 `fdc2f77 plan`이 남음. 임시 디렉터리 지움. 통과
  - 완료 조건 4, run의 낱말 "작업 트리의 스킬 줄"(47줄)과 review의 낱말 "갈라진 곳"(31줄)을 읽음 → 둘 다 로컬 기본 브랜치의 merge-base. 통과
  - 완료 조건 4, run의 `RUNLOG.md` 절(498줄) → 물은 자리 목록에 `기본 브랜치`가 있다. 통과
  - 완료 조건 4, review 4번(88줄), 5번 등급표와 그 아래 줄, PR 모드 절을 읽음 → 결과물인 마크다운(과 실행 경로 없는 파일)만 바뀐 경우의 A~E 표, 읽기만 하는 확인과 `돌리지 않음`이 낮은 칸, PR 모드의 판단 못함이 있다. 통과
  - 완료 조건 4, run 498줄의 목록과 eval 40줄 "정해 둔 물음"을 견줌 → `멈춤`을 뺀 여섯(`실행 방식`, `커밋하지 않은 변경`, `기본 브랜치`, `고칠 phase`, `다음 task`, `고칠지`)이 같다. 통과
  - 완료 조건 4, retro 5번의 "멈춤" 줄을 읽음 → 물은 자리가 `멈춤`인 줄에서 모으고 그 밖은 멈춤이 아니라 eval과 맞는다. 통과
  - 완료 조건 4, `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "0.15.0",`. 통과
  - 완료 조건 4, `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
  - 완료 조건 4, `python3 -m unittest discover -s tests` → `Ran 104 tests in 17.879s`, 마지막 줄 `OK`. 통과
  - 완료 조건 4, `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `README.md`를 문서마다 `돌리지 않음`, `남은 것`, `결과물인 마크다운`, `테스트 적절성`, `실행 경로`로 찾아 그 줄을 읽음 → ADR-024 트레이드오프가 "마크다운뿐이면"이라 새 조건과 맞지 않아 고쳤고, 고친 뒤 어긋나는 줄이 없다. 통과

## 계획과 달라진 점
- 계획의 TODO는 check와 review만 고치는데, 통과 조건(완료 조건 4의 문서 확인)을 맞추려고 `docs/ADR.md` ADR-024 트레이드오프의 괄호 한 곳을 review의 새 조건에 맞춰 고쳤다. 그대로 두면 "결과물인 마크다운뿐이면"이 바뀐 review와 어긋난다

## 남은 것
- 바뀐 check 5번과 review의 테스트 적절성 조건을 헤드리스로 돌려 보지 않았다. 본문을 읽어 확인했을 뿐이다
- "실행 경로 없는 파일"은 바뀐 줄이 동작을 고르지 않는 값인지를 review가 판단으로 가른다. 버전 줄 말고 다른 설정 값에서는 판단이 갈릴 수 있다
- 완료 조건 4의 git 확인에서 `git branch -f`가 `main`에 upstream(`origin/main`)을 잡았다. 이전 tasks에서도 적힌 동작이고 이 phase가 바꾼 것이 아니다

## 하네스에서 걸린 것
- 완료 조건 4의 `mktemp -d` 확인은 bare 원격을 어떻게 채우는지 적지 않는다. 앞선 기록대로 푸시 훅을 피하려 `git clone --bare`로 원격을 채웠다
- task 머리 완료 조건 4가 "tasks 완료 조건 1~7"을 가리키지만 phase 스킬은 tasks 머리를 읽지 않는다. 완료 조건 4에 딸린 확인 줄들만 돌렸다
