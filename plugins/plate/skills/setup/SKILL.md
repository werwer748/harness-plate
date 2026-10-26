---
name: setup
description: 프로젝트에 하네스를 설치한다. `docs/`에 문서 양식(PRD, ARCHITECTURE, ADR, 화면이 있는 프로젝트면 DESIGN)과 tasks 기록 폴더를 만들고, `AGENTS.md`에 문서 지도와 작업 규칙을 넣고, `CLAUDE.md`가 `AGENTS.md`를 불러오게 한다. GitHub 원격이 있고 plate 워크플로가 없으면 PR마다 review로 평가해 판정대로 자동 머지, 머지 요청, 닫기를 하는 CI 워크플로를 둘지 묻고, 승인하면 `.github/workflows/`에 쓰고 보고에 시크릿 등록 방법을 적는다. 설치만 하고 보고로 끝나며, 끝에 다른 일로 이어 갈지 묻지 않는다. plate를 프로젝트에 처음 쓸 때, 또는 "하네스 셋업해줘", "문서 위치 잡아줘"라고 할 때 쓴다. 문서 내용을 채우는 일에는 쓰지 않는다.
---

# 셋업

**막는 실패**: 기록을 둘 위치가 정해져 있지 않으면 세션마다 다른 곳에 문서를 만들고, 다음 세션은 그 문서를 찾지 못한다.

프로젝트에 하네스 문서의 위치 기준을 세운다. 끝나면 `docs/`에 문서 양식과 tasks 기록 폴더가 있고, `AGENTS.md`에 문서 지도와 작업 규칙이 있고, `CLAUDE.md`가 `AGENTS.md`를 불러온다. CI 에이전트를 승인했으면 `.github/workflows/plate-review.yml`이 있다. 문서의 내용은 채우지 않고, 4번의 보고로 끝난다.

## 절대 규칙

1. **승인받지 않은 기존 파일은 옮기지도, 덮어쓰지도, 지우지도 않는다.** 프로젝트가 작아도, 결과가 뻔해 보여도 예외가 없다.
2. **양식의 `{…}` 칸을 채우지 않는다.** 추측으로도, 저장소에서 확인한 사실로도 채우지 않는다. 채우기는 이 스킬의 일이 아니다.
3. **양식은 한 글자도 바꾸지 않고 옮긴다.** 빈 프로젝트든 코드가 있는 프로젝트든 같다.
4. **커밋하지 않는다.** 스테이징도 하지 않는다.

## 1. 현재 상태를 본다

- git 레포인지 확인한다.
- 파일 목록을 본다. git 레포면 `git ls-files --cached --others --exclude-standard`, 아니면 숨김 파일을 포함한 전체 목록을 쓴다.
- `AGENTS.md`, `CLAUDE.md`, `docs/`가 있으면 읽는다.
- 아래 기준으로 여섯 가지를 판정한다. 기준에 없는 것을 근거로 판정하지 않는다.

**빈 프로젝트**: 소스 코드 파일과 빌드 매니페스트(`package.json`, `pyproject.toml`, `build.gradle`, `build.gradle.kts`, `pom.xml`, `Cargo.toml`, `go.mod`, `Gemfile`, `pubspec.yaml`, `Package.swift`)가 하나도 없으면 빈 프로젝트다.

**UI 프로젝트**: 아래 둘 중 하나에 해당하면 UI 프로젝트다. 빈 프로젝트는 판정하지 않고 2번에서 묻는다. 다만 빈 프로젝트라도 `AGENTS.md`에 문서 지도 구간이 이미 있으면 묻지 않고, 구간에 `docs/DESIGN.md` 행이 있으면 UI 프로젝트로 본다.
- 빌드 매니페스트의 의존성에 다음 중 하나가 있다: `react`, `react-dom`, `react-native`, `next`, `vue`, `nuxt`, `svelte`, `@sveltejs/kit`, `@angular/core`, `solid-js`, `preact`, `astro`, `expo`, `flutter`
- 파일 목록에 확장자가 `.tsx`, `.jsx`, `.vue`, `.svelte`, `.html`, `.css`인 파일이 있다

