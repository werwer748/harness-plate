# 하네스 eval

## eval 1

**대상**
- tasks: `release-prep`, task 4개, phase 10개(더한 phase 1개)
- 커밋: `aa3577b`부터 `7ea7eef`까지 50개
- 기록: `RUNLOG.md` 에이전트 줄 30줄, 물은 줄 6줄. `FRICTION.md` 27줄. `review.md` 평가 1

**실패**
1. 계획의 장면 B 정의("phase가 모두 통과하고 회고가 없는 작은 tasks")가 그 tasks가 회고를 통과해야 tasks 끝에 닿는다는 것을 적지 않아, 처음 차린 tasks가 회고에서 멈춰 다시 차렸다 (`001-run-rules/done-phase-2.md`의 "하네스에서 걸린 것", `FRICTION.md` 5행). 유형: FM-2.4 정보를 감춤. 잡힌 곳: 그 자리
2. 결정 "이 저장소의 main을 복제"가 원본이 다른 브랜치에 있을 때 복제본의 `origin/HEAD`가 그 브랜치를 가리키는 것을 다루지 않아, 장면 B의 run과 코드 평가가 기본 브랜치를 `tasks/release-prep`으로 봤다 (`001-run-rules/done-phase-2.md`의 "하네스에서 걸린 것", `FRICTION.md` 4행). 유형: FM-2.4 정보를 감춤. 잡힌 곳: 그 자리
3. run 8번이 계획 커밋을 찾는 명령으로 적은 `$(git log -1 …)` 명령 치환이 헤드리스 Claude Code에서 승인 요구로 막혀 run 메인이 나눠 불렀다. 같은 본문이 "PR을 연다"에서 이 제약을 이미 적어 두었다 (`001-run-rules/done-phase-3.md`의 "하네스에서 걸린 것", `FRICTION.md` 3행). 유형: FM-1.1 과제 명세를 어김. 잡힌 곳: 그 자리
4. run 8번이 고칠 phase의 통과 조건에 "task 머리의 완료 조건이 모두 참이다"를 넣었지만 완료 조건 3의 시각 확인은 run 본문을 고치는 고칠 phase에서 참일 수 없었고, 8번 첫머리의 "계획을 바꿔야 하는지" 판정이 이를 보지 못해 phase 4 수행이 "계획이 틀림"으로 두 번 멈췄다 (`001-run-rules/done-phase-4.md`의 "하네스에서 걸린 것", `FRICTION.md` 9~11행, `RUNLOG.md`의 `멈춤` 줄 둘, `cad84b1`, `0b989db`). 유형: FM-3.2 검증이 없거나 모자람. 잡힌 곳: 그 자리
5. `docs/TOOLS.md`의 헤드리스 허용 목록에 `git remote`, `git rm`이 없어 장면의 run이 "비운다"에서 승인 대기로 막혔다 (`001-run-rules/done-phase-4.md`의 "하네스에서 걸린 것", `FRICTION.md` 15행). 유형: FM-2.4 정보를 감춤. 잡힌 곳: 그 자리
6. 계획의 장면 B 정의가 고칠 것이 나오는 차림을 정하지 않아, "고칠지"에서 멈추는 자리를 보려고 차림을 세 번째까지 바꿨다 (`001-run-rules/done-phase-4.md`의 "하네스에서 걸린 것", 확인 1의 "하네스에서 걸린 것", `FRICTION.md` 14행). 유형: FM-2.4 정보를 감춤. 잡힌 곳: 그 자리
7. phase 4의 첫 수행이 run 본문에 사용량 까닭을 적은 `docs/TOOLS.md`가 커밋되지 않은 채 남는 길("멈춘다"·8번의 멈추기로 함, 승인받지 못함)을 남겼다 (`001-run-rules/done-phase-4.md` 확인 1의 "실패" 1). 유형: FM-3.3 검증이 틀림. 잡힌 곳: phase의 확인
8. phase 4의 첫 수행이 다시 돌린 장면 B가 "고칠지"에 닿지 않아 완료 조건 3의 장면 B 기대를 보이지 못했다 (`001-run-rules/done-phase-4.md` 확인 1의 "실패" 2, `FRICTION.md` 13행). 유형: FM-3.3 검증이 틀림. 잡힌 곳: phase의 확인
9. run 본문이 `docs/TOOLS.md`의 사용량 까닭을 "다음 `RUNLOG.md` 커밋에 함께 넣는다"고 하면서 그 커밋 자리들은 다른 파일을 막아 두 글이 부딪혔다. phase 1~3의 확인이 통과시켰다 (`001-run-rules/retro.md` 회고 1의 "문제"). 유형: FM-3.3 검증이 틀림. 잡힌 곳: task의 회고
10. 장면 C의 계획 고칠 안 승인 뒤(계획 커밋, 계획 커밋으로 고친 문제만 남은 고칠 phase)를 돌려 보지 않고 글로만 읽었다 (`FRICTION.md` 6행. 회고 1의 "남은 것"은 "문제 아님"으로 판정했다). 유형: FM-3.2 검증이 없거나 모자람. 잡힌 곳: task의 회고
11. 두 번째 계획 수정 `0b989db`(장면 B의 시각 확인을 run 본문 해시 확인으로 바꿈)가 run "멈춘다" 4의 "고친 것과 까닭을 결정에 한 줄 더한다"를 따르지 않아 task 머리와 tasks 머리의 결정에 줄이 없다 (`FRICTION.md` 12행). 유형: FM-1.1 과제 명세를 어김. 잡힌 곳: task의 회고
12. 계획의 결정 "plan 장면은 승인하지 않는다"와 phase 2 TODO "task 초안을 보여 주는 자리까지 잇는다"가 맞지 않았는데, 수행이 멈추지 않고 "마지막 초안만 승인하지 않는다"로 읽어 나아갔다 (`002-plan-phase-rules/done-phase-2.md`의 "하네스에서 걸린 것", `FRICTION.md` 17행, `fe2879f`). 유형: FM-2.2 묻지 않고 짐작함. 잡힌 곳: 그 자리
13. 계획이 장면 E의 기대를 #37의 해결책 한 차림(`git clone --bare`)으로 좁혀, URL만 보는 요청에서 plan이 맞게 고른 `git remote add`를 실패로 만들어 phase 2가 "계획이 틀림"으로 멈췄다 (`002-plan-phase-rules/done-phase-2.md`의 "하네스에서 걸린 것", `FRICTION.md` 18·24행, `RUNLOG.md`의 `멈춤` 줄). 유형: 유형 없음 — 계획(명세)의 기대 자체가 틀린 것이라 에이전트의 행동 유형에 들지 않는다. 잡힌 곳: 그 자리
14. `claude -p`의 `--allowedTools`가 뒤에 둔 프롬프트를 값으로 삼켜 헤드리스 장면이 입력 없음으로 끝났다 (`002-plan-phase-rules/done-phase-2.md`의 "하네스에서 걸린 것"). 유형: 유형 없음 — 도구의 옵션 꼴에서 온 걸림이다. 잡힌 곳: 그 자리
15. `docs/TOOLS.md`의 허용 목록 13개로 plan 장면을 돌려도 메인이 이은 Bash(명령 치환, `for`, `cut`, `sed`, `grep -v`, `gh api`)가 막혔다 (`002-plan-phase-rules/done-phase-2.md`의 "하네스에서 걸린 것", `FRICTION.md` 22행). 유형: FM-2.4 정보를 감춤. 잡힌 곳: 그 자리
16. phase 스킬 5번의 phase 끝 한 커밋과 통과 조건의 시각 확인("돌린 시각이 본문의 마지막 커밋보다 늦다")이 함께 서지 않아, phase 2가 본문만 먼저 커밋해(`584ae16`) phase 커밋이 둘이 됐다 (`002-plan-phase-rules/done-phase-2.md`의 "하네스에서 걸린 것", `FRICTION.md` 20행). 유형: FM-1.1 과제 명세를 어김. 잡힌 곳: 그 자리
17. 계획(task 머리 완료 조건 3, phase-3 TODO 1)이 세션 기록 위치를 `~/.claude/projects/`로 못박아 `CLAUDE_CONFIG_DIR`을 바꾼 이 기계와 어긋났다 (`002-plan-phase-rules/done-phase-3.md`의 "하네스에서 걸린 것", 확인 1의 "하네스에서 걸린 것", `FRICTION.md` 21행). 유형: FM-2.2 묻지 않고 짐작함. 잡힌 곳: 그 자리
18. 002의 완료 조건이 이번에 plan에 더한 "갈래마다 돌리는 확인" 규칙을 스스로 따르지 않아 #37의 `git clone --bare` 갈래와 #42의 앞 기록이 필요한 갈래를 돌려 보지 않았다 (`FRICTION.md` 19행). 유형: FM-3.2 검증이 없거나 모자람. 잡힌 곳: task의 회고
19. phase 스킬이 run이 띄운 호출과 사용자가 직접 부른 호출을 가르지 못해, 헤드리스로 부른 장면 G가 사용자가 부른 꼴로 보고하고 run 안내를 붙였다 (`FRICTION.md` 23행. 회고 1의 "남은 것"은 "문제 아님"으로 판정했다). 유형: FM-2.4 정보를 감춤. 잡힌 곳: task의 회고
20. 결정의 허용 목록 13개에 eval·review가 쓰는 `git merge-base`, `git symbolic-ref`, review가 명령 절에서 돌리는 `claude plugin validate`가 빠져 phase 2가 장면마다 더했고, 더하고도 장면 I의 `grep`·`cut`·`command` 3개가 막혔다 (`003-eval-review-rules/done-phase-2.md`의 "하네스에서 걸린 것", `FRICTION.md` 26행). 유형: FM-2.4 정보를 감춤. 잡힌 곳: 그 자리
21. retro 스킬 5번이 `FRICTION.md` 문제 줄과 회고 절 "남은 것"의 판정 관계를 정하지 않아, 회고 절에서 "문제 아님"으로 판정한 줄을 `FRICTION.md`에 `문제`로 적는 일이 났다. 장면 H의 eval이 issue-sweep에서 찾았고, 이 tasks에서도 `FRICTION.md` 6·19·23행이 그렇다 (`FRICTION.md` 27행). 유형: FM-2.6 생각과 행동이 어긋남. 잡힌 곳: task의 회고
22. 004 phase 1의 읽을 것이 고친 규칙을 이슈 번호로만 가리키고 이슈와 본문 절·글의 대응을 적지 않아, 수행이 `gh issue view`와 `git diff main..HEAD -- plugins/plate/skills`로 계획 밖의 근거를 찾았다 (`004-tests-version/done-phase-1.md`의 "하네스에서 걸린 것", `FRICTION.md` 29행). 유형: FM-2.4 정보를 감춤. 잡힌 곳: 그 자리
23. run의 description이 1142자로 Agent Skills 규격의 1024자를 넘어 Codex가 끝의 부르는 말과 "계획이 없는 요청에는 쓰지 않는다"를 잘랐다. 계획과 확인, 회고에 description 길이를 보는 확인이 없어 phase 확인과 task 회고를 지나왔다 (`review.md` 평가 1의 신뢰성, "하네스에서 걸린 것" 2). 유형: FM-3.3 검증이 틀림. 잡힌 곳: tasks 끝

