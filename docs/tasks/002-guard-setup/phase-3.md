# Phase 3: setup의 CODEOWNERS, ruleset 안내, 양식 워크플로

**목표**: setup이 CI 물음에 login을 보여 주고, CODEOWNERS를 결정대로 쓰거나 보고에 적고, 보고에 ruleset 거는 법을 적고, 양식 워크플로가 바뀐 파일 목록을 판정 스크립트에 넘긴다.

**테스트 먼저**: 아니오 — `.md`만 고친다

**읽을 것**
- `plugins/plate/skills/setup/SKILL.md`: 3줄(설명), 10줄(첫머리), 절대 규칙, 1번의 "GitHub 원격"·"plate 워크플로" 판정, 2번 표의 마지막 행, 3번의 "CI 워크플로", 4번의 시크릿 등록 줄, 양식 절의 `.github/workflows/plate-review.yml` 설명과 verdict 잡
- `docs/TOOLS.md`에서 `001-ruleset-probe`가 더한, 다섯 장면을 적은 절 (시험한 ruleset JSON과 무엇이 막았는지)
- `plugins/plate/ci/verdict.py`의 맨 위 설명 (`--changed-files`의 꼴)
- `docs/ARCHITECTURE.md`의 23줄, 51줄, 데이터 흐름의 셋업 줄과 verdict 잡 줄
- `docs/ADR.md`의 ADR-021 (CI의 결정과 트레이드오프)

**TODO**
- [x] setup의 1번에 판정이 더해진다: GitHub 원격이 있고 plate 워크플로가 없으면 `gh api user`의 login을 읽고 `.github/CODEOWNERS`가 있는지 본다 (`plugins/plate/skills/setup/SKILL.md`)
- [x] 2번 표 마지막 행의 묻는 것에 login과 CODEOWNERS를 쓴다는 것(또는 이미 있어 쓰지 않는다는 것)이 더해진다 (같은 파일)
- [x] 3번의 "CI 워크플로"에 CODEOWNERS를 쓰는 규칙이 더해진다: 승인했고 파일이 없고 login이 있을 때만 task 머리의 두 줄을 쓰고, 그 밖에는 쓰지 않는다. 절대 규칙 2·3(양식 칸을 채우지 않는다, 양식을 바꾸지 않는다)과 어긋나지 않게 적는다 (같은 파일)
- [x] 4번의 시크릿 등록 줄 뒤에 두 줄이 더해진다. 하나는 쓰지 못한 CODEOWNERS의 넣을 줄이다. 다른 하나는 ruleset 거는 법이다: `docs/TOOLS.md`의 시험한 JSON으로 만드는 `gh api` 명령, Settings → Rules → Rulesets 경로, 비공개 저장소는 요금제에 따라 걸 수 없다는 것, 걸기 전에는 워크플로를 바꾼 PR을 판정 검사만 막는다는 것, 걸어도 PR을 연 계정이 유일한 코드 소유자면 막지 못하고 닫으려면 코드 소유자를 PR을 여는 계정과 다른 쓰기 권한 계정으로 둔다는 것 (같은 파일)
- [x] 양식 절의 verdict 잡이 PR의 바뀐 파일 목록(`gh pr diff --name-only`)을 파일로 받아 판정 스크립트에 `--changed-files`로 넘기도록 바뀌고, 양식 위의 설명에 그것이 더해진다 (같은 파일)
- [x] 3줄(설명)과 10줄(첫머리)에 CODEOWNERS와 ruleset 안내가 더해진다 (같은 파일)
- [x] `docs/ARCHITECTURE.md` 23줄의 setup 설명, 51줄의 PR의 CI, 데이터 흐름의 셋업 줄과 verdict 잡 줄에 CODEOWNERS, ruleset 안내, 바뀐 파일 목록 넘기기가 더해진다 (`docs/ARCHITECTURE.md`)
- [x] `docs/ADR.md`에 ADR-023이 더해진다. 결정: 워크플로를 바꾼 PR은 판정 스크립트의 워크플로 검사가 머지 요청으로 내리고, 저장소 설정(ruleset과 CODEOWNERS)은 PR을 연 계정이 코드 소유자가 아닐 때의 머지와 main 직접 푸시를 막는다. setup은 CODEOWNERS만 쓰고 ruleset은 안내한다. 이유: PR이 저장소 설정은 바꾸지 못하지만, GitHub는 작성자가 유일한 코드 소유자면 코드 소유자 리뷰를 채운 것으로 본다(`docs/TOOLS.md`). 시크릿처럼 관리자 권한이 드는 일은 사용자가 한다. 트레이드오프: 사용자가 ruleset을 걸지 않으면 판정 검사만 남는다. 비공개 저장소는 요금제에 따라 걸 수 없다. 워크플로를 바꾼 PR은 사람이 관리자 우회로 머지해야 한다. 판정 검사는 PR이 워크플로를 고쳐 건너뛸 수 있다. 혼자 쓰는 저장소에서는 다른 쓰기 권한 계정을 코드 소유자로 두어야 설정이 길을 닫는다 (`docs/ADR.md`)

