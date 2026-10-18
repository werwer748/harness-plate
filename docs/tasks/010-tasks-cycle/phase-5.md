# Phase 5: review를 만든다

**목표**: review 스킬이 tasks 끝에 tasks에서 바뀐 코드를 다섯 범주 A~E로 평가해 `docs/tasks/review.md`에 적는다.

**테스트 먼저**: 아니오 — `.md`만 만든다.

**읽을 것**
- `plugins/plate/skills/retro/SKILL.md` (phase 4의 task 회고. 점검 기준과 기록의 꼴을 맞춘다)
- `plugins/plate/skills/check/SKILL.md` (명령 절을 읽고 "없음"을 적는 법)
- `plugins/plate/skills/plan/SKILL.md` (tasks 머리의 양식과 이름)
- https://docs.sonarsource.com/sonarqube-server/latest/user-guide/code-metrics/metrics-definition/ (Sonar 등급. 신뢰성·보안은 0건이면 A이고 B~E는 가장 심각한 이슈의 등급으로 정한다. 유지보수성은 기술부채 비율로 A ≤5%, B <10%, C <20%, D <50%, E ≥50%이고, 비율은 부채 ÷ (줄 수 × 30분))
- https://docs.sonarsource.com/sonarqube-server/latest/quality-standards-administration/managing-quality-gates/introduction-to-quality-gates/ (Sonar way 게이트. 새 코드만 보고 새 이슈 0, 핫스팟 100% 검토, 커버리지 ≥80%, 중복 ≤3%. 새 줄이 20줄 미만이면 커버리지와 중복은 보지 않는다)
- https://testing.googleblog.com/2020/08/code-coverage-best-practices.html (커버리지 60% 수용, 75% 우수, 90% 모범)
- https://google.github.io/eng-practices/review/reviewer/looking-for.html (리뷰 항목: 설계, 기능, 복잡도, 테스트, 이름, 주석, 스타일, 일관성, 문서)
- https://platform.claude.com/docs/en/test-and-evaluate/develop-tests (점수 전에 근거를 먼저 적게 한다)
- https://arxiv.org/abs/2310.08491 (점수마다 기준 설명과 기준 답안을 준다)

**TODO**
- [x] review 스킬이 생긴다: tasks 머리를 읽고, tasks 브랜치가 기본 브랜치에서 갈라진 곳부터 바뀐 코드 파일만 평가한다 (`plugins/plate/skills/review/SKILL.md`)
- [x] 다섯 범주(신뢰성, 보안, 유지보수성, 테스트 적절성, 기능 적합성)마다 A~E와 근거를 적고 총점은 두지 않는다. 기능 적합성은 tasks 머리의 완료 조건 확인을 직접 돌려 매긴다
- [x] 잴 수 있는 것(명령 절의 빌드·린트·테스트, 커버리지, 프로젝트에 있는 정적 분석이나 보안 검사)은 도구로 재고 명령과 결과를 적는다. 도구가 없으면 "측정 못함"이다
- [x] 판단 항목은 Google 리뷰 지침의 항목과 범주마다의 등급표로 매기고, 근거(파일:줄)를 먼저 적은 뒤 등급을 매긴다. 정할 수 없으면 "판단 못함"이다
- [x] Sonar way 게이트의 통과 여부를 조건마다 적는다
- [x] 소스 문제 목록이 문제마다 한 줄(무엇, 파일:줄, 범주)로 있어 고칠지 묻는 자리에서 쓴다
- [x] `docs/tasks/review.md`에 적고 그 파일만 tasks 이름으로 시작하는 메시지로 커밋한다. 고치지 않고 묻지 않으며, 범주 등급, 게이트 통과 여부, 문제 수, 기록 위치를 정해 둔 줄로 돌려준다

**통과 조건**
- review 본문이 TODO대로다
  - 확인: `plugins/plate/skills/review/SKILL.md`를 읽어 TODO 항목마다 그 동작이 적힌 곳을 찾는다
- 완료 조건 2 가운데 review 본문의 몫이 참이다
  - 확인: `grep -n "작업" plugins/plate/skills/review/SKILL.md`의 줄을 모두 읽어 tasks, task, phase를 가리키는 "작업"이 없다