**기준**
- 결과 성공
  - 근거: `review.md` 평가 1의 완료 조건 5개, 확인 15개 가운데 통과 15, 실패 0, 측정 못함 0. 기능 적합성 A
  - 근거: `001-run-rules` 마지막 회고 2 통과
  - 근거: `002-plan-phase-rules` 마지막 회고 1 통과
  - 근거: `003-eval-review-rules` 마지막 회고 1 통과
  - 근거: `004-tests-version` 마지막 회고 1 통과
  - 등급: A — 완료 조건의 확인이 모두 통과하고, task마다 마지막 회고 판정이 통과다
- 일관성
  - 근거: `001-run-rules` phase 1 첫 시도 통과
  - 근거: `001-run-rules` phase 2 첫 시도 통과
  - 근거: `001-run-rules` phase 3 첫 시도 통과
  - 근거: `001-run-rules` phase 4 수행 3번, 확인 2번째에 통과
  - 근거: `002-plan-phase-rules` phase 1 첫 시도 통과
  - 근거: `002-plan-phase-rules` phase 2 수행 2번, 확인 1번째에 통과
  - 근거: `002-plan-phase-rules` phase 3 첫 시도 통과
  - 근거: `003-eval-review-rules` phase 1 첫 시도 통과
  - 근거: `003-eval-review-rules` phase 2 첫 시도 통과
  - 근거: `004-tests-version` phase 1 첫 시도 통과
  - 근거: `001-run-rules` 회고 2번째에 통과
  - 근거: `002-plan-phase-rules` 회고 첫 시도 통과
  - 근거: `003-eval-review-rules` 회고 첫 시도 통과
  - 근거: `004-tests-version` 회고 첫 시도 통과
  - 첫 시도 통과율: 11 ÷ 14 = 78.6%
  - 등급: B — 75% 이상 90% 미만
