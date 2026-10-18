# Phase 3: phase를 task 구조에 맞추고 check를 만든다

**목표**: 수행 에이전트가 task 머리와 자기 phase 파일로 수행하고, 새 check 스킬이 phase 하나를 따로 확인해 판정을 그 phase 파일에 남긴다.

**테스트 먼저**: 아니오 — `.md`만 고치고 만든다.

**읽을 것**
- `plugins/plate/skills/phase/SKILL.md` (지금의 수행 절차, 기록 다섯 절의 양식, 막힘과 계획이 틀림)
- `plugins/plate/skills/retro/SKILL.md` (지금의 "확인만" 방식과 회고 절의 양식. check가 이 확인을 이어받는다)
- `plugins/plate/skills/plan/SKILL.md` (phase 1이 바꾼 tasks 구조, task 머리 양식, 명령 절 규칙)
- `docs/ARCHITECTURE.md` (스킬 본문을 쓰는 규칙)

**TODO**
- [x] phase의 낱말이 task 폴더, task 머리, phase로 바뀌고, 읽는 것이 task 머리와 넘겨받은 `phase-N.md`다 (`plugins/plate/skills/phase/SKILL.md`)
- [x] phase가 넘겨받는 "고칠 문제"가 그 `phase-N.md`의 마지막 확인 절에 적힌 실패로 바뀌고, 회고 절을 가리키는 글이 없어진다
- [x] check 스킬이 생긴다: task 폴더와 phase 번호를 받아 그 phase의 통과 조건 확인과 `docs/ARCHITECTURE.md` 명령 절의 빌드·린트·테스트를 직접 돌린다. 없는 명령은 "없음"으로 적는다. 테스트 먼저가 "예"이면 기록에 실패 출력과 통과 출력이 이 순서로 있는지 본다 (`plugins/plate/skills/check/SKILL.md`)
- [x] check가 `phase-N.md` 끝에 확인 절(몇 번째인지, 확인마다 돌린 명령과 결과, 판정 통과 또는 실패)을 더하고 그 파일만 `NNN-slug: phase N 확인`으로 커밋한다. 고치지 않고 묻지 않으며, 판정과 실패 수와 기록 위치를 정해 둔 줄로 돌려준다
- [x] 두 스킬의 description이 새 동작을 말한다

**통과 조건**
- 두 본문이 TODO대로다
  - 확인: 두 `SKILL.md`를 읽어 TODO 항목마다 그 동작이 적힌 곳을 찾는다
- phase 본문이 회고 절을 가리키지 않는다
  - 확인: `grep -n "회고" plugins/plate/skills/phase/SKILL.md` → 0줄
- 완료 조건 2 가운데 두 본문의 몫이 참이다
  - 확인: `grep -n "작업" plugins/plate/skills/phase/SKILL.md plugins/plate/skills/check/SKILL.md`의 줄을 모두 읽어 tasks, task, phase를 가리키는 "작업"이 없다

## 한 일
- phase의 낱말이 task 폴더, task 머리, phase로 바뀌고, 읽는 것이 task 머리와 넘겨받은 `phase-N.md`다: 낱말 절을 tasks, task 폴더, task 머리(네 절), `phase-N.md`, 확인 절, 고칠 문제로 바꿨고, 1번 "읽는다"가 task 머리와 넘겨받은 `phase-N.md`만 읽고 tasks 머리와 다른 phase의 파일(`phase-N.md`, `done-phase-N.md`)은 읽지 않는다고 적는다. 절대 규칙 1·3, 계획이 틀림의 머리, 커밋에서 빼는 파일도 task 머리로 맞췄고, 첫머리의 "지우지 않고"를 "이름을 바꾸지 않고"로 바꿨다 (`plugins/plate/skills/phase/SKILL.md`)
- phase가 넘겨받는 "고칠 문제"가 그 `phase-N.md`의 마지막 확인 절에 적힌 실패로 바뀌고, 회고 절을 가리키는 글이 없어진다: 낱말 "고칠 문제"를 마지막 확인 절의 "실패"에 적힌 것으로 정의하고, 1·2번과 테스트 먼저 실패 출력을 되살리는 경우를 그 실패로 바꿨다. 4번의 "회고 절은 건드리지 않는다"는 "확인 절은 건드리지 않는다"로, 6번의 직접 부른 경우 안내는 "확인과 그 뒤의 일은 run"으로 바꿨다 (`plugins/plate/skills/phase/SKILL.md`)
- check 스킬이 생긴다: 0번에서 task 폴더와 phase 번호를 받고, 2번에서 통과 조건의 확인을, 3번에서 명령 절의 빌드·린트·테스트를 이 순서로 직접 돌리며 "없음"이거나 명령 절·줄이 없는 명령은 "없음"(실패 아님)으로 적고, 4번에서 테스트 먼저가 "예"이면 실패 출력과 통과 출력의 순서를 본다 (`plugins/plate/skills/check/SKILL.md`)
- check가 확인 절을 더하고 그 파일만 커밋하며 정해 둔 줄로 돌려준다: 5번과 양식이 `## 확인 {몇 번째}` 절(통과 조건, 명령, 테스트 먼저 기록, 실패, 하네스에서 걸린 것, 판정)을 끝에 쌓고, 6번이 판정이 실패여도 `phase-N.md` 하나만 `NNN-slug: phase N 확인`으로 커밋하고, 7번이 판정·실패 수·기록 세 줄을 돌려준다. 절대 규칙 1·4가 고치지 않고 묻지 않는다 (`plugins/plate/skills/check/SKILL.md`)
- 두 스킬의 description이 새 동작을 말한다: phase는 task 머리와 `phase-N.md`만 읽고 고칠 문제면 마지막 확인 절의 실패를 고친다고, check는 통과 조건·명령 절·테스트 먼저 기록을 직접 보고 확인 절을 더해 그 파일만 커밋한다고 적는다 (`plugins/plate/skills/phase/SKILL.md`, `plugins/plate/skills/check/SKILL.md`)

