# Phase 6: 이 레포의 문서를 4단계 상태로 고친다

**목표**: README, 두 매니페스트, PRD, ARCHITECTURE, TOOLS가 스킬 여섯과 `phase-N.md`로 나뉜 계획을 말한다.

**읽을 것**
- `README.md`, `plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`
- `docs/PRD.md` (핵심 기능의 3~5번과 그 아래 문장)
- `docs/ARCHITECTURE.md` (디렉터리 구조, "패턴과 규칙"의 마지막 줄, 데이터 흐름과 그 아래 두 문장)
- `docs/TOOLS.md` (첫머리, "지금 상태")
- `plugins/plate/skills/run/SKILL.md`, `phase/SKILL.md`, `retro/SKILL.md`, `plan/SKILL.md`의 설명 (표에 옮길 한 줄)

**TODO**
- [x] 스킬 표에 run, phase, retro가 있고 plan의 줄이 `plan.md`와 `phase-N.md`를 말하며, 부르는 법에 세 스킬이 있다 (`README.md`)
- [x] 두 매니페스트의 설명에 세 스킬이 있다
- [x] 핵심 기능의 계획 줄이 `plan.md`와 `phase-N.md`를 말하고 실행 줄이 4단계에서 만들었다고 말한다 (`docs/PRD.md`)
- [x] 디렉터리 구조에 세 스킬이 있고, 프로젝트의 규칙 줄이 네 스킬의 본문에 넣었다고 말하고, 데이터 흐름과 그 아래 문장이 phase 파일을 지우는 것과 `docs/LESSONS.md`를 말한다 (`docs/ARCHITECTURE.md`)
- [x] 첫머리와 "지금 상태"에 4단계가 있다 (`docs/TOOLS.md`)

**통과 조건**
- 완료 조건 19가 참이다.
  - 확인: 완료 조건 19의 확인 둘을 돌리고 읽어 기대와 같은지 본다
- 문서에 한 파일 시절의 글이 없다.
  - 확인: `grep -n 'phase 절' README.md docs/PRD.md docs/ARCHITECTURE.md` → 출력 없음

## 한 일
- 스킬 표에 run, phase, retro가 있고 plan의 줄이 `plan.md`와 `phase-N.md`를 말하며, 부르는 법에 세 스킬이 있다: 첫 줄의 스킬 수를 여섯으로, 표에 세 줄을, Claude Code와 Codex의 부르는 법에 세 이름을 더했다. Codex에서 확인하지 않은 스킬의 줄에도 셋을 넣었다 (`README.md`)
- 두 매니페스트의 설명에 세 스킬이 있다: 설명 끝의 plan 스킬 뒤에 run, phase, retro를 이었다. 버전은 4단계를 시작하며 올린 0.7.0 그대로다 (`plugins/plate/.claude-plugin/plugin.json`, `plugins/plate/.codex-plugin/plugin.json`)
- 핵심 기능의 계획 줄이 `plan.md`와 `phase-N.md`를 말하고 실행 줄이 4단계에서 만들었다고 말한다: 3번과 4번을 고치고 그 아래 문장을 5단계만 말하게 했다 (`docs/PRD.md`)
- 디렉터리 구조에 세 스킬이 있고, 프로젝트의 규칙 줄이 네 스킬의 본문에 넣었다고 말하고, 데이터 흐름과 그 아래 문장이 phase 파일을 지우는 것과 `docs/LESSONS.md`를 말한다: 구조에 세 줄을 더했고, 데이터 흐름의 계획과 실행 줄을 고쳤고, 그 아래 두 문장에서 실행을 만든 것으로 옮기고 "머리만 남은"을 뺐다 (`docs/ARCHITECTURE.md`)
- 첫머리와 "지금 상태"에 4단계가 있다 (`docs/TOOLS.md`)

## 확인 결과
- 완료 조건 19가 참이다.
  - `grep -c 'retro' README.md plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json docs/ARCHITECTURE.md` → 4, 1, 1, 2. 통과
  - `grep -n '만들기 전' docs/PRD.md docs/ARCHITECTURE.md` → 세 줄(PRD의 5번 검증, PRD의 "5단계의 세부는…", ARCHITECTURE의 "검증은 만들기 전이다")이고 모두 검증을 말한다. 통과
- 문서에 한 파일 시절의 글이 없다.
  - `grep -n 'phase 절' README.md docs/PRD.md docs/ARCHITECTURE.md` → 출력 없음. 통과

## 계획과 달라진 점
- `docs/TOOLS.md`는 TODO에 적힌 첫머리와 "지금 상태" 말고 "Claude Code" 절의 두 줄도 고쳤다. 판정을 돌린 버전의 줄에 4단계(2.1.296)를, 스킬을 부르는 이름의 줄에 세 스킬을 더했다. 그대로 두면 스킬이 셋이라고 읽힌다.

## 남은 것
- `docs/ARCHITECTURE.md`의 기술 스택 줄은 Claude Code의 버전을 3단계까지만 적고 있다. TODO와 읽을 것에 없어 고치지 않았다.

## 하네스에서 걸린 것
없음
