# harness-plate 핸드오프 — 하네스 작업 순환 6축 설계 검토

> 작성: 2026-09-29. 개정: 2026-10-04([ADVISE.md](./ADVISE.md) 검토와 재조사 반영). 2026-10-04에 문서를 나눴다. 이 파일은 매 세션에 읽는 진입점이고, 본문은 아래 "문서 지도"의 파일에 있다. 하네스 작업이 끝나면 이 파일은 지운다. 에이전트가 예외 없이 지킬 규칙은 여기에 적지 않고 [plugins/plate/AGENTS.md](plugins/plate/AGENTS.md)에만 적는다.

## 다음 세션 시작하기

- 시작 프롬프트 예: **`HANDOFF.md 읽고 긴 세션 대응부터 정하자`**
- 순서가 바뀌었다. 6축을 모두 결정한 뒤 만드는 대신, 최소 기본 흐름을 먼저 돌리고 확인된 실패에만 장치를 더한다. [docs/rules.md](docs/rules.md)의 "진행 방식"에 있다.
- 열려 있던 결정은 2026-10-04에 모두 정했고, M4의 토큰 합산도 같은 날 구현했다(`session-report.py --all`).
- 캐시 읽기가 가장 컸던 2026-09-22 세션 둘의 원인을 2026-10-06에 확인했다. 둘 다 긴 세션이다. `vibe2`의 `0bdd86bf`(87.5M)는 여러 작업을 한 세션에 이어 요청당 컨텍스트가 106K에서 534K로 자랐고, `excel-viewer`의 `8271817f`(139.5M)는 메인이 82K에서 478K로 자랐다. `8271817f`에는 위임도 있었다. 조사를 맡긴 general-purpose 에이전트 하나가 하위 에이전트를 다시 띄워 3단계 9개가 됐고 87.8M을 썼다(같은 세션의 Explore 4개와 claude-code-guide 1개는 합쳐 1.6M). 반복 탐색과 같은 검사의 재실행은 원인이 아니었다.
- 남은 것은 긴 세션(2회)의 대응 결정이다. 사용자가 2026-10-06에 다음 세션으로 미뤘다. 선택지는 둘이다: 장치 없이 관찰하거나(`/clear` 규칙은 2026-10-04에 적었고 두 세션은 그 전 것이다. 그 뒤 이 레포 세션은 최대 8.8M이다), `plate`에 컨텍스트 경고 훅을 더한다. 위임은 1회라 장치를 더하지 않고 지켜본다.
- 설치본을 0.2.0으로 올린 뒤 재시작하지 않았다. 다음 세션에서 `/plate:init`이 뜨는지 확인한다.
- `plate` 0.3.0(작업 헌법)은 아직 설치본에 반영하지 않았다. `main`에 합친 뒤 업데이트 명령([1축](docs/axes/1-structure.md) 1번)으로 반영하고 재시작해, 새 세션에 작업 헌법이 실리는지 확인한다.
- 원문 발췌는 부록 A–G([docs/references.md](docs/references.md))에, 2026-10-04 재조사 결과는 부록 H([docs/research-2026-10-04.md](docs/research-2026-10-04.md))에 있으므로 레포와 문서를 다시 뒤질 필요가 없다. 더 깊이 볼 때만 다시 받는다.

## 지금까지 합의된 것

- **목표**: 두 레퍼런스를 참고해 개인 하네스를 `~/Desktop/harness-plate`에 만들고, 꾸준히 업데이트하며 쓴다. 가능 여부는 확인했다.
- **기준은 하네스 작업 순환 6축이다** (사용자가 정의함):
  1. **구조 설계**: 폴더 / 도구 / 경계
  2. **맥락 설계**: 설정 상속 / CLAUDE.md / Progressive Disclosure
  3. **계획하기**: 계획 / 실행 / 검증
  4. **실행하기**: 혼자 / Subagent / Team / Ralph Loop
  5. **검증하기**: Generator/Evaluator 분리 / 모델 교차검증
  6. **개선**: 단순화. 그 결과는 다시 1축으로 돌아간다
