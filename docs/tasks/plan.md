# 워크플로를 바꾼 PR이 CI 판정을 건너뛰지 못하게 한다

**이름**: workflow-guard

## 요청
GitHub 이슈 #18 "같은 저장소 PR이 워크플로 파일을 바꿔 CI 판정을 건너뛸 수 있다"를 고친다

## 목표
`.github/workflows/`를 바꾸거나 더한 PR은 판정 스크립트가 자동 머지 대신 머지 요청으로 내린다. setup이 쓰는 CODEOWNERS와 사용자가 거는 ruleset은 PR을 연 계정이 코드 소유자가 아니면 그런 PR의 github-actions 머지를 막고, 워크플로가 main에 직접 푸시하는 것은 늘 막는다. PR을 연 계정이 유일한 코드 소유자면 GitHub가 코드 소유자 리뷰를 채운 것으로 봐 막지 못한다. 이 한계와 닫는 법(코드 소유자를 PR을 여는 계정과 다른 쓰기 권한 계정으로 두기)을 setup 보고와 README가 알린다. 이 동작은 시험 저장소에서 확인해 `docs/TOOLS.md`에 남고, 플러그인 버전은 0.14.0이 된다.

## 범위 밖
- setup이 ruleset을 직접 거는 것. 사용자가 건다
- 이미 CI 워크플로를 둔 프로젝트의 파일을 고치는 것. README의 안내로 한다
- fork에서 온 PR
- `pull_request_target`으로 바꾸는 것
- 이슈 #26~#29
- Codex와 Grok Build에서 확인하는 것(ADR-018)
- GitHub 이슈를 닫는 것. PR이 머지된 뒤 사용자가 닫는다

## 완료 조건
1. 시험 저장소 `werwer748/plate-ci-test`에 ruleset과 CODEOWNERS를 건 상태에서 본 다섯 장면의 결과가 `docs/TOOLS.md`에 있다. 장면마다 무엇이 막았는지 가를 수 있게 오류 글을 함께 적고, 쓴 ruleset JSON도 적는다.
   - 장면 1: werwer748이 연, 워크플로를 바꾸지 않은 PR은 github-actions 토큰으로 머지된다
   - 장면 2: 코드 소유자가 아닌 계정(github-actions)이 연, 기존 워크플로를 고친 PR은 그 토큰의 머지가 막힌다
   - 장면 3: PR을 연 계정이 유일한 코드 소유자(werwer748)면, 새 워크플로를 더한 PR이 그 워크플로의 토큰으로 스스로 머지된다(한계)
   - 장면 4: 그 PR의 워크플로가 main에 직접 푸시하는 것은 막힌다
   - 장면 5: 장면 2의 PR을 관리자 우회로 머지하는 것은 된다
   - 확인: `docs/TOOLS.md`의 새 절을 읽어 다섯 장면이 저마다 PR 번호, 돌린 명령이나 실행 id, 결과, 막혔으면 오류 글을 적었고, ruleset JSON이 있다. 하나라도 없으면 실패
2. 판정 스크립트는 넘겨받은 바뀐 파일 목록에 `.github/workflows/` 아래 경로가 있으면 자동 머지 대신 머지 요청을 낸다. 닫기와 머지 요청은 그대로다. 목록을 받지 않으면 지금과 같은 판정을 낸다.
   - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
   - 확인: `tests/test_verdict.py`를 읽어 세 경우가 저마다 시험에 있다: 워크플로 경로가 든 목록이면 merge가 request가 된다, close는 그대로다, 목록이 없으면 지금과 같다
3. 편집 훅은 아직 없는 `.github/CODEOWNERS`를 쓰는 것을 막지 않고, 이미 있는 것의 편집은 다른 코드 파일처럼 막는다.
   - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
   - 확인: `tests/test_edit_guard.py`를 읽어 두 경우(처음 쓰기는 통과, 이미 있으면 막음)가 저마다 시험에 있다
