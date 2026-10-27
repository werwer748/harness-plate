# Phase 1: 테스트를 더하고 버전과 문서를 맞춘다

**목표**: 두 테스트 파일이 더해지고 BACKLOG 항목이 지워지며, 버전이 0.17.0이 되고 맥락 문서와 README가 맞춰진다.

**테스트 먼저**: 아니오 — 새 테스트 파일을 더할 뿐 기존 코드 파일의 동작을 바꾸지 않는다. 새 테스트가 깨질 때 실패하는지는 통과 조건이 복사본에서 본다

**읽을 것**
- `tests/test_cleanup_skill.py` (스킬 본문의 글을 시험하는 선례)
- `plugins/plate/skills/run/SKILL.md`, `plugins/plate/skills/plan/SKILL.md`, `plugins/plate/skills/phase/SKILL.md`, `plugins/plate/skills/eval/SKILL.md` (앞 task들이 고친 규칙)
- `plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json` (두 매니페스트)
- `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `docs/BACKLOG.md`, `README.md` (맥락 문서와 README)

**TODO**
- [x] `tests/test_manifests.py`가 더해진다. 두 매니페스트의 `"version"`이 서로 같은지 본다 (`tests/test_manifests.py`)
- [x] `tests/test_skill_rules.py`가 더해진다. run의 #34·#35·#38·#40·#44, plan의 #37·#41, phase의 #42, eval의 #36이 고친 규칙의 글이 저마다 그 본문의 그 절에 있는지 본다 (`tests/test_skill_rules.py`)
- [x] `docs/BACKLOG.md`의 항목이 지워지고 `# BACKLOG` 줄만 남는다 (`docs/BACKLOG.md`)
- [x] 두 매니페스트의 버전이 0.17.0으로 바뀐다 (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)
- [x] `docs/ARCHITECTURE.md`의 "디렉터리 구조"의 `tests/` 아래에 두 테스트 파일이 저마다 한 줄로 더해지고, 다섯 문서 가운데 이 tasks가 바꾼 동작과 어긋나는 줄이 그 동작을 담게 바뀐다 (`docs/ARCHITECTURE.md`, `docs/PRD.md`, `docs/ADR.md`, `docs/TOOLS.md`, `README.md`)

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건 1~4의 확인을 모두 돌린다

