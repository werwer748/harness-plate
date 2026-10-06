# 레일 1단계 설계: 플러그인 뼈대 + 셋업 스킬

> 진행 순서와 체크는 [TODO.md](TODO.md)에 있다. 이 파일은 TODO를 하다가 "무엇을, 왜, 어떤 규격으로"가 필요할 때 읽는다.

## 배경

프로젝트 지침을 품은 하네스를 새로 만든다. 지금까지의 실패는 둘이었다: 하네스가 완성되지 않았고(결정만 쌓임), 결과물이 의도와 달랐다(구현 목표 불명확). 그래서 큰 계획을 한 번에 확정하지 않고, 5단계(셋업 → 맥락 → 계획 → 실행 → 검증)를 **하나씩 완성**한다. 각 단계 앞에서 질문 라운드를 다시 연다.

하네스는 "레일"이다. 같은 규격으로 물품을 찍어내고, 레일을 돌리는 프로그램(Claude Code, Codex, Grok Build)이 바뀌어도 똑같이 작동한다. 그래서 레일 규격(단계 순서, 기록 위치와 형식, 통과 조건)은 도구에 기대지 않는 파일로 두고, 서브에이전트와 훅은 도구별 구현으로 둔다.

1단계의 결과물은 두 도구에 설치되는 플러그인 뼈대와, 대상 프로젝트에 md 위치 기준을 세우는 셋업 스킬이다.

## 범위

| 포함 | 제외 (해당 단계에서 다시 질문) |
|---|---|
| 레포 준비(옛 내용은 태그로 보존) | 맥락 채우기 스킬 (2단계) |
| Claude Code용·Codex용 매니페스트 | 계획·실행·검증 스킬, 작업 기록 양식 (3~5단계) |
| 셋업 스킬 1개 (본문 공유) | 훅 전부 (옛 branch-guard, constitution 포함) |
| 빈 폴더 + excel-viewer 복제본에서 두 도구로 확인 | Grok Build 확인 (설치한 시점의 단계부터) |
| 하네스 레포에 자기 셋업 적용, 결정을 ADR로 기록 | `main` 교체와 GitHub 푸시 (1단계 뒤 따로 확인) |

## 만들 파일

```
harness-plate/                          # 브랜치 rail
  .claude-plugin/marketplace.json       # Claude Code 목록
  .agents/plugins/marketplace.json      # Codex 목록
  plugins/plate/
    .claude-plugin/plugin.json          # version 0.4.0
    .codex-plugin/plugin.json
    skills/setup/SKILL.md               # 본문 하나, 두 도구가 공유
  README.md                             # 두 도구의 설치 명령만 (최소)
  AGENTS.md, CLAUDE.md, docs/…          # E 묶음에서 자기 셋업으로 생성
```

## 셋업 스킬 규격

**쓰는 방식**
- 한국어. 도구 이름 대신 동작으로 쓴다("사용자에게 묻는다", "파일을 옮긴다"). 세 도구가 같은 본문을 쓴다.
- 양식은 본문 안에 넣는다. 별도 파일로 두면 대상 프로젝트의 작업 디렉터리 밖이라 읽기가 거부된 전례가 있다.
- superpowers에서 기법만 가져온다(MIT, 출처 표기): 절대 규칙 문장, 승인 전 진행 금지.

**절차**
1. **현재 상태를 본다.** git 레포 여부, 파일 목록, `AGENTS.md`·`CLAUDE.md`·`docs/`, 같은 역할의 기존 문서, 빈 프로젝트 여부, UI 프로젝트 여부. 판정 기준은 본문에 목록으로 적어 도구마다 결과가 갈리지 않게 한다.
   - 같은 역할 문서 후보: 이름 목록(`SPEC.md`, `REQUIREMENTS.md`, `docs/architecture.md`, `DECISIONS.md`, `docs/adr/`, `UI_GUIDE.md` 등)으로 찾고 내용을 읽어 확인한다.
   - UI 프로젝트: UI 프레임워크 의존성이나 화면 파일(`.tsx`, `.jsx`, `.vue`, `.svelte`, `.html`, `.css`)이 있을 때.
