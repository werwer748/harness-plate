# 아키텍처

## 기술 스택
- 코드가 없다. 마크다운 스킬(`SKILL.md`)과 JSON 매니페스트로 이루어진 플러그인이다.
- 대상 도구: Claude Code(2.1.291에서 확인), Codex(0.160.0에서 확인). Grok Build는 설치한 시점부터 확인한다.
- 배포: 플러그인과 마켓플레이스 목록. 레포는 GitHub의 `werwer748/harness-plate`(비공개)다.

## 디렉터리 구조
```
.claude-plugin/marketplace.json    # Claude Code용 마켓플레이스 목록
.agents/plugins/marketplace.json   # Codex용 마켓플레이스 목록
plugins/plate/
├── .claude-plugin/plugin.json     # Claude Code용 매니페스트
├── .codex-plugin/plugin.json      # Codex용 매니페스트
└── skills/setup/SKILL.md          # 셋업 스킬. 본문 하나를 두 도구가 함께 쓴다
docs/                              # 이 레포의 하네스 기록. 위치는 AGENTS.md의 문서 지도를 따른다
```

## 패턴과 규칙
- 레일 규격(단계 순서, 기록 위치와 형식, 통과 조건)은 도구에 기대지 않는 파일로 두고, 서브에이전트와 훅은 도구별 구현으로 둔다. 이유: 레일을 돌리는 도구가 바뀌어도 똑같이 작동해야 한다(ADR-004).
- 스킬 본문은 하나만 두고 도구별 매니페스트가 같은 폴더를 가리킨다. 본문은 도구 이름 대신 동작으로 쓴다("사용자에게 묻는다", "파일을 옮긴다")(ADR-004).
- 양식은 스킬 본문 안에 넣는다. 이유: 별도 파일로 두면 대상 프로젝트의 작업 디렉터리 밖이라 읽기가 거부된 전례가 있다.
- 위치 규칙은 대상 프로젝트의 `AGENTS.md`에 두고 `CLAUDE.md`에는 `@AGENTS.md` 임포트만 둔다. 이유: Claude Code는 `CLAUDE.md`가 없을 때만 `AGENTS.md`를 읽고, Codex와 Grok Build는 `AGENTS.md`를 자동으로 읽는다(ADR-007).
- 각 단계는 Claude Code에서 만들고 Codex에서 같은 결과를 확인해야 완성이다. 빈 폴더는 결과가 완전히 같아야 하고, 기존 프로젝트는 파일 목록·위치·지도 구간이 같아야 한다(ADR-004, ADR-010).
- Codex는 설치할 때 플러그인을 `~/.codex/plugins/cache/` 아래로 복사해 그 사본을 읽는다. 스킬을 고친 뒤에는 `codex plugin add plate@harness-plate`를 다시 실행해 설치본을 갱신한다.

## 데이터 흐름
```
셋업(AGENTS.md의 문서 지도, docs/의 양식)
→ 맥락(docs/PRD.md, docs/ARCHITECTURE.md, docs/ADR.md, UI 프로젝트면 docs/DESIGN.md)
→ 계획(docs/tasks/NNN-slug/plan.md)
→ 실행(docs/tasks/NNN-slug/phase-N.md, phase마다 새 컨텍스트의 에이전트)
→ 검증(docs/tasks/NNN-slug/verify.md)
```
셋업만 만들었다. 맥락부터 검증까지는 만들기 전이다.
