# 검증

## 검증 1

**확인**
- 1. 훅이 setup 안 됨, 코드 파일이 아닌 파일, 남은 phase 없음(테스트가 없는 프로젝트 포함), 테스트 먼저 "예"이고 커밋되지 않은 테스트 변경 없음, 통과시키는 경우들, 세 번째 막음의 경우대로 한다.
  - `python3 -m unittest discover -s tests -v` → 31개 모두 `ok`, `Ran 31 tests in 8.278s`, 마지막 줄 `OK`. 통과
  - `tests/test_edit_guard.py`를 읽음 → 경우마다 상황을 만들고 종료 코드(2 막음, 0 통과)와 stderr의 글을 단언한다. setup 안 됨(`test_setup_not_done_passes`), 코드 파일이 아님(`test_non_code_files_pass`), 남은 phase 없음에 "계획부터"·`plate:plan`(`test_no_remaining_phase_blocks_code_file`, `test_finished_task_does_not_count`), 테스트 없는 프로젝트에서도 같음(`test_no_remaining_phase_blocks_in_project_without_tests`), 테스트 먼저 "예"이고 테스트 변경 없음에 "실패하는 테스트부터"(`test_blocks_code_without_test_change`, `test_other_uncommitted_change_does_not_count`, `test_test_change_committed_already_does_not_count`), 커밋되지 않은 테스트 변경(`test_modified_test_file_passes`, `test_new_untracked_test_file_passes`, `test_staged_test_file_passes`), "아니오"(`test_marker_no_passes`), 표시 없음(`test_no_marker_passes`), 테스트 없는 프로젝트(`test_project_without_tests_passes`), 테스트 파일을 고침(`test_editing_test_file_passes`), 세 번째 막음에 "더 시도하지 않는다"·"막힘"·"까닭"·"해결책"(`test_third_block_of_same_file_says_stop`), 파일마다 셈(`test_count_is_per_file`), 계획이 바뀌면 다시 셈(`test_plan_change_resets_count`). 통과
- 2. 플러그인을 켜면 훅이 실리고 서브에이전트의 편집에도 돈다.
  - 완료 조건 11의 확인 → 아래 11과 같다. 통과
- 3. plan 본문의 phase 양식, 적는 규칙, 5번의 엣지케이스 물음.
  - `plugins/plate/skills/plan/SKILL.md`를 읽음 → 152행에 목표 바로 아래 `**테스트 먼저**: {예, 또는 아니오 — 이유}` 줄이 있고 항목이 다섯이다. 199행 "항목은 다섯", 200행에 `**테스트 먼저**: 예` / `**테스트 먼저**: 아니오 — {이유}`의 꼴, 동작을 바꾸는 phase는 "예", "아니오"는 이유를 적고 리팩터링 phase는 기존 테스트가 바꾼 뒤에도 모두 통과한다는 통과 조건을 둔다는 규칙이 있다. 80~83행에 테스트 먼저 "예"인 phase가 있으면 엣지케이스를 논의할지 묻고 후보를 먼저 내지 않는다, 논의하지 않으면 수행 에이전트가 정한다, 논의하면 후보를 선택지로 주거나 더할 케이스를 묻고 고른 것은 TODO에 테스트로, 뺀 것은 머리의 범위 밖에 적는다가 있다. 통과
- 4. phase 본문의 테스트 먼저 순서와 세 번째 막음 멈춤.
  - `plugins/plate/skills/phase/SKILL.md`를 읽음 → 44~50행에 테스트 먼저 "예"이면 테스트를 먼저 쓰고 돌려 실패를 보고, 구현한 뒤 통과를 보고, 두 명령과 출력을 "한 일"에 적는 규칙이, 52행에 훅이 세 번째 막았다고 알리면 더 시도하지 않고 상태 "막힘"으로 까닭과 해결책을 "남은 것"과 "하네스에서 걸린 것"에 적는 규칙이 있다. 통과
- 5. retro와 verify의 3번이 테스트 먼저 기록을 본다.
  - `plugins/plate/skills/retro/SKILL.md` 60행과 `plugins/plate/skills/verify/SKILL.md` 61행을 읽음 → 둘 다 테스트 먼저 "예"인 phase의 기록에 실패 출력과 통과 출력이 이 순서로 있는지 보고 없으면 기준 "계획"으로 적는다. 통과
