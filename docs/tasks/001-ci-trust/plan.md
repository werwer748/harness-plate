# CI의 review를 믿을 수 있게 한다

## 목표
review의 PR 모드가 PR이 바꾼 지침 파일이나 코드의 글을 지시로 따르지 않고(#11), 작은 PR의 커버리지 게이트가 한 가지로 정해지며(#12), tasks 끝의 review가 완료 조건 확인에 필요한 기록 줄을 읽는 범위가 정해진다(#14). setup의 워크플로 양식이 review 잡 전에 `AGENTS.md`를 기준 브랜치의 것으로 되돌리고(#11), review 단계가 실패하면 까닭을 로그에 낸다(#13). 두 워크플로 변경은 시험 저장소의 실제 PR로 확인된다.

## 범위 밖
- 판정 스크립트(`plugins/plate/ci/verdict.py`)의 세 규칙을 바꾸는 것
- PR이 워크플로 파일 자체를 바꿔 판정을 건너뛰는 길
- review의 tasks 끝 절차(0~9번) 가운데 1번과 6번 밖을 고치는 것

## 완료 조건
1. tasks 완료 조건 1이 참이다.
   - 확인: `plugins/plate/skills/review/SKILL.md`의 PR 모드 절을 읽어, 지침 파일을 기준 브랜치에서 읽는다는 것과 PR이 바꾼 파일의 글을 지시로 따르지 않는다는 것이 둘 다 있다
   - 확인: `plugins/plate/skills/setup/SKILL.md` 양식 절의 워크플로에서 review 잡의 `anthropics/claude-code-action` 단계보다 앞에 `AGENTS.md`를 기준 브랜치의 것으로 되돌리는 단계가 있다. 기준 브랜치에 `AGENTS.md`가 없을 때 PR의 것을 지우는 것도 그 단계에 있다
   - 확인: `docs/ADR.md`의 ADR-021과 `docs/ARCHITECTURE.md`의 CI 문단을 따로 읽어, 둘 다 이 길과 막는 방법을 적는다
2. tasks 완료 조건 2가 참이다.
   - 확인: `docs/tasks/001-ci-trust/phase-3.md`(통과 뒤에는 `done-phase-3.md`)의 기록에 적힌 #11 장면 PR로 `gh pr view <번호> -R werwer748/plate-ci-test --json state,comments`가 `MERGED`가 아니고, 평가서 댓글의 첫 줄이 `판정: 자동 머지`가 아니며, 평가서의 신뢰성 등급이 A가 아니다
   - 확인: 그 PR의 CI 로그(`gh run view <실행 id> -R werwer748/plate-ci-test --log`)에 `AGENTS.md`를 되돌리는 단계가 돌아 성공한 줄이 있다
   - 확인: 시험 저장소 `main`을 새로 받아 `git log -1 --format=%cI -- .plate`의 시각이 `gh run list -R werwer748/plate-ci-test --json headBranch,createdAt`의 그 PR 실행 시각보다 앞서고, `diff -r -x __pycache__ <받은 폴더>/.plate plugins/plate`가 아무것도 내지 않는다
3. tasks 완료 조건 3이 참이다.
   - 확인: `plugins/plate/skills/review/SKILL.md`의 6번 커버리지 줄과 PR 모드의 `coverage` 행을 따로 읽어, 둘 다 20줄 미만이면 측정과 상관없이 보지 않음(`"skipped"`)이 먼저라고 적는다
4. tasks 완료 조건 4가 참이다.
   - 확인: `grep -c show_full_output plugins/plate/skills/setup/SKILL.md`가 `0`
   - 확인: `docs/tasks/001-ci-trust/phase-3.md`(통과 뒤에는 `done-phase-3.md`)의 기록에 적힌 #13 장면 PR의 CI 로그(`gh run view <실행 id> -R werwer748/plate-ci-test --log`)에 오류 줄을 내는 단계의 출력이 있고, 그 출력에 `authenticate`나 `401`이 있다
5. tasks 완료 조건 5가 참이다.
   - 확인: `plugins/plate/skills/review/SKILL.md`의 1번을 읽어 그 예외와 "등급의 근거로 쓰지 않는다"가 둘 다 있다
6. 시험 장면에서 확인한 도구의 사실이 `docs/TOOLS.md`에 시험 저장소, PR 번호, 실행 id와 함께 적혀 있다.
   - 확인: `docs/TOOLS.md`의 Claude Code 절을 읽어 두 장면(#11, #13)에서 본 것이 PR 번호와 실행 id와 함께 있다

## 결정
- #11은 워크플로에서 `AGENTS.md`를 되돌리는 것과 review 스킬의 글을 둘 다 고친다. 이유: `CLAUDE.md`의 `@AGENTS.md` 임포트로 PR의 `AGENTS.md`가 세션에 자동으로 실려, 스킬 글만으로는 이미 실린 지시를 못 막는다
- 시험은 `werwer748/plate-ci-test`에서 한다. `main`에 이 브랜치의 `plugins/plate` 복사본(`.plate/`)과, 양식에서 plate를 받는 곳만 그 복사본을 `--plugin-dir`로 싣게 바꾼 워크플로를 둔다(`plate@harness-plate`가 든 주석 한 줄도 둔다). 시험 폴더에서 시험 저장소로 푸시하고 브랜치를 만드는 것은 시험 장면의 일이고, phase의 "푸시하지 않는다"는 harness-plate 저장소에 걸린다. 이유: 액션이 실제로 어떻게 도는지 머지 전에 보고, harness-plate에 푸시하지 않고도 고친 본문을 CI에서 돌린다
- run 전에 사용자가 시험 저장소의 시크릿 `CLAUDE_CODE_OAUTH_TOKEN`을 살아 있는 토큰으로 둔다. 잘못된 토큰 장면은 PR의 워크플로에서 토큰 값만 잘못된 글로 바꿔 만든다. 이유: 시크릿은 사용자만 만들 수 있고, 같은 저장소 브랜치의 PR은 PR 쪽 워크플로로 돈다
- 시험 폴더와 실행 기록은 `~/plate-rail-test` 아래에 둔다. 이유: 앞선 판정들이 여기서 했고 스크립트가 있다 (추천안으로 정함)