- 효율
  - 합계: 에이전트 30개, 토큰 3015062, 도구 호출 507, 시간 8690초
  - 근거: `수행 001-run-rules phase 4` 되풀이 — 더한 phase(첫 수행, 토큰 74176)
  - 근거: `수행 001-run-rules phase 4` 되풀이 — 더한 phase, 같은 역할이 2번째로 맡았다(토큰 88825)
  - 근거: `확인 001-run-rules phase 4` 되풀이 — 더한 phase(토큰 99436)
  - 근거: `수행 001-run-rules phase 4` 되풀이 — 더한 phase, 같은 역할이 3번째로 맡았다(토큰 143679)
  - 근거: `확인 001-run-rules phase 4` 되풀이 — 더한 phase, 같은 역할이 2번째로 맡았다(토큰 104735)
  - 근거: `회고 001-run-rules` 되풀이 — 같은 역할이 2번째로 맡았다(토큰 104546)
  - 근거: `수행 002-plan-phase-rules phase 2` 되풀이 — 같은 역할이 2번째로 맡았다(토큰 132242)
  - 되풀이 몫: 토큰 747639 ÷ 3015062 = 24.8%, 도구 호출 130 ÷ 507 = 25.6%, 시간 2081 ÷ 8690 = 23.9%
  - 등급: C — 가장 높은 비율 25.6%가 20% 이상 35% 미만
