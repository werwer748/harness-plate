# 회고

## 회고 1

**확인**
- 1. #69: phase·check·retro 본문의 확인을 돌리는 절에 고침 규칙이 있다
  - `grep -cF -e '<글>' <파일>`을 phase 글 셋(`plugins/plate/skills/phase/SKILL.md`), check 글 넷(`plugins/plate/skills/check/SKILL.md`), retro 글 넷(`plugins/plate/skills/retro/SKILL.md`)마다 돌림 → 열한 번 모두 `1`. 통과
  - `done-phase-1.md` "한 일"의 check 헤드리스 시험을 읽음 → 차림의 조건 1은 `grep -F '- abc' f.txt`, 조건 2는 `grep -F 'abc' nofile.txt`. 더해진 `## 확인 1`에서 조건 1의 줄은 통과, "하네스에서 걸린 것"에 적힌 명령 `grep -F '- abc' f.txt`와 고친 명령 `grep -F -e '- abc' f.txt`가 함께 있음, 조건 2의 줄은 실패, 판정은 실패. 적힌 해시 `24447065aed4abec74deb384330d05f80ab79ee8`와 지금 `git hash-object plugins/plate/skills/check/SKILL.md` → `24447065aed4abec74deb384330d05f80ab79ee8`로 같음. 통과
- 2. #70: review 본문의 테스트 파일 낱말과 표 고르기 글, ADR-024 트레이드오프
  - `grep -cF -e '결과물인 마크다운, 실행 경로 없는 파일, 테스트 파일뿐이면' plugins/plate/skills/review/SKILL.md` → `3`, `grep -cF -e '결과물인 마크다운과 실행 경로 없는 파일뿐이면' plugins/plate/skills/review/SKILL.md` → `0`, 정의 글 → `1`, `**테스트 파일**` → `1`, `테스트 파일은 바뀐 동작이 아니라 그 근거라 표를 고를 때 세지 않는다` → `1`, `테스트 적절성의 근거 첫 줄에 어느 표로 매겼는지 적는다` → `1`, `grep -cF -e '테스트 파일뿐이면' docs/ADR.md` → `1`. 통과
  - `done-phase-2.md` "한 일"의 review 헤드리스 시험 두 갈래를 읽음 → 갈래 1(바뀐 코드 파일 `skills/x/SKILL.md`, `tests/test_x.py`, 완료 조건은 읽기만 하는 `grep` 확인과 `돌리지 않음` 줄)의 근거 첫 줄 "결과물인 마크다운만 바뀐 경우의 표로 매김", 등급 D(A 아님). 갈래 2(`tool.py`도 바뀜)의 근거 첫 줄 "기본 등급표로 매김". 적힌 해시 `82c5234e494bc39eb3f414cdb1088d8ea3dc4a83`와 지금 `git hash-object plugins/plate/skills/review/SKILL.md` → `82c5234e494bc39eb3f414cdb1088d8ea3dc4a83`로 같음. 통과
- 3. #68: plan 본문 절대 규칙 3, 6번 점검 목록, 적는 규칙 "조건"
  - `grep -cF -e '<글>' plugins/plate/skills/plan/SKILL.md` → 옛 글 `0`, 새 글 다섯(절대 규칙 3의 글, `읽기만 하는 확인 명령(파일이나 저장소를 바꾸지 않는 것)을 돌려 적힌 그대로 도는지 본다`, `결과값은 견주지 않는다`, `쓰는 명령은 돌리지 않고 같은 꼴을 글로 본다`, `확인 명령은 적힌 그대로 돌게 적는다`) 저마다 `1`. 통과
  - `grep -F -e '- 확인은 돌릴 명령과 기대 결과를 우선한다.' plugins/plate/skills/plan/SKILL.md` → 한 줄, 그 줄에 `확인 명령은 적힌 그대로 돌게 적는다`가 듦(`grep -cF` `1`). 통과
