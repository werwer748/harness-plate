# Phase 4: 맥락 문서와 버전

**목표**: PRD, ARCHITECTURE, ADR이 훅과 6~9단계를 반영하고 두 매니페스트가 0.9.0이다.

**읽을 것**
- `docs/PRD.md` (목표, 핵심 기능, 범위 밖)
- `docs/ARCHITECTURE.md` (기술 스택, 디렉터리 구조, 패턴과 규칙의 "막는 장치" 줄)
- `docs/ADR.md` (항목의 꼴: 결정, 이유, 트레이드오프)
- `plugins/plate/hooks/`, `tests/` (phase 1의 결과)
- `plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`

**TODO**
- [x] PRD의 목표, 범위 밖, 핵심 기능이 완료 조건 7대로 바뀐다 (`docs/PRD.md`)
- [x] ARCHITECTURE의 기술 스택에 Python 3 훅이, 디렉터리 구조에 `plugins/plate/hooks/`와 `tests/`가 들어간다. 패턴과 규칙의 "훅은 두지 않는다"는 바뀐 규칙이 된다: 규칙 구간이 기본이고, 훅은 Claude Code의 구현이며, 세 번 막히면 멈춰 논의한다 (`docs/ARCHITECTURE.md`)
- [x] ADR에 훅 스크립트의 런타임(Python 3 표준 라이브러리) 항목이 생긴다 (`docs/ADR.md`)
- [x] 두 매니페스트의 버전이 0.9.0이 되고 설명에 훅이 들어간다 (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)

**통과 조건**
- 완료 조건 1, 7, 8, 13이 참이다.
  - 확인: 완료 조건 1, 7, 8, 13의 확인을 모두 돌린다

## 한 일
- PRD의 목표, 범위 밖, 핵심 기능이 완료 조건 7대로 바뀐다: 목표의 막는 장치를 "규칙 구간이 기본이고 Claude Code 훅이 테스트 먼저와 계획 없는 편집을 더 막는다"로 바꾸고 "도구가 동작을 끊는 장치는 두지 않는다"를 지웠다. 핵심 기능에 6(TDD와 엣지케이스, 6단계에서 만들었다), 7(자동 사이클), 8(푸시 전 평가), 9(정리·리팩터링)와 "9단계까지 만든 뒤 1.0.0을 낸다"를 더했다. 범위 밖의 훅 줄을 "검증 없는 종료를 막는 훅. v1.0 뒤에 한다"로 줄였다 (`docs/PRD.md`)
- ARCHITECTURE의 기술 스택, 디렉터리 구조, 패턴과 규칙: 기술 스택의 "코드가 없다" 줄을 스킬·매니페스트·Claude Code 훅으로 바꾸고, 훅 스크립트는 Python 3 표준 라이브러리와 `unittest`라는 줄(ADR-019, 2026-10-17 Python 3.13.2)을 더했다. 디렉터리 구조에 `plugins/plate/hooks/`(`hooks.json`, `edit_guard.py`)와 `tests/`를 넣었다. 막는 장치 줄의 "훅은 두지 않는다"를 지우고, 규칙 구간이 기본이며 훅은 Claude Code의 구현으로 파일 편집 도구의 호출만 보고 두 경우를 막고, 같은 파일을 테스트 먼저 때문에 세 번 막으면 멈춰 까닭과 해결책을 논의하며 끄는 스위치는 두지 않는다고 적었다. 이유도 그에 맞게 바꿨다 (`docs/ARCHITECTURE.md`)
- ADR에 훅 스크립트의 런타임 항목: ADR-019 "훅 스크립트는 Python 3 표준 라이브러리로 쓴다"를 더했다. 결정, 이유(계획의 결정 그대로), 트레이드오프(`python3`가 없는 환경에서는 훅이 돌지 않고 규칙 구간만 남는다) (`docs/ADR.md`)
- 두 매니페스트: 버전을 0.8.1에서 0.9.0으로 올리고 설명 끝에 "Claude Code에서는 계획 없는 코드 편집과, 테스트 먼저인 phase에서 테스트보다 앞선 구현을 막는 훅이 함께 돈다."를 더했다 (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)