**같은 역할 문서**: 표준 위치가 아닌 곳에 있지만 표준 문서와 역할이 같은 기존 문서다.

| 역할 | 표준 위치 | 후보 이름 |
|---|---|---|
| 무엇을 왜 만드는지 | `docs/PRD.md` | `PRD.md`, `SPEC.md`, `REQUIREMENTS.md` |
| 기술 스택과 구조 | `docs/ARCHITECTURE.md` | `ARCHITECTURE.md` |
| 이미 내린 결정과 이유 | `docs/ADR.md` | `ADR.md`, `DECISIONS.md`, 폴더 `adr/`, 폴더 `decisions/` |
| 디자인 토큰과 UI 규칙 | `docs/DESIGN.md` | `DESIGN.md`, `UI_GUIDE.md`, `STYLE_GUIDE.md`, `DESIGN_SYSTEM.md` |

- 후보는 프로젝트 루트와 `docs/` 바로 아래에서만 찾는다. 대소문자는 구분하지 않는다.
- 이름이 맞으면 내용을 읽어 역할이 맞는지 확인한다. 역할이 다르면 같은 역할 문서가 아니다.
- 표에 없는 이름은 같은 역할 문서로 보지 않는다.
- 표준 위치에 파일이 이미 있는 역할은 후보를 찾지 않는다.

**`CLAUDE.md`의 상태**: 셋 중 하나다. 없음 / `@AGENTS.md` 한 줄뿐 / 다른 내용이 있음.

**GitHub 원격**: git 레포이고 `git remote -v`에 URL이 `github.com`인 원격이 있으면 GitHub 원격이 있다.

**plate 워크플로**: `.github/workflows/` 아래에 `plate@harness-plate`가 적힌 파일이 있으면 plate 워크플로가 있다.

## 2. 할 일을 표 하나로 보여 주고 한 번에 묻는다

3번에서 할 일을 표 하나로 보여 준다(할 일, 대상, 승인이 필요한지). 승인이 필요한 일은 아래 여섯뿐이고, 해당하는 것을 한 번에 묻는다.

| 조건 | 묻는 것 |
|---|---|
| 같은 역할 문서가 파일 하나다 | 표준 위치로 옮길지. 문서마다 따로 묻는다 |
| `CLAUDE.md`에 다른 내용이 있다 | 그 내용을 `AGENTS.md`로 옮길지 |
| git 레포가 아니다 | `git init`을 할지 |
| 빈 프로젝트이고 `AGENTS.md`에 문서 지도 구간이 없다 | 화면이 있는 프로젝트인지 |
| `AGENTS.md`에 문서 지도 구간이 있고 규칙 구간이 없다 | 규칙 구간을 더할지. 더할 글을 표 아래에 함께 보여 준다 |
| GitHub 원격이 있고 plate 워크플로가 없다 | CI 에이전트를 둘지. PR이 열리거나 갱신될 때 review가 평가하고 판정대로 평가서 댓글을 달고 자동 머지하거나 PR을 닫는 워크플로이고, 저장소에 시크릿을 넣어야 돈다고 함께 알린다 |

- 물을 것이 하나도 없으면 묻지 않고 3번으로 간다.
- 요청에 이미 답이 적혀 있는 물음은 다시 묻지 않는다.
- `AGENTS.md`의 문서 지도에 이미 경로가 적혀 있는 같은 역할 문서는 옮길지 다시 묻지 않는다. 지금 위치에 두기로 한 것이다.
- 폴더로 된 같은 역할 문서(`docs/adr/` 등)는 옮기자고 하지 않는다.
- **답을 받기 전에는 3번으로 가지 않는다.**

## 3. 승인받은 것만 실행한다

아래에 적힌 것만 한다. 다른 파일은 만들지도 고치지도 않는다. 만드는 파일은 `.gitkeep`만 빼고 모두 줄바꿈 하나로 끝난다.

**git**: `git init`을 승인받았으면 실행한다.

