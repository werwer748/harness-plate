# 회고

## 회고 1

**확인**
- 두 매니페스트의 버전이 서로 다르면 실패하는 테스트와, 앞 task들이 고친 규칙(run의 #34·#35·#38·#40·#44, plan의 #37·#41, phase의 #42, eval의 #36)의 글이 본문에서 빠지면 실패하는 테스트가 `tests/`에 있다. 테스트는 표준 라이브러리의 `unittest`로 쓴다(ADR-019)
  - `python3 -m unittest discover -s tests 2>&1 | tail -1` → `Ran 143 tests`, 마지막 줄 `OK`. 통과
  - `mktemp -d`(스크래치 폴더 안)에 `rsync -a --exclude .git --exclude __pycache__`로 복사하고 `plugins/plate/.codex-plugin/plugin.json`의 `"version"`만 `0.0.0`으로 바꿔 그 복사본에서 테스트 → `FAILED (failures=1)`. 통과
  - 새 복사본마다 하나씩 줄을 지우고 테스트: run 167줄(7번의 "그 자리에서 `RUNLOG.md`만 한 커밋으로 넣는다 … 메시지는 `NNN-slug: RUNLOG`다", #44) → `FAILED (failures=1)`, plan 236줄(적는 규칙 **조건**의 "갈래마다 그 갈래를 차려 돌리는 확인을 둔다", #37) → `FAILED (failures=1)`, phase 37줄(1번의 "앞 phase의 결과가 필요하면 계획의 읽을 것에 적힌 산출물 파일만 읽는다 …", #42) → `FAILED (failures=1)`, eval 77줄(2번의 `` `남은 것:` ``으로 시작하는 줄의 규칙, #36) → `FAILED (failures=1)`. 넷 모두 통과
- `docs/BACKLOG.md`의 항목이 지워지고 `# BACKLOG` 줄만 남는다
  - `cat docs/BACKLOG.md` → `# BACKLOG` 한 줄뿐. 통과
- 두 매니페스트의 버전이 0.17.0이고 마켓플레이스가 유효하다
  - `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "0.17.0",`. 통과
  - `claude plugin validate . 2>&1 | tail -1` → `✔ Validation passed`. 통과
- 맥락 문서와 README가 이 tasks가 바꾼 동작과 새 테스트 파일과 맞는다
  - `docs/ARCHITECTURE.md` 25~42줄 → "디렉터리 구조"의 `tests/` 아래에 `test_manifests.py`(38줄), `test_skill_rules.py`(39줄)가 저마다 한 줄. 통과
  - `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `README.md`를 문서마다 따로 `grep`(`RUNLOG`, `권한`, `plan 모드`, `앞 phase`, `갈래`, `남은 것`, `읽지 않`, `만 읽`, `tests/`, `unittest`, `멈춘`, `0.1x.`)으로 걸린 줄을 읽음 → run의 시작 권한 물음·`RUNLOG.md` 커밋 자리·계획을 바꾸는 회고의 멈춤은 PRD 17줄, ARCHITECTURE 54·64·70·71줄, README 10줄이 담고 있고 run 본문과 맞다. plan의 갈래마다 확인·앞 phase 산출물 조건, phase의 앞 phase 기록 읽지 않음, eval의 `남은 것:` 줄은 다섯 문서가 세부를 적지 않고 어긋나는 줄도 없다(PRD 13·14줄, README 9·11줄). TOOLS.md의 걸린 줄은 장면 기록이다. 새 테스트 파일은 ADR-019(ADR 24줄, `unittest`, `tests/`)와 ARCHITECTURE 5·33줄과 맞다. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 143 tests`, `OK`. 통과

**남은 것**
- phase 1: `tests/test_skill_rules.py`는 글의 조각이 그 절에 있는지만 본다. 글을 바꿔 쓰면(뜻이 같아도) 실패하고, 글이 남은 채 규칙의 동작이 바뀌는 것은 잡지 못한다 → 문제 아님 (task 머리와 tasks 머리 완료 조건 1·4가 약속한 것은 글이 빠지면 실패하는 것뿐이고, 그 동작은 이번 회고에서 넷 모두 돌려 맞았다. 동작의 결함이 아닌 한계다)
- phase 1: 다섯 문서는 plan·phase·eval의 이번 규칙을 따로 적지 않는다. 어긋나는 줄이 없어 더하지 않았다 → 문제 아님 (완료 조건 4는 어긋나는 줄이 없는지를 보고, 직접 읽어 어긋나는 줄이 없었다)

**문제**
- 없음

**판정**: 통과