## 확인 결과
- 완료 조건 1, 7, 8, 13이 참이다.
  - 완료 조건 1: `python3 -m unittest discover -s tests -v` → `Ran 31 tests`, 마지막 줄 `OK`. 통과
  - 완료 조건 1: `tests/test_edit_guard.py`를 읽음 → 경우마다 테스트가 있다. setup 안 됨 통과(`test_setup_not_done_passes`), 코드 파일이 아닌 파일 통과(`test_non_code_files_pass`), 남은 phase 없음 막음과 "계획부터"·`plate:plan`(`test_no_remaining_phase_blocks_code_file`), 테스트 없는 프로젝트에서도 같음(`test_no_remaining_phase_blocks_in_project_without_tests`), 테스트 먼저 "예"이고 테스트 변경 없음 막음과 "실패하는 테스트부터"(`test_blocks_code_without_test_change`), 커밋되지 않은 테스트 변경 통과(`test_modified_test_file_passes`, `test_new_untracked_test_file_passes`, `test_staged_test_file_passes`), "아니오" 통과(`test_marker_no_passes`), 표시 없음 통과(`test_no_marker_passes`), 테스트 없는 프로젝트 통과(`test_project_without_tests_passes`), 테스트 파일 편집 통과(`test_editing_test_file_passes`), 세 번째 막음에 "더 시도하지 않는다"·"막힘"·"까닭"·"해결책"(`test_third_block_of_same_file_says_stop`)과 계획이 바뀌면 다시 셈(`test_plan_change_resets_count`). 통과
  - 완료 조건 7: `grep -n '도구가 동작을 끊는 장치는 두지 않는다' docs/PRD.md` → 출력 없음(종료 코드 1). 통과
  - 완료 조건 7: `grep -n '훅은 두지 않는다' docs/ARCHITECTURE.md` → 출력 없음(종료 코드 1). 통과
  - 완료 조건 7: `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`를 읽음 → PRD 목표에 "규칙 구간이 기본이고 Claude Code 훅이 테스트 먼저와 계획 없는 편집을 더 막는다", 범위 밖의 훅 줄은 검증 없는 종료를 막는 훅만 v1.0 뒤, 핵심 기능에 6(만들었다)·7~9·1.0.0이 있다. ARCHITECTURE의 기술 스택에 Python 3 훅, 디렉터리 구조에 `plugins/plate/hooks/`와 `tests/`, 패턴과 규칙에 바뀐 훅 규칙이 있다. ADR에 ADR-019(훅 스크립트의 런타임)가 있다. 통과
  - 완료 조건 8: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `  "version": "0.9.0",`. 통과
  - 완료 조건 13: `python3 -m unittest discover -s tests` → 마지막 줄 `OK`. 통과

## 계획과 달라진 점
없음

## 남은 것
없음

## 하네스에서 걸린 것
- ADR 항목의 번호와 트레이드오프가 계획에 없다. 번호는 context 스킬의 "ADR 번호는 있는 번호 뒤에 잇는다"를 따라 ADR-019로 했다(지금 남은 번호는 004, 005, 018이고, 019~033은 예전에 쓰였다가 커밋 `9b0dfb6`에서 지워졌다). 트레이드오프는 결정에서 바로 나오는 사실(`python3`가 없으면 훅이 돌지 않는다)만 적었다.
- 통과 조건의 확인(`python3 -m unittest discover -s tests`)을 돌리면 `tests/__pycache__/`가 커밋되지 않은 파일로 생긴다. 레포에 `.gitignore`가 없다. 이 phase에서 생긴 것이라 지우고 커밋에 넣지 않았다.

## 회고 1: 회고

