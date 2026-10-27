# Phase 1: cleanup 스킬 본문

**목표**: `plugins/plate/skills/cleanup/SKILL.md`가 task 머리의 결정대로 절차, 낱말, 절대 규칙, 보고서 양식을 담는다.

**테스트 먼저**: 아니오 — `.md`만 쓴다

**읽을 것**
- `plugins/plate/skills/review/SKILL.md` (앞머리와 description의 꼴, 절대 규칙의 꼴과 "프로젝트의 규칙이 우선" 문단, 바뀐 코드 파일·결과물인 마크다운·측정 못함의 낱말)
- `plugins/plate/skills/run/SKILL.md`의 323~352줄 (`docs/BACKLOG.md`를 처음 만들 때 문서 지도에 행을 더하는 방식과 양식을 적는 꼴)
- `plugins/plate/skills/setup/SKILL.md`의 150~166줄 (문서 지도 구간의 표식과 표)
- `plugins/plate/skills/plan/SKILL.md` (plan이 요청 글을 어떻게 받는지, 진행 중인 tasks가 있을 때 묻는 것)
- `docs/ARCHITECTURE.md`의 "패턴과 규칙" (다른 스킬은 이름으로 부른다, 양식은 본문 안에, 동작으로 쓰고 도구 이름을 쓰지 않는다)
- `docs/PRD.md`의 9단계 줄

**TODO**
- [ ] `plugins/plate/skills/cleanup/SKILL.md`가 새로 생긴다. 앞머리에 `name: cleanup`과, 무엇을 하고 언제 쓰고 언제 쓰지 않는지(코드 평가, 회고, phase 확인에는 쓰지 않는다)를 적은 description이 있다 (`plugins/plate/skills/cleanup/SKILL.md`)
- [ ] 본문에 막는 실패, 절대 규칙(프로젝트 규칙 우선 문단, 코드를 고치지 않는다, 쓰는 파일과 커밋은 보고서와 지도 행뿐, 푸시·브랜치 금지, 묻는 자리는 tasks로 만들지 묻는 곳뿐), 낱말이 들어간다 (같은 파일)
- [ ] 본문에 task 머리 결정의 차례대로 단계가 들어간다: 셋업 확인, 범위, 지난 보고서, 1라운드(여섯 기준의 새 에이전트), 2라운드(기준마다 새 에이전트의 교차 검토), 보고서 쓰기와 지도 행과 커밋, tasks로 만들지 묻기(발견 번호를 고르게 한다), 동의하면 보고서 경로와 고른 번호를 담은 요청으로 `plate:plan`을 부르고 고르지 않은 것은 "미룸"으로 표시해 커밋, 보고 (같은 파일)
- [ ] 본문에 에이전트에게 맡기는 글의 꼴(기준, 범위, 근거 꼴, 2라운드에 넘길 다른 기준의 발견)과 보고서 양식(범위, 지난 보고서와 견준 것, 기준마다의 절, 발견마다 번호·근거·심각도·2라운드 판정, 버린 것과 까닭, 미룬 것)이 코드 블록으로 들어간다 (같은 파일)

**통과 조건**
- 스킬 파일이 있고 앞머리가 맞다(완료 조건 1)
  - 확인: `head -3 plugins/plate/skills/cleanup/SKILL.md`에 `name: cleanup`이 있다
- 여섯 기준, 보고서 위치, plan 호출이 본문에 있다
  - 확인: `grep -c -E '보안|성능|신뢰성|유지보수성|기능 적합성|기존 작업 정합성' plugins/plate/skills/cleanup/SKILL.md`가 6 이상
  - 확인: `grep -o -E 'docs/cleanup/|plate:plan|미룸' plugins/plate/skills/cleanup/SKILL.md | sort -u`가 세 줄을 모두 낸다
- 금지가 절대 규칙에 있다
  - 확인: 절대 규칙 절을 읽어 코드를 고치지 않는다, 보고서와 지도 행만 커밋한다, 푸시하지 않는다, 브랜치를 만들거나 바꾸지 않는다가 저마다 있다. 하나라도 없으면 실패
- 마켓플레이스가 유효하고 테스트가 통과한다
  - 확인: `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
  - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
