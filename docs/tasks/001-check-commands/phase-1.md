# Phase 1: phase·check·retro가 확인 명령을 적힌 그대로 돌린다 (#69)

**목표**: 완료 조건 1이 참이 되고, 그 글의 테스트와 check의 헤드리스 시험 기록이 있다.

**테스트 먼저**: 아니오 — 고치는 것은 스킬 본문(`.md`)이고, 더하는 테스트는 그 글이 있는지를 볼 뿐 코드의 동작을 바꾸지 않는다

**읽을 것**
- `gh issue view 69 --repo werwer748/harness-plate` (원인과 해결책)
- `plugins/plate/skills/phase/SKILL.md`의 "2. TODO를 차례로 끝낸다"(계획이 실제와 다를 때의 두 갈래), "3. 통과 조건의 확인을 모두 돌린다", 적는 규칙의 "하네스에서 걸린 것" 줄
- `plugins/plate/skills/check/SKILL.md`의 "2. 통과 조건의 확인을 모두 돌린다", "확인 절의 양식", 적는 규칙
- `plugins/plate/skills/retro/SKILL.md`의 "2. 완료 조건의 확인을 모두 돌린다", "5. tasks 끝에 볼 것을 모은다"의 문제 갈래, "회고 절" 양식
- `tests/test_skill_rules.py`의 모듈 docstring, `section`·`part` 도우미, `PhaseRulesTest`, `RetroRulesTest` (테스트의 꼴)
- `docs/TOOLS.md`의 "스킬을 헤드리스로 돌려 볼 때의 허용 목록"과 `--plugin-dir`·헤드리스 줄 (시험을 돌리는 법)
- `docs/ARCHITECTURE.md` 디렉터리 구조의 `test_skill_rules.py` 줄

**TODO**
- [ ] phase 3번 절에 완료 조건 1의 phase 글 셋이 더해진다. 적힌 그대로 돌지 않는다는 것이 옵션·문법 오류로 돌지 않는 것(`-`로 시작하는 패턴이 옵션으로 읽힌다, 따옴표가 어긋난다)이라는 것과 허용하는 고침(`-e`나 `--` 붙이기, 따옴표 맞추기)도 함께 적는다. 2번의 "그 밖의 차이" 예시에도 고쳐 돌린 확인 명령이 든다 (`plugins/plate/skills/phase/SKILL.md`)
- [ ] check 2번 절에 완료 조건 1의 check 글 넷이 더해진다. 확인 절 "통과 조건"의 결과 줄에 고쳐 돌렸으면 고친 명령을 적는다는 것도 적는다 (`plugins/plate/skills/check/SKILL.md`)
- [ ] retro 2번 절에 완료 조건 1의 retro 글 넷이 더해진다. 5번 문제 갈래의 "확인 명령이 돌지 않았다"와 같은 것을 시키게 맞춘다 (`plugins/plate/skills/retro/SKILL.md`)
- [ ] `PhaseRulesTest.test_69_fix_check_command_and_record`, 새 `CheckRulesTest.test_69_run_check_as_written`, `RetroRulesTest.test_69_run_check_as_written`이 더해진다. 저마다 그 본문의 그 절에 완료 조건 1의 글이 모두 있는지 본다. 모듈 docstring의 phase·check·retro 목록에 `#69`가 더해진다 (`tests/test_skill_rules.py`)
- [ ] 디렉터리 구조의 `test_skill_rules.py` 줄의 규칙 목록에 "phase·check·retro가 적힌 그대로 돌지 않는 확인 명령을 대상·패턴·기대를 바꾸지 않는 고침으로만 고쳐 돌리고 기록함"이 더해진다 (`docs/ARCHITECTURE.md`)
- [ ] check의 헤드리스 시험을 돌리고 이 phase의 "한 일"에 기록한다. 차림: `mktemp -d`로 만든 시험 저장소에 `git init`, 명령 절만 있고 네 줄이 모두 "없음"인 `docs/ARCHITECTURE.md`, `- abc` 줄이 있는 `f.txt`, `docs/tasks/001-x/plan.md`와 `phase-1.md`(계획 다섯 항목과 기록 다섯 절이 있고, 통과 조건은 둘: 조건 1 `grep -F '- abc' f.txt`가 한 줄을 낸다, 조건 2 `grep -F 'abc' nofile.txt`가 한 줄을 낸다)를 두고 커밋한다. 그 저장소에서 `claude -p`로 `/plate:check`를 맡기는 글 `task 폴더: docs/tasks/001-x`, `phase: 1`, `부른 쪽: plate:run`과 함께 부르고, `--plugin-dir`에 작업 트리의 `plugins/plate`를, `--permission-mode bypassPermissions`를 준다. 기대: 더해진 `## 확인 1`에서 조건 1은 통과이고 "하네스에서 걸린 것"에 적힌 명령과 `-e`나 `--`를 넣은 고친 명령이 함께 있으며, 조건 2는 실패이고 판정은 실패다. 기록: 차림, 돌린 명령, 돌려받은 세 줄, `## 확인 1` 절 전문, 돌릴 때의 `git hash-object plugins/plate/skills/check/SKILL.md` 값

**통과 조건**
- 완료 조건 1이 참이다
  - 확인: phase·check·retro의 글마다 `grep -cF -e '<글>' <파일>`이 `1`이다
  - 확인: 이 phase의 "한 일"에 적힌 헤드리스 시험의 `## 확인 1` 절에서 조건 1은 통과이고 "하네스에서 걸린 것"에 `grep -F '- abc' f.txt`와 `-e`나 `--`를 넣은 고친 명령이 함께 있으며, 조건 2는 실패이고 판정은 실패다. 적힌 해시가 지금 작업 트리의 `git hash-object plugins/plate/skills/check/SKILL.md`와 같다
- 테스트가 모두 통과하고, 고친 글이 빠지면 실패한다
  - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
  - 확인: 세 시험을 저마다 새 사본(`mktemp -d`로 만든 폴더에 작업 트리의 `plugins`와 `tests`를 `cp -R`로 복사한 것)에서 한다. 그 글이 사본의 파일에 한 번 있는지 보고, 빈 글로 바꿔 `python3 -m unittest discover -s tests`를 돌리면 출력에 그 줄로 시작하는 줄이 있다. phase 본문의 `고친 명령과 까닭을 "계획과 달라진 점"과 "하네스에서 걸린 것"에 적는다` → `FAIL: test_69_fix_check_command_and_record (test_skill_rules.PhaseRulesTest`, check 본문의 `적힌 명령, 고친 명령, 까닭을 "하네스에서 걸린 것"에 적는다` → `FAIL: test_69_run_check_as_written (test_skill_rules.CheckRulesTest`, retro 본문의 `적힌 명령, 고친 명령, 까닭을 "확인"의 결과에 적고 5번의 문제로 모은다` → `FAIL: test_69_run_check_as_written (test_skill_rules.RetroRulesTest`
- 문서가 맞는다
  - 확인: `grep -F -e '적힌 그대로 돌지 않는 확인 명령' docs/ARCHITECTURE.md`가 낸 줄이 `test_skill_rules.py`를 담는다. `sed -n '1,8p' tests/test_skill_rules.py`의 phase·check·retro 목록에 `#69`가 있다
