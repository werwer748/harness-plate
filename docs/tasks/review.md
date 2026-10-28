# 코드 평가

## 평가 1

**대상**
- 범위: `1439f62`(main에서 갈라진 곳)부터 `e8ea82d`까지
- 결과물인 마크다운 절: `plugins/plate/skills/*/SKILL.md`
- 바뀐 코드 파일 8개, 새 줄 89줄, 잴 새 줄 71줄
  - `plugins/plate/.claude-plugin/plugin.json` +1
  - `plugins/plate/.codex-plugin/plugin.json` +1
  - `tests/test_skill_rules.py` +69
  - `plugins/plate/skills/check/SKILL.md` +3 (결과물인 마크다운)
  - `plugins/plate/skills/phase/SKILL.md` +2 (결과물인 마크다운)
  - `plugins/plate/skills/plan/SKILL.md` +4 (결과물인 마크다운)
  - `plugins/plate/skills/retro/SKILL.md` +3 (결과물인 마크다운)
  - `plugins/plate/skills/review/SKILL.md` +6 (결과물인 마크다운)

**잰 것**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 198 tests in 16.836s` / `OK`. 통과
- 커버리지: 측정 못함 — `python3 -c "import coverage"` → `ModuleNotFoundError: No module named 'coverage'`. 명령 절도 커버리지 도구를 두지 않는다(ADR-024)
- 중복: 측정 못함 — `which jscpd` → `jscpd not found`. 명령 절도 중복 도구를 두지 않는다(ADR-024)
- 정적 분석: `python3 -m py_compile tests/test_skill_rules.py` → 오류 없음. `python3 -m pyflakes` → `No module named pyflakes`(측정 못함). 바뀐 코드 파일에 걸린 결과 없음
- 보안 검사: 측정 못함 — `which bandit semgrep pip-audit` → 셋 모두 `not found`. 의존성 목록도 없다(ADR-024)

**완료 조건**
- 1. #69: phase·check·retro 본문의 확인을 돌리는 절에 고침 규칙이 있다
  - `grep -cF -e '<글>' <파일>`을 phase 글 셋, check 글 넷, retro 글 넷마다 돌림 → 열한 개 모두 `1`. 통과
  - `done-phase-1.md` "한 일"의 check 헤드리스 시험을 읽음 → `## 확인 1`에서 조건 1 `grep -F -e '- abc' f.txt` 통과, "하네스에서 걸린 것"에 적힌 명령 `grep -F '- abc' f.txt`와 고친 명령 `grep -F -e '- abc' f.txt`가 함께 있음, 조건 2 실패, 판정 실패. 적힌 해시 `24447065aed4abec74deb384330d05f80ab79ee8`가 지금 `git hash-object plugins/plate/skills/check/SKILL.md`와 같음. 통과
- 2. #70: review 본문의 낱말에 `**테스트 파일**`이 있고 표 고르기에서 테스트 파일을 세지 않는다
  - `grep -cF -e '결과물인 마크다운, 실행 경로 없는 파일, 테스트 파일뿐이면' plugins/plate/skills/review/SKILL.md` → `3`, 옛 글 → `0`, 정의 글·`**테스트 파일**`·5번의 두 글 → 저마다 `1`, `grep -cF -e '테스트 파일뿐이면' docs/ADR.md` → `1`. 통과
  - `done-phase-2.md` "한 일"의 review 헤드리스 시험 두 갈래를 읽음 → 갈래 1 근거 첫 줄 "결과물인 마크다운만 바뀐 경우의 표로 매김", 등급 D(A 아님). 갈래 2 근거 첫 줄 "기본 등급표로 매김". 적힌 해시 `82c5234e494bc39eb3f414cdb1088d8ea3dc4a83`가 지금 `git hash-object plugins/plate/skills/review/SKILL.md`와 같음. 통과
- 3. #68: plan 본문이 읽기만 하는 확인 명령을 초안 점검에서 돌린다
  - 옛 글 `grep -cF -e` → `0`, 새 글 다섯 → 저마다 `1`. 통과
  - `grep -F -e '- 확인은 돌릴 명령과 기대 결과를 우선한다.' plugins/plate/skills/plan/SKILL.md` → 한 줄이고 그 줄에 `확인 명령은 적힌 그대로 돌게 적는다`가 듦. 통과
- 4. 고친 글이 빠지면 실패하는 테스트가 있고, 모든 테스트가 통과한다
  - `python3 -m unittest discover -s tests` → 마지막 줄 `OK`. 통과
  - 다섯 시험을 저마다 `tempfile.mkdtemp()`로 만든 새 사본(작업 트리의 `plugins`와 `tests`를 `shutil.copytree`로 복사)에서 함 → 다섯 글 모두 사본에 한 번 있고, 빈 글로 바꿔 돌린 출력에 `FAIL: test_69_fix_check_command_and_record (test_skill_rules.PhaseRulesTest`, `FAIL: test_69_run_check_as_written (test_skill_rules.CheckRulesTest`, `FAIL: test_69_run_check_as_written (test_skill_rules.RetroRulesTest`, `FAIL: test_70_test_files_do_not_pick_default_table (test_skill_rules.ReviewRulesTest`, `FAIL: test_68_check_commands_run_as_written (test_skill_rules.PlanRulesTest`가 저마다 있음. 통과
- 5. 두 매니페스트의 버전이 0.21.0이고, 마켓플레이스가 유효하고, 문서와 테스트 설명이 바뀐 규칙과 맞는다
  - `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "0.21.0",`. 통과
  - `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
  - `docs/ARCHITECTURE.md`의 `test_skill_rules.py` 줄에 세 글을 `grep -cF -e`로 봄 → 저마다 `1`. 통과
  - `sed -n '1,8p' tests/test_skill_rules.py` → plan의 `#68`, phase·check·retro의 `#69`, review의 `#70`이 있음. 통과

