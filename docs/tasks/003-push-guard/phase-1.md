# Phase 1: 푸시 훅

**목표**: 에이전트의 Bash 호출이 기본 브랜치로 푸시하면 plate의 훅이 막는다.

**테스트 먼저**: 예

**읽을 것**
- `plugins/plate/hooks/edit_guard.py` (셋업 판정, git 호출, 종료 코드 2로 막는 꼴)
- `plugins/plate/hooks/hooks.json` (훅을 거는 꼴과 스크립트가 없을 때의 처리)
- `tests/test_edit_guard.py` (훅 테스트의 꼴)
- `docs/TOOLS.md`의 "훅" (종료 코드, stderr가 에이전트에게 가는 꼴, 셸 꼴의 명령)
- `docs/ADR.md`의 ADR-019 (Python 3 표준 라이브러리와 unittest)
- https://code.claude.com/docs/en/hooks (Bash의 PreToolUse가 받는 입력)
- `docs/PRD.md` (목표), `docs/ARCHITECTURE.md` (기술 스택, 디렉터리 구조, 패턴과 규칙의 막는 장치)

**TODO**
- [ ] 푸시 훅의 테스트가 생긴다. 막는 경우(기본 브랜치에 있는 채 대상 없이 하는 push, 기본 브랜치를 가리키는 push, 기본 브랜치를 지우는 push, 이어진 명령과 `git -C` 안의 push)와 막지 않는 경우(다른 브랜치, origin 밖 원격, 셋업 안 된 프로젝트)를 본다 (`tests/`)
- [ ] 푸시 훅이 Bash 호출의 명령을 읽어 기본 브랜치로 가는 push면 종료 코드 2로 막고, 무엇을 왜 막았는지 stderr로 알린다 (`plugins/plate/hooks/` 아래)
- [ ] hooks.json이 Bash의 PreToolUse에 푸시 훅을 건다 (`plugins/plate/hooks/hooks.json`)
- [ ] PRD의 목표와 ARCHITECTURE의 기술 스택, 디렉터리 구조, 막는 장치가 푸시 훅을 적는다 (`docs/PRD.md`, `docs/ARCHITECTURE.md`)

**통과 조건**
- 완료 조건 1, 2, 3, 4가 참이다.
  - 확인: 완료 조건 1, 2, 3, 4의 확인을 모두 돌린다
