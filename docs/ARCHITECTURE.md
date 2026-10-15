# 아키텍처

## 기술 스택
- 코드가 없다. 마크다운 스킬(`SKILL.md`)과 JSON 매니페스트로 이루어진 플러그인이다.
- 대상 도구: Claude Code(1단계는 2.1.291, 2단계의 2026-10-08 판정은 2.1.293, 3단계는 2.1.294에서 확인). Codex(0.160.0)는 2026-10-08에 확인을 멈췄고, Codex와 Grok Build로 넓히는 일은 v1.0 뒤에 한다(ADR-018). 도구별로 확인해 둔 사실은 `docs/TOOLS.md`에 있다.
- 배포: 플러그인과 마켓플레이스 목록. 레포는 GitHub의 `werwer748/harness-plate`(비공개)다.

## 디렉터리 구조
```
.claude-plugin/marketplace.json    # Claude Code용 마켓플레이스 목록
.agents/plugins/marketplace.json   # Codex용 마켓플레이스 목록
plugins/plate/
├── .claude-plugin/plugin.json     # Claude Code용 매니페스트
├── .codex-plugin/plugin.json      # Codex용 매니페스트
└── skills/
    ├── setup/SKILL.md             # 셋업 스킬. 본문 하나를 두 도구가 함께 쓴다
    ├── context/SKILL.md           # 맥락 채우기 스킬. 본문 하나를 두 도구가 함께 쓴다
    ├── plan/SKILL.md              # 계획 스킬. 본문 하나를 두 도구가 함께 쓴다
    ├── run/SKILL.md               # 실행 스킬. 조율만 하고 수행과 회고는 아래 두 스킬에 맡긴다
    ├── phase/SKILL.md             # 수행 스킬. run이 띄운 에이전트가 부른다
    └── retro/SKILL.md             # 회고 스킬. run이 띄운 에이전트가 부른다
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
- 대상 프로젝트의 규칙이 스킬의 규칙과 부딪히면 프로젝트의 규칙이 우선한다. 스킬의 절대 규칙도 든다. 네 스킬(plan, run, phase, retro)의 본문에 넣었고, 따른 곳은 보고나 기록에 적는다.

## 데이터 흐름
```
셋업(AGENTS.md의 문서 지도, docs/의 양식)
→ 맥락(docs/PRD.md, docs/ARCHITECTURE.md, docs/ADR.md, UI 프로젝트면 docs/DESIGN.md)
→ 계획(docs/tasks/NNN-slug/에 plan.md와 phase마다의 phase-N.md를 쓰고 그 파일들만 커밋한다)
→ 실행(phase마다 새 컨텍스트의 에이전트가 수행하고 그 phase의 phase-N.md에 기록을 덧붙인다
       → 회고 → 통과하면 배운 것과 하네스의 문제점을 docs/LESSONS.md로 옮기고 phase-N.md를 지운다)
→ 검증(작업 전체를 plan.md의 완료 조건에 대어 보고 docs/tasks/NNN-slug/verify.md를 남긴다)
```
셋업, 맥락, 계획, 실행을 만들었다. 검증은 만들기 전이다.

통과한 phase의 근거는 git 이력에만 남는다. 검증까지 통과한 작업의 폴더에는 `plan.md`와 `verify.md`가 남는다.