**문서 옮기기**: 승인받은 같은 역할 문서를 표준 위치로 옮긴다. 파일만 옮기고 스테이징하지 않는다. 거절한 문서와 폴더로 된 문서는 그대로 둔다.

**양식 만들기**: 이 문서 끝의 "양식" 절에서 가져온다.
- `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`: 표준 위치에 파일이 없고, 그 역할의 같은 역할 문서도 없을 때만 만든다.
- `docs/DESIGN.md`: UI 프로젝트일 때만, 위와 같은 조건으로 만든다.
- `docs/tasks/`: 폴더가 없으면 만들고 내용이 없는(0바이트) 파일 `.gitkeep`을 둔다.

**CI 워크플로**: CI 에이전트를 승인받았으면 이 문서 끝의 "양식" 절에서 `.github/workflows/plate-review.yml`을 가져와 그 경로에 쓴다. 거절했으면 쓰지 않는다.

**`AGENTS.md`**: 순서대로 한다.
1. `CLAUDE.md` 내용을 옮기기로 했으면, `CLAUDE.md`에서 `@AGENTS.md` 줄을 뺀 나머지를 한 글자도 바꾸지 않고 `AGENTS.md` 끝에 붙인다. `AGENTS.md`에 기존 내용이 있으면 그 뒤에 빈 줄 하나를 두고 붙인다. `AGENTS.md`가 없거나 비어 있으면 빈 줄 없이 첫 줄부터 적는다. `AGENTS.md`의 기존 내용은 바꾸지 않는다.
2. 문서 지도 구간을 만든다. 이 문서의 "문서 지도 구간" 절의 글에서 시작해 두 가지만 바꾼다.
   - UI 프로젝트가 아니면 `docs/DESIGN.md` 행을 뺀다.
   - 표준 위치가 아닌 곳에 남은 같은 역할 문서가 있으면 그 행의 위치 칸에 실제 경로를 적는다.
3. 구간을 넣는다.
   - `AGENTS.md`가 없으면 구간만 있는 파일로 만든다.
   - `AGENTS.md`에 구간이 없으면 파일 끝에 빈 줄 하나를 두고 구간을 붙인다.
   - 구간이 이미 있으면 표식 사이에서 표 위의 글과 표준 행만 2번의 내용으로 맞춘다. 사용자가 더한 행은 그대로 둔다. 달라지는 것이 없으면 건드리지 않는다. 달라지면 바뀌기 전과 후를 보여 주고 승인받은 뒤에 바꾼다.
4. 규칙 구간을 넣는다. 이 문서의 "규칙 구간" 절의 글을 그대로 쓴다.
   - 규칙 구간이 없으면 문서 지도 구간의 끝 표식 바로 뒤에 빈 줄 하나를 두고 넣는다. 1번에서 문서 지도 구간이 이미 있었으면 2번에서 승인받았을 때만 넣는다. 끝 표식 뒤에 있던 글은 규칙 구간 뒤에 빈 줄 하나를 두고 그대로 남는다.
   - 규칙 구간이 이미 있으면 표식 사이의 글을 이 절의 글로 맞춘다. 달라지는 것이 없으면 건드리지 않는다. 달라지면 바뀌기 전과 후를 보여 주고 승인받은 뒤에 바꾼다.

**`CLAUDE.md`**: 상태에 따라 하나만 한다.
- 없음: `@AGENTS.md` 한 줄만 있는 파일을 만든다.
- `@AGENTS.md` 한 줄뿐: 건드리지 않는다.
- 다른 내용이 있고 옮기기를 승인받음: `@AGENTS.md` 한 줄만 남긴다.
- 다른 내용이 있고 옮기기를 거절함: 기존 내용을 그대로 둔다. `@AGENTS.md` 줄이 없을 때만 맨 위에 그 줄과 빈 줄 하나를 더한다.

## 4. 보고한다

