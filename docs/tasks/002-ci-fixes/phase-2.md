# Phase 2: 등급 묶음의 꼴 세 곳을 견주는 테스트

**목표**: 유지보수성-1이 고쳐져, 등급 묶음의 꼴이 세 곳에서 같은지 테스트가 본다.

**테스트 먼저**: 아니오 — 테스트만 더하고 코드의 동작을 바꾸지 않는다

**읽을 것**
- `docs/cleanup/2026-10-29.md` (유지보수성-1의 근거와 고치는 방향)
- `plugins/plate/skills/setup/SKILL.md`의 CI 워크플로 양식의 `--json-schema` 줄
- `plugins/plate/skills/review/SKILL.md`의 PR 모드 절의 등급 묶음 표
- `plugins/plate/ci/verdict.py` (`COMMANDS`, `GRADES`, docstring의 값)
- `tests/test_verdict.py`

**TODO**
- [ ] `BundleShapeTest`가 더해진다: setup 양식에서 `--json-schema`의 JSON을 뽑아 키와 열거를 얻고, review 표의 키와 값, `verdict.py`의 `COMMANDS`·`GRADES`와 견준다. 셋 가운데 하나라도 다르면 실패한다 (`tests/test_verdict.py`)
- [ ] `docs/ARCHITECTURE.md`의 디렉터리 구조의 `test_verdict.py` 줄에 등급 묶음의 꼴을 견준다는 것이 더해진다 (`docs/ARCHITECTURE.md`)

**통과 조건**
- 지금 세 곳이 같아 테스트가 통과한다(완료 조건 2).
  - 확인: `python3 -m unittest tests.test_verdict.BundleShapeTest -v` → `OK`
- 한 곳이 어긋나면 실패한다(완료 조건 2).
  - 확인: 작업 트리를 `cp -R`로 `mktemp -d` 사본에 옮기고, 사본의 `plugins/plate/skills/setup/SKILL.md`에서 `"maintainability":{"type":"string","enum":["A","B","C","D","E","unjudged"]}`를 `"maintainability":{"type":"string","enum":["A","B","C","D","E"]}`로 바꿔 사본에서 `python3 -m unittest tests.test_verdict.BundleShapeTest` → 실패(`FAILED`)
- 앞 phase의 동작이 그대로다(완료 조건 1).
  - 확인: `printf 'not json' | python3 plugins/plate/ci/verdict.py; echo "exit=$?"` → `request`, `exit=0`
- 테스트 묶음이 통과한다.
  - 확인: `python3 -m unittest discover -s tests` → 마지막 줄이 `OK`