## 확인 결과
- 두 본문이 TODO대로다
  - 두 `SKILL.md`를 읽어 TODO 항목마다 찾음 → TODO 1: phase 낱말 절(25~29줄)과 1번(34줄). TODO 2: 낱말 "고칠 문제"(29줄), 1번(38줄), 2번(45·47·55줄), 4번(76줄). TODO 3: check 0번(32줄), 2번(42줄), 3번(48줄, "없음"은 실패가 아님), 4번(52줄). TODO 4: check 5번과 양식(54·58·81~101줄), 6번(62줄, `NNN-slug: phase N 확인`), 7번(64~71줄 세 줄), 절대 규칙 1·4(16·19줄). TODO 5: 두 파일의 3줄 description. 통과
- phase 본문이 회고 절을 가리키지 않는다
  - `grep -n "회고" plugins/plate/skills/phase/SKILL.md` → 0줄. 통과
- 완료 조건 2 가운데 두 본문의 몫이 참이다
  - `grep -n "작업" plugins/plate/skills/phase/SKILL.md plugins/plate/skills/check/SKILL.md` → 0줄(읽을 줄이 없어 tasks, task, phase를 가리키는 "작업"이 없다). 통과

## 계획과 달라진 점
없음

## 남은 것
없음

## 하네스에서 걸린 것
- phase-3.md TODO 4의 "확인 절"은 phase 기록에 이미 있는 "확인 결과" 절과 이름이 겹친다. check의 절 제목을 `## 확인 1`처럼 번호를 붙여 가르고, 두 스킬의 낱말 절에 "기록의 '확인 결과' 절과 다르다"를 적었다. 훅이나 run이 제목으로 확인 절을 셀 때는 `## 확인 결과`를 빼고 `## 확인 <번호>`만 세야 한다.
- 이 레포의 `docs/ARCHITECTURE.md`에는 아직 명령 절이 없다. check는 그때 세 명령을 "없음"으로 적고 "하네스에서 걸린 것"에 적도록 했다.

## 회고 1: 확인만

**확인**
- 두 본문이 TODO대로다
  - 두 `SKILL.md`를 읽어 TODO 항목마다 찾음 → TODO 1: phase 낱말 절(24~29줄)에 tasks, task 폴더, task 머리, `phase-N.md`가 있고 1번(34줄)이 task 머리와 넘겨받은 `phase-N.md`만 읽으며 tasks 머리와 다른 phase의 파일은 읽지 않는다. TODO 2: 낱말 "고칠 문제"(29줄)가 마지막 확인 절의 "실패"에 적힌 것이고 1번(38줄), 2번(45·55줄)이 그것을 쓴다. TODO 3: check 0번(34줄)이 task 폴더와 phase 번호를 받고, 2번(44줄)이 통과 조건의 확인을, 3번(48줄)이 명령 절의 빌드·린트·테스트를 직접 돌리며 없는 명령은 "없음"(실패 아님)으로 적고, 4번(52줄)이 테스트 먼저가 "예"이면 실패 출력과 통과 출력의 순서를 본다. TODO 4: 5번(56줄)과 양식(81~101줄)이 번호, 확인마다 돌린 명령과 결과, 판정을 둔 확인 절을 끝에 더하고, 6번(62줄)이 그 파일만 `NNN-slug: phase N 확인`으로 커밋하고, 절대 규칙 1·4(16·19줄)가 고치지 않고 묻지 않으며, 7번(68~72줄)이 판정·실패 수·기록 세 줄을 돌려준다. TODO 5: 두 파일의 3줄 description이 새 동작을 말한다. 통과
- phase 본문이 회고 절을 가리키지 않는다
  - `grep -n "회고" plugins/plate/skills/phase/SKILL.md` → 0줄(종료 코드 1). 통과
- 완료 조건 2 가운데 두 본문의 몫이 참이다
  - `grep -n "작업" plugins/plate/skills/phase/SKILL.md plugins/plate/skills/check/SKILL.md` → 0줄(종료 코드 1). 읽을 줄이 없어 tasks, task, phase를 가리키는 "작업"이 없다. 통과

**문제**
- 없음

**판정**: 통과