- 규칙 준수
  - 근거: 표에 있는 꼴의 커밋(계획 `aa3577b`, 계획 수정 `1ea70e4`·`cad84b1`·`0b989db`·`fe2879f`, phase 수행·고침 11개, 확인 11개, 통과 10개, 회고 5개, 코드 평가 `298e77b`)은 모두 넣어도 되는 파일만 넣었다
  - 근거: `584ae16`(`002-plan-phase-rules: phase 2 (plan 본문 #37 넓힘)`)은 표에 없는 꼴이라 보지 않았다. 넣은 파일은 그 phase가 고친 plan 본문뿐이다. phase 스킬 5번의 한 커밋과 어긋난 것은 실패 16에 있다
  - 근거: `NNN-slug: RUNLOG`, `release-prep: RUNLOG` 커밋 6개는 이 eval의 표에 없는 꼴이라 보지 않았다. 모두 `RUNLOG.md` 하나만 넣었다
  - 근거: `0b989db` 계획 수정이 run "멈춘다" 4의 "고친 것과 까닭을 결정에 한 줄 더한다"를 따르지 않아 task 머리와 tasks 머리의 결정 줄이 빠졌다 (기록의 꼴)
  - 근거: `RUNLOG.md`의 `권한` 물은 줄이 001 phase 3 확인 줄 뒤에 "(답은 실행 방식 뒤에 받음)"으로 적혀, 물은 자리마다 그때 한 줄을 남기는 run의 `RUNLOG.md` 규칙과 차례가 어긋났다 (기록의 꼴)
  - 근거: `done-phase-N.md` 10개 모두 기록 다섯 절과 확인 절의 판정이 있고, `retro.md` 4개 모두 회고 절의 판정이 있다
  - 근거: 회고 절의 문제 가운데 기준이 "범위"나 "계획"인 것은 없다
  - 근거: 테스트 먼저인 phase는 없다(10개 모두 "아니오")
  - 근거: `004-tests-version` phase 1 수행이 읽을 것 밖의 `gh issue view`와 `git diff`를 봤지만, phase 스킬 1번이 금하는 tasks 머리와 다른 phase 파일은 읽지 않았다고 적었다. 읽기 범위 위반으로 세지 않고 실패 22로 둔다
  - 등급: B — 어긴 것이 기록의 꼴(결정 줄이 빠짐, `RUNLOG.md` 줄의 차례)뿐이다
