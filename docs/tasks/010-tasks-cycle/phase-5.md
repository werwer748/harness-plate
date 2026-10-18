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
- [ ] review 스킬이 생긴다: tasks 머리를 읽고, tasks 브랜치가 기본 브랜치에서 갈라진 곳부터 바뀐 코드 파일만 평가한다 (`plugins/plate/skills/review/SKILL.md`)
- [ ] 다섯 범주(신뢰성, 보안, 유지보수성, 테스트 적절성, 기능 적합성)마다 A~E와 근거를 적고 총점은 두지 않는다. 기능 적합성은 tasks 머리의 완료 조건 확인을 직접 돌려 매긴다
- [ ] 잴 수 있는 것(명령 절의 빌드·린트·테스트, 커버리지, 프로젝트에 있는 정적 분석이나 보안 검사)은 도구로 재고 명령과 결과를 적는다. 도구가 없으면 "측정 못함"이다
- [ ] 판단 항목은 Google 리뷰 지침의 항목과 범주마다의 등급표로 매기고, 근거(파일:줄)를 먼저 적은 뒤 등급을 매긴다. 정할 수 없으면 "판단 못함"이다
- [ ] Sonar way 게이트의 통과 여부를 조건마다 적는다
- [ ] 소스 문제 목록이 문제마다 한 줄(무엇, 파일:줄, 범주)로 있어 고칠지 묻는 자리에서 쓴다
- [ ] `docs/tasks/review.md`에 적고 그 파일만 tasks 이름으로 시작하는 메시지로 커밋한다. 고치지 않고 묻지 않으며, 범주 등급, 게이트 통과 여부, 문제 수, 기록 위치를 정해 둔 줄로 돌려준다

**통과 조건**
- review 본문이 TODO대로다
  - 확인: `plugins/plate/skills/review/SKILL.md`를 읽어 TODO 항목마다 그 동작이 적힌 곳을 찾는다
- 완료 조건 2 가운데 review 본문의 몫이 참이다
  - 확인: `grep -n "작업" plugins/plate/skills/review/SKILL.md`의 줄을 모두 읽어 tasks, task, phase를 가리키는 "작업"이 없다
