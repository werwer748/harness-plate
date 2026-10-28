# Phase 3: 맥락 문서, 테스트 설명, 버전을 맞춘다

**목표**: ADR, PRD, ARCHITECTURE, 문서 지도, 이 저장소의 BACKLOG, 테스트 모듈 설명이 바뀐 규칙과 맞고 버전이 0.22.0이 된다.

**테스트 먼저**: 아니오 — 문서와 매니페스트의 버전 줄만 바꾼다

**읽을 것**
- `docs/ADR.md` (ADR-020, ADR-024의 꼴)
- `docs/PRD.md` (핵심 기능 8)
- `docs/ARCHITECTURE.md` (디렉터리 구조의 `test_skill_rules.py` 줄, 데이터 흐름의 tasks 끝)
- `AGENTS.md` (문서 지도의 `docs/BACKLOG.md` 행)
- `docs/BACKLOG.md`
- `tests/test_skill_rules.py` (모듈 docstring)
- `plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`
- `docs/TOOLS.md`, `docs/cleanup/2026-10-28.md` (맥락 문서)

**TODO**
- [x] `docs/ADR.md` 끝에 ADR-025가 더해진다. 내용은 task 머리의 결정 "ADR-025의 내용"(결정, 이유, 트레이드오프)이고, ADR-020의 결정에 `ADR-025로 바뀜`이 붙는다 (`docs/ADR.md`)
- [x] PRD 핵심 기능 8의 `plate 자체의 고칠 거리는 GitHub 이슈로 올리고(ADR-020)`가 `문턱을 넘은 plate 자체의 고칠 거리만 GitHub 이슈로 올리고(ADR-025)`로 바뀌고, 넘지 않은 것과 감수한 것이 `docs/BACKLOG.md`로 간다는 것이 같은 문장에 든다 (`docs/PRD.md`)
- [x] ARCHITECTURE 데이터 흐름의 `승인받은 대로 plate 자체의 고칠 거리는 GitHub 이슈로 올리고`가 `문턱을 넘은 plate 자체의 고칠 거리는 GitHub 이슈로 올리고`로 바뀌고, 미룬 하네스 고칠 거리와 감수한 것도 `docs/BACKLOG.md`에 적는다는 것이 든다. `test_skill_rules.py` 줄의 괄호 목록 끝에 `eval 고칠 거리의 처리와 문턱`과 `run 처음 안의 문턱과 BACKLOG 세 절`이 더해진다 (`docs/ARCHITECTURE.md`)
- [x] 문서 지도의 BACKLOG 행이 task 머리의 결정의 행으로 바뀐다 (`AGENTS.md`)
- [x] `docs/BACKLOG.md`가 `# BACKLOG` 아래에 세 절(`## 소스 문제`, `## 하네스 고칠 거리`, `## 감수한 것`)을 가진 빈 꼴이 된다 (`docs/BACKLOG.md`)
- [x] 테스트 모듈 docstring의 eval 목록에 `#74`가 더해진다 (`tests/test_skill_rules.py`)
- [x] 두 매니페스트의 `"version"`이 `0.22.0`이 된다 (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)

**통과 조건**
- 완료 조건 4, 5, 6이 참이다.
  - 확인: 완료 조건 4의 확인을 모두 돌린다
  - 확인: 완료 조건 5의 확인을 모두 돌린다(네 시험 모두)
  - 확인: 완료 조건 6의 확인을 모두 돌린다
- 완료 조건 1, 2, 3의 글이 그대로 있다.
  - 확인: 완료 조건 1, 2, 3의 `grep` 확인을 모두 돌린다(헤드리스 시험은 다시 돌리지 않는다)

