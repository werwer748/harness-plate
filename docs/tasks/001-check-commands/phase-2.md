# Phase 2: review가 테스트 파일을 빼고 테스트 적절성의 표를 고른다 (#70)

**목표**: 완료 조건 2가 참이 되고, 그 글의 테스트와 review의 헤드리스 시험 기록이 있다.

**테스트 먼저**: 아니오 — 고치는 것은 스킬 본문과 ADR(`.md`)이고, 더하는 테스트는 그 글이 있는지를 볼 뿐 코드의 동작을 바꾸지 않는다

**읽을 것**
- `gh issue view 70 --repo werwer748/harness-plate` (원인과 해결책)
- `plugins/plate/skills/review/SKILL.md`의 "낱말"(실행 경로 없는 파일, 바뀐 코드 파일), "4. 판단한다"의 범주 표, "5. 등급을 매긴다"의 표 고르기 줄과 "결과물인 마크다운만 바뀐 경우의 테스트 적절성" 표, "PR 모드"의 등급을 매기는 줄, "기록의 양식"의 테스트 적절성 자리
- `plugins/plate/skills/run/SKILL.md`의 낱말 "테스트가 있는 프로젝트" (옮길 테스트 파일의 정의)
- `docs/ADR.md`의 ADR-024 트레이드오프
- `tests/test_skill_rules.py`의 모듈 docstring과 도우미 (테스트의 꼴)
- `docs/TOOLS.md`의 "스킬을 헤드리스로 돌려 볼 때의 허용 목록"
- `docs/ARCHITECTURE.md` 디렉터리 구조의 `test_skill_rules.py` 줄

**TODO**
- [x] review 낱말에 `**테스트 파일**`이 완료 조건 2의 정의 글(run의 정의와 같다)로 더해진다 (`plugins/plate/skills/review/SKILL.md`)
- [x] 4번 범주 표, 5번 표 고르기 줄, PR 모드의 등급을 매기는 줄의 `결과물인 마크다운과 실행 경로 없는 파일뿐이면`이 `결과물인 마크다운, 실행 경로 없는 파일, 테스트 파일뿐이면`으로 바뀐다. 5번에 `테스트 파일은 바뀐 동작이 아니라 그 근거라 표를 고를 때 세지 않는다`와 `테스트 적절성의 근거 첫 줄에 어느 표로 매겼는지 적는다`가 더해지고, "기록의 양식"의 테스트 적절성 자리에도 그 첫 줄이 든다 (`plugins/plate/skills/review/SKILL.md`)
- [x] ADR-024 트레이드오프의 괄호 안 글이 "결과물인 마크다운, 실행 경로 없는 파일(매니페스트의 버전 줄 같은 것), 테스트 파일뿐이면"으로 바뀐다 (`docs/ADR.md`)
- [x] 새 `ReviewRulesTest.test_70_test_files_do_not_pick_default_table`이 더해진다. 완료 조건 2의 review 글들이 그 절에 있고 옛 글이 없는지 본다. 모듈 docstring의 review 목록에 `#70`이 더해진다 (`tests/test_skill_rules.py`)
- [x] 디렉터리 구조의 `test_skill_rules.py` 줄의 규칙 목록에 "review가 테스트 파일도 빼고 표를 고름, 근거 첫 줄에 쓴 표를 적음"이 더해진다 (`docs/ARCHITECTURE.md`)
- [x] review의 헤드리스 시험을 두 갈래로 돌리고 이 phase의 "한 일"에 기록한다. 차림(갈래마다 따로 만든 `mktemp -d` 시험 저장소): `main`에 문서 지도에 `docs/ARCHITECTURE.md` 행이 있는 `AGENTS.md`, 결과물인 마크다운 절에 `skills/*/SKILL.md`와 명령 절의 테스트 `python3 -m unittest discover -s tests`가 있는 `docs/ARCHITECTURE.md`, `skills/x/SKILL.md`, 그 글을 보는 `tests/test_x.py`를 커밋한다. `tasks/x` 브랜치에서 `skills/x/SKILL.md`와 `tests/test_x.py`를 바꾸고, 완료 조건 하나에 읽기만 하는 확인(`grep`) 하나와 `돌리지 않음` 줄 하나만 있는 `docs/tasks/plan.md`를 두고, 갈래 2에서만 `tool.py`와 그것을 시험하는 `tests/test_tool.py`를 더해 커밋한다. `claude -p`로 `/plate:review`를 맡기는 글 `부른 쪽: plate:run`과 함께 부르고, `--plugin-dir`에 작업 트리의 `plugins/plate`를, `--permission-mode bypassPermissions`를 준다. 기대: 갈래 1에서 `docs/tasks/review.md`의 테스트 적절성 근거 첫 줄이 결과물인 마크다운만 바뀐 경우의 표로 매겼다고 적고 등급이 A가 아니다. 갈래 2에서 근거 첫 줄이 기본 등급표로 매겼다고 적는다. 기록: 갈래마다 차림, 돌린 명령, 돌려받은 줄, 테스트 적절성 절 전문, 돌릴 때의 `git hash-object plugins/plate/skills/review/SKILL.md` 값

