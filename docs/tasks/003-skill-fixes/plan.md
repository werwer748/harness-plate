# run, phase, cleanup, review 본문의 발견을 고친다

## 목표
정리 점검 2026-10-29의 신뢰성-2·3·8, 기존 작업 정합성-5·7·8, 성능-2·4를 run, phase, cleanup, review의 본문과 테스트에서 고치고, 같은 동작을 적은 PRD·ARCHITECTURE의 줄을 맞춘다.

## 범위 밖
- run, cleanup, review를 헤드리스로 끝까지 돌리는 것(에이전트를 띄우고 사용자에게 묻는 스킬이다).
- run 본문을 참고 파일로 나누는 것(지난 점검들이 버렸다).
- 이 저장소에 커버리지 도구를 두는 것(ADR-024).

## 완료 조건
1. run이 띄운 에이전트가 정한 결과(수행의 기록 절, 확인 절, 회고 절, `review.md`, `eval.md`)를 남기지 않고 돌아오면 같은 자리를 다시 띄우고 `RUNLOG.md`의 에이전트 줄에 `| 다시 띄움: 결과 없음`을 덧붙이며, 같은 자리에서 연달아 세 번째면 "멈춘다"로 간다. 코드 평가 뒤 `review.md`가 없으면 하네스 eval로 가지 않는다(신뢰성-3).
   - 확인: `grep -n '다시 띄움: 결과 없음' plugins/plate/skills/run/SKILL.md` → "멈춘다" 절의 자리 목록과 `RUNLOG.md` 절에 저마다 한 줄 이상
   - 확인: `python3 -m unittest tests.test_skill_rules.RunRulesTest.test_no_result_relaunch_limit -v` → `OK`
   - 돌리지 않음: 에이전트가 결과 없이 돌아오는 장면은 run을 헤드리스로 돌려 일부러 만들 수 없다
2. run 1번이 tasks 브랜치를 정한 뒤에 계획을 커밋한다(신뢰성-8).
   - 확인: `grep -n -e '\*\*tasks 브랜치\.\*\*' -e '\*\*계획의 커밋\.\*\*' plugins/plate/skills/run/SKILL.md` → `tasks 브랜치`의 줄 번호가 `계획의 커밋`보다 작다
3. run의 "이슈를 올린다" 2번과 PR 본문의 꼴의 "올린 이슈"가, `gh api user`의 login이 쓴 본문과 댓글에 tasks 이름이 있을 때만 이미 있다고 본다(기존 작업 정합성-5).
   - 확인: `grep -n 'gh api user' plugins/plate/skills/run/SKILL.md` → "이슈를 올린다"와 "PR 본문의 꼴"에 저마다 한 줄 이상
   - 확인: `gh api user --jq .login` → login 한 줄. `gh issue view 68 --repo werwer748/harness-plate --json author,comments --jq '.author.login'` → login 한 줄(본문에 넣은 명령 예가 그 필드를 낸다)
4. run 3번의 `멈춤` 줄 grep을 가짜 `RUNLOG.md`에 돌려 마지막 `멈춤` 줄을 뽑는지 테스트가 보고, 패턴이 바뀌면 실패한다(기존 작업 정합성-7).
   - 확인: `python3 -m unittest tests.test_skill_rules.RunRulesTest.test_stop_line_grep_runs_on_fake_runlog -v` → `OK`
5. phase 스킬의 실패 출력 얻기가 부모 커밋에 없는 구현 파일을 잠깐 옮겨 테스트를 돌리고 되살리는 갈래를 적고, 그 명령 예가 새 파일과 바뀐 파일에서 돈다(신뢰성-2).
   - 확인: `grep -n '부모 커밋에 없' plugins/plate/skills/phase/SKILL.md` → "2. TODO를 차례로 끝낸다" 절에 한 줄 이상
   - 확인: `mktemp -d` 시험 레포에서 phase 커밋이 새로 만든 구현 파일과 바꾼 구현 파일을 저마다 두고, 본문의 명령 예대로 되돌리고 되살린 뒤 `git status --porcelain`이 비어 있다
