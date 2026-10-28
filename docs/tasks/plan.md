# plan·phase·check·retro·review의 확인 명령과 테스트 적절성 이슈를 고친다

**이름**: check-commands

## 요청
열린 GitHub 이슈 #68, #69, #70(지난 compare-checks tasks의 하네스 eval이 낸 plate 자체 고칠 거리)을 한 tasks로 고친다. #69: phase·check·retro가 계획의 확인 명령을 적힌 그대로 돌리고, 고쳐 돌렸으면 기록에 남긴다. #70: review의 테스트 적절성에서 바뀐 실행 코드가 테스트 파일뿐인 경우의 등급표를 정한다. #68: plan의 초안 점검에서 확인 명령이 적힌 그대로 도는지(옵션 오류 등) 돌려 본다 — `-` 패턴만이 아니라 넓혀서. 버전은 0.21.0.

## 목표
phase·check·retro는 적힌 그대로 돌지 않는 확인 명령을 대상·패턴·기대를 바꾸지 않는 고침으로만 고쳐 돌리고 그 사실을 기록한다(#69). review는 테스트 파일을 빼고 테스트 적절성의 표를 고르고 어느 표를 썼는지 근거에 적는다(#70). plan은 읽기만 하는 확인 명령을 초안 점검에서 돌려 적힌 그대로 도는지 본다(#68). check와 review의 바뀐 동작은 헤드리스로 돌려 보고, 고친 글마다 빠지면 실패하는 테스트를 더한다. 버전은 0.21.0이 되고, `docs/ARCHITECTURE.md`의 `test_skill_rules.py` 줄, 테스트 모듈 docstring, ADR-024의 트레이드오프가 바뀐 규칙에 맞춰진다.

## 범위 밖
- plan·phase·retro의 바뀐 동작을 헤드리스로 돌려 보는 것. `돌리지 않음`으로 둔다
- 테스트 적절성을 결과물인 마크다운과 실행 코드로 나눠 따로 매기는 것(섞인 tasks는 지금처럼 기본 등급표다)
- GitHub 이슈 #68·#69·#70을 닫는 것. PR이 머지된 뒤 닫는다
- 1.0.0을 내는 것

## 완료 조건
1. #69: phase·check·retro 본문의 확인을 돌리는 절에 고침 규칙이 있다. phase 3번 절에 `대상과 패턴과 기대를 바꾸지 않는 고침만 해 다시 돌린다`, `고친 명령과 까닭을 "계획과 달라진 점"과 "하네스에서 걸린 것"에 적는다`, `대상이나 패턴이나 기대를 바꿔야 돌면 상태는 "계획이 틀림"이다`가 있다. check 2번 절에 `확인은 적힌 그대로 먼저 돌린다`, `대상과 패턴과 기대를 바꾸지 않는 고침만 해 다시 돌린다`, `적힌 명령, 고친 명령, 까닭을 "하네스에서 걸린 것"에 적는다`, `대상이나 패턴이나 기대를 바꿔야 돌면 그 확인은 실패다`가 있다. retro 2번 절에 `확인은 적힌 그대로 먼저 돌린다`, `대상과 패턴과 기대를 바꾸지 않는 고침만 해 다시 돌린다`, `적힌 명령, 고친 명령, 까닭을 "확인"의 결과에 적고 5번의 문제로 모은다`, `대상이나 패턴이나 기대를 바꿔야 돌면 그 확인은 실패다`가 있다
   - 확인: `grep -cF -e '<글>' <파일>`을 위 글과 파일(phase는 `plugins/plate/skills/phase/SKILL.md`, check는 `plugins/plate/skills/check/SKILL.md`, retro는 `plugins/plate/skills/retro/SKILL.md`)마다 돌리면 저마다 `1`이다. 하나라도 `1`이 아니면 실패
   - 확인: phase 1 기록의 check 헤드리스 시험 결과를 읽는다. 시험 저장소의 `phase-1.md` 통과 조건 둘 가운데 조건 1은 `grep -F '- abc' f.txt`(`f.txt`에 `- abc` 줄이 있다), 조건 2는 없는 파일을 보는 `grep -F 'abc' nofile.txt`다. 더해진 `## 확인 1` 절에서 조건 1의 줄은 통과이고 그 절의 "하네스에서 걸린 것"에 적힌 명령 `grep -F '- abc' f.txt`와 `-e`나 `--`를 넣은 고친 명령이 함께 있고, 조건 2의 줄은 실패이고 판정은 실패다. 기록에 적힌 `git hash-object plugins/plate/skills/check/SKILL.md`의 값이 지금 작업 트리에서 다시 낸 값과 같다. 하나라도 아니면 실패
   - 돌리지 않음: phase와 retro의 고침 규칙은 헤드리스로 돌리지 않는다. 사용자가 check·review만 돌리기로 정했다
2. #70: review 본문의 낱말에 `**테스트 파일**`이 있고, 그 정의는 `` `.md`가 아닌 파일 가운데 `tests/`, `test/`, `__tests__/` 아래에 있거나 이름이 `test_*`, `*_test.*`, `*.test.*`, `*.spec.*` 꼴인 것 ``이다. `결과물인 마크다운, 실행 경로 없는 파일, 테스트 파일뿐이면`이 4번의 범주 표, 5번, PR 모드에 저마다 있고 옛 글 `결과물인 마크다운과 실행 경로 없는 파일뿐이면`은 없다. 5번에 `테스트 파일은 바뀐 동작이 아니라 그 근거라 표를 고를 때 세지 않는다`와 `테스트 적절성의 근거 첫 줄에 어느 표로 매겼는지 적는다`가 있다. `docs/ADR.md` ADR-024의 트레이드오프도 테스트 파일을 든다
   - 확인: `grep -cF -e '결과물인 마크다운, 실행 경로 없는 파일, 테스트 파일뿐이면' plugins/plate/skills/review/SKILL.md`가 `3`, `grep -cF -e '결과물인 마크다운과 실행 경로 없는 파일뿐이면' plugins/plate/skills/review/SKILL.md`가 `0`이다. 정의 글, `**테스트 파일**`, 5번의 두 글은 `grep -cF -e`로 저마다 `1`이다. `grep -cF -e '테스트 파일뿐이면' docs/ADR.md`가 `1`이다. 하나라도 아니면 실패
   - 확인: phase 2 기록의 review 헤드리스 시험 결과를 두 갈래로 읽는다. 갈래 1(바뀐 코드 파일이 결과물인 마크다운 `skills/x/SKILL.md`와 테스트 파일 `tests/test_x.py`뿐이고 완료 조건에 읽기만 하는 확인과 `돌리지 않음` 줄만 있다)에서 `review.md`의 테스트 적절성 근거 첫 줄이 결과물인 마크다운만 바뀐 경우의 표로 매겼다고 적고 등급이 A가 아니다. 갈래 2(테스트 파일이 아닌 실행 코드 `tool.py`도 바뀌었다)에서 근거 첫 줄이 기본 등급표로 매겼다고 적는다. 기록에 적힌 `git hash-object plugins/plate/skills/review/SKILL.md`의 값이 지금 작업 트리에서 다시 낸 값과 같다. 하나라도 아니면 실패
3. #68: plan 본문 절대 규칙 3의 옛 글 `완료 조건과 통과 조건에 적는 확인 명령은 미리 돌려 보지 않고 적는다`가 `완료 조건과 통과 조건의 확인 명령은 읽기만 하는 것만 6번의 점검에서 돌려 적힌 그대로 도는지 본다`로 바뀐다. 6번 "초안을 보여 주기 전에 아래를 본다." 목록에 `읽기만 하는 확인 명령(파일이나 저장소를 바꾸지 않는 것)을 돌려 적힌 그대로 도는지 본다`, `결과값은 견주지 않는다`, `쓰는 명령은 돌리지 않고 같은 꼴을 글로 본다`가 있다. 적는 규칙 "조건"의 `- 확인은 돌릴 명령과 기대 결과를 우선한다.`로 시작하는 항목에 `확인 명령은 적힌 그대로 돌게 적는다`가 있다
   - 확인: 옛 글은 `grep -cF -e '<글>' plugins/plate/skills/plan/SKILL.md`로 `0`이고 새 글 다섯은 저마다 `1`이다. 하나라도 아니면 실패
   - 확인: `grep -F -e '- 확인은 돌릴 명령과 기대 결과를 우선한다.' plugins/plate/skills/plan/SKILL.md`가 한 줄을 내고 그 줄에 `확인 명령은 적힌 그대로 돌게 적는다`가 든다
   - 돌리지 않음: plan은 사람에게 묻고 초안마다 승인을 받는 스킬이라, 고친 점검대로 초안이 점검되는지는 여러 턴의 답을 이어야 닿는다
4. 고친 글이 빠지면 실패하는 테스트가 있고, 모든 테스트가 통과한다
   - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
   - 확인: 아래 다섯 시험을 저마다 새 사본(`mktemp -d`로 만든 폴더에 작업 트리의 `plugins`와 `tests`를 `cp -R`로 복사한 것)에서 한다. 그 글이 사본의 파일에 한 번 있는지 보고(없으면 실패), 그 글을 빈 글로 바꾸고 사본에서 `python3 -m unittest discover -s tests`를 돌리면 출력에 그 테스트의 `FAIL:` 줄이 있다. phase 본문의 `고친 명령과 까닭을 "계획과 달라진 점"과 "하네스에서 걸린 것"에 적는다` → `FAIL: test_69_fix_check_command_and_record (test_skill_rules.PhaseRulesTest`, check 본문의 `적힌 명령, 고친 명령, 까닭을 "하네스에서 걸린 것"에 적는다` → `FAIL: test_69_run_check_as_written (test_skill_rules.CheckRulesTest`, retro 본문의 `적힌 명령, 고친 명령, 까닭을 "확인"의 결과에 적고 5번의 문제로 모은다` → `FAIL: test_69_run_check_as_written (test_skill_rules.RetroRulesTest`, review 본문의 `테스트 파일은 바뀐 동작이 아니라 그 근거라 표를 고를 때 세지 않는다` → `FAIL: test_70_test_files_do_not_pick_default_table (test_skill_rules.ReviewRulesTest`, plan 본문의 `읽기만 하는 확인 명령(파일이나 저장소를 바꾸지 않는 것)을 돌려 적힌 그대로 도는지 본다` → `FAIL: test_68_check_commands_run_as_written (test_skill_rules.PlanRulesTest`
5. 두 매니페스트의 버전이 0.21.0이고, 마켓플레이스가 유효하고, 문서와 테스트 설명이 바뀐 규칙과 맞는다
   - 확인: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json`의 두 줄이 모두 `0.21.0`
   - 확인: `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
   - 확인: `docs/ARCHITECTURE.md`의 `test_skill_rules.py` 줄에 `적힌 그대로 돌지 않는 확인 명령`, `테스트 파일도 빼고 표를 고름`, `읽기만 하는 확인 명령을 초안 점검에서 돌림`이 저마다 든다. 한 글이라도 빠지면 실패
   - 확인: `sed -n '1,8p' tests/test_skill_rules.py`의 목록에 plan의 `#68`, phase·check·retro의 `#69`, review의 `#70`이 있다. 하나라도 없으면 실패

## 결정
- 적힌 그대로 돌지 않는 확인 명령(옵션·문법 오류로 돌지 않는 것)은 대상·패턴·기대를 바꾸지 않는 고침(`-e`나 `--` 붙이기, 따옴표 맞추기)으로만 고쳐 돌리고 기록한다. 더 큰 고침이 필요하면 수행은 "계획이 틀림", 확인과 회고는 실패다. 이유: 오타 하나로 run을 멈추지 않으면서도 tasks 끝까지 숨기지 않는다
- 테스트 적절성의 표를 고를 때 테스트 파일은 세지 않는다. 테스트 파일의 정의는 run·plan의 것과 같다. 이유: 테스트 파일은 제품 동작이 아니라 근거이고, 이 저장소의 tasks는 대부분 이 꼴이라 스킬 동작을 돌려 보는 확인을 요구하는 장치가 매번 비켜 갔다
- plan은 읽기만 하는 확인 명령만 초안 점검에서 돌리고, 결과값은 견주지 않고 적힌 그대로 도는지만 본다. 쓰는 명령(`mktemp`, `cp`, 커밋)은 돌리지 않는다. 이유: `-` 패턴 말고도 따옴표 어긋남, 없는 옵션 같은 오류를 함께 잡고, 쓰기 부작용은 막는다
- 헤드리스로 돌려 보는 확인은 check와 review만 둔다. 이유: 두 핵심 동작은 실제로 보고, plan은 사람에게 묻는 스킬이라 돌리기 어렵다
- 헤드리스 시험은 `mktemp -d`의 시험 저장소에서 `claude -p`에 작업 트리의 `plugins/plate`를 `--plugin-dir`로, `--permission-mode bypassPermissions`로 돌리고, 기록에는 차림, 출력, 그때의 본문 해시(`git hash-object`)를 남긴다. 이유: `docs/TOOLS.md`의 "스킬을 헤드리스로 돌려 볼 때의 허용 목록"(이은 Bash는 허용 목록으로 풀리지 않는다)과 plan의 남은 결과를 읽는 확인 규칙 (추천안으로 정함)
- task 하나에 phase 셋으로 한다(#69, #70, #68 순서. 버전은 마지막 phase에서 올린다). 이유: 고칠 스킬이 이슈마다 달라 phase마다 따로 확인할 수 있다 (추천안으로 정함)
- 고친 글과 테스트 이름은 완료 조건에 적은 그대로 한다. 이유: 지울 글을 그대로 인용하고 실패할 테스트를 미리 적으려면 글과 이름이 계획에서 정해져야 한다 (추천안으로 정함)
- 버전은 0.21.0이다. 이유: 요청
- run을 시작하기 전에 사용자가 plan 모드를 끄고 bypassPermissions로 둔다. 이유: `AGENTS.md`의 작업 규칙(`plugins/plate/skills/` 편집이 auto mode에서 막힌다)

## task 목록
- `001-check-commands`: #68·#69·#70이 고쳐지고, 그 규칙 글의 테스트와 check·review의 헤드리스 시험이 더해지고, 버전이 0.21.0이 된다