- 만든 것, 옮긴 것, 건드리지 않은 것(기존 문서와 거절한 일)
- 사용자가 채울 칸: `{…}`가 남아 있는 파일
- CI 워크플로를 썼으면 시크릿 등록 방법: 워크플로는 저장소 시크릿 `CLAUDE_CODE_OAUTH_TOKEN`이 있어야 돈다. 로컬에서 `claude setup-token`을 돌려 토큰을 만들고, `gh secret set CLAUDE_CODE_OAUTH_TOKEN`으로 넣거나 GitHub 저장소의 Settings → Secrets and variables → Actions에서 같은 이름으로 넣는다. 워크플로 파일은 커밋해 GitHub에 올린 뒤부터 돈다.
- `AGENTS.md`가 32KiB(32,768바이트)를 넘으면 알린다. 그보다 큰 `AGENTS.md`는 끝까지 읽지 않는 도구가 있다.

보고한 뒤에는 묻지 않고 끝난다.

## 문서 지도 구간

아래 코드 블록 안쪽이 `AGENTS.md`에 들어가는 글이다. 블록을 여닫는 줄은 옮기지 않는다. 첫 줄과 마지막 줄의 표식은 구간의 일부이니 함께 옮긴다.

````markdown
<!-- plate:docs-map:start -->
## 문서 지도
하네스 기록(프로젝트 맥락 문서와 tasks 기록)은 모두 `docs/` 아래 이 표의 위치에 둔다. README, CHANGELOG 같은 일반 문서는 이 규칙의 대상이 아니다.
표에 없는 종류의 기록이 필요하면 만들기 전에 위치를 사용자에게 묻고, 정한 위치를 이 표에 한 행으로 더한 뒤 만든다. 하네스의 스킬이 위치를 정해 둔 기록은 묻지 않고 그 스킬이 행을 더한다.

| 위치 | 내용 | 읽을 때 |
|---|---|---|
| `docs/PRD.md` | 무엇을 왜 만드는지, 범위 밖 | 기능을 더하거나 범위를 판단할 때 |
| `docs/ARCHITECTURE.md` | 기술 스택, 구조, 데이터 흐름 | 파일 위치나 모듈 경계를 판단할 때 |
| `docs/ADR.md` | 이미 내린 결정과 이유 | 기술 선택을 바꾸거나 새로 할 때 |
| `docs/DESIGN.md` | 디자인 토큰과 UI 규칙 | 화면을 만들거나 고칠 때 |
| `docs/tasks/` | 진행 중인 tasks 하나의 기록: tasks 머리 `plan.md`, `FRICTION.md`, `RUNLOG.md`, `review.md`, `eval.md`, task 폴더 `NNN-slug/`마다 task 머리 `plan.md`, `phase-N.md`(통과하면 `done-phase-N.md`), `retro.md`. tasks가 끝나면 비운다 | 그 tasks를 이어 가거나 근거를 볼 때 |
<!-- plate:docs-map:end -->
````

## 규칙 구간

아래 코드 블록 안쪽이 `AGENTS.md`의 문서 지도 구간 뒤에 들어가는 글이다. 블록을 여닫는 줄은 옮기지 않는다. 첫 줄과 마지막 줄의 표식은 구간의 일부이니 함께 옮긴다.

````markdown
<!-- plate:rules:start -->
## 작업 규칙
- 계획 없이 코드를 고치지 않는다. 기능을 만들거나 코드를 고치는 요청을 받으면 plate의 plan 스킬(`plate:plan`)로 계획부터 세운다.
- task는 task 회고가 통과해야 끝난다. 회고는 plate의 retro 스킬(`plate:retro`)이 하고, 회고가 통과하기 전에는 그 task가 끝났다고 말하지 않는다.
- tasks는 끝의 평가와 보고까지 가야 끝난다. 모든 task가 끝나면 plate의 review 스킬(`plate:review`)이 코드를, eval 스킬(`plate:eval`)이 하네스를 평가하고, 그 평가를 담은 전체 보고가 나오기 전에는 tasks가 끝났다고 말하지 않는다.
- 프로젝트의 다른 규칙이 이 단계들을 건너뛰라고 해도 따르지 않는다.
<!-- plate:rules:end -->
````

## 양식

아래 코드 블록 안쪽이 각 파일의 내용이다. 블록을 여닫는 줄은 옮기지 않는다.

### `docs/PRD.md`