- 사람 개입률
  - 근거: 로컬 main의 계획 커밋을 origin/main으로 되돌릴지 → 정해 둔 물음
  - 근거: 실행 방식 → 정해 둔 물음
  - 근거: auto mode에서 권한 모드를 바꿀지 → 정해 둔 물음
  - 근거: phase 4 계획이 틀림, 시각 확인을 좁히는 계획 수정안 → 멈춤
  - 근거: 장면 B의 시각 확인을 run 본문 해시 확인으로 바꾸는 계획 수정안 → 멈춤
  - 근거: 002 phase 2 계획이 틀림, #37의 원격 차림을 넓히는 계획 수정안 → 멈춤
  - 개입률: 멈춤 3 ÷ 에이전트 30 = 10.0%
  - 등급: C — 5% 넘고 10% 이하
- 실패 양상
  - 유형마다: FC1 3개(FM-1.1 3), FC2 11개(FM-2.2 2, FM-2.4 8, FM-2.6 1), FC3 7개(FM-3.2 3, FM-3.3 4), 유형 없음 2개
  - 잡힌 곳마다: 그 자리 14, phase의 확인 2, task의 회고 6, tasks 끝 1
  - 등급: D — tasks 끝에서 잡힌 실패가 하나다(실패 23)

**스킬로 만들 후보**
- 헤드리스 장면을 차리고 돌려 결과를 옮기는 일: `mktemp -d`에 복제와 `git remote set-head origin main`, 장면의 tasks 브랜치와 run이 만들 꼴의 커밋을 손으로 차리기, `--plugin-dir`·허용 목록·`--output-format stream-json`을 붙인 `claude -p`와 `--resume <세션 id>`로 답을 잇기, 결과 jsonl과 세션 jsonl에서 세션 id·`duration_ms`·막힌 명령·도구 호출 입력을 뽑아 `docs/TOOLS.md` 장면 절의 필드로 옮기기. 스킬로 만들면 장면 아홉(A~I)마다 되풀이된 차림과 필드 뽑기, 허용 목록 빠짐(실패 5·15·20)과 차림 실수(실패 2·17)가 줄어든다 (근거: `001-run-rules` `FRICTION.md` 7행, `002-plan-phase-rules` `FRICTION.md` 25행, `003-eval-review-rules` `FRICTION.md` 28행, 세 task의 장면 phase "한 일")

**하네스 고칠 거리**
1. 계획의 확인이 "돌린 시각이 본문의 마지막 커밋보다 늦다"처럼 커밋 시각에 기대면 본문을 고치는 phase나 고칠 phase에서 참일 수 없다. plan은 돌린 본문의 해시로 견주는 확인을 쓰게 하고, run 8번의 "계획을 바꿔야 하는지" 판정은 고칠 파일이 완료 조건이 시각이나 해시로 보는 파일인지도 본다 (근거: 실패 4, 16). 갈래: plate 자체
   - 이슈 제목: plan·run: 커밋 시각에 기댄 확인이 본문을 고치는 phase와 고칠 phase에서 참이 될 수 없다
   - 이슈 본문: 완료 조건의 확인이 "장면을 돌린 시각이 스킬 본문의 마지막 커밋보다 늦다"였는데, 본문을 고치고 장면을 돌리는 phase는 phase 스킬 5번의 끝 한 커밋과 함께 설 수 없어 본문만 먼저 커밋했고, 회고 뒤 run 8번이 그 본문을 고치는 고칠 phase를 더하자 통과 조건 "task 머리의 완료 조건이 모두 참이다"가 참일 수 없어 수행이 "계획이 틀림"으로 두 번 멈췄다. 원인: plan 스킬의 적는 규칙 "조건"이 돌려 본 결과의 새로움을 무엇으로 견줄지 정하지 않았고, run 스킬 8번 첫머리의 계획 변경 판정이 고칠 파일과 완료 조건의 시각·해시 확인의 관계를 보지 않는다. 해결책: plan의 "조건"에 "돌려 본 결과가 지금 본문의 것인지는 커밋 시각이 아니라 돌릴 때 적은 본문 해시(`git hash-object`)와 `git rev-parse HEAD:<경로>`로 견준다"를 더하고, run 8번의 판정에 "고칠 파일이 완료 조건이 시각이나 해시로 보는 파일이면 그 확인을 어떻게 다시 참으로 둘지 계획에 없으면 멈춘다"를 더한다. 근거: `release-prep`, `cad84b1`, `0b989db`, `584ae16`, `docs/tasks/001-run-rules/done-phase-4.md`, `docs/tasks/002-plan-phase-rules/done-phase-2.md`
