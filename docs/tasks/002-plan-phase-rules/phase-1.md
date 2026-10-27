# Phase 1: plan과 phase 본문과 문서를 고친다

**목표**: plan과 phase 본문에 세 이슈의 해결이 들어가고 맥락 문서와 README가 맞춰진다.

**테스트 먼저**: 아니오 — `.md`(스킬 본문과 문서)만 고친다

**읽을 것**
- `plugins/plate/skills/plan/SKILL.md`, `plugins/plate/skills/phase/SKILL.md` (고칠 본문)
- `gh issue view 37 --repo werwer748/harness-plate`, 41, 42 (이슈마다의 원인과 해결책)
- `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `docs/BACKLOG.md`, `README.md` (맥락 문서와 README)

**TODO**
- [x] plan 적는 규칙의 "조건" 절에 완료 조건이 갈래를 가지면 갈래마다 돌리는 확인을 두고, 요약 줄을 보는 확인에는 견줄 갈래를 적고, git 원격이 있는 장면은 `git clone --bare`로 푸시 없이 채운다는 글이 더해지고, "6. 초안을 보여 주고 승인받는다"의 점검 목록에 같은 점검이 더해진다 (#37) (`plugins/plate/skills/plan/SKILL.md`)
- [x] plan 적는 규칙의 "TODO" 절(또는 "결정" 절)에 뒤 phase의 실행 조건(허용 목록, 차례)이 앞 phase의 산출물에 기대면 그 phase의 TODO 첫 항목에 "앞 phase의 산출물에 대어 조건을 맞춘다"를 두거나 결정에 "앞 phase의 결과로 정한다"고 적는다는 글이 더해지고, 6번의 점검 목록에 같은 점검이 더해진다 (#41) (`plugins/plate/skills/plan/SKILL.md`)
- [x] phase 본문의 "1. 읽는다"에 앞 phase의 결과가 필요하면 계획의 읽을 것에 적힌 산출물 파일만 읽고, 그 밖의 앞 phase 기록이 필요하면 읽지 않고 "하네스에서 걸린 것"에 적는다는 글이 더해진다 (#42) (`plugins/plate/skills/phase/SKILL.md`)
- [x] 두 본문 앞머리의 description, `docs/PRD.md`의 핵심 기능 3·4, `docs/ARCHITECTURE.md`의 "데이터 흐름"의 계획과 실행 갈래, `README.md`의 `plan`·`phase` 행 가운데 세 동작과 어긋나는 줄이 그 동작을 담게 바뀐다 (`plugins/plate/skills/plan/SKILL.md`, `plugins/plate/skills/phase/SKILL.md`, `docs/PRD.md`, `docs/ARCHITECTURE.md`, `README.md`)

**통과 조건**
- 완료 조건 1의 본문이 적혀 있다.
  - 확인: plan 본문의 "6. 초안을 보여 주고 승인받는다"와 적는 규칙의 "조건", "TODO" 절, phase 본문의 "1. 읽는다" 절을 읽어 세 해결이 저마다 적혀 있다. 하나라도 없으면 실패
  - 확인: `python3 -m unittest discover -s tests`의 마지막 줄이 `OK`, `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
- 완료 조건 2가 참이다.
  - 확인: `docs/PRD.md`의 핵심 기능 3·4, `docs/ARCHITECTURE.md`의 "데이터 흐름"의 계획과 실행 갈래, `README.md`의 `plan`·`phase` 행, 두 본문 앞머리의 description을 저마다 읽어 세 동작과 어긋나는 줄이 없다

## 한 일
- plan "조건" 절과 6번 점검에 #37의 글: "조건" 절에 세 항목(갈래마다 돌리는 확인을 둔다, 요약 줄을 보는 확인에는 담아야 할 갈래를 견줄 것으로 적는다, git 원격이 있어야 하는 장면은 `git clone --bare`로 채우고 푸시로 채우지 않는다)을 더하고, 6번의 점검 목록에 같은 세 가지를 보는 항목을 더했다 (`plugins/plate/skills/plan/SKILL.md`)
- plan "TODO" 절과 6번 점검에 #41의 글: "TODO" 절에 뒤 phase의 실행 조건(허용 목록, 차례)이 앞 phase 산출물의 동작에 기대면 짐작해 정하지 않고 TODO 첫 항목에 "앞 phase의 산출물에 대어 조건을 맞춘다"를 두거나 결정에 "앞 phase의 결과로 정한다"고 적는다는 항목을 더하고, 6번에 그것을 보는 점검 항목을 더했다 (`plugins/plate/skills/plan/SKILL.md`)
- phase "1. 읽는다"에 #42의 글: 앞 phase의 결과가 필요하면 읽을 것에 적힌 산출물 파일만 읽고, 그 밖의 앞 phase 기록(`done-phase-N.md`, 다른 `phase-N.md`의 기록·확인 절)이 필요하면 읽지 않고 "하네스에서 걸린 것"에 적는다는 항목을 더했다 (`plugins/plate/skills/phase/SKILL.md`)
- description과 맥락 문서·README: phase description의 "`phase-N.md`만 읽고"가 읽을 것의 산출물 파일을 읽는 것과 엇갈려 보여 "(앞 phase의 결과는 계획의 읽을 것에 적힌 산출물 파일로만 보고, 앞 phase의 기록은 읽지 않는다)"를 더했다 (`plugins/plate/skills/phase/SKILL.md`). plan description, `docs/PRD.md` 핵심 기능 3·4, `docs/ARCHITECTURE.md` "데이터 흐름"의 계획·실행 갈래, `README.md`의 `plan`·`phase` 행은 읽어 보니 세 동작과 어긋나는 줄이 없어 고치지 않았다