## 한 일
- review 스킬이 생긴다: 새 스킬을 만들었다. 1번에서 tasks 머리와 task 머리를 읽고, 낱말의 "갈라진 곳"(`git merge-base <기본 브랜치> HEAD`)과 "바뀐 코드 파일"(`git diff --name-only --diff-filter=d <갈라진 곳> HEAD` 가운데 `.md`가 아니고 `docs/tasks/` 밖이며 잠금 파일 같은 도구가 만든 파일이 아닌 것)만 평가한다. 기본 브랜치의 뜻은 run 본문의 정의를 그대로 옮겼다. 0번에서 tasks 머리가 없거나, `phase-N.md`가 남은 task 폴더가 있거나, 지금 브랜치가 기본 브랜치이면 평가하지 않는다 (`plugins/plate/skills/review/SKILL.md`)
- 다섯 범주마다 A~E와 근거, 총점 없음, 기능 적합성은 완료 조건 확인을 직접 돌려 매김: 5번의 등급표에 범주마다 칸을 두고, 3번에서 tasks 머리의 완료 조건 확인을 모두 돌리며, 적는 규칙에 "총점, 평균, 범주를 합친 등급을 적지 않는다"를 두었다. 신뢰성·보안은 Sonar처럼 가장 무거운 문제의 심각도(막힘, 높음, 중간, 낮음)로, 유지보수성은 부채 비율(부채 ÷ (새 줄 수 × 30분), A 5% 이하 ~ E 50% 이상)로, 테스트 적절성은 Google의 커버리지 칸(90/75/60%)과 판단 가운데 낮은 쪽으로 매긴다 (`plugins/plate/skills/review/SKILL.md`)
- 잴 수 있는 것은 도구로 재고 명령과 결과를 적음, 도구가 없으면 "측정 못함": 2번에 명령 절, 커버리지, 중복, 정적 분석, 보안 검사를 차례로 두고, 설정됐거나 설치된 도구만 쓰고 새로 설치하지 않으며, 도구가 없거나 돌지 않으면 "측정 못함"이라고 적었다 (`plugins/plate/skills/review/SKILL.md`)
- 판단 항목은 Google 리뷰 지침의 항목과 등급표로, 근거(파일:줄) 먼저, 정할 수 없으면 "판단 못함": 4번의 표가 범주마다 Google 항목(기능, 설계, 복잡도, 이름, 주석, 스타일, 일관성, 문서, 테스트)을 잇고, 절대 규칙 3과 5번 첫 문단, 적는 규칙이 근거를 등급보다 먼저 적게 하며, 칸에 들지 못하면 "판단 못함"이다 (`plugins/plate/skills/review/SKILL.md`)
- Sonar way 게이트의 통과 여부를 조건마다: 6번에 조건 넷(새 문제 0개, 핫스팟 모두 검토, 새 줄 커버리지 80% 이상, 새 줄 중복 3% 이하)과 20줄 미만의 "보지 않음"을 두고, 양식의 "Sonar way 게이트" 항목에 조건마다 한 줄을 적게 했다 (`plugins/plate/skills/review/SKILL.md`)
- 소스 문제 목록이 문제마다 한 줄(무엇, 파일:줄, 범주): 양식의 "소스 문제"가 번호 붙은 `{무엇} (`{파일:줄}`). 범주: {범주}` 줄이고, 적는 규칙이 다섯 범주의 문제를 모두 옮기고 고칠지 묻는 자리에서 번호로 가리키게 한다. 하네스의 문제는 "하네스에서 걸린 것"으로 가른다 (`plugins/plate/skills/review/SKILL.md`)
- `docs/tasks/review.md`에 적고 그 파일만 커밋, 고치지 않고 묻지 않음, 정해 둔 줄로 돌려줌: 7번이 `review.md` 끝에 `## 평가 N`을 더하고, 8번이 그 파일만 `<tasks 이름>: 코드 평가` 메시지로 커밋하며, 9번이 등급, 게이트, 문제, 기록 네 줄을 돌려준다. 절대 규칙 1과 4가 고치지 않고 묻지 않게 한다 (`plugins/plate/skills/review/SKILL.md`)

## 확인 결과
- review 본문이 TODO대로다
  - `plugins/plate/skills/review/SKILL.md`를 읽음 → TODO 1: 51줄(tasks 머리 읽기), 29~30줄(갈라진 곳, 바뀐 코드 파일). TODO 2: 102~114줄(등급표), 70줄(완료 조건 확인을 직접 돌림), 213줄(총점 없음). TODO 3: 60~66줄(도구로 재고 "측정 못함"). TODO 4: 72~87줄(Google 항목 표, 83줄 파일:줄 근거), 18줄과 91줄, 211줄(근거 먼저, 칸에 못 들면 "판단 못함"). TODO 5: 116~125줄과 192~197줄(조건마다 통과 여부). TODO 6: 199~200줄, 214줄(번호 붙은 한 줄 목록). TODO 7: 127~146줄(`review.md`, 그 파일만 `<tasks 이름>: 코드 평가`로 커밋, 네 줄), 16줄과 19줄(고치지 않음, 묻지 않음). 통과
- 완료 조건 2 가운데 review 본문의 몫이 참이다
  - `grep -n "작업" plugins/plate/skills/review/SKILL.md` → 0줄(exit 1). 읽을 줄이 없어 tasks, task, phase를 가리키는 "작업"이 없다. 통과

## 계획과 달라진 점
없음

## 남은 것
없음

## 하네스에서 걸린 것
- 읽을 것의 https://testing.googleblog.com/2020/08/code-coverage-best-practices.html 은 WebFetch가 본문 없이 제목과 댓글만 돌려줘서 `curl`로 받아 60%·75%·90% 문장을 읽었다. https://platform.claude.com/docs/en/test-and-evaluate/develop-tests 는 길어서 WebFetch의 첫 결과에 채점 지침이 없었고 `offset: 100000`으로 다시 읽어 "Encourage reasoning" 줄을 찾았다.
- 읽을 것에 기본 브랜치를 정하는 법이 없어 `plugins/plate/skills/run/SKILL.md`의 "기본 브랜치" 정의(37줄)를 grep으로 찾아 그대로 옮겼다. run 본문은 아직 옛 낱말이라 뒤 phase에서 run이 바뀌면 이 정의와 어긋나지 않는지 볼 곳이다.
- 계획은 커밋 메시지를 "tasks 이름으로 시작하는 메시지"로만 정해서 `<tasks 이름>: 코드 평가`로 정했다. 일괄 실행의 커밋 순서를 보는 tasks 완료 조건 6과 run이 이 메시지를 알아야 한다.
