# 아키텍처

## 기술 스택
- 마크다운 스킬(`SKILL.md`), JSON 매니페스트, Claude Code 훅으로 이루어진 플러그인이다.
- 훅 스크립트는 Python 3 표준 라이브러리로 쓰고 테스트는 `unittest`로 돌린다(ADR-019). 2026-10-17에 Python 3.13.2에서 테스트가 통과했다.
- 대상 도구: Claude Code(1단계는 2.1.291, 2단계의 2026-10-08 판정은 2.1.293, 3단계는 2.1.294에서 확인). Codex(0.160.0)는 2026-10-08에 확인을 멈췄고, Codex와 Grok Build로 넓히는 일은 v1.0 뒤에 한다(ADR-018). 도구별로 확인해 둔 사실은 `docs/TOOLS.md`에 있다.
- 배포: 플러그인과 마켓플레이스 목록. 레포는 GitHub의 `werwer748/harness-plate`(비공개)다.

## 디렉터리 구조
```
.claude-plugin/marketplace.json    # Claude Code용 마켓플레이스 목록
.agents/plugins/marketplace.json   # Codex용 마켓플레이스 목록
plugins/plate/
├── .claude-plugin/plugin.json     # Claude Code용 매니페스트
├── .codex-plugin/plugin.json      # Codex용 매니페스트
├── ci/
│   └── verdict.py                 # 판정 스크립트. CI의 워크플로가 PR 모드 review의 등급 묶음으로 자동 머지, 머지 요청, 닫기 가운데 하나를 고른다
├── hooks/
│   ├── hooks.json                 # Claude Code 훅 설정. 파일 편집 도구의 PreToolUse에 edit_guard.py를 건다
│   └── edit_guard.py              # 계획 없는 코드 편집과, 테스트 먼저인 phase에서 테스트보다 앞선 구현을 막는 훅
└── skills/
    ├── setup/SKILL.md             # 셋업 스킬. 본문 하나를 두 도구가 함께 쓴다. GitHub 원격이 있는 프로젝트에 둘 CI 워크플로(`.github/workflows/plate-review.yml`)의 양식도 담는다
    ├── context/SKILL.md           # 맥락 채우기 스킬. 본문 하나를 두 도구가 함께 쓴다
    ├── plan/SKILL.md              # 계획 스킬. 본문 하나를 두 도구가 함께 쓴다
    ├── run/SKILL.md               # 실행 스킬. 조율만 하고 수행, 확인, 회고, 코드 평가, 하네스 eval은 아래 다섯 스킬에 맡긴다
    ├── phase/SKILL.md             # 수행 스킬. run이 띄운 에이전트가 부른다
    ├── check/SKILL.md             # phase 확인 스킬. run이 수행 뒤에 띄운 에이전트가 부른다
    ├── retro/SKILL.md             # task 회고 스킬. run이 task의 phase가 모두 통과한 뒤 띄운 에이전트가 부른다
    ├── review/SKILL.md            # 코드 평가 스킬. run이 tasks 끝에 띄운 에이전트가 부른다
    └── eval/SKILL.md              # 하네스 eval 스킬. run이 tasks 끝에 코드 평가 뒤 띄운 에이전트가 부른다
tests/                             # 단위 테스트(`python3 -m unittest discover -s tests`)
├── test_edit_guard.py             # 훅의 테스트
└── test_verdict.py                # 판정 스크립트의 테스트
docs/                              # 이 레포의 하네스 기록. 위치는 AGENTS.md의 문서 지도를 따른다
```