- 6. 스킬 본문이 계획 다섯 항목에 맞고, run이 세 번째 막음을 논의하고 고칠 phase 양식에 테스트 먼저 줄이 있다.
  - `grep -rn '네 항목\|항목은 넷' plugins/plate/skills` → 출력 없음(종료 코드 1). 통과
  - `plugins/plate/skills/run/SKILL.md`의 3번과 "고칠 phase를 더한다"를 읽음 → 95~97행에 "훅이 테스트 먼저 때문에 세 번째 막음:" 줄이 있으면 선택지 대신 까닭과 해결책을 보여 주고 논의하며, 계획을 바꾸는 해결책이면 안을 승인받아 고쳐 커밋한 뒤 새 에이전트에게 맡기고 아니면 8번으로 멈추는 규칙이, 193행에 테스트 먼저를 정하는 규칙이, 205행 양식의 목표 아래에 `**테스트 먼저**: {예, 또는 아니오 — 이유}` 줄이 있다. 통과
- 7. PRD, ARCHITECTURE, ADR이 바뀐다.
  - `grep -n '도구가 동작을 끊는 장치는 두지 않는다' docs/PRD.md` → 출력 없음(종료 코드 1). 통과
  - `grep -n '훅은 두지 않는다' docs/ARCHITECTURE.md` → 출력 없음(종료 코드 1). 통과
  - `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`를 읽음 → PRD 4행 목표에 "규칙 구간이 기본이고 Claude Code 훅이 테스트 먼저와 계획 없는 편집을 더 막는다", 29행 범위 밖의 훅 줄은 "검증 없는 종료를 막는 훅. v1.0 뒤에 한다"뿐, 16~21행 핵심 기능에 6(6단계에서 만들었다), 7~9, "9단계까지 만든 뒤 1.0.0을 낸다"가 있다. ARCHITECTURE 4~5행 기술 스택에 Claude Code 훅과 Python 3(ADR-019), 16~18행과 27행 디렉터리 구조에 `plugins/plate/hooks/`와 `tests/`, 40행 패턴과 규칙에 바뀐 훅 규칙이 있다. ADR 23~26행에 ADR-019(훅 스크립트의 런타임)가 있다. 통과
