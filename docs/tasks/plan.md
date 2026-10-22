# PR과 CI

**이름**: pr-ci

## 요청
011 PR과 CI

## 목표
GitHub 원격이 있는 프로젝트에서는 tasks 끝이 로컬 병합 대신 PR로 간다. CI 워크플로를 둔 프로젝트에서는 CI 에이전트가 PR의 코드를 평가하고, 그 등급에 따라 자동 머지, 머지 요청, 닫기 가운데 하나가 된다. 에이전트가 기본 브랜치로 푸시하면 plate의 훅이 막는다. harness-plate는 공개 저장소가 되고 버전은 0.11.0이 된다.

## 범위 밖
- 사람의 푸시를 막는 것(git pre-push 훅, GitHub 브랜치 보호 규칙)
- harness-plate 저장소에 CI 에이전트를 두는 것. 이 저장소에는 Claude 키를 넣지 않는다
- 하네스 자체의 업데이트 방식(이슈 → 자기 적용 → PR, 결정적 CI, 버전과 릴리스)
- 커밋 이력의 작성자 메일을 바꾸는 것

## 완료 조건
1. CI 워크플로를 둔 저장소에서 PR이 열리면 CI가 PR의 코드를 평가해 평가서를 PR 댓글로 달고, 세 판정 규칙대로 자동 머지, 머지 요청, 닫기 가운데 하나가 된다.
   - 확인: `python3 -m unittest discover -s tests`가 통과하고, 그 가운데 판정 스크립트의 테스트가 세 규칙의 경계를 본다
   - 확인: `docs/tasks/005-publish-verify/done-phase-3.md`의 기록에 적힌 세 장면의 PR마다 `gh pr view <번호> -R werwer748/plate-ci-test --json state,comments`가 자동 머지 장면은 `MERGED`, 머지 요청 장면은 `OPEN`, 닫기 장면은 `CLOSED`를 내고, 셋 모두 평가서 댓글이 있다
   - 확인: 시험 저장소의 기본 브랜치를 새로 받아 그 안의 plate 복사본을 `diff -r <복사본> plugins/plate`로 견주면 아무것도 나오지 않는다
2. GitHub 원격이 있는 프로젝트에서 run이 tasks 끝에 `docs/tasks/`를 비운 뒤 PR을 열지 묻고, 승인하면 tasks 브랜치를 푸시해 기본 브랜치로 가는 PR을 연다. plate의 CI 워크플로가 없으면 로컬 평가서를 PR 댓글로 단다. GitHub 원격이 없으면 지금처럼 합칠지 묻는다.
   - 확인: `docs/tasks/005-publish-verify/`의 `done-phase-2.md`, `done-phase-3.md`, `done-phase-4.md`에 적힌 run 장면의 실행 기록마다 PR을 열지(원격 없는 장면은 합칠지) 묻는 글이 있고, 기록마다 `test <기록> -nt plugins/plate/skills/run/SKILL.md`가 참이다
   - 확인: 그 기록에 적힌 run 장면의 PR마다 `gh pr view <번호> -R werwer748/plate-ci-test --json headRefName,baseRefName,comments`의 머리 브랜치가 `tasks/`로 시작하고 기준 브랜치가 `main`이며, CI 워크플로가 없던 장면의 PR에는 평가서 댓글이 있다
   - 확인: 원격 없는 장면의 시험 폴더에서 `git log --format=%s main`에 그 tasks의 `<이름>: 비움` 커밋이 있다
3. 셋업된 프로젝트에서 에이전트가 기본 브랜치로 푸시하면 plate의 훅이 막는다. 기본 브랜치를 지우는 푸시, 이어진 명령과 `git -C` 안의 push도 막는다. 다른 브랜치나 origin 밖 원격으로의 푸시, 셋업 안 된 프로젝트의 푸시는 막지 않는다.
   - 확인: `python3 -m unittest discover -s tests`가 통과하고, 그 가운데 푸시 훅의 테스트가 이 경우들을 본다
   - 확인: `docs/tasks/005-publish-verify/done-phase-4.md`에 적힌 푸시 훅 장면의 실행 기록에 기본 브랜치로의 `git push`가 훅에 막힌 결과(`is_error`가 `true`)가 있고, `test <기록> -nt <푸시 훅 스크립트>`가 참이다
