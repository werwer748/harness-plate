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
- [x] `plugins/plate/skills/cleanup/SKILL.md`가 새로 생긴다. 앞머리에 `name: cleanup`과, 무엇을 하고 언제 쓰고 언제 쓰지 않는지(코드 평가, 회고, phase 확인에는 쓰지 않는다)를 적은 description이 있다 (`plugins/plate/skills/cleanup/SKILL.md`)
- [x] 본문에 막는 실패, 절대 규칙(프로젝트 규칙 우선 문단, 코드를 고치지 않는다, 쓰는 파일과 커밋은 보고서와 지도 행뿐, 푸시·브랜치 금지, 묻는 자리는 tasks로 만들지 묻는 곳뿐), 낱말이 들어간다 (같은 파일)
- [x] 본문에 task 머리 결정의 차례대로 단계가 들어간다: 셋업 확인, 범위, 지난 보고서, 1라운드(여섯 기준의 새 에이전트), 2라운드(기준마다 새 에이전트의 교차 검토), 보고서 쓰기와 지도 행과 커밋, tasks로 만들지 묻기(발견 번호를 고르게 한다), 동의하면 보고서 경로와 고른 번호를 담은 요청으로 `plate:plan`을 부르고 고르지 않은 것은 "미룸"으로 표시해 커밋, 보고 (같은 파일)
- [x] 본문에 에이전트에게 맡기는 글의 꼴(기준, 범위, 근거 꼴, 2라운드에 넘길 다른 기준의 발견)과 보고서 양식(범위, 지난 보고서와 견준 것, 기준마다의 절, 발견마다 번호·근거·심각도·2라운드 판정, 버린 것과 까닭, 미룬 것)이 코드 블록으로 들어간다 (같은 파일)

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

## 한 일
- `plugins/plate/skills/cleanup/SKILL.md`가 새로 생긴다(앞머리): `name: cleanup`과, 하는 일, 쓸 때, 쓰지 않을 때(코드 평가, task 회고, phase 확인, 하네스 eval)를 적은 description을 넣었다 (`plugins/plate/skills/cleanup/SKILL.md`)
- 막는 실패, 절대 규칙, 낱말: 프로젝트 규칙 우선 문단과 다섯 절대 규칙(코드를 고치지 않는다, 쓰는 파일과 커밋은 보고서와 지도 행뿐, 푸시·브랜치 금지, 묻는 자리는 6번뿐, 근거 없이 발견을 적지 않는다), 여섯 기준·살필 파일·결과물인 마크다운(review와 같은 뜻)·발견·심각도·2라운드 판정·버림·미룸·측정 못함의 낱말을 넣었다 (같은 파일)
- 단계: 0 셋업 확인(없으면 setup을 알리고 끝남, 묻지 않음), 1 범위와 보고서 경로(같은 날이면 `-2` 번호), 2 지난 보고서, 3 1라운드(기준 표, 기준마다 새 에이전트, `gh` 실패는 측정 못함), 4 2라운드(기준마다 새 에이전트, 메인이 반박·중복·충돌을 정해 버림을 까닭과 함께), 5 보고서·지도 행·커밋(묻기 전에), 6 번호로 고르게 묻기, 7 미룸 표시 커밋 뒤 고른 번호와 보고서 경로를 담은 요청으로 `plate:plan` 호출, 8 보고 (같은 파일)
- 맡기는 글과 보고서 양식: 1라운드·2라운드에 맡기는 글, plan에 넘기는 요청, 보고서 양식(범위, 지난 보고서와 견준 것, 여섯 기준의 절, 발견마다 번호·근거·심각도·고치는 방향·2라운드·처리, 버린 것, 미룬 것, 하네스에서 걸린 것)과 적는 규칙을 코드 블록으로 넣었다 (같은 파일)

## 확인 결과
- 스킬 파일이 있고 앞머리가 맞다(완료 조건 1)
  - `head -3 plugins/plate/skills/cleanup/SKILL.md` → 둘째 줄이 `name: cleanup`. 통과
- 여섯 기준, 보고서 위치, plan 호출이 본문에 있다
  - `grep -c -E '보안|성능|신뢰성|유지보수성|기능 적합성|기존 작업 정합성' plugins/plate/skills/cleanup/SKILL.md` → `29`. 통과
  - `grep -o -E 'docs/cleanup/|plate:plan|미룸' plugins/plate/skills/cleanup/SKILL.md | sort -u` → `docs/cleanup/`, `plate:plan`, `미룸` 세 줄. 통과