2. **할 일을 표 하나로 보여 주고 한 번에 묻는다.** 물을 것이 없으면 묻지 않는다.
   - 파일 하나로 된 같은 역할 문서: 표준 위치로 옮길지 (문서마다)
   - 내용이 있는 `CLAUDE.md`: 내용을 `AGENTS.md`로 옮길지
   - git 레포가 아닐 때: `git init` 할지
   - 빈 프로젝트일 때: 화면이 있는 프로젝트인지
3. **승인받은 것만 실행한다.**
   - 승인한 문서를 옮긴다. 거절한 문서와 여러 파일로 나뉜 문서(`docs/adr/` 등)는 그대로 두고 지도에 실제 경로를 적는다.
   - 없는 양식만 만든다: `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, UI 프로젝트면 `docs/DESIGN.md`. `docs/tasks/.gitkeep`도 만든다.
   - `AGENTS.md`에 문서 지도 구간을 넣는다. 구간이 이미 있으면 표준 행만 갱신하고 사용자가 더한 행은 유지하며, 바뀔 내용을 보여 주고 승인받는다.
   - `CLAUDE.md`는 `@AGENTS.md` 한 줄로 만든다. 내용 이동을 거절했으면 기존 내용을 두고 맨 위에 `@AGENTS.md`만 더한다.
4. **보고한다.** 만든 것, 옮긴 것, 건드리지 않은 것, 사용자가 채울 칸. `AGENTS.md`가 32KiB(Codex 상한)를 넘으면 알린다.

**절대 규칙**: 승인 없이 기존 파일을 옮기거나 덮어쓰지 않는다. 양식을 추측으로 채우지 않는다(채우기는 2단계). 빈 프로젝트에는 양식을 한 글자도 바꾸지 않고 옮긴다. 커밋하지 않는다.

**양식**
- PRD·ARCHITECTURE·ADR: 옛 `init` 스킬의 양식 절을 그대로 쓴다 (`git show legacy-0.3.0:plugins/plate/skills/init/SKILL.md`).
- DESIGN: Google DESIGN.md 규격(alpha)을 따른다. 앞머리 키는 `version`, `name`, `description`, `colors`, `typography`, `rounded`, `spacing`, `components`. 본문 절은 Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, Do's and Don'ts 순서.

**문서 지도 구간** (`AGENTS.md`에 들어가는 글. `docs/DESIGN.md` 행은 UI 프로젝트일 때만 넣는다)

```markdown
<!-- plate:docs-map:start -->
## 문서 지도
하네스 기록(프로젝트 맥락 문서와 작업 기록)은 모두 `docs/` 아래 이 표의 위치에 둔다. README, CHANGELOG 같은 일반 문서는 이 규칙의 대상이 아니다.
표에 없는 종류의 기록이 필요하면 만들기 전에 위치를 사용자에게 묻고, 정한 위치를 이 표에 한 행으로 더한 뒤 만든다.

