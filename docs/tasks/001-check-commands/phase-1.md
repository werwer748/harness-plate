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
- [x] phase 3번 절에 완료 조건 1의 phase 글 셋이 더해진다. 적힌 그대로 돌지 않는다는 것이 옵션·문법 오류로 돌지 않는 것(`-`로 시작하는 패턴이 옵션으로 읽힌다, 따옴표가 어긋난다)이라는 것과 허용하는 고침(`-e`나 `--` 붙이기, 따옴표 맞추기)도 함께 적는다. 2번의 "그 밖의 차이" 예시에도 고쳐 돌린 확인 명령이 든다 (`plugins/plate/skills/phase/SKILL.md`)
- [x] check 2번 절에 완료 조건 1의 check 글 넷이 더해진다. 확인 절 "통과 조건"의 결과 줄에 고쳐 돌렸으면 고친 명령을 적는다는 것도 적는다 (`plugins/plate/skills/check/SKILL.md`)
- [x] retro 2번 절에 완료 조건 1의 retro 글 넷이 더해진다. 5번 문제 갈래의 "확인 명령이 돌지 않았다"와 같은 것을 시키게 맞춘다 (`plugins/plate/skills/retro/SKILL.md`)
- [x] `PhaseRulesTest.test_69_fix_check_command_and_record`, 새 `CheckRulesTest.test_69_run_check_as_written`, `RetroRulesTest.test_69_run_check_as_written`이 더해진다. 저마다 그 본문의 그 절에 완료 조건 1의 글이 모두 있는지 본다. 모듈 docstring의 phase·check·retro 목록에 `#69`가 더해진다 (`tests/test_skill_rules.py`)
- [x] 디렉터리 구조의 `test_skill_rules.py` 줄의 규칙 목록에 "phase·check·retro가 적힌 그대로 돌지 않는 확인 명령을 대상·패턴·기대를 바꾸지 않는 고침으로만 고쳐 돌리고 기록함"이 더해진다 (`docs/ARCHITECTURE.md`)
- [x] check의 헤드리스 시험을 돌리고 이 phase의 "한 일"에 기록한다. 차림: `mktemp -d`로 만든 시험 저장소에 `git init`, 명령 절만 있고 네 줄이 모두 "없음"인 `docs/ARCHITECTURE.md`, `- abc` 줄이 있는 `f.txt`, `docs/tasks/001-x/plan.md`와 `phase-1.md`(계획 다섯 항목과 기록 다섯 절이 있고, 통과 조건은 둘: 조건 1 `grep -F '- abc' f.txt`가 한 줄을 낸다, 조건 2 `grep -F 'abc' nofile.txt`가 한 줄을 낸다)를 두고 커밋한다. 그 저장소에서 `claude -p`로 `/plate:check`를 맡기는 글 `task 폴더: docs/tasks/001-x`, `phase: 1`, `부른 쪽: plate:run`과 함께 부르고, `--plugin-dir`에 작업 트리의 `plugins/plate`를, `--permission-mode bypassPermissions`를 준다. 기대: 더해진 `## 확인 1`에서 조건 1은 통과이고 "하네스에서 걸린 것"에 적힌 명령과 `-e`나 `--`를 넣은 고친 명령이 함께 있으며, 조건 2는 실패이고 판정은 실패다. 기록: 차림, 돌린 명령, 돌려받은 세 줄, `## 확인 1` 절 전문, 돌릴 때의 `git hash-object plugins/plate/skills/check/SKILL.md` 값

**통과 조건**
- 완료 조건 1이 참이다
  - 확인: phase·check·retro의 글마다 `grep -cF -e '<글>' <파일>`이 `1`이다
  - 확인: 이 phase의 "한 일"에 적힌 헤드리스 시험의 `## 확인 1` 절에서 조건 1은 통과이고 "하네스에서 걸린 것"에 `grep -F '- abc' f.txt`와 `-e`나 `--`를 넣은 고친 명령이 함께 있으며, 조건 2는 실패이고 판정은 실패다. 적힌 해시가 지금 작업 트리의 `git hash-object plugins/plate/skills/check/SKILL.md`와 같다
