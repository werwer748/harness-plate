# 하네스 eval

## eval 1

**대상**
- tasks: `issue-fixes`, task 6개, phase 12개(더한 phase 0개)
- 커밋: `d8072a3`부터 `5695f77`까지 44개
- 기록: `RUNLOG.md` 에이전트 줄 35줄, 물은 줄 7줄. `FRICTION.md` 18줄. `review.md` 평가 1

**실패**
1. `001-ci-trust` phase 3에서 푸시 훅이 셋업된 시험 저장소 `main`의 푸시를 막았다. 계획의 결정은 그 푸시를 "시험 장면의 일"로 적고 사용자의 단계로 두지 않았다 (`docs/tasks/001-ci-trust/done-phase-3.md` 하네스에서 걸린 것, `RUNLOG.md` 멈춤 두 줄, `FRICTION.md` 001 첫 줄). 유형: FM-2.4 정보를 감춤. 잡힌 곳: 그 자리
2. `001-ci-trust` 계획의 run 전 사용자 준비에 `gh auth`의 `workflow` 범위가 빠져 phase 3이 사용자를 기다렸다. 첫 답이 해결책을 하지 않은 채라 같은 막힘을 한 번 더 물었다 (`RUNLOG.md` 7·8줄, `FRICTION.md` 001 셋째·다섯째 줄). 유형: FM-2.4 정보를 감춤. 잡힌 곳: 그 자리
3. `001-ci-trust` phase 3의 읽을 것과 결정이 가리킨 `~/plate-rail-test`(스크립트, 앞선 로그)가 없어 수행이 스크립트를 새로 썼다 (`docs/tasks/001-ci-trust/done-phase-3.md` 계획과 달라진 점, 하네스에서 걸린 것). 유형: FM-2.4 정보를 감춤. 잡힌 곳: 그 자리
4. `001-ci-trust` 완료 조건 2의 둘째 확인 "로그에 되돌리는 단계가 성공한 줄"을 Actions 로그가 내지 않아 잡 API로 대신 봤다 (`docs/tasks/001-ci-trust/done-phase-3.md` 하네스에서 걸린 것, `FRICTION.md` 001 넷째 줄). 유형: FM-3.2 검증이 없거나 모자람 — 확인의 글대로는 조건을 볼 수 없었다. 잡힌 곳: 그 자리
5. `002-run-rules` phase 1의 통과 조건 `grep -n '"\$('`가 파일 전체를 훑어, 금지하는 꼴을 설명하는 글까지 잡아 수행이 글로 풀어 적었다 (`docs/tasks/002-run-rules/done-phase-1.md` 하네스에서 걸린 것). 유형: FM-3.2 검증이 없거나 모자람 — 확인이 보아야 할 줄(명령 줄)을 가리지 못했다. 잡힌 곳: 그 자리
6. `003-plan-rules` phase 2의 `plugins/plate/skills/plan/SKILL.md` Edit가 auto mode 분류기의 판정 없음으로 세 번 막혀 run이 네 번 멈췄다 (`docs/tasks/003-plan-rules/done-phase-2.md` 하네스에서 걸린 것, `RUNLOG.md` 멈춤 네 줄). 유형: 유형 없음 — 에이전트 사이의 실패가 아니라 실행 환경의 권한 모드가 막았다. 잡힌 곳: 그 자리
7. `003-plan-rules` phase 2의 통과 조건 "phase 1의 통과 조건 확인을 다시 돌린다"가 다른 phase를 가리키기만 해, 수행은 task 머리의 글로, 확인은 `done-phase-1.md`로 서로 다른 것을 봤다 (`docs/tasks/003-plan-rules/done-phase-2.md` 하네스에서 걸린 것, 확인 1 하네스에서 걸린 것). 유형: FM-2.4 정보를 감춤. 잡힌 곳: 그 자리
8. `004-retro-phase` phase 2에서 7과 같은 꼴이 되풀이됐다 (`docs/tasks/004-retro-phase/done-phase-2.md` 하네스에서 걸린 것, 확인 1 하네스에서 걸린 것). 유형: FM-2.4 정보를 감춤. 잡힌 곳: 그 자리
9. `004-retro-phase` 계획의 TODO 여럿이 "4번에 생긴다.", "적는 규칙에 생긴다."로 시작해 동사가 없어 수행이 "더한다"로 짐작해 읽었다 (`docs/tasks/004-retro-phase/done-phase-2.md` 하네스에서 걸린 것, `FRICTION.md` 004 둘째 줄). 유형: FM-2.2 묻지 않고 짐작함. 잡힌 곳: 그 자리
10. `004-retro-phase` 회고에서 실린 `plate:retro` 본문이 이 task가 고친 작업 트리의 글이 아니라 고치기 전 글이었다 (`FRICTION.md` 004 셋째 줄). 유형: FM-1.4 대화 기록을 잃음 — 세션이 고치기 전 상태의 스킬을 들고 있었다. 잡힌 곳: task의 회고
11. `005-eval-rules` 완료 조건 1이 run의 낱말 "계획 파일"을 "(tasks 머리, task 머리)"로 좁혀 옮겨, 수행이 표에 `phase-N.md`의 계획 다섯 항목을 더 넣었다 (`docs/tasks/005-eval-rules/done-phase-2.md` 계획과 달라진 점, 하네스에서 걸린 것). 유형: FM-2.4 정보를 감춤. 잡힌 곳: 그 자리
12. `005-eval-rules` phase 2에서 7과 같은 꼴이 다시 되풀이됐다(이번에는 두 쪽이 같은 줄을 봤다) (`FRICTION.md` 005 둘째 줄). 유형: FM-2.4 정보를 감춤. 잡힌 곳: task의 회고
13. `005-eval-rules` 회고에서 10과 같이 고치기 전 retro 본문이 실렸다 (`FRICTION.md` 005 셋째 줄). 유형: FM-1.4 대화 기록을 잃음. 잡힌 곳: task의 회고
14. `006-release` phase 1의 읽을 것 `git show e521e80 -- …`가 머지 커밋이라 diff를 내지 않아 수행이 `git diff e521e80^1 e521e80`으로 바꿨다 (`docs/tasks/006-release/done-phase-1.md` 하네스에서 걸린 것). 유형: FM-2.4 정보를 감춤. 잡힌 곳: 그 자리
15. `006-release` phase 1의 TODO가 Claude Code 버전을 001 phase 3의 기록에서 가져오라 했지만 그 기록에 없어 수행이 이 Mac의 `claude --version`을 썼다 (`docs/tasks/006-release/done-phase-1.md` 하네스에서 걸린 것, 남은 것). 유형: FM-2.4 정보를 감춤. 잡힌 곳: 그 자리
16. `006-release` 회고에서 10과 같이 고치기 전 retro 본문이 실렸다 (`FRICTION.md` 006 셋째 줄). 유형: FM-1.4 대화 기록을 잃음. 잡힌 곳: task의 회고
17. tasks 머리 완료 조건 2의 셋째 확인(`diff -r -x __pycache__ <시험 저장소 .plate> plugins/plate`)이 견줄 시점을 적지 않아, 뒤 task들이 `plugins/plate`를 바꾼 HEAD에서 실패했다. `001-ci-trust` 회고는 그 시점에 통과시켰다 (`review.md` 평가 1 완료 조건 2, 하네스에서 걸린 것 둘째 줄). 유형: FM-3.2 검증이 없거나 모자람 — 확인이 시점을 정하지 않아 조건을 다 보지 못했다. 잡힌 곳: tasks 끝
18. review의 "바뀐 코드 파일"이 `.md`를 빼서, 결과물이 스킬 본문(마크다운)인 이 tasks에서 코드 평가가 버전 2줄만 봤다 (`review.md` 평가 1 하네스에서 걸린 것 첫 줄). 유형: FM-3.2 검증이 없거나 모자람. 잡힌 곳: tasks 끝