## 확인 결과
- 완료 조건 1의 본문이 적혀 있다.
  - plan 본문 "6. 초안을 보여 주고 승인받는다"(갈래·요약 줄·`git clone --bare` 점검 항목, 앞 phase 산출물 점검 항목), 적는 규칙 "조건"(세 항목), "TODO"(#41 항목), phase 본문 "1. 읽는다"(#42 항목)를 `git diff`로 읽음 → 세 해결이 저마다 있다. 통과
  - `python3 -m unittest discover -s tests` → `Ran 129 tests in 16.098s` / `OK`. `claude plugin validate .` → `✔ Validation passed`. 통과
- 완료 조건 2가 참이다.
  - `docs/PRD.md` 핵심 기능 3·4, `docs/ARCHITECTURE.md` "데이터 흐름"의 계획·실행 갈래, `README.md`의 `plan`·`phase` 행, 두 본문의 description을 읽음 → 갈래마다의 확인, 앞 phase 산출물에 기대는 조건, phase가 앞 phase 기록을 읽지 않는 것과 어긋나는 줄 없음(phase description은 위처럼 고친 뒤). 통과

## 계획과 달라진 점
- 없음

## 남은 것
- `docs/PRD.md`, `docs/ARCHITECTURE.md`, `README.md`는 어긋나는 줄이 없어 바꾸지 않았다. 세 동작을 요약에 새로 적지는 않았으므로, 확인하는 쪽이 "담지 않음"을 어긋남으로 읽으면 다르게 판정할 수 있다
- 고친 동작은 아직 돌려 보지 않았다(장면 E~G는 phase 2·3의 일)

## 하네스에서 걸린 것
- 없음

## 확인 1

**통과 조건**
- 완료 조건 1의 본문이 적혀 있다.
  - plan 본문 "6. 초안을 보여 주고 승인받는다", 적는 규칙 "조건", "TODO" 절, phase 본문 "1. 읽는다"를 읽음 → #37: "조건" 절에 갈래마다 돌리는 확인, 요약 줄 확인에 견줄 갈래, `git clone --bare`로 푸시 없이 채운다는 세 항목이 있고 6번에 같은 점검 항목이 있다. #41: "TODO" 절에 TODO 첫 항목 "앞 phase의 산출물에 대어 조건을 맞춘다" 또는 결정의 "앞 phase의 결과로 정한다" 항목이 있고 6번에 같은 점검 항목이 있다. #42: "1. 읽는다"에 읽을 것의 산출물 파일만 읽고 그 밖의 앞 phase 기록은 읽지 않고 "하네스에서 걸린 것"에 적는다는 항목이 있다. 통과
  - `python3 -m unittest discover -s tests` → `Ran 129 tests in 16.200s` / `OK`. `claude plugin validate .` → `✔ Validation passed`. 통과
- 완료 조건 2가 참이다.
  - `docs/PRD.md` 핵심 기능 3·4, `docs/ARCHITECTURE.md` "데이터 흐름"의 계획·실행 갈래, `README.md`의 `plan`·`phase` 행, 두 본문의 description을 읽음 → 갈래마다의 확인, 앞 phase 산출물에 기대는 조건, phase가 앞 phase 기록을 읽지 않는 것과 어긋나는 줄이 없다(phase description은 앞 phase의 기록을 읽지 않는다고 적는다). 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 129 tests` / `OK`. 통과

**남은 것**
- 고친 동작은 아직 돌려 보지 않았다(장면 E~G는 phase 2·3의 일) → 돌려 보지 않은 위험이나, 이 phase의 통과 조건은 본문과 문서의 글만 보고 동작을 돌리지 않는다. 돌리는 확인은 task 완료 조건 3과 phase 2·3의 몫이다. 하네스에서 걸린 것

**실패**
- 없음

**하네스에서 걸린 것**
- 남은 것: 고친 plan·phase 동작은 이 phase에서 돌려 보지 않았다(장면 E~G는 phase 2·3에서 돌린다)

**판정**: 통과
