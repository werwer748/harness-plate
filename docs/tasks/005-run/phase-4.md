# Phase 4: 판정 도구와 시험 폴더를 준비한다

**목표**: 완료 조건 1~15를 돌릴 판정 도구, 시험 폴더, 요청과 답 파일이 `~/plate-rail-test`에 있다.

**읽을 것**
- `docs/TOOLS.md` ("Claude Code" 절: 헤드리스 명령의 꼴, 서브에이전트와 권한의 허용 목록, worktree)
- `~/plate-rail-test/bin/run.sh`, `~/plate-rail-test/bin/plancheck.py`, `~/plate-rail-test/bin/calls.py` (지금의 실행 스크립트와 판정 도구)
- `~/plate-rail-test/answers/plan-small.md`, `plan-big.md`, `plan-adr.md`, `plan-turn-1.md` (3단계의 요청과 답 파일의 꼴)
- `plugins/plate/skills/plan/SKILL.md`, `run/SKILL.md`, `phase/SKILL.md`, `retro/SKILL.md` (판정할 동작)

**TODO**
- [x] `bin/runcheck.py`가 생긴다. 완료 조건 1~13과 15의 기대 가운데 기계로 볼 수 있는 것을 본다: 커밋의 순서와 메시지와 든 파일, 작업 폴더에 남은 파일, 통과 커밋 직전의 `phase-N.md`의 꼴, `docs/LESSONS.md`와 지도의 행, worktree와 브랜치, 실행 기록의 에이전트 호출과 메인이 직접 고친 파일
- [x] `bin/plancheck.py`가 `plan.md`(머리 다섯 절, 번호 목록의 완료 조건)와 `phase-N.md`(제목, 계획 네 항목)를 보고, 계획 커밋에 그 파일들만 들었는지 본다
- [x] `bin/run.sh`가 run 스킬을 요청과 답이 함께 든 파일로 돌리고 worktree 폴더(`<폴더>/.worktrees/<이름>`)에서도 돌린다. 권한은 `docs/TOOLS.md`의 허용 목록으로 준다. 모든 명령을 허용하는 옵션은 쓰지 않고, 필요하면 쓰기 전에 사용자에게 묻는다
- [x] 시험 폴더가 생긴다. `plan-base`에 고친 plan 스킬로 계획한 "계획 직후" 둘(작은 요청, 큰 요청)과 수행까지 돌린 "수행 커밋 직후"를 바탕으로 `run-small`, `run-big`, `run-all`, `run-skip`, `run-fix`, `run-wrong`, `run-resume`, `run-wt`, `run-rule`, `run-nogit`, `run-dirty`, `run-noplan`, `run-lessons`를 만든다
- [x] 손으로 만드는 상태가 들어 있다: 5(실패하는 확인), 6(맞출 수 없는 통과 조건), 7(체크된 첫 TODO), 9(`AGENTS.md`의 커밋 메시지 규칙), 11(상관없는 파일의 커밋하지 않은 변경), 13("하네스에서 걸린 것" 한 줄)
- [x] `run-ev`가 생긴다. `ctx-ev`를 복사해 채운 맥락 문서를 커밋한 것이다. 요청 글은 빌드 없이 확인할 수 있는 작은 요청으로 사용자에게 물어 정한다(excel-viewer는 Gradle 빌드다)
- [x] 요청과 답 파일이 생긴다. plan 다시 판정의 것도 든다 (`~/plate-rail-test/answers/run-*.md`)

**통과 조건**
- `runcheck.py`가 통과 표본을 통과로, 실패 표본을 실패로 낸다.
  - 확인: 손으로 만든 통과 표본 하나와 실패 표본 셋(커밋의 순서가 다르다, 통과 커밋에 `plan.md`가 들었다, `phase-N.md`가 남았다)을 돌려 결과를 본다
- `plancheck.py`가 새 꼴의 계획을 통과로, 옛 꼴을 실패로 낸다.
  - 확인: 고친 plan 스킬로 쓴 "계획 직후" 폴더와 `plan-small`(phase 절이 든 `plan.md` 하나)을 돌려 결과를 본다
- 시험 폴더와 답 파일이 있다.
  - 확인: `ls -d ~/plate-rail-test/run-*` → 열넷. `ls ~/plate-rail-test/answers/run-*.md`

