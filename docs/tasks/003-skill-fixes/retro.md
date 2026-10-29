# 회고

## 회고 1

**확인**
- 1. run이 띄운 에이전트가 정한 결과를 남기지 않고 돌아오면 같은 자리를 다시 띄우고 `| 다시 띄움: 결과 없음`을 덧붙이며, 연달아 세 번째면 "멈춘다"로 간다. 코드 평가 뒤 `review.md`가 없으면 하네스 eval로 가지 않는다(신뢰성-3).
  - `grep -n '다시 띄움: 결과 없음' plugins/plate/skills/run/SKILL.md` → 59(낱말), 293("## 멈춘다" 285행~"## tasks 끝" 306행 사이), 570("## `RUNLOG.md`" 555행~"## 출처" 580행 사이). 두 절에 저마다 한 줄. 통과
  - `python3 -m unittest tests.test_skill_rules.RunRulesTest.test_no_result_relaunch_limit -v` → `Ran 1 test`, `OK`. 통과
  - 돌리지 않음(task 머리): 결과 없이 돌아오는 장면은 헤드리스로 만들 수 없다. 대신 59행의 셈을 읽어 따라가 봤다: 첫 줄(표시 없음)→다시 띄움(표시)→다시 띄움(표시)에서 마지막 둘이 모두 표시라 세 번째에 멈춘다. 325행은 `review.md`가 있을 때만 하네스 eval로 간다
- 2. run 1번이 tasks 브랜치를 정한 뒤에 계획을 커밋한다(신뢰성-8).
  - `grep -n -e '\*\*tasks 브랜치\.\*\*' -e '\*\*계획의 커밋\.\*\*' plugins/plate/skills/run/SKILL.md` → `89:2. **tasks 브랜치.**`, `96:3. **계획의 커밋.**`. 89 < 96. 통과
- 3. "이슈를 올린다" 2번과 "PR 본문의 꼴"의 "올린 이슈"가 `gh api user`의 login이 쓴 본문과 댓글로만 이미 있다고 본다(기존 작업 정합성-5).
  - `grep -n 'gh api user' plugins/plate/skills/run/SKILL.md` → 376행("### 이슈를 올린다" 369행~"### BACKLOG를 고친다" 383행 사이), 519행("## PR을 연다" 503행 아래 "**PR 본문의 꼴**" 516행 뒤의 올린 이슈 항목). 통과
  - `gh api user --jq .login` → `werwer748` 한 줄. `gh issue view 68 --repo werwer748/harness-plate --json author,comments --jq '.author.login'` → `werwer748` 한 줄. 통과
- 4. run 3번의 `멈춤` 줄 grep을 가짜 `RUNLOG.md`에 돌리는 테스트가 있고, 패턴이 바뀌면 실패한다(기존 작업 정합성-7).
  - `python3 -m unittest tests.test_skill_rules.RunRulesTest.test_stop_line_grep_runs_on_fake_runlog -v` → `Ran 1 test`, `OK`. 통과
- 5. phase 스킬의 실패 출력 얻기가 부모 커밋에 없는 구현 파일의 갈래를 적고, 명령 예가 새 파일과 바뀐 파일에서 돈다(신뢰성-2).
  - `grep -n '부모 커밋에 없' plugins/plate/skills/phase/SKILL.md` → 59행. "## 2. TODO를 차례로 끝낸다"(42행)~"## 3."(70행) 사이. 통과
  - scratchpad 아래 `mktemp -d` 시험 레포: `base`에 `tests/test_a.py`(test_old는 `old.f()==1`, test_new는 `new.g()==2`)와 `old.py`(`return 0`), `001-a: phase 1`에서 `old.py`를 줄 수가 다른 `return 1` 판으로 고치고 `new.py`를 새로 만듦. 시작 `git status --porcelain` → 빈 줄. `git cat-file -e "$c^:<파일>"` → `old.py in parent`, `new.py not in parent`. `git checkout "$c^" -- old.py`, `tmp=$(mktemp -d) && mv new.py "$tmp"/` 뒤 `python3 -B -m unittest discover -s tests` → `FAILED (failures=1, errors=1)`. `git checkout HEAD -- old.py`, `mv "$tmp"/new.py new.py` 뒤 → `OK`. 끝 `git status --porcelain` → 빈 줄. 통과
- 6. review 2번이 커버리지 도구가 테스트 명령을 감쌀 수 있으면 한 번 돌려 함께 쓴다(성능-4).
  - `grep -n '한 번' plugins/plate/skills/review/SKILL.md` → 72행 `2. **커버리지**: … 한 번만 돌려 …`. "## 2. 잰다"(67행)~"## 3."(77행) 사이의 커버리지 항목. 통과
  - 돌리지 않음(task 머리): 이 저장소에 커버리지 도구가 없다(ADR-024)
