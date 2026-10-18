# Phase 4: retro를 task 회고로 바꾸고 verify를 없앤다

**목표**: retro가 task 하나를 회고해 `retro.md`와 `FRICTION.md`에 적고, verify 스킬은 없다.

**테스트 먼저**: 아니오 — `.md`만 고치고 지운다.

**읽을 것**
- `plugins/plate/skills/retro/SKILL.md` (지금의 phase 회고)
- `plugins/plate/skills/verify/SKILL.md` (지금의 작업 검증: 완료 조건 확인, 작업 전체 점검의 넷, 테스트 먼저 기록 확인. 지우기 전에 읽는다)
- `plugins/plate/skills/check/SKILL.md` (phase 3이 만든 확인 절)
- `plugins/plate/skills/phase/SKILL.md` (기록 다섯 절과 "하네스에서 걸린 것")
- `plugins/plate/skills/plan/SKILL.md` (tasks 머리와 task 머리의 양식)

**TODO**
- [x] retro가 task 폴더 하나를 받아 task 머리의 완료 조건 확인과 `docs/ARCHITECTURE.md` 명령 절의 빌드·린트·테스트를 직접 돌린다(없는 명령은 "없음") (`plugins/plate/skills/retro/SKILL.md`)
- [x] task의 커밋이 바꾼 것 전부를 task 머리, tasks 머리, 맥락 문서에 대어 지금 verify의 넷(목표와 결정, 범위 밖, 맥락 문서, 결함)으로 점검하고, 테스트 먼저가 "예"인 `done-phase-N.md`마다 실패 출력과 통과 출력이 이 순서로 있는지 본다
- [x] 회고 기록이 task 폴더의 `retro.md`에 회고 절(몇 번째인지, 확인, 문제, 판정 통과 또는 문제 있음)로 쌓이고, 판정과 문제 수와 기록 위치를 정해 둔 줄로 돌려준다
- [x] retro가 `docs/tasks/FRICTION.md`에 그 task에서 tasks 끝에 볼 것(문제, 멈춤, 스킬로 만들 후보)을 task 이름과 함께 한 줄씩 더한다. phase 기록의 "하네스에서 걸린 것", `RUNLOG.md`의 물은 줄, 점검에서 본 것에서 모은다. 볼 것이 없으면 task 이름과 "없음"을 한 줄로 적는다. 파일이 없으면 만든다
- [x] retro는 `retro.md`와 `FRICTION.md`만 `NNN-slug: 회고`로 커밋한다. 고치지 않고 묻지 않는다
- [x] phase 하나의 회고, "확인만" 방식, 끝나지 않은 작업, "배운 것"이 본문에서 빠진다
- [x] `plugins/plate/skills/verify/`가 지워진다
- [x] description이 새 동작을 말한다

**통과 조건**
- retro 본문이 TODO대로다
  - 확인: `plugins/plate/skills/retro/SKILL.md`를 읽어 TODO 항목마다 그 동작이 적힌 곳을 찾는다
- verify가 없고 retro에 옛 방식이 남지 않았다
  - 확인: `ls plugins/plate/skills/verify` → `No such file or directory`
  - 확인: `grep -n "verify\|확인만\|배운 것" plugins/plate/skills/retro/SKILL.md` → 0줄
- 완료 조건 2 가운데 retro 본문의 몫이 참이다
  - 확인: `grep -n "작업" plugins/plate/skills/retro/SKILL.md`의 줄을 모두 읽어 tasks, task, phase를 가리키는 "작업"이 없다

## 한 일
- retro가 task 폴더 하나를 받아 task 머리의 완료 조건 확인과 `docs/ARCHITECTURE.md` 명령 절의 빌드·린트·테스트를 직접 돌린다(없는 명령은 "없음"): 0번이 넘겨받은 task 폴더(또는 사용자가 준 번호나 이름)를 대상으로 삼고, 받지 못했거나 `phase-N.md`가 남았으면 회고하지 않는다(지운 verify의 0번에서 옮김). 2번이 task 머리의 완료 조건 확인을, 3번이 명령 절의 세 명령을 check와 같은 글로 돌린다 (`plugins/plate/skills/retro/SKILL.md`)
- task의 커밋이 바꾼 것 전부를 넷으로 점검하고 테스트 먼저 기록을 본다: 4번이 task 전체의 변경을 task 머리·tasks 머리의 목표와 결정, 범위 밖과 다른 task의 일, 맥락 문서, 결함에 대어 보고, 테스트 먼저가 "예"인 `done-phase-N.md`마다 실패·통과 출력의 순서를 본다. "task의 커밋"을 낱말 절에 정의했다(계획의 커밋과 다른 task 이름의 커밋은 이 task 폴더의 변경만 본다) (`plugins/plate/skills/retro/SKILL.md`)
- 회고 기록이 `retro.md`의 회고 절로 쌓이고 정해 둔 줄로 돌려준다: 6번과 양식이 `## 회고 {번호}` 아래 확인(완료 조건, 명령 절, 테스트 먼저 기록), 문제, 판정(통과 | 문제 있음)을 적고, 파일이 없으면 `# 회고`로 만든다. 9번이 판정, 문제 수, 기록 위치 세 줄을 돌려준다 (`plugins/plate/skills/retro/SKILL.md`)
- retro가 `FRICTION.md`에 tasks 끝에 볼 것을 더한다: 5번이 문제(기록과 확인 절의 "하네스에서 걸린 것", 실패였던 확인 절, 점검에서 본 것), 멈춤(`RUNLOG.md`의 물은 줄), 스킬로 만들 후보(되풀이된 손일)를 모으고, 7번이 task 이름을 붙여 한 줄씩 더한다. 볼 것이 없으면 task 이름과 "없음"을 한 줄로 적고, 파일이 없으면 `# FRICTION`으로 만든다. 같은 task를 다시 회고할 때 이미 있는 줄은 다시 적지 않는다 (`plugins/plate/skills/retro/SKILL.md`)
- retro는 `retro.md`와 `FRICTION.md`만 `NNN-slug: 회고`로 커밋하고 고치지도 묻지도 않는다: 절대 규칙 1·4·5와 8번에 적었다 (`plugins/plate/skills/retro/SKILL.md`)
- phase 하나의 회고, "확인만" 방식, 끝나지 않은 작업, "배운 것"이 빠진다: 본문을 새로 써 넷 모두 없앴다. 옛 "하네스의 문제점"은 `FRICTION.md`의 문제 줄로 옮겼다 (`plugins/plate/skills/retro/SKILL.md`)
- `plugins/plate/skills/verify/`가 지워진다: `git rm -r plugins/plate/skills/verify` (`plugins/plate/skills/verify/SKILL.md`)
- description이 새 동작을 말한다: task 회고, 두 파일에 적기, 두 파일만 커밋, run이 부르는 때, 쓰지 않는 일(phase 하나의 확인, tasks 끝의 평가)을 적었다 (`plugins/plate/skills/retro/SKILL.md`)

