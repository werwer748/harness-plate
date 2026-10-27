# 회고

## 회고 1

**확인**
- 1. retro와 eval의 #49, #50이 고쳐졌다
  - `plugins/plate/skills/retro/SKILL.md` "5. tasks 끝에 볼 것을 모은다"를 읽음 → "문제" 갈래에 `확인 절 "하네스에서 걸린 것"의 \`남은 것:\`으로 시작하는 줄은 이번 회고 절 "남은 것"에서 "문제"로 판정한 것만 모으고, "문제 아님"으로 판정한 줄은 모으지 않는다`가, "멈춤" 갈래의 정해 둔 자리 목록에 `(권한, 실행 방식, …)`이 있다. 통과
  - `plugins/plate/skills/eval/SKILL.md` 3번 규칙 준수 표와 낱말을 읽음 → `| \`NNN-slug: RUNLOG\` | run | \`RUNLOG.md\`와 사용량 까닭을 적은 \`docs/TOOLS.md\` |`와 `<tasks 이름>: RUNLOG` 행이 같은 꼴로 있고, 낱말 "정해 둔 물음"의 목록이 `` 모두(`권한`, `실행 방식`, … ``이다. 통과
- 2. 다섯 스킬의 #51이 고쳐졌다
  - phase 6번, check 8번, retro 9번, review 9번 "네 줄을 돌려준다"(끝 보고 절), eval 8번을 읽음 → 다섯 모두 "맡은 글에 `부른 쪽: plate:run` 줄도 작업 트리의 스킬 줄(`작업 트리의 {경로}를 읽어 그 절차를 따른다.`로 시작하는 줄)도 없을 때만 사용자가 직접 부른 것으로 보고, 그때는 …"이고, `grep -c '사용자가 직접 불렀으면'`이 다섯 파일 모두 0이다. 그 앞부분은 run 낱말 "작업 트리의 스킬 줄"의 한 줄(47줄)의 앞부분과 같다. 통과
- 3. 1과 2의 규칙마다 글이 빠지면 실패하는 테스트가 있고 모든 테스트가 통과한다
  - `python3 -m unittest discover -s tests` → `Ran 161 tests`, 마지막 줄 `OK`. 통과
  - `mktemp -d` 두 곳에 `git archive HEAD`(`a117ee9`)를 풀어 (a) retro 5번의 #49 해결 글("다만 확인 절 … 갈린다.")을 지우고, (b) review "9. 네 줄을 돌려준다" 절에서 `` `부른 쪽: plate:run` ``을 지우고 저마다 돌림 → (a) `FAIL: test_49_friction_problem_only_for_remaining_lines_judged_problem (test_skill_rules.RetroRulesTest)` / `FAILED (failures=1)`, (b) `FAIL: test_51_direct_report_only_without_marker (test_skill_rules.CallerMarkerTest) (skill='review')` / `FAILED (failures=1)`. 통과
- 4. 네 장면의 결과가 `docs/TOOLS.md`에 있고 기대와 같다
  - `docs/TOOLS.md`의 "고친 retro·eval·phase를 장면 R·E·P1·P2로 돌려 본 것" 절을 읽고, 복제본 넷(`/var/folders/0j/cj37rxmj1mj73vhflqpgsxm00000gn/T/tmp.{76H9C4jcJ7,VFG670zFa8,UsX54VhM8I,se95VXuvAu}`)의 `repo`에서 `git log --name-only -1`, `turn<장면>.jsonl` 결과 줄의 `session_id`·`permission_denials`·`result`, R의 `retro.md` 회고 1과 `84c1f06`이 `FRICTION.md`에 더한 줄, E의 `eval.md` 규칙 준수·사람 개입률·"하네스에서 걸린 것"을 직접 봄 → 장면마다 Claude Code 버전(2.1.311), 돌린 시각, 세션 id(결과 줄과 같음), 본문 해시, 차림, 기대, 본 결과, 막힌 명령(모두 빈 `permission_denials`)이 있다. R: `84c1f06`이 `retro.md`·`FRICTION.md`만, "남은 것" 여섯 줄 모두 "문제 아님", 더한 `문제` 여섯 줄에 그 내용이 없음, `result`는 `판정: 통과`부터 세 줄이고 `plate:run` 없음. E: `51e104b`가 `eval.md`만, 규칙 준수 근거가 `RUNLOG` 커밋을 표 안으로 보고 표에 없는 꼴은 `584ae16`뿐, 사람 개입률 근거 "권한 모드를 바꿀지 → 정해 둔 물음", "하네스에서 걸린 것"에 `RUNLOG` 행·`권한` 줄 없음, `result` 세 줄에 `plate:run` 없음. P1: `59610b8`에 `hello.txt`·`phase-1.md`, `result`는 `상태: 끝남`부터 다섯 줄뿐. P2: `4fd9c1b`에 같은 두 파일, `result` 다섯 줄 아래 "확인과 그 뒤의 일은 plate의 run 스킬(`plate:run`)을 부르면 이어집니다." 기대와 같다. 통과
  - `git rev-parse HEAD:plugins/plate/skills/{retro,eval,phase}/SKILL.md` → `f1d13ac4f304a38bfe77b35b176536fa77cb948c`, `9414c9dcbd63ee37bbec018f602f829688cdf404`, `69385efac7a60483bbe40db3ca573da7ca1d90b7`. 절에 적힌 해시와 같다. 통과
  - 절 머리를 읽음 → 전과 뒤의 `git rev-parse HEAD`가 모두 `34280136ff018c57e3fb17fdd4c03b973217604a`, `git status --short`가 모두 ` M docs/tasks/003-agent-rules/phase-2.md`. 같다. 통과
- 5. 버전이 0.18.0이고 마켓플레이스가 유효하고 tasks 완료 조건 5가 참이다
  - `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → `"version": "0.18.0",` 두 줄. 통과
  - `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
  - `docs/PRD.md` 5·7, `docs/ARCHITECTURE.md` 맡기는 글 문단(48줄)·run 문단(54줄)·데이터 흐름 회고 줄(69줄)·`test_skill_rules.py` 줄(39줄), `README.md`의 run·phase·check·retro·review·eval 행을 따로 읽음 → 맡기는 글 문단이 다섯 스킬이 표지 줄이나 작업 트리의 스킬 줄로 run이 띄운 것을 가른다고 적고 표지 줄 글이 남아 있다. `test_skill_rules.py` 줄이 001(시작 권한 물음, RUNLOG 커밋 자리, 표지 줄 등), 002(갈래마다 확인, 본문 해시, 초안 점검 등), 이 task(retro #49, eval #50, 다섯 스킬 #51)를 담는다. run 문단에 시각·해시 파일의 멈춤, 결정 줄, 맡기는 글 문단에 표지 줄이 그대로다. PRD 5, 데이터 흐름의 회고 줄, README 다섯 행에 #49·#51과 어긋나는 글이 없다. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 161 tests in 16.184s`, `OK`. 통과

**남은 것**
- phase 1: 다섯 스킬의 기준 글이 작업 트리의 스킬 줄을 그 줄의 앞부분으로만 가리켜, run이 그 줄의 글을 바꾸면 다섯 본문도 함께 고쳐야 하고 테스트는 run 낱말의 글과 맞는지 보지 않는다 → 문제 아님 (지금 run 낱말 47줄의 한 줄이 다섯 본문이 가리키는 앞부분으로 시작해 어긋남이 없고, 앞으로의 변경에 대한 위험이라 넷 가운데 어느 것에도 걸리지 않는다)
- phase 1: 고친 retro, eval, phase가 실제로 그렇게 도는지 돌려 보지 않았다 → 문제 아님 (phase 2가 장면 R·E·P1·P2로 돌렸고 이번 회고에서 복제본의 커밋과 결과 줄을 직접 대어 기대와 같음을 봤다)
- phase 2: 원본의 "돌리기 전" `git status --short`를 장면을 띄우기 직전에 재지 않고 00:36:37의 값과 TODO 1 체크로 적었다 → 문제 아님 (장면 커밋은 모두 복제본에만 있고 원본 HEAD는 전후 같으며, 그 사이 원본의 변경은 체크 한 줄이라 장면이 원본을 바꾸지 않았다는 완료 조건 4의 동작에 걸리지 않는다)
- phase 2: 장면 E의 eval이 #49를 고치기 전의 retro가 쓴 `FRICTION.md` 문제 줄과 회고 "문제 아님"을 어느 쪽으로 셀지 정하지 않은 채다 → 문제 아님 (완료 조건 4의 장면 E 기대는 `RUNLOG` 행과 `권한`만 보고, #49를 고친 뒤의 retro는 그 꼴의 줄을 만들지 않는다)
- phase 2: 장면 R의 retro가 `문제` 0개로 판정하면서 `FRICTION.md`에 `문제` 줄 여섯을 더했다 → 문제 아님 (그 여섯 줄은 기록·확인 절의 "하네스에서 걸린 것"과 계획 수정에서 온 것으로 retro 5번대로이고, 장면 R의 기대는 "문제 아님" 줄의 내용이 들지 않는 것이라 걸리지 않는다)
- phase 2: 복제본과 출력 기록은 임시 폴더라 지워질 수 있다 → 문제 아님 (회고 때 넷 모두 남아 있어 직접 대어 봤고, 장면 절이 본 결과를 글로 남겼다)

**문제**
- 없음

**판정**: 통과
