# Phase 1: 버전을 올리고 문서를 맞춘다

**목표**: 버전이 0.12.0이고, 매니페스트 설명, README, ARCHITECTURE, ADR, TOOLS가 바뀐 동작과 맞으며, 검증과 테스트가 통과한다.

**테스트 먼저**: 아니오 — 버전 값과 `.md`만 고친다

**읽을 것**
- `docs/tasks/plan.md` (tasks 머리의 목표와 완료 조건)
- `docs/tasks/001-ci-trust/`~`docs/tasks/005-eval-rules/`의 task 머리 (바뀐 동작을 모으려고)
- `plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`
- `README.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`
- `git show e521e80 -- plugins/plate/.claude-plugin/plugin.json docs/TOOLS.md` (0.11.0을 낼 때 바꾼 꼴)

**TODO**
- [x] 두 매니페스트의 `version`을 `0.12.0`으로 올린다 (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)
- [x] 두 매니페스트의 `description`에서 완료 조건 2의 일곱과 어긋나는 글을 고친다. 어긋남이 없으면 그대로 둔다 (같은 두 파일)
- [x] `README.md`에서 바뀐 동작과 어긋나는 줄을 고친다. 특히 "CI 워크플로" 절이 지침 파일 되돌리기와 실패 때 오류 줄을 다루는지 본다 (`README.md`)
- [x] `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`를 하나씩 읽어 001~005가 맞추고 남긴 어긋남을 고친다 (같은 세 파일)
- [x] `docs/TOOLS.md` 17줄 근처의 판정 버전 문단에 `tasks issue-fixes(0.12.0)`의 시험을 돌린 Claude Code 버전과 날짜를 더한다. 버전은 `claude --version`으로, 날짜는 001 phase 3의 기록에서 가져온다 (`docs/TOOLS.md`)

**통과 조건**
- 완료 조건 1이 참이다.
  - 확인: `grep -n '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json`이 두 줄 모두 `"0.12.0"`
  - 확인: `claude plugin validate .`가 오류 없이 끝난다
  - 확인: 네 문서를 하나씩 따로 읽어 문서마다 일곱과 어긋나는 줄이 없다. 문서마다 결과를 적는다
- 완료 조건 2가 참이다.
  - 확인: 두 `description`을 읽어 어긋나는 글이 없다
- 완료 조건 3이 참이다.
  - 확인: `grep -n 'issue-fixes(0.12.0)' docs/TOOLS.md`가 판정 버전 문단에서 한 줄을 낸다
- 테스트가 모두 통과한다.
  - 확인: `python3 -m unittest discover -s tests`가 `OK`