**기준**
- 결과 성공
  - 근거: `review.md` 평가 1의 완료 조건 확인 22개 가운데 통과 21, 실패 1(완료 조건 2의 셋째), 측정 못함 0. 기능 적합성 B
  - 근거: `001-ci-trust` 마지막 회고 1 통과
  - 근거: `002-run-rules` 마지막 회고 1 통과
  - 근거: `003-plan-rules` 마지막 회고 1 통과
  - 근거: `004-retro-phase` 마지막 회고 1 통과
  - 근거: `005-eval-rules` 마지막 회고 1 통과
  - 근거: `006-release` 마지막 회고 1 통과
  - 등급: C — 실패한 확인이 있어 A·B에 들지 못하고, 기능 적합성이 B(결과물의 동작은 맞다)인 칸이다
- 일관성
  - 근거: `001-ci-trust` phase 1 첫 시도 통과
  - 근거: `001-ci-trust` phase 2 첫 시도 통과
  - 근거: `001-ci-trust` phase 3 수행 2번, 확인 1번째에 통과
  - 근거: `002-run-rules` phase 1 첫 시도 통과
  - 근거: `002-run-rules` phase 2 첫 시도 통과
  - 근거: `003-plan-rules` phase 1 첫 시도 통과
  - 근거: `003-plan-rules` phase 2 수행 4번, 확인 1번째에 통과
  - 근거: `004-retro-phase` phase 1 첫 시도 통과
  - 근거: `004-retro-phase` phase 2 첫 시도 통과
  - 근거: `005-eval-rules` phase 1 첫 시도 통과
  - 근거: `005-eval-rules` phase 2 첫 시도 통과
  - 근거: `006-release` phase 1 첫 시도 통과
  - 근거: `001-ci-trust`, `002-run-rules`, `003-plan-rules`, `004-retro-phase`, `005-eval-rules`, `006-release` 회고 모두 첫 시도 통과
  - 첫 시도 통과율: 16 ÷ 18 = 88.9%
  - 등급: B — 75% 이상 90% 미만
