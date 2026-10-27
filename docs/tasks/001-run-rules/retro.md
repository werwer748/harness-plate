# 회고

## 회고 1

**확인**
- 1. `plugins/plate/skills/run/SKILL.md`에 다섯 이슈의 해결이 적혀 있다
  - run 본문의 "1. 시작 조건을 본다"(62~68행), "7. task 회고를 맡긴다"(167행), "8. 고칠 phase를 더한다"(174·181·182행, 양식 212~218행), "멈춘다"(259·268행), "코드 평가를 맡긴다"(292행), "하네스 eval을 맡긴다"(302행), "`RUNLOG.md`"(501·512·514·515행)를 읽음 → #40(첫 에이전트 전 권한 확인, 확인할 수 없으면 보고에 적고 잇는다), #44(회고 뒤 `NNN-slug: RUNLOG`, 평가 뒤 `<tasks 이름>: RUNLOG`로 `RUNLOG.md`만 커밋), #35(단위 없는 `모름`), #34·#38(계획의 목표나 완료 조건을 바꾸거나 좁혀야 하면 어느 방식이든 "멈춘다", 물은 자리 `멈춤`), #38(맥락 문서·README 줄을 TODO에, 계획 커밋으로 고친 문제는 통과 조건에 해시와 함께)이 저마다 있다. 통과
  - `python3 -m unittest discover -s tests` → `Ran 129 tests in 15.951s` / `OK`. `claude plugin validate .` → `✔ Validation passed`. 통과
- 2. 맥락 문서와 README가 1의 동작과 맞는다
  - `docs/PRD.md` 핵심 기능 7, `docs/ARCHITECTURE.md` "패턴과 규칙"의 새 run 문단(52행)과 기본 브랜치 문단, "데이터 흐름"의 실행 갈래와 그 아래 멈추는 자리 문단, `README.md`의 `run` 행, run 본문 description을 읽음 → 시작할 때의 권한 물음, `RUNLOG.md`의 커밋 자리, 회고가 계획을 바꾸게 할 때 멈추는 것을 모두 담고 어긋나는 줄이 없다. 통과
- 3. 네 장면의 결과가 `docs/TOOLS.md`에 있고 기대대로다
  - `docs/TOOLS.md`의 "고친 run을 장면 A·B로 돌려 본 것"과 "고친 run을 장면 C·D로 돌려 본 것"을 읽음 → 장면 A~D마다 버전 2.1.311, 돌린 시각, 세션 id(`75d5f20c-…`, `02367cb0-…`, `515d9b64-…`, `6b7d5d04-…`), 기대한 결과, 본 결과가 있고 본 결과가 기대와 같다(A: Agent 0, `RUNLOG.md` 없음, plan 모드를 알리고 묻고 멈춤. B: 회고·코드 평가·하네스 eval 커밋 뒤에 `RUNLOG.md`만 바꾼 커밋, `git status --short` 빔. C: 새 `phase-2.md` 없음, 원인과 해결책을 보이고 멈춤, 답한 뒤 마지막 물음 줄이 `멈춤`. D: `6dd079b`의 `phase-2.md`가 문제 1의 TODO에 `README.md`, 문제 2는 통과 조건에 `2813e4a`와 함께). 통과
  - `git log -1 --format=%cI -- plugins/plate/skills/run/SKILL.md` → `2026-10-27T18:38:03+09:00`. 장면 시각 A 18:40:01, B 18:44:23, C 19:30:40, D 19:32:30(모두 2026-10-27 +09:00)이 늦다. 통과
  - 돌리지 않음: #35는 task 머리의 `돌리지 않음` 줄대로 장면이 없다
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 129 tests` / `OK`. 통과

**남은 것**
- phase 1: 고친 동작은 글로만 맞췄고 돌려 보지 않았다 → 문제 아님 (phase 2, 3의 장면 A~D가 돌렸고 기대대로다)
- phase 1: 권한 확인은 세션이 지금 모드나 막힐 경로를 모르면 묻지 않고 지나간다 → 문제 아님 (완료 조건 1이 "확인할 수 없으면 그렇다고 적고 잇는다"로 정한 동작 그대로다)
- phase 1: 계획 커밋을 찾는 명령이 `retro.md`를 마지막으로 바꾼 커밋을 기준으로 해 회고 절 뒤 다른 커밋이 `retro.md`를 바꾸면 어긋날 수 있다 → 문제 아님 (run 본문의 "멈춘다" 4와 8번의 길은 `retro.md`를 건드리지 않고, `retro.md`를 쓰는 것은 회고뿐이라 회고 절 뒤에 `retro.md`를 바꾸는 커밋이 없다)
- phase 2: 장면 B의 복제본 `origin/HEAD`가 `tasks/release-prep`을 가리켜 run과 코드 평가의 `git merge-base`가 실패하고 원격 추적 ref로 돌아갔다 → 문제 아님 (장면 차림에서 온 것이고, review·run이 로컬 기본 브랜치가 없을 때의 길은 task 머리의 범위 밖인 다른 스킬 본문과 이 task가 고치지 않은 run 절에 걸린다)
- phase 2: 헤드리스 acceptEdits 세션에서 plan 모드 밖의 "쓰기가 막힐 모드" 갈래는 돌려 보지 않았다 → 문제 아님 (완료 조건 3의 장면 A는 plan 모드 갈래만 정했다. 이 tasks의 실제 실행에서 auto mode를 알리고 물은 `권한` 줄이 `docs/tasks/RUNLOG.md`에 있다)
- phase 2: `;`·`&&`·`for`·명령 치환으로 이은 Bash 6개가 승인 요구로 막혔다 → 문제 아님 (도구의 허용 목록 꼴이고 `docs/TOOLS.md`에 이미 적힌 사실이다. 장면 결과에 걸리지 않았다)
- phase 3: 장면 C는 계획 고칠 안의 승인 뒤(계획 커밋, TODO 없는 고칠 phase)를 돌리지 않았다 → 문제 아님 (완료 조건 3의 장면 C는 멈추고 묻는 데까지와 `멈춤` 줄을 본다. run 본문 268행은 그 뒤 8번에서 "남은 문제"만 고칠 phase로 더하고 계획 커밋으로 고친 문제는 통과 조건에 따로 적는다고 읽힌다)
- phase 3: K가 1일 때 고칠 phase의 읽을 것이 "`## 회고 1`부터 `## 회고 1`까지의 절"로 나온다 → 문제 아님 (양식의 글꼴이고 동작이 틀리지 않는다)
- phase 3: 8번의 명령 치환이 헤드리스에서 막혀 나눠 불렀다 → 문제 아님 (장면 D의 결과가 기대와 같다. 하네스의 걸림으로 `FRICTION.md`에 적는다)