## 패턴과 규칙
- 레일 규격(단계 순서, 기록 위치와 형식, 통과 조건)은 도구에 기대지 않는 파일로 두고, 서브에이전트와 훅은 도구별 구현으로 둔다. 이유: 레일을 돌리는 도구가 바뀌어도 똑같이 작동해야 한다(ADR-004).
- 스킬 본문은 하나만 두고 도구별 매니페스트가 같은 폴더를 가리킨다. 본문은 도구 이름 대신 동작으로 쓴다("사용자에게 묻는다", "파일을 옮긴다")(ADR-004).
- 양식은 스킬 본문 안에 넣는다. 이유: 별도 파일로 두면 대상 프로젝트의 작업 디렉터리 밖이라 읽기가 거부된 전례가 있다.
- 위치 규칙은 대상 프로젝트의 `AGENTS.md`에 두고 `CLAUDE.md`에는 `@AGENTS.md` 임포트만 둔다. 이유: Claude Code는 `CLAUDE.md`가 없을 때만 `AGENTS.md`를 읽고, Codex와 Grok Build는 `AGENTS.md`를 자동으로 읽는다.
- 스킬이 다른 스킬의 절차를 써야 하면 그 스킬을 이름으로 부른다(`plate:setup`, `plate:context`). 절차를 복사하지 않는다.
- 각 단계의 완성은 Claude Code에서 실제로 실행한 결과를 기대값(답 파일, 빌드 매니페스트, 토큰 파일)과 견줘 판정한다. 1단계 전부와 2단계 판정의 일부는 Codex에서도 같은 결과를 확인했고, 2026-10-08부터는 Codex에서 확인하지 않는다(ADR-018).
- 도구마다 다른 동작과 확인을 멈춘 지점은 `docs/TOOLS.md`에 적는다(ADR-018).
- 대상 프로젝트의 규칙이 스킬의 규칙과 부딪히면 프로젝트의 규칙이 우선한다. 스킬의 절대 규칙도 든다. 단계를 건너뛰라는 규칙은 들지 않는다. 일곱 스킬(plan, run, phase, check, retro, review, eval)의 본문에 넣었고, 따른 곳은 보고나 기록에 적는다.
- 막는 장치는 setup이 대상 프로젝트의 `AGENTS.md`에 넣는 규칙 구간(`<!-- plate:rules:start -->`부터 `<!-- plate:rules:end -->`까지)이다. 코드를 고치는 요청은 계획부터 세우고, task는 task 회고가 통과해야 끝나고, tasks는 끝의 코드 평가와 하네스 eval을 담은 전체 보고가 나와야 끝나며, 다른 규칙이 이 단계들을 건너뛰라고 해도 따르지 않는다. 이 규칙 구간이 기본이고, 훅(`plugins/plate/hooks/`)은 Claude Code의 구현으로 더 막는다. 훅은 파일 편집 도구의 호출만 보고, `phase-N.md`가 있는 task가 없을 때의 코드 편집(setup이 아직 없는 `.github/workflows/plate-review.yml`을 쓰는 것은 빼고)과 테스트 먼저인 phase에서 테스트 변경 없는 구현 편집을 막는다. 같은 파일을 테스트 먼저 때문에 세 번 막으면 더 시도하지 않고 막힘으로 멈춰 까닭과 해결책을 논의하며, 훅을 끄는 스위치는 두지 않는다. 이유: 세 도구가 모두 `AGENTS.md`를 읽고 서브에이전트에도 실린다. 훅은 Claude Code에서만 돌므로 규칙을 대신하지 않고, 잘못 막을 때는 끄는 대신 까닭을 찾아 해결책을 논의한다.
- run은 기본 브랜치(`origin`의 HEAD, 없으면 `main`, 그다음 `master`)에서 시작하면 tasks마다 하나인 `tasks/<이름>` 브랜치를 만들어 실행하고, tasks 끝에서 `docs/tasks/`를 비운 뒤 기본 브랜치로 합칠지 묻는다. 실행 방식과 상관없이 묻는다. 이유: 끝의 평가와 보고까지 가지 않은 tasks가 기본 브랜치에 들어가지 않게 한다.
- PR의 CI는 setup이 대상 프로젝트에 쓰는 워크플로(`.github/workflows/plate-review.yml`)가 한다. setup은 GitHub 원격이 있고 plate 워크플로가 없을 때 둘지 묻고, 승인하면 쓴다. 훅은 남은 phase가 없을 때 아직 없는 이 파일을 쓰는 것은 막지 않아서, 이미 셋업된 프로젝트에서 setup을 다시 불러도 쓴다. `review` 잡은 읽기 권한만으로 토큰 없이 공개 마켓플레이스(`werwer748/harness-plate`)에서 plate를 받아 review의 PR 모드를 부르고 등급 묶음을 구조화 출력으로 낸다. `verdict` 잡이 쓰기 권한으로 등급 묶음을 판정 스크립트(`plugins/plate/ci/verdict.py`)에 넘겨 평가서를 PR 댓글로 달고, 자동 머지면 merge commit으로 합치고 머리 브랜치를 지우며, 닫기면 PR을 닫는다. 이유: 판정 규칙은 숫자와 등급만 보므로 스크립트가 늘 같은 답을 내고, PR 코드에 숨은 지시가 있어도 에이전트에게는 머지 권한이 없다(ADR-021).