- 효율
  - 합계: 에이전트 35개, 토큰 2449744, 도구 호출 339, 시간 2728초
  - 근거: `수행 001-ci-trust phase 3` 되풀이 — 같은 역할이 두 번째로 맡았다(토큰 95046, 도구 호출 26, 298초)
  - 근거: `수행 003-plan-rules phase 2` 되풀이 — 같은 역할이 두 번째로 맡았다(토큰 63536, 도구 호출 11, 80초)
  - 근거: `수행 003-plan-rules phase 2` 되풀이 — 같은 역할이 세 번째로 맡았다(토큰 58723, 도구 호출 9, 38초)
  - 근거: `수행 003-plan-rules phase 2` 되풀이 — 같은 역할이 네 번째로 맡았다(토큰 66774, 도구 호출 10, 64초)
  - 되풀이 몫: 토큰 284079 ÷ 2449744 = 11.6%, 도구 호출 56 ÷ 339 = 16.5%, 시간 480 ÷ 2728 = 17.6%
  - 등급: B — 가장 높은 비율(시간 17.6%)이 10% 이상 20% 미만
- 규칙 준수
  - 근거: `d8072a3`(plan), phase 커밋 12개, 확인 커밋 12개, 통과 커밋 12개, 회고 커밋 6개, `5695f77`(코드 평가)를 표에 대어 봄 → 넣어도 되는 파일 밖을 넣은 커밋 없음. `004-retro-phase: phase 1`(`15eae74`)의 `plugins/plate/skills/eval/SKILL.md`는 그 phase의 TODO가 가리킨 파일이다
  - 근거: `done-phase-N.md` 12개 모두 기록 다섯 절과 `## 확인 1`의 판정이 있고, `retro.md` 6개 모두 회고 1의 판정이 있다
  - 근거: `docs/tasks/003-plan-rules/done-phase-2.md` 확인 1이 통과 조건 셋째를 돌리려고 `done-phase-1.md`를 읽었다. check 스킬 1번의 읽을 것(task 머리, 그 `phase-N.md`, 명령 절) 밖이다
  - 근거: 회고 절의 문제가 모두 "없음"이라 기준이 "범위"·"계획"인 문제가 없다. 테스트 먼저인 phase는 없다
  - 등급: C — 확인이 자기 스킬의 읽기 범위 밖을 읽은 곳이 하나다
- 사람 개입률
  - 근거: 실행 방식 → 정해 둔 물음
  - 근거: `001-ci-trust` phase 3 막힘의 해결책 → 멈춤
  - 근거: `001-ci-trust` phase 3 막힘의 해결책(두 번째) → 멈춤
  - 근거: `003-plan-rules` phase 2 막힘(분류기) → 멈춤
  - 근거: `003-plan-rules` phase 2 두 번째 막힘 → 멈춤
  - 근거: `003-plan-rules` 사용자가 규칙을 넣었는지 → 멈춤
  - 근거: `003-plan-rules` phase 2 세 번째 막힘 → 멈춤
  - 개입률: 멈춤 6 ÷ 에이전트 35 = 17.1%
  - 등급: D — 10% 넘고 20% 이하
- 실패 양상
  - 유형마다: FC1 3개(FM-1.4 3), FC2 10개(FM-2.2 1, FM-2.4 9), FC3 4개(FM-3.2 4), 유형 없음 1개
  - 잡힌 곳마다: 그 자리 12, phase의 확인 0, task의 회고 4, tasks 끝 2
  - 등급: E — tasks 끝에서 잡힌 실패가 둘(17, 18)이다