**문제**
- run 본문이 #35를 고치며 `docs/TOOLS.md`에 적은 까닭을 "다음 `RUNLOG.md` 커밋에 함께 넣는다"(512행)고 했는데, 그 커밋 자리는 모두 다른 파일을 막는다: 회고·코드 평가·하네스 eval 뒤는 "`RUNLOG.md`만 한 커밋"(167·292·302·501행), phase 통과는 "이 변경과 `RUNLOG.md`만"(154행), 고칠 phase는 "그 파일과 `RUNLOG.md`만"(195행)이다. 어느 쪽을 따르든 한 글을 어기고, 커밋 자리의 글을 따르면 `docs/TOOLS.md`가 커밋되지 않은 채 남아 "고칠지"에서 작업 트리가 깨끗하다는 #44의 목표와 어긋난다 (`plugins/plate/skills/run/SKILL.md`). 기준: 결함

**판정**: 문제 있음

## 회고 2

**확인**
- 1. `plugins/plate/skills/run/SKILL.md`에 다섯 이슈의 해결이 적혀 있다
  - run 본문의 "1. 시작 조건을 본다", "7. task 회고를 맡긴다", "8. 고칠 phase를 더한다", "멈춘다", "코드 평가를 맡긴다", "하네스 eval을 맡긴다", "`RUNLOG.md`" 절을 `git diff dfb0852 HEAD -- plugins/plate/skills/run/SKILL.md`와 함께 읽음 → 회고 1에서 본 다섯 해결(#40 권한 물음과 확인할 수 없을 때 잇기, #44 회고 뒤 `NNN-slug: RUNLOG`·평가 뒤 `<tasks 이름>: RUNLOG` 커밋, #35 단위 없는 `모름`, #34·#38 계획의 목표나 완료 조건을 바꾸게 하면 어느 방식이든 "멈춘다"와 물은 자리 `멈춤`, #38 TODO의 맥락 문서·README 줄과 계획 커밋 해시를 적은 통과 조건)이 그대로 있고, phase 4는 커밋 자리마다 `docs/TOOLS.md`를 넣는 괄호와 10번의 보고 앞 커밋 문단만 더했다. 통과
  - `python3 -m unittest discover -s tests` → `Ran 129 tests in 16.271s` / `OK`. `claude plugin validate .` → `✔ Validation passed`. 통과
- 2. 맥락 문서와 README가 1의 동작과 맞는다
  - `docs/PRD.md` 핵심 기능 7, `docs/ARCHITECTURE.md` "패턴과 규칙"의 run 문단과 "데이터 흐름"의 실행 갈래, `README.md`의 `run` 행, run 본문 description을 읽음(`git diff 77018b6 HEAD`로 phase 4의 바뀐 줄도 봄) → 시작할 때의 권한 물음, `RUNLOG.md`의 커밋 자리(사용량 까닭을 적은 `docs/TOOLS.md`를 함께 넣는 것과 보고 앞 커밋 포함), 회고가 계획을 바꾸게 할 때 멈추는 것을 담고 어긋나는 줄이 없다. 통과
- 3. 네 장면의 결과가 `docs/TOOLS.md`에 있고 기대대로다
  - `docs/TOOLS.md` 272~315행의 장면 A·B 절과 장면 C·D 절을 읽음 → 장면 A(18:40:01, `75d5f20c-…`), C(19:30:40, `515d9b64-…`), D(19:32:30, `6b7d5d04-…`)는 버전, 시각, 세션 id, 기대한 결과, 본 결과가 있고 기대와 같다. 장면 B의 마지막 항목(Claude Code 2.1.311, 2026-10-27T20:43:55+09:00, 세션 id `8d673fe3-99ee-4f55-8117-e254cdf261ee`)은 회고·코드 평가·하네스 eval 뒤에 `RUNLOG.md`만 바꾼 커밋(`ae7c965`, `4a25b42`, `5def566`)이 있고 "고칠 안대로 할까요?"로 묻고 멈춘 자리의 `git status --short`가 비어 기대와 같다. 통과
  - `git hash-object plugins/plate/skills/run/SKILL.md` → `6fb11a43b9f522cbaf0686c4ccbe098bd43036e0`, `git rev-parse HEAD:plugins/plate/skills/run/SKILL.md` → `6fb11a43b9f522cbaf0686c4ccbe098bd43036e0`로 마지막 장면 B 항목의 해시와 같다. `git log -1 --format=%cI dfb0852` → `2026-10-27T18:38:03+09:00`이고 장면 A 18:40:01, C 19:30:40, D 19:32:30이 늦다. `git diff dfb0852 HEAD -- plugins/plate/skills/run/SKILL.md` → 바뀐 글은 6·7·8번, "멈춘다" 4, 코드 평가·하네스 eval 뒤, "비운다" 1의 커밋 글에 붙은 `docs/TOOLS.md` 괄호, 10번의 보고 앞 커밋 문단, "`RUNLOG.md`" 절의 커밋 자리 글과 사용량 줄의 괄호뿐이고 모두 `docs/TOOLS.md`를 커밋 자리에 넣는 글이다. 통과
  - 돌리지 않음: #35는 task 머리의 `돌리지 않음` 줄대로 장면이 없다
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 129 tests in 16.271s` / `OK`. 통과

**남은 것**
- phase 4: 사용량이 돌아오지 않아 `docs/TOOLS.md`에 까닭을 적고 `RUNLOG.md`와 함께 커밋하는 길(10번의 보고 앞 커밋도 든다)은 장면에서 돌지 않았다 → 문제 아님 (task 머리의 `돌리지 않음` 줄이 #35를 돌리지 않기로 정했고, run 본문을 읽어 커밋 없이 10번으로 오는 길(8번·"멈춘다"의 승인받지 못함, "멈춘다" 4의 멈추기로 함)이 모두 10번 첫 문단의 커밋을 지난다)
- phase 4: 한계: `docs/TOOLS.md` 없이 "멈춘다"에서 멈추기로 하면 `RUNLOG.md`의 물음 줄이 커밋되지 않은 채 남는다 → 문제 아님 (#44의 해결로 정한 경계는 회고·코드 평가·하네스 eval 에이전트 뒤의 커밋과 "고칠지"에서 멈춘 자리이고, "멈춘다"의 물음 줄은 이 task 전부터의 동작이다. `FRICTION.md`에 경계 밖으로 적는다)
- phase 4: 장면의 허용 목록에 `"Bash(git remote:*)" "Bash(git rm:*)"`가 없어 run의 "비운다"가 막혔다 → 문제 아님 (장면 B가 보는 커밋 자리와 "고칠지"는 "비운다" 앞이고, 장면 차림의 허용 목록에서 온 것이다)
- phase 1~3의 줄은 회고 1에서 판정했고 그 뒤 바뀐 것이 없다

**문제**
- 없음

**판정**: 통과