**통과 조건**
- (완료 조건 3) setup의 네 곳이 바뀐 동작을 적는다
  - 확인: `plugins/plate/skills/setup/SKILL.md`의 2번 표, 3번, 4번, 양식 절을 하나씩 읽어 네 곳이 저마다 위 TODO의 것을 적는다. 한 곳이라도 없으면 실패
  - 확인: setup 4번의 ruleset JSON이 `docs/TOOLS.md`에서 `001-ruleset-probe`가 더한 절의 JSON과 규칙, 우회 목록, 대상 브랜치에서 같다
  - 확인: 양식 절의 verdict 잡에서 판정 스크립트를 부르는 줄에 `--changed-files`가 있다
- (완료 조건 4) 맥락 문서가 맞는다
  - 확인: `docs/ARCHITECTURE.md`의 17·20·23줄, 49줄, 51줄, 데이터 흐름의 셋업 줄과 verdict 잡 줄을 하나씩 읽어 바뀐 동작과 어긋나지 않는다(줄 번호는 이 task의 계획 커밋 시점 기준)
  - 확인: `docs/ADR.md`에 ADR-023이 있고 결정, 이유, 트레이드오프를 적는다
- (완료 조건 1, 2) 시험이 그대로 통과한다
  - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`

## 한 일
- setup 1번 판정: "GitHub login과 CODEOWNERS" 기준을 더했다. GitHub 원격이 있고 plate 워크플로가 없을 때만 `gh api user`의 login을 읽고 `.github/CODEOWNERS`가 있는지 본다. 판정 수를 "여섯"에서 "일곱"으로 고쳤다 (`plugins/plate/skills/setup/SKILL.md`)
- 2번 표 마지막 행: login을 보여 주고, 승인하면 CODEOWNERS에 두 줄을 쓴다는 것과, 이미 있거나 login이 없으면 쓰지 않고 넣을 줄을 보고에 적는다는 것을 더했다 (같은 파일)
- 3번 "CI 워크플로": 승인했고 파일이 없고 login이 있을 때만 `/.github/workflows/ @<login>`, `/.github/CODEOWNERS @<login>`을 쓰는 규칙과, 이것이 양식 칸 채우기나 양식 바꾸기가 아니라는 줄(절대 규칙 2·3), 이미 있는 것은 고치지 않는다는 줄(절대 규칙 1)을 더했다 (같은 파일)
- 4번: 시크릿 줄 뒤에 쓰지 못한 CODEOWNERS의 넣을 줄과, ruleset 거는 법(`docs/TOOLS.md`의 시험한 JSON으로 만든 `gh api -X POST 'repos/{owner}/{repo}/rulesets' --input -` 명령, Settings → Rules → Rulesets 경로, 비공개 저장소의 요금제 제한, 걸기 전에는 판정 검사만 막는다는 것, 유일한 코드 소유자가 연 PR은 막지 못하고 다른 쓰기 권한 계정을 코드 소유자로 두라는 것)을 더했다 (같은 파일)
- 양식 절: verdict 잡이 `gh pr diff "$PR" --name-only > changed-files.txt`로 목록을 받아 `verdict.py --changed-files changed-files.txt`로 넘기게 바꾸고, 양식 위 설명에 그것을 더했다 (같은 파일)
- 3줄(설명)과 10줄(첫머리)에 CODEOWNERS와 ruleset 안내를 더했다 (같은 파일)
- `docs/ARCHITECTURE.md`: 23줄 setup 설명, 51줄 PR의 CI(login 보여 주기, CODEOWNERS 규칙, ruleset 안내, 바뀐 파일 목록 넘기기, 이유에 ADR-023), 데이터 흐름의 셋업 줄과 verdict 잡 줄을 고쳤다 (`docs/ARCHITECTURE.md`)
- `docs/ADR.md`: ADR-023을 결정, 이유, 트레이드오프로 더했다 (`docs/ADR.md`)

## 확인 결과
- (완료 조건 3) setup의 네 곳이 바뀐 동작을 적는다
  - `plugins/plate/skills/setup/SKILL.md`의 2번 표 마지막 행(login, CODEOWNERS 쓰기/쓰지 않음), 3번 "CI 워크플로"의 CODEOWNERS 항목, 4번의 CODEOWNERS 줄과 ruleset 줄, 양식 절 설명과 verdict 잡을 하나씩 읽었다 → 네 곳 모두 TODO의 것을 적는다. 통과
  - 4번의 ruleset JSON과 `docs/TOOLS.md`의 "ruleset과 CODEOWNERS로 워크플로 PR의 자동 머지를 막는지 본 것" 절 JSON을 견줬다 → `target: branch`, `conditions.ref_name.include: ["~DEFAULT_BRANCH"]`, `rules`의 `pull_request` 파라미터 다섯, `bypass_actors`(actor_id 5, RepositoryRole, pull_request)가 같다. `name`만 `plate-workflow-guard`로 다르다. 통과
  - `grep -n "changed-files" plugins/plate/skills/setup/SKILL.md` → verdict 잡의 `verdict=$(printf '%s' "$BUNDLE" | python3 harness-plate/plugins/plate/ci/verdict.py --changed-files changed-files.txt)` 줄. 통과
- (완료 조건 4) 맥락 문서가 맞는다
  - `docs/ARCHITECTURE.md`의 17줄(verdict.py의 `--changed-files`), 20줄(edit_guard), 23줄(setup), 49줄(훅이 아직 없는 CODEOWNERS 쓰기를 뺀다), 51줄(PR의 CI), 데이터 흐름의 셋업 줄과 verdict 잡 줄을 읽었다 → 바뀐 동작과 어긋나지 않는다. 통과
  - `grep -n "ADR-023" docs/ADR.md` → `### ADR-023: 워크플로를 바꾼 PR은 판정 검사가 머지 요청으로 내리고, 저장소 설정이 머지를 막는다`, 아래에 결정, 이유, 트레이드오프 세 줄. 통과
- (완료 조건 1, 2) 시험이 그대로 통과한다
  - `python3 -m unittest discover -s tests` → `Ran 104 tests in 17.147s`, 마지막 줄 `OK`. 통과

## 계획과 달라진 점
없음

## 남은 것
- ruleset JSON의 `name`은 시험 때의 `workflow-guard-probe` 대신 `plate-workflow-guard`로 두었다. 규칙, 우회 목록, 대상 브랜치는 같다
- 양식의 `gh pr diff "$PR" --name-only`가 실패하면(예: GitHub가 diff를 내지 못할 만큼 큰 PR) 그 단계가 실패해 판정 댓글이 달리지 않는다. 실제 GitHub에서 돌려 보지는 않았다
- 4번의 `{owner}`/`{repo}` 자리표시는 `gh api`가 바꾸는 것이고, 실제 대상 저장소에서 명령을 돌려 보지는 않았다

## 하네스에서 걸린 것
없음