**통과 조건**
- 완료 조건 2가 참이다
  - 확인: `grep -cF -e '결과물인 마크다운, 실행 경로 없는 파일, 테스트 파일뿐이면' plugins/plate/skills/review/SKILL.md`가 `3`, `grep -cF -e '결과물인 마크다운과 실행 경로 없는 파일뿐이면' plugins/plate/skills/review/SKILL.md`가 `0`이다. 정의 글, `**테스트 파일**`, 5번의 두 글은 `grep -cF -e`로 저마다 `1`이다. `grep -cF -e '테스트 파일뿐이면' docs/ADR.md`가 `1`이다
  - 확인: 이 phase의 "한 일"에 적힌 두 갈래의 테스트 적절성 절이 TODO의 기대대로다. 적힌 해시가 지금 작업 트리의 `git hash-object plugins/plate/skills/review/SKILL.md`와 같다
- 테스트가 모두 통과하고, 고친 글이 빠지면 실패한다
  - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
  - 확인: 새 사본(`mktemp -d`로 만든 폴더에 작업 트리의 `plugins`와 `tests`를 `cp -R`로 복사한 것)에서 review 본문의 `테스트 파일은 바뀐 동작이 아니라 그 근거라 표를 고를 때 세지 않는다`가 한 번 있는지 보고, 빈 글로 바꿔 `python3 -m unittest discover -s tests`를 돌리면 출력에 `FAIL: test_70_test_files_do_not_pick_default_table (test_skill_rules.ReviewRulesTest`로 시작하는 줄이 있다
- 문서가 맞는다
  - 확인: `grep -F -e '테스트 파일도 빼고 표를 고름' docs/ARCHITECTURE.md`가 낸 줄이 `test_skill_rules.py`를 담는다. `sed -n '1,8p' tests/test_skill_rules.py`의 review 목록에 `#70`이 있다