6. review 2번이 커버리지 도구가 테스트 명령을 감쌀 수 있으면 한 번 돌려 테스트와 커버리지에 함께 쓴다(성능-4).
   - 확인: `grep -n '한 번' plugins/plate/skills/review/SKILL.md` → "2. 잰다" 절의 커버리지 항목에 한 줄 이상
   - 돌리지 않음: 이 저장소에는 커버리지 도구가 없어(ADR-024) review를 돌려도 그 갈래에 닿지 않는다
7. cleanup 2번이 맥락 문서를 모두 읽지 않고, 4번이 반박 판정에 필요한 맥락 문서를 읽으며 "결정이 정한 것"의 범위(맥락 문서에 적힌 것과 지난 tasks 머리·task 머리의 결정 절)를 한 줄로 정하고, 2라운드에 맡기는 글이 그 근거를 반박에 들라고 한다(성능-2, 기존 작업 정합성-8).
   - 확인: `grep -n '맥락 문서를 모두 읽는다' plugins/plate/skills/cleanup/SKILL.md` → 아무것도 나오지 않음
   - 확인: `grep -n '결정 절' plugins/plate/skills/cleanup/SKILL.md` → "4. 2라운드" 절과 "2라운드에 맡기는 글" 절에 저마다 한 줄 이상
   - 돌리지 않음: cleanup은 에이전트 열두 개를 띄우고 묻는 스킬이라 헤드리스로 돌리지 않는다
8. PRD와 ARCHITECTURE가 바뀐 동작과 맞다: PRD 핵심 기능 7과 ARCHITECTURE의 멈춤 문단(데이터 흐름 뒤 "어느 실행 방식이든")이 결과 없는 에이전트의 세 번째에서 멈춘다고 적고, ARCHITECTURE의 run 이슈·PR 문단이 이슈의 "이미 있음"을 plate를 돌린 계정의 글로 좁힌다고 적는다.
   - 확인: `grep -n '결과 없' docs/PRD.md docs/ARCHITECTURE.md` → 두 파일에 저마다 한 줄 이상
   - 확인: `grep -n 'gh api user' docs/ARCHITECTURE.md` → run의 이슈·PR 문단에 한 줄 이상
9. 테스트 묶음이 모두 통과한다(tasks 완료 조건 1).
   - 확인: `python3 -m unittest discover -s tests` → 마지막 줄이 `OK`

## 결정
- 결과 없이 돌아온 에이전트는 같은 자리에서 연달아 세 번째면 멈추고, 횟수는 `RUNLOG.md`의 `다시 띄움: 결과 없음` 줄로 센다. 이유: run의 다른 상한(확인·회고의 세 번 실패, 훅의 세 번째 막음)과 같은 수이고, 세션을 끊어도 남는다.
- 이슈의 "이미 있음"은 `gh api user`의 login이 쓴 본문과 댓글에 tasks 이름이 있을 때만이다. login을 얻지 못하면 이미 있지 않은 것으로 본다. 이유: 밖의 입력이 판정을 바꾸는 길을 닫는다.
- "결정이 정한 것"은 맥락 문서(PRD의 범위 밖, ARCHITECTURE의 규칙, ADR, BACKLOG의 감수한 것)에 적힌 것과 지난 tasks 머리·task 머리의 결정 절(커밋으로 인용)이다. 닫힌 이슈의 글과 테스트만으로는 결정으로 치지 않는다. 이유: 오늘 점검이 실제로 쓴 근거와 맞고, 밖의 사람이 쓸 수 있는 이슈 글은 빠진다.
- 이 task의 phase는 스킬 본문을 run이 넘긴 판으로 수행하고 확인한다. 고친 본문의 동작은 본문의 명령 예를 시험 저장소에서 돌리는 것으로 본다. 이유: AGENTS.md의 작업 규칙과 `docs/TOOLS.md`의 "세션 도중의 스킬 본문 고침" (추천안으로 정함)