## 한 일
- `bin/runcheck.py`가 생긴다: 폴더 이름으로 경우의 기대(`CASES`)를 찾아 커밋의 순서와 메시지와 든 파일, 남은 파일, 통과 커밋 직전의 `phase-N.md`, `docs/LESSONS.md`와 지도의 행, worktree, 실행 기록의 에이전트 호출과 메인이 고친 파일을 본다. 여러 턴으로 도는 경우의 중간 상태는 `--stage`로 본다 (`~/plate-rail-test/bin/runcheck.py`, 표본을 만드는 `bin/rcsample.sh`)
- `bin/plancheck.py`가 계획 파일을 본다: `plan.md`의 절 다섯, 번호 목록의 완료 조건, 결정의 이유와 고르지 않은 안, `phase-N.md`의 제목과 계획 네 항목, 계획 커밋에 든 파일을 본다. 프로젝트의 커밋 메시지 꼴은 `--msg`로 준다 (`~/plate-rail-test/bin/plancheck.py`)
- `bin/run.sh`가 실행 스킬을 돌린다: `run`, `phase`, `retro`에 허용 목록과 `--forward-subagent-text`를 주고, worktree 폴더에서도 돌며, 한 실행에만 더할 허용 항목을 `RUN_ALLOW`로 받는다. 계획 스킬을 두 턴으로 돌리는 `bin/plan2.sh`를 더했다 (`~/plate-rail-test/bin/run.sh`, `bin/plan2.sh`)
- 시험 폴더가 생긴다: 고친 plan 스킬로 계획한 `base-small`, `base-big`(phase 셋), `base-nogit`과 phase 스킬을 직접 불러 수행까지 돌린 `base-small-done`을 바탕으로 열셋을 만들었다 (`~/plate-rail-test/run-*`)
- 손으로 만드는 상태: 5번은 `.gitignore`의 한 줄을 틀리게 고쳐 수행 커밋에 넣었고, 6번은 범위 밖과 부딪히는 통과 조건(`.env`)을 `phase-1.md`에 넣어 커밋했고, 7번은 첫 TODO의 결과(`pyproject.toml`)를 표식과 함께 만들어 체크했고, 9번은 `AGENTS.md`에 커밋 메시지 규칙을 적었고, 11번은 `NOTES.md`를 고쳐 두었고, 13번은 "하네스에서 걸린 것"에 한 줄을 넣어 수행 커밋에 넣었다
- `run-ev`가 생긴다: `ctx-ev`를 복사해 채운 맥락 문서를 커밋했다. 사용자가 요청은 "`plugin.xml`에 `<change-notes>` 추가"를, 그 프로젝트의 훅 플러그인은 "복제본에서만 끈다"를 골랐다 (`~/plate-rail-test/run-ev`, `answers/run-plan-ev.md`)
- 요청과 답 파일이 생긴다: 실행의 것 열일곱과 계획의 것 다섯(`run-plan-*.md`), 승인 턴의 `approve.md`, phase를 직접 부르는 `run-phase-small.md`를 썼다 (`~/plate-rail-test/answers/`)

## 확인 결과
- `runcheck.py`가 통과 표본을 통과로, 실패 표본을 실패로 낸다.
  - `zsh bin/rcsample.sh` 뒤 `python3 bin/runcheck.py rc-ok --as run-small --logs rc-ok` → 모두 통과(exit 0). 통과
  - 같은 명령을 `rc-order`, `rc-planmd`, `rc-left`에 → 셋 다 "실패한 곳이 있음"(exit 1). 실패한 줄은 차례로 커밋의 순서(RPD), 통과 커밋에 든 `plan.md`, 남은 `phase-1.md`였다. 통과
- `plancheck.py`가 새 꼴의 계획을 통과로, 옛 꼴을 실패로 낸다.
  - `python3 bin/plancheck.py base-small --base <계획 전의 HEAD>` → 모두 통과. `base-big`, `run-wt --task 002`도 모두 통과. 통과
  - `python3 bin/plancheck.py plan-small` → 실패 셋(phase 파일이 없다, 절이 다섯을 넘는다, 완료 조건이 번호 목록이 아니다). 통과
- 시험 폴더와 답 파일이 있다.
  - `ls -d ~/plate-rail-test/run-*` → 열넷. `ls ~/plate-rail-test/answers/run-*.md` → 스물넷. 통과

## 계획과 달라진 점
- 바탕 폴더가 "계획 직후 둘과 수행 커밋 직후"에 `base-nogit`을 더해 넷이다. git 레포가 아닌 폴더는 새 꼴로 다시 계획해야 했다.
- 허용 목록에 `docs/TOOLS.md`에 없는 항목을 더했다: `git mv`, `git check-ignore`, `python3.12`, `python`, `pip`, `pip3`, `pytest`, `.venv/bin/pytest`, `.venv/bin/booklog`, `mktemp`, `echo`. 계획이 적은 확인 명령 `git check-ignore`가 승인을 요구해 수행 에이전트가 막힌 것을 보고 계획의 확인 명령에 나오는 것을 넣었다. 모든 명령을 허용하는 옵션은 쓰지 않았다.
- 6번의 통과 조건은 머리의 결정이 아니라 범위 밖과 부딪히게 만들었다. `base-small`의 결정이 "없음"이었다.
- `run-ev`에서는 그 프로젝트의 훅 플러그인을 껐다. 복제본에도 그 플러그인이 실려 커밋마다 Gradle 검사가 도는 것을 보고 사용자에게 물어 정했다.

## 남은 것
없음

## 하네스에서 걸린 것
- plan 스킬의 6번(ADR 후보)이 `base-big`의 계획에서 다섯 범주의 경계에 있는 결정 둘(테스트 도구 pytest, `LIKE` 검색)까지 후보로 냈다. 완료 조건 14에서 본다.
- 계획이 적은 확인 명령이 헤드리스의 권한에 막히면 수행 에이전트가 그 명령을 여러 꼴로 다시 시도하며 명령마다 약 65초를 기다린다.