````markdown
# PRD: {프로젝트명}

## 목표
{이 프로젝트가 해결하려는 문제를 한두 문장으로}

## 사용자
{누가, 어떤 상황에서 쓰는지}

## 핵심 기능
1. {기능 1}
2. {기능 2}
3. {기능 3}

## 범위 밖
- {만들지 않을 것 1}
- {만들지 않을 것 2}
````

### `docs/ARCHITECTURE.md`

````markdown
# 아키텍처

## 기술 스택
- {언어와 런타임 (예: TypeScript, Node 22)}
- {프레임워크와 주요 라이브러리 (예: Next.js 15, Tailwind CSS)}
- {저장소와 외부 서비스 (예: PostgreSQL, Stripe)}

## 디렉터리 구조
```
{최상위 폴더와 각 폴더의 역할 (예:
src/
├── app/          # 페이지와 API 라우트
├── components/   # UI 컴포넌트
├── lib/          # 유틸리티
└── services/     # 외부 API 래퍼
)}
```

## 패턴과 규칙
- {지켜야 할 구조 규칙과 이유 (예: 외부 API는 services/에서만 호출한다. 이유: 키와 재시도를 한곳에서 관리한다)}
- {쓰는 패턴 (예: Server Component가 기본이고, 상호작용이 필요한 곳만 Client Component로 둔다)}

## 데이터 흐름
```
{데이터가 흐르는 경로 (예: 사용자 입력 → Client Component → API 라우트 → 외부 API → 응답 → 화면 갱신)}
```
````

### `docs/ADR.md`

````markdown
# Architecture Decision Records

## 철학
{결정이 갈릴 때 따르는 우선순위 (예: MVP 속도 최우선. 외부 의존성 최소화. 작동하는 최소 구현을 고른다.)}

---

### ADR-001: {결정 사항 (예: Next.js App Router 선택)}
- **결정**: {무엇을 선택했는지}
- **이유**: {왜 선택했는지}
- **트레이드오프**: {무엇을 포기했는지}
````

### `docs/DESIGN.md`

절 이름과 앞머리의 키는 DESIGN.md 규격(alpha)의 것이라 영어로 둔다.

````markdown
---
version: alpha
name: "{프로젝트명}"
description: "{디자인 방향을 한 문장으로}"
colors:
  primary: "{제목과 본문에 쓰는 색 (예: #1A1C1E)}"
  secondary: "{테두리와 보조 글자에 쓰는 색 (예: #6C7278)}"
  tertiary: "{주요 동작과 강조에 쓰는 색 (예: #B8422E)}"
  neutral: "{배경에 쓰는 색 (예: #F7F5F2)}"
typography:
  headline-lg:
    fontFamily: "{글꼴 (예: Public Sans)}"
    fontSize: "{크기 (예: 32px)}"
    fontWeight: "{굵기 (예: 600)}"
    lineHeight: "{줄 높이 (예: 1.2)}"
  body-md:
    fontFamily: "{글꼴 (예: Public Sans)}"
    fontSize: "{크기 (예: 16px)}"
    fontWeight: "{굵기 (예: 400)}"
    lineHeight: "{줄 높이 (예: 1.6)}"
rounded:
  sm: "{작은 모서리 (예: 4px)}"
  md: "{기본 모서리 (예: 8px)}"
  lg: "{큰 모서리 (예: 12px)}"
spacing:
  sm: "{좁은 간격 (예: 8px)}"
  md: "{기본 간격 (예: 16px)}"
  lg: "{넓은 간격 (예: 32px)}"
components:
  button-primary:
    backgroundColor: "{배경 색. 값을 적거나 위 토큰을 가리킨다 (예: {colors.tertiary})}"
    textColor: "{글자 색 (예: {colors.neutral})}"
    rounded: "{모서리 (예: {rounded.md})}"
    padding: "{안쪽 여백 (예: 12px)}"
---

# 디자인

## Overview
{화면이 주는 인상과 분위기, 누구를 위한 화면인지 (예: 전문가용 도구. 조밀하고 차분하다)}