**스킬로 만들 후보**
- CI 장면 확인(시험 저장소를 새로 받아 `.plate`를 `plugins/plate`에 `diff -r -x __pycache__`로 견주기, `.plate`의 마지막 커밋 시각과 `gh run list`의 실행 시각 비교, `gh pr view --json state,comments`의 첫 줄과 등급 뽑기, `gh run view --log`와 `--json jobs`의 단계 결과)를 스크립트나 스킬로 두면 phase 3의 수행·확인과 회고, 코드 평가가 손으로 네 번 돌린 묶음이 줄어든다 (근거: `001-ci-trust` `FRICTION.md`의 스킬 후보 줄, `review.md` 평가 1 완료 조건 2)
- 바뀐 규칙의 낱말로 맥락 문서와 다른 스킬을 `grep`해 나온 줄을 하나씩 읽어 어긋남을 보는 확인을 스킬로 두면, phase마다 낱말 고르기와 줄 읽기를 손으로 되풀이하는 것이 줄어든다 (근거: `002-run-rules`, `003-plan-rules`, `004-retro-phase`, `005-eval-rules`, `006-release`의 `done-phase-N.md` 확인 절의 "어긋나는 줄" 확인)

**하네스 고칠 거리**
1. plan이 계획에 적는 바깥 사실(저장소 밖 경로, 읽을 것의 명령이 내는 것, 가져올 값이 있는 기록, run 전 사용자가 할 준비와 훅이 막을 동작)을 실제에 대어 보지 않는다 (근거: 실패 1, 2, 3, 14, 15). 갈래: plate 자체
   - 이슈 제목: plan: 계획이 가리키는 경로·명령·값과 사용자 준비를 초안 전에 실제에 대어 본다
   - 이슈 본문: 한 tasks에서 phase의 읽을 것이 없는 저장소 밖 경로를 가리켰고, 읽을 것의 `git show <머지 커밋> -- <파일>`이 diff를 내지 않았고, TODO가 값을 가져오라 한 기록에 그 값이 없었다. 결정은 run 전 사용자 준비로 시크릿만 적어 `gh auth`의 `workflow` 범위와 푸시 훅이 막을 셋업된 저장소의 기본 브랜치 푸시를 빠뜨려 phase가 막히고 실행이 두 번 멈췄다. 원인: plan 스킬 6번의 초안 전 점검이 완료 조건과 통과 조건의 확인만 대어 보고, 읽을 것과 TODO가 가리키는 바깥 사실과 사용자의 준비는 대어 보지 않는다. 해결책: 6번의 초안 전 점검에 (1) 읽을 것과 결정이 가리키는 저장소 밖 경로가 있는지, (2) 읽을 것의 명령을 돌려 기대한 것이 나오는지, (3) 가져올 값이 가리킨 기록에 있는지, (4) phase가 하는 푸시·권한·인증이 훅이나 권한 범위에 막히지 않는지 보고 막히면 사용자의 단계로 결정에 적는 것을 더한다. 근거: `issue-fixes`, `6fa174e` `714d75e` `docs/tasks/001-ci-trust/done-phase-3.md` `docs/tasks/006-release/done-phase-1.md` `docs/tasks/RUNLOG.md`
2. 통과 조건이 다른 phase의 확인을 "다시 돌린다"로 가리키기만 해 phase와 check가 서로 다른 것을 보고, check가 읽기 범위 밖을 읽게 된다 (근거: 실패 7, 8, 12, 규칙 준수의 근거 `003-plan-rules` phase 2 확인 1). 갈래: plate 자체
   - 이슈 제목: plan: 앞 phase의 확인을 다시 돌리게 할 때 그 확인을 통과 조건에 옮겨 적는다
   - 이슈 본문: 한 tasks의 task 셋에서 통과 조건이 "phase 1의 통과 조건 확인을 다시 돌린다"로 적혀, phase 스킬은 다른 phase 파일을 읽지 못해 task 머리의 글로 대신 봤고 check 스킬은 읽을 것 밖인 `done-phase-1.md`를 읽거나(한 번) 그 줄만 읽고 돌렸다. 원인: plan 스킬의 적는 규칙(phase는 task 머리와 그 phase 파일만으로 할 수 있다)이 통과 조건이 다른 phase를 가리키는 꼴을 막는 줄로 이어지지 않고, 6번 초안 전 점검도 이 꼴을 보지 않는다. 해결책: 적는 규칙 "조건"에 다른 phase의 확인을 다시 돌릴 때는 그 확인 글을 이 phase의 통과 조건에 옮겨 적고 "phase N의 확인" 같은 가리킴만 두지 않는다는 줄을 더하고, 6번 점검에서 통과 조건에 다른 phase를 가리키는 글이 있으면 고친다. 근거: `issue-fixes`, `0200e13` `13c13c9` `3e7379d` `f4df654` `docs/tasks/003-plan-rules/done-phase-2.md` `docs/tasks/004-retro-phase/done-phase-2.md`
