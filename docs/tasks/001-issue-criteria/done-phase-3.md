# Phase 3: ADR-026, 맥락 문서, BACKLOG를 맞춘다

**목표**: ADR-026이 결정을 적고, PRD와 ARCHITECTURE가 세 기준과 "eval에만"을 적고, BACKLOG의 하네스 고칠 거리가 비어 있다.

**테스트 먼저**: 아니오 — `.md`만 고친다

**읽을 것**
- `docs/ADR.md` (ADR-020의 "ADR-025로 바뀜" 꼴, ADR-025의 결정·이유·트레이드오프)
- `docs/PRD.md` (핵심 기능 8번)
- `docs/ARCHITECTURE.md` (디렉터리 구조의 `test_skill_rules.py` 주석, 데이터 흐름의 tasks 끝 "승인받은 대로 …" 줄)
- `docs/BACKLOG.md` (하네스 고칠 거리 절의 세 항목)

**TODO**
- [x] ADR-025 뒤에 ADR-026이 더해진다. 결정: eval은 하네스 고칠 거리마다(두 갈래 모두) 세 기준(task 머리 결정의 피해, 일반성, 고침의 꼴. 일반성은 plate 자체의 것에만)을 감수와 ADR-025의 문턱보다 먼저 대고, 하나라도 넘지 않으면 "eval에만"으로 `eval.md`에만 남기며 run은 그것을 고침 task, 이슈, BACKLOG, 감수 어디에도 두지 않는다. 코드 평가의 소스 문제에는 걸지 않는다. 이유: 이슈를 고칠 때마다 좁은 규칙이 늘고 그 규칙에서 다시 고칠 거리가 났다. 2026-10-29의 열린 이슈 7개 가운데 4개(#70, #72, #73, #76)는 등급만 낮췄거나 이 저장소에서만 쓰는 장면에서 났다. 트레이드오프: "eval에만"인 것은 BACKLOG에 없어 다시 나도 문턱 (2)로 세지 않고, 기준은 eval의 판단이라 ADR-025의 문턱처럼 기계적으로 가르지 않는다 (`docs/ADR.md`)
- [x] ADR-025의 결정 끝에 ADR-020의 꼴대로 `(ADR-026으로 더함: …)`가 더해진다 (`docs/ADR.md`)
- [x] PRD 핵심 기능 8번의 이슈와 BACKLOG를 적은 글에 세 기준을 넘지 않은 것은 "eval에만"으로 eval.md에만 남는다는 것과 `(ADR-026)`이 더해진다 (`docs/PRD.md`)
- [x] ARCHITECTURE 데이터 흐름의 tasks 끝 "승인받은 대로 …" 줄에 같은 것과 `(ADR-026)`이 더해지고, 디렉터리 구조의 `test_skill_rules.py` 주석에 "eval에만"이 더해진다 (`docs/ARCHITECTURE.md`)
- [x] 하네스 고칠 거리 절의 세 항목이 지워지고 세 절 머리는 남는다 (`docs/BACKLOG.md`)

**통과 조건**
- 완료 조건 3이 참이다.
  - 확인: `grep -n -e '^### ADR-026' -e 'ADR-026' docs/ADR.md docs/PRD.md docs/ARCHITECTURE.md`가 ADR-026 머리, ADR-025 결정 줄, PRD 8번 줄, ARCHITECTURE의 tasks 끝 줄을 낸다
  - 확인: `grep -n -e 'eval에만' docs/PRD.md docs/ARCHITECTURE.md`가 PRD 8번 줄, ARCHITECTURE의 tasks 끝 줄과 `test_skill_rules.py` 주석 줄을 낸다
- 완료 조건 4가 참이다.
  - 확인: `awk '/^## 하네스 고칠 거리/{p=1;next} /^## /{p=0} p && /^- /' docs/BACKLOG.md | wc -l`가 `0`이고 `grep -c -e '^## ' docs/BACKLOG.md`가 `3`이다
- 테스트가 모두 통과한다(완료 조건 6).
  - 확인: `python3 -m unittest discover -s tests`가 OK다

## 한 일
- ADR-025 뒤에 ADR-026이 더해진다: 결정(세 기준을 두 갈래 모두에 감수와 문턱보다 먼저 대고, 일반성은 plate 자체에만, 넘지 않으면 "eval에만"으로 `eval.md`에만, run은 어디에도 두지 않음, 소스 문제에는 걸지 않음), 이유(좁은 규칙이 늘고 열린 이슈 7개 중 4개 #70, #72, #73, #76), 트레이드오프(문턱 (2)로 세지 않음, 기계적으로 가르지 않음)를 적은 ADR-026을 더함 (`docs/ADR.md`)
- ADR-025의 결정 끝에 `(ADR-026으로 더함: …)`가 더해진다: 결정 줄 끝에 더함 (`docs/ADR.md`)
- PRD 핵심 기능 8번에 "eval에만"과 `(ADR-026)`이 더해진다: BACKLOG를 적은 문장 뒤에 한 문장을 더함 (`docs/PRD.md`)
- ARCHITECTURE 데이터 흐름 tasks 끝 줄과 `test_skill_rules.py` 주석: 줄 끝에 괄호로 "eval에만"과 ADR-026을, 주석 끝 목록에 "eval에만" 항목을 더함 (`docs/ARCHITECTURE.md`)
- 하네스 고칠 거리 절의 세 항목이 지워진다: 세 항목을 지우고 세 절 머리를 남김 (`docs/BACKLOG.md`)

## 확인 결과
- 완료 조건 3이 참이다.
  - `grep -n -e '^### ADR-026' -e 'ADR-026' docs/ADR.md docs/PRD.md docs/ARCHITECTURE.md` → `docs/ADR.md:54`(ADR-025 결정 줄), `docs/ADR.md:58`(ADR-026 머리), `docs/PRD.md:18`(8번 줄), `docs/ARCHITECTURE.md:76`(tasks 끝 줄). 통과
  - `grep -n -e 'eval에만' docs/PRD.md docs/ARCHITECTURE.md` → `docs/PRD.md:18`, `docs/ARCHITECTURE.md:39`(`test_skill_rules.py` 주석), `docs/ARCHITECTURE.md:76`. 통과
- 완료 조건 4가 참이다.
  - `awk '/^## 하네스 고칠 거리/{p=1;next} /^## /{p=0} p && /^- /' docs/BACKLOG.md | wc -l` → `0`, `grep -c -e '^## ' docs/BACKLOG.md` → `3`. 통과
- 테스트가 모두 통과한다(완료 조건 6).
  - `python3 -m unittest discover -s tests` → `Ran 205 tests` … `OK`. 통과

## 계획과 달라진 점
없음

## 남은 것
없음

## 하네스에서 걸린 것
없음

## 확인 1

**통과 조건**
- 완료 조건 3이 참이다.
  - `grep -n -e '^### ADR-026' -e 'ADR-026' docs/ADR.md docs/PRD.md docs/ARCHITECTURE.md` → `docs/ADR.md:54`(ADR-025 결정 줄, `(ADR-026으로 더함: …)`), `docs/ADR.md:58`(`### ADR-026` 머리), `docs/PRD.md:18`(핵심 기능 8번 줄), `docs/ARCHITECTURE.md:76`(데이터 흐름의 tasks 끝 "승인받은 대로 …" 줄). 통과
  - `grep -n -e 'eval에만' docs/PRD.md docs/ARCHITECTURE.md` → `docs/PRD.md:18`(8번 줄), `docs/ARCHITECTURE.md:39`(`test_skill_rules.py` 주석 줄), `docs/ARCHITECTURE.md:76`(tasks 끝 줄). 통과
- 완료 조건 4가 참이다.
  - `awk '/^## 하네스 고칠 거리/{p=1;next} /^## /{p=0} p && /^- /' docs/BACKLOG.md | wc -l` → `0`, `grep -c -e '^## ' docs/BACKLOG.md` → `3`(소스 문제, 하네스 고칠 거리, 감수한 것). 통과
- 테스트가 모두 통과한다(완료 조건 6).
  - `python3 -m unittest discover -s tests` → `Ran 205 tests` … `OK`. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 205 tests`, `OK`. 통과

**남은 것**
- 없음

**실패**
- 없음

**하네스에서 걸린 것**
- 없음

**판정**: 통과