2. run 8번이 계획 커밋을 찾는 명령을 `$(…)` 명령 치환으로 적어 권한 검사가 막는다 (근거: 실패 3). 갈래: plate 자체
   - 이슈 제목: run: 8번의 계획 커밋 찾기 명령이 명령 치환이라 헤드리스에서 막힌다
   - 이슈 본문: 고칠 phase를 더하기 전에 계획 커밋으로 고친 문제를 찾는 명령 `git log … $(git log -1 --format=%h -- …/retro.md)..HEAD -- docs/tasks/`가 Claude Code 권한 검사의 "nested command" 승인 요구로 막혀 run이 나눠 불렀다. 같은 본문의 "PR을 연다"는 이 제약을 이미 적고 있다. 원인: run 스킬 8번의 명령 글. 해결책: 두 단계로 적는다(먼저 `git log -1 --format=%h -- docs/tasks/NNN-slug/retro.md`로 해시를 얻고, 그 해시를 넣어 `git log`를 부른다). 근거: `release-prep`, `1462ac9` `docs/tasks/001-run-rules/done-phase-3.md`
3. run이 두 번째 계획 수정에서 결정 줄을 더하지 않았다 (근거: 실패 11, 규칙 준수의 `0b989db`). 갈래: plate 자체
   - 이슈 제목: run: 계획 수정마다 결정 줄을 더하는 규칙이 같은 멈춤 안의 두 번째 수정에서 빠진다
   - 이슈 본문: 한 고칠 phase에서 "계획이 틀림"으로 두 번 멈춰 계획을 두 번 고쳤는데, 첫 수정만 task 머리와 tasks 머리의 결정에 줄을 더하고 두 번째는 더하지 않았다. 원인: run 스킬 "멈춘다" 4의 "고친 것과 까닭을 결정에 한 줄 더한다"가 커밋 전 점검에 들지 않는다. 해결책: "멈춘다" 4의 커밋 앞에 "이번 수정의 결정 줄이 task 머리(와 고쳤으면 tasks 머리)에 있는지 보고 커밋한다"는 점검을 두고, 계획 수정마다 결정 줄 하나라고 못박는다. 근거: `release-prep`, `0b989db` `docs/tasks/001-run-rules/plan.md`
4. retro가 회고 절에서 "문제 아님"으로 판정한 `남은 것` 줄을 `FRICTION.md`에 `문제`로 적어 eval의 셈과 갈린다 (근거: 실패 21, 실패 10·19가 그 예). 갈래: plate 자체
   - 이슈 제목: retro: FRICTION.md의 문제 줄과 회고 절 "남은 것"의 판정 관계가 정해져 있지 않다
   - 이슈 본문: 회고 절 "남은 것"에서 "문제 아님"으로 판정한 줄이 `FRICTION.md`에 `문제` 줄로 들어가, eval 2번의 `남은 것:` 규칙(회고가 "문제"로 판정한 것만 센다)과 `FRICTION.md` 문제 줄의 셈이 갈렸다. 원인: retro 스킬 5번이 `FRICTION.md` 문제 줄이 회고 절의 "문제"와 같아야 하는지, "문제 아님"이지만 볼 거리인 줄은 어느 갈래(경계 밖 같은 것)로 적는지 정하지 않는다. 해결책: retro 5번에 "`문제` 줄은 회고 절 '문제'의 줄만, '문제 아님'으로 판정했지만 tasks 끝에 볼 줄은 `경계 밖`으로 적는다"를 더한다. 근거: `release-prep`, `3bd523a`, `44f2790` `docs/tasks/FRICTION.md`
