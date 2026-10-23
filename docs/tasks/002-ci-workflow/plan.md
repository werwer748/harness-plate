# CI 워크플로

## 목표
GitHub 원격이 있는 프로젝트에서 setup이 CI 워크플로를 둘지 묻는다. 승인하면 워크플로 파일을 쓰고 보고에 시크릿 등록 방법을 적는다. 그 워크플로는 PR이 열리거나 갱신될 때 공개 마켓플레이스에서 plate를 받아 review의 PR 모드로 평가하고, 판정 스크립트의 답대로 평가서 댓글을 달고 자동 머지하거나 PR을 닫는다.

## 범위 밖
- 사용자 대신 시크릿을 등록하거나 GitHub App을 설치하는 것
- 워크플로를 GitHub에서 실제로 돌려 보는 것. `005-publish-verify`에서 한다
- harness-plate를 공개로 돌리는 것. `005-publish-verify`에서 한다

## 완료 조건
1. setup의 승인 표에 "GitHub 원격이 있고 plate 워크플로가 없다 → CI 에이전트를 둘지"가 있다. 승인하면 setup 본문의 양식대로 워크플로 파일을 쓰고, 보고에 `CLAUDE_CODE_OAUTH_TOKEN` 시크릿 등록 방법이 있다. 거절하거나 GitHub 원격이 없으면 워크플로를 쓰지 않는다.
   - 확인: `plugins/plate/skills/setup/SKILL.md`의 1번(판정), 2번(승인 표), 3번(쓰는 일), 4번(보고), 양식 절을 읽어 위의 것이 있다
2. 워크플로 양식은 PR이 열리거나 갱신될 때 돈다. `https://github.com/werwer748/harness-plate.git` 마켓플레이스에서 토큰 없이 `plate@harness-plate`를 받아 review의 PR 모드를 부르고, 등급 묶음을 구조화 출력으로 받는다. 다음 단계가 판정 스크립트를 돌려 평가서를 PR 댓글로 달고, 자동 머지면 merge commit으로 합치고 머리 브랜치를 지우며, 닫기면 PR을 닫는다. review 단계에는 저장소와 PR의 쓰기 권한을 주지 않는다.
   - 확인: setup/SKILL.md의 워크플로 양식을 읽어 트리거, 마켓플레이스와 플러그인 줄, prompt, `--json-schema`, 판정 단계, 단계마다의 permissions에 위의 것이 있다
   - 확인: 양식이 부르는 판정 스크립트의 경로와 입력의 꼴을 `001-ci-review`가 만든 판정 스크립트(`docs/ARCHITECTURE.md`의 디렉터리 구조에 있다)와 견주어 같다
3. `docs/ARCHITECTURE.md`가 setup이 CI 워크플로를 쓰는 것과 PR의 CI 흐름을 적고, `docs/ADR.md`에 ADR-021이 있다.
   - 확인: `docs/ARCHITECTURE.md`의 디렉터리 구조, 패턴과 규칙, 데이터 흐름과 `docs/ADR.md`의 ADR-021을 읽는다

## 결정
- review는 평가만 하고, 판정과 댓글, 머지, 닫기는 워크플로가 판정 스크립트로 한다. 이유: 세 규칙은 숫자와 등급만 보므로 스크립트가 늘 같은 답을 내고, PR 코드에 숨은 지시가 있어도 에이전트에게는 머지 권한이 없다.
- 워크플로는 토큰 없이 공개 마켓플레이스에서 plate를 받는다. harness-plate는 `005-publish-verify`에서 공개로 돌린다. 이유: 말하지 않음.
- 자동 머지는 squash하지 않고 merge commit으로 합친다. 이유: run이 tasks 브랜치를 squash 없이 합치는 것과 같게 phase의 근거를 이력에 남긴다.
- 편집 훅은 아직 없는 `.github/workflows/plate-review.yml`의 Write를 남은 phase가 있든 없든, 테스트 먼저든 아니든 막지 않는다. 이미 있는 그 파일의 편집과 다른 워크플로 파일은 지금처럼 막는다. 이유: setup은 승인받으면 언제든 이 파일을 써야 하고(목표), 이 파일은 plate가 깔아 주는 양식이라 테스트를 먼저 쓸 구현 코드가 아니다. 회고 1~3이 이 예외의 범위를 두고 오갔다.
