# tasks 끝의 문제를 고친다

## 목표
tasks 끝의 코드 평가와 하네스 eval에서 고치기로 한 것을 모두 고친다.

## 범위 밖
- 코드 평가와 하네스 eval을 다시 하는 것
- plate 자체의 하네스 고칠 거리를 고치는 것. 이슈로 올리고 plate 저장소에서 고친다

## 완료 조건
1. CI 양식의 verdict 단계가 판정 전에 `gh pr diff "$PR" --name-only`를 돌려, diff를 받지 못하는 큰 PR에서는 단계가 실패해 판정 댓글과 닫기가 사라진다. 바뀐 파일 목록을 파일 목록 API(`gh api --paginate repos/$GH_REPO/pulls/$PR/files --jq '.[].filename'` 같은 것)로 받고, 그것도 실패하면 워크플로 경로가 있는 것으로 보고 request로 내린다 (`plugins/plate/skills/setup/SKILL.md:426`)
   - 확인: `plugins/plate/skills/setup/SKILL.md`의 양식 절 verdict 단계를 읽어 바뀐 파일 목록을 `gh pr diff`로 받지 않고, 목록을 받지 못하면 request로 내리는 길이 있다
2. setup의 새 동작(login 읽기, CODEOWNERS 쓰기·건너뛰기)과 양식의 바뀐 파일 목록 단계가 자동 시험이나 시험 저장소 실행으로 확인되지 않았다 (`plugins/plate/skills/setup/SKILL.md:52`, `:87-92`, `:426`)
   - 확인: `docs/TOOLS.md`에 새 절이 있어, 고친 양식의 verdict 단계를 시험 저장소 `werwer748/plate-ci-test`에서 워크플로를 바꾼 PR과 바꾸지 않은 PR로 돌린 결과(PR 번호, 실행 id, 판정)와, setup의 CODEOWNERS 쓰기(없을 때)와 건너뛰기(있을 때)를 `mktemp -d`의 임시 git 저장소에서 setup 2~4번대로 따라 한 결과가 저마다 있다
3. `docs/ARCHITECTURE.md` 명령 절이 커버리지·중복·정적 분석 도구를 두지 않아 코드 평가의 게이트가 늘 측정 못함으로 남는다. 도구를 명령 절에 더하거나, 두지 않는다는 결정과 이유를 `docs/ADR.md`에 적는다 (`docs/ARCHITECTURE.md`, `docs/ADR.md`)
   - 확인: `docs/ARCHITECTURE.md`의 명령 절에 그 도구의 명령이 있거나, `docs/ADR.md`에 두지 않는다는 ADR이 있다. 도구를 더했으면 그 명령을 돌려 오류 없이 끝난다
4. `docs/TOOLS.md`의 "ruleset과 CODEOWNERS로 워크플로 PR의 자동 머지를 막는지 본 것" 절의 장면 4 줄이 PR 번호를 직접 적지 않는다. PR #20을 적는다 (`docs/TOOLS.md`)
   - 확인: 그 절의 장면 4 줄에 `#20`이 있다
5. 같은 절의 "막지 못한 다른 설정"의 근거(PR #12~#17, 422 응답, ruleset JSON)가 세션 scratchpad의 `/private/tmp/claude-501/-Users-hugo-Desktop-harness-plate/02098b8e-c6ca-47f0-9084-5888a2489f05/scratchpad/log/` 아래에만 있다. 그 내용을 `docs/TOOLS.md`의 그 절에 옮겨, 저장소 밖 경로를 가리키지 않게 한다 (`docs/TOOLS.md`)
   - 확인: `grep -n 'scratchpad' docs/TOOLS.md`가 아무것도 내지 않고, 그 절에 PR #12~#17의 결과와 두 422 오류 글이 있다
6. tasks 완료 조건 1, 2, 3, 4, 5가 참이다.
   - 확인: `docs/TOOLS.md`의 새 절을 읽어 다섯 장면이 저마다 PR 번호, 돌린 명령이나 실행 id, 결과, 막혔으면 오류 글을 적었고, ruleset JSON이 있다. 하나라도 없으면 실패
   - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`
   - 확인: `tests/test_verdict.py`를 읽어 세 경우가 저마다 시험에 있다: 워크플로 경로가 든 목록이면 merge가 request가 된다, close는 그대로다, 목록이 없으면 지금과 같다
   - 확인: `tests/test_edit_guard.py`를 읽어 두 경우(처음 쓰기는 통과, 이미 있으면 막음)가 저마다 시험에 있다
   - 확인: `plugins/plate/skills/setup/SKILL.md`의 2번 표, 3번, 4번, 양식 절을 하나씩 읽어 네 곳이 저마다 tasks 완료 조건 4의 것(login 보이기, CODEOWNERS가 없을 때만 쓰기, 쓰지 못하면 넣을 줄 보고, ruleset 거는 법과 한계, verdict 단계가 바뀐 파일 목록을 넘김)을 적는다. 한 곳이라도 없으면 실패
   - 확인: setup 보고의 ruleset JSON이 `docs/TOOLS.md`에 적힌 시험한 JSON과 규칙, 우회 목록, 대상 브랜치에서 같다
   - 확인: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json`의 두 줄이 모두 `0.14.0`
   - 확인: `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
   - 확인: `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `README.md`를 문서마다 따로 읽어, 바뀐 동작과 어긋나는 줄이 없다. 바뀐 동작은 CODEOWNERS와 ruleset, 판정의 워크플로 검사, 편집 훅의 CODEOWNERS 예외다

## 결정
- 없음
