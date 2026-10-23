# 회고

## 회고 1

**확인**
- 명령 절의 정의가 설치, 빌드, 린트, 테스트 네 줄이 되고(없는 명령은 "없음"), plan이 명령 절을 챙길 때 설치 명령도 찾거나 묻는다. 설치 명령은 CI의 review만 돌리고 check, retro, tasks 끝의 review는 돌리지 않는다. 이 저장소의 명령 절에 `- 설치: 없음`이 있다.
  - `grep -n "설치" plugins/plate/skills/plan/SKILL.md plugins/plate/skills/check/SKILL.md plugins/plate/skills/retro/SKILL.md plugins/plate/skills/review/SKILL.md` → 네 파일 모두 명령 절 정의에 `` `- 설치: {명령}` ``으로 시작하는 네 줄 정의가 나온다(plan:29, check:29, retro:29, review:34). 그 밖에 plan:62, 76, 260, check:48, retro:60, review:62, 168, 175가 나온다. 통과
  - `grep -c "^- 설치: 없음$" docs/ARCHITECTURE.md` → `1`. 통과
  - `plugins/plate/skills/plan/SKILL.md`의 3번(62줄)과 5번(76줄), check 3번(48줄), retro 3번(60줄), review의 낱말(34줄)과 2번(62~68줄)과 PR 모드 절(168줄)을 읽음 → plan 3번은 설치, 빌드, 린트, 테스트 가운데 적히지 않은 것을 빌드 매니페스트와 코드에서 찾고 찾지 못한 것은 5번에서 묻는다. plan 5번은 "3번에서 찾지 못한 명령(설치, 빌드, 린트, 테스트)도 여기서 묻는다". check 3번과 retro 3번에 "설치는 돌리지 않는다"가 있다. review 2번의 1은 빌드, 린트, 테스트만 돌리고 낱말에 "tasks 끝의 코드 평가는 설치를 돌리지 않는다"가 있으며, 설치를 돌리는 곳은 PR 모드 절의 "설치한다"뿐이다. 통과
- review를 PR 모드로 부르면 tasks 머리 없이, 기준 브랜치에서 갈라진 곳부터 바뀐 코드 파일만 평가한다. 재기 전에 명령 절의 설치 명령을 돌리고, 명령 절, 커버리지, 네 범주(신뢰성, 보안, 유지보수성, 테스트 적절성), 게이트를 매기며, 기능 적합성은 매기지 않는다. 평가서를 파일로 쓰고, 판정 스크립트가 읽을 등급 묶음을 구조화 출력으로 돌려주며, 커밋하지 않고 묻지 않는다. tasks 끝의 코드 평가 절차는 바뀌지 않는다.
  - `plugins/plate/skills/review/SKILL.md`의 "PR 모드" 절(150~190줄)을 읽음 → 받는 것(`PR 모드`, 기준 브랜치, 평가서 파일)과 갈라진 곳 `git merge-base <기준 브랜치> HEAD`부터 바뀐 코드 파일과 새 줄을 센다(158줄), 0번의 조건을 보지 않고 tasks 머리와 task 머리를 읽지 않는다(165, 167줄), 재기 전에 설치 명령을 돌린다(168줄), 2번대로 명령 절·커버리지·중복·정적 분석·보안 검사를 잰다(169줄), 네 범주를 매기고 기능 적합성은 매기지 않는다(171줄), 6번대로 게이트를 본다(172줄), 받은 경로에 평가서를 새로 쓴다(173줄), 커밋하지 않고 고치지 않고 묻지 않는다(177줄), 등급 묶음 JSON을 구조화 출력으로 돌려준다(178줄). 등급 묶음의 키(`build`, `lint`, `test`, `coverage`, `reliability`, `security`, `maintainability`)와 값의 표가 있다(184~190줄). 통과
  - `git diff "$(git log --format=%h -1 --grep='^001-ci-review: phase 1$')^" -- plugins/plate/skills/review/SKILL.md`(기준 `f7dbd2a^`) → 바뀐 곳은 description, 머리말 한 줄(12줄), 절대 규칙 1과 5, 낱말의 명령 절 정의(34줄), 9번 뒤에 더한 "PR 모드" 절이다. `## 0.`~`## 9.` 절 안에는 변경이 없다. 통과
- 판정 스크립트가 등급 묶음을 받아 세 규칙대로 자동 머지, 머지 요청, 닫기 가운데 하나를 낸다. 커버리지가 "보지 않음"이면 다른 조건이 맞을 때 자동 머지를 막지 않는다. `docs/ARCHITECTURE.md`의 디렉터리 구조에 판정 스크립트와 그 테스트가 적혀 있다.
  - `python3 -m unittest discover -s tests` → `Ran 53 tests in 17.040s` / `OK`(종료 코드 0). 통과
  - `tests/test_verdict.py`를 읽음 → 커버리지 79·79.9는 request, 80·80.0은 merge(`CoverageTest.test_boundary_79_and_80`). 신뢰성·보안·유지보수성의 A는 merge, B는 request(`GradeTest.test_a_merges_b_requests`). 보안 B는 request, C·D·E는 close(`GradeTest.test_security_b_requests_c_and_below_close`). 모름은 빌드·린트·테스트의 `"unmeasured"`와 세 등급의 `"unjudged"`가 request(`UnknownTest` 두 테스트), 커버리지 `"unmeasured"`가 request(`CoverageTest.test_coverage_unmeasured_requests`). 빌드·린트·테스트의 `"fail"`은 close(`CloseTest.test_failed_command_closes`). 커버리지 `"skipped"`에서 다른 조건이 맞으면 merge(`MergeTest.test_coverage_skipped_does_not_block_merge`). `python3 -m unittest tests.test_verdict -v` → 14개 모두 `ok`. 통과
  - `docs/ARCHITECTURE.md`의 디렉터리 구조를 읽음 → `plugins/plate/` 아래 `ci/verdict.py`(판정 스크립트, 17줄)와 `tests/` 아래 `test_verdict.py`(판정 스크립트의 테스트, 33줄)가 있다. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 53 tests in 17.040s` / `OK`(종료 코드 0). 통과
- 테스트 먼저 기록: phase 3
  - `done-phase-3.md`의 "한 일"의 테스트 먼저 → 실패 출력(`verdict.py`가 없어 test_verdict의 27개가 `AssertionError: 종료 코드 2: ... No such file or directory`로 실패, `Ran 53 tests` / `FAILED (failures=27)`)이 먼저, 통과 출력(`Ran 53 tests in 15.921s` / `OK`)이 뒤에 있다. 27은 테스트 14개의 subTest를 따로 센 실패 수와 맞는다. 통과

**문제**
- 없음

**판정**: 통과