3. 같은 tasks에서 plate의 스킬을 고쳐도 세션에 실린 스킬 본문이 고치기 전 글이라 뒤의 회고와 eval이 고친 규칙을 쓰지 않는다 (근거: 실패 10, 13, 16, 하네스에서 걸린 것 첫 줄). 갈래: plate 자체
   - 이슈 제목: run: tasks가 plate 스킬을 고치면 뒤의 에이전트가 작업 트리의 스킬 본문을 읽게 한다
   - 이슈 본문: plate 저장소에서 retro와 eval 스킬을 고친 tasks의 뒤 task 회고 세 번과 끝의 eval에서, 스킬 도구가 실은 본문이 작업 트리의 고친 글이 아니라 세션이 시작할 때 실린 고치기 전 글이었다. 원인: run 스킬이 에이전트에게 스킬 이름으로만 일을 맡기고, 세션에 실린 플러그인은 작업 트리의 스킬을 다시 읽지 않는다. 해결책: run이 에이전트를 띄울 때 tasks의 커밋이 그 스킬의 `SKILL.md`를 바꿨으면 "작업 트리의 `<경로>/SKILL.md`를 읽어 그 절차를 따른다"를 함께 넘긴다. 또는 이런 tasks의 계획에 뒤 회고는 고치기 전 규칙으로 돈다는 것을 결정으로 적게 한다. 근거: `issue-fixes`, `78e37d2` `ef4a589` `9472246` `docs/tasks/FRICTION.md`
4. review의 "바뀐 코드 파일"이 `.md`를 빼서, 결과물이 마크다운(스킬 본문, 워크플로 양식)인 프로젝트에서 코드 평가의 네 범주가 결과물을 보지 못한다 (근거: 실패 18). 갈래: plate 자체
   - 이슈 제목: review: 마크다운이 결과물인 프로젝트에서 바뀐 코드 파일이 비지 않게 한다
   - 이슈 본문: 스킬 본문 7개와 워크플로 양식(셸·파이썬 단계)을 바꾼 tasks에서 코드 평가가 매니페스트의 버전 2줄만 평가했다. 원인: review 스킬의 낱말 "바뀐 코드 파일"이 `.md`를 모두 뺀다. 해결책: 맥락 문서(`docs/ARCHITECTURE.md`)가 결과물로 적은 `.md` 경로(예: 스킬 본문)는 바뀐 코드 파일에 넣거나, 마크다운 안의 코드 블록(워크플로 양식 같은 것)을 코드로 보게 하고, 그 판단을 평가 절의 대상에 적는다. 근거: `issue-fixes`, `5695f77` `docs/tasks/review.md`
5. plan이 확인 글을 도구가 실제로 내는 것, 보아야 할 줄의 범위, 견줄 시점에 대어 쓰지 않아 확인이 글대로 돌 수 없거나 나중 task가 거짓으로 만든다 (근거: 실패 4, 5, 17). 갈래: plate 자체
   - 이슈 제목: plan: 확인 글을 도구의 실제 출력, 대상 줄, 견줄 시점에 대어 쓴다
   - 이슈 본문: 한 tasks에서 "로그에 단계가 성공한 줄이 있다"는 Actions 로그가 내지 않는 줄이었고, "쓰지 않는다"를 보는 확인이 파일 전체 `grep`이라 금지를 설명하는 글까지 잡았고, 앞 task의 결과를 `plugins/plate`와 견주는 tasks 완료 조건이 시점을 적지 않아 뒤 task들이 그 디렉터리를 바꾼 끝에서 실패했다. 원인: plan 스킬의 적는 규칙 "조건"과 6번의 초안 전 점검이 확인이 무엇을 내는지, 어느 줄을 보는지, 어느 시점의 것과 견주는지를 다루지 않는다. 해결책: "조건"에 (1) 도구 출력을 보는 확인은 그 도구가 실제로 내는 필드나 줄로 적고, (2) 금지를 보는 `grep`은 대상 줄(명령 줄, 코드 블록)로 좁히고, (3) 뒤 task가 바꿀 수 있는 대상과 견주는 확인은 견줄 커밋이나 task 끝을 적는다는 줄을 더한다. 근거: `issue-fixes`, `6fa174e` `e23f844` `5695f77` `docs/tasks/001-ci-trust/done-phase-3.md` `docs/tasks/002-run-rules/done-phase-1.md` `docs/tasks/review.md`
