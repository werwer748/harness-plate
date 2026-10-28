# 회고

## 회고 1

**확인**
- 1. run 3번 "상태를 읽는 법"의 `awk` 명령과 "글을 넘기는 법"의 작은따옴표 넘기기를 시험 파일에 본문의 `awk`를 돌리는 테스트와 가짜 `gh`에 따옴표·백틱·`$(…)`가 든 제목을 넘기는 테스트로 남긴다
  - `tests/test_skill_rules.py`의 `test_state_reading_awk_runs_on_trap_files`, `test_text_passing_rule_survives_fake_gh`를 읽음 → 둘 다 run 본문에서 명령(`awk -v h='확인' …` 줄, `'{…}'`가 든 `gh` 명령 셋)과 바꾸는 글(`'\''`)을 뽑아 `tempfile.TemporaryDirectory()`에서 `sh -c`로 돌린다. 통과
  - `python3 -m unittest tests.test_skill_rules -k awk_runs -k fake_gh -v` → `Ran 2 tests`, `OK`. 통과
  - `python3 -m unittest discover -s tests` → `Ran 192 tests`, `OK`. 통과
  - 스크래치에 `git ls-files`를 베낀 사본 셋에서 run 본문을 바꿔 `python3 -m unittest tests.test_skill_rules`: m1(`f != "" { next }` → `f != "" { }`) → `test_state_reading_awk_runs_on_trap_files` 세 case 실패, `FAILED (failures=3)`. m2(`$0 ~ ("^## " h " [0-9]+$")` → `$0 ~ ("## " h " [0-9]+")`) → 같은 테스트 `phase_with_traps`와 `test_state_reading_and_stop_line_rows` 실패, `FAILED (failures=2)`. m3(`'\''`·`'it'\''s'` → `\'`·`'it\'s'`) → `test_text_passing_rule_survives_fake_gh` 세 template과 `test_text_passing_rule_in_one_place` 실패, `FAILED (failures=4)`. 통과
- 2. heredoc 도구 동작을 확인한 버전과 함께 `docs/TOOLS.md`의 `## Claude Code` 첫 목록에 한 줄로 남긴다
  - `grep -c 'Non-UTF-8' docs/TOOLS.md` → 1. 통과
  - `wc -c < docs/TOOLS.md` → 14527(≤ 15360). 통과
  - `git show 2e49f53 -- docs/TOOLS.md` → 줄이 `## Claude Code` 첫 목록의 `git clone` 줄 앞에 `(2.1.312)`와 함께 더해짐. 통과
- 3. tasks 완료 조건 1, 2, 3, 4가 참이다
  - 1: `python3 -m unittest discover -s tests` → `OK`. 통과
  - 2: `wc -c < docs/TOOLS.md` → 14527. 통과
  - 2: 네 절 이름마다 `grep -c '<절 이름>' docs/TOOLS.md` → 1, 1, 1, 1. 통과
  - 2: `grep -cE '/var/folders/|tmp\.[A-Za-z0-9]{6,}|장면 [A-Z]' docs/TOOLS.md` → 0. 통과
  - 3: `git grep -n 'TOOLS.md' -- plugins/` → 출력 없음(종료 1). 통과
  - 3: `git grep -nE '사용량.*TOOLS\.md|TOOLS\.md.*사용량' -- docs/PRD.md docs/ARCHITECTURE.md docs/ADR.md README.md AGENTS.md` → 출력 없음(종료 1). 통과
  - 4: `grep -c '처리: plan으로 넘김' docs/cleanup/2026-10-28.md` → 29. 보고서의 `- **{기준}-N**` 머리 아래 `처리: plan으로 넘김` 번호와 세 task 머리 `## 완료 조건`의 발견 번호를 뽑아 견준 스크립트 → `29 29 True []`. 통과
  - 4: `001-tools-doc`, `002-run-rules`, `003-plan-rules`의 `retro.md` 마지막 회고 절(`## 회고 1`)의 판정 → 셋 다 `**판정**: 통과`. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 192 tests in 17.072s`, `OK`. 통과

**남은 것**
- phase 1: `test_text_passing_rule_survives_fake_gh`는 `'{…}'` 자리만 제목으로 채우고 `--body-file` 넘기기와 임시 파일 지우기는 돌려 보지 않는다 → 문제 아님 (완료 조건 1과 review 소스 문제 1이 정한 것은 제목·검색어의 작은따옴표 넘기기이고, 이 task는 본문 넘기기를 바꾸지 않았다)
- phase 1: `awk` 테스트를 BSD awk(20200816)에서만 돌렸다 → 문제 아님 (이 환경에 gawk·mawk가 없어 돌리지 못했다. run 본문의 `awk`를 읽어 보니 `match`·`RLENGTH`·`substr`·동적 정규식 `$0 ~ (…)`·`printf`만 쓰는 POSIX awk의 꼴이고, 이 task는 그 명령을 바꾸지 않고 테스트만 더했다)
- phase 1: `docs/TOOLS.md` heredoc 줄의 2.1.312는 이 세션의 버전이고 `002-run-rules`에서 깨졌을 때의 버전인지 확인하지 못했다 → 문제 아님 (줄이 "깨질 수 있다", "늘 깨지지는 않아 같은 꼴이 돈 때도 있다(2.1.312)"로 확인한 만큼만 적었고, 완료 조건 2는 확인한 버전을 붙이라고만 한다. `claude --version` → 2.1.312로 같다)

**문제**
- 없음

**판정**: 통과
