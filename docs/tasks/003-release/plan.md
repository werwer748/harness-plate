# 0.14.0으로 올리고 README와 맥락 문서를 맞춘다

## 목표
두 매니페스트의 버전이 0.14.0이 된다. README와 `docs/PRD.md`가 CODEOWNERS와 ruleset, 판정의 워크플로 검사, 편집 훅의 CODEOWNERS 예외를 적는다. 이미 CI 워크플로를 둔 프로젝트가 따라 할 안내도 README에 생긴다. 맥락 문서 전체가 바뀐 동작과 맞는다.

## 범위 밖
- 스킬, 훅, 판정 스크립트를 고치는 것
- 시험 저장소를 다시 시험하는 것

## 완료 조건
1. (tasks 완료 조건 5) 두 매니페스트의 버전이 0.14.0이고 마켓플레이스가 유효하며 테스트가 통과한다.
   - 확인: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json`의 두 줄이 모두 `0.14.0`
   - 확인: `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
   - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
2. README가 바뀐 동작과 이미 CI 워크플로를 둔 프로젝트의 안내를 적는다.
   - 확인: `README.md`의 표의 `setup` 행, "CI 워크플로" 절, "훅" 절을 하나씩 읽는다. 세 곳이 저마다 CODEOWNERS와 ruleset, 판정의 워크플로 검사, 편집 훅의 CODEOWNERS 예외 가운데 그 자리에 걸리는 것을 적는다
   - 확인: "CI 워크플로" 절에 이미 워크플로를 둔 프로젝트가 할 세 가지가 저마다 있다: CODEOWNERS 두 줄 넣기, ruleset 걸기, verdict 단계에 `--changed-files` 넘기기
3. (tasks 완료 조건 5) 맥락 문서와 README가 바뀐 동작과 어긋나지 않는다.
   - 확인: `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `README.md`를 문서마다 따로 읽어 어긋나는 줄이 없다. 바뀐 동작은 CODEOWNERS와 ruleset, 판정의 워크플로 검사, 편집 훅의 CODEOWNERS 예외다

## 결정
- 버전은 0.14.0이다. 이유: 동작이 바뀌어 tasks마다 마이너를 올린다
- 이미 CI 워크플로를 둔 프로젝트에는 README로 안내한다. 이유: tasks 머리의 범위 밖
