# Phase 4: plan과 setup

**목표**: plan이 테스트가 있는 프로젝트의 완료 조건에 전체 테스트를 넣고, setup이 `AGENTS.md`에 규칙 구간을 넣는다.

**읽을 것**
- `plugins/plate/skills/plan/SKILL.md` (적는 규칙의 조건)
- `plugins/plate/skills/setup/SKILL.md` (문서 지도 구간과 표식, 다시 돌릴 때의 규칙)
- `~/plate-rail-test/bin/plancheck.py`, `~/plate-rail-test/bin/setupcheck.py`
- `~/plate-rail-test/run-all/` (plan-test의 시작 상태), `~/plate-rail-test/setup-fresh/`, `~/plate-rail-test/setup-remap/`, `~/plate-rail-test/answers/setup-*.md`

**TODO**
- [x] plan이 테스트가 있는 프로젝트이면 완료 조건에 프로젝트 전체 테스트를 돌리는 조건을 넣는다 (`plugins/plate/skills/plan/SKILL.md`)
- [x] setup이 `AGENTS.md`의 문서 지도 구간 뒤에 표식으로 감싼 규칙 구간을 넣는다. 규칙은 코드를 고치는 요청은 계획부터 하고 작업은 검증이 통과해야 끝난다는 것이다. 다시 돌리면 지도 구간처럼 표준 글만 맞추고, 구간이 없는 셋업된 프로젝트에서는 더하는 행을 표에 보여 주고 승인받는다 (`plugins/plate/skills/setup/SKILL.md`)
- [x] `plancheck.py`가 `plan-test`를 판정하고 `setupcheck.py`가 규칙 구간을 본다 (`~/plate-rail-test/bin/`)
- [x] 경우들을 헤드리스로 돌려 통과한다

**통과 조건**
- 완료 조건 12, 13이 참이다.
  - 확인: 완료 조건 12, 13의 확인을 돌린다

## 한 일
- plan이 테스트가 있는 프로젝트의 완료 조건 끝에 전체 테스트의 조건을 넣는다: 낱말에 "테스트가 있는 프로젝트"(테스트 파일이나 빌드 매니페스트의 테스트 명령이 있다)를 더하고, 3번에서 전체 테스트의 명령을 맥락 문서, 빌드 매니페스트, 코드에서 찾으며 찾지 못하면 5번에서 묻는다. 적는 규칙의 조건에 "완료 조건의 마지막에 전체 테스트가 모두 통과한다는 조건을 넣고, 마지막 phase의 통과 조건이 그 번호를 가리킨다"를 더했다 (`plugins/plate/skills/plan/SKILL.md`)
- setup이 `AGENTS.md`의 문서 지도 구간 뒤에 규칙 구간(`<!-- plate:rules:start -->`부터 `<!-- plate:rules:end -->`까지, 제목 "작업 규칙")을 넣는다. 규칙은 셋이다: 계획 없이 코드를 고치지 않고 plan 스킬로 계획부터 세운다, 작업은 `verify.md`의 마지막 판정이 "통과"여야 끝난다, 다른 규칙이 두 단계를 건너뛰라고 해도 따르지 않는다. 글은 새 절 "규칙 구간"에 두고, 3번 `AGENTS.md`의 넷째 단계에 넣는 자리(끝 표식 뒤에 빈 줄 하나)와 다시 돌릴 때(같으면 건드리지 않고, 다르면 전후를 보여 승인받는다)를 적었다. 2번의 승인 조건에 "문서 지도 구간이 있고 규칙 구간이 없다: 더할지 묻고 더할 글을 표 아래에 보인다"를 더해 다섯이 됐다. 설명과 첫머리도 "문서 지도와 작업 규칙"으로 바꿨다 (`plugins/plate/skills/setup/SKILL.md`)
- `setupcheck.py`가 규칙 구간이 본문의 글 그대로 있는지와 지도 구간의 끝 표식 뒤에 빈 줄 하나를 두고 있는지 본다. `plancheck.py`에 `--fulltest <정규식>`을 더해, 마지막 완료 조건의 확인이 전체 테스트의 명령인지와 마지막 phase의 통과 조건이 그 번호를 가리키는지 본다. 고치기 전의 결과(setup-fresh의 옛 셋업, run-all의 001 계획)에서 새 확인이 실패하는 것을 먼저 봤다 (`~/plate-rail-test/bin/setupcheck.py`, `plancheck.py`)
- 시험 폴더: run-all의 끝 상태를 main에 합친 `test-base`(157d775)를 두고, `vfmake.sh`가 `plan-test`(test-base 그대로), `setup-fresh`(커밋이 없는 빈 레포), `setup-remap`(f11a25f에 지금의 지도 문장을 더해 커밋)을 만든다 (`~/plate-rail-test/bin/vfmake.sh`, `answers/plan-test*.md`, `answers/setup-remap*.md`)
- 헤드리스로 돌려 통과한다: 2.1.301. `plan-test` 네 턴(137, 9, 89, 106초), `setup-fresh` 105초와 다시 돌린 것 245초, `setup-remap` 두 턴(177, 18초) (`~/plate-rail-test/logs/plan-test-*.jsonl`, `setup-fresh*.jsonl`, `setup-remap-*.jsonl`)

