# 코드 평가

## 평가 1

**대상**
- 범위: `5247154`(main에서 갈라진 곳)부터 `907650b`까지
- 결과물인 마크다운 절: `plugins/plate/skills/*/SKILL.md`
- 바뀐 코드 파일 6개, 새 줄 253줄, 잴 새 줄 169줄
  - `tests/test_cleanup_skill.py` +51
  - `tests/test_skill_rules.py` +118
  - `plugins/plate/skills/cleanup/SKILL.md` +41 (결과물인 마크다운)
  - `plugins/plate/skills/plan/SKILL.md` +9 (결과물인 마크다운)
  - `plugins/plate/skills/retro/SKILL.md` +2 (결과물인 마크다운)
  - `plugins/plate/skills/run/SKILL.md` +32 (결과물인 마크다운)

**잰 것**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 263 tests in 23.234s`, `OK`. 통과
- 커버리지: 측정 못함 — 명령 절이 커버리지 도구를 두지 않는다(ADR-024)
- 중복: 측정 못함 — 명령 절이 중복 검사 도구를 두지 않는다(ADR-024)
- 정적 분석: 측정 못함 — 프로젝트에 설정된 정적 분석 도구가 없다
- 보안 검사: 측정 못함 — 명령 절이 보안 검사 도구를 두지 않고 의존성 목록도 없다(ADR-024)

**완료 조건**
- 1. 테스트 묶음이 모두 통과한다.
  - `python3 -m unittest discover -s tests` → 마지막 줄 `OK`(263개). 통과
- 2. plan의 초안 점검과 조건 규칙, retro 4번이 되풀이되는 이름과 여러 입력의 경우를 덮게 하고, 테스트가 그 글을 지킨다(#80).
  - `grep -n '지난 tasks의 같은 이름' plugins/plate/skills/plan/SKILL.md plugins/plate/skills/retro/SKILL.md` → plan:115("6. 초안을 보여 주고 승인받는다", 102~136줄 안), plan:266("적는 규칙"의 **조건**, 260줄 아래), retro:79("4. task의 변경을 점검한다", 64~84줄 안). 통과
  - `cp -R`로 `mktemp -d` 사본을 만들고 사본의 plan·retro 본문에서 그 낱말이 든 줄을 `sed -i '' '/지난 tasks의 같은 이름/d'`로 지운 뒤 `python3 -m unittest tests.test_skill_rules.PlanRulesTest.test_80_repeated_names_and_multiple_inputs_covered tests.test_skill_rules.RetroRulesTest.test_80_decided_behavior_with_repeated_names_goes_out_of_bounds` → `FAILED (failures=4)`. 통과
  - 돌리지 않음 줄: plan과 retro를 헤드리스로 끝까지 돌리지 않는다(계획대로). 측정 못함
- 3. cleanup이 지금 브랜치의 HEAD에서 `cleanup/<보고서 이름>`을 만들어 커밋하고, 같은 이름이 있으면 번호를 붙이고, 고른 발견이 없으면 PR이나 합침을 묻는다.
  - `grep -n -F 'cleanup/<' plugins/plate/skills/cleanup/SKILL.md` → 절대 규칙 17·18줄, 5번 115·127줄, "고른 발견이 없을 때" 149~165줄. 통과
  - `mktemp -d` 시험 레포(`main`, 커밋 하나)에서 본문 5번의 이름 고르기(`git rev-parse --verify --quiet refs/heads/cleanup/<보고서 이름>`, 있으면 `-2`…)와 `git switch -c {고른 이름}`을 세 갈래로 돌림 → `main`에서: `cleanup/2026-10-29`가 `main`의 HEAD에서 생기고 `main` 해시 그대로. `tasks/x`(커밋 하나 더)에서: `cleanup/2026-10-29-2`가 `tasks/x`의 HEAD에서 생기고 `main` 그대로. 같은 이름이 이미 있을 때: `-2`가 붙고 옛 `cleanup/2026-10-29`의 해시 그대로. 통과
  - 돌리지 않음 줄: cleanup을 헤드리스로 끝까지 돌리지 않는다. 측정 못함
- 4. plan이 `cleanup/…`에서 묻지 않고 `tasks/<이름>`을 만들고 `**보낼 곳**:` 줄을 적는다.
  - `grep -n '보낼 곳' plugins/plate/skills/plan/SKILL.md` → 1번 55줄, 7번 139줄, 양식 170줄(절대 규칙 19줄도). 통과
  - 같은 시험 레포의 `cleanup/x`(`main`보다 커밋 하나 앞섬)에서 본문 7번의 `git rev-parse --verify --quiet refs/heads/tasks/y`(빈 출력) → `git switch -c tasks/y` → `git merge-base --is-ancestor cleanup/x tasks/y`가 0, `main` 해시 그대로. 통과
  - 돌리지 않음 줄: plan을 헤드리스로 끝까지 돌리지 않는다. 측정 못함
- 5. run이 보낼 곳이 있으면 비운 뒤 그 브랜치에 합치고 PR이나 합침을 묻고, 없으면 알리고 10번으로 간다.
  - `grep -n '보낼 곳' plugins/plate/skills/run/SKILL.md` → 0번 69·71·73·75줄, "비운다" 499·505줄, "PR을 연다" 523줄, "합친다" 564줄(절대 규칙 20줄도). 통과
  - 시험 레포에서 `cleanup/x` → `tasks/y`(커밋 둘, 마지막 `y: 비움`)를 두고 본문의 `git switch cleanup/x`, `git merge --no-ff -m 'y: 보낼 곳으로 합침' tasks/y`, `git branch -d tasks/y` → `cleanup/x`가 합친 끝 커밋을 품고 `main` 해시 그대로. 합친 뒤 `git branch --show-current`는 `cleanup/x`, `git log -1 --format=%s`는 `y: 보낼 곳으로 합침`, `git show HEAD^2^:…`이 읽힌다(0번의 보낼 곳으로 합친 뒤의 재개로 간다). `cleanup/x`를 지운 레포에서 `git rev-parse --verify --quiet refs/heads/cleanup/x` → 빈 출력. 통과
  - 돌리지 않음 줄: run을 헤드리스로 끝까지 돌리지 않고 PR은 GitHub이 있어야 한다. 측정 못함
- 6. 맥락 문서가 바뀐 동작과 맞다.
  - `grep -n -F 'cleanup/<' docs/PRD.md docs/ARCHITECTURE.md` → PRD 19줄(핵심 기능 9), ARCHITECTURE 56줄(plan 문단), 95·98줄(데이터 흐름의 정리 점검), 32줄(디렉터리 구조 cleanup 줄). 통과
  - `grep -n '보낼 곳' docs/PRD.md docs/ARCHITECTURE.md` → PRD 18줄(핵심 기능 8), ARCHITECTURE 57줄(run 문단), 81·84줄(데이터 흐름의 tasks 끝), 56·65줄(plan 문단과 계획). 통과

**범주**
- 신뢰성
  - 근거: `plugins/plate/skills/cleanup/SKILL.md:68` 보고서 경로는 작업 트리의 `docs/cleanup/`만 보고 정하는데, 이 tasks로 보고서는 기본 브랜치가 아니라 `cleanup/<보고서 이름>`에만 커밋된다(127줄). 같은 날 첫 cleanup 브랜치가 아직 합쳐지지 않은 채 기본 브랜치에서 다시 부르면 보고서 경로는 다시 `YYYY-MM-DD.md`이고 브랜치만 `-2`가 붙는다(115줄). 두 브랜치를 차례로 기본 브랜치에 합치면 같은 경로를 더한 add/add 충돌이 난다(시험 레포에서 `git merge cleanup/2026-10-29-2` → "충돌 (추가/추가): docs/cleanup/2026-10-29.md"로 확인). 2번의 지난 보고서도 합쳐지지 않은 cleanup 브랜치의 것을 보지 못한다. 지난 tasks의 같은 이름이 남은 경우를 브랜치에만 덮고 보고서 파일에는 덮지 않았다 (기능, 중간)
  - 등급: C — 가장 무거운 문제가 중간
- 보안
  - 핫스팟: `plugins/plate/skills/cleanup/SKILL.md:155` 보고서 첫 줄을 `gh pr create --title '…'`에 넣는다. 낱말 56줄의 작은따옴표 감싸기와 `'\''` 바꾸기, 본문은 `--body-file`로 보고서 경로를 그대로 넘긴다 → 안전
  - 핫스팟: `plugins/plate/skills/run/SKILL.md:514`·`515` tasks 머리의 `**보낼 곳**:` 줄 값을 `git switch {보낼 곳}`에 넣는다. 그 값은 plan이 `git branch --show-current`로 얻어 적은 브랜치 이름이고, 그 전에 511줄의 `git rev-parse --verify --quiet refs/heads/{보낼 곳}`이 로컬 브랜치인지 본다. 합침 메시지의 `<이름>`은 영어 소문자 이름이다 → 안전
  - 근거: 바뀐 네 스킬 본문의 새 줄과 두 테스트 파일의 새 줄을 모두 읽었고, 비밀, 권한 건너뛰기, 명령 치환으로 넘기는 글(`$(`)은 없다(테스트가 run 본문의 `$(`를 막는다). 문제 없음
  - 등급: A — 문제 0개
- 유지보수성
  - 근거: `plugins/plate/skills/cleanup/SKILL.md:54`·`55` "기본 브랜치"와 "GitHub 원격"의 정의를 run(`run/SKILL.md:47`·`55`)에서 그대로 복사했고, 52줄의 "cleanup 브랜치"는 plan(`plan/SKILL.md:27`)에 다른 글로 다시 정의했는데, 복사한 정의가 같은지 지키는 시험은 run·plan의 "테스트가 있는 프로젝트" 줄에만 있다(`tests/test_skill_rules.py:995`). 새 복사본이 어긋나도 걸리지 않는다. 지난 cleanup(2026-10-28 유지보수성-6)이 같은 꼴을 짚은 것과 일관되지 않다 (일관성, 15분)
  - 부채 비율: 15분 ÷ (253줄 × 30분) = 0.2%
  - 등급: A — 부채 비율 5% 이하
- 테스트 적절성
  - 근거: 결과물인 마크다운만 바뀐 경우의 표로 매김 — 바뀐 코드 파일이 결과물인 마크다운(네 스킬 본문)과 테스트 파일(`tests/test_cleanup_skill.py`, `tests/test_skill_rules.py`)뿐이다
  - 근거: cleanup 5번의 브랜치 고르기와 만들기, plan 7번의 `cleanup/…`에서 가르기, run "보낼 곳으로 합친다"의 합침·없을 때·재개 판정은 완료 조건 3·4·5가 시험 레포에서 돌려 보는 확인을 둔다
  - 근거: #80의 plan 6번·조건 규칙과 retro 4번(tasks 완료 조건 2, task 001)은 grep과 그 글을 지키는 단위 시험(읽기만 하는 확인)과 `돌리지 않음` 줄뿐이다. 요청의 두 축 가운데 하나라 주된 동작이다
  - 근거: cleanup "고른 발견이 없을 때"의 합침 갈래(`plugins/plate/skills/cleanup/SKILL.md:159`~`165`, `git switch {기본 브랜치}`, `git merge`, `git merge --abort`, `git branch -d`)와 run "보낼 곳으로 합친다" 6번의 충돌 뒤 되돌림은 GitHub 없이 시험 레포에서 돌릴 수 있는데 완료 조건에 돌려 보는 확인이 없고 grep·단위 시험과 `돌리지 않음` 줄만 있다
  - 등급: C — 주된 동작 가운데 돌려 보는 확인 없이 읽기만 하는 확인이나 `돌리지 않음` 줄만 있는 것이 있다
- 기능 적합성
  - 근거: 완료 조건 1 통과: 테스트 263개 `OK`
  - 근거: 완료 조건 2 통과: grep이 세 자리에 한 줄씩, 지운 사본에서 새 시험 `FAIL`
  - 근거: 완료 조건 3 통과: grep 세 자리, 시험 레포 세 갈래가 기대대로
  - 근거: 완료 조건 4 통과: grep 세 자리, 시험 레포에서 `tasks/y`가 `cleanup/x`를 품고 `main` 그대로
  - 근거: 완료 조건 5 통과: grep 네 자리, 시험 레포 세 갈래가 기대대로
  - 근거: 완료 조건 6 통과: 두 grep이 적힌 자리에 저마다 한 줄 이상
  - 근거: 2~5의 `돌리지 않음` 줄은 측정 못함(계획대로 헤드리스로 돌리지 않음)
  - 등급: A — 완료 조건의 확인이 모두 통과한다

**Sonar way 게이트**
- 새 문제 0개: 2개(신뢰성 1, 유지보수성 1). 실패
- 새 보안 핫스팟 모두 검토: 2/2. 통과
- 새 줄 커버리지 80% 이상: 측정 못함 — 잴 새 줄 169줄, 커버리지 도구 없음. 측정 못함
- 새 줄 중복 3% 이하: 측정 못함 — 중복 검사 도구 없음. 측정 못함
- 게이트: 실패

**소스 문제**
1. 보고서 경로를 작업 트리의 `docs/cleanup/`만 보고 정해, 같은 날 합쳐지지 않은 cleanup 브랜치가 있을 때 기본 브랜치에서 다시 부르면 브랜치는 `-2`가 붙지만 보고서 파일 이름은 같아 두 브랜치를 기본 브랜치에 합칠 때 add/add 충돌이 나고, 지난 보고서 읽기도 그 보고서를 놓친다 (`plugins/plate/skills/cleanup/SKILL.md:68`). 범주: 신뢰성
2. cleanup에 복사한 "기본 브랜치"·"GitHub 원격" 정의(run에서)와 plan·cleanup의 "cleanup 브랜치" 정의가 같은지 지키는 시험이 없다 (`plugins/plate/skills/cleanup/SKILL.md:52`). 범주: 유지보수성
3. cleanup "고른 발견이 없을 때"의 합침 갈래와 run "보낼 곳으로 합친다"의 충돌 뒤 되돌림, #80의 plan·retro 규칙에 돌려 보는 확인이 없다 (`plugins/plate/skills/cleanup/SKILL.md:159`). 범주: 테스트 적절성

**하네스에서 걸린 것**
- plan의 초안 점검(이 tasks가 더한 #80 규칙, `plugins/plate/skills/plan/SKILL.md:115`)이 "지난 tasks의 같은 이름이 남은 경우"를 브랜치 이름에는 덮었지만, 같은 변경이 만든 보고서 파일 이름의 되풀이(합쳐지지 않은 cleanup 브랜치)에는 확인을 두지 않았다. 완료 조건 3의 "같은 이름의 `cleanup/…`" 갈래가 브랜치만 본다.
- 명령 절이 커버리지·중복·보안 검사를 두지 않아(ADR-024) 잴 새 줄이 169줄인데 게이트의 커버리지와 중복이 측정 못함이다.