**확인**
- 완료 조건 1, 7, 8, 13이 참이다.
  - 완료 조건 1: `python3 -m unittest discover -s tests -v` → `Ran 31 tests`, 마지막 줄 `OK`. 통과
  - 완료 조건 1: `tests/test_edit_guard.py`를 읽음 → 경우마다 상황을 만들고 종료 코드(2 막음, 0 통과)와 stderr의 글을 단언한다. setup 안 됨(`test_setup_not_done_passes`), 코드 파일이 아님(`test_non_code_files_pass`), 남은 phase 없음에 "계획부터"·`plate:plan`(`test_no_remaining_phase_blocks_code_file`), 테스트 없는 프로젝트에서도 같음(`test_no_remaining_phase_blocks_in_project_without_tests`), 테스트 먼저 "예"이고 테스트 변경 없음에 "실패하는 테스트부터"(`test_blocks_code_without_test_change`), 커밋되지 않은 테스트 변경(`test_modified_test_file_passes`, `test_new_untracked_test_file_passes`, `test_staged_test_file_passes`), "아니오"(`test_marker_no_passes`), 표시 없음(`test_no_marker_passes`), 테스트 없는 프로젝트(`test_project_without_tests_passes`), 테스트 파일 편집(`test_editing_test_file_passes`), 세 번째 막음에 "더 시도하지 않는다"·"막힘"·"까닭"·"해결책"·`phase-1.md`(`test_third_block_of_same_file_says_stop`). 통과
  - 완료 조건 7: `grep -n '도구가 동작을 끊는 장치는 두지 않는다' docs/PRD.md` → 출력 없음(종료 코드 1). 통과
  - 완료 조건 7: `grep -n '훅은 두지 않는다' docs/ARCHITECTURE.md` → 출력 없음(종료 코드 1). 통과
  - 완료 조건 7: `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`를 읽음 → PRD 목표에 "규칙 구간이 기본이고 Claude Code 훅이 테스트 먼저와 계획 없는 편집을 더 막는다"가 있고 옛 문장은 없다. 범위 밖의 훅 줄은 "검증 없는 종료를 막는 훅. v1.0 뒤에 한다"뿐이다. 핵심 기능에 6(6단계에서 만들었다), 7~9, "9단계까지 만든 뒤 1.0.0을 낸다"가 있다. ARCHITECTURE의 기술 스택에 Python 3 훅(ADR-019), 디렉터리 구조에 `plugins/plate/hooks/`(`hooks.json`, `edit_guard.py`)와 `tests/`, 패턴과 규칙의 막는 장치 줄에 바뀐 훅 규칙이 있다. ADR에 ADR-019(훅 스크립트의 런타임)가 결정·이유·트레이드오프로 있다. 통과
  - 완료 조건 8: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `  "version": "0.9.0",`. 통과
  - 완료 조건 13: `python3 -m unittest discover -s tests` → `Ran 31 tests`, 마지막 줄 `OK`. 통과

**문제**
- 없음

**배운 것**
- 없음

**하네스의 문제점**
- 계획의 phase 4 TODO 3("ADR에 훅 스크립트의 런타임(Python 3 표준 라이브러리) 항목이 생긴다")과 그 근거인 머리의 결정은 ADR 항목의 번호와 트레이드오프를 정하지 않아 수행이 둘 다 정했다. 번호는 phase 기록에 적힌 context 스킬의 규칙("있는 번호 뒤에 잇는다")대로 ADR-019인데, 이 번호는 커밋 `9b0dfb6`에서 지운 옛 ADR-019("2단계의 완성 판정과 시험 폴더")와 겹친다. `git log --oneline -S'ADR-019' -- docs`에 `9b0dfb6` 전의 커밋이 여럿 나오고, 그 커밋들의 ADR-019는 지금의 ADR-019와 다른 결정이다. 트레이드오프("`python3`가 없는 환경에서는 훅이 돌지 않고 규칙 구간만 남는다")는 확인되지 않았다. 이 회고에서 `env PATH=/nonexistent /bin/sh -c 'python3 /x'`는 종료 코드 127(막는 코드 2가 아님)이었지만, Claude Code가 그 종료 코드를 통과로 다루는지는 `docs/TOOLS.md`에 없고 이 회고에서 보지 않았다.
- 통과 조건의 확인(`python3 -m unittest discover -s tests`)을 돌리면 `tests/__pycache__/`가 추적되지 않는 파일로 생긴다(phase 기록의 "하네스에서 걸린 것"). `docs/LESSONS.md`의 (008-tdd, phase 1) 줄과 같은 일이고, 이 회고에서도 생겨 지웠다.
- 이 회고가 `plate:retro`를 불러 받은 본문은 디스크의 `plugins/plate/skills/retro/SKILL.md`와 달랐다. 받은 본문은 낱말이 "계획 네 항목"이고 3번에 테스트 먼저 기록의 점검이 없다. 디스크의 글은 26행이 "계획 다섯 항목", 60행이 그 점검이다. `docs/LESSONS.md`의 (008-tdd, phase 3) 줄과 같은 일이고, 이 phase에는 테스트 먼저 표시가 없어 판정에 영향이 없다.

**판정**: 통과