4. setup은 CI 에이전트를 묻는 자리에서 다음을 한다.
   - `gh api user`의 login을 함께 보여 준다.
   - 승인하면 `.github/CODEOWNERS`가 없을 때만 그 파일을 써서 `/.github/workflows/`와 `/.github/CODEOWNERS`를 그 계정에 둔다.
   - 파일이 이미 있거나 login을 얻지 못하면 쓰지 않고, 넣을 줄을 보고에 적는다.
   - 보고에 ruleset을 거는 법을 적는다: gh api 명령과 Settings 경로, 비공개 저장소의 요금제 조건, PR을 연 계정이 유일한 코드 소유자면 막지 못한다는 한계와 닫는 법(코드 소유자를 다른 쓰기 권한 계정으로).
   - 양식 워크플로의 verdict 단계가 PR의 바뀐 파일 목록을 판정 스크립트에 넘긴다.
   - 확인: `plugins/plate/skills/setup/SKILL.md`의 2번 표, 3번, 4번, 양식 절을 하나씩 읽어 네 곳이 저마다 위의 것을 적는다. 한 곳이라도 없으면 실패
   - 확인: setup 보고의 ruleset JSON이 `docs/TOOLS.md`에 적힌 시험한 JSON과 규칙, 우회 목록, 대상 브랜치에서 같다
