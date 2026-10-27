# 코드 평가

## 평가 1

**대상**
- 범위: `a3c1158`(main에서 갈라진 곳)부터 `27a5c72`까지
- 결과물인 마크다운 절: `plugins/plate/skills/*/SKILL.md`
- 바뀐 코드 파일 8개, 새 줄 65줄, 잴 새 줄 2줄
  - `plugins/plate/.claude-plugin/plugin.json` +1
  - `plugins/plate/.codex-plugin/plugin.json` +1
  - `plugins/plate/skills/check/SKILL.md` +22 (결과물인 마크다운)
  - `plugins/plate/skills/eval/SKILL.md` +5 (결과물인 마크다운)
  - `plugins/plate/skills/plan/SKILL.md` +7 (결과물인 마크다운)
  - `plugins/plate/skills/retro/SKILL.md` +6 (결과물인 마크다운)
  - `plugins/plate/skills/review/SKILL.md` +14 (결과물인 마크다운)
  - `plugins/plate/skills/run/SKILL.md` +9 (결과물인 마크다운)

**잰 것**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 104 tests in 17.804s`, `OK`. 통과
- 커버리지: 측정 못함 — 명령 절과 ADR-024가 커버리지 도구를 두지 않는다. 잴 새 줄은 2줄(JSON의 버전 줄)이다
- 중복: 측정 못함 — 명령 절과 ADR-024가 중복 검사 도구를 두지 않는다(`jscpd` 없음)
- 정적 분석: `python3 -m json.tool plugins/plate/.claude-plugin/plugin.json`, `python3 -m json.tool plugins/plate/.codex-plugin/plugin.json` → 두 파일 모두 유효한 JSON. 마크다운에 댈 정적 분석 도구는 없다
- 보안 검사: 측정 못함 — 의존성 목록이 없고 보안 규칙 검사 도구(`semgrep`, `bandit`, `pip-audit`)가 이 환경에 없다

**완료 조건**
- 1 (#26) plan의 "phase의 파일" 읽을 것 줄, "조건", 6번에 줄 번호 대신 절 이름이나 항목 이름으로 가리킨다는 줄과 점검 줄이 있다
  - `plugins/plate/skills/plan/SKILL.md`의 "phase의 파일" 읽을 것 줄(270줄), "조건"(234줄), 6번(98줄)을 읽음 → 세 곳 모두 적혀 있고 6번은 이웃 줄을 빠뜨리지 않는지도 본다. 통과
- 2 (#32) plan의 "조건", 6번, 양식의 tasks 머리·task 머리 완료 조건이 돌려 보는 확인과 `- 돌리지 않음: {까닭}` 줄의 규칙과 맞는다
  - "조건"(233줄), 6번(99줄), tasks 머리 양식(156줄), task 머리 양식(179줄)을 읽음 → 네 곳 모두 맞는다. 통과
- 3 (#31) check와 retro가 "남은 것"을 판정한다
  - check의 절대 규칙 3(18줄), 5번(54~62줄), 확인 절의 양식(104~105줄), 적는 규칙(122~126줄)을 읽음 → 실패와 "하네스에서 걸린 것"으로 가르는 규칙이 서로 어긋나지 않는다. 통과
  - retro 4번(77줄)과 회고 절의 양식(144~145줄)을 읽음 → `done-phase-N.md`마다 세 종류의 줄을 모아 줄마다 판정해 적는다. 통과
  - eval의 낱말 `done-phase-N.md`와 `retro.md`(29~30줄)를 읽음 → 확인 절의 "남은 것"과 회고 절의 "남은 것"이 들어 있다. 통과
- 4 (#29) run의 로컬 기본 브랜치 물음과 갈라진 곳
  - `mktemp -d` 안에 seed 저장소를 bare로 복제해 원격을 만들고(푸시 훅이 `main`으로의 푸시를 막아 푸시 없이 원격을 채웠다) 그 복제본의 `main`에 커밋 `plan`을 더한 뒤 run 1번의 명령을 적힌 그대로 돌림 → `git switch -c tasks/x`, `git remote get-url origin` 성공, `git rev-parse --verify --quiet refs/remotes/origin/main` 성공, 되돌리기 전 `git log --oneline refs/remotes/origin/main..main` 1개, `git log --oneline tasks/x..main` 0개, `git branch -f main refs/remotes/origin/main` 뒤 0개, `git merge-base main tasks/x`가 `refs/remotes/origin/main`과 같음, `git log tasks/x`에 `plan`이 남음. 이미 있던 `tasks/y`로 바꾼 갈래는 두 알아보기가 각각 1개를 내 묻지 않는 갈래였고 `main`에 커밋이 남음. 임시 디렉터리는 지움. 통과
  - run의 낱말 "작업 트리의 스킬 줄"(47줄)과 review의 낱말 "갈라진 곳"(31줄)을 읽음 → 둘 다 원격 추적 ref가 아니라 로컬 기본 브랜치의 `git merge-base`라고 적는다. 통과
  - run의 `RUNLOG.md` 절(498~499줄)을 읽음 → 물은 자리 목록과 task에 걸리지 않는 물음 목록에 `기본 브랜치`가 있다. 통과
- 5 (#27) review의 결과물인 마크다운만 바뀐 경우의 테스트 적절성
  - review의 4번(88줄), 5번의 등급표 아래 줄과 표(121~131줄), PR 모드 절(196줄)을 읽음 → A~E 칸이 있고 읽기만 하는 확인과 `돌리지 않음` 줄은 돌려 보는 확인보다 낮은 칸에 들고, PR 모드는 판단 못함이다. 통과
- 6 (#28) eval의 정해 둔 물음과 멈춤
  - run의 물은 자리 목록(`실행 방식`, `커밋하지 않은 변경`, `기본 브랜치`, `고칠 phase`, `다음 task`, `멈춤`, `고칠지`)과 eval의 낱말 "정해 둔 물음"(40줄)을 견줌 → `멈춤`을 뺀 여섯이 같다. 통과
  - retro 5번의 "멈춤"(86줄)을 읽음 → 물은 자리가 `멈춤`인 줄에서 모으고 그 밖은 멈춤이 아니라고 적어 eval과 맞는다. 통과
- 7 버전, 마켓플레이스, 테스트, 문서
  - `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "0.15.0",`. 통과
  - `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
  - `python3 -m unittest discover -s tests` → 마지막 줄 `OK`. 통과
  - `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `README.md`를 바뀐 여섯 동작의 낱말(남은 것, 정해 둔 물음, 멈춤, 테스트 적절성, merge-base, 갈라진 곳, 줄 번호, 돌리지 않음, 되돌림)과 check·retro·review·eval·plan·run을 말하는 줄로 찾아 읽음 → ARCHITECTURE 50·59줄, ADR-024 트레이드오프(51줄), README 10줄은 새 동작과 맞고, 어긋나는 줄은 찾지 못했다. 통과

**범주**
- 신뢰성
  - 근거: `plugins/plate/skills/check/SKILL.md:56` 5번이 "돌려 보지 않은 위험"을 적은 줄을 통과 조건이 보는 동작에 걸리면 모두 실패로 하고(58줄), 계획이 이미 `- 돌리지 않음: {까닭}` 줄로 돌리지 않기로 정한 동작(plan 233줄)을 빼지 않는다. 수행이 그 동작을 돌려 보지 않았다고 정직하게 "남은 것"에 적으면 수행이 고칠 길이 없는 실패가 되고, 다시 수행해도 같아 세 번 실패의 멈춤으로 간다. phase 스킬의 "남은 것" 규칙도 이 경우를 다루지 않는다 (기능, 중간)
  - 근거: `plugins/plate/skills/review/SKILL.md:121` 결과물인 마크다운만 바뀐 경우의 표는 바뀐 코드 파일이 결과물인 마크다운"뿐"일 때만 쓰여, 버전 올림처럼 실행 경로가 없는 JSON 한 줄이 함께 바뀌면 일반 등급표로 돌아간다. 이 레포는 tasks마다 매니페스트 버전을 올리므로(tasks 머리의 결정 "동작이 바뀌어 tasks마다 마이너를 올린다", 이 tasks의 `005-release`) 새 표가 이 레포의 tasks 끝 평가에서 쓰이지 않고, 테스트 적절성이 `tests/`의 테스트로만 매겨진다(이 평가가 그랬다) (기능, 낮음)
  - 등급: C — 가장 무거운 문제가 중간
- 보안
  - 핫스팟: `plugins/plate/skills/run/SKILL.md:69` `git branch -f {기본 브랜치} refs/remotes/origin/{기본 브랜치}`가 사용자의 로컬 기본 브랜치를 옮긴다 → 안전. 승인한 뒤에만 돌고, 바로 앞(67~68줄)의 `git log --oneline tasks/<이름>..{기본 브랜치}`가 비어 있을 때만 물어 옮긴 커밋은 tasks 브랜치에 남는다. 임시 저장소에서 돌려 커밋이 남는 것을 봤다
  - 근거: 바뀐 코드 파일의 새 줄 65줄을 모두 읽었다. 비밀, 밖에서 들어온 입력을 셸에 넣는 곳, 권한을 건너뛰는 규칙은 없다. 문제 0개
  - 등급: A — 문제 0개
- 유지보수성
  - 근거: `plugins/plate/skills/review/SKILL.md:132` 일반 등급표에 딸린 "기능 적합성은 돌린 확인으로 매긴다" 줄이 새로 끼운 결과물인 마크다운만 바뀐 경우의 표(123~131줄) 바로 뒤에 빈 줄 없이 붙어, 그 표에 딸린 줄처럼 읽힌다. 119~121줄의 목록 안으로 옮기면 된다 (문서, 5분)
  - 부채 비율: 5분 ÷ (65줄 × 30분) = 0.26%
  - 등급: A — 부채 비율 5% 이하
- 테스트 적절성
  - 근거: 바뀐 코드 파일에 JSON 두 개가 들어 결과물인 마크다운만 바뀐 경우가 아니므로 일반 등급표로 매긴다. 커버리지는 측정 못함이라 판단만으로 매긴다
  - 근거: `tests/`(`test_edit_guard.py`, `test_push_guard.py`, `test_verdict.py`)는 훅과 판정 스크립트만 시험하고, 바뀐 동작(버전 줄, 여섯 스킬의 규칙)을 시험하는 테스트는 없다. 버전 줄은 완료 조건의 `grep`과 `claude plugin validate .`이, run의 #29 명령은 완료 조건의 `mktemp -d` 확인이 돌려 봤지만 테스트 스위트에는 들지 않아 깨져도 실패할 테스트가 없다
  - 등급: E — 바뀐 동작에 테스트가 하나도 없다
- 기능 적합성
  - 근거: 완료 조건 1 통과: plan의 세 곳에 줄 번호 규칙이 있다
  - 근거: 완료 조건 2 통과: plan의 네 곳이 돌려 보는 확인 규칙과 맞는다
  - 근거: 완료 조건 3 통과: check, retro, eval이 "남은 것"의 판정과 꼴에서 맞는다
  - 근거: 완료 조건 4 통과: 임시 저장소에서 run 1번의 명령이 적힌 대로 돌았고 낱말과 물은 자리가 맞다
  - 근거: 완료 조건 5 통과: review의 새 칸과 PR 모드의 판단 못함이 적혀 있다
  - 근거: 완료 조건 6 통과: eval과 run의 목록이 `멈춤`을 빼고 같고 retro와 맞는다
  - 근거: 완료 조건 7 통과: 버전 0.15.0, 검증 통과, 테스트 OK, 문서에 어긋나는 줄 없음
  - 등급: A — 완료 조건의 확인이 모두 통과한다

**Sonar way 게이트**
- 새 문제 0개: 3개(신뢰성 2, 보안 0, 유지보수성 1). 실패
- 새 보안 핫스팟 모두 검토: 1/1. 통과
- 새 줄 커버리지 80% 이상: 잴 새 줄 2줄로 20줄 미만. 보지 않음
- 새 줄 중복 3% 이하: 잴 새 줄 2줄로 20줄 미만. 보지 않음
- 게이트: 실패

**소스 문제**
1. check 5번이 계획의 `- 돌리지 않음: {까닭}` 줄로 돌리지 않기로 정한 동작에 대한 "돌려 보지 않은 위험" 줄까지 실패로 해, 수행이 고칠 길 없는 실패와 세 번 실패의 멈춤으로 이어질 수 있다 (`plugins/plate/skills/check/SKILL.md:56`). 범주: 신뢰성
2. 결과물인 마크다운만 바뀐 경우의 테스트 적절성 표가 실행 경로 없는 파일(매니페스트 버전 줄)이 함께 바뀌면 쓰이지 않아, tasks마다 버전을 올리는 이 레포에서는 새 표가 쓰일 일이 없다 (`plugins/plate/skills/review/SKILL.md:121`). 범주: 신뢰성
3. "기능 적합성은 돌린 확인으로 매긴다" 줄이 새 표 뒤에 붙어 일반 등급표의 줄인지 새 표의 줄인지 흐려진다 (`plugins/plate/skills/review/SKILL.md:132`). 범주: 유지보수성
4. 바뀐 동작(버전 줄, 스킬 규칙)을 시험하는 테스트가 `tests/`에 없다 (`tests/`). 범주: 테스트 적절성

**하네스에서 걸린 것**
- review의 테스트 적절성: 바뀐 코드 파일에 매니페스트 JSON 두 줄이 들어 결과물인 마크다운만 바뀐 경우의 표를 쓰지 못하고 일반 등급표로 E를 매겼다. 새 표로 매겼다면 run의 #29만 돌려 보는 확인이 있고 나머지 다섯 동작은 읽기만 하는 확인과 `돌리지 않음` 줄뿐이라 D였다(소스 문제 2)
- 완료 조건 4의 확인은 "bare 원격과 그 복제본을 만들고"를 푸시로 채우려 했으나 plate의 푸시 훅(`push_guard.py`)이 임시 저장소의 `main`으로 하는 푸시도 막았다. seed 저장소를 `git clone --bare`해 푸시 없이 원격을 채워 돌렸다. 계획의 확인이 푸시 없이 원격을 만드는 방법을 적지 않았다
- 명령 절에 커버리지·중복·보안 검사 도구가 없어(ADR-024) 그 셋은 측정 못함이다