## 한 일
- `docs/ADR.md` 끝에 ADR-025: ADR-025(결정, 이유, 트레이드오프)를 task 머리의 결정대로 더하고, ADR-020의 결정의 이슈로 올린다는 문장 끝에 `(ADR-025로 바뀜: 문턱을 넘고 처리가 감수가 아닌 것만 올린다)`를 붙였다 (`docs/ADR.md`)
- PRD 핵심 기능 8: `문턱을 넘은 plate 자체의 고칠 거리만 GitHub 이슈로 올리고(ADR-025), 미룬 소스 문제와 문턱을 넘지 않은 하네스 고칠 거리와 감수한 것은 `docs/BACKLOG.md`에 적는다`로 바꿨다 (`docs/PRD.md`)
- ARCHITECTURE: 데이터 흐름의 줄을 `승인받은 대로 문턱을 넘은 plate 자체의 고칠 거리는 GitHub 이슈로 올리고, 미룬 소스 문제와 미룬 하네스 고칠 거리와 감수한 것은 docs/BACKLOG.md에 적고, …`로 바꾸고, `test_skill_rules.py` 줄의 괄호 목록 끝에 `eval 고칠 거리의 처리와 문턱, run 처음 안의 문턱과 BACKLOG 세 절`을 더했다 (`docs/ARCHITECTURE.md`)
- 문서 지도의 BACKLOG 행: task 머리의 결정의 행으로 바꿨다 (`AGENTS.md`)
- `docs/BACKLOG.md`: `# BACKLOG` 아래에 `## 소스 문제`, `## 하네스 고칠 거리`, `## 감수한 것`의 빈 꼴로 만들었다 (`docs/BACKLOG.md`)
- 테스트 모듈 docstring의 eval 목록에 `#74`: 이미 `eval의 #36·#50·#51·#74`로 들어 있어 고치지 않았다 (`tests/test_skill_rules.py`)
- 두 매니페스트의 `"version"`: `0.21.0`에서 `0.22.0`으로 바꿨다 (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)

## 확인 결과
- 완료 조건 4
  - `grep -cF -e '### ADR-025' docs/ADR.md` → `1`, `grep -cF -e 'ADR-025로 바뀜' docs/ADR.md` → `1`. 통과
  - PRD 옛 글 `grep -cF` → `0`, 새 글 → `1`. 통과
  - ARCHITECTURE 옛 글 `grep -cF` → `0`, 새 글 → `1`. 통과
  - `AGENTS.md`의 새 문서 지도 행 `grep -cF -e` → `1`, 옛 행 → `0`. 통과
  - `grep -cxF -e '## 감수한 것' docs/BACKLOG.md` → `1`, `## 소스 문제` → `1`, `## 하네스 고칠 거리` → `1`. 통과
  - `grep 'test_skill_rules.py' docs/ARCHITECTURE.md`에서 `eval 고칠 거리의 처리와 문턱` → `1`, `run 처음 안의 문턱과 BACKLOG 세 절` → `1`. `sed -n '1,8p' tests/test_skill_rules.py`에 `eval의 #36·#50·#51·#74`가 있다. 통과
- 완료 조건 5
  - `python3 -m unittest discover -s tests` → 마지막 줄 `OK`. 통과
  - 네 시험(새 임시 폴더마다 `plugins`, `tests` 복사, 글 개수 확인 뒤 빈 글로 바꾸고 `python3 -m unittest discover -s tests`): 네 글 모두 사본에 `count= 1`, 출력에 저마다 `FAIL: test_threshold_and_disposition (test_skill_rules.EvalRulesTest`, `FAIL: test_74_untested_lines_not_failures (test_skill_rules.EvalRulesTest`, `FAIL: test_first_proposal_uses_threshold (test_skill_rules.RunRulesTest`, `FAIL: test_backlog_three_sections (test_skill_rules.RunRulesTest`가 있고 마지막 줄 `FAILED (failures=1)`. 통과
