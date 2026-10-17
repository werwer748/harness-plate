# Phase 3: retro, verify, context의 규칙 충돌

**목표**: retro, verify, context 본문의 규칙 충돌이 풀리고, 회고·검증 절에 통과한 테스트 먼저 점검이 남는다.

**테스트 먼저**: 아니오 — 스킬 본문(`.md`)만 고친다

**읽을 것**
- `plugins/plate/skills/retro/SKILL.md` (1번, 3번, 4번, 회고 절의 양식, 적는 규칙)
- `plugins/plate/skills/verify/SKILL.md` (1번, 3번, 4번, 검증 절의 양식, 적는 규칙)
- `plugins/plate/skills/context/SKILL.md` (절대 규칙 5)
- `docs/TOOLS.md`의 Codex 절 "스킬"(본문에 다른 스킬을 이름으로만 적어도 그 `SKILL.md`를 연다)과 Claude Code 절 "실행 스킬의 판정에서 본 것"(에이전트는 프로젝트 밖의 파일을 읽지 못한다)
- `git show ec2f192:docs/LESSONS.md`의 하네스의 문제점 절에서 (007-harness-issues, 검증 1)의 셋째 줄, (008-tdd, phase 1)의 넷째 줄, (008-tdd, phase 3)의 다섯째 줄, (008-tdd, phase 5)의 첫째 줄과, 미룬 문제 절의 (004-context-rules, 검증 1) 줄 (고칠 문제의 원문)

**TODO**
- [x] retro와 verify의 4번에서 다른 스킬의 본문이 그 phase(verify는 작업)의 커밋이 바꾼 파일이거나 계획의 읽을 것이면 1번대로 읽는다 (`plugins/plate/skills/retro/SKILL.md`, `plugins/plate/skills/verify/SKILL.md`)
- [x] retro 3번에서 머리의 결정이나 완료 조건이 바꾸기로 한 맥락 문서의 줄과 어긋나는 것은 문제로 적지 않는다 (`plugins/plate/skills/retro/SKILL.md`)
- [x] 회고 방식의 회고 절과 검증 절의 "확인"에, 테스트 먼저가 "예"인 phase이면 그 기록을 본 줄(본 곳, 실패 출력과 통과 출력이 순서대로 있는지, 통과 | 실패)이 통과해도 적힌다. 양식과 적는 규칙이 이에 맞다 (`plugins/plate/skills/retro/SKILL.md`, `plugins/plate/skills/verify/SKILL.md`)
- [x] context의 절대 규칙 5에 다른 스킬을 이름으로 불러 도구가 그 스킬의 본문을 여는 것은 예외라는 것이 있다 (`plugins/plate/skills/context/SKILL.md`)

**통과 조건**
- 완료 조건 5가 참이다.
  - 확인: 완료 조건 5의 확인을 돌린다
- 완료 조건 6이 참이다.
  - 확인: 완료 조건 6의 확인을 돌린다

