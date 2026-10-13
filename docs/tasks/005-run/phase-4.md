# Phase 4: 판정 도구와 시험 폴더를 준비한다

**목표**: 완료 조건 1~15를 돌릴 판정 도구, 시험 폴더, 요청과 답 파일이 `~/plate-rail-test`에 있다.

**읽을 것**
- `docs/TOOLS.md` ("Claude Code" 절: 헤드리스 명령의 꼴, 서브에이전트와 권한의 허용 목록, worktree)
- `~/plate-rail-test/bin/run.sh`, `~/plate-rail-test/bin/plancheck.py`, `~/plate-rail-test/bin/calls.py` (지금의 실행 스크립트와 판정 도구)
- `~/plate-rail-test/answers/plan-small.md`, `plan-big.md`, `plan-adr.md`, `plan-turn-1.md` (3단계의 요청과 답 파일의 꼴)
- `plugins/plate/skills/plan/SKILL.md`, `run/SKILL.md`, `phase/SKILL.md`, `retro/SKILL.md` (판정할 동작)

**TODO**
- [ ] `bin/runcheck.py`가 생긴다. 완료 조건 1~13과 15의 기대 가운데 기계로 볼 수 있는 것을 본다: 커밋의 순서와 메시지와 든 파일, 작업 폴더에 남은 파일, 통과 커밋 직전의 `phase-N.md`의 꼴, `docs/LESSONS.md`와 지도의 행, worktree와 브랜치, 실행 기록의 에이전트 호출과 메인이 직접 고친 파일
- [ ] `bin/plancheck.py`가 `plan.md`(머리 다섯 절, 번호 목록의 완료 조건)와 `phase-N.md`(제목, 계획 네 항목)를 보고, 계획 커밋에 그 파일들만 들었는지 본다
- [ ] `bin/run.sh`가 run 스킬을 요청과 답이 함께 든 파일로 돌리고 worktree 폴더(`<폴더>/.worktrees/<이름>`)에서도 돌린다. 권한은 `docs/TOOLS.md`의 허용 목록으로 준다. 모든 명령을 허용하는 옵션은 쓰지 않고, 필요하면 쓰기 전에 사용자에게 묻는다
- [ ] 시험 폴더가 생긴다. `plan-base`에 고친 plan 스킬로 계획한 "계획 직후" 둘(작은 요청, 큰 요청)과 수행까지 돌린 "수행 커밋 직후"를 바탕으로 `run-small`, `run-big`, `run-all`, `run-skip`, `run-fix`, `run-wrong`, `run-resume`, `run-wt`, `run-rule`, `run-nogit`, `run-dirty`, `run-noplan`, `run-lessons`를 만든다
- [ ] 손으로 만드는 상태가 들어 있다: 5(실패하는 확인), 6(맞출 수 없는 통과 조건), 7(체크된 첫 TODO), 9(`AGENTS.md`의 커밋 메시지 규칙), 11(상관없는 파일의 커밋하지 않은 변경), 13("하네스에서 걸린 것" 한 줄)
- [ ] `run-ev`가 생긴다. `ctx-ev`를 복사해 채운 맥락 문서를 커밋한 것이다. 요청 글은 빌드 없이 확인할 수 있는 작은 요청으로 사용자에게 물어 정한다(excel-viewer는 Gradle 빌드다)
- [ ] 요청과 답 파일이 생긴다. plan 다시 판정의 것도 든다 (`~/plate-rail-test/answers/run-*.md`)

**통과 조건**
- `runcheck.py`가 통과 표본을 통과로, 실패 표본을 실패로 낸다.
  - 확인: 손으로 만든 통과 표본 하나와 실패 표본 셋(커밋의 순서가 다르다, 통과 커밋에 `plan.md`가 들었다, `phase-N.md`가 남았다)을 돌려 결과를 본다
- `plancheck.py`가 새 꼴의 계획을 통과로, 옛 꼴을 실패로 낸다.
  - 확인: 고친 plan 스킬로 쓴 "계획 직후" 폴더와 `plan-small`(phase 절이 든 `plan.md` 하나)을 돌려 결과를 본다
- 시험 폴더와 답 파일이 있다.
  - 확인: `ls -d ~/plate-rail-test/run-*` → 열넷. `ls ~/plate-rail-test/answers/run-*.md`