- 완료 조건 6
  - `grep -h '"version"' …` → 두 줄 모두 `"version": "0.22.0",`. 통과
  - `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
- 완료 조건 1, 2, 3의 글이 그대로 있다
  - 완료 조건 1의 새 글 여덟 `grep -cF -e … plugins/plate/skills/eval/SKILL.md` → 모두 `1`, 옛 글 → `0`. 통과
  - 완료 조건 2의 글 `grep -cF -e` → `1`. 통과
  - 완료 조건 3의 새 글 열셋 `grep -cF -e … plugins/plate/skills/run/SKILL.md` → 모두 `1`, 세 절 머리 `grep -cxF -e` → 저마다 `1`, 옛 글 셋 → `0`, `grep -cE '^   - BACKLOG로 미룰 것: 소스 문제의 번호$'` → `0`. 통과

## 계획과 달라진 점
- 완료 조건 5의 네 시험은 `mktemp -d`와 `cp -R` 대신 Python의 `tempfile.mkdtemp()`와 `shutil.copytree`로 같은 꼴의 새 사본을 만들어 돌렸다. 대상, 바꾸는 글, 기대는 같다. 네 시험을 한 스크립트로 묶으려고 그랬다
- 테스트 docstring의 `#74`는 이미 있어 고치지 않았다

## 남은 것
- 없음

## 하네스에서 걸린 것
- TODO의 "테스트 모듈 docstring의 eval 목록에 `#74`가 더해진다"는 이미 참이었다(앞 phase가 더한 것으로 보이나 앞 phase 기록은 읽지 않아 확인하지 않았다)

## 확인 1

**통과 조건**
- 완료 조건 4, 5, 6이 참이다.
  - 완료 조건 4: `grep -cF -e '### ADR-025' docs/ADR.md` → `1`, `grep -cF -e 'ADR-025로 바뀜' docs/ADR.md` → `1`; PRD 옛 글 `grep -cF -e` → `0`, 새 글 → `1`; ARCHITECTURE 옛 글 → `0`, 새 글 → `1`; `AGENTS.md`의 새 문서 지도 행 `grep -cF -e` → `1`, 옛 행 → `0`; `grep -cxF -e '## 감수한 것' docs/BACKLOG.md` → `1`, `## 소스 문제` → `1`, `## 하네스 고칠 거리` → `1`; `grep 'test_skill_rules.py' docs/ARCHITECTURE.md | grep -cF -e '…'`로 `eval 고칠 거리의 처리와 문턱` → `1`, `run 처음 안의 문턱과 BACKLOG 세 절` → `1`; `sed -n '1,8p' tests/test_skill_rules.py`에 `eval의 #36·#50·#51·#74`가 있다. 통과
  - 완료 조건 5: `python3 -m unittest discover -s tests` → `Ran 202 tests`, 마지막 줄 `OK`. 통과
  - 완료 조건 5의 네 시험(시험마다 `mktemp -d`에 `cp -R plugins tests`, 글을 빈 글로 바꾸고 사본에서 `python3 -m unittest discover -s tests`): 네 글 모두 사본에 `count=1`, 출력에 저마다 `FAIL: test_threshold_and_disposition (test_skill_rules.EvalRulesTest`, `FAIL: test_74_untested_lines_not_failures (test_skill_rules.EvalRulesTest`, `FAIL: test_first_proposal_uses_threshold (test_skill_rules.RunRulesTest`, `FAIL: test_backlog_three_sections (test_skill_rules.RunRulesTest`가 있고 마지막 줄 `FAILED (failures=1)`. 통과
  - 완료 조건 6: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "0.22.0",`; `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
- 완료 조건 1, 2, 3의 글이 그대로 있다.
  - 완료 조건 1: 새 글 여덟마다 `grep -cF -e '<글>' plugins/plate/skills/eval/SKILL.md` → 모두 `1`, 옛 글 → `0`. 통과
  - 완료 조건 2: `grep -cF -e '<글>' plugins/plate/skills/eval/SKILL.md` → `1`. 통과
  - 완료 조건 3: 새 글 열셋마다 `grep -cF -e '<글>' plugins/plate/skills/run/SKILL.md` → 모두 `1`; 세 절 머리 `grep -cxF -e` → 저마다 `1`; 옛 글 셋 `grep -cF -e` → 모두 `0`; `grep -cE '^   - BACKLOG로 미룰 것: 소스 문제의 번호$' plugins/plate/skills/run/SKILL.md` → `0`. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 202 tests`, `OK`. 통과

**남은 것**
- 없음

**실패**
- 없음

**하네스에서 걸린 것**
- 없음

**판정**: 통과