**범주**
- 신뢰성
  - 근거: 새 줄 89줄을 모두 읽고 그 파일 전체와 맥락 문서에 댐. `plugins/plate/skills/phase/SKILL.md:63,70`의 고침 규칙과 2번 "계획이 틀림" 갈래, `plugins/plate/skills/check/SKILL.md:46,123`의 판정·기록 자리, `plugins/plate/skills/retro/SKILL.md:56,87`의 확인 결과와 5번 문제 모음, `plugins/plate/skills/plan/SKILL.md:18,110,251,257`의 절대 규칙·6번 점검·적는 규칙, `plugins/plate/skills/review/SKILL.md:36,90,124-125,199,260`의 정의·표 고르기·PR 모드·양식이 서로 어긋나지 않음. 헤드리스 시험 두 기록(check, review)이 바뀐 규칙대로 돌았고, 테스트 198개가 통과함. 문제 없음
  - 등급: A — 문제 0개
- 보안
  - 핫스팟: 없음. 바뀐 실행 코드는 `tests/test_skill_rules.py`의 본문 읽기와 글 견주기뿐이고 셸 실행, 밖의 입력, 비밀이 없음
  - 근거: 없음. 매니페스트는 버전 줄만 바뀜
  - 등급: A — 문제 0개
- 유지보수성
  - 근거: 바뀐 규칙 글은 이웃 규칙과 같은 문체·위치(그 절의 문단이나 목록 항목)이고, 새 테스트(`tests/test_skill_rules.py:603-617,711-738,762-792`)는 기존 `section`·`part`·`subTest` 꼴을 따름. ARCHITECTURE와 ADR-024, 모듈 docstring이 바뀐 규칙에 맞춰짐. 문제 없음
  - 부채 비율: 0분 ÷ (89줄 × 30분) = 0%
  - 등급: A — 부채 비율 5% 이하
- 테스트 적절성
  - 근거: 결과물인 마크다운만 바뀐 경우의 표로 매김 — 바뀐 코드 파일이 결과물인 마크다운(스킬 본문 다섯), 실행 경로 없는 파일(두 매니페스트의 `"version"` 줄), 테스트 파일(`tests/test_skill_rules.py`)뿐이다. 커버리지는 보지 않음
  - 근거: 바뀐 동작은 다섯(phase·check·retro의 확인 명령 고침 규칙, review의 표 고르기, plan의 초안 점검 돌리기)
  - 근거: `docs/tasks/plan.md:20` check의 고침 규칙은 헤드리스로 돌려 보는 확인이 있음
  - 근거: `docs/tasks/plan.md:24` review의 표 고르기는 두 갈래를 헤드리스로 돌려 보는 확인이 있음
  - 근거: `docs/tasks/plan.md:19,21` phase와 retro의 고침 규칙은 읽기만 하는 확인(`grep -cF`)과 `돌리지 않음` 줄뿐임
  - 근거: `docs/tasks/plan.md:26-28` plan의 초안 점검 규칙은 읽기만 하는 확인과 `돌리지 않음` 줄뿐임
  - 근거: 다섯 동작 가운데 셋(phase, retro, plan)에 돌려 보는 확인이 없음. 셋 모두 tasks 머리의 범위 밖과 결정(`docs/tasks/plan.md:12,42`)이 돌리지 않기로 정한 것이라 소스 문제로 적지 않음
  - 등급: D — 주된 동작의 절반 넘게(5개 가운데 3개) 돌려 보는 확인이 없다
- 기능 적합성
  - 근거: 완료 조건 1 통과: grep 열한 개와 check 헤드리스 기록·해시
  - 근거: 완료 조건 2 통과: grep과 review 헤드리스 두 갈래 기록·해시
  - 근거: 완료 조건 3 통과: 옛 글 0, 새 글 다섯, 적는 규칙 줄
  - 근거: 완료 조건 4 통과: 테스트 `OK`, 다섯 글을 지운 사본마다 해당 `FAIL:` 줄
  - 근거: 완료 조건 5 통과: 버전 0.21.0, `✔ Validation passed`, ARCHITECTURE 세 글, docstring의 `#68`·`#69`·`#70`
  - 등급: A — 완료 조건의 확인이 모두 통과한다

**Sonar way 게이트**
- 새 문제 0개: 0개. 통과
- 새 보안 핫스팟 모두 검토: 0/0. 통과
- 새 줄 커버리지 80% 이상: 잴 새 줄 71줄. 측정 못함
- 새 줄 중복 3% 이하: 잴 새 줄 71줄. 측정 못함
- 게이트: 통과

**소스 문제**
없음

**하네스에서 걸린 것**
- 테스트 적절성이 D인 것은 소스의 결함이 아니라 tasks 머리가 phase·retro·plan의 바뀐 동작을 헤드리스로 돌리지 않기로 정한 결과다(`docs/tasks/plan.md:12,21,28,42`). 결정이 정한 것이라 소스 문제로 적지 않았고, 표는 결정과 상관없이 칸을 매기게 돼 있어 등급에만 드러난다
- 완료 조건 4의 두 번째 확인은 `mktemp -d`와 `cp -R` 대신 같은 일을 하는 `tempfile.mkdtemp()`와 `shutil.copytree`로 사본을 만들어 돌렸다. 대상·패턴·기대는 같다
- ADR-024대로 커버리지·중복·보안 검사 도구가 없어 게이트의 커버리지와 중복이 측정 못함이다