4. GitHub 원격이 있는 프로젝트에서 setup이 CI 워크플로를 둘지 묻고, 승인하면 워크플로 파일을 쓰고 보고에 시크릿 등록 방법을 적는다.
   - 확인: `docs/tasks/005-publish-verify/done-phase-2.md`에 적힌 setup 장면의 실행 기록에 그 물음과 시크릿 등록 안내가 있고, 그 시험 폴더에 워크플로 파일이 있으며, `test <기록> -nt plugins/plate/skills/setup/SKILL.md`가 참이다
5. harness-plate가 공개 저장소이고 그 마켓플레이스가 유효하다.
   - 확인: `gh repo view werwer748/harness-plate --json visibility -q .visibility`가 `PUBLIC`
   - 확인: `GIT_TERMINAL_PROMPT=0 git -c credential.helper= ls-remote https://github.com/werwer748/harness-plate.git HEAD`가 자격 증명 없이 해시 한 줄을 낸다
   - 확인: `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
6. 맥락 문서, README, 두 매니페스트가 바뀐 동작과 맞고 플러그인 버전이 0.11.0이다.
   - 확인: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json`의 두 줄이 모두 `0.11.0`
   - 확인: `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `README.md`를 읽어 PR, CI 판정, 푸시 훅, 명령 절의 설치 줄, 공개 저장소가 적혀 있고, 옛 동작(GitHub 원격이 있어도 로컬로 합친다, 비공개 저장소)이 남지 않았다

## 결정
- ARCHITECTURE의 run 병합 규칙과 데이터 흐름, PRD의 목표와 ARCHITECTURE의 막는 장치를 바꾸기로 하고 진행한다. 이유: 늘 PR로 가고 기본 브랜치 푸시를 막는 훅을 두기로 이미 정했고, PRD 기능 8도 011에서 PR과 CI를 만든다고 적는다.
- CI의 판정은 셋이다. 자동 머지는 빌드·린트·테스트 통과, 새 줄 커버리지 80% 이상, 신뢰성·보안·유지보수성 A, 모름 없음이 모두 맞을 때다. 닫기는 빌드·린트·테스트 가운데 실패가 있거나 보안이 C 이하일 때다. 그 밖은 평가서로 머지를 요청한다. 이유: 말하지 않음.
- review는 평가만 하고, 판정과 댓글, 머지, 닫기는 워크플로가 판정 스크립트로 한다. 이유: 세 규칙은 숫자와 등급만 보므로 스크립트가 늘 같은 답을 내고, PR 코드에 숨은 지시가 있어도 에이전트에게는 머지 권한이 없다.
- harness-plate를 이번 tasks에서 공개로 돌린다. 이유: 말하지 않음.
- 시험 저장소는 `werwer748/plate-ci-test`다. run 전에 사용자가 비공개로 바꾸고 `CLAUDE_CODE_OAUTH_TOKEN` 시크릿을 등록해 두며, 시험 뒤에도 남긴다. 이유: Claude 키를 넣어야 하고, 시크릿은 사용자만 만들 수 있으며, 뒤의 CI 시험에 다시 쓴다.

## task 목록
- `001-ci-review`: review의 PR 모드가 PR에서 바뀐 코드를 평가해 평가서와 등급 묶음을 내고, 판정 스크립트가 그 등급으로 자동 머지, 머지 요청, 닫기 가운데 하나를 고르며, 명령 절에 설치 줄이 생긴다
- `002-ci-workflow`: setup이 GitHub 원격이 있는 프로젝트에 CI 워크플로를 둘지 묻고, 승인하면 PR마다 review의 PR 모드와 판정 스크립트를 돌리는 워크플로를 쓴다
- `003-push-guard`: 에이전트가 기본 브랜치로 푸시하면 plate의 훅이 막는다
- `004-run-pr`: run이 tasks 끝에 묻고 tasks 브랜치를 푸시해 PR을 열며, CI 워크플로가 없으면 로컬 평가서를 PR 댓글로 단다
- `005-publish-verify`: harness-plate가 공개되고 0.11.0이 되며, 시험 저장소와 시험 폴더에서 PR, CI, 푸시 훅, setup의 물음이 확인된다
