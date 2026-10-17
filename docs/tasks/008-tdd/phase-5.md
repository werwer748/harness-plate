# Phase 5: 헤드리스 판정과 TOOLS

**목표**: 시험 폴더 셋의 실제 실행이 plan의 엣지케이스 물음, 테스트 먼저 기록, 계획 없는 편집 차단을 보이고, TOOLS에 훅 사실이 적힌다.

**읽을 것**
- `docs/TOOLS.md` (Claude Code 절: 헤드리스 명령의 꼴, 여러 턴, 서브에이전트 기록의 `parent_tool_use_id`, 허용 목록)
- `~/plate-rail-test/bin/vfmake.sh`, `~/plate-rail-test/bin/run.sh`, `~/plate-rail-test/bin/summ.py` (시험 폴더 만들기, 헤드리스 실행, 기록 읽기)
- `~/plate-rail-test/test-base` (booklog. 테스트가 있고 001이 검증 통과. 전체 테스트는 `.venv/bin/python -m pytest`)
- `plugins/plate/skills/plan/SKILL.md` (phase 2가 바꾼 양식과 5번)
- `plugins/plate/hooks/` (phase 1의 훅)

**TODO**
- [x] `bin/vfmake.sh`가 tdd-plan, tdd-run, tdd-edit을 만든다. tdd-run에는 테스트 먼저 "예"인 phase 하나의 계획(작업 002)을 얹는다 (`~/plate-rail-test/bin/vfmake.sh`)
- [x] 완료 조건 9의 tdd-plan 기록과 답 파일이 있다 (`~/plate-rail-test/logs/`, `~/plate-rail-test/answers/`)
- [x] 완료 조건 10의 tdd-run 기록이 있다 (`~/plate-rail-test/logs/tdd-run.jsonl`)
- [x] 완료 조건 11의 tdd-edit 기록이 있다 (`~/plate-rail-test/logs/tdd-edit.jsonl`)
- [x] TOOLS의 Claude Code 절에 완료 조건 12의 사실이 날짜·버전과 함께 적힌다 (`docs/TOOLS.md`)

**통과 조건**
- 머리의 완료 조건 1~13이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다

## 한 일
- `bin/vfmake.sh`가 tdd-plan, tdd-run, tdd-edit을 만든다. tdd-run에는 테스트 먼저 "예"인 phase 하나의 계획(작업 002)을 얹는다: 세 경우를 더했다. 셋 다 test-base를 복제하고, tdd-run은 2026-10-16 plan-test의 계획(9df1d54)을 heredoc으로 쓰고 `phase-1.md`의 목표 아래에 `**테스트 먼저**: 예` 줄을 더해 `plan: 002-list-command`로 커밋한다. 9df1d54와 견주니 그 한 줄(과 빈 줄)만 다르다 (`~/plate-rail-test/bin/vfmake.sh`)
- 완료 조건 9의 tdd-plan 기록과 답 파일이 있다: `bin/run.sh`로 `/plate:plan`을 네 턴 돌렸다(`logs/tdd-plan-1~4.jsonl`, 세션 id는 `logs/tdd-plan.sid`). 요청(`answers/tdd-plan-1.md`)에 출력 위치, 종료 코드, PRD에 더할지를 적어 두었더니 첫 턴이 다른 물음 없이 엣지케이스를 논의할지만 물었고 후보는 없었다. "논의한다"(`answers/tdd-plan-2.md`)에 후보 다섯을 선택지로 냈고, 2번(메모가 여럿 달린 책도 한 줄)만 넣고 1, 3, 4, 5번은 빼는 답(`answers/tdd-plan-3.md`)에 초안을 냈고, 승인(`answers/tdd-plan-4.md`)에 `68d79b8 plan: 002-list-command`로 커밋했다 (`~/plate-rail-test/logs/`, `~/plate-rail-test/answers/`)
- 완료 조건 10의 tdd-run 기록이 있다: `bin/run.sh claude tdd-run run tdd-run answers/tdd-run.md`(회고한다, 합친다를 미리 줌)로 한 번 돌렸다(626초). 수행 에이전트가 `tests/test_list.py`를 먼저 쓰고 실패를 본 뒤 구현해 훅에 한 번도 막히지 않았고, 회고 통과, 검증 1 통과, `main`에 fast-forward로 합쳐졌다 (`~/plate-rail-test/logs/tdd-run.jsonl`)
- 완료 조건 11의 tdd-edit 기록이 있다: tdd-edit에서 `claude -p "$(cat ../answers/tdd-edit.md)" --plugin-dir <레포>/plugins/plate --permission-mode acceptEdits --forward-subagent-text --output-format stream-json --verbose`로 돌렸다(27초. `bin/run.sh`는 늘 스킬을 부르므로 직접 돌렸다). 메인이 띄운 서브에이전트의 `booklog/cli.py` Edit가 계획부터를 알리는 글로 막혔다. 메인은 서브에이전트에게 넘긴 글에 "Bash나 Write로 우회하지 않는다"를 스스로 더했다 (`~/plate-rail-test/logs/tdd-edit.jsonl`)
- TOOLS의 Claude Code 절에 완료 조건 12의 사실이 날짜·버전과 함께 적힌다: 버전 줄에 6단계(2.1.302, 2026-10-17)를 더하고, "훅" 묶음에 `--plugin-dir`로 실은 플러그인의 훅이 도는 것, 서브에이전트의 편집에도 도는 것, 막을 때의 `tool_result` 꼴, PreToolUse 훅이 기록에 훅 줄을 남기지 않는 것, 실행 시간을 적었다 (`docs/TOOLS.md`)