- 테스트가 모두 통과하고, 고친 글이 빠지면 실패한다
  - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
  - 확인: 세 시험을 저마다 새 사본(`mktemp -d`로 만든 폴더에 작업 트리의 `plugins`와 `tests`를 `cp -R`로 복사한 것)에서 한다. 그 글이 사본의 파일에 한 번 있는지 보고, 빈 글로 바꿔 `python3 -m unittest discover -s tests`를 돌리면 출력에 그 줄로 시작하는 줄이 있다. phase 본문의 `고친 명령과 까닭을 "계획과 달라진 점"과 "하네스에서 걸린 것"에 적는다` → `FAIL: test_69_fix_check_command_and_record (test_skill_rules.PhaseRulesTest`, check 본문의 `적힌 명령, 고친 명령, 까닭을 "하네스에서 걸린 것"에 적는다` → `FAIL: test_69_run_check_as_written (test_skill_rules.CheckRulesTest`, retro 본문의 `적힌 명령, 고친 명령, 까닭을 "확인"의 결과에 적고 5번의 문제로 모은다` → `FAIL: test_69_run_check_as_written (test_skill_rules.RetroRulesTest`
- 문서가 맞는다
  - 확인: `grep -F -e '적힌 그대로 돌지 않는 확인 명령' docs/ARCHITECTURE.md`가 낸 줄이 `test_skill_rules.py`를 담는다. `sed -n '1,8p' tests/test_skill_rules.py`의 phase·check·retro 목록에 `#69`가 있다