| 위치 | 내용 | 읽을 때 |
|---|---|---|
| `docs/PRD.md` | 무엇을 왜 만드는지, 범위 밖 | 기능을 더하거나 범위를 판단할 때 |
| `docs/ARCHITECTURE.md` | 기술 스택, 구조, 데이터 흐름 | 파일 위치나 모듈 경계를 판단할 때 |
| `docs/ADR.md` | 이미 내린 결정과 이유 | 기술 선택을 바꾸거나 새로 할 때 |
| `docs/DESIGN.md` | 디자인 토큰과 UI 규칙 | 화면을 만들거나 고칠 때 |
| `docs/tasks/NNN-slug/` | 작업 하나의 기록: `plan.md`, `phase-N.md`, `verify.md` | 그 작업을 이어 가거나 근거를 볼 때 |
<!-- plate:docs-map:end -->
```

## 완성 판정 기준

시험 폴더는 `/tmp/plate-rail-test`에 만든다(세션 임시 폴더는 실행 도중 회수된 일이 있어 쓰지 않는다). 원본 프로젝트는 건드리지 않는다.
- 빈 폴더 2개 (`empty-claude`, `empty-codex`)
- `~/Desktop/vibe2/excel-viewer`의 로컬 복제본 4개 (`ev-claude`, `ev-codex`, `ev-refuse`, `ev-refuse2`). `ev-refuse2`는 `CLAUDE.md`에서 `@AGENTS.md` 줄을 지워 복제본 안에서 커밋해 둔 변형이다. 이 프로젝트에는 `AGENTS.md`(4.4KB)와 내용이 있는 `CLAUDE.md`(0.9KB)가 있고 `docs/`가 없다.

실행은 헤드리스로 하고 물음의 답을 프롬프트에 미리 준다(Claude Code는 `claude -p --plugin-dir …`, Codex는 `codex exec --sandbox workspace-write …`). 두 도구에 같은 답을 준다.

| # | 확인 | 방법 |
|---|---|---|
| 1 | 빈 폴더에 정해진 파일만 생긴다: `AGENTS.md`, `CLAUDE.md`, `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/tasks/.gitkeep` | 파일 목록 |
| 2 | **빈 폴더 결과가 두 도구에서 한 글자도 다르지 않다** | `diff -r --exclude=.git empty-claude empty-codex`가 비어 있음 |
| 3 | `CLAUDE.md` 내용이 `@AGENTS.md` 한 줄이다 | 파일 내용 |
| 4 | excel-viewer 복제본(옮기기 승인): 기존 `CLAUDE.md` 내용이 `AGENTS.md`로 갔고, 기존 `AGENTS.md` 내용은 그대로이며, `README.md`·`TODO.md`는 바뀌지 않았다 | `git diff`, `git status` |
| 5 | excel-viewer 결과가 두 도구에서 파일 목록·위치·지도 구간이 같다 | `git status --porcelain` 비교, 지도 구간 diff |
| 6 | 다시 돌려도 변화가 없다 | 각 폴더에서 재실행 뒤 `git status`, diff |
| 7 | 거절 경로(Claude Code만): 기존 `CLAUDE.md` 내용이 남는다. `@AGENTS.md` 줄이 이미 있으면(`ev-refuse`, 원래 복제본) `CLAUDE.md`가 바뀌지 않고, 없으면(`ev-refuse2`, 그 줄을 지운 변형) 맨 위에 그 줄만 더해진다 | `git diff` |
| 8 | Claude Code 서브에이전트에도 문서 지도가 실린다 | 셋업한 폴더에서 서브에이전트에게 작업 기록 위치를 묻는다 |

## 아직 확인하지 못한 것 (구현 중 확인)

- DESIGN.md 규격은 alpha라 절 구성이 바뀔 수 있다

## 확인해 둔 사실

- Claude Code 2.1.291은 `--plugin-dir <path>`로 폴더의 플러그인을 그 세션에만 불러온다. 남아 있는 plate 0.3.0 설치 기록과 마켓플레이스 등록을 건드리지 않고 개발할 수 있다.
- Codex 0.160.0은 `codex plugin marketplace add`(로컬 경로 가능) 뒤 `codex plugin add plate@<이름>`으로 설치한다. 세션 한정 옵션은 없다. 등록과 설치는 확인 뒤에도 그대로 둔다.
- Codex 매니페스트(B 묶음에서 확인, 근거: developers.openai.com/plugins/build/plugins.md, `obra/superpowers`의 `.codex-plugin/plugin.json`과 `.agents/plugins/marketplace.json`):
  - `plugins/plate/.codex-plugin/plugin.json`은 `name`, `version`, `description`, `author`, `repository`, `"skills": "./skills/"`만으로 Codex 0.160.0에 설치된다. `interface`(표시 이름, 아이콘 등)는 없어도 된다.
  - `.agents/plugins/marketplace.json`은 최상위에 `name`, `interface.displayName`, `plugins[]`를 두고, 항목마다 `name`, `source`(`"source": "local"`, `"path": "./plugins/plate"`), `policy.installation`, `policy.authentication`, `category`를 둔다.
  - 스킬 이름은 두 도구에서 같은 `plate:setup`이다. Claude Code는 `/plate:setup`, Codex는 `$plate:setup`으로 부른다. 둘 다 헤드리스에서 확인했다.
  - Codex는 설치할 때 플러그인을 `~/.codex/plugins/cache/harness-plate/plate/0.4.0/`으로 복사해 그 사본을 읽는다. 스킬을 고치면 설치본을 갱신해야 한다.
  - 공식 문서는 새 패키지에 플러그인 루트의 `plugin.json`(Agent Plugins 규격)을 권하고 `.codex-plugin/plugin.json`은 호환용이라고 적는다(지원은 계속된다). Codex가 Claude 형식 매니페스트와 `.claude-plugin/marketplace.json`도 읽는다고 적혀 있으나 직접 확인하지 않았다. 지금은 계획대로 `.codex-plugin`을 쓴다.
- 헤드리스 실행(D 묶음에서 확인):
  - 답을 프롬프트에 미리 주면 두 도구 모두 다시 묻지 않는다. 빈 폴더와 excel-viewer 복제본(옮기기 승인) 모두 두 도구의 결과 폴더가 바이트 단위로 같았다.
  - Codex의 `workspace-write` 샌드박스는 `.git` 쓰기를 막는다. 빈 폴더에서 `git init`이 실패하고, Codex는 실패를 보고한 뒤 나머지를 끝낸다.
  - Codex 설치본은 `codex plugin add plate@harness-plate`를 다시 실행하면 최신 스킬로 갱신된다.
  - excel-viewer의 `CLAUDE.md`에는 이미 `@AGENTS.md` 줄이 있다(3번째 줄). 거절 경로에서 스킬은 그 줄을 다시 더하지 않아 `CLAUDE.md`가 바뀌지 않는다.
- Claude Code는 `CLAUDE.md`가 없을 때만 `AGENTS.md`를 읽는다. 그래서 `@AGENTS.md` 임포트를 항상 둔다. Codex와 Grok Build는 `AGENTS.md`를 자동으로 읽는다.
- Grok Build(1.0.46)는 이 Mac에 없다. Claude 형식 플러그인을 그대로 읽지만 종료 차단 훅이 없다.
- 옛 GitHub 레포는 지워져 있었다. 2026-10-06에 같은 이름의 비공개 레포로 다시 만들었고, `main`은 옛 0b24d71의 파일 내용을 옮긴 부모 없는 커밋 3c8bcb6이다(트리 해시가 옛 것과 같다. 이전 커밋 이력과 PR 기록은 없다). 원본은 `~/.claude/plugins/marketplaces/harness-plate`의 얕은 클론이었다.

## 다음 단계에서 물을 것 (지금 확정하지 않음)

- 2단계: 맥락 채우기의 질문 방식과 종료 조건, 다시 채우기
- 3단계: 계획 단계의 질문 방식, `plan.md` 필수 항목, 작은 작업의 최소 형태, 사람 승인 지점
- 4단계: `phase-N.md` 필수 항목, 서브에이전트 보고 규약, 도구별 서브에이전트 정의
- 5단계: 검증 주체와 증거 형식, 훅 2개의 발동 조건과 탈출구, 종료 차단 훅이 없는 Grok Build에서 "검증 증거 없이는 완료 불가"를 지키는 방법

## 결정 원장 (E 묶음에서 ADR의 원본으로 쓴다)

| # | 결정 | 질문 |
|---|---|---|
| 1 | 완전히 새로 시작한다. 옛 plate v0.3.0과 그 결정 기록은 구속력이 없다 | Q1 |
| 2 | 예외 없이 모든 작업이 파이프라인을 거친다 | Q2 |
| 3 | 강제로 막을 실패는 둘: 긴 세션 컨텍스트 팽창, 검증 없는 완료 선언 | Q3 |
| 4 | 2단 구조: 바깥은 고정 단계(계획 → 실행 → 검증), 실행 안쪽은 계획이 정한 N개 phase. phase마다 에이전트와 기록 | Q4 |
| 5 | 실패의 정체: 하네스가 완성되지 않음, 결과물이 의도와 다름 | Q5 |
| 6 | 설계 과정은 큰 계획을 한 번에 확정하지 않고, 단계마다 질문을 많이 해 구현 목표를 명확히 한다 | Q1 메모, Q6 |
| 7 | 배포는 플러그인 + 셋업 스킬 | Q7 |
| 8 | 실행 phase는 메인이 조율하고 phase마다 새 컨텍스트의 에이전트가 수행한다. 질문과 승인은 메인이 맡는다 | Q8 |
| 9 | 단계별로 하나씩 완성한다(셋업 → 맥락 → 계획 → 실행 → 검증) | Q9 |
| 10 | 하네스 기록은 모두 `docs/` 아래. 맥락은 `docs/*.md`, 작업 기록은 `docs/tasks/NNN-slug/{plan,phase-N,verify}.md` | Q10 |
| 11 | 작업 기록은 git에 커밋해 보존한다 | Q11 |
| 12 | 맥락 채우기는 스캔 + 질문 라운드. 추측으로 적지 않는다 | Q12 |
| 13 | 첫 단계는 플러그인 뼈대 + 셋업만 | Q13 |
| 14 | 위치 규칙은 프로젝트 `AGENTS.md`에, `CLAUDE.md`에는 `@AGENTS.md` 임포트만 | Q14, Q18 |
| 15 | 같은 역할의 기존 문서는 표준 위치로 옮기기를 제안하고 승인받은 것만 옮긴다 | Q15 |
| 16 | 문서 양식은 옛 plate 것 그대로 | Q16 |
| 17 | 레일 구상: 도구가 바뀌어도 같은 규격. 우선 Claude Code, Codex, Grok Build에 맞추고 이후 넓힌다 | Q17 |
| 18 | 내용이 있는 기존 `CLAUDE.md`는 `AGENTS.md`로 옮기기를 제안한다 | Q19 |
| 19 | 셋업은 git 레포가 아니면 `git init`을 제안한다. UI 프로젝트면 디자인 문서를 만든다 | Q20 |
| 20 | 각 단계는 Claude Code에서 만들고 Codex에서 같은 결과를 확인해야 완성이다. Grok Build는 설치한 시점부터 | Q21 |
| 21 | 디자인 문서는 `docs/DESIGN.md`(Google 규격), UI 프로젝트일 때만 만든다 | Q22, Q23 |
| 22 | 기존 레포를 쓰고 옛 내용은 태그로 남긴다. `main` 교체는 1단계 뒤 따로 확인 | Q24 |
| 23 | 위치 규칙은 하네스 기록에만 적용한다 | Q25 |
| 24 | 지도에 없는 기록은 위치를 묻고 지도에 행을 더한 뒤 만든다 | Q26 |
| 25 | 지도는 표식 구간만 교체한다 | Q27 |
| 26 | 완성 판정은 빈 폴더 + 기존 프로젝트 복제본에서 실제 실행 + 체크리스트 | Q28 |
| 27 | 스킬 본문은 하나, 도구별 매니페스트가 같은 폴더를 가리킨다 | Q29 |
| 28 | superpowers는 설치하지 않고 기법만 가져온다 | Q30 |
| 29 | 옛 훅 2개는 1단계에 가져오지 않는다 | Q31 |
| 30 | 결정은 하네스 레포에 자기 셋업을 적용해 `docs/ADR.md`에 남긴다 | Q32 |
| 31 | 새 브랜치에서 옛 파일은 전부 지운다 | Q33 |
| 32 | 여러 파일로 나뉜 기존 문서는 합치지 않고 지도에 경로만 적는다 | Q34 |
| 33 | Codex 확인용 로컬 마켓플레이스 등록과 설치는 그대로 둔다 | Q35 |
| 34 | 일치 기준: 빈 폴더는 완전 일치, 기존 프로젝트는 파일 목록·위치·지도 구간 일치 | Q36 |
| 35 | 양이 많은 계획은 `plan.md`와 `TODO.md`로 나누고, 구현은 새 세션에서 TODO를 체크하며 진행한다 | 계획 승인 때 |
| 36 | GitHub 레포가 지워져 있어 같은 이름의 비공개 레포로 다시 만들고, 옛 파일을 커밋 하나로 `main`에 올린다 | 구현 중 (A1) |
| 37 | 거절 경로에서 `CLAUDE.md`에 `@AGENTS.md` 줄이 이미 있으면 다시 더하지 않는다 | 구현 중 (D7) |
| 38 | 시험 폴더는 `/tmp/plate-rail-test`에 둔다 | 구현 중 (D6) |
| 39 | `plan.md`와 `TODO.md`는 `docs/tasks/001-setup/`에 두고 문서 지도에 행을 더하지 않는다. v1.0이 되면 모두 지운다 | 구현 중 (E3) |

가정으로 둔 것: 개인용, 문서와 스킬은 한국어, 플러그인 이름 `plate`, 스킬 `/plate:setup`, 작업 폴더 `NNN-slug`, 버전 0.4.0, 브랜치 `rail`, 태그 `legacy-0.3.0`.