## 확인 결과
- 머리의 완료 조건 1~13이 모두 참이다.
  - 완료 조건 1: `python3 -m unittest discover -s tests -v` → 31개, 마지막 줄 `OK`. `tests/test_edit_guard.py`를 읽음 → setup 안 됨(`test_setup_not_done_passes`), 코드 파일 아님(`test_non_code_files_pass`), 남은 phase 없음과 테스트 없는 프로젝트(`PlanFirstTest`, "계획부터"와 `plate:plan` 단언), 테스트 먼저 막음("실패하는 테스트부터" 단언), 커밋되지 않은 테스트 변경·아니오·표시 없음·테스트 없는 프로젝트·테스트 파일 편집의 통과, 세 번째 막음("더 시도하지 않는다", "막힘", "까닭", "해결책" 단언)이 모두 있다. 통과
  - 완료 조건 2: 완료 조건 11의 확인 → 아래와 같다. 통과
  - 완료 조건 3: `plugins/plate/skills/plan/SKILL.md`를 읽음 → 5번(80~83행)에 엣지케이스 물음과 후보를 먼저 내지 않는 규칙, 논의할 때와 안 할 때, 양식(152행)의 테스트 먼저 줄, 적는 규칙(199~200행)의 다섯 항목과 예/아니오 규칙이 있다. 통과
  - 완료 조건 4: `plugins/plate/skills/phase/SKILL.md`를 읽음 → 2번(44~52행)에 테스트 먼저의 순서와 출력 기록, 훅의 세 번째 막음에 멈추는 규칙이 있다. 통과
  - 완료 조건 5: retro의 3번(60행), verify의 3번(61행)을 읽음 → 둘 다 실패·통과 출력을 보고 없으면 "계획"으로 적는다. 통과
  - 완료 조건 6: `grep -rn '네 항목\|항목은 넷' plugins/plate/skills` → 출력 없음. run의 3번(95~98행)과 "고칠 phase를 더한다"(193, 205행)를 읽음 → 있다. 통과
  - 완료 조건 7: `grep -n '도구가 동작을 끊는 장치는 두지 않는다' docs/PRD.md` → 출력 없음. `grep -n '훅은 두지 않는다' docs/ARCHITECTURE.md` → 출력 없음. PRD의 목표·범위 밖·핵심 기능 6~9와 1.0.0, ARCHITECTURE의 기술 스택·`hooks/`·`tests/`·훅 규칙, ADR-019를 읽음 → 있다. 통과
  - 완료 조건 8: `grep -h '"version"' …` → 두 줄 모두 `"version": "0.9.0",`. 통과
  - 완료 조건 9: `logs/tdd-plan-1.jsonl`, `-2.jsonl`의 마지막 답글을 읽음 → 1턴은 논의할지만 묻고 후보가 없다, 2턴은 후보 다섯을 선택지로 낸다. `ls ~/plate-rail-test/tdd-plan/docs/tasks/002-*/phase-*.md` → `phase-1.md` 하나. `grep -L '^\*\*테스트 먼저\*\*: ' …` → 출력 없음. 답 파일의 고른 2번은 `phase-1.md` TODO 3번째 항목에, 뺀 1, 3, 4, 5번은 `plan.md` 범위 밖의 네 줄에 있다. `find plugins/plate/skills/plan -newer <가장 오래된 tdd-plan 기록>` → 출력 없음. 통과
  - 완료 조건 10: tdd-run에서 `git show 96d1d52:docs/tasks/002-list-command/phase-1.md` → 40행 `실패: … 2 failed in 0.27s`, 41행 `통과: … 2 passed in 0.03s`가 이 순서로 있다. `.venv/bin/python -m pytest` → `14 passed`. `find plugins/plate/hooks plugins/plate/skills/phase plugins/plate/skills/run -newer ~/plate-rail-test/logs/tdd-run.jsonl` → 출력 없음. 통과
  - 완료 조건 11: `logs/tdd-edit.jsonl` 18행 → `parent_tool_use_id`가 있는 Edit의 `tool_result`가 `is_error: true`이고 "남은 phase가 있는 작업이 없어서 코드 파일을 고치지 않는다 … 계획부터 세운다"를 담는다. `git -C ~/plate-rail-test/tdd-edit status --short` → 출력 없음. `find plugins/plate/hooks -newer ~/plate-rail-test/logs/tdd-edit.jsonl` → 출력 없음. 통과
  - 완료 조건 12: `docs/TOOLS.md`의 Claude Code 절을 읽음 → "훅" 묶음에 세 사실이 2.1.302, 2026-10-17과 함께 있다. 통과
  - 완료 조건 13: `python3 -m unittest discover -s tests` → 마지막 줄 `OK`. 통과