## 한 일
- phase 3번 절에 완료 조건 1의 phase 글 셋: 3번 목록에 "확인 명령이 적힌 그대로 돌지 않으면(옵션·문법 오류로 돌지 않는다: `-`로 시작하는 패턴이 옵션으로 읽힌다, 따옴표가 어긋난다) 대상과 패턴과 기대를 바꾸지 않는 고침만 해 다시 돌린다. 허용하는 고침은 `-e`나 `--` 붙이기, 따옴표 맞추기다. 고친 명령과 까닭을 … 적는다. 대상이나 패턴이나 기대를 바꿔야 돌면 상태는 "계획이 틀림"이다. 더 하지 않고 4번으로 간다." 항목을 더했고, 2번 "그 밖의 차이"의 예시에 "적힌 그대로 돌지 않는 확인 명령을 3번대로 고쳐 돌렸다"를 더했다 (`plugins/plate/skills/phase/SKILL.md`)
- check 2번 절에 완료 조건 1의 check 글 넷: 2번에 "확인은 적힌 그대로 먼저 돌린다. … 대상과 패턴과 기대를 바꾸지 않는 고침만 해 다시 돌린다. … 고쳐 돌린 결과로 판정하고, 적힌 명령, 고친 명령, 까닭을 "하네스에서 걸린 것"에 적는다. 대상이나 패턴이나 기대를 바꿔야 돌면 그 확인은 실패다." 문단을 더했고, 적는 규칙에 "\"통과 조건\"의 결과 줄에는 돌린 명령을 적는다. 2번대로 고쳐 돌렸으면 고친 명령을 적는다."를 더했다 (`plugins/plate/skills/check/SKILL.md`)
- retro 2번 절에 완료 조건 1의 retro 글 넷: 2번에 같은 꼴의 문단(기록 자리는 "적힌 명령, 고친 명령, 까닭을 "확인"의 결과에 적고 5번의 문제로 모은다")을 더했고, 5번 문제 갈래의 "확인 명령이 돌지 않았다"를 "확인 명령이 적힌 그대로 돌지 않아 2번대로 고쳐 돌렸다(적힌 명령, 고친 명령, 까닭을 함께)"로 바꿨다 (`plugins/plate/skills/retro/SKILL.md`)
- 테스트 셋과 docstring: `PhaseRulesTest.test_69_fix_check_command_and_record`, 새 `CheckRulesTest.test_69_run_check_as_written`, `RetroRulesTest.test_69_run_check_as_written`을 더했다. 저마다 그 본문의 그 절(`section`)에 완료 조건 1의 글이 모두 있는지 `subTest`로 본다. docstring에 phase·check·retro의 `#69`를 더했다 (`tests/test_skill_rules.py`)
- ARCHITECTURE의 `test_skill_rules.py` 줄 끝 목록에 "phase·check·retro가 적힌 그대로 돌지 않는 확인 명령을 대상·패턴·기대를 바꾸지 않는 고침으로만 고쳐 돌리고 기록함"을 더했다 (`docs/ARCHITECTURE.md`)
- check의 헤드리스 시험
  - 돌릴 때의 `git hash-object plugins/plate/skills/check/SKILL.md` → `24447065aed4abec74deb384330d05f80ab79ee8`
  - 차림: `mktemp -d`로 만든 `/var/folders/0j/cj37rxmj1mj73vhflqpgsxm00000gn/T/tmp.opz3CFN7mR`에 `git init`. `docs/ARCHITECTURE.md`는 `## 명령` 절만 있고 설치·빌드·린트·테스트 네 줄이 모두 "없음". `f.txt`는 `- abc` 한 줄. `docs/tasks/001-x/plan.md`(목표, 범위 밖, 완료 조건, 결정)와 `phase-1.md`(계획 다섯 항목, TODO 하나 체크됨, 기록 다섯 절. 통과 조건 둘: 조건 1 `grep -F '- abc' f.txt`가 한 줄을 낸다, 조건 2 `grep -F 'abc' nofile.txt`가 한 줄을 낸다)를 두고 `init`으로 커밋
  - 돌린 명령: 그 폴더에서 `claude -p "/plate:check task 폴더: docs/tasks/001-x` ↵ `phase: 1` ↵ `부른 쪽: plate:run" --plugin-dir /Users/hugo/Desktop/harness-plate/plugins/plate --permission-mode bypassPermissions`
  - 돌려받은 세 줄: `판정: 실패` / `실패: 1개` / `기록: docs/tasks/001-x/phase-1.md`. 시험 저장소에 `001-x: phase 1 확인` 커밋이 생겼다
  - 더해진 `## 확인 1` 절 전문:

    ```
    ## 확인 1

    **통과 조건**
    - 조건 1: f.txt에 `- abc` 줄이 있다
      - `grep -F -e '- abc' f.txt` → `- abc` 한 줄. 통과
    - 조건 2: nofile.txt에 abc가 있다
      - `grep -F 'abc' nofile.txt` → `nofile.txt: No such file or directory`, 종료 코드 2, 낸 줄 없음. 실패

    **명령**
    - 빌드: 없음
    - 린트: 없음
    - 테스트: 없음

    **테스트 먼저 기록**
    없음

    **남은 것**
    없음

    **실패**
    - 조건 2: `grep -F 'abc' nofile.txt`가 한 줄을 내야 하는데, nofile.txt가 저장소에 없어 "No such file or directory"(종료 코드 2)로 끝나고 아무 줄도 내지 않았다. 기록의 "확인 결과"에도 이 확인은 "돌리지 않음"으로 남아 있다 (`nofile.txt`)

    **하네스에서 걸린 것**
    - plate:check 2번: 조건 1의 적힌 명령 `grep -F '- abc' f.txt`가 `- abc`를 옵션으로 읽어 "invalid option - abc"(종료 코드 2)로 돌지 않았다. 대상과 패턴과 기대를 바꾸지 않고 `-e`를 붙인 `grep -F -e '- abc' f.txt`로 고쳐 돌려 판정했다. task 머리의 완료 조건 1 확인도 같은 명령이다
    - 명령 절의 빌드·린트·테스트가 모두 "없음"이라 돌리지 않았다

    **판정**: 실패
    ```

  - 기대와 견줌: 조건 1은 통과이고 "하네스에서 걸린 것"에 적힌 명령 `grep -F '- abc' f.txt`와 고친 명령 `grep -F -e '- abc' f.txt`가 함께 있다. 조건 2는 실패이고 판정은 실패다. 기대대로다

