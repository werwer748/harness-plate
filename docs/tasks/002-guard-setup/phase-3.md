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
- [ ] setup의 1번에 판정이 더해진다: GitHub 원격이 있고 plate 워크플로가 없으면 `gh api user`의 login을 읽고 `.github/CODEOWNERS`가 있는지 본다 (`plugins/plate/skills/setup/SKILL.md`)
- [ ] 2번 표 마지막 행의 묻는 것에 login과 CODEOWNERS를 쓴다는 것(또는 이미 있어 쓰지 않는다는 것)이 더해진다 (같은 파일)
- [ ] 3번의 "CI 워크플로"에 CODEOWNERS를 쓰는 규칙이 더해진다: 승인했고 파일이 없고 login이 있을 때만 task 머리의 두 줄을 쓰고, 그 밖에는 쓰지 않는다. 절대 규칙 2·3(양식 칸을 채우지 않는다, 양식을 바꾸지 않는다)과 어긋나지 않게 적는다 (같은 파일)
- [ ] 4번의 시크릿 등록 줄 뒤에 두 줄이 더해진다. 하나는 쓰지 못한 CODEOWNERS의 넣을 줄이다. 다른 하나는 ruleset 거는 법이다: `docs/TOOLS.md`의 시험한 JSON으로 만드는 `gh api` 명령, Settings → Rules → Rulesets 경로, 비공개 저장소는 요금제에 따라 걸 수 없다는 것, 걸기 전에는 워크플로를 바꾼 PR을 판정 검사만 막는다는 것 (같은 파일)
- [ ] 양식 절의 verdict 잡이 PR의 바뀐 파일 목록(`gh pr diff --name-only`)을 파일로 받아 판정 스크립트에 `--changed-files`로 넘기도록 바뀌고, 양식 위의 설명에 그것이 더해진다 (같은 파일)
- [ ] 3줄(설명)과 10줄(첫머리)에 CODEOWNERS와 ruleset 안내가 더해진다 (같은 파일)
- [ ] `docs/ARCHITECTURE.md` 23줄의 setup 설명, 51줄의 PR의 CI, 데이터 흐름의 셋업 줄과 verdict 잡 줄에 CODEOWNERS, ruleset 안내, 바뀐 파일 목록 넘기기가 더해진다 (`docs/ARCHITECTURE.md`)
- [ ] `docs/ADR.md`에 ADR-023이 더해진다. 결정: 워크플로를 바꾼 PR의 자동 머지는 저장소 설정(ruleset과 CODEOWNERS)으로 막고, setup은 CODEOWNERS만 쓰고 ruleset은 안내하며, 판정 스크립트의 워크플로 검사를 보조로 둔다. 이유: PR이 새 워크플로를 더해도 저장소 설정은 바꾸지 못한다. 시크릿처럼 관리자 권한이 드는 일은 사용자가 한다. 트레이드오프: 사용자가 ruleset을 걸지 않으면 판정 검사만 남는다. 비공개 저장소는 요금제에 따라 걸 수 없다. 워크플로를 바꾼 PR은 사람이 관리자 우회로 머지해야 한다 (`docs/ADR.md`)

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
