# tasks 끝의 문제를 고친다

## 목표
tasks 끝의 코드 평가와 하네스 eval에서 고치기로 한 것을 모두 고친다.

## 범위 밖
- 코드 평가와 하네스 eval을 다시 하는 것
- plate 자체의 하네스 고칠 거리를 고치는 것. 이슈로 올리고 plate 저장소에서 고친다

## 완료 조건
1. 시험 저장소 `main`의 `.plate`가 지금의 `plugins/plate`와 같고, 그 위에서 #11 장면 PR을 다시 돌려 tasks 완료 조건 2가 참이다. `main` 푸시는 푸시 훅이 막으므로 사용자가 한다 (`werwer748/plate-ci-test`, `plugins/plate`)
   - 확인: 완료 조건 2를 이룬 phase의 기록에 적힌 PR로 `gh pr view <번호> -R werwer748/plate-ci-test --json state,comments`가 `MERGED`가 아니고, 평가서 댓글의 첫 줄이 `판정: 자동 머지`가 아니며, 평가서의 신뢰성 등급이 A가 아니다
   - 확인: 그 PR의 CI 로그(`gh run view <실행 id> -R werwer748/plate-ci-test --log`)에 `AGENTS.md`를 되돌리는 단계가 돌아 성공한 줄이 있다
   - 확인: 시험 저장소 `main`의 plate 복사본을 마지막으로 바꾼 커밋의 시각이 그 PR의 CI 실행 시각보다 앞서고, 그 복사본을 `diff -r -x __pycache__`로 `plugins/plate`에 견주면 아무것도 나오지 않는다
2. auto mode에서 이 저장소의 스킬 본문 Edit가 분류기에 막히고 `settings.local.json`의 허용 규칙으로 풀리지 않으며 bypass 모드에서 들어갔다는 것이 날짜와 함께 적히고, 스킬 본문을 고치는 tasks는 run 전에 권한 모드를 정해 두라고 적힌다 (`docs/TOOLS.md`)
   - 확인: `docs/TOOLS.md`의 Claude Code 절을 읽어 그 사실, 날짜, run 전 권한 모드의 안내가 있다
3. 명령 절에 이 프로젝트는 커버리지·중복·보안 검사 도구를 두지 않는다고 적혀 코드 평가가 매번 찾지 않는다 (`docs/ARCHITECTURE.md`)
   - 확인: `docs/ARCHITECTURE.md`의 명령 절을 읽어 그 줄이 있다
4. tasks 완료 조건 1, 3, 4, 5, 6, 7, 8, 9, 10, 11이 참이다.
   - 확인: `plugins/plate/skills/review/SKILL.md`의 PR 모드 절을 읽어, 지침 파일을 기준 브랜치에서 읽는다는 것과 PR이 바꾼 파일의 글을 지시로 따르지 않는다는 것이 둘 다 있다
   - 확인: `plugins/plate/skills/setup/SKILL.md` 양식 절의 워크플로에서 review 잡의 `anthropics/claude-code-action` 단계보다 앞에 `AGENTS.md`를 기준 브랜치의 것으로 되돌리는 단계가 있다. 기준 브랜치에 `AGENTS.md`가 없을 때 PR의 것을 지우는 것도 그 단계에 있다
   - 확인: `docs/ADR.md`의 ADR-021과 `docs/ARCHITECTURE.md`의 CI 문단을 따로 읽어, 둘 다 이 길과 막는 방법을 적는다
   - 확인: `plugins/plate/skills/review/SKILL.md`의 6번 커버리지 줄과 PR 모드의 `coverage` 행을 따로 읽어, 둘 다 20줄 미만이면 측정과 상관없이 보지 않음(`"skipped"`)이 먼저라고 적는다
   - 확인: `grep -c show_full_output plugins/plate/skills/setup/SKILL.md`가 `0`
   - 확인: 완료 조건 4를 이룬 phase의 기록에 적힌 PR의 CI 로그(`gh run view <실행 id> -R werwer748/plate-ci-test --log`)에 오류 줄을 내는 단계의 출력이 있고, 그 출력에 인증 실패를 뜻하는 글(`authenticate`나 `401`)이 있다
   - 확인: `plugins/plate/skills/review/SKILL.md`의 1번을 읽어 그 예외와 "등급의 근거로 쓰지 않는다"가 둘 다 있다
   - 확인: `grep -n -- '--body ' plugins/plate/skills/run/SKILL.md`가 아무것도 내지 않는다
   - 확인: `grep -c -- '--body-file' plugins/plate/skills/run/SKILL.md`가 `4` 이상이고, "PR을 연다" 3·4번과 "이슈를 올린다" 3·4번을 하나씩 읽어 네 곳 모두 `--body-file`이다
   - 확인: `plugins/plate/skills/run/SKILL.md`의 8번 본문과 고칠 phase 양식을 읽어 위의 셋이 하나씩 있다
   - 확인: `plugins/plate/skills/retro/SKILL.md`의 4번이나 적는 규칙에서 고칠 쪽을 적는 규칙과 경계 밖의 꼴을 다루는 규칙을 따로 찾아 둘 다 있다
   - 확인: `plugins/plate/skills/phase/SKILL.md`의 적는 규칙에 아는 부작용과 한계를 "남은 것"에 적는다는 줄이 있다
   - 확인: `plugins/plate/skills/plan/SKILL.md`를 읽어 위의 셋(경계 물음, 절마다의 확인과 대상·경우의 읽는 법, TODO의 맥락 문서 줄과 ADR 내용)을 하나씩 찾는다
   - 확인: `plugins/plate/skills/eval/SKILL.md`의 2번 모으는 곳 표와 그 아래 줄을 읽어 측정 못함의 까닭을 실패에서 빼는 규칙이 있다
   - 확인: `grep -n 'plan: NNN-slug 수정\|phase N 통과' plugins/plate/skills/eval/SKILL.md`가 3번 표의 행을 내고, 낱말 "더한 phase"를 읽어 표와 맞는다
   - 확인: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json`의 두 줄이 모두 `0.12.0`
   - 확인: `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
   - 확인: `python3 -m unittest discover -s tests`가 `OK`
   - 확인: `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `README.md`를 문서마다 따로 읽어, 이 tasks가 바꾼 동작(PR 모드의 지침 파일, 워크플로의 되돌림과 오류 줄 단계, 커버리지 게이트, `--body-file`)과 어긋나는 줄이 없다

## 결정
- 없음
