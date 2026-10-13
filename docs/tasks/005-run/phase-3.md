# Phase 3: 004의 계획을 새 꼴로 옮긴다

**목표**: `004-context-rules`의 계획이 `plan.md`(머리)와 `phase-1.md`, `phase-2.md`로 나뉘어 있고 ADR-034에 걸린 것이 없다.

**읽을 것**
- `docs/tasks/004-context-rules/plan.md` (옮길 계획)
- `plugins/plate/skills/plan/SKILL.md` (Phase 1에서 고친 양식 둘과 결정을 적는 규칙)

**TODO**
- [x] `## Phase 1`, `## Phase 2` 절이 `phase-1.md`, `phase-2.md`로 옮겨진다. 제목만 `# Phase N: 이름`으로 바뀌고 글은 그대로다 (`docs/tasks/004-context-rules/`)
- [x] ADR-034에 걸린 것이 빠진다: 완료 조건 5, 결정의 여덟째, Phase 1의 제목과 목표의 "결정을 적는다", Phase 1의 TODO 셋(ADR-034, 원장 설명, ADR-013의 표시)과 통과 조건의 "완료 조건 5", Phase 2의 "고친 내용은 ADR-034에 더해진다"와 통과 조건의 5
- [x] 결정에서 고르지 않은 안을 뺄지를 초안에서 사용자에게 묻고 답대로 한다
- [x] 세 파일의 초안을 사용자에게 보여 주고 승인받은 뒤에 쓰고, 그 세 파일만 `plan: 004-context-rules 수정`으로 커밋한다

**통과 조건**
- 004의 작업 폴더에 세 파일이 있고 `plan.md`에 phase 절이 없다.
  - 확인: `ls docs/tasks/004-context-rules/` → `phase-1.md`, `phase-2.md`, `plan.md`
  - 확인: `grep -c '^## Phase' docs/tasks/004-context-rules/plan.md` → 0
- ADR-034를 가리키는 곳이 없다.
  - 확인: `grep -rc 'ADR-034' docs/tasks/004-context-rules/` → 모두 0
- 커밋에 든 파일이 그 셋뿐이다.
  - 확인: `git log -1 --name-only --format=%s -- docs/tasks/004-context-rules/` → 제목 `plan: 004-context-rules 수정`과 세 파일

## 한 일
- phase 절을 파일로 옮긴다: `## Phase 1`, `## Phase 2` 절을 `phase-1.md`, `phase-2.md`로 옮기고 제목을 `# Phase N: 이름`으로 바꿨다. `plan.md`에는 머리만 남았다 (`docs/tasks/004-context-rules/plan.md`, `phase-1.md`, `phase-2.md`)
- ADR-034에 걸린 것을 뺀다: 완료 조건 5, 결정의 여덟째, Phase 1의 제목과 목표의 그 구절, TODO 셋, 통과 조건의 "완료 조건 5", Phase 2의 그 문장과 통과 조건의 5를 뺐다 (`docs/tasks/004-context-rules/`)
- 고르지 않은 안: 사용자가 "빼고 승인"을 골라 결정의 다섯 문장을 뺐다 (`docs/tasks/004-context-rules/plan.md`)
- 초안과 커밋: 바뀌는 곳을 답글로 보여 주고 승인받은 뒤에 쓰고 세 파일만 커밋했다(`7430f81`)

## 확인 결과
- 004의 작업 폴더에 세 파일이 있고 `plan.md`에 phase 절이 없다.
  - `ls docs/tasks/004-context-rules/` → `phase-1.md`, `phase-2.md`, `plan.md`. 통과
  - `grep -c '^## Phase' docs/tasks/004-context-rules/plan.md` → 0. 통과
- ADR-034를 가리키는 곳이 없다.
  - `grep -rc 'ADR-034' docs/tasks/004-context-rules/` → 세 파일 모두 0. 통과
- 커밋에 든 파일이 그 셋뿐이다.
  - `git log -1 --name-only --format=%s -- docs/tasks/004-context-rules/` → 제목 `plan: 004-context-rules 수정`과 `phase-1.md`, `phase-2.md`, `plan.md`. 통과

## 계획과 달라진 점
- TODO에 적힌 것 말고 Phase 1의 읽을 것에서 `docs/ADR.md` 줄을 뺐다. 그 줄이 가리키는 넷이 모두 빠지는 TODO 셋을 위한 것이었다. 초안에서 보여 주고 승인받았다.
- 옮기지 않은 글은 옛 `plan.md`와 한 글자도 다르지 않다. 옛 파일과 새 세 파일을 이은 것을 `diff`로 대어 위의 것만 다른 것을 봤다.

## 남은 것
없음

## 하네스에서 걸린 것
없음
