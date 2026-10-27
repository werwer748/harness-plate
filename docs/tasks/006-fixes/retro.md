# 회고

## 회고 1

**확인**
- 1. check 5번이 계획의 `- 돌리지 않음: {까닭}` 줄로 돌리지 않기로 정한 동작에 대한 "돌려 보지 않은 위험" 줄까지 실패로 해, 수행이 고칠 길 없는 실패와 세 번 실패의 멈춤으로 이어질 수 있다
  - `plugins/plate/skills/check/SKILL.md` 5번을 읽음 → 셋째 갈래에 "돌려 보지 않은 위험을 적은 줄이 task 머리의 완료 조건에 딸린 `- 돌리지 않음: {까닭}` 줄이 돌리지 않기로 정한 동작에 대한 것이면, 통과 조건이 보는 동작에 걸려도 실패가 아니다"가 있고, 첫 갈래에 "(아래의 `돌리지 않음` 갈래는 빼고)"가 붙었다. description, 절대 규칙 3, 확인 절 양식의 "남은 것" 줄, 적는 규칙의 "남은 것: …" 줄도 같은 뜻이다. 통과
- 2. 결과물인 마크다운만 바뀐 경우의 테스트 적절성 표가 실행 경로 없는 파일(매니페스트 버전 줄)이 함께 바뀌면 쓰이지 않는다
  - `plugins/plate/skills/review/SKILL.md`의 낱말과 5번을 읽음 → 낱말에 "실행 경로 없는 파일"이 있고, 5번에 "바뀐 코드 파일이 결과물인 마크다운과 실행 경로 없는 파일뿐이면 … 실행 경로 없는 파일(매니페스트의 버전 줄 같은 것)이 함께 바뀌어도 이 표를 쓴다"가 있다. 4번의 표와 PR 모드의 판단 못함 조건도 같은 조건이다. 통과
- 3. "기능 적합성은 돌린 확인으로 매긴다" 줄이 새 표 뒤에 붙어 흐려진다
  - review 5번을 읽음 → 그 줄이 등급표 아래 목록의 부채 비율 줄 다음에 있고, 새 표 뒤에는 없다. 통과
