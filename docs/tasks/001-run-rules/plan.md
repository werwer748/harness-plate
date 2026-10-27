# run의 이슈 다섯을 고치고 장면으로 돌려 본다

## 목표
run의 #34, #35, #38, #40, #44가 고쳐지고, 맥락 문서와 README가 고친 동작에 맞춰지며, 고친 동작을 임시 복제본의 네 장면으로 돌린 결과가 `docs/TOOLS.md`에 남는다.

## 범위 밖
- run이 앞 phase의 "계획과 달라진 점"을 다음 phase 에이전트에게 넘기는 것
- plan, phase, check, retro, review, eval, cleanup의 본문
- 버전을 올리는 것과 테스트를 더하는 것. `004-tests-version`이 한다

## 완료 조건
1. `plugins/plate/skills/run/SKILL.md`에 다섯 이슈의 해결이 적혀 있다: #40(첫 에이전트를 띄우기 전에 plan 모드나 쓰기가 막힐 권한 모드를 알리고 바꿀지 묻고, 확인할 수 없으면 그렇다고 적고 잇는다), #44(회고 에이전트와 코드 평가·하네스 eval 에이전트가 돌아와 더한 `RUNLOG.md` 줄을 그 자리에서 그 파일만 넣는 커밋으로 넣는다), #35(돌아오지 않은 값은 단위 없이 `모름`), #34·#38(회고의 문제를 고치려면 계획 파일의 목표나 완료 조건을 바꾸거나 좁혀야 하면 고칠 phase를 더하지 않고 어느 실행 방식이든 "멈춘다"로 가고 물은 자리는 `멈춤`), #38(고칠 phase의 TODO에 고칠 동작을 적은 맥락 문서와 README의 줄이 들고, 계획 커밋으로 이미 고친 문제는 TODO에 넣지 않고 통과 조건에 그 커밋의 해시와 함께 따로 적는다)
   - 확인: run 본문의 "1. 시작 조건을 본다", "7. task 회고를 맡긴다", "8. 고칠 phase를 더한다", "멈춘다", "tasks 끝"의 "코드 평가를 맡긴다"와 "하네스 eval을 맡긴다", "`RUNLOG.md`" 절을 읽어 다섯 해결이 저마다 적혀 있다. 하나라도 없으면 실패
   - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`, `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
2. 맥락 문서와 README가 1의 동작과 맞는다.
   - 확인: `docs/PRD.md`의 핵심 기능 7, `docs/ARCHITECTURE.md`의 "패턴과 규칙"의 run 문단과 "데이터 흐름"의 실행 갈래와 그 아래 멈추는 자리 문단, `README.md`의 `run` 행, run 본문 앞머리의 description을 저마다 읽어, 시작할 때의 권한 물음, `RUNLOG.md`의 커밋 자리, 회고가 계획을 바꾸게 할 때 멈추는 것과 어긋나는 줄이 없다. 하나라도 있으면 실패
3. 고친 동작을 네 장면으로 돌린 결과가 `docs/TOOLS.md`에 있고, 저마다 기대대로다.
   - 확인: `docs/TOOLS.md`의 "Claude Code" 절에 더해진 run 장면 절(phase 2의 것, phase 3의 것)을 읽어, 장면 A~D마다 Claude Code 버전, 돌린 시각, 세션 id, 기대한 결과와 본 결과가 있고 본 결과가 기대와 같다. 하나라도 없거나 다르면 실패
     - 장면 A(#40): plan 모드(`--permission-mode plan`)로 run을 부르면, 띄운 에이전트가 없고(`RUNLOG.md`에 에이전트 줄이 없다) 출력이 plan 모드를 알리며 바꿀지 묻고 멈춘다
     - 장면 B(#44): phase가 모두 통과하고 회고가 없는 작은 tasks를 tasks 일괄로 돌리면, 회고 커밋 뒤와 하네스 eval 커밋 뒤에 `RUNLOG.md`만 바꾼 커밋이 저마다 있고, "고칠지"를 묻고 멈춘 자리에서 `git status --short`가 비었다
     - 장면 C(#34, #38): 마지막 회고 절의 문제가 task 머리의 완료 조건을 좁혀야 고칠 수 있는 작은 tasks를 tasks 일괄로 돌리면, 새 `phase-M.md`가 생기지 않고 출력이 원인과 해결책을 보이고 묻고 멈춘다. 답한 뒤 `RUNLOG.md`의 마지막 물음 줄의 물은 자리가 `멈춤`이다
     - 장면 D(#38): 마지막 회고 절의 문제가 둘(하나는 README에 동작이 적힌 파일의 문제, 하나는 이미 `plan: NNN-slug 수정` 커밋으로 고친 문제)인 작은 tasks를 tasks 일괄로 돌리면, `plan: NNN-slug 수정` 커밋의 `phase-M.md`가 앞의 문제의 TODO에 README 경로를 두고, 뒤의 문제는 TODO에 없고 통과 조건에 그 커밋 해시와 함께 있다
   - 확인: 그 절들의 돌린 시각이 모두 `git log -1 --format=%cI -- plugins/plate/skills/run/SKILL.md`보다 늦다
   - 돌리지 않음: #35는 에이전트의 사용량이 돌아오지 않는 경우를 장면으로 만들 수 없다

## 결정
- 장면은 `mktemp -d`에 이 저장소의 main을 복제한 곳에서 작업 트리의 `plugins/plate`를 `--plugin-dir`로 실어 헤드리스(`claude -p`, 물음에는 `--resume <세션 id>`로 답한다)로 돌린다. 장면의 작은 tasks는 그 복제본에 장면마다 새로 차리고, git 원격이 필요하면 `git clone --bare`로 채워 푸시하지 않는다. 허용 목록은 `docs/TOOLS.md`의 "스킬을 헤드리스로 돌려 볼 때의 허용 목록"을 쓴다. 이유: tasks 머리의 결정
- 장면 절은 장면마다 Claude Code 버전, 복제본의 main 커밋, 돌린 시각, 세션 id, 차린 tasks의 꼴, 기대한 결과, 본 결과, 걸린 시간, 막힌 명령을 적고, 임시 폴더의 기록 경로도 적되 지워질 수 있다고 밝힌다. 이유: tasks 완료 조건 1의 확인이 이 필드를 본다
- `RUNLOG.md`의 새 커밋 메시지는 회고 뒤가 `NNN-slug: RUNLOG`, 코드 평가와 하네스 eval 뒤가 `<tasks 이름>: RUNLOG`다 (추천안으로 정함)
- 시작할 때의 권한 물음의 물은 자리는 `권한`이고 task 이름 자리는 "없음"이다 (추천안으로 정함)