## 확인 결과
- 완료 조건 1이 참이다
  - phase의 글 셋을 `grep -cF -e '<글>' plugins/plate/skills/phase/SKILL.md`로, check의 글 넷을 `.../check/SKILL.md`로, retro의 글 넷을 `.../retro/SKILL.md`로 돌림 → 열한 번 모두 `1`. 통과
  - 위 "한 일"의 헤드리스 시험 `## 확인 1` → 조건 1 통과, "하네스에서 걸린 것"에 `grep -F '- abc' f.txt`와 `grep -F -e '- abc' f.txt`가 함께 있음, 조건 2 실패, 판정 실패. 기록 뒤에 `git hash-object plugins/plate/skills/check/SKILL.md`를 다시 냄 → `24447065aed4abec74deb384330d05f80ab79ee8`로 같음. 통과
- 테스트가 모두 통과하고, 고친 글이 빠지면 실패한다
  - `python3 -m unittest discover -s tests` → `Ran 196 tests in 17.125s`, 마지막 줄 `OK`. 통과
  - 세 시험을 저마다 `tempfile.mkdtemp()`의 새 폴더에 `plugins`와 `tests`를 복사한 사본에서 돌림(스크래치 패드의 `mut.py`) → phase: 글 수 1, 빈 글로 바꾸자 `FAIL: test_69_fix_check_command_and_record (test_skill_rules.PhaseRulesTest) (key=…)`, `FAILED (failures=1)`. check: 글 수 1, `FAIL: test_69_run_check_as_written (test_skill_rules.CheckRulesTest) (key=…)`, `FAILED (failures=1)`. retro: 글 수 1, `FAIL: test_69_run_check_as_written (test_skill_rules.RetroRulesTest) (key=…)`, `FAILED (failures=1)`. 통과
- 문서가 맞는다
  - `grep -F -e '적힌 그대로 돌지 않는 확인 명령' docs/ARCHITECTURE.md | grep -c test_skill_rules.py` → `1`. `sed -n '1,8p' tests/test_skill_rules.py` → `phase의 #42·#51·#69, check의 #51·#69,` / `retro의 #49·#50·#51·#69,`. 통과

## 계획과 달라진 점
- 고친 글이 빠지면 실패하는지 보는 시험의 사본을 `mktemp -d`와 `cp -R` 대신 Python의 `tempfile.mkdtemp()`와 `shutil.copytree`로 만들었다. 같은 꼴(새 임시 폴더에 작업 트리의 `plugins`와 `tests`를 통째로 복사)이고, 세 시험을 한 스크립트로 돌리려고 그렇게 했다

## 남은 것
- phase와 retro의 고침 규칙은 헤드리스로 돌려 보지 않았다(task 머리 완료 조건 1의 `돌리지 않음` 줄). 그 두 본문의 고침 규칙대로 수행·회고가 움직이는지는 글이 있는지만 확인했다
- check의 헤드리스 시험은 한 번, `-e`를 붙이는 꼴 하나만 봤다. 따옴표가 어긋난 명령이나 "대상이나 패턴이나 기대를 바꿔야 돌면 실패"의 갈래는 돌려 보지 않았다

## 하네스에서 걸린 것
- 이 phase가 고친 phase 본문이 지금 이 수행을 이끄는 스킬 본문이기도 하다. 수행은 불려 온 때의 본문(고치기 전)대로 했다
- 이 저장소 셸이 zsh라 `echo ====`가 `=` 확장으로 `=== not found` 오류를 냈다(헤드리스 시험 출력 뒤 구분 줄). 시험 자체에는 영향이 없었다

## 확인 1

