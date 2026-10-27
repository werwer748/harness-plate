# retro, eval과 다섯 스킬의 이슈 셋을 고치고 장면으로 돌린다

## 목표
retro 본문의 #49, eval과 retro 본문의 #50, phase·check·retro·review·eval 본문의 #51(끝 보고의 갈래)을 고치고, 그 규칙 글이 빠지면 실패하는 테스트를 더하고, 버전을 0.18.0으로 올린다. 그다음 고친 retro, eval, phase를 임시 복제본에서 네 장면으로 돌려 `docs/TOOLS.md`에 남긴다.

## 범위 밖
- run과 plan 본문을 고치는 것(001, 002의 일)
- 다섯 스킬의 description을 고치는 것
- 장면을 이 저장소에서 돌리는 것. 장면은 모두 `mktemp -d`의 복제본에서 돌린다

## 완료 조건
1. retro와 eval의 #49, #50이 고쳐졌다
   - 확인: `plugins/plate/skills/retro/SKILL.md`의 "5. tasks 끝에 볼 것을 모은다"를 읽어, "문제" 갈래가 확인 절 "하네스에서 걸린 것"의 `남은 것:`으로 시작하는 줄을 이번 회고 절 "남은 것"에서 "문제"로 판정한 것만 모으고 "문제 아님"인 줄은 모으지 않는다는 글과, "멈춤" 갈래의 정해 둔 자리 목록에 `권한`이 있다. 하나라도 없으면 실패
   - 확인: `plugins/plate/skills/eval/SKILL.md`의 "3. 기준마다 근거를 적고 등급을 매긴다" 규칙 준수 표에 `NNN-slug: RUNLOG`와 `<tasks 이름>: RUNLOG` 행이 있고, 만든 스킬이 run, 넣어도 되는 파일이 `RUNLOG.md`와 사용량 까닭을 적은 `docs/TOOLS.md`다. 낱말 "정해 둔 물음"의 목록에 `권한`이 있다. 하나라도 없으면 실패
2. 다섯 스킬의 #51이 고쳐졌다
   - 확인: `plugins/plate/skills/phase/SKILL.md`의 "6. 다섯 줄을 돌려준다", `check/SKILL.md`의 "8. 세 줄을 돌려준다", `retro/SKILL.md`의 "9. 세 줄을 돌려준다", `review/SKILL.md`의 끝 보고 절(네 줄을 돌려주는 절), `eval/SKILL.md`의 "8. 세 줄을 돌려준다"를 저마다 읽어, 사용자가 직접 부른 꼴의 보고(목록이나 run 안내를 더한다)가 맡은 글에 `부른 쪽: plate:run` 줄도 작업 트리의 스킬 줄도 없을 때만이라고 적혀 있다. 다섯 가운데 하나라도 없으면 실패
3. 1과 2의 규칙마다 글이 빠지면 실패하는 테스트가 `tests/test_skill_rules.py`에 있고, 이 task의 마지막 커밋에서 모든 테스트(001, 002가 더한 것도)가 통과한다
   - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
   - 확인: `mktemp -d`에 `git archive HEAD`를 풀어 retro 5번의 #49 해결 글을 지우고 돌리면 실패한다. 다시 풀어 review 끝 보고 절에서 `부른 쪽: plate:run`을 지우고 돌리면 실패한다
4. 고친 retro, eval, phase를 네 장면으로 돌린 결과가 `docs/TOOLS.md`에 있고 저마다 기대와 같다(tasks 완료 조건 3)
   - 확인: `docs/TOOLS.md`의 이번 장면 절을 읽어 장면 R, E, P1, P2마다 Claude Code 버전, 돌린 시각, 세션 id, 돌릴 때의 대상 본문 해시(`git hash-object`), 차림, 기대한 결과, 본 결과, 막힌 명령이 있고, 본 결과가 기대와 같다. 장면의 차림과 기대는 아래 결정의 것이다. 하나라도 빠지거나 다르면 실패
   - 확인: 장면 절마다 적힌 본문 해시가 `git rev-parse HEAD:plugins/plate/skills/<retro|eval|phase>/SKILL.md`와 같다
   - 확인: 장면 절에 적힌, 장면을 돌리기 전과 뒤의 원본 `git rev-parse HEAD`가 같고 `git status --short`의 출력이 같다