## 데이터 흐름
```
셋업(AGENTS.md의 문서 지도와 규칙 구간, docs/의 양식, GitHub 원격이 있고 승인하면 .github/workflows/plate-review.yml. 설치만 하고 묻지 않고 끝난다)
→ 맥락(docs/PRD.md, docs/ARCHITECTURE.md, docs/ADR.md, UI 프로젝트면 docs/DESIGN.md)
→ 계획(docs/tasks/에 tasks 머리 plan.md와, task 폴더 NNN-slug/마다 task 머리 plan.md와 phase-N.md를 쓰고 한 커밋으로 넣는다
       → tasks가 진행 중이면 새 요청을 지금 tasks에 task로 더할지 묻는다)
→ 실행(tasks/<이름> 브랜치에서 시작할 때 실행 방식(task 하나씩, tasks 일괄)을 묻는다
       → phase마다 새 에이전트가 수행해 phase-N.md에 기록을 덧붙이고, 다른 새 에이전트가 통과 조건과 빌드·린트·테스트를 돌려 확인 절을 더한다
       → 확인이 통과하면 phase-N.md를 done-phase-N.md로 바꾼다
       → task의 phase가 모두 통과하면 또 다른 새 에이전트가 task 회고를 task 폴더의 retro.md에, tasks 끝에 볼 것을 docs/tasks/FRICTION.md에 적는다
       → 회고의 문제는 고칠 phase를 더해 고친다(task 하나씩은 승인받고, tasks 일괄은 묻지 않는다)
       → 띄운 에이전트마다, 물은 자리마다 docs/tasks/RUNLOG.md에 한 줄을 남긴다)
→ tasks 끝(새 에이전트가 바뀐 코드를 평가해 docs/tasks/review.md에, 다른 새 에이전트가 하네스를 eval해 docs/tasks/eval.md에 적는다
       → 전체 보고와 고칠 안을 한 번에 묻는다
       → 승인받은 대로 plate 자체의 고칠 거리는 GitHub 이슈로 올리고, 미룬 소스 문제는 docs/BACKLOG.md에 적고, 고칠 것은 고침 task로 더해 같은 레일로 돌린다
       → docs/tasks/를 비우고 기본 브랜치로 합칠지 묻는다)

PR(CI 워크플로가 있는 프로젝트에서 열리거나 갱신되면)
→ review 잡(읽기 권한만. 공개 마켓플레이스에서 받은 plate의 review가 PR 모드로 평가서 파일과 등급 묶음(구조화 출력)을 낸다)
→ verdict 잡(쓰기 권한. 판정 스크립트가 등급 묶음으로 자동 머지, 머지 요청, 닫기 가운데 하나를 고른다
       → 평가서를 PR 댓글로 단다
       → 자동 머지면 merge commit으로 합치고 머리 브랜치를 지우고, 닫기면 PR을 닫고, 머지 요청이면 사람이 머지하도록 둔다)
```

어느 실행 방식이든 막힘, 훅의 세 번째 막음, 계획이 틀림, 같은 phase의 확인이나 같은 task의 회고의 세 번 실패에서는 멈추고 원인과 해결책을 보여 논의한다. tasks의 기록은 비운 커밋의 부모에 남고, `docs/BACKLOG.md`는 `docs/tasks/` 밖에 있어 비워도 남는다.

## 명령
- 설치: 없음
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests`