## 계획과 달라진 점
- 완료 조건 9는 "하나를 고르고 하나를 빼서"다. plan이 후보를 다섯 냈고 고르지 않은 후보는 범위 밖에 적는다고 해서, 하나(2번)를 고르고 나머지 넷을 모두 뺐다. 뺀 넷이 모두 범위 밖에 있어 확인은 그대로 돌았다.

## 남은 것
없음

## 하네스에서 걸린 것
- 이 세션이 받은 phase 스킬 본문은 바뀌기 전의 것(계획 네 항목, 테스트 먼저 규칙 없음)이었다. 머리의 결정대로 이 phase에는 테스트 먼저 표시가 없어 걸린 곳은 없었다.
- `python3 -m unittest discover -s tests`를 돌리면 `tests/__pycache__/`가 추적되지 않는 파일로 남는다(`.gitignore`에 없다). 커밋에 넣지 않으려고 지웠다.
- tdd-run의 회고 절과 검증 절에는 테스트 먼저의 실패·통과 출력을 보았다는 글이 없다. 통과일 때는 그 점검을 적을 자리가 양식에 없어서, 기록만으로는 점검했는지 알 수 없다.

## 회고 1: 회고

**확인**
- 머리의 완료 조건 1~13이 모두 참이다.
  - 완료 조건 1: `python3 -m unittest discover -s tests -v` → `Ran 31 tests`, 마지막 줄 `OK`. `tests/test_edit_guard.py`를 읽음 → setup 안 됨(`test_setup_not_done_passes`), 코드 파일 아님(`test_non_code_files_pass`), 남은 phase 없음과 테스트 없는 프로젝트의 막음(`PlanFirstTest`, "계획부터"와 `plate:plan` 단언), 테스트 먼저 막음(`test_blocks_code_without_test_change`, "실패하는 테스트부터" 단언), 커밋되지 않은 테스트 변경·아니오·표시 없음·테스트 없는 프로젝트·테스트 파일 편집의 통과, 세 번째 막음(`test_third_block_of_same_file_says_stop`, "더 시도하지 않는다", "막힘", "까닭", "해결책" 단언)이 있다. 통과
  - 완료 조건 2: 완료 조건 11의 확인 → 아래와 같다. 통과
  - 완료 조건 3: `plugins/plate/skills/plan/SKILL.md`를 읽음 → 5번(80~83행)에 엣지케이스 물음, 후보를 먼저 내지 않는 규칙, 논의할 때와 안 할 때가, 양식(152행)에 테스트 먼저 줄이, 적는 규칙(199~200행)에 다섯 항목과 예/아니오 규칙이 있다. 통과
  - 완료 조건 4: `plugins/plate/skills/phase/SKILL.md`를 읽음 → 2번(44~52행)에 테스트 먼저의 순서와 출력 기록, 훅의 세 번째 막음에 멈추는 규칙이 있다. 통과
  - 완료 조건 5: retro의 3번(60행)과 verify의 3번(61행)을 읽음 → 둘 다 실패·통과 출력을 보고 없으면 "계획"으로 적는다. 통과
  - 완료 조건 6: `grep -rn '네 항목\|항목은 넷' plugins/plate/skills` → 출력 없음. run의 3번(95~97행)과 "고칠 phase를 더한다"(193, 205행)를 읽음 → 있다. 통과
  - 완료 조건 7: `grep -n '도구가 동작을 끊는 장치는 두지 않는다' docs/PRD.md` → 출력 없음. `grep -n '훅은 두지 않는다' docs/ARCHITECTURE.md` → 출력 없음. PRD의 목표(규칙 구간이 기본이고 훅이 더 막는다), 범위 밖(검증 없는 종료를 막는 훅만), 핵심 기능 6~9와 21행의 1.0.0, ARCHITECTURE의 기술 스택·`hooks/`·`tests/`·훅 규칙, ADR-019를 읽음 → 있다. 통과
  - 완료 조건 8: `grep -h '"version"' …` → 두 줄 모두 `"version": "0.9.0",`. 통과
  - 완료 조건 9: `logs/tdd-plan-1.jsonl`의 마지막 답글 → 엣지케이스를 논의할지만 묻고 후보가 없다. `logs/tdd-plan-2.jsonl`의 마지막 답글 → 후보 다섯을 선택지로 낸다. `ls ~/plate-rail-test/tdd-plan/docs/tasks/002-*/phase-*.md` → `phase-1.md` 하나. `grep -L '^\*\*테스트 먼저\*\*: ' …` → 출력 없음. `answers/tdd-plan-3.md`(2번만 넣고 1, 3, 4, 5번은 뺀다)를 견줌 → 2번은 `phase-1.md` TODO 셋째 항목에, 1, 3, 4, 5번은 `plan.md` 범위 밖의 네 줄에 있다. `find plugins/plate/skills/plan -newer <tdd-plan-1.jsonl>` → 출력 없음. 통과
  - 완료 조건 10: tdd-run에서 `git show 96d1d52:docs/tasks/002-list-command/phase-1.md` → "한 일"에 실패 `2 failed in 0.27s`, 통과 `2 passed in 0.03s`가 이 순서로 있다. `logs/tdd-run.jsonl`의 수행 에이전트 호출도 `tests/test_list.py` Write → pytest 실패(종료 코드 1) → `store.py`·`cli.py` Edit → pytest 통과 순서다. `.venv/bin/python -m pytest` → `14 passed`. `find plugins/plate/hooks plugins/plate/skills/phase plugins/plate/skills/run -newer ~/plate-rail-test/logs/tdd-run.jsonl` → 출력 없음. 통과
  - 완료 조건 11: `logs/tdd-edit.jsonl` 18행 → `parent_tool_use_id`가 있는 Edit의 `tool_result`가 `is_error: true`이고 "남은 phase가 있는 작업이 없어서 코드 파일을 고치지 않는다: `booklog/cli.py` / 계획부터 세운다. plate의 plan 스킬(`plate:plan`)로 …"를 담는다. `git -C ~/plate-rail-test/tdd-edit status --short` → 출력 없음. `find plugins/plate/hooks -newer ~/plate-rail-test/logs/tdd-edit.jsonl` → 출력 없음. 통과
  - 완료 조건 12: `docs/TOOLS.md`의 Claude Code 절을 읽음 → 17행에 6단계의 2.1.302(2026-10-17), 66~72행 "훅" 묶음에 세 사실이 있다. 세 기록에 대어 봄 → init 줄의 `plate@inline`, 막은 호출의 `tool_result` 글과 `tool_use_result`의 `Error: `, `permission_decision`, `hook_started`·`hook_response` 줄이 SessionStart에만 있는 것이 적힌 대로다. 통과
  - 완료 조건 13: `python3 -m unittest discover -s tests` → 마지막 줄 `OK`. 통과