5. 버전이 0.18.0이고 마켓플레이스가 유효하고, 이 task의 마지막 커밋에서 tasks 완료 조건 5가 참이다
   - 확인: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json`의 두 줄이 모두 `0.18.0`
   - 확인: `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
   - 확인: `docs/PRD.md`의 5와 7, `docs/ARCHITECTURE.md` "패턴과 규칙"의 맡기는 글 문단과 run 문단, 데이터 흐름의 회고 줄, 디렉터리 구조의 `test_skill_rules.py` 줄, `README.md`의 `run`, `phase`, `check`, `retro`, `review`, `eval` 행을 문서마다 따로 읽는다. 견줄 것: 맡기는 글 문단이 다섯 스킬이 표지 줄이나 작업 트리의 스킬 줄로 run이 띄운 것을 가른다고 적는다. `test_skill_rules.py` 줄이 001(run), 002(plan), 이 task(retro #49, eval #50, 다섯 스킬 #51) 규칙을 모두 담는다. 001이 맞춘 run 줄(해시·시각 파일의 멈춤, 결정 줄, 표지 줄)이 그대로 있다. PRD 5와 데이터 흐름의 회고 줄, README의 다섯 행이 #49·#51과 어긋나지 않는다. 하나라도 어긋나면 실패

## 결정
- 표지는 둘이다: 001이 run의 맡기는 글 다섯의 마지막 줄로 더한 `부른 쪽: plate:run`(`plugins/plate/skills/run/SKILL.md`의 4번, 5번, 7번, "코드 평가를 맡긴다", "하네스 eval을 맡긴다" 코드 블록)과, run 낱말 "작업 트리의 스킬 줄"의 한 줄(`작업 트리의 {경로}를 읽어 그 절차를 따른다. 불러 온 스킬의 본문과 다르면 이 파일을 따른다.`). 이유: tasks 머리의 결정
- 장면의 공통 차림: 장면마다 `mktemp -d` 아래에 `git clone --branch main /Users/hugo/Desktop/harness-plate repo`로 복제하고, 곧바로 `git remote set-head origin main`을 한다. 플러그인은 `--plugin-dir /Users/hugo/Desktop/harness-plate/plugins/plate`, 명령은 `claude -p "<프롬프트>" --plugin-dir … --permission-mode bypassPermissions --output-format stream-json --verbose`로 프롬프트를 `-p` 바로 뒤에 둔다. 프롬프트에는 작업 트리의 스킬 줄을 붙이지 않는다(복제본의 스킬 본문은 고치기 전의 것이다). 돌리기 전과 뒤에 원본에서 `git rev-parse HEAD`와 `git status --short`를 적는다. 세션 기록은 `${CLAUDE_CONFIG_DIR:-~/.claude}/projects/` 아래에 있다. 네 장면은 폴더가 달라 함께 띄워도 된다. 이유: tasks 머리의 결정과 `docs/TOOLS.md`의 "스킬을 헤드리스로 돌려 볼 때의 허용 목록"의 "차림에서 지킬 것"
- 장면 R(#49, retro): 복제본에서 `git switch -c tasks/release-prep 44f2790^`, `git branch -f main 509b234`. 프롬프트는 run 7번의 맡기는 글에 task 폴더 `docs/tasks/002-plan-phase-rules`를 넣은 세 줄과 `부른 쪽: plate:run`이다. 기대: 새 `002-plan-phase-rules: 회고` 커밋이 `retro.md`와 `FRICTION.md`만 바꾼다. 새 `## 회고 1`의 "남은 것"에 "문제 아님"으로 판정한 줄이 하나 이상 있다. 그 커밋이 `FRICTION.md`에 더한 `문제` 줄 가운데 "문제 아님"으로 판정한 줄의 내용을 담은 것이 없다. 결과 줄의 `result`가 `판정:`으로 시작하는 세 줄이고 `plate:run`이 없다. 이유: 그 커밋의 확인 절에는 `남은 것:` 줄 다섯이 있고, 지난 회고는 모두 "문제 아님"으로 판정하고도 그 가운데 둘을 `FRICTION.md`의 `문제`로 넣었다(`44f2790`)
- 장면 E(#50, eval): 복제본에서 `git switch -c tasks/release-prep 7ea7eef`, `git branch -f main 509b234`. 프롬프트는 run "하네스 eval을 맡긴다"의 맡기는 글과 `부른 쪽: plate:run`이다. 기대: 새 `release-prep: 하네스 eval` 커밋이 `docs/tasks/eval.md`만 바꾼다. eval 절 규칙 준수의 근거가 `RUNLOG` 커밋 여섯(`77018b6`, `3562d24`, `735dbae`, `98e74a7`, `bb41212`, `7ea7eef`)을 표의 행으로 보고 "표에 없는 꼴"로 빼지 않는다. 사람 개입률의 근거가 `권한` 물은 줄을 정해 둔 물음으로 센다. "하네스에서 걸린 것"에 표에 `RUNLOG` 행이 없다거나 정해 둔 물음에 `권한`이 없다는 줄이 없다. 결과 줄의 `result`가 세 줄이고 `plate:run`이 없다. 이유: 그 기록의 지난 eval(`f080761`)이 이 둘을 "하네스에서 걸린 것"에 적었다
- 장면 P1, P2(#51, phase): 복제본 둘에서 `git switch -c tasks/scene-p`. 장면을 돌리는 수행이 아래 작은 tasks를 손으로 써서 `plan: scene-p` 한 커밋으로 넣는다. tasks 머리 `docs/tasks/plan.md`(이름 `scene-p`, task 목록 `001-hello`), task 머리 `docs/tasks/001-hello/plan.md`, `docs/tasks/001-hello/phase-1.md`(테스트 먼저 "아니오 — 글 파일 하나를 만든다", TODO "`hello.txt`에 `hi` 한 줄이 생긴다 (`hello.txt`)", 통과 조건 "`cat hello.txt`가 `hi`를 낸다"). P1의 프롬프트는 run 4번의 맡기는 글 세 줄(task 폴더 `docs/tasks/001-hello`, phase `1`)과 `부른 쪽: plate:run`이고, P2는 그 세 줄뿐이다. 기대: 두 장면 모두 `001-hello: phase 1` 커밋에 `hello.txt`와 `phase-1.md`가 든다. P1 결과 줄의 `result`는 `상태:`로 시작하는 다섯 줄뿐이고 `plate:run`이 없다. P2 결과 줄의 `result`에는 다섯 줄 아래에 `plate:run`을 부르면 이어진다는 글이 있다. 이유: 표지가 있을 때와 없을 때의 두 갈래를 저마다 돌린다