## 한 일
- `tests/test_manifests.py`가 더해진다: 두 매니페스트의 `"version"`이 `X.Y.Z` 꼴인지와 서로 같은지를 본다 (`tests/test_manifests.py`)
- `tests/test_skill_rules.py`가 더해진다: run의 `1. 시작 조건을 본다`(#40), `7. task 회고를 맡긴다`(#44), `8. 고칠 phase를 더한다`와 `멈춘다`(#38), `tasks 끝`과 `` `RUNLOG.md` ``(#34·#35·#44), plan의 `6. 초안을 보여 주고 승인받는다`와 `적는 규칙`의 **조건**(#37)·**TODO**(#41), phase의 `1. 읽는다`(#42), eval의 `2. 실패를 모아 MAST 유형으로 나눈다`(#36)에서 고친 규칙의 글이 그 절에 있는지 본다. 절은 코드 블록(백틱 셋 이상) 안의 `## `을 건너뛰고 자른다 (`tests/test_skill_rules.py`)
- `docs/BACKLOG.md`의 항목이 지워지고 `# BACKLOG` 줄만 남는다 (`docs/BACKLOG.md`)
- 두 매니페스트의 버전이 0.16.0에서 0.17.0으로 바뀐다 (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)
- `docs/ARCHITECTURE.md`의 "디렉터리 구조"의 `tests/` 아래에 `test_manifests.py`와 `test_skill_rules.py`가 저마다 한 줄로 더해진다(`test_cleanup_skill.py` 줄의 `└──`를 `├──`로). 다섯 문서는 앞 task들이 이미 run의 바뀐 동작(시작 권한 물음, `RUNLOG.md` 커밋 자리, 계획을 바꾸는 회고의 멈춤)을 담았고, plan·phase·eval의 바뀐 규칙과 어긋나는 줄은 찾지 못해 다른 줄은 고치지 않았다 (`docs/ARCHITECTURE.md`)

## 확인 결과
- 완료 조건 1: `python3 -m unittest discover -s tests`
  - `python3 -m unittest discover -s tests 2>&1 | tail -1` → `OK`(143개). 통과
  - `mktemp -d`에 `rsync -a --exclude .git --exclude __pycache__`로 복사하고 `.codex-plugin/plugin.json`의 버전만 `0.0.0`으로 바꿔 돌림 → `FAILED (failures=1)`. 통과
  - 복사본마다 하나씩 지우고 돌림: run 7번의 "그 자리에서 `RUNLOG.md`만 한 커밋으로 넣는다(…). 메시지는 `NNN-slug: RUNLOG`다." 글(#44) → `FAILED (failures=1)`, plan 적는 규칙 **조건**의 "갈래마다 그 갈래를 차려 돌리는 확인을 둔다" 줄(#37) → `FAILED (failures=1)`, phase 1번의 "앞 phase의 결과가 필요하면 … 산출물 파일만 읽는다 …" 줄(#42) → `FAILED (failures=1)`, eval 2번의 `` `남은 것:` ``으로 시작하는 줄의 규칙 줄(#36) → `FAILED (failures=1)`. 넷 모두 통과
- 완료 조건 2: `cat docs/BACKLOG.md` → `# BACKLOG` 한 줄뿐. 통과
- 완료 조건 3
  - `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "0.17.0",`. 통과
  - `claude plugin validate . 2>&1 | tail -1` → `✔ Validation passed`. 통과
- 완료 조건 4
  - `docs/ARCHITECTURE.md`의 "디렉터리 구조" `tests/` 아래 → `test_manifests.py`, `test_skill_rules.py`가 저마다 한 줄. 통과
  - `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `README.md`를 문서마다 따로 읽고 `grep`(`앞 phase`, `갈래`, `남은 것`, `읽지 않`, `RUNLOG`, `권한 모드`, `plan 모드`, `phase-N.md만`, `만 읽`, `tests/`, `unittest`, `0.16`)으로 걸리는 줄을 봄 → run의 시작 권한 물음·`RUNLOG.md` 커밋 자리·계획을 바꾸는 회고의 멈춤은 PRD 7, ARCHITECTURE의 run 문단과 흐름, README의 `run` 행이 담고 있다. plan의 갈래마다 확인·앞 phase 산출물 조건, phase의 앞 phase 기록 읽지 않음, eval의 `남은 것:` 줄과 어긋나는 줄은 없다(README의 `plan`·`phase`·`eval` 행과 PRD 3·4·8은 그 세부를 적지 않는다. TOOLS.md 294줄의 "task 머리와 `phase-N.md`만 읽게 해"는 시험 자료로 넣은 글을 옮긴 것이다). 새 테스트 파일과 어긋나는 줄도 없다(ADR-019의 `unittest`와 `tests/`와 맞다). 통과

## 계획과 달라진 점
- 없음

## 남은 것
- `tests/test_skill_rules.py`는 글의 조각이 그 절에 있는지만 본다. 글을 바꿔 쓰면(뜻이 같아도) 실패하고, 글이 남은 채 규칙의 동작이 바뀌는 것은 잡지 못한다
- 다섯 문서는 plan·phase·eval의 이번 규칙을 따로 적지 않는다. 어긋나는 줄이 없어 더하지 않았다

## 하네스에서 걸린 것
- 계획의 읽을 것에 이슈 번호(#34·#35·#38·#40·#44, #37·#41, #42, #36)와 규칙의 대응이 없어, `gh issue view`로 이슈 제목을 보고 `git diff main..HEAD -- plugins/plate/skills`로 고친 글을 찾았다. 앞 phase 기록과 tasks 머리는 읽지 않았다

## 확인 1

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 완료 조건 1: `python3 -m unittest discover -s tests 2>&1 | tail -1` → `OK`(143개). 통과
  - 완료 조건 1: `mktemp -d`에 `rsync -a --exclude .git --exclude __pycache__`로 복사하고 `plugins/plate/.codex-plugin/plugin.json`의 `"version"`만 `0.0.0`으로 바꿔 그 복사본에서 테스트 → `FAILED (failures=1)`. 통과
  - 완료 조건 1: 새 복사본마다 하나씩 지우고 테스트 → run 167줄의 "그 자리에서 `RUNLOG.md`만 한 커밋으로 넣는다(…). 메시지는 `NNN-slug: RUNLOG`다." 글(#44) `FAILED (failures=1)`, plan 236줄 "갈래마다 그 갈래를 차려 돌리는 확인을 둔다" 줄(#37) `FAILED (failures=1)`, phase 37줄 "앞 phase의 결과가 필요하면 … 산출물 파일만 읽는다 …" 줄(#42) `FAILED (failures=1)`, eval 77줄 `` `남은 것:` ``으로 시작하는 줄의 규칙 줄(#36) `FAILED (failures=1)`. 넷 모두 통과
  - 완료 조건 2: `cat docs/BACKLOG.md` → `# BACKLOG` 한 줄뿐. 통과
  - 완료 조건 3: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "0.17.0",`. 통과
  - 완료 조건 3: `claude plugin validate . 2>&1 | tail -1` → `✔ Validation passed`. 통과
  - 완료 조건 4: `docs/ARCHITECTURE.md` "디렉터리 구조"의 `tests/` 아래 → `test_manifests.py`(38줄), `test_skill_rules.py`(39줄)가 저마다 한 줄. 통과
  - 완료 조건 4: `docs/PRD.md`(전문), `docs/ARCHITECTURE.md`(40~104줄과 `grep`), `docs/ADR.md`, `docs/TOOLS.md`, `README.md`를 문서마다 따로 읽고 `grep`(`앞 phase`, `갈래`, `남은 것`, `읽지 않`, `만 읽`, `RUNLOG`, `권한`, `plan 모드`, `tests/`, `unittest`, `phase`)으로 본 줄 → run의 시작 권한 물음·`RUNLOG.md` 커밋 자리·계획을 바꾸는 회고의 멈춤은 PRD 7, ARCHITECTURE 54줄과 데이터 흐름, README 10줄이 담고 있다. plan의 갈래마다 확인·앞 phase 산출물 조건, phase의 앞 phase 기록 읽지 않음, eval의 `남은 것:` 줄과 어긋나는 줄은 없다(README 9·11·15줄, PRD 3·4·8은 그 세부를 적지 않는다. TOOLS.md 294줄은 시험 자료로 넣은 글을 옮긴 것). 새 테스트 파일은 ADR-019(`unittest`, `tests/`)와 맞는다. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 143 tests`, `OK`. 통과

**남은 것**
- `tests/test_skill_rules.py`는 글의 조각이 그 절에 있는지만 본다(바꿔 쓰면 실패하고, 글이 남은 채 동작이 바뀌는 것은 잡지 못한다) → 통과 조건(완료 조건 1)은 글이 빠질 때 실패하는지만 보며 그 동작은 확인에서 맞았다. 걸리지 않는다. 하네스에서 걸린 것

**실패**
- 없음

**하네스에서 걸린 것**
- 남은 것: `tests/test_skill_rules.py`는 글의 조각이 그 절에 있는지만 본다. 글을 바꿔 쓰면(뜻이 같아도) 실패하고, 글이 남은 채 규칙의 동작이 바뀌는 것은 잡지 못한다
- 명령 절의 빌드와 린트가 "없음"이다

**판정**: 통과