## 한 일
- review 낱말에 `**테스트 파일**`: "실행 경로 없는 파일" 아래에 run의 정의와 같은 글(`` `.md`가 아닌 파일 가운데 `tests/`, `test/`, `__tests__/` 아래에 있거나 이름이 `test_*`, `*_test.*`, `*.test.*`, `*.spec.*` 꼴인 것 ``)에 "테스트 적절성의 표를 고를 때는 세지 않는다(5번)."를 붙여 더했다 (`plugins/plate/skills/review/SKILL.md`)
- 4번 범주 표, 5번 표 고르기 줄, PR 모드 등급 줄: 세 곳의 `결과물인 마크다운과 실행 경로 없는 파일뿐이면`을 `결과물인 마크다운, 실행 경로 없는 파일, 테스트 파일뿐이면`으로 바꿨다. 5번 표 고르기 줄에 "실행 경로 없는 파일(…)이나 테스트 파일이 함께 바뀌어도 이 표를 쓴다", `테스트 파일은 바뀐 동작이 아니라 그 근거라 표를 고를 때 세지 않는다`, "테스트 파일이 아닌 실행 코드가 하나라도 바뀌었으면 위 등급표로 매긴다"를 넣고, 그 아래 줄로 `테스트 적절성의 근거 첫 줄에 어느 표로 매겼는지 적는다(…)`를 더했다. "기록의 양식"의 테스트 적절성 첫 근거 줄로 `  - 근거: {기본 등급표 | 결과물인 마크다운만 바뀐 경우의 표}로 매김 — {그 표를 고른 까닭}`을 넣었다 (`plugins/plate/skills/review/SKILL.md`)
- ADR-024 트레이드오프의 괄호 안 글을 "바뀐 코드 파일이 결과물인 마크다운, 실행 경로 없는 파일(매니페스트의 버전 줄 같은 것), 테스트 파일뿐이면"으로 바꿨다 (`docs/ADR.md`)
- 새 `ReviewRulesTest.test_70_test_files_do_not_pick_default_table`: 낱말의 정의 글, 4번·5번·PR 모드 절마다 새 글이 있고 옛 글이 없음, 본문 전체에 옛 글이 없음, 5번의 두 글, 기록의 양식의 첫 근거 줄을 본다. 모듈 docstring의 review 목록을 `#51·#70`으로 바꿨다 (`tests/test_skill_rules.py`)
- 디렉터리 구조의 `test_skill_rules.py` 줄 규칙 목록 끝에 "review가 테스트 파일도 빼고 표를 고름, 근거 첫 줄에 쓴 표를 적음"을 더했다 (`docs/ARCHITECTURE.md`)
- review 헤드리스 시험 두 갈래
  - 차림: 시험 저장소를 만드는 스크립트(`/private/tmp/claude-501/-Users-hugo-Desktop-harness-plate/1901ca54-85e8-4207-af37-376e63109655/scratchpad/setup_review.sh <갈래>`)가 갈래마다 `mktemp -d`로 새 저장소를 만든다. `main`에 문서 지도에 `docs/ARCHITECTURE.md` 행과 `docs/tasks/` 행이 있는 `AGENTS.md`, `## 결과물인 마크다운` 절에 `- skills/*/SKILL.md`와 `## 명령` 절(설치·빌드·린트 없음, 테스트 `python3 -m unittest discover -s tests`)이 있는 `docs/ARCHITECTURE.md`, `skills/x/SKILL.md`(`사용자에게 "안녕"이라고 말한다.`), 그 글을 보는 `tests/test_x.py`를 커밋한다. `tasks/x` 브랜치에서 `skills/x/SKILL.md`에 `"안녕, {이름}"이라고 말한다` 규칙을, `tests/test_x.py`에 그 글을 보는 테스트를 더하고, 완료 조건 하나에 `` 확인: `grep -cF -e '"안녕, {이름}"이라고 말한다' skills/x/SKILL.md`가 `1` ``과 `돌리지 않음: 스킬을 헤드리스로 돌려 보지 않는다. 사용자가 정했다`만 있는 `docs/tasks/plan.md`(이름 `x`)와 같은 완료 조건의 task 머리 `docs/tasks/001-greet-name/plan.md`를 두고, 갈래 2에서만 `tool.py`(`greet(name=None)`)와 그것을 시험하는 `tests/test_tool.py`를 더해 커밋한다. 갈래 1 저장소 `/var/folders/0j/cj37rxmj1mj73vhflqpgsxm00000gn/T/tmp.xbyXsh0faD`, 갈래 2 저장소 `/var/folders/0j/cj37rxmj1mj73vhflqpgsxm00000gn/T/tmp.YQxWAydJFq`
  - 돌린 명령(갈래마다 그 저장소에서): `claude -p $'/plate:review\n부른 쪽: plate:run' --plugin-dir /Users/hugo/Desktop/harness-plate/plugins/plate --permission-mode bypassPermissions` (claude 2.1.312)
  - 돌릴 때의 `git hash-object plugins/plate/skills/review/SKILL.md`: `82c5234e494bc39eb3f414cdb1088d8ea3dc4a83`
  - 갈래 1 돌려받은 줄: `등급: 신뢰성 A, 보안 A, 유지보수성 A, 테스트 적절성 D, 기능 적합성 A` / `게이트: 통과` / `문제: 0개` / `기록: docs/tasks/review.md` (커밋 `x: 코드 평가`)
  - 갈래 1 `docs/tasks/review.md`의 테스트 적절성 절 전문:
    ```
    - 테스트 적절성
      - 근거: 결과물인 마크다운만 바뀐 경우의 표로 매김 — 바뀐 코드 파일이 결과물인 마크다운(`skills/x/SKILL.md`)과 테스트 파일(`tests/test_x.py`)뿐이다
      - 근거: 바뀐 동작은 하나(이름을 알려 주면 "안녕, {이름}"이라고 인사한다). tasks 머리와 task 머리(`docs/tasks/001-greet-name/plan.md:11-12`)의 완료 조건에 그 동작의 확인은 본문을 grep하는 읽기만 하는 확인과 `돌리지 않음` 줄뿐이고, 스킬을 실제로 돌려 보는 확인이 없다. `tests/test_x.py:11-12`도 본문의 글을 보는 테스트다
      - 등급: D — 돌려 보는 확인이 하나도 없고 읽기만 하는 확인과 `돌리지 않음` 줄뿐이다
    ```
  - 갈래 2 돌려받은 줄: `등급: 신뢰성 A, 보안 A, 유지보수성 A, 테스트 적절성 A, 기능 적합성 A` / `게이트: 실패` / `문제: 1개` / `기록: docs/tasks/review.md` (커밋 `x: 코드 평가`)
  - 갈래 2 `docs/tasks/review.md`의 테스트 적절성 절 전문:
    ```
    - 테스트 적절성
      - 근거: 기본 등급표로 매김 — 테스트 파일이 아닌 실행 코드 `tool.py`가 바뀌었다
      - 근거: `tests/test_tool.py:10-14` 이름이 없을 때와 있을 때의 `greet`를 모두 시험하고, 어느 갈래가 깨져도 `assertEqual`이 실패한다
      - 근거: `tests/test_x.py:11-12` 스킬 본문에 새 규칙의 글이 없어지면 실패한다
      - 근거: 빈 문자열 이름(`greet("")`)은 테스트가 없지만 엣지케이스다. 커버리지 94.4%
      - 등급: A — 새 줄 커버리지 90% 이상이고, 바뀐 동작마다 깨지면 실패할 테스트가 있다
    ```