- 7. cleanup 2번이 맥락 문서를 모두 읽지 않고, 4번과 2라운드 글이 결정의 범위와 반박 근거를 적는다(성능-2, 기존 작업 정합성-8).
  - `grep -n '맥락 문서를 모두 읽는다' plugins/plate/skills/cleanup/SKILL.md` → 출력 없음(`exit=1`). 통과
  - `grep -n '결정 절' plugins/plate/skills/cleanup/SKILL.md` → 99행("## 4. 2라운드" 90행~"## 5." 104행 사이), 190행("## 2라운드에 맡기는 글" 172행~"## plan에 넘기는 요청" 199행 사이). 통과
  - 돌리지 않음(task 머리): cleanup은 에이전트 열두 개를 띄우고 묻는 스킬이다. 1라운드 글은 "대어 볼 자료"에 경로만 넘겨, 2번의 읽기를 지워도 1라운드의 자료가 빠지지 않는 것을 3번 기준 표와 1라운드 글에서 읽어 봤다
- 8. PRD와 ARCHITECTURE가 바뀐 동작과 맞다.
  - `grep -n '결과 없' docs/PRD.md docs/ARCHITECTURE.md` → `docs/PRD.md:17`(핵심 기능 7), `docs/ARCHITECTURE.md:39`(`test_skill_rules.py` 줄), `docs/ARCHITECTURE.md:98`("어느 실행 방식이든" 문단, 세 번째에서 멈춘다고 적음). 통과
  - `grep -n 'gh api user' docs/ARCHITECTURE.md` → 56행(run 이슈·PR 문단, login이 쓴 본문·댓글로 좁힘), 57행(CI 문단). 통과
- 9. 테스트 묶음이 모두 통과한다.
  - `python3 -m unittest discover -s tests` → `Ran 236 tests in 20.661s`, 마지막 줄 `OK`. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 236 tests`, `OK`. 통과

**남은 것**
- phase 1: 수행의 결과를 `## 한 일` 유무로만 봐, 기록 절이 이미 있는 고칠 문제 수행이 아무것도 바꾸지 않고 돌아오면 결과 없음으로 잡지 못한다 → 문제 아님 (완료 조건 1이 수행의 결과를 "기록 절"로 정했고, 이 꼴은 그 경계 밖이다. 확인이 다시 실패해 확인의 세 번 실패로 멈춘다)
- phase 1: 세션을 끊고 3번 표로 같은 자리를 다시 맡길 때 `결과 없음` 표시를 달지 정하지 않았다 → 문제 아님 (완료 조건 1과 결정은 돌아온 뒤의 다시 띄움만 정한다. 경계 밖)
- phase 1: 동작을 헤드리스로 돌려 보지 않았다 → 문제 아님 (완료 조건 1의 `돌리지 않음` 줄. 셈은 본문을 읽어 따라가 봤다)
- phase 2: 계획 파일을 커밋하지 않은 채 이미 있는 `tasks/<이름>`으로 `git switch`할 때 같은 경로의 추적 파일이 있으면 switch가 실패할 수 있고 본문이 그 갈래를 다루지 않는다 → 문제 아님 (완료 조건 2는 차례만 정하고, 실패는 조용히 계획을 잃던 옛 꼴과 달리 git 오류로 드러난다. 경계 밖)
- phase 2: 다른 사람이 같은 tasks 이름을 적은 이슈에는 댓글을 한 번 더 달 수 있다 → 문제 아님 (tasks 머리·task 머리의 결정이 의도한 동작)
- phase 3: 새 갈래와 한 번 돌림을 지키는 시험이 `tests/`에 없다 → 문제 아님 (완료 조건 5·6은 grep과 시험 레포로 보고 시험을 두라고 하지 않았다)
- phase 3: `sys.pycache_prefix`의 낡은 바이트코드가 되돌린 Python 파일 대신 읽혀 실패 출력을 가릴 수 있다 → 문제 아님 (완료 조건 5가 보는 시험 레포의 되돌림·되살림은 이번 회고에서도 돌았다. 대상 프로젝트의 캐시 꼴은 경계 밖)
- phase 3: 구현 파일에 커밋되지 않은 변경이 있으면 `git checkout HEAD -- <구현 파일>`이 그 변경을 지운다 → 문제 아님 (옛 글에도 있던 되살림이고, 이 문단은 phase 커밋 뒤 실패 출력만 얻는 자리다)
- phase 4: 고친 cleanup 본문의 동작을 돌려 보지 않았다 → 문제 아님 (완료 조건 7의 `돌리지 않음` 줄)

**문제**
없음

**판정**: 통과