## 확인 결과
- retro 본문이 TODO대로다
  - `plugins/plate/skills/retro/SKILL.md`를 읽음 → TODO 1: 0·2·3번, TODO 2: 4번, TODO 3: 6·9번과 회고 절 양식, TODO 4: 5·7번과 `FRICTION.md`의 줄 양식, TODO 5: 절대 규칙 1·4·5와 8번, TODO 6: 본문에 phase 회고·확인만·끝나지 않은 작업·배운 것이 없음, TODO 8: description. 통과
- verify가 없고 retro에 옛 방식이 남지 않았다
  - `ls plugins/plate/skills/verify` → `ls: plugins/plate/skills/verify: No such file or directory`. 통과
  - `grep -n "verify\|확인만\|배운 것" plugins/plate/skills/retro/SKILL.md` → 0줄. 통과
- 완료 조건 2 가운데 retro 본문의 몫이 참이다
  - `grep -n "작업" plugins/plate/skills/retro/SKILL.md` → 0줄(읽을 줄이 없어 tasks, task, phase를 가리키는 "작업"이 없다). 통과

## 계획과 달라진 점
- 없음

## 남은 것
- 없음

## 하네스에서 걸린 것
- `RUNLOG.md`의 줄 꼴은 이 phase의 읽을 것에 없다(run 본문에 정해질 것). 그래서 retro 5번은 "물은 줄 가운데 이 task를 실행하며 물은 것"을 뜻으로만 가리켰다. 물은 줄에 task 이름이 들지 않으면 retro가 이 task의 물음을 가려내지 못할 수 있다.
- verify를 지운 뒤에도 `plugins/plate/skills/run/SKILL.md`, 두 매니페스트, `README.md`, `AGENTS.md`, `docs/PRD.md`, `docs/ARCHITECTURE.md`에 verify가 남아 있다. 이 phase의 TODO가 아니라 고치지 않았다(머리의 완료 조건 5, 10, 12의 몫).

## 회고 1: 확인만

**확인**
- retro 본문이 TODO대로다
  - `plugins/plate/skills/retro/SKILL.md`를 읽음 → TODO 1: 0번(38줄, 넘겨받은 task 폴더), 2번(54줄, task 머리의 완료 조건 확인), 3번(60줄, 명령 절의 빌드·린트·테스트, 없는 명령은 "없음"). TODO 2: 4번(64~69줄, task의 커밋이 바꾼 것 전부를 목표와 결정·범위 밖·맥락 문서·결함 넷에 대어 봄), 73줄(테스트 먼저 "예"인 `done-phase-N.md`마다 실패·통과 출력 순서). TODO 3: 6번(91줄)과 회고 절 양식(125~140줄, 번호·확인·문제·판정 통과 | 문제 있음), 9번(110~114줄, 판정·문제 수·기록 세 줄). TODO 4: 5번(79~81줄, "하네스에서 걸린 것"·`RUNLOG.md`의 물은 줄·점검에서 본 것), 7번(97~99줄, task 이름을 붙인 한 줄, 없으면 "없음", 파일이 없으면 `# FRICTION`으로 만듦)과 줄 양식(146~147줄). TODO 5: 절대 규칙 1·4·5(16~20줄)와 8번(104줄, `NNN-slug: 회고`). TODO 6: 본문에 phase 하나의 회고 절차·확인만·끝나지 않은 작업·배운 것이 없고, 40줄이 `phase-N.md`가 남은 task는 회고하지 않는다고 적음. TODO 7: 아래 `ls`. TODO 8: description(3줄)이 task 회고, 두 파일에 적기, 두 파일만 커밋, run이 부르는 때, 쓰지 않는 일을 말함. 통과
- verify가 없고 retro에 옛 방식이 남지 않았다
  - `ls plugins/plate/skills/verify` → `ls: plugins/plate/skills/verify: No such file or directory`. 통과
  - `grep -n "verify\|확인만\|배운 것" plugins/plate/skills/retro/SKILL.md` → 0줄. 통과
- 완료 조건 2 가운데 retro 본문의 몫이 참이다
  - `grep -n "작업" plugins/plate/skills/retro/SKILL.md` → 0줄(읽을 줄이 없어 tasks, task, phase를 가리키는 "작업"이 없다). 통과

**문제**
- 없음

**판정**: 통과
