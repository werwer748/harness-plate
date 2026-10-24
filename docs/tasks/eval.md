# 하네스 eval

## eval 1

**대상**
- tasks: `pr-ci`, task 5개, phase 20개(더한 phase 10개)
- 커밋: `7616256`부터 `d094722`까지 87개
- 기록: `RUNLOG.md` 에이전트 줄 57줄, 물은 줄 12줄. `FRICTION.md` 52줄. `review.md` 평가 1

**실패**
1. `001-ci-review` phase 1이 review의 "설치를 돌리지 않는다"를 2번이 아닌 낱말의 명령 절 정의에 두어 check, retro와 적은 자리가 다르다. task 머리 완료 조건 1과 2의 확인이 맞물려 다른 자리를 둘 수 없었다 (`docs/tasks/001-ci-review/done-phase-1.md`의 하네스에서 걸린 것, `FRICTION.md` 3줄). 유형: 유형 없음 — 계획의 두 확인이 맞물려 생긴 글 자리의 차이이고, 에이전트가 어기거나 놓친 것이 없다. 잡힌 곳: 그 자리
2. 결정의 이유("PR 코드에 숨은 지시가 있어도 에이전트에게는 머지 권한이 없다")와 달리, PR이 바꾼 코드나 `AGENTS.md`의 지시가 PR 모드 review의 등급 묶음을 올려 자동 머지를 이끌 길이 남았다. `002-ci-workflow`의 워크플로도 막지 않고 tasks 끝까지 열려 있다 (`docs/tasks/001-ci-review/done-phase-2.md`의 하네스에서 걸린 것, `FRICTION.md` 4줄, 10줄). 유형: FM-1.1 과제 명세를 어김. 잡힌 곳: 그 자리
3. `001-ci-review` phase 2·3의 확인 에이전트와 회고 에이전트에 phase 1이 고치기 전의 check, retro 본문이 실렸다. 설치가 "없음"이라 판정에는 걸리지 않았다 (`docs/tasks/001-ci-review/done-phase-2.md`·`done-phase-3.md`의 확인 1의 하네스에서 걸린 것, `FRICTION.md` 5줄). 유형: FM-1.4 대화 기록을 잃음 — 앞 상태의 스킬 본문으로 돌았다. 잡힌 곳: 그 자리
4. 이미 셋업된 프로젝트에서 setup을 다시 불러 CI 에이전트를 승인하면 편집 훅이 `.github/workflows/plate-review.yml`의 Write를 막는다. 수행이 적었지만 완료 조건 1의 확인이 setup 본문의 글만 읽어 phase가 통과했고 회고 1이 문제로 넣었다 (`docs/tasks/002-ci-workflow/done-phase-1.md`의 하네스에서 걸린 것, `docs/tasks/002-ci-workflow/retro.md`의 회고 1, `FRICTION.md` 6줄, 7줄). 유형: FM-3.2 검증이 없거나 모자람. 잡힌 곳: 그 자리
5. `002-ci-workflow` phase 1의 수행이 ADR-021의 앞선 언급을 찾으려고 저장소 전체를 `grep`해 다른 phase의 파일(`005-publish-verify/phase-2.md`, `phase-3.md`, `001-ci-review/done-phase-2.md`)의 줄을 읽었다. 그 내용은 쓰지 않았다 (`docs/tasks/002-ci-workflow/done-phase-1.md`의 하네스에서 걸린 것, `FRICTION.md` 8줄). 유형: FM-1.2 역할 명세를 어김. 잡힌 곳: 그 자리
6. `002-ci-workflow`의 회고 에이전트에 `001-ci-review` 전의 retro 본문이 다시 실렸다 (`FRICTION.md` 9줄). 유형: FM-1.4 대화 기록을 잃음 — 앞 상태의 스킬 본문으로 돌았다. 잡힌 곳: task의 회고
7. phase 2가 넓힌 편집 훅의 CI 워크플로 예외가 테스트 먼저의 막음도 건너뛴다. phase 2의 통과 조건은 회고 1이 적은 곳과 완료 조건만 다시 돌렸다 (`docs/tasks/002-ci-workflow/retro.md`의 회고 2, `FRICTION.md` 11줄). 유형: FM-3.2 검증이 없거나 모자람. 잡힌 곳: task의 회고
8. 회고 2가 코드와 `docs/ARCHITECTURE.md` 가운데 어느 쪽을 고칠지 적지 않았고, phase 3이 예외를 남은 phase가 없을 때로 좁혀 회고 1의 문제가 남은 phase가 테스트 먼저일 때 다시 났다 (`docs/tasks/002-ci-workflow/retro.md`의 회고 3, `FRICTION.md` 13줄). 유형: FM-2.4 정보를 감춤. 잡힌 곳: task의 회고
9. `002-ci-workflow` phase 4의 통과 조건이 "이미 있는 그 파일의 Edit·Write와 `other.yml`의 Write는 막는다"가 세 경우 가운데 어디에 걸리는지 적지 않아, 확인이 task 머리 결정의 "지금처럼 막는다"로 읽어 정했다 (`docs/tasks/002-ci-workflow/done-phase-4.md`의 확인 1의 하네스에서 걸린 것, `FRICTION.md` 15줄). 유형: FM-2.2 묻지 않고 짐작함. 잡힌 곳: 그 자리
10. `002-ci-workflow`가 회고 1 → phase 2(예외를 넓힘) → 회고 2 → phase 3(좁힘) → 회고 3으로 같은 예외를 오가 회고가 세 번 "문제 있음"이 되고, run이 멈춰 두 번 물었다 (`RUNLOG.md` 20~21줄, `FRICTION.md` 16줄). 유형: FM-1.3 단계 되풀이. 잡힌 곳: 그 자리
11. 푸시 훅이 기본 브랜치를 이름 없이 보내는 push(`--all`, `--mirror`, `refs/heads/*`)를 막지 않는다. 완료 조건 1이 경우를 낱낱이 적고 확인은 그 경우마다 테스트가 있는지만 봤다 (`docs/tasks/003-push-guard/retro.md`의 회고 1, `FRICTION.md` 17줄). 유형: FM-3.2 검증이 없거나 모자람. 잡힌 곳: task의 회고
12. 푸시 훅이 기본 브랜치에서 태그만 보내는 push(`--tags`)를 막는다 (`docs/tasks/003-push-guard/retro.md`의 회고 1, `FRICTION.md` 17줄). 유형: FM-3.2 검증이 없거나 모자람. 잡힌 곳: task의 회고
13. 푸시 훅이 따옴표 없는 heredoc의 본문 줄을 명령으로 읽어 막는다 (`docs/tasks/003-push-guard/retro.md`의 회고 1, `FRICTION.md` 17줄). 유형: FM-3.2 검증이 없거나 모자람. 잡힌 곳: task의 회고
14. `003-push-guard`의 회고 에이전트에 `001-ci-review` 전의 retro 본문이 세 번째로 실렸다 (`FRICTION.md` 18줄). 유형: FM-1.4 대화 기록을 잃음 — 앞 상태의 스킬 본문으로 돌았다. 잡힌 곳: task의 회고
15. 푸시 훅이 줄 잇기(`\`+줄바꿈)를 명령의 경계로 읽는다. phase 2의 통과 조건은 회고 1의 세 꼴과 완료 조건만 다시 돌렸다 (`docs/tasks/003-push-guard/retro.md`의 회고 2, `FRICTION.md` 19줄). 유형: FM-3.2 검증이 없거나 모자람. 잡힌 곳: task의 회고
16. 푸시 훅이 `#` 주석을 명령의 글로 읽는다 (`docs/tasks/003-push-guard/retro.md`의 회고 2, `FRICTION.md` 19줄). 유형: FM-3.2 검증이 없거나 모자람. 잡힌 곳: task의 회고
17. 푸시 훅이 `cd <폴더> &&` 뒤의 push를 호출의 `cwd`에서 본다 (`docs/tasks/003-push-guard/retro.md`의 회고 3). 유형: FM-3.2 검증이 없거나 모자람. 잡힌 곳: task의 회고
18. 푸시 훅이 기본 브랜치에서 명령 치환으로 지금 브랜치를 적은 push를 막지 않는다 (`docs/tasks/003-push-guard/retro.md`의 회고 3). 유형: FM-3.2 검증이 없거나 모자람. 잡힌 곳: task의 회고
19. phase 3이 더한 주석 빼기가 `"$( … )"` 안쪽 따옴표의 오독 위에서 phase 1·2의 훅이 막던 명령을 통과시켰다. phase 3의 통과 조건과 더한 테스트는 고친 꼴만 봤다 (`docs/tasks/003-push-guard/retro.md`의 회고 3, `FRICTION.md` 21줄). 유형: FM-3.2 검증이 없거나 모자람. 잡힌 곳: task의 회고
20. `003-push-guard`의 회고 1~3이 "문제 있음"이라 run이 멈춰 두 번 물었다. 회고 1~6은 매번 시험 밖의 새 꼴을 결함으로 찾았고, retro 4번에는 열린 입력을 읽는 코드에서 결함을 어디까지 찾는지 정한 글이 없다 (`RUNLOG.md` 34~35줄, `FRICTION.md` 22줄, 33줄). 유형: FM-1.5 끝낼 조건을 모름. 잡힌 곳: 그 자리
21. 같은 오독 위에서 주석 빼기가 따옴표 짝을 맞춰 `&&`·`;` 뒤의 push를 지운다. phase 4의 통과 조건은 회고 3의 두 명령과 완료 조건만 다시 돌렸다 (`docs/tasks/003-push-guard/retro.md`의 회고 4, `FRICTION.md` 23줄). 유형: FM-3.2 검증이 없거나 모자람. 잡힌 곳: task의 회고
22. task 머리 결정의 한계 목록이 복합 명령(`{ …; }`, `if … fi`)을 적지 않았는데, 회고 4가 그것을 한계 안으로 읽어 문제로 적지 않았다 (`FRICTION.md` 24줄). 유형: FM-2.2 묻지 않고 짐작함. 잡힌 곳: task의 회고
23. 회고 4도 "문제 있음"이라 run이 멈춰 두 번 물었다 (`RUNLOG.md` 39~40줄, `FRICTION.md` 25줄). 유형: FM-1.5 끝낼 조건을 모름. 잡힌 곳: 그 자리
24. 같은 오독이 매개변수 확장(`"${ … }"`)에 남아 뒤의 push를 지운다. phase 5의 통과 조건은 회고 4의 명령과 완료 조건만 다시 돌렸다 (`docs/tasks/003-push-guard/retro.md`의 회고 5, `FRICTION.md` 26줄). 유형: FM-3.2 검증이 없거나 모자람. 잡힌 곳: task의 회고
25. 산술 명령 `(( … << … ))` 뒤 줄의 push를 막지 않는다. phase 2의 기록이 이 부작용을 "한 일"에만 적고 "남은 것"은 "없음"으로 두어, 그 확인과 회고 2~4가 문제로 보지 않았다 (`docs/tasks/003-push-guard/retro.md`의 회고 5, `FRICTION.md` 27줄). 유형: FM-2.4 정보를 감춤. 잡힌 곳: task의 회고
26. 회고 5도 "문제 있음"이라 run이 멈춰 두 번 물었다 (`RUNLOG.md` 44~45줄, `FRICTION.md` 28줄). 유형: FM-1.5 끝낼 조건을 모름. 잡힌 곳: 그 자리
27. 고칠 phase 6의 TODO가 "훅을 고치지 않고"라면서 끝의 파일 목록에 `plugins/plate/hooks/push_guard.py`를 두었다 (`docs/tasks/003-push-guard/done-phase-6.md`의 하네스에서 걸린 것, `FRICTION.md` 29줄). 유형: FM-2.6 생각과 행동이 어긋남. 잡힌 곳: 그 자리
28. 푸시 훅이 기본 브랜치를 `heads/<이름>`으로 적은 push를 막지 않는다 (`docs/tasks/003-push-guard/retro.md`의 회고 6, `FRICTION.md` 30줄). 유형: FM-3.2 검증이 없거나 모자람. 잡힌 곳: task의 회고
29. 푸시 훅이 기본 브랜치에서 `--repo`로 origin 밖 원격을 적은 push를 막는다 (`docs/tasks/003-push-guard/retro.md`의 회고 6). 유형: FM-3.2 검증이 없거나 모자람. 잡힌 곳: task의 회고
30. 회고 6도 "문제 있음"이라 run이 멈춰 두 번 물었다 (`RUNLOG.md` 49~50줄, `FRICTION.md` 31줄). 유형: FM-1.5 끝낼 조건을 모름. 잡힌 곳: 그 자리
31. 고칠 phase 7의 TODO도 "훅을 고치지 않고"라면서 파일 목록에 `push_guard.py`를 두었고, 수행 기록의 하네스에서 걸린 것은 "없음"이다 (`FRICTION.md` 32줄). 유형: FM-2.6 생각과 행동이 어긋남. 잡힌 곳: task의 회고
32. `004-run-pr` phase 1의 TODO와 완료 조건 3이 `docs/ARCHITECTURE.md`에서 run 규칙과 데이터 흐름만 가리켜, 막는 장치 문단의 "스킬마다의 '푸시하지 않는다' 규칙"이 바뀐 run과 어긋난 채 남았다 (`docs/tasks/004-run-pr/done-phase-1.md`의 하네스에서 걸린 것, `docs/tasks/004-run-pr/retro.md`의 회고 1, `FRICTION.md` 34줄). 유형: FM-2.4 정보를 감춤. 잡힌 곳: 그 자리
33. run "PR을 연다"의 `--body "$(cat <<'EOF' … EOF)"` 꼴이 macOS `/bin/bash` 3.2에서 본문의 짝 없는 따옴표·백틱으로 구문 오류가 나고, 시험 장면의 run은 비슷한 `--body "$( … )"`가 권한 검사에 막혀 `--body-file -`로 바꿨다 (`FRICTION.md` 35줄, 40줄, `docs/tasks/005-publish-verify/done-phase-2.md`의 하네스에서 걸린 것). 유형: FM-3.2 검증이 없거나 모자람. 잡힌 곳: task의 회고
34. `005-publish-verify` phase 1의 TODO "ADR-022가 더해진다"와 task 머리가 그 내용을 적지 않아, 수행이 ADR-021과 세션에 실린 사용자 메모리로 정해 적었다 (`docs/tasks/005-publish-verify/done-phase-1.md`의 하네스에서 걸린 것, `FRICTION.md` 36줄). 유형: FM-2.2 묻지 않고 짐작함. 잡힌 곳: 그 자리
35. 완료 조건 2의 "네 문서가 … 적고"를 합쳐 보는지 문서마다 보는지 정하지 않아 확인이 합쳐 보았다 (`docs/tasks/005-publish-verify/done-phase-1.md`의 확인 1의 하네스에서 걸린 것, `FRICTION.md` 37줄). 유형: FM-2.2 묻지 않고 짐작함. 잡힌 곳: 그 자리
36. 두 매니페스트의 `description`이 푸시 훅과 CI를 적지 않는다. tasks 머리 완료 조건 6의 "두 매니페스트가 바뀐 동작과 맞고"를 보는 확인이 없고 task의 목표와 TODO도 버전만 다뤘다. 코드 평가가 완료 조건 6의 실패로 냈다 (`FRICTION.md` 38줄, `review.md` 평가 1의 완료 조건 6). 유형: FM-3.2 검증이 없거나 모자람. 잡힌 곳: task의 회고
37. `~/plate-rail-test/bin/run.sh`의 허용 목록에 `Bash(git push:*)`가 없어 run 장면마다 `RUN_ALLOW`로 더했다 (`docs/tasks/005-publish-verify/done-phase-2.md`의 하네스에서 걸린 것, `FRICTION.md` 39줄). 유형: 유형 없음 — 시험 폴더 스크립트의 설정이 모자란 것이고 에이전트 사이의 실패가 아니다. 잡힌 곳: 그 자리
38. 시험 장면의 하네스 eval 셋(`ci-norun` `c65829e`, `ci-run` `bb5dada`, `ci-local` `62e0228`)이 낸 plate 자체의 고칠 거리가 이슈로 올라가지 않고 시험 폴더의 커밋에만 있다 (`docs/tasks/005-publish-verify/done-phase-2.md`의 하네스에서 걸린 것, `FRICTION.md` 41줄, 42줄). 유형: 유형 없음 — 시험 장면에서 올리지 않는다고 답한 대로 둔 것이고 이 tasks의 에이전트가 틀린 것이 아니다. 잡힌 곳: 그 자리
39. phase 3의 첫 수행이 시험 저장소 시크릿의 OAuth 토큰 폐기(401)로 막혀 run이 멈춰 물었다 (`docs/tasks/005-publish-verify/done-phase-3.md`의 하네스에서 걸린 것, `RUNLOG.md` 65줄, `FRICTION.md` 53줄). 유형: 유형 없음 — 바깥 자격 증명이 폐기된 것이고 에이전트 사이의 실패가 아니다. 잡힌 곳: 그 자리
40. setup 양식의 워크플로가 review 단계의 실패 까닭을 로그에 남기지 않아, 토큰 폐기 때 `--json-schema was provided but Claude did not return structured_output`만 보였고 진단 PR을 따로 열었다 (`docs/tasks/005-publish-verify/done-phase-3.md`의 하네스에서 걸린 것, `FRICTION.md` 43줄). 유형: FM-2.4 정보를 감춤. 잡힌 곳: 그 자리
41. 막힘이면 phase가 커밋하지 않아 첫 수행이 확인한 사실을 `docs/TOOLS.md`에 옮기지 못하고 기록에만 두었다 (`docs/tasks/005-publish-verify/done-phase-3.md`의 하네스에서 걸린 것, `FRICTION.md` 44줄). 유형: 유형 없음 — 막힘의 규칙대로 한 것이고 이어 한 수행(`07e28e9`)이 옮겨 잃은 것이 없다. 잡힌 곳: 그 자리
42. 완료 조건 4(tasks 머리 완료 조건 1)의 `diff -r <복사본> plugins/plate`가 git이 무시하는 `plugins/plate/hooks/__pycache__`를 다른 것으로 낸다. 테스트와 `--plugin-dir` 세션의 푸시 훅이 그 폴더를 만든다. 확인은 그 폴더를 지우고 견줬고 코드 평가는 완료 조건 1의 실패로 냈다 (`docs/tasks/005-publish-verify/done-phase-3.md`의 하네스에서 걸린 것과 확인 1의 하네스에서 걸린 것, `FRICTION.md` 45줄, `review.md` 평가 1의 완료 조건 1과 하네스에서 걸린 것). 유형: FM-3.3 검증이 틀림. 잡힌 곳: 그 자리
43. 이 레포의 세션에 실린 푸시 훅이 `cd` 뒤 push를 호출한 폴더에서 봐서, 시험 저장소로의 푸시를 `git -C <폴더> push`로 해야 했다 (`docs/tasks/005-publish-verify/done-phase-3.md`의 하네스에서 걸린 것, `FRICTION.md` 46줄). 유형: 유형 없음 — `003-push-guard`의 결정이 정한 한계대로 돈 것이다. 잡힌 곳: 그 자리
44. review 6번의 커버리지 게이트가 "새 줄 20줄 미만이면 보지 않음"과 "측정 못함"이 함께 맞을 때를 정하지 않아, CI에서 11줄인 #3은 `"unmeasured"`를, 11줄인 #4와 16줄인 #2는 `"skipped"`를 냈다 (`docs/tasks/005-publish-verify/done-phase-3.md`의 하네스에서 걸린 것, `FRICTION.md` 47줄). 유형: FM-2.2 묻지 않고 짐작함. 잡힌 곳: 그 자리
45. claude-code-action이 PR의 `CLAUDE.md`를 기준 브랜치의 것으로 되돌려 PR #6의 review가 `CLAUDE.md`가 없는 작업 트리를 봤다 (`docs/tasks/005-publish-verify/done-phase-3.md`의 하네스에서 걸린 것, `FRICTION.md` 48줄). 유형: 유형 없음 — 바깥 도구의 동작이고 평가에는 걸리지 않았다. 잡힌 곳: 그 자리
46. run이 연 PR #6의 본문 끝에 run의 "PR 본문의 꼴"에 없는 `🤖 Generated with …` 줄이 붙었다 (`docs/tasks/005-publish-verify/done-phase-3.md`의 하네스에서 걸린 것, `FRICTION.md` 49줄). 유형: FM-1.1 과제 명세를 어김. 잡힌 곳: 그 자리
47. 시험 폴더의 셋업·계획 커밋이 로컬 `main`에만 있어 run의 PR에 들어갔고, tasks 모드 review가 갈라진 곳을 로컬 `main`과 `origin/main` 가운데 무엇으로 셀지 정해 두지 않았다 (`docs/tasks/005-publish-verify/done-phase-3.md`의 하네스에서 걸린 것, `FRICTION.md` 50줄). 유형: FM-2.2 묻지 않고 짐작함. 잡힌 곳: 그 자리
48. 원격 없는 run의 둘째 턴(합칠지 물은 턴) 답글만 영어였다 (`docs/tasks/005-publish-verify/done-phase-4.md`의 하네스에서 걸린 것, `FRICTION.md` 51줄). 유형: 유형 없음 — 까닭을 확인하지 않았고 판정에 걸리지 않았다. 잡힌 곳: 그 자리
49. 원격 없는 run의 마지막 보고가 BACKLOG의 U+2028을 바꿔 적었다고 했지만 `docs/BACKLOG.md`에는 그 문자가 그대로 있다 (`docs/tasks/005-publish-verify/done-phase-4.md`의 하네스에서 걸린 것, `FRICTION.md` 52줄). 유형: FM-2.6 생각과 행동이 어긋남. 잡힌 곳: 그 자리
50. 코드 평가에서 커버리지, 중복, 타입·복잡도, 보안 검사 도구가 없어 중복과 보안 검사는 측정 못함이 되고, 커버리지는 `trace`로, 인지 복잡도는 손으로 셌다 (`review.md` 평가 1의 하네스에서 걸린 것 첫 줄). 유형: FM-3.2 검증이 없거나 모자람. 잡힌 곳: tasks 끝
51. review 1번은 task 폴더의 기록을 읽지 않게 하지만 tasks 머리 완료 조건 1~4의 확인은 `done-phase-2.md`~`done-phase-4.md`의 실행 기록 경로와 PR 번호를 읽어야 돌아, 코드 평가가 그 줄을 읽었다 (`review.md` 평가 1의 하네스에서 걸린 것 셋째 줄). 유형: FM-1.2 역할 명세를 어김. 잡힌 곳: tasks 끝

**기준**
- 결과 성공
  - 근거: `review.md` 평가 1의 완료 조건 6개, 확인 15개 가운데 통과 13, 실패 2(완료 조건 1의 `diff -r`, 완료 조건 6의 매니페스트 `description`), 측정 못함 0. 기능 적합성 B
  - 근거: `001-ci-review` 마지막 회고 1 통과
  - 근거: `002-ci-workflow` 마지막 회고 4 통과
  - 근거: `003-push-guard` 마지막 회고 7 통과
  - 근거: `004-run-pr` 마지막 회고 2 통과
  - 근거: `005-publish-verify` 마지막 회고 1 통과
  - 등급: C — 실패한 확인이 있어 A·B 칸에 들지 못하고, 기능 적합성이 B라 C 칸에 든다
- 일관성
  - 근거: `001-ci-review` phase 1 첫 시도 통과
  - 근거: `001-ci-review` phase 2 첫 시도 통과
  - 근거: `001-ci-review` phase 3 첫 시도 통과
  - 근거: `002-ci-workflow` phase 1 첫 시도 통과
  - 근거: `002-ci-workflow` phase 2 첫 시도 통과
  - 근거: `002-ci-workflow` phase 3 첫 시도 통과
  - 근거: `002-ci-workflow` phase 4 첫 시도 통과
  - 근거: `003-push-guard` phase 1 첫 시도 통과
  - 근거: `003-push-guard` phase 2 첫 시도 통과
  - 근거: `003-push-guard` phase 3 첫 시도 통과
  - 근거: `003-push-guard` phase 4 첫 시도 통과
  - 근거: `003-push-guard` phase 5 첫 시도 통과
  - 근거: `003-push-guard` phase 6 첫 시도 통과
  - 근거: `003-push-guard` phase 7 첫 시도 통과
  - 근거: `004-run-pr` phase 1 첫 시도 통과
  - 근거: `004-run-pr` phase 2 첫 시도 통과
  - 근거: `005-publish-verify` phase 1 첫 시도 통과
  - 근거: `005-publish-verify` phase 2 첫 시도 통과
  - 근거: `005-publish-verify` phase 3 수행 2번(첫 수행은 막힘), 확인 1번째에 통과
  - 근거: `005-publish-verify` phase 4 첫 시도 통과
  - 근거: `001-ci-review` 회고 첫 시도 통과
  - 근거: `002-ci-workflow` 회고 4번째에 통과
  - 근거: `003-push-guard` 회고 7번째에 통과
  - 근거: `004-run-pr` 회고 2번째에 통과
  - 근거: `005-publish-verify` 회고 첫 시도 통과
  - 첫 시도 통과율: 21 ÷ 25 = 84.0%
  - 등급: B — 75% 이상 90% 미만
- 효율
  - 합계: 에이전트 57개, 토큰 7424098, 도구 호출 1506, 시간 26748초
  - 근거: `수행 002-ci-workflow phase 2` 되풀이 — 더한 phase
  - 근거: `확인 002-ci-workflow phase 2` 되풀이 — 더한 phase
  - 근거: `회고 002-ci-workflow` 되풀이 — 같은 역할이 두 번째로 맡았다
  - 근거: `수행 002-ci-workflow phase 3` 되풀이 — 더한 phase
  - 근거: `확인 002-ci-workflow phase 3` 되풀이 — 더한 phase
  - 근거: `회고 002-ci-workflow` 되풀이 — 같은 역할이 세 번째로 맡았다
  - 근거: `수행 002-ci-workflow phase 4` 되풀이 — 더한 phase
  - 근거: `확인 002-ci-workflow phase 4` 되풀이 — 더한 phase
  - 근거: `회고 002-ci-workflow` 되풀이 — 같은 역할이 네 번째로 맡았다
  - 근거: `수행 003-push-guard phase 2` 되풀이 — 더한 phase
  - 근거: `확인 003-push-guard phase 2` 되풀이 — 더한 phase
  - 근거: `회고 003-push-guard` 되풀이 — 같은 역할이 두 번째로 맡았다
  - 근거: `수행 003-push-guard phase 3` 되풀이 — 더한 phase
  - 근거: `확인 003-push-guard phase 3` 되풀이 — 더한 phase
  - 근거: `회고 003-push-guard` 되풀이 — 같은 역할이 세 번째로 맡았다
  - 근거: `수행 003-push-guard phase 4` 되풀이 — 더한 phase
  - 근거: `확인 003-push-guard phase 4` 되풀이 — 더한 phase
  - 근거: `회고 003-push-guard` 되풀이 — 같은 역할이 네 번째로 맡았다
  - 근거: `수행 003-push-guard phase 5` 되풀이 — 더한 phase
  - 근거: `확인 003-push-guard phase 5` 되풀이 — 더한 phase
  - 근거: `회고 003-push-guard` 되풀이 — 같은 역할이 다섯 번째로 맡았다
  - 근거: `수행 003-push-guard phase 6` 되풀이 — 더한 phase
  - 근거: `확인 003-push-guard phase 6` 되풀이 — 더한 phase
  - 근거: `회고 003-push-guard` 되풀이 — 같은 역할이 여섯 번째로 맡았다
  - 근거: `수행 003-push-guard phase 7` 되풀이 — 더한 phase
  - 근거: `확인 003-push-guard phase 7` 되풀이 — 더한 phase
  - 근거: `회고 003-push-guard` 되풀이 — 같은 역할이 일곱 번째로 맡았다
  - 근거: `수행 004-run-pr phase 2` 되풀이 — 더한 phase
  - 근거: `확인 004-run-pr phase 2` 되풀이 — 더한 phase
  - 근거: `회고 004-run-pr` 되풀이 — 같은 역할이 두 번째로 맡았다
  - 근거: `수행 005-publish-verify phase 3` 되풀이 — 같은 역할이 두 번째로 맡았다(첫 수행이 막힘)
  - 되풀이 몫: 토큰 4064580 ÷ 7424098 = 54.7%, 도구 호출 783 ÷ 1506 = 52.0%, 시간 14942 ÷ 26748 = 55.9%
  - 등급: E — 가장 높은 비율(시간 55.9%)이 50% 이상
- 규칙 준수
  - 근거: `7616256` `plan: pr-ci`는 tasks 머리, task 머리, `phase-N.md`만 넣었다. 맞다
  - 근거: `NNN-slug: phase N` 커밋 20개는 그 `phase-N.md`와 그 phase가 바꾼 파일만 넣었고 tasks 머리와 task 머리는 없다. 맞다
  - 근거: `NNN-slug: phase N 확인` 커밋 20개는 그 `phase-N.md`만 넣었다. 맞다
  - 근거: `NNN-slug: 회고` 커밋 15개는 그 task의 `retro.md`와 `FRICTION.md`만 넣었다. 맞다
  - 근거: `d094722` `pr-ci: 코드 평가`는 `review.md`만 넣었다. 맞다
  - 근거: `plan: NNN-slug 수정` 커밋 10개와 `NNN-slug: phase N 통과` 커밋 20개는 표에 없는 꼴이라 보지 않았다
  - 근거: `done-phase-N.md` 20개 모두 기록 다섯 절과 `## 확인 1`의 판정이 있고, 테스트 먼저인 phase의 확인 절은 모두 "테스트 먼저 기록"을 통과로 적었다. "없음"이 목록 꼴이 아닌 곳이 넷(`002-ci-workflow/done-phase-2.md` 48줄, `003-push-guard/done-phase-3.md` 48줄, `done-phase-7.md` 50줄, `004-run-pr/done-phase-1.md` 45줄)이지만 절은 있다
  - 근거: `retro.md` 5개 모두 회고 절마다 판정이 있다. 회고 문제 17개의 기준은 결함 15, 맥락 문서 2이고 "범위"와 "계획"은 없다
  - 근거: `002-ci-workflow/done-phase-1.md` 53줄 수행이 저장소 전체를 `grep`해 다른 phase의 파일을 읽었다. phase 스킬의 "다른 phase의 파일은 읽지 않는다"와 어긋난다
  - 근거: `005-publish-verify/done-phase-1.md` 53줄 수행이 ADR-022의 두 글을 세션에 실린 사용자 메모리에서 가져왔다. 파일을 읽은 것이 아니라 읽기 범위 위반으로 세지 않았다
  - 근거: `review.md` 평가 1의 하네스에서 걸린 것 셋째 줄 코드 평가가 review 1번이 읽지 않게 한 `done-phase-2.md`~`done-phase-4.md`의 경로·PR 번호 줄을 읽었다. 등급표의 C 칸은 수행과 확인의 읽기만 들어 이 칸에 넣지 않았고, 커밋은 `review.md`만이다
  - 근거: `005-publish-verify/done-phase-3.md` 확인 1의 하네스에서 걸린 것 확인이 자기 테스트가 만든 `plugins/plate/hooks/__pycache__`(git이 무시한다)를 지웠다. 확인 전의 상태로 되돌린 것이고 커밋은 `phase-3.md`만이다
  - 등급: C — 수행이 자기 스킬의 읽기 범위 밖을 읽은 곳이 하나다
- 사람 개입률
  - 근거: 실행 방식(task 하나씩, tasks 일괄) → 정해 둔 물음 (`RUNLOG.md` 3줄)
  - 근거: `002-ci-workflow` 회고 세 번 문제 있음, 훅 예외를 남은 phase·테스트 먼저와 상관없이 두는 해결책으로 갈지 → 멈춤 (20줄)
  - 근거: `002-ci-workflow` task 머리 결정 한 줄과 `phase-4.md`를 더하는 안을 승인할지 → 멈춤 (21줄)
  - 근거: `003-push-guard` 회고 세 번 문제 있음, 훅이 읽는 범위를 정하는 해결책으로 갈지 → 멈춤 (34줄)
  - 근거: `003-push-guard` task 머리 결정 한 줄과 `phase-4.md`를 더하는 안을 승인할지 → 멈춤 (35줄)
  - 근거: `003-push-guard` 회고 4도 문제 있음, 명령 치환을 따로 읽는 해결책으로 갈지 → 멈춤 (39줄)
  - 근거: `003-push-guard` task 머리 결정 한 줄과 `phase-5.md`를 더하는 안을 승인할지 → 멈춤 (40줄)
  - 근거: `003-push-guard` 회고 5도 문제 있음, 약속하는 꼴만 적는 해결책으로 갈지 → 멈춤 (44줄)
  - 근거: `003-push-guard` task 머리 결정 한 줄과 `phase-6.md`를 더하는 안을 승인할지 → 멈춤 (45줄)
  - 근거: `003-push-guard` 회고 6도 문제 있음, 약속을 테스트가 다루는 꼴로 닫는 해결책으로 갈지 → 멈춤 (49줄)
  - 근거: `003-push-guard` task 머리 결정 한 줄과 `phase-7.md`를 더하는 안을 승인할지 → 멈춤 (50줄)
  - 근거: `005-publish-verify` phase 3 막힘(OAuth 토큰 폐기), 새 토큰을 시크릿으로 넣고 다시 맡길지 → 멈춤 (65줄)
  - 개입률: 멈춤 11 ÷ 에이전트 57 = 19.3%
  - 등급: D — 10% 넘고 20% 이하
- 실패 양상
  - 유형마다: FC1 12개(FM-1.1 2, FM-1.2 2, FM-1.3 1, FM-1.4 3, FM-1.5 4), FC2 13개(FM-2.2 6, FM-2.4 4, FM-2.6 3), FC3 18개(FM-3.2 17, FM-3.3 1), 유형 없음 8개
  - 잡힌 곳마다: 그 자리 28, phase의 확인 0, task의 회고 21, tasks 끝 2
  - 등급: E — tasks 끝에서 잡힌 실패가 둘(실패 50, 51)이다

**스킬로 만들 후보**
- setup 양식 절의 워크플로를 뽑아 YAML로 파싱하고, `--json-schema`를 판정 스크립트의 키와 값에 대어 보고, `verdict` 잡의 run을 가짜 `gh`로 돌리는 묶음을 스크립트나 테스트로 두면, 수행·확인·회고가 저마다 새로 짜던 양식 확인이 명령 하나로 같게 돈다 (근거: `002-ci-workflow` `FRICTION.md` 12줄)
- 문서 지도 구간, 커밋된 테스트, `phase-N.md`, 로컬 bare origin을 둔 스크래치 git 레포 장면을 만들어 PreToolUse JSON을 훅(`edit_guard.py`, `push_guard.py`)에 넣고 종료 코드와 글을, 푸시 훅이면 `git push --dry-run --porcelain`의 결과와 나란히 내는 스크립트로 두면, 훅을 고친 phase의 수행·확인과 회고마다 장면을 새로 짜는 일이 줄고 앞선 회고의 재현도 같은 명령으로 다시 돌린다 (근거: `002-ci-workflow` `FRICTION.md` 14줄, `003-push-guard` `FRICTION.md` 20줄, 두 task의 `done-phase-2.md`~`done-phase-4.md`의 한 일과 확인 1)
- 시험 폴더의 꼴(원격 없음, GitHub, CI 있음)과 tasks를 받아 셋업, 계획 커밋, run의 세 턴, 물음 글 세기와 `test <기록> -nt <본문>`을 한 번에 돌리는 스크립트로 두면, 시험 장면마다 새로 쓰던 스크립트와 손 확인이 준다 (근거: `005-publish-verify` `FRICTION.md` 54줄)

**하네스 고칠 거리**
1. 고칠 phase가 회고가 적은 재현만 다시 돌려 같은 뿌리의 다른 꼴과 회귀를 놓치고, 회고는 어긋남을 적으며 어느 쪽을 고칠지 적지 않는다 (근거: 실패 7, 8, 10, 15, 16, 17, 18, 19, 21, 24). 갈래: plate 자체
   - 이슈 제목: run이 더하는 고칠 phase의 통과 조건이 회고가 적은 재현만 다시 돌린다
   - 이슈 본문: 회고의 문제를 고치려고 run이 더한 phase가 그 회고가 적은 명령과 완료 조건만 다시 돌리고 통과해, 같은 함수의 다른 꼴이나 앞서 막던 꼴의 회귀가 다음 회고에서야 드러난 일이 한 tasks에서 여섯 번 났다. 회고가 문서와 코드의 어긋남을 적으며 어느 쪽을 기준으로 할지 적지 않아, 고칠 phase가 반대쪽을 고치고 같은 예외를 두 번 오간 일도 있었다. 원인: run 스킬이 쓰는 고칠 phase(`# Phase M: 회고 K의 문제를 고친다`)의 통과 조건이 회고 K가 적은 곳과 완료 조건뿐이고, retro 스킬의 문제 글에는 기준이 되는 쪽을 적는 규칙이 없다. 해결책: 고칠 phase의 통과 조건에 앞선 회고들이 적은 재현을 모두 다시 돌리는 것과, 고친 코드에서 같은 뿌리의 꼴을 찾아 테스트로 남기는 것을 넣는다. retro는 어긋남을 문제로 적을 때 task 머리의 목표와 결정에 비춰 어느 쪽을 고칠지 적는다. 근거: `pr-ci`, `77deb39` `cdc6aba` `a09c9eb` `5120f47` `c52e8c8` `2356bf8`, `docs/tasks/FRICTION.md`(11, 13, 19, 21, 23, 26줄), `docs/tasks/002-ci-workflow/retro.md`, `docs/tasks/003-push-guard/retro.md`
2. 입력의 꼴이 열린 코드에서 회고의 결함 점검에 끝이 없다 (근거: 실패 20, 22, 23, 26, 30). 갈래: plate 자체
   - 이슈 제목: 열린 입력을 읽는 코드에서 retro의 결함 점검이 끝나지 않는다
   - 이슈 본문: 셸 명령 글을 읽는 훅을 만든 task에서 회고 1~6이 매번 시험 밖의 새 꼴(셸 구문, git 표기)을 결함으로 찾아 run이 세 번 실패로 네 번 멈췄고, task 머리 결정이 약속을 시험이 다루는 꼴로 닫고서야 회고가 통과했다. 원인: retro 스킬 4번의 "동작이 틀리는 결함이 있는가"에 결함을 어디까지 찾는지의 경계가 없고, plan 스킬은 입력의 꼴이 열린 기능에서 약속하는 꼴을 정하게 하지 않는다. 해결책: plan은 입력의 꼴이 열린 기능(셸 글이나 사용자 글을 읽는 것)이면 약속하는 꼴의 경계를 결정으로 정하게 묻고, retro는 그 경계 밖에서 찾은 꼴을 "문제"가 아니라 `FRICTION.md`의 볼 거리로 적는다. 근거: `pr-ci`, `c52e8c8` `2356bf8` `85c486b` `1e58e93`, `docs/tasks/003-push-guard/plan.md`의 결정, `docs/tasks/RUNLOG.md` 34~50줄, `docs/tasks/FRICTION.md` 24, 33줄
3. 계획의 완료 조건과 통과 조건이 조건의 일부 절을 보지 않고 읽는 법이 갈린다 (근거: 실패 4, 9, 35, 36). 갈래: plate 자체
   - 이슈 제목: plan의 완료 조건 확인이 조건의 일부 절을 보지 않고 여러 대상을 보는 확인의 읽는 법이 갈린다
   - 이슈 본문: 완료 조건의 "두 매니페스트가 바뀐 동작과 맞고"를 보는 확인이 없어 확인과 회고가 지나치고 코드 평가에서 실패가 됐다. "네 문서가 … 적고"는 합쳐 보는지 문서마다 보는지, "이미 있는 그 파일의 편집은 막는다"는 어느 경우에 걸리는지 정하지 않아 확인이 짐작으로 정했다. setup을 다시 부르는 경우는 완료 조건에 없어 확인이 본문 글만 읽고 통과시켰다. 원인: plan 스킬의 완료 조건과 통과 조건을 쓰는 규칙에 조건의 절마다 확인을 두고, 여러 대상이나 경우를 보는 확인은 대상마다인지 합쳐서인지와 경우마다의 기대를 적는 규칙이 없다. 해결책: 초안을 보여 주기 전에 조건의 절마다 그것을 보는 확인이 있는지 대어 보고, 여러 대상이나 경우를 보는 확인에는 대상마다인지 합쳐서인지와 경우마다의 기대를 적게 한다. 근거: `pr-ci`, `7616256` `9ddb9ea`, `docs/tasks/plan.md` 완료 조건 6, `docs/tasks/FRICTION.md` 7, 15, 37, 38줄, `docs/tasks/review.md` 평가 1
4. 계획의 TODO가 바뀌는 규칙을 적은 다른 곳과 더할 ADR의 내용을 빠뜨린다 (근거: 실패 32, 34). 갈래: plate 자체
   - 이슈 제목: plan의 TODO가 바뀌는 규칙을 적은 다른 줄과 더할 ADR의 결정을 빠뜨린다
   - 이슈 본문: 한 스킬의 절대 규칙을 바꾸는 phase의 TODO가 맥락 문서의 두 절만 가리켜, 같은 문서의 다른 문단이 바뀐 규칙과 어긋난 채 남았고 회고 뒤에 고칠 phase를 더했다. "ADR-022가 더해진다"는 TODO는 무엇을 정하는지 적지 않아 수행이 세션의 메모리로 정했다. 원인: plan 스킬이 TODO를 쓸 때 바뀌는 규칙을 적은 맥락 문서의 줄을 찾게 하지 않고, 더할 ADR의 결정을 적게 하지 않는다. 해결책: 규칙이나 동작을 바꾸는 TODO는 그것을 적은 맥락 문서의 줄을 찾아 모두 가리키고, ADR을 더하는 TODO에는 결정과 이유를 적는다. 근거: `pr-ci`, `7616256` `fb5b134`, `docs/tasks/004-run-pr/done-phase-1.md`, `docs/tasks/005-publish-verify/done-phase-1.md`
5. run이 쓴 고칠 phase의 TODO가 회고 글의 파일 목록을 옮겨 TODO의 글과 어긋난다 (근거: 실패 27, 31). 갈래: plate 자체
   - 이슈 제목: run이 쓴 고칠 phase의 TODO가 "고치지 않는다"면서 그 파일을 목록에 둔다
   - 이슈 본문: 회고의 문제를 고칠 phase를 run이 쓸 때 두 번 연이어 TODO가 "훅을 고치지 않고"라면서 끝의 파일 목록에 훅 파일을 두었고, 수행은 테스트 먼저 줄에 기대어 읽었다. 원인: run 스킬이 고칠 phase를 쓸 때 TODO의 파일 목록을 회고의 문제 글에서 옮기고 TODO 글과 맞는지 보지 않는다. 해결책: 고칠 phase의 파일 목록에는 TODO가 고치는 파일만 적고, 쓰기 전에 TODO 글과 대어 본다. 근거: `pr-ci`, `85c486b` `1e58e93`, `docs/tasks/003-push-guard/done-phase-6.md`, `docs/tasks/003-push-guard/done-phase-7.md`
6. 수행이 아는 부작용을 "한 일"에만 적어 확인과 회고가 놓친다 (근거: 실패 25). 갈래: plate 자체
   - 이슈 제목: phase가 아는 부작용을 한 일에만 적어 확인과 회고가 놓친다
   - 이슈 본문: 수행이 고친 코드가 다른 꼴을 잘못 읽는다는 것을 "한 일"에 적고 "남은 것"은 "없음"으로 두어, 그 phase의 확인과 다음 회고 셋이 문제로 보지 않았고 세 회고 뒤에야 결함으로 찾았다. 원인: phase 스킬의 기록 규칙이 아는 부작용과 한계를 어느 절에 적는지 정하지 않는다. 해결책: 수행이 아는 부작용과 한계는 "남은 것"에 적게 한다. 근거: `pr-ci`, `5cdb2a0`, `docs/tasks/003-push-guard/done-phase-2.md`, `docs/tasks/003-push-guard/retro.md`의 회고 5
7. run의 PR 본문·댓글 꼴이 실제 셸과 권한 검사에서 실패한다 (근거: 실패 33). 갈래: plate 자체
   - 이슈 제목: run의 `--body "$(cat <<'EOF' … EOF)"` 꼴이 bash 3.2와 권한 검사에서 실패한다
   - 이슈 본문: run 스킬 "PR을 연다"는 PR 본문과 평가서 댓글을 `--body "$(cat <<'EOF' … EOF)"`로 넘기게 적는데, macOS의 `/bin/bash` 3.2에서 본문에 짝 없는 따옴표나 백틱이 있으면 구문 오류가 나고, 시험 장면에서는 비슷한 `--body "$( … )"` 꼴이 Claude Code의 권한 검사("Quoted text in this command can't be checked before it runs")에 막혀 run이 `--body-file -`로 바꿔 달았다. 원인: run 스킬 "PR을 연다" 3·4번의 꼴. 해결책: 본문을 파일이나 표준 입력으로 넘기는 `--body-file`로 바꾼다. 근거: `pr-ci`, `946bb82`, `docs/tasks/FRICTION.md` 35, 40줄, `docs/tasks/005-publish-verify/done-phase-2.md`
8. PR이 바꾼 지침 파일이나 코드가 PR 모드 review의 등급을 올릴 길이 열려 있다 (근거: 실패 2). 갈래: plate 자체
   - 이슈 제목: PR이 바꾼 AGENTS.md나 코드가 PR 모드 review의 등급 묶음을 올려 자동 머지를 이끌 수 있다
   - 이슈 본문: CI의 자동 머지는 PR 모드 review가 내는 등급 묶음으로 정해진다. review의 절대 규칙은 프로젝트의 지침 파일 규칙을 따르게 하고 PR 모드에 예외가 없어, PR이 바꾼 `AGENTS.md`나 코드 속 글이 등급을 올리게 할 길이 남는다(claude-code-action은 `CLAUDE.md`와 `.claude`만 기준 브랜치의 것으로 되돌린다). 결정의 이유("에이전트에게는 머지 권한이 없다")는 머지 권한을 막지만 등급을 막지 않는다. 원인: review 스킬의 절대 규칙과 PR 모드 절, setup의 워크플로 양식. 해결책: PR 모드에서는 지침 파일을 기준 브랜치의 것으로 읽고, PR이 바꾼 파일의 글은 평가할 데이터로만 보며 지시로 따르지 않는다고 적는다. ADR의 트레이드오프에 이 길을 적는다. 근거: `pr-ci`, `f9c250d` `7afa149`, `docs/tasks/001-ci-review/done-phase-2.md`, `docs/tasks/FRICTION.md` 4, 10, 48줄
9. review의 커버리지 게이트가 "20줄 미만"과 "측정 못함"이 함께 맞을 때를 정하지 않는다 (근거: 실패 44). 갈래: plate 자체
   - 이슈 제목: review의 커버리지 게이트가 작은 PR에서 skipped와 unmeasured로 갈린다
   - 이슈 본문: CI에서 새 줄이 11줄인 PR 둘이 하나는 `"unmeasured"`, 하나는 `"skipped"`를 냈고, 판정 스크립트는 `"unmeasured"`를 머지 요청으로 보낸다. 그래서 같은 꼴의 작은 PR이 이 갈림에 따라 자동 머지 대신 머지 요청이 된다. 원인: review 스킬 6번의 커버리지 게이트 규칙. 해결책: 새 줄이 20줄 미만이면 측정과 상관없이 "보지 않음"(`"skipped"`)으로 먼저 정한다고 적는다. 근거: `pr-ci`, `07e28e9`, `docs/tasks/005-publish-verify/done-phase-3.md`, `docs/tasks/FRICTION.md` 47줄
10. setup의 CI 워크플로가 review 단계의 실패 까닭을 로그에 남기지 않는다 (근거: 실패 40). 갈래: plate 자체
    - 이슈 제목: setup의 CI 워크플로가 review 단계의 실패 까닭을 로그에 남기지 않는다
    - 이슈 본문: 시크릿의 OAuth 토큰이 폐기됐을 때 CI 로그에는 `--json-schema was provided but Claude did not return structured_output`만 남아, 인증 실패라는 것을 진단 PR을 따로 열어서야 찾았다. 원인: setup 스킬의 워크플로 양식이 review 단계가 구조화 출력을 내지 못했을 때 까닭을 내는 단계를 두지 않는다. 해결책: review 단계가 실패하면 액션의 실행 결과에서 오류 줄만 로그에 내는 단계를 둔다. `show_full_output`은 대화 전체를 로그에 내므로 켜지 않는다. 근거: `pr-ci`, `07e28e9`, `docs/tasks/005-publish-verify/done-phase-3.md`, `docs/TOOLS.md`
11. review의 읽기 범위가 tasks 머리 확인이 가리키는 task 기록을 막는다 (근거: 실패 51). 갈래: plate 자체
    - 이슈 제목: review가 읽지 못하는 task 기록에 tasks 머리 완료 조건의 확인이 기댄다
    - 이슈 본문: 실행 기록의 경로나 PR 번호처럼 phase를 수행할 때 정해지는 값은 `done-phase-N.md`에만 적히고, tasks 머리의 확인은 그 파일을 가리킨다. review 스킬 1번은 task 폴더의 기록을 읽지 않게 해, 코드 평가가 3번(확인을 모두 돌린다)을 따르려고 규칙과 어긋나게 그 줄을 읽었다. 원인: review 스킬 1번의 읽기 범위. 해결책: review 1번에 "tasks 머리의 확인이 가리키는 기록의 줄은 그 확인을 돌리는 데만 읽고 등급의 근거로 쓰지 않는다"를 더한다. 근거: `pr-ci`, `d094722`, `docs/tasks/review.md` 평가 1의 하네스에서 걸린 것, `docs/tasks/plan.md` 완료 조건 1~4
12. eval이 코드 평가의 "하네스에서 걸린 것"을 모두 tasks 끝의 실패로 세어, 환경의 한계만으로 실패 양상이 E가 된다 (근거: 실패 50, 하네스에서 걸린 것). 갈래: plate 자체
    - 이슈 제목: eval이 코드 평가가 적은 환경의 한계를 tasks 끝의 실패로 세어 실패 양상이 E가 된다
    - 이슈 본문: 코드 평가는 측정 도구가 없다는 것 같은 환경의 한계도 "하네스에서 걸린 것"에 적는다. eval 스킬 2번은 그 줄을 모두 tasks 끝에서 잡힌 실패로 세고 등급표는 tasks 끝의 실패가 둘이면 실패 양상을 E로 매겨, 하네스가 틀리지 않은 줄로도 등급이 한 칸 내려간다. 이 tasks의 시험 장면 eval 셋도 같은 것을 고칠 거리로 냈다. 원인: eval 스킬 2번의 모으는 곳 표. 해결책: 코드 평가의 "하네스에서 걸린 것" 가운데 측정 못함의 까닭(도구가 없다)은 실패로 세지 않고, tasks 끝의 실패는 완료 조건 확인의 실패, 신뢰성 문제, 하네스의 규칙이나 계획에서 걸린 것으로 둔다. 근거: `pr-ci`, `d094722`, `docs/tasks/review.md` 평가 1, `docs/tasks/FRICTION.md` 41줄
13. eval의 규칙 준수 표에 run이 만드는 커밋 꼴이 없다 (근거: 하네스에서 걸린 것). 갈래: plate 자체
    - 이슈 제목: eval의 규칙 준수 표에 run의 `plan: NNN-slug 수정`과 `NNN-slug: phase N 통과`가 없다
    - 이슈 본문: run은 고칠 phase를 `plan: NNN-slug 수정`(`phase-M.md`, 고친 task 머리, `RUNLOG.md`)으로, 통과한 phase의 이름 바꾸기를 `NNN-slug: phase N 통과`(이름 바꾸기와 `RUNLOG.md`)로 커밋하는데, eval 스킬 3번의 규칙 준수 표에는 `plan: NNN-slug 더함`만 있어 이 tasks의 커밋 87개 가운데 30개를 보지 못했다. eval의 낱말 "더한 phase"는 `plan: NNN-slug 수정`을 적어 표와도 어긋난다. 원인: eval 스킬 3번의 표. 해결책: 표에 run의 두 꼴과 넣어도 되는 파일을 더한다. 근거: `pr-ci`, `77deb39` `e8465ea`, `docs/tasks/FRICTION.md` 42줄
14. 띄운 에이전트에 실린 plate 스킬 본문이 tasks가 고친 저장소의 본문을 따라오지 않는다 (근거: 실패 3, 6, 14). 갈래: 이 프로젝트만
    - 고칠 곳: `docs/TOOLS.md`
    - 해결책: 세션에 실린 plate 스킬 본문은 세션을 띄울 때의 것이라 같은 세션에서 띄운 에이전트에는 tasks가 고치기 전의 본문이 실린다는 사실을 적고, 스킬의 절차를 바꾸는 tasks는 그 절차에 기대는 다음 단계를 새 세션에서 이어 간다고 적는다.
15. 복사본과 견주는 `diff -r`가 git이 무시하는 `__pycache__`를 다른 것으로 낸다 (근거: 실패 42). 갈래: 이 프로젝트만
    - 고칠 곳: `docs/ARCHITECTURE.md`
    - 해결책: 테스트와 `--plugin-dir` 세션의 훅이 `plugins/plate/hooks/__pycache__`를 만든다는 것을 적고, `plugins/plate`를 복사본과 견주는 확인은 `diff -r -x __pycache__`로 쓴다.
16. 시험 폴더의 run 허용 목록에 푸시가 없다 (근거: 실패 37). 갈래: 이 프로젝트만
    - 고칠 곳: `~/plate-rail-test/bin/run.sh`
    - 해결책: run의 허용 목록에 `Bash(git push:*)`를 넣어 장면마다 `RUN_ALLOW`로 더하지 않게 한다.

**하네스에서 걸린 것**
- eval 스킬 2번: 코드 평가의 "하네스에서 걸린 것" 첫 줄(측정 도구가 없다)이 규칙대로 tasks 끝의 실패(실패 50)가 되어 실패 양상이 E로 매겨졌다. 시험 장면 eval들이 낸 것과 같다(고칠 거리 12)
- eval 스킬 3번: 규칙 준수 표에 `plan: NNN-slug 수정`과 `NNN-slug: phase N 통과`가 없어 커밋 30개를 보지 않았다(고칠 거리 13)
- `RUNLOG.md`의 마지막 두 줄(`005-publish-verify` 회고, 코드 평가)은 커밋되지 않고 작업 트리에만 있어 작업 트리의 것을 읽었다
- 멈춤 하나마다 물은 줄이 둘(해결책, 고칠 안의 승인)씩 남아, 개입률은 물은 줄로 11을 세고 실패는 멈춤마다 하나(여섯)로 셌다
- 다른 기록이 같은 일을 다시 적은 것은 하나로 셌고, 같은 원인이 다른 에이전트에서 다시 난 것(옛 스킬 본문이 실림, 고칠 phase의 어긋난 TODO)은 난 곳마다 셌다
- `review.md` 평가 1의 완료 조건 6 셋째 줄은 tasks 머리에 없는 확인을 코드 평가가 더한 것인데, 결과 성공의 확인 수(15)에 넣었다
- 시험 장면 eval이 낸 고칠 거리 가운데 "retro와 plan이 PRD의 다른 절과의 어긋남을 보지 않는다"와 "review가 `/tmp`에 쓴 측정 파일을 지우지 못한다"는 시험 폴더(`~/plate-rail-test`)의 커밋에만 있어, 이 tasks의 기록과 커밋만 근거로 삼는 규칙 때문에 고칠 거리로 옮기지 못했다