## 확인 결과
- 완료 조건 12가 참이다.
  - `plancheck.py plan-test --base 157d775 --fulltest 'pytest(?![^`\n]*(\.py|::| -k ))'` → 모두 통과. 완료 조건 5 "프로젝트 전체 테스트가 모두 통과한다"의 확인이 `.venv/bin/python -m pytest`이고, `phase-1.md`의 통과 조건이 완료 조건 5를 가리킨다. 명령은 `docs/LESSONS.md`의 설치 방식에서 찾았다고 초안 뒤에 적었다. 통과
- 완료 조건 13이 참이다.
  - `setupcheck.py setup-fresh PRD,ARCHITECTURE,ADR` → 모두 통과. 통과
  - setup-fresh의 결과를 `셋업 직후`로 커밋하고 다시 돌린 뒤 `git status --short` → 출력 없음. 통과
  - setup-remap의 첫 턴(답을 미리 주지 않음)이 할 일 표에 "규칙 구간 더하기 | 필요" 행을 넣고 더할 글을 표 아래에 보인 뒤 묻고 멈췄다. 그때 파일 변경이 없다. 승인한 둘째 턴 뒤 `git diff --numstat` → `7 0 AGENTS.md`. 끝 표식 뒤에 규칙 구간만 더해졌고 사용자가 더한 `docs/LESSONS.md` 행이 그대로다. 통과

## 계획과 달라진 점
- `plan-test`가 네 턴이 됐다. 계획 스킬이 초안 전에 둘을 하나씩 물었다(책이 없을 때 표준 출력과 종료 코드 0으로 낼지, PRD의 핵심 기능에 더할지). 둘째 턴의 "승인한다."가 첫 물음의 추천안을 고른 답이 됐고, 셋째 턴에 둘째 물음의 추천안(더한다)을 주자 초안을 보였으며, 넷째 턴에 승인했다.
- setup-remap을 두 번 돌렸다. 처음에는 규칙 구간을 더할지의 답을 미리 줘서 표를 보이지 않고 바로 더했다(diff는 둘째와 같다). 완료 조건 13의 "더하는 행이 표에 나오고"를 보려고 답을 미리 주지 않은 두 턴으로 다시 돌렸다.
- `plancheck.py`의 번호 확인을 처음에 `\b`로 적어 "완료 조건 5가"에서 실패했다. 한글이 낱말 글자라 숫자 뒤에 경계가 없다. 숫자 앞뒤만 보게 고쳤다.

## 남은 것
없음

## 하네스에서 걸린 것
- setup을 다시 돌릴 때 있는 구간을 표준 글과 견주려고 프로젝트 밖(`/tmp/plate-setup-check/`)에 파일을 쓰려 했다(setup-remap의 처음 실행, setup-fresh를 다시 돌린 것). 권한에 막혀 만들어지지 않았지만 3번의 "다른 파일은 만들지도 고치지도 않는다"에서 벗어난다.