6. plan이 TODO를 동사 없이 쓰거나 다른 스킬의 낱말을 정의보다 좁혀 옮겨, 수행이 짐작하거나 계획과 다르게 했다 (근거: 실패 9, 11). 갈래: plate 자체
   - 이슈 제목: plan: TODO는 할 일의 동사로 쓰고, 다른 스킬의 낱말은 정의에 대어 옮긴다
   - 이슈 본문: 한 tasks에서 TODO 여럿이 "4번에 생긴다."처럼 동사 없이 적혀 수행이 "더한다"로 짐작해 읽었고, 완료 조건이 run 스킬의 낱말 "계획 파일"을 정의보다 좁게 옮겨 수행이 다른 완료 조건을 지키려고 계획과 다르게 했다. 원인: plan 스킬의 적는 규칙 "TODO"가 TODO의 글꼴(할 일의 동사로 끝남)을 정하지 않고, 다른 스킬의 낱말을 옮길 때 그 정의를 대어 보는 규칙이 없다. 해결책: "TODO"에 할 일의 동사(더한다, 고친다, 지운다)로 쓴다는 줄을, 6번 점검에 조건과 TODO가 다른 스킬의 낱말을 쓰면 그 스킬의 낱말 절과 대어 본다는 줄을 더한다. 근거: `issue-fixes`, `15eae74` `f4df654` `docs/tasks/004-retro-phase/done-phase-2.md` `docs/tasks/005-eval-rules/done-phase-2.md`
7. auto mode 분류기가 `plugins/plate/skills/**`의 Edit를 판정 없음으로 막고 `settings.local.json`의 허용 규칙으로도 풀리지 않아 실행이 네 번 멈췄다 (근거: 실패 6). 갈래: 이 프로젝트만
   - 고칠 곳: `docs/TOOLS.md`
   - 해결책: Claude Code 절에 auto mode에서 이 저장소의 스킬 본문 Edit가 분류기에 막히고 허용 규칙으로 풀리지 않으며 bypass 모드에서 들어갔다는 것을 날짜와 함께 적고, 스킬 본문을 고치는 tasks는 run 전에 권한 모드를 정해 두라고 적는다
8. 코드 평가가 커버리지, 중복, 보안 검사를 이 환경에 도구가 없어 재지 못했다 (근거: `review.md` 평가 1 하네스에서 걸린 것 셋째 줄). 갈래: 이 프로젝트만
   - 고칠 곳: `docs/ARCHITECTURE.md`
   - 해결책: 명령 절에 커버리지 명령(`python3 -m coverage run -m unittest discover -s tests` 같은 것)을 쓰려면 `coverage`를 깔아 두거나, 이 프로젝트는 커버리지·중복·보안 검사 도구를 두지 않는다고 적어 코드 평가가 매번 찾지 않게 한다

**하네스에서 걸린 것**
- 이 eval에서 실린 `plate:eval` 본문이 작업 트리의 `plugins/plate/skills/eval/SKILL.md`가 아니라 `005-eval-rules`가 고치기 전 글이었다(2번 표 아래의 측정 못함 줄 규칙, 3번 표의 `NNN-slug: phase N 통과`·`plan: NNN-slug 수정` 행이 없음). 이 tasks가 고친 작업 트리의 두 규칙을 따랐다: 코드 평가의 측정 못함 줄은 실패로 세지 않고 고칠 거리 8로만 봤고, 통과 커밋 12개를 표에 대어 봤다. 고치기 전 글로 세어도 tasks 끝의 실패가 셋이 될 뿐 등급은 같다
- `docs/tasks/RUNLOG.md`의 마지막 두 줄(`006-release` 회고, 코드 평가)은 작업 트리에만 있고 커밋되지 않았다. 작업 트리의 것을 읽어 셌고, 이 eval은 `eval.md`만 커밋하므로 그 변경은 그대로 둔다
- `review.md` 하네스에서 걸린 것 넷째 줄(review 1번의 예외대로 기록의 줄만 읽음)은 규칙을 따른 것이라 실패로 세지 않았다