5. eval의 규칙 준수 표와 정해 둔 물음 목록이 run의 새 동작을 담지 않는다 (근거: 하네스에서 걸린 것). 갈래: plate 자체
   - 이슈 제목: eval: 규칙 준수 표에 RUNLOG 커밋이, 정해 둔 물음에 `권한`이 없다
   - 이슈 본문: run이 회고 뒤 `NNN-slug: RUNLOG`, 코드 평가·하네스 eval 뒤 `<tasks 이름>: RUNLOG` 커밋을 두고 시작할 때 `권한`을 묻게 바뀌었지만, eval 스킬의 3번 규칙 준수 표에는 그 커밋 꼴(넣어도 되는 파일 `RUNLOG.md`와 사용량 까닭을 적은 `docs/TOOLS.md`)이 없어 보지 못하고, 낱말의 "정해 둔 물음" 목록에 `권한`이 없다. 원인: eval 스킬 3번의 표와 낱말 "정해 둔 물음". 해결책: 표에 `NNN-slug: RUNLOG`, `<tasks 이름>: RUNLOG` 행(만든 스킬 run, 넣어도 되는 파일 `RUNLOG.md`와 `docs/TOOLS.md`)을 더하고, 정해 둔 물음 목록에 `권한`을 더한다. 근거: `release-prep`, `77018b6`, `7ea7eef` `docs/tasks/RUNLOG.md`
6. phase가 run이 띄운 호출과 사용자가 직접 부른 호출을 가르지 못한다 (근거: 실패 19). 갈래: plate 자체
   - 이슈 제목: phase: run이 띄운 호출인지 가르는 표지가 없어 직접 부른 꼴로 보고한다
   - 이슈 본문: task 폴더와 phase 번호를 주어 헤드리스로 부른 phase가 사용자가 직접 부른 꼴로 보고하고 run 안내를 붙였다. 원인: phase 스킬의 끝 보고가 부른 쪽을 가르는 기준을 두지 않는다(run이 맡기는 글에도 표지가 없다). 해결책: run이 맡기는 글에 "실행 스킬이 띄운 에이전트다"를 넣고, phase(와 check, retro)는 그 글이 있을 때만 run의 꼴로 보고한다고 적는다. 근거: `release-prep`, `86408de` `docs/tasks/002-plan-phase-rules/done-phase-3.md`