**통과 조건**
- 완료 조건 1이 참이다
  - phase의 글 셋을 `grep -cF -e '<글>' plugins/plate/skills/phase/SKILL.md`로, check의 글 넷을 `grep -cF -e '<글>' plugins/plate/skills/check/SKILL.md`로, retro의 글 넷을 `grep -cF -e '<글>' plugins/plate/skills/retro/SKILL.md`로 돌림 → 열한 번 모두 `1`. 통과
  - 이 phase "한 일"의 헤드리스 시험 `## 확인 1` 절을 읽음 → 조건 1의 줄은 통과, "하네스에서 걸린 것"에 적힌 명령 `grep -F '- abc' f.txt`와 고친 명령 `grep -F -e '- abc' f.txt`가 함께 있음, 조건 2의 줄은 실패, 판정은 실패. 적힌 해시 `24447065aed4abec74deb384330d05f80ab79ee8`와 지금 `git hash-object plugins/plate/skills/check/SKILL.md` → `24447065aed4abec74deb384330d05f80ab79ee8`로 같음. 통과
- 테스트가 모두 통과하고, 고친 글이 빠지면 실패한다
  - `python3 -m unittest discover -s tests` → `Ran 196 tests`, 마지막 줄 `OK`. 통과
  - 세 시험을 저마다 `mktemp -d`의 새 폴더에 `cp -R plugins tests`로 만든 사본에서 글 수를 `grep -cF -e`로 보고 그 글을 빈 글로 바꿔 `python3 -m unittest discover -s tests`를 돌림 → phase: 글 수 1, `FAIL: test_69_fix_check_command_and_record (test_skill_rules.PhaseRulesTest) (key=…)`. check: 글 수 1, `FAIL: test_69_run_check_as_written (test_skill_rules.CheckRulesTest) (key=…)`. retro: 글 수 1, `FAIL: test_69_run_check_as_written (test_skill_rules.RetroRulesTest) (key=…)`. 셋 모두 `FAILED (failures=1)`. 통과
- 문서가 맞는다
  - `grep -F -e '적힌 그대로 돌지 않는 확인 명령' docs/ARCHITECTURE.md`가 낸 줄 → `test_skill_rules.py`를 담음(`grep -c test_skill_rules.py`로 `1`). `sed -n '1,8p' tests/test_skill_rules.py` → `phase의 #42·#51·#69, check의 #51·#69,`와 `retro의 #49·#50·#51·#69,`가 있음. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 196 tests`, `OK`. 통과

**남은 것**
- phase와 retro의 고침 규칙은 헤드리스로 돌려 보지 않았다 → 돌려 보지 않은 위험이고, task 머리 완료 조건 1의 `- 돌리지 않음: phase와 retro의 고침 규칙은 헤드리스로 돌리지 않는다. 사용자가 check·review만 돌리기로 정했다` 줄이 돌리지 않기로 정한 동작이다. 하네스에서 걸린 것
- check의 헤드리스 시험은 `-e`를 붙이는 꼴 하나만 봤고 따옴표가 어긋난 명령이나 "대상이나 패턴이나 기대를 바꿔야 돌면 실패"의 갈래는 돌려 보지 않았다 → 돌려 보지 않은 위험이나, 통과 조건이 보는 동작(헤드리스 시험에서 `-` 패턴을 `-e`나 `--`로 고쳐 돌려 통과로 판정하고 기록하는 것, 없는 파일의 조건을 실패로 판정하는 것)에 걸리지 않는다. 하네스에서 걸린 것

**실패**
- 없음

**하네스에서 걸린 것**
- 남은 것: phase와 retro의 고침 규칙은 헤드리스로 돌려 보지 않았다(task 머리 완료 조건 1의 `돌리지 않음` 줄이 정한 것)
- 남은 것: check의 헤드리스 시험은 `-e`를 붙이는 꼴 하나만 봤고, 따옴표가 어긋난 명령과 "대상이나 패턴이나 기대를 바꿔야 돌면 실패"의 갈래는 돌려 보지 않았다
- 확인을 맡은 이 check 본문이 이 phase가 고친 본문이기도 하다. 확인은 작업 트리의 고친 본문대로 했다

**판정**: 통과