- 8. 두 매니페스트의 버전이 0.9.0이다.
  - `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `  "version": "0.9.0",`. 통과
- 9. tdd-plan의 헤드리스 기록이 엣지케이스 물음의 흐름대로다.
  - `~/plate-rail-test/logs/tdd-plan-1.jsonl`과 `-2.jsonl`의 메인 마지막 답글을 읽음 → 1턴은 "이 작업의 엣지케이스를 지금 같이 정할까요?"(논의한다 / 논의하지 않는다)만 묻고 추천안의 이유에도 후보가 없다. 2턴은 후보 다섯을 표의 선택지로 낸다. 통과
  - `ls ~/plate-rail-test/tdd-plan/docs/tasks/002-*/phase-*.md` → `phase-1.md` 하나. `grep -L '^\*\*테스트 먼저\*\*: ' …` → 출력 없음(종료 코드 1). 통과
  - `~/plate-rail-test/answers/tdd-plan-3.md`(2번만 넣고 1, 3, 4, 5번은 뺀다)를 견줌 → 2번(메모가 달린 책도 한 줄)은 `phase-1.md` TODO 셋째 항목에, 1, 3, 4, 5번은 `plan.md` 범위 밖의 네 줄에 있다. 통과
  - `find plugins/plate/skills/plan -newer "$(ls -t ~/plate-rail-test/logs/tdd-plan-*.jsonl | tail -1)"`(가장 오래된 `tdd-plan-1.jsonl`) → 출력 없음. 통과
- 10. tdd-run의 수행 커밋에 실패 출력과 통과 출력이 이 순서로 있다.
  - `~/plate-rail-test/tdd-run`에서 `git show 96d1d52:docs/tasks/002-list-command/phase-1.md` → 40행 실패 `… 2 failed in 0.27s`, 41행 통과 `… 2 passed in 0.03s`가 이 순서로 있다. 통과
  - `~/plate-rail-test/tdd-run`에서 `.venv/bin/python -m pytest` → `14 passed in 0.07s`. 통과
  - `find plugins/plate/hooks plugins/plate/skills/phase plugins/plate/skills/run -newer ~/plate-rail-test/logs/tdd-run.jsonl` → 출력 없음. 통과
- 11. tdd-edit에서 서브에이전트의 편집이 훅에 막혀 계획부터를 알렸고 파일은 그대로다.
  - `~/plate-rail-test/logs/tdd-edit.jsonl`을 읽음 → 17행에 `parent_tool_use_id`가 있는 `booklog/cli.py` Edit, 18행 그 결과가 `is_error: true`이고 "plate: 남은 phase가 있는 작업이 없어서 코드 파일을 고치지 않는다: `booklog/cli.py` / 계획부터 세운다. plate의 plan 스킬(`plate:plan`)로 …"를 담는다. 통과
  - `git -C ~/plate-rail-test/tdd-edit status --short` → 출력 없음. 통과
  - `find plugins/plate/hooks -newer ~/plate-rail-test/logs/tdd-edit.jsonl` → 출력 없음. 통과
- 12. `docs/TOOLS.md`의 Claude Code 절에 훅에서 확인한 세 사실이 날짜·버전과 함께 있다.
  - `docs/TOOLS.md`를 읽음 → 66행 "훅" 묶음의 머리에 2.1.302, 2026-10-17이 있고, 68행 `--plugin-dir`로 실은 플러그인의 훅이 돈다, 69행 서브에이전트의 편집에도 돈다, 70행 막을 때 `tool_result`의 꼴이 있다. 18행의 `tdd-edit.jsonl` 기록과 견주니 적힌 대로다. 통과
- 13. 이 레포의 전체 테스트가 모두 통과한다.
  - `python3 -m unittest discover -s tests` → `Ran 31 tests in 8.304s`, 마지막 줄 `OK`. 통과

**문제**
- 없음

**배운 것**
- 없음

**하네스의 문제점**
- 머리의 결정 "코드 파일은 `.md`가 아니고 `.worktrees/` 아래가 아닌 모든 파일이다"는 setup 스킬 3번이 만드는 `docs/tasks/.gitkeep`을 가리지 않는다. 문서 지도 구간이 이미 있는 `AGENTS.md`와 `docs/tasks/`가 없는 git 프로젝트를 만들고 `docs/tasks/.gitkeep`의 Write를 훅(`plugins/plate/hooks/edit_guard.py`)에 주니 종료 코드 2로 막고 "계획부터 세운다. plate의 plan 스킬(`plate:plan`)로 …"를 냈다. setup 본문은 구간이 이미 있는 프로젝트에서 다시 도는 갈래를 두므로, 그런 프로젝트에서 setup을 다시 돌리면 `.gitkeep`을 파일 편집 도구로 만들 때 막히고 setup에 맞지 않는 안내를 받는다. 첫 셋업은 본문의 순서대로 양식을 `AGENTS.md`보다 먼저 만들면 걸리지 않는다. 이 작업의 헤드리스 시험 셋(tdd-plan, tdd-run, tdd-edit)은 모두 셋업이 된 test-base에서 돌아 setup과 훅이 만나는 곳은 어느 확인도 지나지 않았다.
- 이 검증의 에이전트가 `plate:verify`를 불러 받은 본문은 디스크의 `plugins/plate/skills/verify/SKILL.md`와 달랐다. 받은 본문은 3번에 테스트 먼저 기록의 점검(디스크 61행)이 없고 적는 규칙이 "목표와 결정대로"(디스크 119행은 "목표와 결정, 테스트 먼저대로")다. `docs/LESSONS.md`의 (008-tdd, phase 3)·(phase 4)의 retro 본문과 같은 일이다. 이 작업의 phase 파일(`e6a5f00`)에는 테스트 먼저 표시가 없어(머리의 결정) 그 점검이 걸리지 않으므로 판정은 달라지지 않는다.
- 완료 조건 1과 13의 확인(`python3 -m unittest discover -s tests`)을 돌리면 `tests/__pycache__/test_edit_guard.cpython-313.pyc`가 추적되지 않는 파일로 생긴다. `docs/LESSONS.md`의 (008-tdd, phase 1)·(phase 4) 줄과 같은 일이고, 이 검증에서도 생겨 지웠다.

**판정**: 통과