## 한 일
- retro와 verify의 4번에서 다른 스킬의 본문이 그 phase(verify는 작업)의 커밋이 바꾼 파일이거나 계획의 읽을 것이면 1번대로 읽는다: 두 본문 4번의 "다른 스킬의 본문은 열지 않고 이름으로만 가리킨다." 뒤에 "다만 그 본문이 그 phase의 커밋이 바꾼 파일(verify는 작업의 커밋이 바꾼 파일)이거나 계획의 읽을 것이면 1번대로 읽고 그 글에 대어 적는다."를 더했다 (`plugins/plate/skills/retro/SKILL.md`, `plugins/plate/skills/verify/SKILL.md`)
- retro 3번에서 머리의 결정이나 완료 조건이 바꾸기로 한 맥락 문서의 줄과 어긋나는 것은 문제로 적지 않는다: 3번의 "넷 가운데 하나에 걸리는 것만 문제로 적는다." 뒤에 그 문장을 더했다 (`plugins/plate/skills/retro/SKILL.md`)
- 회고 방식의 회고 절과 검증 절의 "확인"에, 테스트 먼저가 "예"인 phase이면 그 기록을 본 줄이 통과해도 적힌다. 양식과 적는 규칙이 이에 맞다: 두 본문 3번의 테스트 먼저 기록 점검에 "본 결과는 통과해도 … '확인'에 적는다"(verify는 phase마다)를 더했다. 양식의 "확인"에 "테스트 먼저 기록"(verify는 "테스트 먼저 기록: phase {번호}") 항목과 그 아래 `{본 곳} → {실패 출력과 통과 출력이 이 순서로 있는지}. {통과 | 실패}` 줄을 더했다. 적는 규칙에 그 항목을 적는 때(retro는 회고 방식에서 테스트 먼저 "예"인 phase에만, verify는 그런 phase마다 완료 조건 뒤에)와 "통과해도 적는다", 실패면 "문제"의 기준이 "계획"이라는 것을 더했다 (`plugins/plate/skills/retro/SKILL.md`, `plugins/plate/skills/verify/SKILL.md`)
- context의 절대 규칙 5에 다른 스킬을 이름으로 불러 도구가 그 스킬의 본문을 여는 것은 예외라는 것이 있다: 절대 규칙 5 끝에 "다른 스킬을 이름으로 불러 도구가 그 스킬의 본문을 여는 것(0번의 `plate:setup`)은 예외다."를 더했다 (`plugins/plate/skills/context/SKILL.md`)

## 확인 결과
- 완료 조건 5가 참이다.
  - `plugins/plate/skills/retro/SKILL.md`의 3번(58행, 60행), 4번(64행), 양식(99~100행), 적는 규칙(119~120행)을 읽었다 → (가) 64행 "다만 그 본문이 그 phase의 커밋이 바꾼 파일이거나 계획의 읽을 것이면 1번대로 읽고 그 글에 대어 적는다", (나) 58행 "머리의 결정이나 완료 조건이 바꾸기로 한 맥락 문서의 줄과 어긋나는 것은 문제로 적지 않는다", (다) 60행 "본 결과는 통과해도 회고 절의 '확인'에 적는다", 양식의 "테스트 먼저 기록" 항목, 119행 "회고 방식에서 테스트 먼저가 '예'인 phase에만 적는다. 통과해도 적는다". 통과
  - `plugins/plate/skills/verify/SKILL.md`의 3번(61행), 4번(65행), 양식(100~101행), 적는 규칙(120~121행)을 읽었다 → (가) 65행 "다만 그 본문이 작업의 커밋이 바꾼 파일이거나 계획의 읽을 것이면 1번대로 읽고 그 글에 대어 적는다", (다) 61행 "본 결과는 통과해도 검증 절의 '확인'에 phase마다 적는다", 양식의 "테스트 먼저 기록: phase {번호}" 항목, 120행 "테스트 먼저가 '예'인 phase마다 완료 조건 뒤에 적는다. 통과해도 적는다". (나)는 retro에만 있다. 통과
- 완료 조건 6이 참이다.
  - `plugins/plate/skills/context/SKILL.md`의 절대 규칙 5(18행)를 읽었다 → "다른 스킬을 이름으로 불러 도구가 그 스킬의 본문을 여는 것(0번의 `plate:setup`)은 예외다."가 있다. 통과

## 계획과 달라진 점
없음

## 남은 것
없음

## 하네스에서 걸린 것
- 계획의 완료 조건 5 (가)와 이 phase의 TODO 1: "계획의 읽을 것이면 1번대로 읽는다"의 1번(retro와 verify의 "읽는다")은 계획의 읽을 것을 읽을 목록으로 적지 않는다(retro 1번은 `phase-N.md`의 계획 다섯 항목, verify 1번은 작업의 커밋이 바꾼 것). 커밋이 바꾸지 않고 읽을 것에만 든 스킬 본문은 "1번대로"가 가리키는 줄이 없어, 계획의 글 그대로 "1번대로 읽고"로 적었다.