## 한 일
- 두 매니페스트의 `version`을 `0.12.0`으로 올린다: `0.11.0` → `0.12.0` (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)
- 두 매니페스트의 `description`에서 완료 조건 2의 일곱과 어긋나는 글을 고친다: 두 설명은 스킬 아홉, CI 워크플로가 PR 모드 review와 판정 스크립트로 셋 가운데 하나를 고르는 것, 두 훅만 다룬다. 일곱 가운데 다루는 것(PR 모드 review로 평가)과 어긋나는 글이 없어 그대로 뒀다 (같은 두 파일)
- `README.md`에서 바뀐 동작과 어긋나는 줄을 고친다: "CI 워크플로" 절이 되돌리기와 오류 줄을 다루지 않아, 판정 표 앞에 한 문단을 더했다. `review` 잡이 `AGENTS.md`를 기준 브랜치의 것으로 되돌리고(없으면 지운다), PR 모드가 지침 파일을 기준 브랜치에서 읽고 PR이 바꾼 글을 데이터로만 보며, 평가 단계가 실패하면 오류 줄만 로그에 내고 메시지 전부를 내는 입력은 켜지 않으며, 새 줄 20줄 미만은 커버리지를 재든 못 재든 "보지 않음"이라는 것 (`README.md`)
- `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`를 하나씩 읽어 어긋남을 고친다: ARCHITECTURE의 CI 문단은 되돌림, 기준 브랜치의 지침 파일, 오류 줄 단계를 이미 적었고, 자동 머지 조건의 "보지 않음"에 20줄 미만이면 측정과 상관없이 먼저 보지 않음이라는 괄호를 더했다. ADR-021은 되돌림, PR 모드 규칙, 오류 줄(#11, #13)을 이미 적어 고치지 않았다. TOOLS는 날짜를 단 관찰 기록이라 어긋나는 현재 규칙의 줄이 없어 판정 버전 줄만 고쳤다 (`docs/ARCHITECTURE.md`)
- `docs/TOOLS.md` 17줄의 판정 버전 문단에 시험 버전과 날짜를 더한다: `claude --version` → `2.1.310 (Claude Code)`, 날짜는 `docs/tasks/001-ci-trust/done-phase-3.md`의 시험 커밋·실행 시각(2026-10-26)에서 가져와 ", tasks issue-fixes(0.12.0)의 시험은 2.1.310(2026-10-26)"을 더했다 (`docs/TOOLS.md`)

## 확인 결과
- 완료 조건 1: 버전
  - `grep -n '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "0.12.0",`. 통과
- 완료 조건 1: 검증
  - `claude plugin validate .` → `✔ Validation passed`(오류 없음). 통과
- 완료 조건 1: 네 문서를 하나씩
  - `docs/ARCHITECTURE.md` 전체를 읽음 → CI 문단(51줄)과 데이터 흐름(73줄)이 되돌림·기준 브랜치 지침·오류 줄을 적고, 커버리지는 20줄 규칙을 더함. 고칠 phase·회고·eval 줄(62~67줄)은 일곱과 어긋나지 않음. 어긋남 없음. 통과
  - `docs/ADR.md` 전체를 읽음 → ADR-021 트레이드오프가 #11의 두 막음과 #13의 오류 줄을 적음. 다른 ADR은 일곱을 다루지 않음. 어긋남 없음. 통과
  - `docs/TOOLS.md`를 읽음(1~60줄 전체, 나머지는 `grep -n 'show_full_output\|되돌\|20줄\|--body\|고칠 phase\|규칙 준수\|측정 못함\|경계 밖\|남은 것'`으로 걸린 줄) → `--body "$(…)"`(91, 103줄)와 커버리지가 갈린 것(118줄), `show_full_output`(113줄)은 날짜를 단 그때의 관찰이고, 124~128줄이 고친 뒤의 동작을 적음. 어긋남 없음. 통과
  - `README.md` 전체를 읽음 → CI 절에 더한 문단이 되돌림·PR 모드·오류 줄·20줄 규칙을 다루고, 스킬 표와 PR 절은 일곱과 어긋나지 않음. 어긋남 없음. 통과
- 완료 조건 2
  - 두 `plugin.json`의 `description`을 읽음 → 두 글이 같고, CI를 "PR마다 review의 PR 모드로 평가하고 판정 스크립트로 자동 머지, 머지 요청, 닫기 가운데 하나를 고른다"로만 적어 일곱과 어긋나는 글 없음. 통과
- 완료 조건 3
  - `grep -n 'issue-fixes(0.12.0)' docs/TOOLS.md` → `17:` 한 줄(판정 버전 문단). 통과
- 테스트
  - `python3 -m unittest discover -s tests` → `Ran 99 tests in 16.814s` / `OK`. 통과

## 계획과 달라진 점
- 없음

## 남은 것
- `docs/ARCHITECTURE.md` 6줄의 대상 도구 버전(1~3단계의 버전만 적음)은 일곱과 상관없는 옛 글이라 고치지 않았다. 판정 버전은 `docs/TOOLS.md` 17줄에 있다
- TOOLS의 001 phase 3 문단(124줄)에는 CI 쪽 `claude_code_version`이 적혀 있지 않다. 17줄의 2.1.310은 이 Mac의 `claude --version`이다

## 하네스에서 걸린 것
- 계획의 읽을 것 `git show e521e80 -- …`는 머지 커밋이라 diff를 내지 않았다. `git diff e521e80^1 e521e80 -- …`로 봤다
- 시험 버전을 TODO가 가리킨 001 phase 3의 기록에서 찾지 못해(기록에 Claude Code 버전이 없다) `claude --version`만 썼다