## 확인 결과
- 완료 조건 2가 참이다
  - `grep -cF -e '결과물인 마크다운, 실행 경로 없는 파일, 테스트 파일뿐이면' plugins/plate/skills/review/SKILL.md` → `3`, `grep -cF -e '결과물인 마크다운과 실행 경로 없는 파일뿐이면' …` → `0`, 정의 글 → `1`, `**테스트 파일**` → `1`, `테스트 파일은 바뀐 동작이 아니라 그 근거라 표를 고를 때 세지 않는다` → `1`, `테스트 적절성의 근거 첫 줄에 어느 표로 매겼는지 적는다` → `1`, `grep -cF -e '테스트 파일뿐이면' docs/ADR.md` → `1`. 통과
  - "한 일"의 두 갈래: 갈래 1 근거 첫 줄이 "결과물인 마크다운만 바뀐 경우의 표로 매김"이고 등급 D(A 아님), 갈래 2 근거 첫 줄이 "기본 등급표로 매김". 적힌 해시 `82c5234e494bc39eb3f414cdb1088d8ea3dc4a83`가 지금 `git hash-object plugins/plate/skills/review/SKILL.md`와 같다. 통과
- 테스트가 모두 통과하고, 고친 글이 빠지면 실패한다
  - `python3 -m unittest discover -s tests` → `Ran 197 tests` … 마지막 줄 `OK`. 통과
  - 새 사본(`mktemp -d`의 `/var/folders/0j/cj37rxmj1mj73vhflqpgsxm00000gn/T/tmp.0x8PwWeQj0`에 `plugins`, `tests`를 `cp -R`)에서 그 글이 `1`번 있음을 보고 빈 글로 바꿔 돌림 → `FAIL: test_70_test_files_do_not_pick_default_table (test_skill_rules.ReviewRulesTest) (key='테스트 파일은 바뀐 동작이 아니라 그 근거라 표를 고를 때 세지 않는다')`, `FAILED (failures=1)`. 통과
- 문서가 맞는다
  - `grep -F -e '테스트 파일도 빼고 표를 고름' docs/ARCHITECTURE.md`가 낸 한 줄에 `test_skill_rules.py`가 든다. `sed -n '1,8p' tests/test_skill_rules.py`의 4번째 줄에 `review의 #51·#70`. 통과

## 계획과 달라진 점
- 시험 저장소에 TODO에 적힌 것 말고 task 머리 `docs/tasks/001-greet-name/plan.md`(tasks 머리와 같은 완료 조건)와 문서 지도의 `docs/tasks/` 행을 더 두었다. review 1번이 task 폴더마다의 task 머리를 읽으라 해, tasks 머리의 task 목록이 가리키는 폴더가 없으면 평가가 그 빈칸에 걸릴 수 있어서다. 기대(테스트 적절성의 표 고르기)는 바꾸지 않았다

## 남은 것
- 갈래 2의 게이트가 실패(새 문제 1개)다. 시험 저장소의 코드에서 나온 것이고 테스트 적절성의 표 고르기와는 상관없어 보지 않았다
- 테스트 파일의 판별은 경로·이름 꼴로만 한다. `tests/` 아래의 도우미(`conftest.py`, 픽스처 모듈 같은 것)도 테스트 파일로 세어, 그것만 바뀌어도 결과물인 마크다운만 바뀐 경우의 표로 간다

## 하네스에서 걸린 것
- 없음