5. 두 매니페스트의 버전이 0.14.0이고, 마켓플레이스가 유효하고, 테스트가 통과하고, 맥락 문서와 README가 바뀐 동작과 맞는다.
   - 확인: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json`의 두 줄이 모두 `0.14.0`
   - 확인: `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
   - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
   - 확인: `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `README.md`를 문서마다 따로 읽어, 바뀐 동작과 어긋나는 줄이 없다. 바뀐 동작은 CODEOWNERS와 ruleset, 판정의 워크플로 검사, 편집 훅의 CODEOWNERS 예외다

## 결정
- 워크플로를 바꾼 PR은 판정 스크립트의 워크플로 검사가 머지 요청으로 내리고, 저장소 설정(ruleset과 CODEOWNERS)은 PR을 연 계정이 코드 소유자가 아닐 때의 머지와 워크플로의 main 직접 푸시를 막는다. 이유: 시험 저장소에서 PR을 연 계정이 유일한 코드 소유자면 코드 소유자 리뷰 필수가 통과로 매겨졌고(rule suite 4728049352, 4728300432), 개인 저장소는 push ruleset과 file_path_restriction을 걸 수 없어(422) 설정만으로는 그 길을 닫지 못한다. 판정 검사는 PR이 워크플로를 고쳐 건너뛸 수 있어 실수만 막는다
- setup은 CODEOWNERS만 쓰고, ruleset은 보고에 거는 법을 적어 사용자가 건다. 이유: 시크릿 등록을 사용자가 하는 지금 방식(ADR-021)과 같고, 관리자 권한이 드는 일을 에이전트가 하지 않는다
- ruleset의 꼴은 이렇다: 대상은 기본 브랜치, PR 필수, 승인 수 0, 코드 소유자 리뷰 필수, 우회 목록에 저장소 관리자(PR로만). 이유: 개인용 하네스라 다른 승인자가 없고, github-actions는 관리자가 아니라 우회하지 못한다
- CODEOWNERS의 소유자는 `gh api user`의 login이다. 얻지 못하면 쓰지 않고 넣을 줄을 보고에 적는다. 이유: PR을 여는 계정과 같아 관리자 우회 머지와 맞고, 조직 저장소에서도 맞다
- CODEOWNERS는 `/.github/workflows/`와 `/.github/CODEOWNERS`를 소유한다. 이유: CODEOWNERS를 바꾸는 PR도 사람이 머지한다 (추천안으로 정함)
- `.github/CODEOWNERS`가 이미 있으면 setup은 건드리지 않고 넣을 줄을 보고에 적는다. 이유: setup의 절대 규칙 1(승인받지 않은 기존 파일은 덮어쓰지 않는다) (추천안으로 정함)
- 워크플로 검사는 판정 스크립트에 두고, 목록을 받지 않으면 지금처럼 판정한다. 이유: 판정 스크립트는 harness-plate에서 받아 PR이 고치지 못하고 시험할 수 있다. 이미 깔린 워크플로는 목록을 넘기지 않아도 지금처럼 돈다(호환 부분은 추천안으로 정함)
- 동작은 시험 저장소 `werwer748/plate-ci-test`(비공개)에서 확인하고 결과를 `docs/TOOLS.md`에 적는다. 이유: 안내할 설정이 실제로 길을 닫는지 모르는 채로 안내하면 잘못된 안심을 준다
- 시험 준비는 에이전트가 `mktemp -d`의 임시 복제본에서 한다. 브랜치 `probe-setup`에 두 파일을 커밋해 푸시하고 ruleset JSON을 기록에 남긴다. 두 파일은 CODEOWNERS와, PR 번호를 받아 `GITHUB_TOKEN`으로 머지하는 `workflow_dispatch` 머지 시험 워크플로다. 이유: 기본 브랜치 푸시와 저장소 설정은 사람이 하고 나머지는 에이전트가 한다
- 사용자의 단계: `001`의 phase 1이 통과한 뒤 사용자가 `probe-setup`을 시험 저장소의 main에 올리고 ruleset을 건다. 명령은 phase 1의 기록에 있다. phase 2는 둘 중 하나라도 없으면 막힘으로 멈춘다. 이유: 에이전트의 main 푸시는 푸시 훅이 막는다
- 장면의 결과가 기대와 다르면 계획이 틀린 것으로 보고 멈춰 논의한다. 기대와 다른 경우는 완료 조건 1의 장면 가운데 하나라도 적힌 결과와 다른 것, 비공개 저장소라 ruleset을 걸 수 없는 것이다. 이유: 이 tasks의 방식이 그 동작에 기댄다 (추천안으로 정함)
- 버전은 0.14.0이다. 이유: 동작이 바뀌어 tasks마다 마이너를 올린다
- 장면 2·3의 기대를 바꾸고 목표를 판정 검사가 주 장치인 꼴로 고친다. 이유: 001 phase 2와 그 뒤 조사에서, PR을 연 계정이 유일한 코드 소유자면 승인 수 0이든 1이든 github-actions가 워크플로 PR을 머지했다(#11, #13, #16). 코드 소유자가 아닌 계정이 연 PR은 막혔다(#14, "Waiting on code owner review"). 설정으로 닫는 다른 길(push ruleset, file_path_restriction, 쓰기 권한 없는 소유자)은 개인 저장소에서 안 되거나 무시됐다 (001 phase 2의 계획이 틀림에서, 사용자가 미리 정한 대로 해결 에이전트의 추천안으로 정함)
- 장면 2의 PR은 에이전트가 시험 저장소에서만 "GitHub Actions가 PR을 만들고 승인하게 허용"을 잠깐 켜고 github-actions로 연 뒤, 바로 끈다. 이유: 코드 소유자가 아닌 작성자를 만들 계정이 따로 없다
- 계획의 사용자 단계(시험 저장소 main 올리기, ruleset 걸기)는 사용자가 이번 실행에서 정한 대로 에이전트가 `gh api`로 했다(plate-ci-test에 한함). 이유: 사용자가 개입 없이 끝까지 돌리기로 했다

## task 목록
- `001-ruleset-probe`: 시험 저장소에서 ruleset과 CODEOWNERS가 워크플로를 바꾼 PR의 자동 머지를 막는지 확인해 `docs/TOOLS.md`에 남긴다
- `002-guard-setup`: 판정 스크립트의 워크플로 검사, 편집 훅의 CODEOWNERS 예외, setup의 CODEOWNERS와 ruleset 안내가 들어가고 맥락 문서가 맞춰진다
- `003-release`: 버전이 0.14.0이 되고 README와 맥락 문서가 바뀐 동작과 맞는다