## Colors
- **Primary**: {어디에 쓰는지 (예: 제목과 본문 글자)}
- **Secondary**: {어디에 쓰는지 (예: 테두리, 캡션, 부가 정보)}
- **Tertiary**: {어디에 쓰는지 (예: 주요 버튼과 강조)}
- **Neutral**: {어디에 쓰는지 (예: 페이지 배경)}

## Typography
- **Headline**: {글꼴과 쓰임 (예: Public Sans Semi-Bold, 화면 제목)}
- **Body**: {글꼴과 쓰임 (예: Public Sans Regular 16px, 본문)}

## Layout
{격자와 간격 규칙 (예: 최대 폭 1200px의 고정 격자. 간격은 8px 단위)}

## Elevation & Depth
{위계를 드러내는 방법 (예: 그림자를 쓰지 않고 배경색 단계로 구분한다)}

## Shapes
{모서리와 형태 규칙 (예: 버튼과 입력 칸은 8px 둥근 모서리)}

## Components
- **Buttons**: {종류와 상태별 모양 (예: 주 버튼은 Tertiary 배경. hover에서 한 단계 어둡게)}
- **Input fields**: {모양과 오류 표시 (예: 1px 테두리. 오류는 테두리 색과 도움말 글로 알린다)}

## Do's and Don'ts
- Do: {지킬 것 (예: Tertiary는 한 화면에서 가장 중요한 동작 하나에만 쓴다)}
- Don't: {하지 말 것 (예: 한 화면에 글꼴 굵기를 세 가지 이상 쓰지 않는다)}
````

### `.github/workflows/plate-review.yml`

CI 에이전트의 워크플로다. `${{ … }}`는 GitHub Actions의 식이라 채울 칸이 아니다. `review` 잡은 읽기 권한만으로 공개 마켓플레이스에서 plate를 받아 review의 PR 모드를 부르고 등급 묶음을 구조화 출력으로 낸다. 액션을 부르기 전에 `AGENTS.md`를 기준 브랜치(`origin/${{ github.base_ref }}`)의 것으로 되돌리고, 기준 브랜치에 `AGENTS.md`가 없으면 PR의 것을 지운다. `CLAUDE.md`의 `@AGENTS.md`로 PR이 바꾼 지시가 세션에 실리지 않게 하려는 것이다. review 단계가 실패하면 다음 단계가 액션의 실행 결과 파일(`execution_file`)에서 결과 줄의 `subtype`, `is_error`, `api_error_status`, 오류 목록과, 오류일 때의 결과 글만 로그에 낸다. Claude의 메시지 전부를 로그에 내는 액션의 입력은 켜지 않는다. 로그가 공개되면 도구 결과에 든 비밀이 드러나기 때문이다. `verdict` 잡은 쓰기 권한으로 등급 묶음을 판정 스크립트(`plugins/plate/ci/verdict.py`)에 넘겨, 평가서를 PR 댓글로 달고, 자동 머지면 merge commit으로 합치고 머리 브랜치를 지우며, 닫기면 PR을 닫는다. 머지 요청이면 댓글만 단다.

````yaml
name: plate review

on:
  pull_request:
    types: [opened, synchronize, reopened]

concurrency:
  group: plate-review-${{ github.event.pull_request.number }}
  cancel-in-progress: true