- 4. tasks 완료 조건 1~7이 참이다
  - plan의 "phase의 파일" 읽을 것 줄(270줄), "조건"(234줄), 6번(98줄)을 읽음 → 세 곳 모두 앞 phase나 앞 task가 고칠 파일을 줄 번호 대신 절·항목 이름으로 가리키고, 6번은 이웃 줄을 빠뜨리지 않는지도 본다. 통과
  - plan의 "조건"(233줄), 6번(99줄), tasks 머리 양식(156줄), task 머리 양식(179줄)을 읽음 → 네 곳 모두 돌려 보는 확인과 따로 두는 `- 돌리지 않음: {까닭}` 줄의 규칙과 맞는다. 통과
  - check의 절대 규칙 3, 5번, 확인 절 양식, 적는 규칙을 읽음 → 걸리면 실패, 걸리지 않거나 `돌리지 않음`으로 정한 동작의 위험이면 "하네스에서 걸린 것"으로, 네 곳이 서로 어긋나지 않는다. 통과
  - retro 4번과 회고 절 양식을 읽음 → `done-phase-N.md`마다 "남은 것"의 세 종류 줄을 모아 줄마다 판정해 회고 절 "남은 것"에 적는다. 통과
  - eval의 낱말 `done-phase-N.md`(29줄)와 `retro.md`(30줄)를 읽음 → 확인 절의 "남은 것", "실패", "하네스에서 걸린 것", "판정"과 회고 절의 "확인", "남은 것", "문제", "판정"이 바뀐 꼴과 맞는다. 통과
  - `mktemp -d` 안에 seed 저장소, `git clone --bare`로 bare 원격, 그 복제본을 만들고 복제본 `main`에 커밋 `plan`을 더한 뒤 `git switch -c tasks/x`, `git remote get-url origin`, `git rev-parse --verify --quiet refs/remotes/origin/main`, `git log --oneline refs/remotes/origin/main..main`, `git log --oneline tasks/x..main`, `git branch -f main refs/remotes/origin/main`을 돌림 → 되돌리기 전 알아보기 1개(`ae22298 plan`, tasks/x..main 0개), 되돌린 뒤 0개, `git merge-base main tasks/x`가 `refs/remotes/origin/main`과 같은 `139fd17`, `git log tasks/x`에 `ae22298 plan`이 남음. 임시 디렉터리 지움(`ls` → No such file or directory). 통과
  - run의 낱말 "작업 트리의 스킬 줄"(47줄)과 review의 낱말 "갈라진 곳"(31줄)을 읽음 → 둘 다 원격 추적 ref가 아니라 로컬 기본 브랜치의 `git merge-base {기본 브랜치} HEAD`라고 적는다. 통과
  - run의 `RUNLOG.md` 절(498줄)을 읽음 → 물은 자리 목록에 `기본 브랜치`가 있다. 통과
  - review 4번의 테스트 적절성 줄, 5번 등급표와 그 아래 줄과 새 표, PR 모드의 "등급을 매긴다" 줄을 읽음 → 완료 조건의 돌려 보는 확인으로 매기는 A~E 표, 읽기만 하는 확인과 `돌리지 않음` 줄이 낮은 칸에 든다는 줄, PR 모드의 "판단 못함 — 완료 조건이 없다"가 있다. 통과
  - run 498줄의 목록과 eval 낱말 "정해 둔 물음"(40줄)을 견줌 → `멈춤`을 뺀 `실행 방식`, `커밋하지 않은 변경`, `기본 브랜치`, `고칠 phase`, `다음 task`, `고칠지` 여섯이 같다. 통과
  - retro 5번의 "멈춤" 줄을 읽음 → 물은 자리가 `멈춤`인 줄에서 모으고 정해 둔 자리의 줄은 멈춤이 아니라고 적어 eval 41줄의 "멈춤"과 맞는다. 통과
  - `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "0.15.0",`. 통과
  - `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
  - `python3 -m unittest discover -s tests` → `Ran 104 tests in 17.989s`, 마지막 줄 `OK`. 통과
  - `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `README.md`를 문서마다 `결과물인 마크다운`, `테스트 적절성`, `실행 경로`, `돌리지 않음`, `남은 것`, `정해 둔 물음`, `merge-base`, `갈라진 곳`으로 찾아 그 줄을 읽음 → ADR-024 트레이드오프(51줄)가 review의 새 조건과 맞고, PRD 18줄, ARCHITECTURE 51·74줄, README 25·116줄, TOOLS 10·84·120줄은 바뀐 동작과 어긋나지 않는다. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 104 tests`, `OK`. 통과

**남은 것**
- phase 1: 바뀐 check 5번과 review의 테스트 적절성 조건을 헤드리스로 돌려 보지 않았다. 본문을 읽어 확인했을 뿐이다 → 문제 아님 (tasks 머리의 범위 밖 "바뀐 스킬을 헤드리스 세션으로 돌려 보는 것"과 결정 "에이전트가 도는 동작은 본문을 읽어서 확인한다"가 돌리지 않기로 정했고, task 머리 완료 조건 1~3은 본문에 규칙이 적혀 있는지를 본다)
- phase 1: "실행 경로 없는 파일"은 바뀐 줄이 동작을 고르지 않는 값인지를 review가 판단으로 가른다. 버전 줄 말고 다른 설정 값에서는 판단이 갈릴 수 있다 → 문제 아님 (task 머리 완료 조건 2와 리뷰의 소스 문제 2는 매니페스트 버전 줄이 함께 바뀐 경우만 다루고, 그 경우는 낱말의 예로 명시돼 갈리지 않는다)
- phase 1: 완료 조건 4의 git 확인에서 `git branch -f`가 `main`에 upstream(`origin/main`)을 잡았다 → 문제 아님 (이 task가 바꾼 동작이 아니고, 회고에서 다시 돌려도 같은 메시지 `branch 'main' set up to track 'origin/main'.`가 나왔지만 되돌린 `main`이 `origin/main`을 추적하는 것은 되돌리기의 뜻과 맞는다)

**문제**
- 없음

**판정**: 통과
