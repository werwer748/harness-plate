# 판정 검사, 훅 예외, setup의 CODEOWNERS와 ruleset 안내를 넣는다

## 목표
판정 스크립트가 워크플로를 바꾼 PR을 자동 머지 대신 머지 요청으로 내리고, 편집 훅이 setup의 첫 CODEOWNERS 쓰기를 막지 않는다. setup이 CODEOWNERS를 쓰고 ruleset을 거는 법을 보고에 적고, 양식 워크플로가 바뀐 파일 목록을 판정 스크립트에 넘긴다. 이 동작을 적은 `docs/ARCHITECTURE.md`의 줄과 `docs/ADR.md`가 맞춰진다.

## 범위 밖
- 버전을 올리는 것과 README, `docs/PRD.md`를 고치는 것. `003-release`가 한다
- setup이 ruleset을 직접 거는 것
- 이미 CI 워크플로를 둔 프로젝트의 파일을 고치는 것

## 완료 조건
1. (tasks 완료 조건 2) 판정 스크립트는 바뀐 파일 목록에 워크플로 경로가 있으면 merge 대신 request를 낸다. close와 request는 그대로이고, 목록을 받지 않으면 지금과 같다.
   - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
   - 확인: `tests/test_verdict.py`를 읽어 세 경우가 저마다 시험에 있다: 워크플로 경로가 든 목록이면 merge가 request가 된다, close는 그대로다, 목록이 없으면 지금과 같다
2. (tasks 완료 조건 3) 편집 훅은 아직 없는 `.github/CODEOWNERS`를 쓰는 것을 막지 않고, 이미 있는 것의 편집은 막는다.
   - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
   - 확인: `tests/test_edit_guard.py`를 읽어 두 경우(처음 쓰기는 통과, 이미 있으면 막음)가 저마다 시험에 있다
3. (tasks 완료 조건 4) setup이 CI 물음에 login을 보여 주고, CODEOWNERS를 결정대로 쓰거나 보고에 적고, ruleset 거는 법을 보고에 적고, 양식 워크플로가 바뀐 파일 목록을 넘긴다.
   - 확인: `plugins/plate/skills/setup/SKILL.md`의 2번 표, 3번, 4번, 양식 절을 하나씩 읽어 네 곳이 저마다 위의 것을 적는다. 한 곳이라도 없으면 실패
   - 확인: setup 4번의 ruleset JSON이 `docs/TOOLS.md`에서 `001-ruleset-probe`가 더한 절의 ruleset JSON과 규칙, 우회 목록, 대상 브랜치에서 같다
4. `docs/ARCHITECTURE.md`와 `docs/ADR.md`가 바뀐 동작과 맞는다.
   - 확인: `docs/ARCHITECTURE.md`의 17·20·23줄(디렉터리 구조), 49줄(막는 장치), 51줄(PR의 CI), 데이터 흐름의 셋업 줄과 verdict 잡 줄을 하나씩 읽어 바뀐 동작과 어긋나지 않는다. 줄 번호는 이 task의 계획 커밋 시점 기준이다
   - 확인: `docs/ADR.md`에 ADR-023이 있고 결정, 이유, 트레이드오프를 적는다

## 결정
- 워크플로 경로는 `.github/workflows/`로 시작하는 경로다. 이유: tasks 머리의 결정과 같다
- 판정 스크립트는 바뀐 파일 목록을 선택 인자 `--changed-files <파일>`(한 줄에 경로 하나)로 받는다. 인자가 없으면 지금처럼 판정한다. 이유: 이미 깔린 워크플로는 인자를 넘기지 않아도 지금처럼 돌고, stdin의 등급 묶음 꼴은 그대로 둔다 (추천안으로 정함)
- CODEOWNERS는 두 줄 `/.github/workflows/ @<login>`, `/.github/CODEOWNERS @<login>`이다. login은 `gh api user`의 login이다. 파일이 이미 있거나 login을 얻지 못하면 쓰지 않고, 넣을 줄을 보고에 적는다. 이유: tasks 머리의 결정과 같다
- ruleset은 대상이 기본 브랜치, PR 필수, 승인 수 0, 코드 소유자 리뷰 필수, 우회 목록에 저장소 관리자(PR로만)다. 실제 JSON은 `001-ruleset-probe`가 `docs/TOOLS.md`에 적은 것을 쓴다. 이유: 시험한 설정만 안내한다