- 금지가 절대 규칙에 있다
  - 절대 규칙 절을 읽음 → 1번 "코드를 고치지 않는다", 2번 "쓰는 파일은 그 날의 보고서와 `AGENTS.md` 문서 지도의 행뿐이다. 커밋에도 이 둘만", 3번 "푸시하지 않는다. 브랜치를 만들거나 바꾸지 않는다"가 있다. 통과
- 마켓플레이스가 유효하고 테스트가 통과한다
  - `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
  - `python3 -m unittest discover -s tests` → 마지막 줄 `OK`. 통과

## 계획과 달라진 점
- TODO 3은 "plan을 부르고 고르지 않은 것은 미룸으로 표시해 커밋"의 차례로 적었으나, 본문은 미룸 표시 커밋을 먼저 하고 plan을 부르게 적었다. plan은 여러 번 묻고 그 사이 세션이 끊길 수 있어, 보고서를 묻기 전에 커밋하는 결정과 같은 까닭으로 미룸을 먼저 남겼다. 하는 일은 같고 차례만 다르다.
- 결정이 정하지 않은 세부를 본문에서 정했다: 커밋 메시지(`cleanup: YYYY-MM-DD`, `cleanup: YYYY-MM-DD 미룸`), 하나도 고르지 않으면 모든 발견을 미룸으로 적는 것, 에이전트가 답을 돌려주지 않으면 다시 띄우지 않고 측정 못함으로 적는 것, 심각도를 높음·중간·낮음 셋으로 둔 것.

## 남은 것
- 없음. 다만 본문은 아직 실제로 돌려 보지 않았다. 두 장면으로 돌리는 확인은 phase 2가 한다.

## 하네스에서 걸린 것
- 막힘: 권한 — 파일 쓰기 도구의 호출이 auto mode 분류기의 무판정으로 막혀 `plugins/plate/skills/cleanup/SKILL.md`를 만들지 못함. 해결책: 사용자가 그 쓰기를 승인하거나 권한 모드를 바꾼 뒤 이어 수행.
- 막힘(이어 한 수행에서 다시): 같은 파일을 쓰는 호출이 다시 auto mode 분류기의 무판정으로 막힘. 다른 도구(셸)로 돌아가 쓰는 것은 권한 검사를 피하는 일이라 하지 않음. 해결책: 사용자가 `plugins/plate/skills/cleanup/` 쓰기를 허용(권한 규칙 추가나 수동 승인 모드)한 뒤 이어 수행.
- 이어 한 수행에서 plan 모드가 끝난 뒤 다시 쓰자 `plugins/plate/skills/cleanup/SKILL.md` 쓰기가 통과했다. 앞의 두 막힘은 plan 모드가 켜진 채라 분류기가 쓰기를 판정하지 않은 것으로 보인다.

## 확인 1

**통과 조건**
- 스킬 파일이 있고 앞머리가 맞다(완료 조건 1)
  - `head -3 plugins/plate/skills/cleanup/SKILL.md` → 둘째 줄이 `name: cleanup`. 통과
- 여섯 기준, 보고서 위치, plan 호출이 본문에 있다
  - `grep -c -E '보안|성능|신뢰성|유지보수성|기능 적합성|기존 작업 정합성' plugins/plate/skills/cleanup/SKILL.md` → `29`. 통과
  - `grep -o -E 'docs/cleanup/|plate:plan|미룸' plugins/plate/skills/cleanup/SKILL.md | sort -u` → `docs/cleanup/`, `plate:plan`, `미룸` 세 줄. 통과
- 금지가 절대 규칙에 있다
  - `plugins/plate/skills/cleanup/SKILL.md`의 `## 절대 규칙` 절을 읽음 → 1번 "코드를 고치지 않는다", 2번 "쓰는 파일은 그 날의 보고서와 `AGENTS.md` 문서 지도의 행뿐이다. 커밋에도 이 둘만 넣는다", 3번 "푸시하지 않는다. 브랜치를 만들거나 바꾸지 않는다"가 있다. 통과
- 마켓플레이스가 유효하고 테스트가 통과한다
  - `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
  - `python3 -m unittest discover -s tests` → `Ran 104 tests`, 마지막 줄 `OK`. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → 104개 실행, `OK`. 통과

**실패**
- 없음

**하네스에서 걸린 것**
- 없음

**판정**: 통과
