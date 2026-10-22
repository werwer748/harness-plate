# Phase 1: setup의 CI 워크플로

**목표**: setup이 GitHub 원격이 있는 프로젝트에 CI 워크플로를 둘지 묻고, 승인하면 양식대로 워크플로 파일을 쓰고 시크릿 등록 방법을 안내한다.

**테스트 먼저**: 아니오 — 스킬 본문과 문서(`.md`)만 고친다

**읽을 것**
- `plugins/plate/skills/setup/SKILL.md` (판정, 승인 표, 쓰는 일, 보고, 양식)
- `plugins/plate/skills/review/SKILL.md`의 PR 모드 절 (`001-ci-review`가 적은 부르는 꼴과 등급 묶음의 꼴)
- `docs/ARCHITECTURE.md`의 디렉터리 구조 (`001-ci-review`가 만든 판정 스크립트의 경로. 입력과 출력의 꼴은 그 스크립트에 있다)
- `plugins/plate/hooks/edit_guard.py` (셋업된 프로젝트에서 남은 phase가 없으면 `.md`가 아닌 파일의 편집을 막는다)
- https://code.claude.com/docs/en/github-actions (설정, 시크릿 이름과 `claude setup-token`, permissions, `plugin_marketplaces`와 `plugins`로 플러그인 스킬 부르기)
- https://raw.githubusercontent.com/anthropics/claude-code-action/main/action.yml (입력과 `structured_output`)
- `docs/ADR.md` (항목의 꼴)

**TODO**
- [ ] setup의 1번이 GitHub 원격과 plate 워크플로가 있는지를 보고, 2번의 승인 표에 "GitHub 원격이 있고 plate 워크플로가 없다 → CI 에이전트를 둘지"가 더해진다 (`plugins/plate/skills/setup/SKILL.md`)
- [ ] 승인하면 setup이 양식 절의 워크플로를 `.github/workflows/` 아래에 쓰고, 4번의 보고에 `CLAUDE_CODE_OAUTH_TOKEN` 시크릿 등록 방법(`claude setup-token`으로 토큰을 만들어 저장소 시크릿으로 넣는다)이 들어간다 (`plugins/plate/skills/setup/SKILL.md`)
- [ ] 양식 절에 워크플로가 생긴다. PR이 열리거나 갱신될 때 돌고, 공개 마켓플레이스에서 plate를 받아 review의 PR 모드를 부르고, 등급 묶음을 구조화 출력으로 받는다. 다음 단계가 판정 스크립트를 돌려 평가서를 PR 댓글로 달고, 자동 머지면 merge commit으로 합치고 머리 브랜치를 지우며, 닫기면 PR을 닫는다. review 단계에는 저장소와 PR의 쓰기 권한이 없다 (`plugins/plate/skills/setup/SKILL.md`)
- [ ] setup의 설명(description)과 ARCHITECTURE의 디렉터리 구조, 패턴과 규칙, 데이터 흐름이 CI 워크플로를 적는다 (`plugins/plate/skills/setup/SKILL.md`, `docs/ARCHITECTURE.md`)
- [ ] ADR-021이 더해진다 (`docs/ADR.md`)

**통과 조건**
- 완료 조건 1, 2, 3이 참이다.
  - 확인: 완료 조건 1, 2, 3의 확인을 모두 돌린다
