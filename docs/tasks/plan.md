# 1.0.0 전에 열린 이슈와 BACKLOG를 모두 고친다

**이름**: release-prep

## 요청
대상 저장소: /Users/hugo/Desktop/harness-plate. 요청: 1.0.0 릴리스. 지금 레포의 열린 이슈를 전부 처리하고, 전체 점검(cleanup)을 한 번 돌려서 이슈가 없으면 1.0.0을 배포한다.

## 목표
열린 이슈 10개(#34, #35, #36, #37, #38, #40, #41, #42, #43, #44)와 `docs/BACKLOG.md`의 항목을 고치고, 고친 스킬 동작을 저마다 임시 복제본에서 실제로 돌려 `docs/TOOLS.md`에 남긴다. 플러그인 버전은 0.17.0이 되고, 맥락 문서와 README가 고친 동작에 맞춰진다.

## 범위 밖
- 전체 점검(`plate:cleanup`)을 돌리는 것과 1.0.0으로 버전을 올리는 것, 태그와 릴리스. 이 tasks가 main에 들어간 뒤 사용자가 main에서 cleanup을 부르고, 발견이 없으면 별도 릴리스 tasks에서 한다
- GitHub 이슈를 닫는 것. PR이 머지된 뒤 닫는다
- run이 앞 phase의 "계획과 달라진 점"을 다음 phase 에이전트에게 넘기는 것(#42 해결책의 run 쪽)
- Codex와 Grok Build에서 확인하는 것(ADR-018)

## 완료 조건
1. run의 이슈 다섯이 고쳐졌다: #34(회고의 고침이 계획 파일을 고치게 하면 어느 실행 방식이든 "멈춘다"로 가고 물은 자리는 `멈춤`), #35(모르는 값은 단위 없이 `모름`), #38(고칠 phase의 TODO에 고친 동작을 적은 맥락 문서·README의 줄이 들고, 고침이 계획의 목표·완료 조건을 바꾸면 "멈춘다", 계획 커밋으로 고친 문제는 통과 조건에 따로 적는다), #40(첫 에이전트를 띄우기 전에 plan 모드나 쓰기가 막힐 권한 모드를 알리고 묻는다), #44(회고와 평가 에이전트 뒤의 `RUNLOG.md` 줄이 커밋되어 다음 에이전트가 깨끗한 작업 트리에서 시작한다)
   - 확인: `plugins/plate/skills/run/SKILL.md`의 "1. 시작 조건을 본다", "7. task 회고를 맡긴다", "8. 고칠 phase를 더한다", "tasks 끝", "`RUNLOG.md`" 절을 읽어 다섯 이슈의 해결이 저마다 적혀 있다. 하나라도 없으면 실패
   - 확인: `docs/TOOLS.md`의 run 장면 절을 읽어 장면마다 Claude Code 버전, 돌린 시각, 세션 id, 기대한 결과와 본 결과가 있고, 본 결과가 기대와 같다. 장면은 넷이다: plan 모드에서 run을 부르면 첫 에이전트를 띄우기 전에 묻고 멈춘다(#40), 회고 뒤와 하네스 eval 뒤의 `RUNLOG.md` 줄이 커밋되어 "고칠지"를 묻는 자리에서 `git status --short`가 비었다(#44), 회고의 문제가 task 머리의 완료 조건을 좁혀야 하면 tasks 일괄에서도 "멈춘다"로 가고 답한 뒤 `RUNLOG.md`의 물은 자리가 `멈춤`이다(#34, #38), 고칠 phase의 TODO에 맥락 문서·README의 줄이 들고 계획 커밋으로 고친 문제는 통과 조건에 커밋 해시와 함께 따로 적힌다(#38)
   - 확인: 장면 B 절에 적힌, 장면을 돌릴 때의 run 본문 해시(`git hash-object plugins/plate/skills/run/SKILL.md`)가 `git rev-parse HEAD:plugins/plate/skills/run/SKILL.md`와 같고, 장면 A·C·D의 돌린 시각이 `dfb0852`(2026-10-27T18:38:03+09:00)보다 늦고, `git diff dfb0852 HEAD -- plugins/plate/skills/run/SKILL.md`를 읽어 `dfb0852` 뒤에 바뀐 글이 `docs/TOOLS.md`를 커밋 자리에 넣는 글뿐이다
   - 돌리지 않음: #35는 에이전트의 사용량이 돌아오지 않는 경우를 장면으로 만들 수 없다
2. plan과 phase의 이슈 셋이 고쳐졌다: #37(완료 조건이 갈래를 가지면 갈래마다 돌리는 확인을 두고, 요약 줄의 확인에 견줄 갈래를 적고, git 원격이 있는 장면은 `git clone --bare`로 푸시 없이 채운다. 6번의 점검에도 같은 줄), #41(뒤 phase의 실행 조건이 앞 phase의 산출물에 기대면 그 phase의 TODO 첫 항목이나 결정에 "앞 phase의 산출물에 대어 맞춘다"를 적는다), #42(phase가 앞 phase의 결과가 필요하면 계획의 읽을 것에 적힌 산출물 파일만 읽고, 그 밖의 기록이 필요하면 읽지 않고 "하네스에서 걸린 것"에 적는다)
   - 확인: `plugins/plate/skills/plan/SKILL.md`의 "6. 초안을 보여 주고 승인받는다"와 적는 규칙의 "조건", "TODO" 절, `plugins/plate/skills/phase/SKILL.md`의 "1. 읽는다" 절을 읽어 세 이슈의 해결이 저마다 적혀 있다. 하나라도 없으면 실패
   - 확인: `docs/TOOLS.md`의 plan·phase 장면 절을 읽어 장면마다 Claude Code 버전, 돌린 시각, 세션 id, 기대한 결과와 본 결과가 있고, 본 결과가 기대와 같다. 장면은 셋이다: "만들거나 바꾼다" 갈래가 있는 요청의 tasks 머리 초안이 두 갈래마다 확인을 두고 git 장면을 `git clone --bare`로 채운다(#37), 뒤 phase가 앞 phase의 산출물을 돌리는 요청의 초안이 그 phase의 TODO 첫 항목이나 결정에 앞 phase의 산출물에 대어 맞춘다고 적는다(#41), 앞 phase의 산출물이 읽을 것에 든 phase를 수행한 세션의 기록에 `done-phase-1.md`를 읽은 도구 호출이 없다(#42)
   - 확인: 그 절의 돌린 시각이 `git log -1 --format=%cI -- plugins/plate/skills/plan/SKILL.md plugins/plate/skills/phase/SKILL.md`보다 늦다
3. eval과 review의 이슈 둘이 고쳐졌다: #36(`남은 것:`으로 시작하는 줄은 그 task의 회고에서 "문제"로 판정된 것만 실패로 세고, 명령 절의 사실이나 판단을 적은 메모 줄은 실패가 아니다), #43(결과물인 마크다운과 실행 경로 없는 파일만 바뀐 tasks의 테스트 적절성이 실행 코드의 테스트를 가정하지 않고 완료 조건의 돌려 보는 확인으로 매겨진다)
   - 확인: `plugins/plate/skills/eval/SKILL.md`의 "2. 실패를 모아 MAST 유형으로 나눈다" 절을 읽어 #36의 해결이 적혀 있다
   - 확인: `docs/TOOLS.md`의 eval·review 장면 절을 읽어 장면마다 Claude Code 버전, 돌린 시각, 세션 id, 기대한 결과와 본 결과가 있고, 본 결과가 기대와 같다. 장면은 둘이다: issue-sweep의 기록(`e3836b2`의 `docs/tasks/`에서 `eval.md`를 뺀 것)으로 돌린 eval의 실패 목록에, 그 task의 회고가 "문제"로 판정하지 않은 `남은 것:` 줄과 메모 줄이 하나도 없다(#36), cleanup의 기록(`6292d12`)으로 돌린 review의 테스트 적절성이 "결과물인 마크다운만 바뀐 경우"의 표로 매겨지고 근거가 완료 조건의 확인 줄이다(#43)
   - 확인: 그 절의 돌린 시각이 `git log -1 --format=%cI -- plugins/plate/skills/eval/SKILL.md plugins/plate/skills/review/SKILL.md`보다 늦다
4. BACKLOG의 항목이 고쳐졌다: 두 매니페스트의 버전이 다르거나, 1~3이 고친 스킬 규칙의 글이 본문에서 빠지면 실패하는 테스트가 `tests/`에 있고, `docs/BACKLOG.md`에서 그 항목이 지워졌다
   - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
   - 확인: `mktemp -d`에 저장소를 복사해 `plugins/plate/.codex-plugin/plugin.json`의 버전만 바꾸고 테스트를 돌리면 실패한다. 다시 복사해 run 본문의 #44 해결 글을 지우고 돌리면 실패한다
   - 확인: `docs/BACKLOG.md`에 `# BACKLOG` 줄만 남고 그 항목이 없다
5. 두 매니페스트의 버전이 0.17.0이고, 마켓플레이스가 유효하고, 맥락 문서와 README가 1~4가 바꾼 동작과 어긋나지 않는다.
   - 확인: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json`의 두 줄이 모두 `0.17.0`
   - 확인: `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
   - 확인: `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `README.md`를 문서마다 따로 읽어, 1~4가 바꾼 동작(run의 시작 물음, RUNLOG 커밋, 고칠 phase, plan의 갈래 확인과 앞 phase 산출물, phase의 읽기, eval의 남은 것 줄, 새 테스트 파일)과 어긋나는 줄이 없다. 하나라도 있으면 실패

## 결정
- 이 tasks는 열린 이슈와 BACKLOG만 고친다. 전체 점검은 머지 뒤 사용자가 main에서 부르고, 발견이 없으면 별도 릴리스 tasks에서 1.0.0을 낸다. 이유: cleanup은 사람에게 묻는 스킬이고 발견이 나오면 plan으로 새 tasks가 생기는 설계라 tasks 안에 넣으면 꼬인다
- 이슈는 PR이 머지된 뒤 닫는다. 이유: 기본 브랜치에 들어간 고침만 닫힌 것으로 본다
- 버전은 0.17.0이다. PR 전에 main이 먼저 0.17.0 이상이 되면 PR에서 다음 마이너로 맞춘다. 이유: 스킬 동작이 바뀌어 tasks마다 마이너를 올린다
- 스킬 동작을 바꾸는 조건은 모두 실제로 돌려 본다. 장면을 만들 수 없는 것만 `돌리지 않음`으로 둔다. 이유: "1.0 전이니까 확실하게 다 검증하고 싶어"
- 장면은 `mktemp -d`에 이 저장소를 복제한 곳에서 작업 트리의 `plugins/plate`를 `--plugin-dir`로 실어 헤드리스(`claude -p`, 물음에는 `--resume`으로 답한다)로 돌린다. 장면에 쓰는 tasks 기록은 이력의 지난 tasks 기록(`e3836b2`, `6292d12`)이거나 장면이 만든 작은 tasks이고, git 원격이 필요하면 `git clone --bare`로 채워 푸시하지 않는다. 허용 목록은 `docs/TOOLS.md`의 "Claude Code" 절의 것을 쓴다. 이유: 이 저장소를 더럽히지 않고, 지난 tasks에서 푸시로 원격을 채우다 푸시 훅에 걸렸다(#37)
- #43은 issue-sweep이 review에 더한 "결과물인 마크다운만 바뀐 경우"의 표로 이미 고쳐졌을 수 있으니, 장면을 먼저 돌려 기대대로면 review 본문을 고치지 않는다 (추천안으로 정함)
- #42는 phase의 "1. 읽는다"와 plan의 읽을 것으로 고치고, run이 앞 phase의 기록을 넘기게 하지 않는다 (추천안으로 정함). 이유: run이 맡기는 글은 고정이라 다른 글을 더하지 않는다
- run을 시작하기 전에 사용자가 plan 모드를 끄고 `plugins/plate/skills/` 쓰기가 막히지 않는 권한 모드로 둔다. 이유: `AGENTS.md`의 작업 규칙
- run 본문을 고치는 고칠 phase가 생겨, 시각 확인을 장면이 본 동작이 바뀐 커밋 기준으로 좁히고 그 동작에 걸리는 장면 B만 다시 돌린다 (001-run-rules phase 4의 멈춤에서 승인)

## task 목록
- `001-run-rules`: run의 이슈 다섯(#34, #35, #38, #40, #44)이 고쳐지고, 임시 복제본의 네 장면 결과가 `docs/TOOLS.md`에 남는다
- `002-plan-phase-rules`: plan과 phase의 이슈 셋(#37, #41, #42)이 고쳐지고, 세 장면 결과가 `docs/TOOLS.md`에 남는다
- `003-eval-review-rules`: eval과 review의 이슈 둘(#36, #43)이 고쳐지거나 이미 고쳐졌음이 확인되고, 두 장면 결과가 `docs/TOOLS.md`에 남는다
- `004-tests-version`: 버전 줄과 고친 규칙을 시험하는 테스트가 더해지고 BACKLOG 항목이 지워지며, 버전이 0.17.0이 되고 맥락 문서와 README가 맞춰진다