- 4. 고친 글이 빠지면 실패하는 테스트가 있고, 모든 테스트가 통과한다
  - `python3 -m unittest discover -s tests` → `Ran 198 tests in 16.950s`, 마지막 줄 `OK`. 통과
  - 다섯 시험을 저마다 `mktemp -d`의 새 폴더에 작업 트리의 `plugins`와 `tests`를 `cp -R`한 사본에서 함 → 다섯 글 모두 사본 파일에 `1`번 있고, 빈 글로 바꿔 `python3 -m unittest discover -s tests`를 돌린 출력에 `FAIL: test_69_fix_check_command_and_record (test_skill_rules.PhaseRulesTest`, `FAIL: test_69_run_check_as_written (test_skill_rules.CheckRulesTest`, `FAIL: test_69_run_check_as_written (test_skill_rules.RetroRulesTest`, `FAIL: test_70_test_files_do_not_pick_default_table (test_skill_rules.ReviewRulesTest`, `FAIL: test_68_check_commands_run_as_written (test_skill_rules.PlanRulesTest`가 저마다 있음. 통과
- 5. 두 매니페스트의 버전이 0.21.0이고, 마켓플레이스가 유효하고, 문서와 테스트 설명이 바뀐 규칙과 맞는다
  - `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "0.21.0",`. 통과
  - `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
  - `docs/ARCHITECTURE.md`의 `test_skill_rules.py` 줄 → `적힌 그대로 돌지 않는 확인 명령`, `테스트 파일도 빼고 표를 고름`, `읽기만 하는 확인 명령을 초안 점검에서 돌림` 저마다 듦. 통과
  - `sed -n '1,8p' tests/test_skill_rules.py` → `plan의 …·#65·#68`, `phase의 #42·#51·#69`, `check의 #51·#69`, `retro의 #49·#50·#51·#69`, `review의 #51·#70`. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 198 tests`, `OK`. 통과

**남은 것**
- phase 1: phase와 retro의 고침 규칙은 헤드리스로 돌려 보지 않았다 → 문제 아님 (task 머리 완료 조건 1의 `돌리지 않음` 줄과 tasks 머리의 결정 "헤드리스로 돌려 보는 확인은 check와 review만 둔다"가 돌리지 않기로 정한 동작이다. 두 본문의 고침 규칙 글을 직접 읽어 check의 것과 같은 꼴이고 phase는 더 큰 고침에서 "계획이 틀림"으로 가는 것을 봤다)
- phase 1: check의 헤드리스 시험은 `-e`를 붙이는 꼴 하나만 봤고 따옴표가 어긋난 명령과 "바꿔야 돌면 실패"의 갈래는 돌려 보지 않았다 → 문제 아님 (check 2번의 바뀐 글을 직접 읽음: 따옴표 맞추기를 허용하는 고침에 넣고 대상·패턴·기대를 바꿔야 돌면 실패라 적어 결정대로다. 동작이 틀리는 곳을 찾지 못했다)
- phase 2: 갈래 2 시험 저장소의 게이트 실패(새 문제 1개)는 보지 않았다 → 문제 아님 (시험 저장소의 코드에서 나온 것이고 완료 조건 2가 보는 표 고르기와 근거 첫 줄과 상관없다)
- phase 2: 테스트 파일의 판별이 경로·이름 꼴뿐이라 `tests/` 아래의 도우미(`conftest.py`, 픽스처 모듈)도 테스트 파일로 센다 → 문제 아님 (tasks 머리의 결정 "테스트 파일의 정의는 run·plan의 것과 같다"대로이고, review 낱말의 정의 글이 run·plan의 것과 같음을 `grep -rnoF`로 봤다(`plan/SKILL.md:32`, `review/SKILL.md:36`, `run/SKILL.md:57`))
- phase 3: plan의 바뀐 6번 점검대로 초안이 점검되는지는 돌려 보지 않았다 → 문제 아님 (task 머리 완료 조건 3의 `돌리지 않음` 줄이 돌리지 않기로 정한 동작이다. 바뀐 절대 규칙 3, 6번 항목, 명령 예 항목의 괄호 글을 직접 읽어 서로 어긋나지 않음을 봤다)

**문제**
없음

**판정**: 통과