- **6축의 지위** (2026-10-04): 6축은 설계를 검토하는 틀이다. 모든 작업이 거쳐야 하는 실행 절차가 아니다.
- **기본 원칙** (2026-10-04): 일반 작업은 메인 에이전트가 한 세션에서 직접 끝낸다. 추가 절차는 필요 조건이 있을 때만 켠다. [docs/rules.md](docs/rules.md)의 "기본 흐름과 확장 조건"에 있다.
- **작업 방식** (2026-10-04 변경): 구현 규칙([docs/rules.md](docs/rules.md))을 기준으로 하네스를 조금씩 만든다. 파일 작업은 사용자가 지시할 때만 한다.
- **배포 형태** (2026-10-04 결정): 플러그인이다. 이 레포가 마켓플레이스이고 플러그인 `plate`는 `plugins/plate/`에 있다([1축](docs/axes/1-structure.md) 1번). 쓸 프로젝트에 프로젝트 범위로만 설치하고, 하네스 때문에 전역 Claude 설정을 고치지 않는다. 플러그인 파일을 고치는 PR은 `plugin.json`의 version을 올린다. v0.1 범위는 기본 흐름과 기록으로 정했다.
- **현재 상태**: `harness-plate`는 공개 git 레포다(https://github.com/werwer748/harness-plate). 2026-10-04에 v0.1의 "기록"으로 [docs/task-log.md](docs/task-log.md)를, 첫 장치로 브랜치 가드 훅(`plugins/plate/hooks/branch-guard.sh`, 테스트는 `tests/test-branch-guard.sh`)을 만들어 플러그인 `plate` 0.1.0에 넣었다. 이 레포에 프로젝트 범위로 설치했다(`.claude/settings.json`). 다른 프로젝트에는 설치하지 않았다. 2026-10-06에 프로젝트 문서 세트(PRD·ARCHITECTURE·ADR)를 처음 만드는 스킬 `/plate:init`(`plugins/plate/skills/init/SKILL.md`)을 더해 `plate`를 0.2.0으로 올렸다. 같은 날 `main`에 합치고 업데이트 명령([1축](docs/axes/1-structure.md) 1번)으로 이 레포의 설치본에 반영했다. 2026-10-06에 작업 헌법(`plugins/plate/AGENTS.md`)과 이를 세션마다 싣는 SessionStart 훅(`plugins/plate/hooks/constitution.sh`, 테스트는 `tests/test-constitution.sh`)을 더해 `plate`를 0.3.0으로 올렸다. 헌법은 뼈대만 있고 규칙은 아직 없다. 그 밖의 구현은 없다. `ADVISE.md`는 2026-10-04에 문서를 나눌 때 폴더에 없었다(아래 링크는 깨져 있다. 검토 결과는 부록 H와 결정 기록에 남아 있다).

## 재료

| 기호 | 출처 | 비고 |
|---|---|---|
| **J** | https://github.com/jha0313/harness_framework (HEAD `da676bc`) | 복사형 템플릿. CLAUDE.md, `docs/`(PRD·ARCH·ADR·UI_GUIDE), `/harness`·`/review` 명령, `phases/*/step{N}.md`, `scripts/execute.py`. README·버전·CHANGELOG는 없다 |
| **J+** | https://github.com/jha0313/agentic-workflow-playbook | 같은 저자의 오케스트레이션 설계 원칙 7개(부록 E) |
| **R** | https://github.com/revfactory/harness v2.1.0 (HEAD `92d9f1b`) | 플러그인 겸 마켓플레이스. 메타 스킬 `harness`와 `harness:evolve`. 이 Mac에는 `~/.claude/plugins/marketplaces/harness-marketplace/`에 있다 |
| **R 사례** | `~/Desktop/meta-harness` | R로 생성한 웹툰 하네스 |
| **M1** | `~/Desktop/vibe2/excel-viewer/plugins/sheetview-kit/` (v1.1.0) | 내 플러그인. 훅 9개, `.cycle-state`, 읽기 전용 에이전트, `test-hooks.sh` |
| **M2** | `~/Desktop/vibe2/excel-viewer/.claude/rules/harness.md` | 설계 원칙 5개, 사이클 기계, 래칫, 리뷰어 속도 A/B 측정 |
| **M3** | `~/.claude/plans/wise-wibbling-waterfall.md` | J식 템플릿(`~/Desktop/클로드.md 예제/harness_project`)을 실제로 돌려 보고 진단한 문서(P0/P1/P2). 그 프로젝트 폴더는 2026-10-04 현재 없다 |
| **M4** | `~/.claude/scripts/session-report.py` | 세션 트랜스크립트에서 시간 분포, 훅 타이밍, 토큰 합계(메인과 서브에이전트 따로)를 뽑는다. `--all`은 모든 프로젝트를 훑어 캐시 읽기가 큰 세션을 보여 준다. 금액은 계산하지 않는다 |
| **ADV** | [ADVISE.md](./ADVISE.md) (2026-10-04) | 토큰과 작업 시간 관점의 설계 검토. 우선 검토할 7가지와 권장 기본값 |

## 문서 지도

이 파일은 매 세션에 읽는다. 나머지는 "읽을 때"에 해당할 때만 읽는다. 원문을 그대로 옮겼고 내용은 줄이지 않았다.

| 파일 | 내용 | 읽을 때 |
|---|---|---|
| [plugins/plate/AGENTS.md](plugins/plate/AGENTS.md) | 작업 헌법. plate를 설치한 프로젝트에서 에이전트가 예외 없이 지키는 규칙. SessionStart 훅이 세션마다 싣는다 | 절대 규칙을 더하거나 고칠 때(사용자가 확인한 것만) |
| [docs/rules.md](docs/rules.md) | 구현 규칙. 기본 흐름과 확장 조건 표, 내장 기능 우선, v0.1에서 기본으로 켜지 않는 것, 진행 방식(순서, 측정, 축 검토, 확인 기준) | 장치를 만들거나 고치기 전에 항상 |
| [docs/axes/1-structure.md](docs/axes/1-structure.md) | 1축 구조 설계. 배포 형태, 공통부와 고유부의 경계, 폴더 규약, 도구 경계를 거는 층, 프로젝트 옵트인, 플러그인·훅 함정 | 폴더, 권한, 훅, 플러그인을 다룰 때 |
| [docs/axes/2-context.md](docs/axes/2-context.md) | 2축 맥락 설계. 전역·프로젝트 `CLAUDE.md`, `docs/` 주입 여부, 컨텍스트 예산, 메모리와 규칙 문서, `paths`·summary 함정 | `CLAUDE.md`, 규칙, 스킬, 메모리를 다룰 때 |
| [docs/axes/3-planning.md](docs/axes/3-planning.md) | 3축 계획하기. 계획 산출물 형식, AC 형식, 승인 지점과 계획 밖 결정의 기록, 실행·검증 방식 명시 | 계획, 스펙, step 파일을 다룰 때 |
| [docs/axes/4-execution.md](docs/axes/4-execution.md) | 4축 실행하기. 모드 선택 기준, 모델 티어, 재시도 상한, 격리 수단, 커밋 주체, Ralph Loop | 서브에이전트, 위임, 무인 실행, 커밋을 다룰 때 |
| [docs/axes/5-verification.md](docs/axes/5-verification.md) | 5축 검증하기. 검증 층위, 완료 판정 주체, 교차검증 조합, verdict 형식, 게이트 강도 | 검사, 리뷰어, Stop 게이트를 다룰 때 |
| [docs/axes/6-improvement.md](docs/axes/6-improvement.md) | 6축 개선. 교훈 반영 경로, 제거 기준, 측정 수단(M4), 버전 정책, v0.1 범위 | 장치를 더하거나 뺄 때, 측정하거나 회고할 때 |
| [docs/decisions.md](docs/decisions.md) | 결정 기록. 사용자에게 확인받은 결정 10건과 근거, 날짜 | 결정을 확정했을 때(행을 더한다), 결정의 근거를 볼 때 |
| [docs/task-log.md](docs/task-log.md) | 작업 기록. 작업당 한 줄(세션 ID, 개입 횟수, 뒤에 발견한 결함, 켠 장치)과 적는 법 | 작업을 끝냈을 때(행을 더한다), 장치의 유지 여부를 판단할 때 |
| [docs/references.md](docs/references.md) | 부록 A–G. 레퍼런스 원문 발췌와, 기본으로 채택하지 않은 항목 표 | 레퍼런스를 근거로 선택지를 낼 때 |
| [docs/research-2026-10-04.md](docs/research-2026-10-04.md) | 부록 H. 공식 자료 확인, 내 자산 확인, 세션 기록 집계, ADVISE.md와 달라진 점 | 비용·토큰 근거가 필요할 때 |

축별 "결정과 처리" 표의 표시는 이렇다. **기본값**은 [docs/rules.md](docs/rules.md)의 원칙에서 따라 나온 것이다. **결정**은 사용자에게 확인받아 [결정 기록](docs/decisions.md)에 올린 것이다. **보류**는 적어 둔 조건이 생기면 연다. **남음**은 비용과 무관하게 아직 열려 있다.

**문서를 고칠 때**: 결정을 확정하거나 바꾸면 해당 축 문서의 표와 `docs/decisions.md`를 함께 고친다. 진행 상태(다음 할 일, 현재 상태)는 이 파일에만 적는다.
