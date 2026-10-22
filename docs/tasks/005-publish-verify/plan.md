# 공개와 시험

## 목표
harness-plate가 공개 저장소가 되고 플러그인 버전이 0.11.0이 되며, 맥락 문서와 README가 바뀐 동작과 맞는다. 시험 저장소와 시험 폴더에서 setup의 CI 물음, run의 PR(CI 워크플로가 없을 때, 있을 때, GitHub 원격이 없을 때), CI의 세 판정, 푸시 훅이 실제로 도는 것이 확인된다.

## 범위 밖
- 0.11.0의 태그나 GitHub 릴리스를 만드는 것. 하네스 자체의 버전과 릴리스 방식은 따로 한다

## 완료 조건
1. harness-plate가 공개 저장소이고 그 마켓플레이스가 유효하다.
   - 확인: `gh repo view werwer748/harness-plate --json visibility -q .visibility`가 `PUBLIC`
   - 확인: `GIT_TERMINAL_PROMPT=0 git -c credential.helper= ls-remote https://github.com/werwer748/harness-plate.git HEAD`가 자격 증명 없이 해시 한 줄을 낸다
   - 확인: `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
2. 두 매니페스트의 버전이 0.11.0이다. `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `README.md`가 PR, CI 판정, 푸시 훅, 명령 절의 설치 줄, 공개 저장소를 적고, `docs/ADR.md`에 ADR-022가 있다.
   - 확인: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json`의 두 줄이 모두 `0.11.0`
   - 확인: `grep -c "^### ADR-022: " docs/ADR.md`가 `1`
   - 확인: 네 문서를 읽어 위의 것이 적혀 있고, 옛 동작(GitHub 원격이 있어도 로컬로 합친다, 비공개 저장소)이 남지 않았다
3. 시험 저장소를 origin으로 둔 시험 폴더에서 setup이 CI 워크플로를 둘지 묻고, 승인하면 워크플로 파일을 쓰고 보고에 시크릿 등록 방법을 적는다. plate 워크플로가 없는 시험 저장소로 run이 tasks 끝에 PR을 열지 묻고, 승인하면 `tasks/`로 시작하는 브랜치에서 `main`으로 가는 PR을 열고 평가서 댓글을 단다.
   - 확인: `docs/tasks/005-publish-verify/done-phase-2.md`에 적힌 setup 장면의 실행 기록에 그 물음과 `CLAUDE_CODE_OAUTH_TOKEN` 시크릿 등록 안내가 있고, 그 시험 폴더의 `.github/workflows/` 아래에 워크플로 파일이 있으며, `test <기록> -nt plugins/plate/skills/setup/SKILL.md`가 참이다
   - 확인: 같은 파일에 적힌 run 장면의 실행 기록에 PR을 열지 묻는 글이 있고, `test <기록> -nt plugins/plate/skills/run/SKILL.md`가 참이다
   - 확인: 그 장면의 PR로 `gh pr view <번호> -R werwer748/plate-ci-test --json headRefName,baseRefName,comments`의 머리 브랜치가 `tasks/`로 시작하고 기준 브랜치가 `main`이며 평가서 댓글이 있다
4. 시험 저장소의 `main`에 plate 복사본과 그것을 `--plugin-dir`로 싣는 CI 워크플로가 있다. CI가 PR마다 평가서를 PR 댓글로 달고 판정대로 하며, 세 판정마다 그 판정이 나오게 바꾼 PR이 하나씩 있다. plate 워크플로가 있는 시험 저장소로 run이 PR을 열면 run은 평가서 댓글을 달지 않고 CI가 단다.
   - 확인: `docs/tasks/005-publish-verify/done-phase-3.md`에 적힌 세 장면의 PR마다 `gh pr view <번호> -R werwer748/plate-ci-test --json state,comments`가 자동 머지 장면은 `MERGED`, 머지 요청 장면은 `OPEN`, 닫기 장면은 `CLOSED`를 내고, 셋 모두 평가서 댓글이 있다
   - 확인: 시험 저장소의 `main`을 새로 받아 그 안의 복사본을 `diff -r <복사본> plugins/plate`로 견주면 아무것도 나오지 않고, 그 `main`에서 복사본을 마지막으로 바꾼 커밋의 시각(`git log -1 --format=%cI -- <복사본>`)이 세 PR의 CI 실행 시각(`gh run list -R werwer748/plate-ci-test --json headBranch,createdAt`)보다 앞선다
   - 확인: 같은 파일에 적힌 run 장면의 실행 기록에 PR을 열지 묻는 글이 있고, `test <기록> -nt plugins/plate/skills/run/SKILL.md`가 참이다
   - 확인: 그 장면의 PR로 `gh pr view <번호> -R werwer748/plate-ci-test --json headRefName,baseRefName,comments`의 머리 브랜치가 `tasks/`로 시작하고 기준 브랜치가 `main`이며, 댓글 가운데 작성자가 `werwer748`인 것은 없고 CI의 평가서 댓글이 있다
5. GitHub 원격이 없는 시험 폴더에서 run이 tasks 끝에 PR 대신 합칠지 묻고, 승인하면 `main`에 그 tasks의 `<이름>: 비움` 커밋이 들어온다. 셋업된 시험 폴더에서 에이전트가 기본 브랜치로 `git push`하면 푸시 훅이 막는다.
   - 확인: `docs/tasks/005-publish-verify/done-phase-4.md`에 적힌 원격 없는 장면의 실행 기록에 합칠지 묻는 글이 있고, `test <기록> -nt plugins/plate/skills/run/SKILL.md`가 참이며, 그 시험 폴더에서 `git log --format=%s main`에 `<이름>: 비움` 커밋이 있다
   - 확인: 같은 파일에 적힌 푸시 훅 장면의 실행 기록에 기본 브랜치로의 `git push`가 훅에 막힌 결과(`is_error`가 `true`이고 내용에 푸시 훅의 stderr가 있다)가 있고, `test <기록> -nt <푸시 훅 스크립트>`가 참이다

## 결정
- CI의 판정은 셋이다. 자동 머지는 빌드·린트·테스트 통과, 새 줄 커버리지 80% 이상, 신뢰성·보안·유지보수성 A, 모름 없음이 모두 맞을 때다. 닫기는 빌드·린트·테스트 가운데 실패가 있거나 보안이 C 이하일 때다. 그 밖은 평가서로 머지를 요청한다. 이유: 말하지 않음.
- 시험 저장소는 `werwer748/plate-ci-test`다. run 전에 사용자가 비공개로 바꾸고 `CLAUDE_CODE_OAUTH_TOKEN` 시크릿을 등록해 두며, 시험 뒤에도 남긴다. 이유: Claude 키를 넣어야 하고, 시크릿은 사용자만 만들 수 있으며, 뒤의 CI 시험에 다시 쓴다.
- CI는 시험 저장소에 둔 plate 복사본으로 시험한다. 시험 폴더에서 시험 저장소로 푸시하고 브랜치를 만드는 것은 시험 장면의 일이고, 푸시하지 않고 브랜치를 바꾸지 않는 phase의 규칙은 harness-plate 저장소에 걸린다. 이유: harness-plate에 푸시하지 않고도 고친 본문을 CI에서 돌릴 수 있다.
- 시험 폴더와 실행 기록은 `~/plate-rail-test` 아래에 둔다. 이유: 재부팅에 지워지는 `/tmp`가 아니고, 앞선 판정들도 여기서 했다.
