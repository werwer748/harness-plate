# 회고

## 회고 1

**확인**
- 1. CI 양식의 verdict 단계가 바뀐 파일 목록을 `gh pr diff`가 아니라 파일 목록 API로 받고, 받지 못하면 request로 내린다
  - `sed -n 395,450p plugins/plate/skills/setup/SKILL.md`와 `grep -nF "pr diff"` → verdict 단계(426~428줄)가 `gh api --paginate "repos/$GH_REPO/pulls/$PR/files" --jq '.[].filename' > changed-files.txt`로 받고, 실패하면 `echo '.github/workflows/' > changed-files.txt`로 적어 `--changed-files`로 넘긴다. `GH_REPO`는 같은 단계의 env에 있다. `gh pr diff`는 330줄 설명 글("diff가 너무 큰 PR에서 실패한다")에만 있다. 통과
- 2. `docs/TOOLS.md`의 새 절에 시험 저장소의 워크플로를 바꾼 PR·바꾸지 않은 PR 결과와 임시 git 저장소의 CODEOWNERS 쓰기·건너뛰기 결과가 있다
  - "verdict 단계의 바뀐 파일 목록과 setup의 CODEOWNERS를 돌려 본 것" 절을 읽었다 → PR #24(실행 `40431431712`, 머지 요청), PR #25(실행 `40431626685`, 자동 머지), `mktemp -d` 저장소에서 CODEOWNERS 없을 때 두 줄 쓰기, 있을 때(`* @someone-else`) 건너뛰고 보고 줄을 낸 결과가 있다. `gh pr view`/`gh run view`로 시험 저장소를 봤다 → #24 `CLOSED`, 파일 `.github/workflows/merge-probe.yml`, 댓글 `판정: 머지 요청`. #25 `MERGED` by `app/github-actions`, 파일 `textkit/core.py`·`tests/test_core.py`, 댓글 `판정: 자동 머지`. 두 실행 모두 `success`. 통과
- 3. 커버리지·중복·정적 분석 도구를 명령 절에 더하거나 두지 않는다는 ADR이 있다
  - `grep -n "ADR-024" docs/ADR.md docs/ARCHITECTURE.md` → ADR.md 48줄 ADR-024(두지 않음, 결정·이유·트레이드오프), ARCHITECTURE.md 90줄 명령 절의 `(ADR-024)` 참조. 도구를 더하지 않아 돌릴 명령은 없다. 통과
- 4. 장면 4 줄에 `#20`이 있다
  - `grep -n "장면 4" docs/TOOLS.md | grep -c "#20"` → `1`. 통과
- 5. `docs/TOOLS.md`가 scratchpad를 가리키지 않고, 그 절에 PR #12~#17의 결과와 두 422 오류 글이 있다
  - `grep -n scratchpad docs/TOOLS.md` → 출력 없음(rc 1). `| #12 |`~`| #17 |` 표 줄이 저마다 있고(#12·#14는 두 줄), `Source only org-owned repos can have push rules`와 `Invalid rule 'file_path_restriction'`가 저마다 두 번 나온다. 통과
- 6. tasks 완료 조건 1~5가 참이다
  - `docs/TOOLS.md` 152~158줄을 읽었다 → 장면 1~5가 저마다 PR 번호(#18, #19, #20, #20, #19), 명령이나 실행 id, 결과, 막힌 장면(2, 4)의 오류 글을 적었고, 135줄에 시험한 ruleset JSON이 있다. 통과
  - `python3 -m unittest discover -s tests` → `Ran 104 tests in 17.051s`, 마지막 줄 `OK`. 통과
  - `tests/test_verdict.py` 120~142줄 → 워크플로 경로면 merge가 request, close·request 그대로, 목록 없음·워크플로 경로 없음은 그대로의 세 시험이 있다. 통과
  - `tests/test_edit_guard.py` 245~253, 279~287줄 → 없는 CODEOWNERS 쓰기 통과, 이미 있으면 막음이 두 경우 모두 있다. 통과
  - setup SKILL.md 52줄(login 읽기), 2번 표 마지막 행(login 보이기, CODEOWNERS 알림), 3번 CODEOWNERS 항목(없을 때만 쓰기), 4번(쓰지 못하면 넣을 줄, ruleset 명령·Settings 경로·요금제 조건·한계와 닫는 법), 양식의 verdict 단계(`--changed-files`로 목록을 넘김)를 읽었다 → 네 곳이 모두 적는다. 통과
  - python으로 SKILL.md 4번의 ruleset JSON과 `docs/TOOLS.md` 135줄의 시험한 JSON을 견줬다 → `target`, `conditions`, `rules`, `bypass_actors`, `enforcement` 같음, `name`만 다름. 통과
  - `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "0.14.0",`. 통과
  - `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
  - `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `README.md`를 따로 보고 `grep -nF "pr diff"`를 돌렸다 → 네 문서에 옛 `gh pr diff --name-only` 글이 남지 않았다. ARCHITECTURE의 CI 항목, README 33줄과 손 작업 3번, ADR-023이 파일 목록 API와 실패 때 머지 요청, CODEOWNERS·ruleset, 판정의 워크플로 검사, 편집 훅의 CODEOWNERS 예외와 맞고 PRD에는 어긋나는 줄이 없다. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 104 tests`, `OK`. 통과

**문제**
- 없음

**판정**: 통과
