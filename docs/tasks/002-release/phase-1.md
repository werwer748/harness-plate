# Phase 1: 버전을 1.0.0으로 올린다

**목표**: 두 매니페스트가 1.0.0이 되고 PRD의 1.0.0 줄이 낸 것으로 맞는다.

**테스트 먼저**: 아니오 — 매니페스트의 버전 줄과 PRD의 글만 바꾸고 코드의 동작을 바꾸지 않는다. 두 버전이 같은지는 `tests/test_manifests.py`가 이미 본다

**읽을 것**
- `plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json` (`version` 칸)
- `tests/test_manifests.py` (두 버전이 같고 `X.Y.Z` 꼴인지 보는 시험)
- `docs/PRD.md` (핵심 기능 아래의 `9단계까지 만든 뒤 1.0.0을 낸다.` 줄)
- `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `docs/BACKLOG.md`

**TODO**
- [x] 두 매니페스트의 `version`이 `0.22.0`에서 `1.0.0`으로 바뀐다 (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)
- [x] PRD의 `9단계까지 만든 뒤 1.0.0을 낸다.` 줄이 `9단계까지 만들어 1.0.0을 냈다.`로 바뀐다 (`docs/PRD.md`)

**통과 조건**
- 완료 조건 1, 2, 3이 참이다.
  - 확인: `grep -n '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "1.0.0"`
  - 확인: `claude plugin validate plugins/plate` → `Validation passed`
  - 확인: `grep -n '1.0.0' docs/PRD.md` → 핵심 기능 아래의 줄이 `9단계까지 만들어 1.0.0을 냈다`를 적고, `낸다`로 끝나는 옛 줄은 없다
  - 확인: `python3 -m unittest discover -s tests` → 마지막 줄이 `OK`

## 한 일
- 두 매니페스트의 `version`이 `0.22.0`에서 `1.0.0`으로 바뀐다: 두 파일의 3행 `"version": "0.22.0"`을 `"version": "1.0.0"`으로 바꿨다 (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)
- PRD의 `9단계까지 만든 뒤 1.0.0을 낸다.` 줄이 `9단계까지 만들어 1.0.0을 냈다.`로 바뀐다: 21행을 바꿨다 (`docs/PRD.md`)

## 확인 결과
- 완료 조건 1, 2, 3이 참이다.
  - `grep -n '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → `plugins/plate/.codex-plugin/plugin.json:3:  "version": "1.0.0",`, `plugins/plate/.claude-plugin/plugin.json:3:  "version": "1.0.0",`. 통과
  - `claude plugin validate plugins/plate` → 마지막 줄 `✔ Validation passed` (디렉터리 검사의 LICENSE_MISSING 문제와 ICON_MISSING 경고가 함께 나왔으나 결과를 바꾸지 않는다고 출력이 적는다). 통과
  - `grep -n '1.0.0' docs/PRD.md` → `21:9단계까지 만들어 1.0.0을 냈다.` 한 줄뿐이고(핵심 기능 목록 9항 바로 아래), `낸다`로 끝나는 옛 줄은 없다. 통과
  - `python3 -m unittest discover -s tests` → `Ran 275 tests in 23.513s`, 마지막 줄 `OK`. 통과

## 계획과 달라진 점
- 없음

## 남은 것
- `claude plugin validate`가 플러그인 디렉터리 제출 기준으로 LICENSE 없음(LICENSE_MISSING)과 아이콘 없음(ICON_MISSING)을 알린다. 통과 판정에는 영향이 없고 이 phase의 범위 밖이라 손대지 않았다.

## 하네스에서 걸린 것
- 없음

## 확인 1

**통과 조건**
- 완료 조건 1, 2, 3이 참이다.
  - `grep -n '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → `plugins/plate/.codex-plugin/plugin.json:3:  "version": "1.0.0",`, `plugins/plate/.claude-plugin/plugin.json:3:  "version": "1.0.0",`. 통과
  - `claude plugin validate plugins/plate` → 마지막 줄 `✔ Validation passed` (ICON_MISSING 경고와 라이선스 파일 없음 안내가 함께 나왔고, 출력은 이 검사들이 결과를 바꾸지 않는다고 적는다). 통과
  - `grep -n '1.0.0' docs/PRD.md` → `21:9단계까지 만들어 1.0.0을 냈다.` 한 줄뿐이고, `grep -n '낸다' docs/PRD.md`로 본 `낸다`로 끝나는 옛 줄은 없다. 통과
  - `python3 -m unittest discover -s tests` → `Ran 275 tests in 25.429s`, 마지막 줄 `OK`. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 275 tests`, `OK`. 통과

**남은 것**
- `claude plugin validate`가 플러그인 디렉터리 제출 기준으로 LICENSE 없음(LICENSE_MISSING)과 아이콘 없음(ICON_MISSING)을 알린다 → 통과 조건이 보는 동작(`Validation passed`)에 걸리지 않는다. 출력도 이 검사들이 결과를 바꾸지 않는다고 적는다. 하네스에서 걸린 것

**실패**
- 없음

**하네스에서 걸린 것**
- 남은 것: `claude plugin validate`의 디렉터리 제출 기준 검사가 LICENSE 없음과 ICON_MISSING을 알린다. 판정에 넣지 않았다.

**판정**: 통과