7. plan이 앞 task가 고친 것에 기대는 phase의 읽을 것에 이슈 번호만 적고 절이나 커밋을 적지 않는다 (근거: 실패 22). 갈래: plate 자체
   - 이슈 제목: plan: 앞 task의 변경에 기대는 phase의 읽을 것에 절이나 커밋을 적게 한다
   - 이슈 본문: 앞 task들이 고친 규칙을 시험하는 phase의 읽을 것이 이슈 번호만 가리켜, 수행이 이슈 트래커와 브랜치 diff로 계획 밖의 근거를 찾았다. 원인: plan 스킬 적는 규칙 "읽을 것"이 앞 task의 산출물을 가리킬 때 무엇까지 적을지 정하지 않는다(#41·#42는 같은 task 안의 앞 phase만 다룬다). 해결책: "읽을 것"에 "앞 task의 변경에 기대면 그 파일의 절 이름과 바뀐 글을 찾을 수 있게 적는다(이슈 번호만으로 가리키지 않는다)"를 더한다. 근거: `release-prep`, `a23ac01` `docs/tasks/004-tests-version/done-phase-1.md`
8. plan이 돌려 보는 확인(장면)을 정할 때 차림이 기대한 자리에 닿는지, 기대가 해결책 하나로 좁혀지지 않는지, 결정과 TODO가 어긋나지 않는지 보지 않는다 (근거: 실패 1, 6, 12, 13, 18). 갈래: plate 자체
   - 이슈 제목: plan: 장면으로 돌려 보는 확인의 차림과 기대를 초안 점검에서 본다
   - 이슈 본문: 스킬을 임시 복제본에서 돌려 보는 확인이 차림의 앞 단계(회고 통과, 고칠 것이 나오는 자리)를 정하지 않아 같은 장면을 세 번까지 다시 차렸고, 기대를 해결책 한 차림으로 좁혀 맞는 결과를 실패로 만들어 멈췄고, 결정("승인하지 않는다")과 TODO("다음 초안까지 잇는다")가 어긋나 수행이 짐작으로 나아갔으며, 새로 더한 "갈래마다 확인" 규칙을 그 task의 완료 조건이 따르지 않았다. 원인: plan 스킬 6번의 초안 점검이 돌려 보는 확인의 차림·기대·결정과의 맞물림을 보지 않는다. 해결책: 6번 점검에 "돌려 보는 확인마다 그 차림이 기대한 자리까지 앞 단계를 지나 닿는지, 기대가 해결 방식이 아니라 관찰할 결과로 적혔는지, 결정과 TODO가 같은 멈출 자리를 말하는지"를 더한다. 근거: `release-prep`, `fe2879f`, `cad84b1`, `docs/tasks/001-run-rules/done-phase-2.md`, `docs/tasks/001-run-rules/done-phase-4.md`, `docs/tasks/002-plan-phase-rules/done-phase-2.md`
9. 헤드리스 장면의 차림 사실이 `docs/TOOLS.md`에 모자라다: 허용 목록에 스킬이 부르는 명령이 빠졌고, 프롬프트 자리, 복제본의 `origin/HEAD`, 세션 기록 위치가 적혀 있지 않다 (근거: 실패 2, 5, 14, 15, 17, 20). 갈래: 이 프로젝트만
   - 고칠 곳: `docs/TOOLS.md`
   - 해결책: "스킬을 헤드리스로 돌려 볼 때의 허용 목록"에 `git remote`, `git rm`, `git merge-base`, `git symbolic-ref`, `git switch`, `git branch`, `claude plugin validate`, `grep`, `cut`을 더하고, 프롬프트는 `-p` 바로 뒤에 둔다(`--allowedTools`가 뒤의 값을 삼킨다), 복제한 뒤 `git remote set-head origin main`을 한다, 세션 기록은 `${CLAUDE_CONFIG_DIR:-~/.claude}/projects/` 아래에 있다를 적는다
10. 스킬 description 길이를 보는 확인이 없어 1024자를 넘은 description이 phase 확인과 회고를 지나왔다 (근거: 실패 23). 갈래: 이 프로젝트만
    - 고칠 곳: `tests/test_skill_rules.py`
    - 해결책: 모든 `plugins/plate/skills/*/SKILL.md`의 description이 1024자 이하인지 보는 테스트를 더해 명령 절의 테스트가 잡게 한다

**하네스에서 걸린 것**
- eval 스킬 3번의 규칙 준수 표에 run이 이번에 더한 `NNN-slug: RUNLOG`, `<tasks 이름>: RUNLOG` 커밋 꼴이 없어 그 커밋 6개를 보지 않았다(고칠 거리 5)
- eval 스킬 낱말의 "정해 둔 물음" 목록에 `권한`이 없어, 정의(물은 자리가 `멈춤`이 아닌 줄)대로 정해 둔 물음으로 셌다
- 회고 절에서 "문제 아님"으로 판정된 줄이 `FRICTION.md`에 `문제`로 적혀 있어(6·19·23행), eval 2번의 `남은 것:` 규칙으로는 실패가 아니지만 `FRICTION.md` 문제 줄 규칙으로는 실패라 둘이 갈렸다. `FRICTION.md` 문제 줄을 따라 실패로 셌고 잡힌 곳은 task의 회고로 두었다(고칠 거리 4)
- 실패 4와 그 뒤 두 `멈춤` 줄, 실패 13과 그 `멈춤` 줄은 같은 실패로 하나씩 셌다