**문제**
- 없음

**배운 것**
- 훅이 막은 호출의 `tool_result_meta`는 객체 하나가 아니라 목록이고, 원소마다 그 호출의 `id`와 `permission_decision`을 담는다(`~/plate-rail-test/logs/tdd-edit.jsonl` 18행). `docs/TOOLS.md`의 "훅" 묶음은 `permission_decision`의 값만 적는다.
- 시험 폴더에서 새로 연 헤드리스 세션의 에이전트는 고친 본문을 받았다. `logs/tdd-run.jsonl`에 retro 3번과 verify 3번의 테스트 먼저 기록 점검 문장과 "계획 다섯 항목"이 있다. 이 작업을 실행하는 세션에서 띄운 이 회고의 에이전트는 옛 본문을 받았다(아래 하네스의 문제점).

**하네스의 문제점**
- retro 스킬의 회고 절 양식은 "확인"에 통과 조건의 확인만 두고, 3번의 테스트 먼저 기록 점검은 걸렸을 때만 "문제"에 적는다. 점검이 통과하면 적을 자리가 없다. tdd-run의 회고 1(`2332cb3`의 `phase-1.md`)과 검증 1(`docs/tasks/002-list-command/verify.md`)은 그 점검을 담은 본문을 받았지만(`logs/tdd-run.jsonl`) 실패·통과 출력을 보았다는 글이 없어, 기록만으로는 점검했는지 알 수 없다. phase 기록의 "하네스에서 걸린 것" 셋째 줄과 같다.
- plan 스킬 5번의 "뺀 것은 머리의 범위 밖에 적는다"는 요청이 이미 정한 동작과 겹치는 후보를 말하지 않는다. tdd-plan에서 plan이 낸 후보 3(`booklog.db`가 없는 폴더에서 `책이 없습니다.`와 종료 코드 0)은 요청과 그 계획의 완료 조건 2가 정한 동작이다. 뺀 뒤 범위 밖에 "따로 보는 테스트"로 적혔지만, TODO 넷째 항목의 테스트도 `booklog.db`가 없는 `empty_dir`(`tests/test_search.py`의 픽스처)에서 같은 출력과 종료 코드를 본다(`~/plate-rail-test/tdd-plan/docs/tasks/002-list-command/`). 완료 조건 9의 확인은 뺀 것이 범위 밖에 있는지만 보아 이 겹침을 가리지 못한다.
- 계획의 phase 5 TODO 다섯째 항목과 완료 조건 12는 `docs/TOOLS.md`의 Claude Code 절만 가리킨다. 같은 문서의 "지금 상태" 표(9행, "1단계 … 5단계(검증)의 판정을 여기서 돌렸다")와 머리글 문단(3행, 5단계까지 어떻게 적었는지)은 6단계를 적지 않은 채 남았다.
- 이 회고의 에이전트가 `plate:retro`를 불러 받은 본문은 디스크의 `plugins/plate/skills/retro/SKILL.md`와 달랐다. 낱말과 1번이 "계획 네 항목"이고 3번에 테스트 먼저 기록의 점검이 없다. `docs/LESSONS.md`의 (008-tdd, phase 3)·(phase 4) 줄과 phase 기록의 "하네스에서 걸린 것" 첫 줄(phase 본문)과 같은 일이고, 이 phase에는 테스트 먼저 표시가 없어(머리의 결정) 판정에 영향이 없다.
- 통과 조건의 확인(`python3 -m unittest discover -s tests`)을 돌리면 `tests/__pycache__/`가 추적되지 않는 파일로 생긴다. `docs/LESSONS.md`의 (008-tdd, phase 1)·(phase 4) 줄과 같은 일이고, 이 회고에서도 생겨 지웠다.

**판정**: 통과
