# Phase 3: 장면 C와 D를 돌린다

**목표**: 회고가 계획을 바꾸게 할 때 멈추는 것(#34, #38)과 고칠 phase의 TODO·통과 조건(#38)을 임시 복제본에서 돌려 `docs/TOOLS.md`에 남긴다.

**테스트 먼저**: 아니오 — 스킬을 돌려 보고 `.md`에 적는다

**읽을 것**
- `plugins/plate/skills/run/SKILL.md`의 "7. task 회고를 맡긴다", "8. 고칠 phase를 더한다", "멈춘다", "`RUNLOG.md`" 절 (phase 1이 고친 동작)
- `docs/TOOLS.md`의 "Claude Code" 절 (헤드리스 명령의 꼴, `--resume`, 허용 목록, phase 2가 더한 run 장면 A·B 절)

**TODO**
- [x] 장면 C: 복제본에 phase가 모두 통과하고 `retro.md`의 마지막 회고 절이 "문제 있음"이며 그 문제가 task 머리의 완료 조건을 좁혀야 고칠 수 있는 작은 tasks(`RUNLOG.md`에 `tasks 일괄`)를 차리고 run을 부른다. 새 `phase-M.md`가 생기지 않고 출력이 원인과 해결책을 보이고 묻고 멈춘 것을 본다. `--resume`으로 답한 뒤 `RUNLOG.md`의 마지막 물음 줄의 물은 자리가 `멈춤`인지 본다 (임시 폴더)
- [x] 장면 D: 새 복제본에 마지막 회고 절의 문제가 둘(README에 동작이 적힌 파일의 문제, 이미 `plan: NNN-slug 수정` 커밋으로 고친 문제)인 작은 tasks(`tasks 일괄`)를 차리고 run을 부른다. 새 `plan: NNN-slug 수정` 커밋의 `phase-M.md`를 `git show`로 읽어 앞의 문제의 TODO에 README 경로가 있고, 뒤의 문제는 TODO에 없고 통과 조건에 그 커밋 해시와 함께 있는지 본다 (임시 폴더)
- [x] 결과가 run 본문의 결함을 보이면 `plugins/plate/skills/run/SKILL.md`를 고치고, 장면 C·D와 함께 장면 A(phase 하나가 남은 작은 tasks를 `--permission-mode plan`으로 부르면 에이전트 줄 없이 plan 모드를 알리며 묻고 멈춘다)와 장면 B(phase가 모두 통과하고 회고가 없는 작은 tasks를 tasks 일괄로 부르면 회고 커밋 뒤와 하네스 eval 커밋 뒤에 `RUNLOG.md`만 바꾼 커밋이 있고 "고칠지"에서 `git status --short`가 비었다)를 새 복제본에서 다시 돌고 phase 2의 절 아래에 다시 돈 결과를 더한다 (`plugins/plate/skills/run/SKILL.md`, `docs/TOOLS.md`)
- [x] `docs/TOOLS.md`의 run 장면 A·B 절 뒤에 장면 C·D 절이 더해진다. task 머리의 결정에 적힌 필드를 장면마다 적는다 (`docs/TOOLS.md`)

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건 1~3의 확인을 모두 돌린다. 완료 조건 3의 장면 A~D는 그 조건에 적힌 기대로 본다

## 한 일
- 장면 C: 복제본(`/var/folders/0j/cj37rxmj1mj73vhflqpgsxm00000gn/T/tmp.FkgMLe4FQ2/repo`)에 완료 조건 1·2가 서로 어긋나 회고 1이 "완료 조건 2를 빼거나 1을 좁혀야 한다"는 문제를 낸 `scene-c`(`tasks 일괄`)를 차리고 `/plate:run`을 불렀다. Agent 호출 0, 새 `phase-2.md` 없음, HEAD 그대로, 원인(회고 1의 문제)과 해결책 하나를 보이고 "이 해결책으로 갈까요?"로 묻고 멈췄다. `--resume`으로 "그 해결책으로 가자"를 답하자 `RUNLOG.md`의 마지막 줄이 `- 물음 | 멈춤 | \`001-hello\` | … | 답: 그 해결책으로 간다`였고, 계획 고칠 안을 보이고 다시 묻고 멈췄다 (임시 폴더)
- 장면 D: 새 복제본(`/var/folders/0j/cj37rxmj1mj73vhflqpgsxm00000gn/T/tmp.6XaFYFkXGv/repo`)에 회고 1의 문제가 둘(`bin/greet.sh`가 이름을 붙이지 않는다, task 머리 결정의 경로가 틀렸다)이고 뒤의 것을 `2813e4a plan: 001-greet 수정`으로 고친 `scene-d`(`tasks 일괄`)를 차리고 `/plate:run`을 불렀다. run이 넣은 `6dd079b plan: 001-greet 수정`의 `phase-2.md`를 `git show`로 읽어, 문제 1의 TODO 파일 목록이 `bin/greet.sh`, `README.md`이고 README의 그 줄을 맞추라고 적었으며, 문제 2는 TODO에 없고 통과 조건에 "회고 1의 문제 2는 계획 커밋 `2813e4a`로 고쳤다."와 확인으로 있는 것을 봤다. 커밋을 본 뒤 run 프로세스를 끝냈다 (임시 폴더)
- 결과가 run 본문의 결함을 보이면 고치고 장면 A~D를 다시 돈다: 장면 C·D 모두 기대와 같았고 run 본문의 결함은 나오지 않아 `plugins/plate/skills/run/SKILL.md`를 고치지 않았고 장면 A·B도 다시 돌지 않았다 (바꾼 파일 없음)
- `docs/TOOLS.md`의 run 장면 A·B 절 뒤에 "고친 run을 장면 C·D로 돌려 본 것" 절을 더했다. 장면마다 Claude Code 버전, 복제본의 main 커밋, 돌린 시각, 세션 id, 차린 tasks의 꼴, 기대한 결과, 본 결과, 걸린 시간, 막힌 명령, 임시 폴더의 기록 경로(지워질 수 있다고 밝힘)를 적었다 (`docs/TOOLS.md`)

## 확인 결과
- task 머리의 완료 조건이 모두 참이다.
  - 완료 조건 1: run 본문의 "1. 시작 조건을 본다"(권한 물음과 확인할 수 없을 때 잇기, 65~68행), "7. task 회고를 맡긴다"(`NNN-slug: RUNLOG` 커밋, 167행), "8. 고칠 phase를 더한다"(계획을 바꾸게 하면 멈춤과 `멈춤`, 174행. README·맥락 문서 줄과 계획 커밋 해시, 181~182행), "멈춘다"(259행), "코드 평가를 맡긴다"(292행)와 "하네스 eval을 맡긴다"(302행), "`RUNLOG.md`"(501·512·514행, `모름`)를 읽어 다섯 해결이 저마다 있다. `python3 -m unittest discover -s tests` → `Ran 129 tests`, `OK`. `claude plugin validate .` → `✔ Validation passed`. 통과
  - 완료 조건 2: `docs/PRD.md` 17행(핵심 기능 7), `docs/ARCHITECTURE.md` 52행(run 문단), "데이터 흐름"의 실행 갈래(권한 물음, 회고가 계획을 바꾸게 하면 멈춤, `RUNLOG.md` 커밋)와 그 아래 멈추는 자리 문단, `README.md`의 `run` 행, run 본문 description을 읽어 시작할 때의 권한 물음, `RUNLOG.md`의 커밋 자리, 회고가 계획을 바꾸게 할 때 멈추는 것과 어긋나는 줄이 없다. 통과
  - 완료 조건 3: `docs/TOOLS.md`의 "고친 run을 장면 A·B로 돌려 본 것"과 "고친 run을 장면 C·D로 돌려 본 것"을 읽어 장면 A~D마다 버전(2.1.311), 돌린 시각, 세션 id, 기대한 결과, 본 결과가 있고 본 결과가 기대와 같다. 돌린 시각(A 18:40:01, B 18:44:23, C 19:30:40, D 19:32:30, 모두 2026-10-27 +09:00)이 `git log -1 --format=%cI -- plugins/plate/skills/run/SKILL.md` → `2026-10-27T18:38:03+09:00`보다 늦다. #35는 task 머리의 "돌리지 않음"대로 장면을 두지 않았다. 통과

## 계획과 달라진 점
- 장면 D는 run이 `plan: 001-greet 수정` 커밋을 넣은 뒤 프로세스를 끝냈다. TODO가 보라는 것은 그 커밋의 `phase-M.md`뿐이고, 그 뒤의 수행·확인·회고·평가는 장면의 대상이 아닌데 장면 B처럼 40분 넘게 걸릴 수 있어서다.
- 장면의 작은 tasks는 run이 만들 꼴의 커밋(phase 수행·확인·통과, 회고, `RUNLOG`)을 손으로 넣어 차렸다. 복제본을 만든 뒤 `git remote set-head origin main`을 더했다(장면 B에서 본 `origin/HEAD` 문제를 피하려고).

## 남은 것
- 장면 C는 계획 고칠 안의 승인 뒤(계획 커밋, TODO 없는 고칠 phase)를 돌리지 않았다. 완료 조건 3이 보는 것은 멈추고 묻는 데까지와 `멈춤` 줄이다.
- 장면 D에서 K가 1일 때 고칠 phase의 읽을 것이 "`## 회고 1`부터 `## 회고 1`까지의 절"로 나온다. run 양식대로이고 동작에 걸리지 않아 고치지 않았다.
- 헤드리스 run은 8번이 적은 명령 치환(`$(git log -1 --format=%h -- …retro.md)`)이 막혀 나눠 불렀다. 결과는 같았다.

## 하네스에서 걸린 것
- run 8번이 계획 커밋을 찾는 명령으로 적은 `git log … $(git log -1 …)..HEAD` 꼴은 헤드리스 Claude Code에서 "A nested command in this command can't be checked before it runs"로 막힌다. run 메인은 커밋 해시를 따로 얻어 다시 불렀다.

## 확인 1

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 완료 조건 1: `plugins/plate/skills/run/SKILL.md`의 "1. 시작 조건을 본다"(첫 에이전트 전 권한 확인, plan 모드나 쓰기가 막힐 모드면 알리고 묻고 멈춤, 확인할 수 없으면 보고에 적고 잇기), "7. task 회고를 맡긴다"(돌아오면 `RUNLOG.md`만 `NNN-slug: RUNLOG`로 커밋), "8. 고칠 phase를 더한다"(계획의 목표·완료 조건을 바꾸거나 좁혀야 하면 고칠 phase 없이 "멈춘다", 물은 자리 `멈춤`; 맥락 문서·README 줄을 TODO에; 계획 커밋으로 고친 문제는 TODO에 넣지 않고 통과 조건에 해시와 함께), "멈춘다"(다섯째 자리), "코드 평가를 맡긴다"·"하네스 eval을 맡긴다"(`<tasks 이름>: RUNLOG` 커밋), "`RUNLOG.md`"(단위 없는 `모름`, `권한`·`멈춤` 자리)를 읽음 → 다섯 해결이 저마다 있다. `python3 -m unittest discover -s tests` → `Ran 129 tests`, 마지막 줄 `OK`. `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
  - 완료 조건 2: `docs/PRD.md` 17행(핵심 기능 7), `docs/ARCHITECTURE.md` 52행(run 문단), "데이터 흐름"의 실행 갈래(권한 물음, 계획을 바꾸게 하면 멈춤, `RUNLOG.md` 그 자리 커밋)와 그 아래 멈추는 자리 문단, `README.md` 10행 `run` 행, run 본문 description을 읽음 → 시작할 때의 권한 물음, `RUNLOG.md`의 커밋 자리, 회고가 계획을 바꾸게 할 때 멈추는 것과 어긋나는 줄이 없다. 통과
  - 완료 조건 3: `docs/TOOLS.md`의 "고친 run을 장면 A·B로 돌려 본 것"(272행~)과 "고친 run을 장면 C·D로 돌려 본 것"(288행~)을 읽음 → 장면 A~D마다 버전 2.1.311, 돌린 시각, 세션 id, 기대한 결과, 본 결과가 있다. A: Agent 0, `RUNLOG.md` 없음, plan 모드를 알리고 "plan 모드를 끄고 이어 갈까요?"로 멈춤. B: 회고·코드 평가·하네스 eval 커밋 뒤에 `RUNLOG.md`만 바꾼 커밋이 저마다 있고 "고칠지"에서 `git status --short`가 빔. C: 새 `phase-2.md` 없음, 원인과 해결책을 보이고 묻고 멈춤, 답한 뒤 마지막 물음 줄이 `멈춤`. D: `6dd079b plan: 001-greet 수정`의 `phase-2.md`가 문제 1의 TODO에 `README.md`를 두고 문제 2는 TODO에 없고 통과 조건에 `2813e4a`와 함께 있음. 모두 기대와 같다. 통과
  - 완료 조건 3의 시각: `git log -1 --format=%cI -- plugins/plate/skills/run/SKILL.md` → `2026-10-27T18:38:03+09:00`. 장면 시각 A 18:40:01, B 18:44:23, C 19:30:40, D 19:32:30(모두 2026-10-27 +09:00)이 모두 늦다. #35는 task 머리의 `돌리지 않음` 줄대로 장면이 없다. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 129 tests`, `OK`. 통과

**남은 것**
- 장면 C는 계획 고칠 안의 승인 뒤(계획 커밋, TODO 없는 고칠 phase)를 돌리지 않았다 → 완료 조건 3의 장면 C가 보는 것은 멈추고 묻는 데까지와 `멈춤` 줄이라 통과 조건이 보는 동작에 걸리지 않는다. 하네스에서 걸린 것
- 장면 D에서 K가 1일 때 고칠 phase의 읽을 것이 "`## 회고 1`부터 `## 회고 1`까지의 절"로 나온다 → 완료 조건 3의 장면 D가 보는 TODO와 통과 조건에 걸리지 않는다. 하네스에서 걸린 것
- 헤드리스 run은 8번이 적은 명령 치환이 막혀 나눠 불렀다 → 장면 D의 결과(`phase-M.md`의 TODO와 통과 조건)는 기대와 같아 통과 조건이 보는 동작에 걸리지 않는다. 하네스에서 걸린 것

**실패**
- 없음

**하네스에서 걸린 것**
- 남은 것: 장면 C의 계획 고칠 안 승인 뒤(계획 커밋, TODO 없는 고칠 phase)는 돌려 보지 않았다.
- 남은 것: 고칠 phase 양식에서 K가 1이면 읽을 것이 "`## 회고 1`부터 `## 회고 1`까지의 절"로 어색하게 나온다(run 8번 양식).
- 남은 것: run 8번이 계획 커밋을 찾는 명령으로 적은 `$(git log -1 …)` 명령 치환 꼴은 헤드리스 Claude Code에서 승인 요구로 막혀 나눠 불러야 한다.

**판정**: 통과