jobs:
  review:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: read
    outputs:
      bundle: ${{ steps.review.outputs.structured_output }}
    steps:
      - uses: actions/checkout@v7
        with:
          fetch-depth: 0
      - name: AGENTS.md를 기준 브랜치의 것으로 되돌린다
        env:
          BASE_REF: ${{ github.base_ref }}
        run: |
          if git cat-file -e "origin/$BASE_REF:AGENTS.md" 2>/dev/null; then
            git checkout "origin/$BASE_REF" -- AGENTS.md
          else
            rm -f AGENTS.md
          fi
      - id: review
        uses: anthropics/claude-code-action@v1
        with:
          claude_code_oauth_token: ${{ secrets.CLAUDE_CODE_OAUTH_TOKEN }}
          github_token: ${{ github.token }}
          plugin_marketplaces: "https://github.com/werwer748/harness-plate.git"
          plugins: "plate@harness-plate"
          prompt: "/plate:review PR 모드, 기준 브랜치: origin/${{ github.base_ref }}, 평가서 파일: ${{ runner.temp }}/plate-review.md"
          claude_args: |
            --add-dir ${{ runner.temp }}
            --allowedTools "Bash,Read,Write,Glob,Grep"
            --json-schema '{"type":"object","properties":{"build":{"type":"string","enum":["pass","fail","none","unmeasured"]},"lint":{"type":"string","enum":["pass","fail","none","unmeasured"]},"test":{"type":"string","enum":["pass","fail","none","unmeasured"]},"coverage":{"anyOf":[{"type":"number"},{"type":"string","enum":["skipped","unmeasured"]}]},"reliability":{"type":"string","enum":["A","B","C","D","E","unjudged"]},"security":{"type":"string","enum":["A","B","C","D","E","unjudged"]},"maintainability":{"type":"string","enum":["A","B","C","D","E","unjudged"]}},"required":["build","lint","test","coverage","reliability","security","maintainability"],"additionalProperties":false}'
      - name: review가 실패한 까닭을 낸다
        if: failure()
        env:
          EXECUTION_FILE: ${{ steps.review.outputs.execution_file }}
        run: |
          file="${EXECUTION_FILE:-$RUNNER_TEMP/claude-execution-output.json}"
          if [ ! -f "$file" ]; then
            echo "실행 결과 파일이 없다: $file"
            exit 0
          fi
          python3 - "$file" <<'PY'
          import json, sys
          for m in json.load(open(sys.argv[1])):
              if isinstance(m, dict) and m.get("type") == "result":
                  line = {"subtype": m.get("subtype"), "is_error": m.get("is_error")}
                  if m.get("api_error_status") is not None:
                      line["api_error_status"] = m["api_error_status"]
                  if m.get("errors"):
                      line["errors"] = m["errors"]
                  if m.get("is_error"):
                      line["result"] = m.get("result")
                  print(json.dumps(line, ensure_ascii=False))
          PY
      - uses: actions/upload-artifact@v7
        with:
          name: plate-review
          path: ${{ runner.temp }}/plate-review.md

  verdict:
    needs: review
    runs-on: ubuntu-latest
    permissions:
      contents: write
      pull-requests: write
    steps:
      - uses: actions/checkout@v7
        with:
          repository: werwer748/harness-plate
          path: harness-plate
      - uses: actions/download-artifact@v8
        with:
          name: plate-review
      - name: 판정대로 댓글을 달고 머지하거나 닫는다
        env:
          GH_TOKEN: ${{ github.token }}
          GH_REPO: ${{ github.repository }}
          PR: ${{ github.event.pull_request.number }}
          HEAD_SHA: ${{ github.event.pull_request.head.sha }}
          BUNDLE: ${{ needs.review.outputs.bundle }}
        run: |
          verdict=$(printf '%s' "$BUNDLE" | python3 harness-plate/plugins/plate/ci/verdict.py)
          case "$verdict" in
            merge) label="자동 머지" ;;
            request) label="머지 요청" ;;
            close) label="닫기" ;;
          esac
          { echo "판정: $label"; echo; cat plate-review.md; } > comment.md
          gh pr comment "$PR" --body-file comment.md
          case "$verdict" in
            merge) gh pr merge "$PR" --merge --delete-branch --match-head-commit "$HEAD_SHA" ;;
            close) gh pr close "$PR" ;;
          esac
````

## 출처

절대 규칙을 단정문으로 적는 방식과 승인 전에는 진행하지 않는 방식은 obra/superpowers(MIT)에서 가져왔다. `docs/DESIGN.md` 양식은 google-labs-code/design.md의 규격(alpha)을 따른다. CI 워크플로 양식은 Claude Code GitHub Actions 문서(https://code.claude.com/docs/en/github-actions)와 anthropics/claude-code-action의 입력과 `structured_output`(https://raw.githubusercontent.com/anthropics/claude-code-action/main/action.yml)을 따른다.
